---
title: 技术支持助手
description: 主页
template: doc
head:
  - tag: style
    content: |
      .content-panel:has(h1) {
        display: none !important;
      }
---

<style>
  /* 仅本页：右侧「本页目录」已隐藏，去掉为移动端 TOC 预留的顶栏高度，与主栏可视区域一致 */
  html:has(.iframe-wrapper) {
    --sl-mobile-toc-height: 0rem;
  }

  .right-sidebar-container {
    display: none !important;
  }

  .main-pane {
    width: 100% !important;
    max-width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
  }
  main {
    width: 100% !important;
    max-width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
  }
  .sl-container {
    max-width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
  }
  .sl-markdown-content {
    max-width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
  }
  .content-panel {
    padding: 0 !important;
    margin: 0 !important;
  }
  /* 第二块内容区顶部分隔线去掉，避免红框内出现横线 */
  main:has(.iframe-wrapper) .content-panel + .content-panel {
    border-top: none !important;
  }
  /* 内嵌占满主栏时不再保留 Starlight 页脚 */
  main:has(.iframe-wrapper) footer {
    display: none !important;
  }

  body {
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden !important;
  }
  html {
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden !important;
  }
</style>

<script>
  // 禁止页面滚动
  document.body.style.overflow = 'hidden';
  document.documentElement.style.overflow = 'hidden';
  window.addEventListener('wheel', e => e.preventDefault(), { passive: false });
  window.addEventListener('touchmove', e => e.preventDefault(), { passive: false });
</script>

<div class="iframe-wrapper">
  <iframe
    src="https://se-support-mx-cinny.pages.dev/"
    frameborder="0"
    allowfullscreen>
  </iframe>
</div>

<style>
  /* 占满侧栏右侧、顶栏下方的内容区（与 Starlight .main-frame 内可视高度一致，不覆盖左侧导航） */
  .iframe-wrapper {
    width: 100%;
    height: calc(100dvh - var(--sl-nav-height) - var(--sl-mobile-toc-height));
    min-height: calc(100dvh - var(--sl-nav-height) - var(--sl-mobile-toc-height));
    margin: 0;
    box-sizing: border-box;
  }

  .iframe-wrapper iframe {
    width: 100%;
    height: 100%;
    border: none;
    display: block;
  }
</style>
