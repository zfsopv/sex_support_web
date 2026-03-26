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
