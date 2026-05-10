#!/usr/bin/env python3
import os
import sys
import plistlib
import glob
import shutil

EXAMPLES_DIR = "/Users/rd/.config/keyboard-maestro/macros/kmmacros/Data/2025-12-29_20•59•14"
ASSETS_DIR = "/Users/rd/.agents/plugins/macro-creator/assets/examples"
ACTION_SOURCING_FILE = "/Users/rd/.agents/plugins/macro-creator/references/ACTION-SOURCING.md"

def extract_actions(node, actions):
    if isinstance(node, dict):
        if 'MacroActionType' in node:
            actions.add(node['MacroActionType'])
        for key, value in node.items():
            extract_actions(value, actions)
    elif isinstance(node, list):
        for item in node:
            extract_actions(item, actions)

def process_examples():
    if not os.path.exists(ASSETS_DIR):
        os.makedirs(ASSETS_DIR)
        
    new_sources = {}
    for root, dirs, files in os.walk(EXAMPLES_DIR):
        for file in files:
            if file.endswith('.kmmacros'):
                source_path = os.path.join(root, file)
                name = file
                dest_path = os.path.join(ASSETS_DIR, name)
                # handle duplicate names by adding random or path hash, here just overwrite
                shutil.copy2(source_path, dest_path)
                print(f"Copied {name}")
                
                with open(dest_path, 'rb') as f:
                    try:
                        plist = plistlib.load(f)
                        actions = set()
                        extract_actions(plist, actions)
                        for action in actions:
                            if action not in new_sources:
                                # use filename without extension as the source
                                new_sources[action] = os.path.splitext(name)[0]
                    except Exception as e:
                        print(f"Failed to parse {dest_path}: {e}")
                
    return new_sources

def update_action_sourcing(new_sources):
    with open(ACTION_SOURCING_FILE, 'r') as f:
        lines = f.readlines()
        
    # Find insertion point before '## If The Action Is Not Listed'
    insert_idx = 0
    for i, line in enumerate(lines):
        if line.startswith('## If The Action Is Not Listed'):
            insert_idx = i - 1
            break
            
    if insert_idx > 0:
        added = 0
        for action_type, source in new_sources.items():
            # Check if action already in file
            if any(f"`{action_type}`" in line for line in lines):
                continue
            new_line = f"| `{action_type}` | `assets/examples/{source}.kmmacros` | [Auto-indexed] | check schema carefully |\n"
            lines.insert(insert_idx, new_line)
            insert_idx += 1
            added += 1
            print(f"Added {action_type} from {source}")
            
        if added > 0:
            with open(ACTION_SOURCING_FILE, 'w') as f:
                f.writelines(lines)
            print("Updated ACTION-SOURCING.md")
        else:
            print("No new actions to add to ACTION-SOURCING.md")

if __name__ == "__main__":
    new_sources = process_examples()
    if new_sources:
        update_action_sourcing(new_sources)
