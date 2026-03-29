# RAG 数据清洗工具

专门为 RAG（检索增强生成）向量数据库设计的文档清洗工具。

## 目录

- [概述](#概述)
- [安装](#安装)
- [快速开始](#快速开始)
- [使用方法](#使用方法)
- [配置](#配置)
- [清洗规则](#清洗规则)
- [输出示例](#输出示例)
- [常见问题](#常见问题)

## 概述

本工具用于清洗从 PDF 转换或 RST 文档生成的 markdown 文件，移除噪声和格式标记，提升向量检索性能。

### 主要特性

- 🤖 **LLM 智能清洗** - 使用大语言模型理解上下文，智能识别和移除噪声
- 📦 **批量处理** - 支持批量处理整个目录
- 🧩 **智能分块** - 自动处理大文件，重叠分块保证上下文连贯
- 📝 **纯文本输出** - 输出无标记符号的纯文本，适合 RAG 索引
- 📊 **清洗报告** - 自动生成详细的清洗统计报告

### 适用场景

- PDF 转换的 markdown 文档
- RST (reStructuredText) 文档
- 技术文档、API 文档
- 用户手册、开发指南
- 包含大量格式标记的文档

## 安装

### 系统要求

- Python 3.7+
- LLM 模式需要 OpenAI API Key 或兼容的 API

### 安装依赖

```bash
# 安装基础依赖
pip3 install requests

# 可选：如果需要 token 精确计数
pip3 install tiktoken
```

## 快速开始

### 使用 LLM 智能清洗

```bash
# 1. 配置 API
cp config.json.template config.json
# 编辑 config.json，填入你的 OpenAI API Key

# 2. 运行清洗（必须提供输入和输出目录）
python3 llm_cleaner.py /path/to/input /path/to/output
```

## 使用方法

### LLM 智能清洗

#### 基本用法

```bash
python3 llm_cleaner.py <输入目录> <输出目录>
```

#### 指定输入输出目录

```bash
python3 llm_cleaner.py /path/to/input /path/to/output
```

#### 使用环境变量配置

```bash
export OPENAI_API_KEY=your_api_key
export OPENAI_API_BASE=https://api.openai.com/v1
export OPENAI_MODEL=gpt-4

python3 llm_cleaner.py /path/to/input /path/to/output
```

#### 脚本参数调整

编辑 `llm_cleaner.py` 调整以下参数：

```python
chunk_size = 15000  # 每个分块的字符数（默认15000）
overlap = 1000      # 分块重叠字符数（默认1000）
```

## 配置

### LLM API 配置

#### 方法 1: 配置文件（推荐）

复制模板并编辑：

```bash
cp config.json.template config.json
```

编辑 `config.json`：

```json
{
  "api_key": "your_openai_api_key_here",
  "api_base": "https://api.openai.com/v1",
  "model": "gpt-4"
}
```

#### 方法 2: 环境变量

```bash
export OPENAI_API_KEY=your_api_key
export OPENAI_API_BASE=https://api.openai.com/v1
export OPENAI_MODEL=gpt-4
```

#### 支持的 API

本工具支持任何 OpenAI 兼容的 API：

- OpenAI 官方 API
- Azure OpenAI
- 通过代理访问的 OpenAI API
- 其他兼容 OpenAI 格式的 API

配置示例：

```json
{
  "api_key": "your_azure_api_key",
  "api_base": "https://your-resource.openai.azure.com/v1",
  "model": "gpt-4"
}
```

### 分块配置

根据文档大小和 API 限制调整：

```python
# 小文档（< 50K tokens）
chunk_size = 15000
overlap = 1000

# 大文档（> 100K tokens）
chunk_size = 10000
overlap = 500

# 超大文档（> 500K tokens）
chunk_size = 8000
overlap = 300
```

## 清洗规则

### LLM 模式清洗内容

LLM 会智能识别并移除以下内容：

| 类别 | 示例 |
|------|------|
| 页眉页脚 | "Page 42", "第5页", "--- 156 ---", "保存三年" |
| Markdown 标记 | `#`, `*`, `**`, `_`, `__`, `` ` ``, `>`, `-`, `+`, `*` |
| RST 指令 | `.. note::`, `.. warning::`, `.. tip::`, `.. toctree::`, `.. image::`, `.. code::` |
| 引用标记 | `[1]`, `[2]`, `[15]`, `Footnote 1`, `*` |
| 目录页码 | "1 声明 1", "2 SAIL 5", "3 编译安装指南 7" |
| PDF 伪影 | 多余空格、换行、分隔符、OCR 错误 |

### 保留原则

LLM 模式会保留：

- ✅ 所有实际内容和说明文字
- ✅ 文档的逻辑结构和层次关系
- ✅ 技术信息和代码示例内容
- ✅ 表格中的实际数据
- ✅ 不确定是否为噪声的内容

## 输出示例

### 输入（PDF 转换的 markdown）

```markdown
# SOPHON-SAIL_zh.pdf

## 第1页

SOPHON-SAIL 使用手册

                  发布3.9.0



                  SOPHGO



                             2024 年10 月19 日

## 第2页

目录



1 声明                                                                         1

2  SAIL                                                                        5

3 编译安装指南                                                                 7
    3.1 源码目录结构.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   7

.. note::
   这是重要的提示信息。

保存三年
```

### 输出（LLM 模式 - 纯文本）

```
SOPHON-SAIL 使用手册

发布 3.9.0

SOPHGO

2024年10月19日

目录

1 声明

2 SAIL

3 编译安装指南

3.1 源码目录结构

这是重要的提示信息。
```

## 清洗报告

清洗完成后会生成 `cleaning_report.json`，包含每个文件的统计信息：

```json
[
  {
    "input_file": "/path/to/input.md",
    "output_file": "/path/to/output.txt",
    "total_chars": 50000,
    "num_chunks": 4,
    "output_chars": 45000,
    "chars_removed": 5000
  }
]
```

## 常见问题

### Q: 分块大小如何设置？

**A:**
- 建议设置为 10000-15000 字符
- 如果 API 限制较严格，设置为 8000-10000
- 文档很大时，减小分块大小以避免超时

### Q: 支持哪些文件格式？

**A:**
- `.md`, `.markdown` - Markdown 文件
- `.rst`, `.rest` - reStructuredText 文件

### Q: 输出格式是什么？

**A:**
- LLM 模式：输出 `.txt` 纯文本，无任何格式标记

### Q: 如何处理超大文档？

**A:**
- 减小 `chunk_size` 到 8000-10000
- 减小 `overlap` 到 500-800
- 考虑分批处理

### Q: API 调用失败怎么办？

**A:**
- 检查 API Key 是否正确
- 检查网络连接
- 检查 API Base URL 是否正确
- 脚本会自动重试，如仍然失败请检查配置

## 技术支持

- 📧 提交 Issue：报告问题和建议
- 📖 查看 [SKILLS.md](SKILLS.md) 了解更多技术细节
- 💬 社区讨论：欢迎分享使用经验

## 许可证

MIT License

## 更新日志

### v1.0.0 (2024-03-27)
- ✨ 初始版本
- ✨ 支持 LLM 智能清洗
- ✨ 支持批量处理
- ✨ 生成清洗报告