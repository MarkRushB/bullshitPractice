# 看见 · 日常影像档案

三个每周摄影主题，68 张恢复的照片与原始总结。Hugo 构建，GitHub Pages 发布。

## 本地预览

使用 Hugo 0.113.0：

```sh
hugo server --destination _site
```

首页为摄影展示页；`posts/week1/`、`posts/week2/`、`posts/week3/` 保留原文章地址和文字。

## 照片

- `static/photos/original/`：68 张恢复的原始文件。
- `static/photos/display/`：最长边 1600px 的 WebP 展示图。
- `static/photos/thumb/`：最长边 640px 的照片墙缩略图。
- `data/photos.json`：照片墙顺序、周次和图片路径。

第一周「在定格时间」的旧图床缩略图尚未找到，以文字说明保留，不用其他照片替代。第二周原文写 18 张照片，但归档正文实际包含 19 个图片，均保留。

点击照片可放大，方向键切换，Esc 关闭，支持按周筛选。查看原图链接可打开仓库内的原始文件。展示页不连接旧评论服务或旧图床。

GitHub Actions 在 PR 中构建检查，在合并到 `main` 后发布。构建输出为 `_site/`，不会混入仓库里历史遗留的 `public/` 文件。

