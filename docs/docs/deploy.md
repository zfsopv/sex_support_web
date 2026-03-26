---
title: 部署到 Cloudflare Pages
description: 如何将项目部署到 Cloudflare Pages
template: doc
---

本文档说明如何将本项目部署到 Cloudflare Pages。

## 前置要求

1. Cloudflare 账号
2. Node.js 环境
3. wrangler CLI 工具

## 安装 wrangler

```bash
pnpm install -g wrangler
```

## 登录 Cloudflare

```bash
wrangler login
```

执行后会打开浏览器，登录并授权。

## 部署步骤

### 1. 构建项目

```bash
pnpm run build
```

### 2. 部署到 Cloudflare Pages

```bash
pnpm run deploy
```
