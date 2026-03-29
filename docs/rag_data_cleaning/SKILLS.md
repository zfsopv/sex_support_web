# RAG 数据清洗 Skill - 技术文档

## Skill 元数据

```yaml
name: RAG Data Cleaning
version: 1.0.0
author: RAG Data Engineer
license: MIT
category: Data Processing
tags: [rag, data-cleaning, markdown, rst, pdf, vector-database, llm]
```

## 概述

本 Skill 专门用于清洗准备存入 RAG（检索增强生成）向量数据库的文档。处理从 PDF 转换或 RST 文档生成的 markdown 文件，移除噪声和格式标记，提升向量检索质量和性能。

## 背景

### 为什么需要数据清洗？

RAG 系统的检索质量严重依赖文档的清洁程度。PDF 转换或 RST 文档生成的 markdown 文件通常包含大量噪声：

1. **页眉页脚**：重复的标题、页码、版权信息
2. **格式标记**：markdown/RST 语法符号
3. **引用标记**：文献引用、脚注编号
4. **转换伪影**：OCR 错误、多余空格、分隔符
5. **结构噪声**：目录页码、重复内容

这些噪声会：
- 降低向量嵌入质量
- 影响语义检索准确性
- 增加存储和计算成本
- 干扰生成模型的回答

### 为什么使用 LLM？

传统的正则表达式清洗虽然快速，但存在局限：

1. **上下文理解不足**：无法区分格式标记和实际内容
2. **规则复杂**：需要编写大量正则表达式
3. **误删风险**：可能错误删除重要内容
4. **维护困难**：新文档类型需要新规则

LLM 的优势：

1. **语义理解**：理解文档语义，智能识别噪声
2. **自适应**：适应不同文档类型和格式
3. **保守清洗**：不确定时保留内容
4. **上下文连贯**：利用重叠分块保持上下文

## 上下文限制与分块策略

### LLM 上下文限制

不同模型的上下文限制：

| 模型 | 上下文限制 |
|------|-----------|
| GPT-3.5 | 4K-16K tokens |
| GPT-4 | 8K-32K tokens |
| GPT-4 Turbo | 128K tokens |
| Claude 3 | 200K tokens |

本工具设计为适应 **20K tokens** 的限制。

### 分块策略

#### 重叠分块

使用重叠分块策略处理大文档：

```
[Chunk 1: 15K chars]
                    [Overlap: 1K chars]
[Chunk 2: 15K chars]
                    [Overlap: 1K chars]
[Chunk 3: 15K chars]
```

**优势：**
- 处理大文件不受上下文限制
- 保持上下文连贯性
- 减少分块边界的内容丢失

**参数：**
- `chunk_size`: 15000 字符（约 12K tokens）
- `overlap`: 1000 字符（约 800 tokens）

#### 上下文窗口

每个分块都包含前后分块的部分内容作为上下文：

```
Previous Chunk End (500 chars)
            |
            V
[Current Chunk Content]
            |
            V
Next Chunk Start (500 chars)
```

**优势：**
- LLM 理解分块在文档中的位置
- 更好地处理跨分块的句子/段落
- 减少边界处的错误判断

## 清洗规则详解

### 页眉页脚

#### 识别模式

| 模式 | 示例 | 清洗策略 |
|------|------|---------|
| 页码 | "Page 42", "第5页", "Page 5 of 10" | 完全移除 |
| 页眉 | "Chapter 3 \| Page 15", "公司名称" | 完全移除 |
| 页脚 | "Copyright 2024", "保存三年" | 完全移除 |
| 分隔符 | "---", "===", "***" (3个以上) | 完全移除 |

#### LLM 处理逻辑

```python
if line matches page_header_pattern:
    remove line
elif line matches page_footer_pattern:
    remove line
elif line is separator:
    remove line
```

### Markdown/RST 标记

#### 识别模式

| 标记类型 | 示例 | 清洗策略 |
|---------|------|---------|
| 标题 | `# H1`, `## H2`, `### H3` | 移除 `#` 符号，保留文本 |
| 加粗 | `**bold**`, `__bold__` | 移除 `**` 或 `__`，保留文本 |
| 斜体 | `*italic*`, `_italic_` | 移除 `*` 或 `_`，保留文本 |
| 代码 | `` `code` `` | 移除反引号，保留代码 |
| 代码块 | ` ``` ` | 移除标记，保留代码内容 |
| 引用 | `> quote` | 移除 `>`，保留内容 |
| 列表 | `- item`, `* item`, `+ item` | 移除标记，保留内容 |
| 链接 | `[text](url)` | 保留文本，移除 URL |

#### RST 指令

| 指令 | 示例 | 清洗策略 |
|-----|------|---------|
| 注释 | `.. note::` | 完全移除 |
| 警告 | `.. warning::` | 完全移除 |
| 提示 | `.. tip::` | 完全移除 |
| 图片 | `.. image:: file.png` | 完全移除 |
| 表格 | `.. table:: Title` | 完全移除 |
| 代码 | `.. code:: python` | 完全移除，保留代码内容 |
| 包含 | `.. include:: file.rst` | 完全移除 |
| 目录 | `.. toctree::` | 完全移除 |

### 引用标记

#### 识别模式

| 模式 | 示例 | 清洗策略 |
|------|------|---------|
| 数字引用 | `[1]`, `[2]`, `[15]` | 完全移除 |
| 字母引用 | `[ref]`, `[REF]` | 完全移除 |
| 脚注 | `Footnote 1`, `Note 1` | 完全移除 |
| 星号标记 | `*` (单独) | 完全移除 |
| 双星号 | `**` (单独) | 完全移除 |

### PDF 转换伪影

#### 识别模式

| 类型 | 示例 | 清洗策略 |
|------|------|---------|
| 连字符断行 | `exam-\nple` | 合并为 `example` |
| 多余空格 | `word  word` | 合并为单个空格 |
| 多余换行 | `\n\n\n\n` | 合并为单个换行 |
| OCR 错误 | `w0rd`, `c0de` | LLM 智能纠正 |
| 列分隔符 | `|` | 移除或转换为逗号 |
| 表格边框 | `+---+---+` | 完全移除 |

### 目录页码

#### 识别模式

```markdown
1 声明                                                                         1
2  SAIL                                                                        5
3 编译安装指南                                                                 7
```

#### 清洗策略

```markdown
1 声明

2 SAIL

3 编译安装指南
```

移除右侧的页码和对齐空格。

## 实现细节

### LLM 清洗流程

```
1. 读取文件
   ↓
2. 创建重叠分块
   ↓
3. 对每个分块：
   a. 准备上下文（前后分块内容）
   b. 构造清洗提示词
   c. 调用 LLM API
   d. 解析响应
   ↓
4. 合并分块（移除重叠）
   ↓
5. 写入输出文件
   ↓
6. 生成清洗报告
```

### 提示词设计

#### Chunk 清洗提示词

```
你是一个专业的文档清洗助手，专门为RAG向量数据库清洗文档。

请清洗以下文档内容，输出纯文本格式（不包含任何markdown标记符号）。

清洗规则：
1. 移除页眉、页脚、页码（如"Page 42"、"第5页"、"--- 156 ---"等）
2. 移除所有markdown/RST标记符号（#、*、`、.. note::等）
3. 移除RST指令（.. note::、.. warning::、.. toctree::、.. image::等）
4. 移除引用标记（[1]、[2]、Footnote 1等）
5. 移除PDF转义产生的多余空格、换行、分隔符
6. 移除重复的页脚信息（如"保存三年"）
7. 移除目录中的页码编号

保留原则：
- 保留所有实际内容和说明文字
- 保留文档的逻辑结构和层次关系
- 保留技术信息和代码示例内容
- 保留表格中的实际数据
- 不确定是否为噪声时，保留它

输出要求：
- 只输出纯文本内容，不包含任何markdown符号
- 保持段落结构清晰
- 内容连贯易读

这是第 {chunk_num}/{total} 个分块。

上下文信息：
- 前一个分块结尾："{previous_end[:200]}..."
- 后一个分块开头："{next_start[:200]}..."

文档内容：
{chunk}

请输出清洗后的纯文本内容：
```

#### 合并验证提示词（可选）

```
你正在验证一个经过分块清洗后合并的文档。

请检查以下问题：
1. 分块边界是否有内容丢失
2. 分块之间的过渡是否自然
3. 是否有重复内容（来自重叠区域）
4. 文档结构是否完整
5. 是否引入了清洗伪影

合并文档（前2000字符）：
{merged_document[:2000]}

返回 "VALID" 如果文档正常，或描述发现的问题。
```

### API 调用优化

#### 超时和重试

```python
max_retries = 3
timeout = 120  # 秒

for attempt in range(max_retries):
    try:
        response = call_llm_api(prompt, timeout)
        break
    except TimeoutError:
        if attempt == max_retries - 1:
            raise
        wait_time = 2 ** attempt  # 指数退避
        time.sleep(wait_time)
```

#### 并发处理

对于大量文件，可以并发处理多个文件：

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(cleaner.clean_file, f) for f in files]
    results = [f.result() for f in futures]
```

### Token 计数

#### 字符到 Token 估算

```python
def estimate_chars(text: str) -> int:
    # 中文：1 字符 ≈ 1 token
    # 英文：4 字符 ≈ 1 token
    chinese_chars = len([c for c in text if '\u4e00' <= c <= '\u9fff'])
    other_chars = len(text) - chinese_chars
    return chinese_chars + (other_chars // 4)
```

#### 精确计数（需要 tiktoken）

```python
import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4")
token_count = len(encoding.encode(text))
```

## 错误处理

### API 失败处理

```python
try:
    cleaned = call_llm_api(prompt)
except APIError as e:
    if can_retry(e):
        retry_with_smaller_chunk()
    else:
        log_error_and_skip()
```

### 分块失败处理

```python
if chunk_empty:
    skip_and_adjust_boundary()
if chunk_too_large:
    split_into_smaller_chunks()
```

### 合并失败处理

```python
if merge_conflict:
    use_llm_to_resolve_conflict()
if context_loss_detected:
    increase_overlap_and_retry()
```

## 性能优化

### 批量处理

- 并发处理多个文件（限制并发数避免 API 限流）
- 分批处理超大批量文件

### 缓存策略

- 缓存已清洗的分块
- 检测文档变化，只清洗修改部分

### 进度跟踪

```python
for idx, chunk in enumerate(chunks):
    print(f"Cleaning chunk {idx + 1}/{len(chunks)}", end="\r")
```

### 日志记录

```python
import logging

logging.basicConfig(
    filename='cleaning.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

## 质量保证

### 验证检查清单

- [ ] 内容完整性检查（对比输入输出长度）
- [ ] 结构完整性检查（标题层级、段落）
- [ ] 语义一致性检查（抽样人工审查）
- [ ] 噪声移除检查（搜索页码、标记等）
- [ ] 边界处理检查（分块边界内容）

### 测试用例

#### 测试 1: 页码移除

```python
input_text = "Page 42\n这是内容"
expected_output = "这是内容"
assert clean(input_text) == expected_output
```

#### 测试 2: 标题移除

```python
input_text = "# 标题\n内容"
expected_output = "标题\n内容"
assert clean(input_text) == expected_output
```

#### 测试 3: 引用移除

```python
input_text = "内容[1]更多内容"
expected_output = "内容更多内容"
assert clean(input_text) == expected_output
```

## 集成示例

### 与 RAG 系统集成

```python
from rag_data_cleaning import LLMCleaner
from vector_db import VectorDB

# 1. 清洗文档
cleaner = LLMCleaner(api_key="your_key")
cleaner.clean_directory("docs/", "cleaned_docs/")

# 2. 索引清洗后的文档
db = VectorDB()
db.index_directory("cleaned_docs/")

# 3. 检索
results = db.search("如何安装？")
```

### 与数据处理流水线集成

```python
import asyncio

async def pipeline():
    # 步骤 1: 下载文档
    await download_docs()
    
    # 步骤 2: 清洗文档
    cleaner = LLMCleaner(api_key="your_key")
    await cleaner.clean_directory_async("raw/", "cleaned/")
    
    # 步骤 3: 分块
    chunks = await split_documents("cleaned/")
    
    # 步骤 4: 生成嵌入
    embeddings = await generate_embeddings(chunks)
    
    # 步骤 5: 索引
    await index_embeddings(embeddings)
```

## 扩展和自定义

### 添加自定义清洗规则

```python
class CustomCleaner(LLMCleaner):
    def clean_chunk(self, chunk, chunk_num, total):
        # 自定义预处理
        chunk = self.custom_preprocess(chunk)
        
        # 调用父类方法
        cleaned = super().clean_chunk(chunk, chunk_num, total)
        
        # 自定义后处理
        cleaned = self.custom_postprocess(cleaned)
        
        return cleaned
    
    def custom_preprocess(self, chunk):
        # 移除特定水印
        chunk = re.sub(r'Watermark: .*', '', chunk)
        return chunk
```

### 自定义分块策略

```python
def create_semantic_chunks(self, text):
    # 基于段落或章节分块
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = []
    current_size = 0
    
    for para in paragraphs:
        if current_size + len(para) > self.chunk_size:
            chunks.append('\n\n'.join(current_chunk))
            current_chunk = [para]
            current_size = len(para)
        else:
            current_chunk.append(para)
            current_size += len(para)
    
    if current_chunk:
        chunks.append('\n\n'.join(current_chunk))
    
    return chunks
```

## 最佳实践

### 1. 选择合适的模式

- **LLM 模式**：高质量要求、复杂文档
- **Regex 模式**：快速批量处理、简单文档

### 2. 调整分块参数

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

### 3. 监控 API 使用

```python
# 设置使用限制
max_tokens_per_minute = 100000
```

### 4. 备份原始文件

```python
# 清洗前备份
shutil.copytree("docs/", "docs_backup/")
```

### 5. 验证清洗结果

```python
# 对比文件大小
original_size = len(original_text)
cleaned_size = len(cleaned_text)
reduction = (original_size - cleaned_size) / original_size

# 通常应该在 10-30% 之间
if reduction < 0.1 or reduction > 0.3:
    print("Warning: Unusual reduction rate")
```

## 故障排除

### 问题 1: API 调用超时

**原因：** 分块太大或网络问题

**解决方案：**
- 减小 `chunk_size`
- 增加 `timeout`
- 检查网络连接

### 问题 2: 清洗后内容丢失

**原因：** 提示词过于激进或 LLM 误删

**解决方案：**
- 修改提示词，强调保守清洗
- 增加 `overlap`
- 使用更高质量的模型

### 问题 3: 清洗效果不明显

**原因：** 文档本身已经很清洁

**解决方案：**
- 检查原始文档
- 确认清洗规则是否适用

### 问题 4: 输出格式不符合预期

**原因：** LLM 没有遵循输出格式要求

**解决方案：**
- 优化提示词中的输出要求
- 添加后处理步骤强制格式

## 参考资源

- [OpenAI API 文档](https://platform.openai.com/docs)
- [RAG 最佳实践](https://www.anthropic.com/claude/docs/retrieval-augmented-generation)
- [向量数据库指南](https://www.pinecone.io/learn/vector-database/)
- [文档处理技巧](https://www.deeplearning.ai/short-courses/)

## 版本历史

### v1.0.0 (2024-03-27)
- ✨ 初始版本
- ✨ LLM 智能清洗
- ✨ Regex 快速清洗
- ✨ 重叠分块策略
- ✨ 批量处理支持
- ✨ 清洗报告生成

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！