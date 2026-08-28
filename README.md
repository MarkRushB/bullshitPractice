# 看见 · 日常影像档案

三个每周摄影主题，68 张恢复的照片与原始总结。Hugo 构建，GitHub Pages 发布。

## 本地预览

使用 Hugo 0.113.0：

```sh
hugo server --destination _site
```

首页仅列出三篇每周总结，不再提供独立摄影展示、照片墙或筛选页面；`posts/week1/`、`posts/week2/`、`posts/week3/` 保留原文章地址、文字和正文照片。

## 照片

- `static/photos/original/`：68 张恢复的原始文件。
- `static/photos/display/`：最长边 1600px 的 WebP 展示图。
- `static/photos/thumb/`：最长边 640px 的照片墙缩略图。
- `data/photos.json`：照片墙顺序、周次和图片路径。

第一周「在定格时间」的旧图床缩略图尚未找到，以文字说明保留，不用其他照片替代。第二周原文写 18 张照片，但归档正文实际包含 19 个图片，均保留。

总结正文中的照片可点击放大，方向键切换，Esc 关闭。查看原图链接可打开仓库内的原始文件。页面不连接旧评论服务或旧图床。恢复的原图与缩略图文件仍保留，不删除图片备份。

GitHub Actions 在 PR 中构建检查，在合并到 `main` 后发布。构建输出为 `_site/`，不会混入仓库里历史遗留的 `public/` 文件。

