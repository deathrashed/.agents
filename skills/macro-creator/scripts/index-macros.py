#!/usr/bin/env python3
import os
import sys
import plistlib
import glob
import shutil

LATEST_BACKUP_DIR = "/Users/rd/.config/keyboard-maestro/macros/kmmacros/Data/2026-05-03_03•13•01/-  Palettes  -/"
ASSETS_DIR = "/Users/rd/.agents/plugins/macro-creator/assets/real-exports/"
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

def process_palette(name):
    source_path = os.path.join(LATEST_BACKUP_DIR, f"{name}.kmmacros")
    if not os.path.exists(source_path):
        print(f"File not found: {source_path}")
        return set()
    
    dest_path = os.path.join(ASSETS_DIR, f"{name.lower()}.kmmacros")
    shutil.copy2(source_path, dest_path)
    print(f"Copied {name} to {dest_path}")
    
    with open(dest_path, 'rb') as f:
        try:
            plist = plistlib.load(f)
            actions = set()
            extract_actions(plist, actions)
            return actions
        except Exception as e:
            print(f"Failed to parse {dest_path}: {e}")
            return set()

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
        for action_type, source in new_sources.items():
            # Check if action already in file
            if any(f"`{action_type}`" in line for line in lines):
                continue
            new_line = f"| `{action_type}` | `assets/real-exports/{source}.kmmacros` | [Auto-indexed] | check schema carefully |\n"
            lines.insert(insert_idx, new_line)
            insert_idx += 1
            print(f"Added {action_type} to ACTION-SOURCING.md")
            
        with open(ACTION_SOURCING_FILE, 'w') as f:
            f.writelines(lines)
        print("Updated ACTION-SOURCING.md")

if __name__ == "__main__":
    symbols_actions = process_palette("Symbols")
    music_actions = process_palette("Music")
    
    new_sources = {}
    for action in symbols_actions:
        new_sources[action] = "symbols"
    for action in music_actions:
        if action not in new_sources:
            new_sources[action] = "music"
            
    if new_sources:
        update_action_sourcing(new_sources)
