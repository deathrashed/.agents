#!/usr/bin/env python3
import os
import sys

EXCLUDE_DIRS = {'.git', 'node_modules', 'venv', '__pycache__', 'vendor', 'build', 'dist', '.next', 'target'}
EXCLUDE_EXTS = {'.png', '.jpg', '.jpeg', '.gif', '.ico', '.svg', '.pyc', '.exe', '.dll', '.so', '.dylib', '.zip', '.tar', '.gz', '.pdf', '.mp4', '.mp3'}

def get_line_count(filepath):
    try:
        with open(filepath, 'rb') as f:
            return sum(1 for _ in f)
    except Exception:
        return 0

def generate_heatmap(root_dir):
    file_stats = []
    dir_stats = {}

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Exclude hidden directories and specific build/dependency dirs
        dirnames[:] = [d for d in dirnames if not d.startswith('.') and d not in EXCLUDE_DIRS]
        
        dir_loc = 0
        for filename in filenames:
            ext = os.path.splitext(filename)[1].lower()
            if ext in EXCLUDE_EXTS or filename.startswith('.'):
                continue
            
            filepath = os.path.join(dirpath, filename)
            if os.path.islink(filepath):
                continue

            loc = get_line_count(filepath)
            rel_path = os.path.relpath(filepath, root_dir)
            file_stats.append((rel_path, loc))
            dir_loc += loc

        rel_dir = os.path.relpath(dirpath, root_dir)
        dir_stats[rel_dir] = dir_stats.get(rel_dir, 0) + dir_loc

    # Aggregate parent directories
    aggregated_dir_stats = {}
    for d, loc in dir_stats.items():
        parts = d.split(os.sep)
        for i in range(1, len(parts) + 1):
            parent = os.sep.join(parts[:i])
            aggregated_dir_stats[parent] = aggregated_dir_stats.get(parent, 0) + loc

    print("=== REPO HEATMAP ===")
    print("\n🔥 TOP 10 LARGEST FILES (Potential Refactor Targets):")
    file_stats.sort(key=lambda x: x[1], reverse=True)
    for path, loc in file_stats[:10]:
        print(f"  {loc:5d} lines | {path}")

    print("\n📂 TOP 5 LARGEST DIRECTORIES:")
    dir_list = sorted([(d, loc) for d, loc in aggregated_dir_stats.items() if d != '.'], key=lambda x: x[1], reverse=True)
    for path, loc in dir_list[:5]:
        print(f"  {loc:5d} lines | {path}/")

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    generate_heatmap(target_dir)
