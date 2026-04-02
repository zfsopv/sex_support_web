#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob
import os
import subprocess

# 工作目录
WORKSPACE = os.getcwd()
WS_DIR = os.path.join(WORKSPACE, "ws")
RST_DOCS_DIR = os.path.join(WORKSPACE, "rst_docs")

# 版本文件
VERSION_FILE = os.path.join(WORKSPACE, "VERSION_FILE")

# 仓库配置
REPOS = {
    'libsophon': {
        'name': 'libsophon',
        'rst_paths': [
            'libsophon/doc/guide',
            'libsophon/doc/reference'
        ]
    },
    'bmvid': {
        'name': 'bmcv参考文档',
        'rst_paths': [
            'bmvid/document/bmcv/source_zh'
        ]
    },
    'middleware-soc': {
        'name': 'sophon-mw',
        'rst_paths': [
            'middleware-soc/document/source_faq',
            'middleware-soc/document/source_guide',
            'middleware-soc/document/source_manual'
        ]
    },
    'bootloader-arm64': {
        'name': 'sophon-img',
        'rst_paths': [
            'bootloader-arm64/docs/bm1684x/bm1684x-soft-dev-doc'
        ]
    },
    'sophon-sail': {
        'name': 'sophon-sail',
        'rst_paths': [
            'sophon-sail/docs/source_zh'
        ]
    },
    'sophon-testhub': {
        'name': 'sophon-testhub',
        'rst_paths': [
            'sophon-testhub/SophonSDK_doc/source_zh'
        ]
    },
    'tpu-mlir': {
        'name': 'tpu-mlir',
        'rst_paths': [
            'tpu-mlir/docs/developer_manual/source_zh',
            'tpu-mlir/docs/quick_start/source_zh'
        ]
    }
}

def run_command(cmd, timeout=3600):
    """运行命令并返回结果"""
    print(f"执行命令: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
    if result.returncode != 0:
        print(f"命令执行失败: {result.stderr}")
        raise Exception(f"命令执行失败: {cmd}")
    return result.stdout

def _walk_all_rst_files(directory):
    """递归查找目录下所有 .rst 文件（无序）"""
    rst_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.rst'):
                rst_files.append(os.path.join(root, file))
    return rst_files


def parse_toctree_blocks_from_index(content):
    """
    解析 index.rst 中所有 .. toctree:: 块（按出现顺序）。
    返回 [(has_glob, [docname, ...]), ...]，docname 已去掉 .rst 后缀。
    """
    lines = content.splitlines()
    blocks = []
    i = 0
    n = len(lines)
    while i < n:
        if lines[i].strip() != '.. toctree::':
            i += 1
            continue
        has_glob = False
        entries = []
        i += 1
        while i < n:
            s = lines[i]
            st = s.strip()
            if st == '':
                i += 1
                continue
            if st.startswith(':'):
                if ':glob:' in st:
                    has_glob = True
                i += 1
                continue
            break
        while i < n:
            s = lines[i]
            st = s.strip()
            if st == '':
                i += 1
                continue
            if not s or not s[0].isspace():
                break
            if st.startswith('..'):
                break
            docname = st.split('#')[0].strip()
            if docname.endswith('.rst'):
                docname = docname[:-4]
            entries.append(docname)
            i += 1
        blocks.append((has_glob, entries))
    return blocks


def resolve_doc_entry_to_paths(base_dir, entry, has_glob):
    """
    将 toctree 条目解析为存在的 .rst 文件路径列表。
    has_glob 为 True 时，对未直接解析的条目尝试 glob 扩展。
    """
    entry_clean = entry.strip()
    if entry_clean.endswith('.rst'):
        entry_clean = entry_clean[:-4]

    if any(ch in entry for ch in '*?['):
        pattern = os.path.join(base_dir, entry)
        return sorted(glob.glob(pattern))

    candidates = [
        os.path.join(base_dir, entry_clean + '.rst'),
        os.path.join(base_dir, entry_clean, 'index.rst'),
    ]
    for c in candidates:
        if os.path.isfile(c):
            return [c]

    if has_glob:
        # 显式列举但带 :glob: 时，仍按文件名尝试
        g = sorted(glob.glob(os.path.join(base_dir, glob.escape(entry_clean) + '.rst')))
        if g:
            return g
        g = sorted(glob.glob(os.path.join(base_dir, entry_clean + '*.rst')))
        if g:
            return g
        g = sorted(glob.glob(os.path.join(base_dir, entry)))
        if g:
            return sorted(g)
    return []


def collect_rst_files_ordered(root_dir):
    """
    按 index.rst 中 toctree 顺序收集 .rst；未出现在 toctree 中的文件按相对路径排在末尾。
    """
    root_dir = os.path.abspath(root_dir)
    all_paths = _walk_all_rst_files(root_dir)
    all_set = set(os.path.abspath(p) for p in all_paths)

    index_path = os.path.join(root_dir, 'index.rst')
    if not os.path.isfile(index_path):
        return sorted(all_paths, key=lambda p: os.path.relpath(p, root_dir))

    content = read_rst_file(index_path)
    blocks = parse_toctree_blocks_from_index(content)

    ordered = []
    seen = set()

    for has_glob, entries in blocks:
        for entry in entries:
            for path in resolve_doc_entry_to_paths(root_dir, entry, has_glob):
                ap = os.path.abspath(path)
                if ap in all_set and ap not in seen:
                    seen.add(ap)
                    ordered.append(path)

    orphans = sorted(
        (p for p in all_paths if os.path.abspath(p) not in seen),
        key=lambda p: os.path.relpath(p, root_dir).replace(os.sep, '/'),
    )
    ordered.extend(orphans)
    return ordered

def read_rst_file(filepath):
    """读取RST文件内容"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='gbk') as f:
            return f.read()

def clean_rst_content(content):
    """清理RST内容，移除不需要的指令"""
    # 移除toctree等Sphinx特定指令
    lines = content.split('\n')
    cleaned_lines = []
    for line in lines:
        # 跳过toctree相关行
        if '.. toctree::' in line:
            continue
        if line.strip().startswith(':'):
            continue
        if line.strip() == '':
            continue
        cleaned_lines.append(line)
    return '\n'.join(cleaned_lines)

def read_version_file():
    """读取版本文件，返回仓库到commit的映射"""
    versions = {}
    try:
        with open(VERSION_FILE, 'r') as f:
            lines = f.readlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line.startswith('module:') and '(' in line:
                module_info = line[len('module:'):].strip()
                if '(' in module_info:
                    module_name = module_info.split('(')[0]
                    commit_line = lines[i+1].strip() if i+1 < len(lines) else ''
                    if commit_line.startswith('commit'):
                        commit = commit_line.split()[1] if len(commit_line.split()) > 1 else ''
                        versions[module_name] = commit
            i += 1
        return versions
    except Exception as e:
        print(f"读取版本文件失败: {e}")
        return {}

def merge_rst_files(rst_files):
    """合并多个RST文件，只合并内容超过100行的文件；正文之间仅换行，不插入文件名等标记"""
    merged_content = []
    for rst_file in rst_files:
        content = read_rst_file(rst_file)
        line_count = len(content.split('\n'))
        if line_count <= 100:
            continue
        if merged_content:
            merged_content.append('\n\n')
        merged_content.append(content)
    return ''.join(merged_content)

def update_repo_to_commit(repo_path, commit):
    """将仓库更新到指定commit或默认分支"""
    if not os.path.exists(repo_path):
        print(f"警告: 仓库路径不存在: {repo_path}")
        return False
    
    try:
        # Fetch origin
        cmd = f"cd {repo_path} && git fetch origin"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
        if result.returncode != 0:
            print(f"fetch失败: {result.stderr}")
            return False
        
        # 如果有commit，checkout到指定commit
        if commit:
            print(f"\n更新仓库: {repo_path} -> {commit[:8]}")
            cmd = f"cd {repo_path} && git checkout {commit}"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
            if result.returncode != 0:
                print(f"checkout到commit失败: {result.stderr}")
                # checkout失败，尝试pull到最新版本
                print("尝试pull到最新版本...")
                if pull_to_latest(repo_path):
                    return True
                return False
            print(f"仓库已更新到: {commit[:8]}")
        else:
            # 没有commit，尝试checkout到默认分支（按优先级尝试 master/release/main）
            print(f"\n仓库没有指定commit，尝试checkout到默认分支...")
            for branch in ['master', 'release', 'main']:
                cmd = f"cd {repo_path} && git checkout origin/{branch}"
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
                if result.returncode == 0:
                    print(f"仓库已更新到: origin/{branch}")
                    return True
            print(f"警告: 无法checkout到任何默认分支")
            # checkout到默认分支失败，尝试pull到最新版本
            print("尝试pull到最新版本...")
            if pull_to_latest(repo_path):
                return True
            return False
        
        return True
    except Exception as e:
        print(f"更新仓库失败: {e}")
        return False

def pull_to_latest(repo_path):
    """尝试pull到最新版本"""
    try:
        # 先获取当前分支
        cmd = f"cd {repo_path} && git rev-parse --abbrev-ref HEAD"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
        current_branch = result.stdout.strip()
        
        if current_branch and current_branch != "HEAD":
            # 如果在某个分支上，尝试pull
            print(f"当前分支: {current_branch}，尝试pull...")
            cmd = f"cd {repo_path} && git pull"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
            if result.returncode == 0:
                print(f"成功pull到最新版本: {current_branch}")
                return True
            else:
                print(f"pull失败: {result.stderr}")
        else:
            # 不在任何分支上，尝试切换到默认分支并pull
            print("当前不在任何分支上，尝试切换到默认分支并pull...")
            for branch in ['master', 'release', 'main']:
                cmd = f"cd {repo_path} && git checkout {branch} && git pull origin {branch}"
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
                if result.returncode == 0:
                    print(f"成功切换到 {branch} 并pull到最新版本")
                    return True
        
        return False
    except Exception as e:
        print(f"pull到最新版本失败: {e}")
        return False

def process_repo(repo_key, repo_config, versions):
    """处理单个仓库的文档"""
    print(f"\n{'='*80}")
    print(f"处理仓库: {repo_config['name']}")
    print(f"{'='*80}\n")
    
    repo_name = repo_config['name']
    rst_paths = repo_config['rst_paths']
    
    # 获取该仓库的commit
    commit = versions.get(repo_key)
    if commit:
        print(f"版本文件中的commit: {commit[:8]}")
    else:
        print(f"警告: 仓库 {repo_key} 在版本文件中没有找到commit信息，将使用默认分支")
    
    # 更新仓库到指定commit或默认分支
    if rst_paths:
        repo_path = os.path.join(WS_DIR, rst_paths[0].split('/')[0])
        if not update_repo_to_commit(repo_path, commit):
            print(f"警告: 无法更新仓库 {repo_key}")
            return
    
    # 输出RST文件
    final_rst = os.path.join(RST_DOCS_DIR, f"{repo_name}.rst")
    
    try:
        # 收集所有RST文件
        all_rst_files = []
        for rst_path in rst_paths:
            full_path = os.path.join(WS_DIR, rst_path)
            if not os.path.exists(full_path):
                print(f"警告: 路径不存在: {full_path}")
                continue
            
            rst_files = collect_rst_files_ordered(full_path)
            if rst_files:
                all_rst_files.extend(rst_files)
                print(f"找到 {len(rst_files)} 个RST文件在: {rst_path}")
        
        if not all_rst_files:
            print(f"警告: 仓库 {repo_name} 没有找到任何RST文件")
            return
        
        # 合并RST文件
        print(f"\n合并 {len(all_rst_files)} 个RST文件...")
        merged_content = merge_rst_files(all_rst_files)
        
        # 写入最终RST文件
        with open(final_rst, 'w', encoding='utf-8') as f:
            f.write(merged_content)
        print(f"合并后的RST文件已保存: {final_rst}")
        
    except Exception as e:
        print(f"处理仓库 {repo_name} 时出错: {e}")

def main():
    """主函数"""
    print("开始处理文档合并...")
    
    # 读取版本文件
    print(f"\n读取版本文件: {VERSION_FILE}")
    versions = read_version_file()
    print(f"读取到 {len(versions)} 个仓库的版本信息")
    for repo_key, commit in versions.items():
        print(f"  - {repo_key}: {commit[:8] if commit else 'N/A'}")
    
    # 确保输出目录存在
    os.makedirs(RST_DOCS_DIR, exist_ok=True)
    
    # 清空输出目录
    for item in os.listdir(RST_DOCS_DIR):
        item_path = os.path.join(RST_DOCS_DIR, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
    
    # 处理每个仓库
    for repo_key in REPOS.keys():
        try:
            process_repo(repo_key, REPOS[repo_key], versions)
        except Exception as e:
            print(f"处理仓库 {repo_key} 失败: {e}")
    
    print("\n" + "="*80)
    print("文档处理完成!")
    print("="*80)
    print(f"\n生成的RST文件保存在: {RST_DOCS_DIR}")
    print("\n文件列表:")
    for item in sorted(os.listdir(RST_DOCS_DIR)):
        print(f"  - {item}")

if __name__ == "__main__":
    main()