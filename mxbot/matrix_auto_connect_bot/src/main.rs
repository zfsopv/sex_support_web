use anyhow::{Context, Result};
use matrix_sdk::ruma::OwnedUserId;
use matrix_sdk::Client;
use reqwest::{header, StatusCode};
use serde::Deserialize;
use std::{collections::HashSet, env, sync::Arc, time::Duration};
use tokio::sync::Mutex;
use tracing::{error, info};

#[derive(Debug, Deserialize)]
struct UserInfo {
    #[serde(rename = "name")]
    user_id: String,
    #[serde(default)]
    #[allow(dead_code)]
    user_type: Option<String>,
    #[serde(default)]
    is_guest: bool,
    #[allow(dead_code)]
    admin: bool,
    deactivated: bool,
}

#[derive(Debug, Deserialize)]
struct UsersResponse {
    users: Vec<UserInfo>,
    #[allow(dead_code)]
    next_token: Option<String>,
    #[allow(dead_code)]
    total: u32,
}

struct AppState {
    client: Client,
    homeserver_url: String,
    admin_token: String,
    #[allow(dead_code)]
    homeserver_domain: String,
    support_bots: Vec<OwnedUserId>,
    known_users: Arc<Mutex<HashSet<OwnedUserId>>>,
    first_run_completed: Arc<Mutex<bool>>,
}

async fn get_user_list(state: &AppState) -> Result<HashSet<OwnedUserId>> {
    let url = format!("{}/_synapse/admin/v2/users", state.homeserver_url);

    let mut headers = header::HeaderMap::new();
    headers.insert(
        header::AUTHORIZATION,
        header::HeaderValue::from_str(&format!("Bearer {}", state.admin_token))?,
    );

    let http_client = reqwest::Client::new();
    let response = http_client.get(&url).headers(headers).send().await?;

    if response.status() == StatusCode::OK {
        let users_response: UsersResponse = response.json().await?;
        let user_ids: HashSet<OwnedUserId> = users_response
            .users
            .iter()
            .filter(|u| !u.deactivated && !u.is_guest)
            .filter_map(|u| u.user_id.parse().ok())
            .collect();

        Ok(user_ids)
    } else {
        let status = response.status();
        let error_text = response.text().await.unwrap_or_default();
        anyhow::bail!("获取用户列表失败. Status: {}, Error: {}", status, error_text);
    }
}

async fn force_join_room(state: &AppState, room_id: &str, user_id: &OwnedUserId) -> Result<()> {
    let url = format!("{}/_synapse/admin/v1/join/{}", state.homeserver_url, room_id);

    let mut headers = header::HeaderMap::new();
    headers.insert(
        header::AUTHORIZATION,
        header::HeaderValue::from_str(&format!("Bearer {}", state.admin_token))?,
    );
    headers.insert(header::CONTENT_TYPE, header::HeaderValue::from_static("application/json"));

    let http_client = reqwest::Client::new();
    let body = serde_json::json!({ "user_id": user_id.to_string() });

    let response = http_client
        .post(&url)
        .headers(headers)
        .json(&body)
        .send()
        .await?;

    if response.status().is_success() {
        info!("已强制用户 {} 加入房间 {}", user_id, room_id);
        Ok(())
    } else {
        let status = response.status();
        let error_text = response.text().await.unwrap_or_default();
        anyhow::bail!("强制加入失败. Status: {}, Error: {}", status, error_text);
    }
}

async fn create_private_room_with_bot(
    client: &Client,
    new_user_id: &OwnedUserId,
    bot_user_id: &OwnedUserId,
    state: &AppState,
) -> Result<()> {
    info!("创建私聊房间：{} 和 {}", new_user_id, bot_user_id);

    use matrix_sdk::ruma::OwnedRoomId;
    use matrix_sdk::ruma::api::client::room::create_room::v3::{Request, RoomPreset};

    let mut request = Request::new();
    request.is_direct = true;
    request.preset = Some(RoomPreset::PrivateChat);
    request.name = Some(format!("{} 与 {}", new_user_id.localpart(), bot_user_id.localpart()));

    let room = client
        .create_room(request)
        .await
        .context("创建私聊失败")?;

    let room_id: OwnedRoomId = room.room_id().to_owned();
    let room_id_str = room_id.as_str();

    info!(
        "已创建私聊房间 {}，正在拉入用户...",
        room_id
    );

    force_join_room(state, room_id_str, new_user_id).await?;
    force_join_room(state, room_id_str, bot_user_id).await?;

    info!("所有用户已拉入，正在设置权限...");

    let admin_user_id = client.user_id().ok_or_else(|| anyhow::anyhow!("未登录"))?.to_string();

    let power_levels = serde_json::json!({
        "users": {
            admin_user_id: 100,
            new_user_id.to_string(): 0,
            bot_user_id.to_string(): 0
        },
        "users_default": 0,
        "events": {
            "m.room.name": 50,
            "m.room.power_levels": 100,
            "m.room.history_visibility": 100,
            "m.room.canonical_alias": 50,
            "m.room.avatar": 50,
            "m.room.topic": 50,
            "m.room.encryption": 100
        },
        "events_default": 0,
        "state_default": 50,
        "ban": 50,
        "kick": 50,
        "redact": 50,
        "invite": 50,
        "notifications": {
            "room": 50
        }
    });

    let url = format!("{}/_matrix/client/v3/rooms/{}/state/m.room.power_levels", state.homeserver_url, room_id_str);

    let mut headers = header::HeaderMap::new();
    headers.insert(
        header::AUTHORIZATION,
        header::HeaderValue::from_str(&format!("Bearer {}", state.admin_token))?,
    );
    headers.insert(header::CONTENT_TYPE, header::HeaderValue::from_static("application/json"));

    let http_client = reqwest::Client::new();
    let response = http_client
        .put(&url)
        .headers(headers)
        .json(&power_levels)
        .send()
        .await?;

    if response.status().is_success() {
        info!("已设置房间 {} 的权限，禁止E2EE", room_id);
    } else {
        let status = response.status();
        let error_text = response.text().await.unwrap_or_default();
        error!("设置房间权限失败 {}: Status: {}, Error: {}", room_id, status, error_text);
    }

    tokio::time::sleep(Duration::from_millis(500)).await;

    if let Err(e) = room.leave().await {
        error!("管理员离开房间失败 {}: {}", room_id, e);
    } else {
        info!("管理员已离开房间 {}", room_id);
    }

    info!(
        "私聊房间 {} 创建完成，参与者：{} 和 {}",
        room_id,
        new_user_id,
        bot_user_id
    );

    Ok(())
}

async fn process_new_users(state: &AppState) -> Result<()> {
    let mut known_users = state.known_users.lock().await;
    let mut first_run_completed = state.first_run_completed.lock().await;

    let all_users = get_user_list(state).await
        .context("获取用户列表失败")?;

    info!("检查新用户... 当前用户数: {}", all_users.len());

    let new_users: Vec<OwnedUserId> = all_users
        .difference(&known_users)
        .filter(|user_id: &&OwnedUserId| {
            let localpart = user_id.localpart();
            !localpart.contains("admin") && !localpart.contains("bot") && !localpart.contains("support")
        })
        .cloned()
        .collect();

    if !new_users.is_empty() {
        if !*first_run_completed {
            info!("首次运行，发现 {} 个现有用户", new_users.len());
            for user_id in &new_users {
                info!("现有用户: {}", user_id);
            }
            *known_users = all_users;
            *first_run_completed = true;
            return Ok(());
        }

        info!("发现 {} 个新用户", new_users.len());
        for user_id in &new_users {
            info!("新用户: {}", user_id);
        }

        for new_user_id in &new_users {
            for bot_user_id in &state.support_bots {
                match create_private_room_with_bot(&state.client, new_user_id, bot_user_id, &state).await {
                    Ok(_) => info!("已创建与 {} 的私聊房间，针对用户 {}", bot_user_id, new_user_id),
                    Err(e) => error!(
                        "创建与 {} 的私聊房间失败，针对用户 {}: {}",
                        bot_user_id, new_user_id, e
                    ),
                }
            }
        }
    }

    *known_users = all_users;
    *first_run_completed = true;

    Ok(())
}

async fn run(state: AppState) -> Result<()> {
    info!("Matrix 自动连接机器人启动中...");

    loop {
        match process_new_users(&state).await {
            Ok(_) => {}
            Err(e) => {
                error!("处理新用户时出错: {}", e);
            }
        }

        tokio::time::sleep(Duration::from_secs(5)).await;
    }
}

fn extract_homeserver(homeserver_url: &str) -> Result<String> {
    let url = url::Url::parse(homeserver_url)?;
    let host = url.host_str().context("Failed to extract host from homeserver URL")?;
    Ok(host.to_string())
}

#[tokio::main]
async fn main() -> Result<()> {
    dotenv::dotenv().ok();

    let filter = tracing_subscriber::EnvFilter::try_from_default_env()
        .unwrap_or_else(|_| {
            tracing_subscriber::EnvFilter::new("warn,matrix_sdk_base=error,matrix_auto_connect_bot=info")
        });

    tracing_subscriber::fmt()
        .with_env_filter(filter)
        .init();

    let homeserver =
        env::var("HOMESERVER").unwrap_or_else(|_| "http://localhost:8008".to_string());
    let homeserver_domain = extract_homeserver(&homeserver)?;

    let admin_user_env =
        env::var("ADMIN_USER").unwrap_or_else(|_| "admin".to_string());
    let admin_user_str = if admin_user_env.starts_with('@') {
        admin_user_env
    } else {
        format!("@{}:{}", admin_user_env, homeserver_domain)
    };
    let admin_user_id: OwnedUserId = admin_user_str.parse().context("Invalid admin user ID")?;
    let admin_password =
        env::var("ADMIN_PASSWORD").expect("ADMIN_PASSWORD environment variable must be set");

    let support_bots_env = env::var("SUPPORT_BOTS").unwrap_or_else(|_| {
        "se7-support-bot,se9-support-bot".to_string()
    });
    let support_bots: Vec<OwnedUserId> = support_bots_env
        .split(',')
        .map(|s| s.trim().to_string())
        .filter(|s| !s.is_empty())
        .map(|username| {
            if username.starts_with('@') {
                Ok::<_, matrix_sdk::ruma::IdParseError>(username.parse()?)
            } else {
                Ok::<_, matrix_sdk::ruma::IdParseError>(format!("@{}:{}", username, homeserver_domain).parse()?)
            }
        })
        .collect::<Result<Vec<_>, _>>()
        .context("Failed to parse support bot user IDs")?;

    if support_bots.is_empty() {
        anyhow::bail!("SUPPORT_BOTS must be configured with at least one bot user ID");
    }

    info!("配置的支持机器人: {:?}", support_bots);

    let client = Client::builder()
        .homeserver_url(&homeserver)
        .build()
        .await?;

    info!("正在以管理员身份登录: {}", admin_user_id);
    let login_response = client
        .matrix_auth()
        .login_username(&admin_user_str, &admin_password)
        .initial_device_display_name("matrix-auto-connect-bot")
        .send()
        .await?;

    let admin_token = login_response.access_token;

    info!("管理员登录成功");
    info!("已连接到服务器: {}", homeserver);

    let state = AppState {
        client,
        homeserver_url: homeserver,
        admin_token,
        homeserver_domain,
        support_bots,
        known_users: Arc::new(Mutex::new(HashSet::new())),
        first_run_completed: Arc::new(Mutex::new(false)),
    };

    run(state).await?;

    Ok(())
}