---
name: keyboard-maestro-actions
description: "Create, modify, package, and debug custom Keyboard Maestro third-party plug-in actions. Trigger when the user wants to build a new action, define XML plist parameters, write Action scripts in Bash, AppleScript, or Python, locate and bind icons, or validate custom actions."
---
# Keyboard Maestro Actions Creator

Guidelines and templates for designing, implementing, and debugging custom Keyboard Maestro plug-in actions.

## Quick Start

1. **Create Action Folder**: Folder name must use ASCII alphanumerics, underscores, and spaces only.
2. **Define XML Parameter Plist**: Create `Keyboard Maestro Action.plist` describing parameters, script name, results, and titles.
3. **Write Script**: Create script file (e.g. `Action.sh` or `Action.scpt`) utilizing `KMPARAM_` environment variables.
4. **Acquire Icon**: Source a 64x64 PNG icon and name it `Icon.png`.
5. **Set Permissions**: Ensure action shell scripts are executable.
6. **Lint and Validate**: Run `plutil -lint` to check plist syntax.
7. **Reload Engine**: Force reload the Keyboard Maestro Engine to test.

---

## Action Structure

Every custom Keyboard Maestro action is a package directory stored in:
`/Users/rd/Library/Application Support/Keyboard Maestro/Keyboard Maestro Actions/[Action Name]/`

It must contain:
- `Keyboard Maestro Action.plist` - Cocoa XML property list defining parameters and title.
- `Action.sh` (or `Action.scpt`, `Action.py`) - The executable code.
- `Icon.png` - Standard 64x64 PNG icon.
- `README.md` - Inline documentation explaining parameters and use cases.

---

## Core Guidelines & Best Practices

### 1. XML Parameter Plist (`Keyboard Maestro Action.plist`)
- Case Sensitivity: XML keys are case-sensitive (e.g., `Name`, `Script`, `Icon`, `Parameters`, `Type`, `Default`, `Menu`).
- Type Support: Use `String`, `TokenString`, `Text`, `TokenText`, `Checkbox`, `Calculation`, `PopupMenu`, or `Hidden`.
- Token Parsing: Use `TokenString` or `TokenText` to resolve Keyboard Maestro tokens (e.g. `%Variable%VarName%`) before passing to the script.
- Return Formats: Define the `Results` string (e.g., `Variable|Clipboard|Window|Briefly|Typing|Pasting`) to specify output routing.
- Linting Constraint: Always validate using `plutil -lint "Keyboard Maestro Action.plist"` after writing/modifying.

### 2. Action Script Execution (`Action.sh`)
- Parameter Retrieval: Retrieve parameters via environment variables prefixed with `KMPARAM_` (e.g., parameter labeled `My Param` is passed as `KMPARAM_My_Param`).
- Spaces to Underscores: Ensure spaces in parameter labels are replaced with underscores in script references.
- Executability: Always set shell script permissions with `chmod +x Action.sh`.
- Multi-line Emojis & International Text: Use the `printenv` try-catch block inside AppleScript wrapper scripts for safe parsing.

### 3. Icon Assets
- Canonical Path: Sourced from `/Volumes/Apfspace/Icons/` and its subdirectories.
- Specification: Always copy the chosen icon to the action directory, resize to `64x64` PNG format, and rename to `Icon.png`.

### 4. Developer Reload Loop
Reload both editor and engine using AppleScript:
```applescript
tell application "Keyboard Maestro" to reload
tell application "Keyboard Maestro Engine" to reload
```

---

## Reference Implementations (Local Workspace)

Refer to existing actions in `/Users/rd/Library/Application Support/Keyboard Maestro/Keyboard Maestro Actions/` as precise design templates:

- **Path Extraction & Type Conversions**: 
  - See [Get Finder Path/Action.scpt](file:///Users/rd/Library/Application%20Support/Keyboard%20Maestro/Keyboard%20Maestro%20Actions/Get%20Finder%20Path/Action.scpt) for converting POSIX paths to HFS paths natively via Finder.
  - See [Get Finder Selection/Keyboard Maestro Action.plist](file:///Users/rd/Library/Application%20Support/Keyboard%20Maestro/Keyboard%20Maestro%20Actions/Get%20Finder%20Selection/Keyboard%20Maestro%20Action.plist) for defining `Return Type` (POSIX/HFS) and list formatting separators.
- **Handling Checkboxes & Shell Loops**:
  - See [Get Finder Selection Contents/Action.sh](file:///Users/rd/Library/Application%20Support/Keyboard%20Maestro/Keyboard%20Maestro%20Actions/Get%20Finder%20Selection%20Contents/Action.sh) for parsing multi-line standard input loops and reading checkboxes (`KMPARAM_Include_File_Names`).
- **Recursive Shell Utilities & CLI Wrappers**:
  - See [Get Finder Selection Tree/Action.sh](file:///Users/rd/Library/Application%20Support/Keyboard%20Maestro/Keyboard%20Maestro%20Actions/Get%20Finder%20Selection%20Tree/Action.sh) for using Brew-based CLI tools (`tree`) inside action scripts.
- **Complex Logic & Filtering Boundaries**:
  - See [Filter Finder Selection/Action.sh](file:///Users/rd/Library/Application%20Support/Keyboard%20Maestro/Keyboard%20Maestro%20Actions/Filter%20Finder%20Selection/Action.sh) for recursive traversing, regex name matching, date mod comparisons, and text-based file size evaluation.

---

## Additional Documentation

For full parameters schemas, details on AppleScript system attribute conversions, and step-by-step installation instructions, see [references/plugin-actions-docs.md](references/plugin-actions-docs.md).
