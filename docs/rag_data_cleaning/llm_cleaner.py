#!/usr/bin/env python3
"""
LLM-based Document Cleaner for RAG
使用LLM清洗markdown/RST文档，输出纯文本格式
支持语义分块，确保边缘区域语义完整
"""

import os
import sys
import json
import requests
import argparse
import time
from pathlib import Path
from typing import List, Tuple, Optional, Dict
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
from functools import wraps


def retry_on_error(max_retries: int = 3, delay: float = 1.0):
    """重试装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt < max_retries - 1:
                        time.sleep(delay * (attempt + 1))
                    else:
                        raise e
            return None
        return wrapper
    return decorator


class LLMCleaner:
    """使用LLM清洗文档"""

    def __init__(
        self,
        api_key: str,
        api_base: str = "https://api.openai.com/v1",
        model: str = "gpt-4",
        chunk_size: int = 10000,
        boundary_size: int = 1000,
        max_workers: int = 20
    ):
        self.api_key = api_key
        self.api_base = api_base.rstrip('/')
        self.model = model
        self.chunk_size = chunk_size
        self.boundary_size = boundary_size
        self.max_workers = max_workers
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        self.results_lock = Lock()
        self.print_lock = Lock()
        self.last_llm_call_time = 0
        self.llm_call_lock = Lock()
        self.current_file = None

    def estimate_tokens(self, text: str) -> int:
        """估算token数（中文1字符约1token，英文4字符约1token）"""
        chinese_chars = len([c for c in text if '\u4e00' <= c <= '\u9fff'])
        other_chars = len(text) - chinese_chars
        return chinese_chars + (other_chars // 4)

    def create_initial_chunks(self, text: str) -> List[Tuple[int, int]]:
        """第一步：按chunk_size创建初始分块，返回(start, end)位置列表"""
        chunks = []
        text_len = len(text)
        
        start = 0
        while start < text_len:
            end = min(start + self.chunk_size, text_len)
            chunks.append((start, end))
            start = end
        
        return chunks

    def analyze_boundary_with_llm(self, text: str, boundary_pos: int, prev_chunk_end: int, next_chunk_start: int) -> int:
        """第二步：使用LLM分析边界区域，返回调整后的分界点位置
        
        Args:
            text: 完整文本
            boundary_pos: 原始边界位置
            prev_chunk_end: 前一个分块结束位置
            next_chunk_start: 下一个分块开始位置
        
        Returns:
            调整后的分界点位置
        """
        left_start = max(prev_chunk_end, boundary_pos - self.boundary_size)
        right_end = min(next_chunk_start, boundary_pos + self.boundary_size)
        
        boundary_text = text[left_start:right_end]
        original_pos_in_boundary = boundary_pos - left_start
        
        prompt = f"""请分析以下文本片段，在范围内找到一个合适的分界点位置，以确保分块之间的语义完整和结构合理。
输出要求：
- 禁止修改源文本内容
- 输出分界点上方3行的文本内容，并且在分界点出用<<<分割点>>>标记出来
- <<<分割点>>>只能出现在空行，避免出现在句子中间
- 只输出<<<分割点>>>和附近文本，不要任何额外解释

文本片段内容:
{boundary_text}

请输出<<<分割点>>>以及附近内容："""

        try:
            result = self.call_llm(prompt)
            with self.print_lock:
                print(f"\n  LLM分割点分析输出:\n{result}")
            
            if result and '<<<分割点>>>' in result:
                split_point_marker = '<<<分割点>>>'
                lines = result.split('\n')
                
                split_line_idx = -1
                for i, line in enumerate(lines):
                    if split_point_marker in line:
                        split_line_idx = i
                        break
                
                if split_line_idx != -1:
                    split_line = lines[split_line_idx]
                    line_without_marker = split_line.replace(split_point_marker, '').strip()
                    
                    with self.print_lock:
                        print(f"\n  解析分割点:")
                        print(f"    分割行索引: {split_line_idx}")
                        print(f"    分割行内容: '{split_line}'")
                        print(f"    去除标记后: '{line_without_marker}'")
                    
                    if not line_without_marker:
                        with self.print_lock:
                            print(f"    分割点是空行，提取上方行内容...")
                        
                        lines_list = result.split('\n')
                        content_lines = []
                        for offset in range(1, split_line_idx + 1):
                            line_text = lines_list[split_line_idx - offset].strip()
                            if line_text:
                                content_lines.insert(0, line_text)
                                if len(content_lines) >= 3:
                                    break
                        
                        if content_lines:
                            with self.print_lock:
                                print(f"    提取到{len(content_lines)}行内容: {content_lines}")
                            
                            for num_lines in [3, 2, 1]:
                                if len(content_lines) >= num_lines:
                                    lines_to_match = content_lines[-num_lines:]
                                    with self.print_lock:
                                        print(f"    尝试匹配{num_lines}行: {lines_to_match}")
                                    
                                    for match_type in ['精确', '模糊']:
                                        with self.print_lock:
                                            print(f"    尝试{match_type}匹配...")
                                        
                                        if match_type == '精确':
                                            match_text = '\n'.join(lines_to_match)
                                            match_pos = boundary_text.rfind(match_text)
                                            if match_pos != -1:
                                                line_end = boundary_text.find('\n', match_pos)
                                                if line_end == -1:
                                                    line_end = match_pos + len(match_text)
                                                new_pos = line_end
                                                adjusted_pos = left_start + new_pos
                                                with self.print_lock:
                                                    print(f"    {match_type}匹配成功！分割点设在该{num_lines}行之后: {adjusted_pos}")
                                                return adjusted_pos
                                        else:
                                            success = True
                                            current_pos = -1
                                            for line in lines_to_match:
                                                if current_pos == -1:
                                                    pos = boundary_text.rfind(line)
                                                else:
                                                    pos = boundary_text.find(line, current_pos)
                                                
                                                if pos == -1:
                                                    success = False
                                                    with self.print_lock:
                                                        print(f"    行'{line[:50]}...'未找到")
                                                    break
                                                
                                                line_end = boundary_text.find('\n', pos)
                                                if line_end != -1:
                                                    current_pos = line_end + 1
                                                else:
                                                    current_pos = pos + len(line)
                                            
                                            if success:
                                                adjusted_pos = left_start + current_pos
                                                with self.print_lock:
                                                    print(f"    {match_type}匹配成功！分割点设在该{num_lines}行之后: {adjusted_pos}")
                                                return adjusted_pos
                    else:
                        exact_match = boundary_text.find(line_without_marker)
                        if exact_match != -1:
                            marker_pos_in_line = split_line.find(split_point_marker)
                            new_pos = exact_match + marker_pos_in_line
                            adjusted_pos = left_start + new_pos
                            
                            with self.print_lock:
                                print(f"    精确匹配位置: {exact_match}")
                                print(f"    标记在行中的偏移: {marker_pos_in_line}")
                                print(f"    边界文本中的分割点位置: {new_pos}")
                                print(f"    完整文本中的分割点位置: {adjusted_pos}")
                            return adjusted_pos
                        else:
                            with self.print_lock:
                                print(f"    精确匹配失败，尝试模糊匹配...")
                            
                            for i, line in enumerate(boundary_text.split('\n')):
                                if line_without_marker in line:
                                    fuzzy_match = boundary_text.find(line)
                                    marker_pos_in_fuzzy_line = split_line.find(split_point_marker)
                                    new_pos = fuzzy_match + marker_pos_in_fuzzy_line
                                    adjusted_pos = left_start + new_pos
                                    with self.print_lock:
                                        print(f"    模糊匹配: 第{i+1}行")
                                        print(f"    模糊匹配位置: {adjusted_pos}")
                                    return adjusted_pos
                    
                    with self.print_lock:
                        print(f"\n  边界文本内容（前20行）:")
                        for i, line in enumerate(boundary_text.split('\n')[:20]):
                            print(f"    行{i}: {line[:80]}")
                    
                    raise ValueError(f"无法在边界文本中找到LLM输出的分割位置")
                else:
                    raise ValueError(f"LLM输出中未找到包含 <<<分割点>>> 标记的行")
            else:
                raise ValueError(f"LLM输出中未找到 <<<分割点>>> 标记")
        except Exception as e:
            with self.print_lock:
                print(f"\n  解析分割点时出错: {e}")
                import traceback
                traceback.print_exc()
            raise e

    def refine_chunks_semantically(self, text: str, initial_chunks: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        """第二步：使用LLM优化所有分块边界"""
        if len(initial_chunks) <= 1:
            return initial_chunks
        
        refined = []
        text_len = len(text)
        
        for i in range(len(initial_chunks)):
            if i == 0:
                curr_start = initial_chunks[0][0]
                next_start = initial_chunks[1][0] if len(initial_chunks) > 1 else initial_chunks[0][1]
            else:
                curr_start = refined[-1][1]
            
            if i == len(initial_chunks) - 1:
                curr_end = initial_chunks[-1][1]
            else:
                next_next_start = initial_chunks[i + 2][0] if i + 2 < len(initial_chunks) else initial_chunks[i + 1][1]
                try:
                    new_end = self.analyze_boundary_with_llm(text, initial_chunks[i + 1][0], curr_start, next_next_start)
                except Exception as e:
                    with self.print_lock:
                        print(f"\n  警告: 分块{i}边界分析失败: {e}")
                        print(f"    使用原始位置: {initial_chunks[i + 1][0]}")
                    new_end = initial_chunks[i + 1][0]
                curr_end = max(new_end, curr_start)
            
            print(f"\n  分块{i}边界调整: 新({curr_start}, {curr_end})")
            
            if curr_start < curr_end:
                refined.append((curr_start, curr_end))
        
        return refined

    def call_llm(self, prompt: str) -> Optional[str]:
        """调用LLM API（带重试）"""
        min_interval = 5.0
        max_retries = 5
        delay = 5.0
        
        for attempt in range(max_retries):
            with self.llm_call_lock:
                now = time.time()
                elapsed = now - self.last_llm_call_time
                if elapsed < min_interval:
                    sleep_time = min_interval - elapsed
                    time.sleep(sleep_time)
            
            try:
                response = requests.post(
                    f"{self.api_base}/chat/completions",
                    headers=self.headers,
                    json={
                        "model": self.model,
                        "messages": [
                            {
                                "role": "system",
                                "content": "你是一个专业的文档处理助手，擅长分析和处理文档结构。"
                            },
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ],
                        "temperature": 0.1
                    },
                    timeout=120
                )
                response.raise_for_status()
                with self.llm_call_lock:
                    self.last_llm_call_time = time.time()
                return response.json()['choices'][0]['message']['content'].strip()
            except Exception as e:
                file_prefix = f"[{self.current_file}] " if self.current_file else ""
                if attempt < max_retries - 1:
                    with self.print_lock:
                        print(f"  {file_prefix}API调用失败（第{attempt + 1}次重试）: {e}")
                    time.sleep(delay * (attempt + 1))
                else:
                    with self.print_lock:
                        print(f"  {file_prefix}API调用失败（已达最大重试次数）: {e}")
                return None

    def clean_chunk(self, chunk: str, chunk_num: int, total: int, prev_context: str = "", next_context: str = "") -> str:
        """第三步：使用LLM清洗单个分块"""
        context_info = ""
        if prev_context:
            context_info += f"\n【上文语境】（最后约{self.boundary_size}字符）:\n{prev_context}\n"
        if next_context:
            context_info += f"\n【下文语境】（最先约{self.boundary_size}字符）:\n{next_context}\n"

        prompt = f"""请将以下文档内容清洗并转换为标准Markdown格式，用于RAG向量数据库索引。

清洗规则：
1. 移除所有噪声内容：页眉、页脚、页码、图片、HTML嵌入块（script、style、iframe等）、目录页码等无意义内容
3. 将RST、HTML等标记语言的文档转换为标准Markdown格式
4. 保留所有实际内容、逻辑结构、技术信息、代码示例、表格数据
5. 移除多余空格、换行、分隔符、重复信息

输出要求：
- 输出标准Markdown格式，但不包含图片和HTML嵌入块等包含噪声较多的信息
- 保持段落结构清晰、内容连贯易读
- 不确定是否为噪声时，保留它
- 确保边缘内容与上下文语义连贯
- 输出的内容整体不要使用```markdown包围

这是第 {chunk_num}/{total} 个分块。
{context_info}
当前分块内容：
{chunk}

请输出清洗后的Markdown内容："""

        result = self.call_llm(prompt)
        
        if result:
            lines = result.split('\n')
            content_lines = []
            skip_start = True
            for line in lines:
                stripped = line.strip()
                if skip_start:
                    if stripped and not stripped.startswith('清洗后的') and not stripped.startswith('输出'):
                        skip_start = False
                if not skip_start:
                    content_lines.append(line)
            return '\n'.join(content_lines).strip()
        
        return chunk

    def clean_file(self, input_path: str, output_path: str) -> dict:
        """清洗单个文件"""
        file_name = Path(input_path).name
        self.current_file = file_name
        print(f"\n处理: {file_name}")
        
        with open(input_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        total_tokens = self.estimate_tokens(text)
        with self.print_lock:
            print(f"  [{file_name}] 总Token数（估算）: {total_tokens:,}")
        
        stats = {
            "input_file": str(input_path),
            "output_file": str(output_path),
            "total_chars": len(text),
            "num_chunks": 0
        }
        
        with self.print_lock:
            print(f"  [{file_name}] 第一步：创建初始分块（大小约{self.chunk_size}字符）...")
        initial_chunks = self.create_initial_chunks(text)
        with self.print_lock:
            print(f"  [{file_name}] 初始分块数: {len(initial_chunks)}")
        
        if len(initial_chunks) > 1:
            with self.print_lock:
                print(f"  [{file_name}] 第二步：使用LLM优化分块边界（边界区域{self.boundary_size}字符）...")
            refined_chunks = self.refine_chunks_semantically(text, initial_chunks)
            with self.print_lock:
                print(f"  [{file_name}] 优化后分块数: {len(refined_chunks)}")
        else:
            refined_chunks = initial_chunks
        
        stats["num_chunks"] = len(refined_chunks)
        
        with self.print_lock:
            print(f"  [{file_name}] 第三步：清洗各分块（并行处理）...")
        
        def clean_single_chunk(chunk_idx: int, start: int, end: str):
            """清洗单个分块的辅助函数"""
            chunk = text[start:end]
            
            prev_context = ""
            if chunk_idx > 0:
                prev_start = refined_chunks[chunk_idx - 1][1]
                context_start = max(prev_start, end - self.boundary_size * 2)
                prev_context = text[context_start:start]
            
            next_context = ""
            if chunk_idx < len(refined_chunks) - 1:
                next_end = refined_chunks[chunk_idx + 1][0]
                context_end = min(next_end, end + self.boundary_size * 2)
                next_context = text[end:context_end]
            
            cleaned = self.clean_chunk(chunk, chunk_idx + 1, len(refined_chunks), prev_context, next_context)
            
            if cleaned:
                return (chunk_idx, cleaned)
            else:
                return (chunk_idx, chunk)
        
        cleaned_chunks_dict: Dict[int, str] = {}
        
        with ThreadPoolExecutor(max_workers=min(self.max_workers, len(refined_chunks))) as executor:
            futures = {
                executor.submit(clean_single_chunk, idx, start, end): idx 
                for idx, (start, end) in enumerate(refined_chunks)
            }
            
            completed = 0
            for future in as_completed(futures):
                chunk_idx = futures[future]
                try:
                    result = future.result()
                    if result:
                        cleaned_chunks_dict[result[0]] = result[1]
                        completed += 1
                        with self.print_lock:
                            print(f"  [{file_name}] 清洗分块 {completed}/{len(refined_chunks)} 完成")
                except Exception as e:
                    with self.print_lock:
                        print(f"  [{file_name}] 清洗分块 {chunk_idx + 1} 失败: {e}")
                    cleaned_chunks_dict[chunk_idx] = text[refined_chunks[chunk_idx][0]:refined_chunks[chunk_idx][1]]
        
        cleaned_chunks = [cleaned_chunks_dict[i] for i in sorted(cleaned_chunks_dict.keys())]
        
        with self.print_lock:
            print(f"  [{file_name}] 合并分块...")
        merged = '\n\n'.join(cleaned_chunks)
        
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(merged)
        
        stats["output_chars"] = len(merged)
        stats["chars_removed"] = len(text) - len(merged)
        
        with self.print_lock:
            print(f"  [{file_name}] 输出: {output_path.name}")
            print(f"  [{file_name}] 输出字符数: {len(merged):,}")
        
        self.current_file = None
        return stats

    def clean_directory(self, input_dir: str, output_dir: str) -> List[dict]:
        """批量清洗目录中的所有文件（支持多线程）"""
        input_path = Path(input_dir)
        output_path = Path(output_dir)
        
        results = []
        
        files = []
        files.extend(input_path.glob("*.md"))
        files.extend(input_path.glob("*.MD"))
        files.extend(input_path.glob("*.rst"))
        files.extend(input_path.glob("*.RST"))
        
        files = sorted(files)
        
        with self.print_lock:
            print(f"\n找到 {len(files)} 个文件")
            print(f"使用 {self.max_workers} 个线程并发处理文件")
        
        def process_file(file, idx):
            output_file = output_path / f"{file.stem}_clear.md"
            file_name = file.name
            
            try:
                stats = self.clean_file(str(file), str(output_file))
                with self.print_lock:
                    print(f"  [{file_name}] 进度: {idx + 1}/{len(files)}")
                return stats
            except Exception as e:
                with self.print_lock:
                    print(f"  [{file_name}] 错误: {e}")
                return None
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(process_file, file, idx) for idx, file in enumerate(files)]
            
            for future in as_completed(futures):
                result = future.result()
                if result:
                    with self.results_lock:
                        results.append(result)
        
        return results


def main():
    parser = argparse.ArgumentParser(description="LLM 文档清洗工具 - 语义分块版（支持多线程）")
    parser.add_argument("input_dir", help="输入目录")
    parser.add_argument("output_dir", help="输出目录")
    parser.add_argument("--api-key", help="API密钥（也可通过环境变量OPENAI_API_KEY设置）")
    parser.add_argument("--api-base", default="https://api.openai.com/v1", help="API基础URL（默认: https://api.openai.com/v1）")
    parser.add_argument("--model", default="gpt-4", help="模型名称（默认: gpt-4）")
    parser.add_argument("--chunk-size", type=int, default=10000, help="分块大小（默认: 10000字符）")
    parser.add_argument("--boundary-size", type=int, default=1000, help="边界区域大小（默认: 1000字符）")
    parser.add_argument("--max-workers", type=int, default=20, help="最大并发线程数（默认: 20）")
    
    args = parser.parse_args()
    
    api_key = args.api_key or os.getenv("OPENAI_API_KEY", "")
    
    if not api_key:
        print("错误: 请提供API密钥")
        print("方式1: --api-key your_api_key")
        print("方式2: export OPENAI_API_KEY=your_api_key")
        print("方式3: 使用配置文件 config.json")
        sys.exit(1)
    
    config_file = Path(__file__).parent / "config.json"
    if config_file.exists():
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
            api_key = config.get("api_key", api_key) if not args.api_key else api_key
            args.api_base = config.get("api_base", args.api_base) if args.api_base == "https://api.openai.com/v1" else args.api_base
            args.model = config.get("model", args.model) if args.model == "gpt-4" else args.model
    
    print("=" * 60)
    print("LLM 文档清洗工具 - 语义分块版")
    print("=" * 60)
    print(f"API Base: {args.api_base}")
    print(f"Model: {args.model}")
    print(f"输入目录: {args.input_dir}")
    print(f"输出目录: {args.output_dir}")
    print(f"分块大小: {args.chunk_size}字符")
    print(f"边界区域: {args.boundary_size}字符")
    print(f"并发线程数: {args.max_workers}")
    print("=" * 60)
    
    cleaner = LLMCleaner(
        api_key=api_key,
        api_base=args.api_base,
        model=args.model,
        chunk_size=args.chunk_size,
        boundary_size=args.boundary_size,
        max_workers=args.max_workers
    )
    
    results = cleaner.clean_directory(args.input_dir, args.output_dir)
    
    print("\n" + "=" * 60)
    print("清洗完成!")
    print(f"处理文件数: {len(results)}")
    total_input = sum(r.get("total_chars", 0) for r in results)
    total_output = sum(r.get("output_chars", 0) for r in results)
    print(f"输入总字符数: {total_input:,}")
    print(f"输出总字符数: {total_output:,}")
    print(f"删除字符数: {total_input - total_output:,}")
    print("=" * 60)

    print("详细结果:")
    for r in results:
        print(f"  {Path(r['input_file']).name}: 输入{r['total_chars']:,}字符 -> 输出{r['output_chars']:,}字符 (删除{r['chars_removed']:,}字符, 分块数: {r['num_chunks']})")


if __name__ == "__main__":
    main()
