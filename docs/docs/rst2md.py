#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys

def convert_rst_to_md(rst_file, md_file):
    with open(rst_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    md_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # 处理RST标题 (下面有装饰线的标题)
        if i + 1 < len(lines):
            next_line = lines[i + 1]
            if next_line and next_line.strip() and all(c in '=-~^"\'#*+' for c in next_line.strip()):
                # 这是一个RST标题
                underline_char = next_line.strip()[0]
                title_level = {
                    '=': 1,      # 主标题
                    '-': 2,      # 二级标题
                    '~': 3,      # 三级标题
                    '^': 4,
                    '"': 5,
                    '\'': 6,
                    '#': 6,
                    '*': 6,
                    '+': 6,
                }.get(underline_char, 3)
                
                if next_line.strip() == '=' * len(next_line.strip()):
                    md_lines.append(f"# {line}")
                elif next_line.strip() == '-' * len(next_line.strip()):
                    md_lines.append(f"## {line}")
                elif next_line.strip() == '~' * len(next_line.strip()):
                    md_lines.append(f"### {line}")
                else:
                    md_lines.append(f"{'#' * title_level} {line}")
                i += 2
                continue
        
        # 处理 .. code-block:: cpp
        if line.strip().startswith('.. code-block::'):
            lang = line.split('::')[1].strip() if '::' in line else ''
            md_lines.append(f"```{lang}")
            i += 1
            continue
        
        # 处理 :: 开头的代码块标记
        if line.strip() == '::':
            md_lines.append("```")
            i += 1
            continue
        
        # 处理代码块的结束 (空行后)
        if i > 0 and md_lines and md_lines[-1].strip().startswith('```') and line.strip() == '':
            # 检查是否需要关闭代码块
            if i + 1 < len(lines) and not lines[i + 1].startswith(' ' * 4):
                md_lines.append("```")
                i += 1
                continue
        
        # 处理 .. attention:: 指令
        if line.strip().startswith('.. attention::'):
            md_lines.append("")
            md_lines.append("> **注意：**")
            i += 1
            # 跳过空行
            while i < len(lines) and lines[i].strip() == '':
                i += 1
            continue
        
        # 处理缩进的段落 (在attention块或代码块中)
        if line.startswith('   ') or line.startswith('\t'):
            if md_lines and md_lines[-1].startswith('>'):
                # 是attention块的后续内容
                md_lines.append(f"> {line.strip()}")
            elif md_lines and md_lines[-1].strip().startswith('```'):
                # 是代码块内容
                md_lines.append(line)
            else:
                md_lines.append(line)
        else:
            # 普通段落
            md_lines.append(line)
        
        i += 1
    
    # 第二次遍历：处理链接和其他标记
    md_content = '\n'.join(md_lines)
    
    # 转换RST链接 `text <url>`_ 为 Markdown [text](url)
    def convert_link(match):
        text = match.group(1)
        url = match.group(2)
        return f"[{text}]({url})"
    
    md_content = re.sub(r'`([^`]+)\s*<([^>]+>`_\s*)', convert_link, md_content)
    
    # 转换简单引用 `text`_ 为 Markdown [text](text)
    md_content = re.sub(r'`([^`]+)`_(?!\w)', r'[\1](\1)', md_content)
    
    # 转换 .. _label: 为 Markdown 锚点注释
    md_content = re.sub(r'\.\. _([^:]+):', r'<!-- \1 -->', md_content)
    
    # 转换表格（简单的列表格式）
    # 处理以 | 开头的行
    lines = md_content.split('\n')
    for idx, line in enumerate(lines):
        if line.strip().startswith('|') and '|' in line[1:]:
            # 这是一个表格行
            pass
    
    md_content = '\n'.join(lines)
    
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md_content)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python rst2md.py <input.rst> <output.md>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    convert_rst_to_md(input_file, output_file)
    print(f"Successfully converted {input_file} to {output_file}")