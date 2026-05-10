#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <macro-file.kmmacros>"
  exit 1
fi

MACRO_FILE="$1"

if [[ ! -f "$MACRO_FILE" ]]; then
  echo "Error: File '$MACRO_FILE' not found."
  exit 1
fi

echo "Running plutil -lint..."
if ! plutil -lint "$MACRO_FILE"; then
  echo "❌ VALIDATION FAILED: Invalid plist syntax."
  exit 1
fi
echo "✅ plutil -lint passed."

# Optional semantic checks via python
echo "Running semantic checks..."
python3 - <<EOF
import plistlib
import sys

file_path = "$MACRO_FILE"
try:
    with open(file_path, 'rb') as f:
        plist = plistlib.load(f)
except Exception as e:
    print(f"❌ VALIDATION FAILED: Could not parse plist. {e}")
    sys.exit(1)

if not isinstance(plist, list):
    print("❌ VALIDATION FAILED: Top level of .kmmacros must be an array.")
    sys.exit(1)

has_macros = False
for group in plist:
    if not isinstance(group, dict):
        print("❌ VALIDATION FAILED: Items in root array must be dictionaries (Macro Groups).")
        sys.exit(1)
        
    if 'Macros' in group:
        has_macros = True
        for macro in group['Macros']:
            if not isinstance(macro, dict):
                print("❌ VALIDATION FAILED: Items in 'Macros' array must be dictionaries.")
                sys.exit(1)
            
            if 'Actions' in macro:
                for action in macro['Actions']:
                    if not isinstance(action, dict):
                        print("❌ VALIDATION FAILED: Items in 'Actions' array must be dictionaries.")
                        sys.exit(1)
                    if 'MacroActionType' not in action:
                        print("❌ VALIDATION FAILED: Every action must have a 'MacroActionType'.")
                        sys.exit(1)

if not has_macros:
    print("⚠️ WARNING: No macros found in the file. This might be just a macro group without macros.")

print("✅ Semantic checks passed.")
EOF

echo "🎉 Validation Complete."
