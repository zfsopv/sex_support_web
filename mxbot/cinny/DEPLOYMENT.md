# Cloudflare Pages / Wrangler 部署指南

本项目已配置支持通过 Cloudflare Wrangler 进行部署。

## 前置要求

1. 安装 Node.js (>=16.0.0)
2. 安装 Wrangler CLI:
   ```bash
   npm install -g wrangler
   ```

## 认证

登录 Cloudflare 账号:

```bash
wrangler login
```

## 部署命令

### 生产环境部署

```bash
npm run deploy
```

此命令会:

1. 构建项目到 `dist/` 目录
2. 部署到 Cloudflare Pages

### 预览部署

```bash
npm run deploy:preview
```

部署到预览环境，用于测试。

### 本地开发

```bash
npm run wrangler:dev
```

在本地使用 Wrangler 模拟 Cloudflare Pages 环境。

## 配置说明

`wrangler.toml` 配置文件包含:

- **pages_build_output_dir**: 构建输出目录 (dist)
- **build**: 构建命令配置
- **redirects**: 路由重定向规则
- **headers**: 安全头和缓存策略

## 环境变量

如需添加环境变量，可以在 `wrangler.toml` 中的 `[vars]` 部分添加:

```toml
[vars]
API_KEY = "your-key"
SOME_VAR = "value"
```

## 部署到自定义域名

1. 在 Cloudflare 仪表板中添加自定义域名
2. 运行部署命令:
   ```bash
   wrangler pages deploy dist --project-name=cinny
   ```

## 注意事项

- 确保在部署前运行 `npm run build` 生成最新构建
- 首次部署时，Wrangler 会询问项目名称和配置
- 生产部署建议配置自定义域名和 SSL 证书
