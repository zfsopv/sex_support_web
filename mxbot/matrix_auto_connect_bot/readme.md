# 自动建立matrix私聊房间

## 功能说明

本程序会使用管理员账户登录matrix服务器（synapse），然后使用synapse专有的API每隔5s检查一次当前用户列表。一旦检测到新增的用户，就会创建两个私聊房间：

1. 新账户与@se7-support-bot:<homeserver>的私聊房间
2. 新账户与@se9-support-bot:<homeserver>的私聊房间

注意：

1. 默认不开启E2EE加密
2. 程序启动后第一次检测到的新账户会被忽略，防止重复创建私聊房间
3. 创建私聊房间后如果管理员账户仍然在房间中，会离开房间
4. 具体需要与新账户创建私聊的账户可以自定义

## 程序语言和编译方式

程序采用rust语言，使用cargo进行编译

## 配置说明

程序通过环境变量进行配置，可以在 `.env` 文件中设置以下变量：

| 环境变量 | 说明 | 示例 | 默认值 |
|---------|------|------|--------|
| HOMESERVER | Matrix服务器地址 | `http://localhost:8008` | `http://localhost:8008` |
| ADMIN_USER | 管理员账户ID | `@admin:localhost` | `@admin:localhost` |
| ADMIN_PASSWORD | 管理员密码 | `your_password` | 无（必须设置） |
| SUPPORT_BOTS | 与新用户创建私聊的机器人列表（逗号分隔） | `se7-support-bot,se9-support-bot` | `se7-support-bot,se9-support-bot` |

**注意：**
- `SUPPORT_BOTS` 可以只提供用户名（如 `se7-support-bot`），程序会自动根据 `HOMESERVER` 的域名拼接成完整的Matrix用户ID（如 `@se7-support-bot:localhost`）
- 也可以直接提供完整的用户ID（以 `@` 开头）

**配置示例文件 `.env`：**
```bash
HOMESERVER=http://localhost:8008
ADMIN_USER=@admin:localhost
ADMIN_PASSWORD=your_admin_password_here
SUPPORT_BOTS=se7-support-bot,se9-support-bot
```

## 使用方式

### 安装依赖
确保已安装 Rust 和 Cargo：
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```

### 编译程序
```bash
cd matrix_auto_connect_bot
cargo build --release
```

### 运行程序

**方式1：使用环境变量**
```bash
export HOMESERVER="http://localhost:8008"
export ADMIN_USER="@admin:localhost"
export ADMIN_PASSWORD="your_password"
export SUPPORT_BOTS="se7-support-bot,se9-support-bot"
cargo run --release
```

**方式2：使用 .env 文件**
```bash
cp .env.example .env
# 编辑 .env 文件，填入实际配置
cargo run --release
```

### 后台运行（推荐）
使用 systemd 或其他进程管理工具保持程序持续运行。

**systemd 服务示例：**
创建 `/etc/systemd/system/matrix-auto-connect-bot.service`：
```ini
[Unit]
Description=Matrix Auto Connect Bot
After=network.target

[Service]
Type=simple
User=your_user
WorkingDirectory=/path/to/matrix_auto_connect_bot
Environment="HOMESERVER=http://localhost:8008"
Environment="ADMIN_USER=@admin:localhost"
Environment="ADMIN_PASSWORD=your_password"
Environment="SUPPORT_BOTS=se7-support-bot,se9-support-bot"
ExecStart=/path/to/cargo run --release
Restart=always

[Install]
WantedBy=multi-user.target
```

启用服务：
```bash
sudo systemctl enable matrix-auto-connect-bot
sudo systemctl start matrix-auto-connect-bot
```