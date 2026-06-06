# 📝 AI CMS

AI内容管理系统工具，支持内容建模、编辑器、发布流程。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🏗️ CMS系统设计
- 📋 内容模型生成
- 📝 富文本编辑器
- 📁 媒体库生成
- 🔄 发布工作流
- 🔍 SEO工具

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_cms import create_tools

tools = create_tools()

# CMS设计
cms = tools.design_cms(["文章", "产品"], ["富文本", "媒体库"])

# 内容模型
model = tools.generate_content_model("文章", fields)

# 富文本编辑器
editor = tools.generate_rich_editor(["工具栏", "Markdown"], "react")

# 媒体库
media = tools.generate_media_library(["上传", "预览", "分类"])

# 发布工作流
workflow = tools.generate_publish_workflow(["编辑", "审核", "发布"])

# SEO工具
seo = tools.generate_seo_tools("文章")
```

## 📁 项目结构

```
ai-cms/
├── tools.py       # CMS工具核心
└── README.md
```

## 📄 许可证

MIT License
