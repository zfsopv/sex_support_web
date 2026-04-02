#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob
import os
import subprocess
import shutil

GERRIT_HOST = "zetao.zhang@gerrit-ai.sophgo.vip:29418"

# RST 收集路径与 Jenkins「Build html」阶段 src_dirs 对齐，见:
# jenkins_pipeline/athena2_sdk/build_sdk_docs.groovy
# 若某仓库的 Makefile 将 SOURCEDIR 设为 source_zh / source_en，则下列路径指向实际含 index.rst 的 Sphinx 源目录（与 groovy 中工程根目录一致）。
REPOS = {
    'sophgo-develop-docs': {
        'name': 'sophgo-develop-docs',
        'rst_paths': [
            # groovy: sophgo-develop-docs/cvitek/athena2-img
            'sophgo-develop-docs/cvitek/athena2-img/source_zh',
            # groovy: sophgo-develop-docs/multimedia（Makefile 对 zh 构建 source_zh / source_faq / source_guide / source_manual）
            'sophgo-develop-docs/multimedia/source_zh',
            'sophgo-develop-docs/multimedia/source_faq',
            'sophgo-develop-docs/multimedia/source_guide',
            'sophgo-develop-docs/multimedia/source_manual',
        ]
    },
    'libsophon': {
        'name': 'libsophon',
        'rst_paths': [
            # groovy: libsophon/doc/guide, guide_en, reference, reference_en, tpu-runtime/docs/reference
            'libsophon/doc/guide',
            'libsophon/doc/reference',
            'libsophon/tpu-runtime/docs/reference',
        ]
    },
    'libsophav': {
        'name': 'libsophav',
        'rst_paths': [
            # groovy: libsophav/bmcv/document/bmcv_demo（SOURCEDIR: source_zh）
            'libsophav/bmcv/document/bmcv_demo/source_zh',
        ]
    },
    'tpu-mlir': {
        'name': 'tpu-mlir',
        'rst_paths': [
            # groovy 在 tpu-mlir 根目录执行 release_doc.sh；HTML 来自 docs/developer_manual、docs/quick_start 的 zh 构建
            'tpu-mlir/docs/developer_manual/source_zh',
            'tpu-mlir/docs/quick_start/source_zh',
        ]
    },
    'sophon-sail': {
        'name': 'sophon-sail',
        'rst_paths': [
            # groovy: sophon-sail/docs（LANG=zh 时 SOURCEDIR=source_zh）
            'sophon-sail/docs/source_zh',
        ]
    },
    'sophon-testhub': {
        'name': 'sophon-testhub',
        'rst_paths': [
            # groovy: sophon-testhub/SophonSDK_doc（LANG=zh 时 SOURCEDIR=source_zh）
            'sophon-testhub/SophonSDK_doc/source_zh',
        ]
    },
}

def clean_env(workspace, output_dir):
    print("清理输出目录...")
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(workspace, exist_ok=True)

def parse_version_file(version_file):
    print("解析版本文件...")
    repo_branch = {}
    repo_commit = {}

    if not os.path.exists(version_file):
        print(f"  警告: 版本文件不存在 {version_file}")
        return repo_branch, repo_commit

    with open(version_file, 'r', encoding='utf-8') as f:
        current_repo = None
        for line in f:
            line = line.strip()
            if line.startswith('module:') and '(' in line:
                start = line.index('module:') + 7
                end = line.index('(')
                current_repo = line[start:end].strip()
                branch_start = line.index('(') + 1
                branch_end = line.index(')')
                branch = line[branch_start:branch_end].strip()
                repo_branch[current_repo] = branch
            elif line.startswith('commit'):
                commit = line.replace('commit', '').strip()
                if current_repo and commit:
                    repo_commit[current_repo] = commit

    return repo_branch, repo_commit

def run_cmd(cmd, cwd=None, check=True):
    print(f"  执行: {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        if check:
            print(f"  警告: 命令执行失败 - {result.stderr}")
        else:
            print(f"  {result.stderr}")
    return result

def clone_and_checkout(repo, branch, commit, workspace):
    repo_dir = os.path.join(workspace, repo)
    repo_url = f"ssh://{GERRIT_HOST}/{repo}"

    print(f"=== 处理仓库: {repo} (分支: {branch}) ===")

    if os.path.exists(repo_dir):
        print("  仓库已存在，使用本地仓库")
        run_cmd("git clean -fd", cwd=repo_dir, check=False)
        run_cmd("git reset --hard", cwd=repo_dir, check=False)
        run_cmd("git fetch origin", cwd=repo_dir, check=False)
    else:
        print("  克隆仓库")
        run_cmd(f"git clone -b {branch} {repo_url} {repo_dir}")

    if commit:
        print(f"  切换到 commit: {commit}")
        run_cmd(f"git checkout {commit}", cwd=repo_dir)
    else:
        print("  使用分支 HEAD")
        run_cmd(f"git checkout origin/{branch}", cwd=repo_dir)

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

def merge_rst_files(rst_files):
    """
    合并多个RST文件，只合并内容超过100行的文件；正文之间仅换行，不插入文件名等标记。
    返回 (合并后的字符串, 合并文件数, 跳过行数<=100 的文件数)
    """
    merged_content = []
    merged_count = 0
    skip_small = 0
    for rst_file in rst_files:
        try:
            content = read_rst_file(rst_file)
        except OSError as e:
            print(f"  警告: 读取文件失败 {rst_file}: {e}")
            continue
        line_count = len(content.split('\n'))
        if line_count <= 100:
            skip_small += 1
            continue
        if merged_content:
            merged_content.append('\n\n')
        merged_content.append(content)
        merged_count += 1
    return ''.join(merged_content), merged_count, skip_small

def process_repo(repo_key, repo_config, workspace, output_dir):
    """处理单个仓库的文档合并"""
    name = repo_config['name']
    rst_paths = repo_config['rst_paths']

    print(f"\n{'='*60}")
    print(f"合并仓库: {name}")
    print(f"{'='*60}")

    all_rst_files = []
    for rst_path in rst_paths:
        full_path = os.path.join(workspace, rst_path)
        if not os.path.exists(full_path):
            print(f"  警告: 路径不存在: {full_path}")
            continue
        ordered = collect_rst_files_ordered(full_path)
        if ordered:
            all_rst_files.extend(ordered)
            print(f"  在 {rst_path} 中收集 {len(ordered)} 个 .rst 文件")

    if not all_rst_files:
        print(f"  警告: 仓库 {name} 未找到任何 RST 文件")
        return 0, 0

    print(f"\n  共 {len(all_rst_files)} 个源文件，开始合并（行数>100）...")
    merged_text, merged_count, skip_small = merge_rst_files(all_rst_files)
    output_file = os.path.join(output_dir, f"{name}.rst")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(merged_text)
    print(f"  跳过(行数<=100): {skip_small}, 合并入输出: {merged_count}")
    print(f"  已写入: {output_file}")
    return merged_count, skip_small

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    version_file = os.path.join(script_dir, 'VERSION_FILE')
    workspace = os.path.join(script_dir, 'a2_ws')
    output_dir = os.path.join(script_dir, 'a2_doc_out')

    clean_env(workspace, output_dir)
    repo_branch, repo_commit = parse_version_file(version_file)

    for repo_key in REPOS:
        branch = repo_branch.get(repo_key, 'master')
        commit = repo_commit.get(repo_key, '')
        clone_and_checkout(repo_key, branch, commit, workspace)

    print("\n=== 开始合并 RST 文档（按 index.rst toctree 顺序）===\n")

    total_merged = 0
    total_skip_small = 0
    for repo_key, repo_config in REPOS.items():
        m, s = process_repo(repo_key, repo_config, workspace, output_dir)
        total_merged += m
        total_skip_small += s

    print(f"\n=== 合并完成 ===")
    print(f"合并入输出的源文件总数: {total_merged}")
    print(f"跳过(行数<=100) 累计: {total_skip_small}")
    print(f"输出目录: {output_dir}")

    for f in sorted(os.listdir(output_dir)):
        file_path = os.path.join(output_dir, f)
        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            print(f"  {f}: {size} bytes")

if __name__ == '__main__':
    main()
