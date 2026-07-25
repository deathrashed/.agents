# Controlling Other Apps from Keyboard Maestro

## Table of Contents
- [Overview](#overview)
- [How to Find an App's AppleScript Dictionary](#how-to-find-an-apps-applescript-dictionary)
- [Test Before Building the Macro](#test-before-building-the-macro)
- [Two Integration Patterns](#two-integration-patterns)
- [Worked Example: TextSoap 9](#worked-example-textsoap-9)
- [Tips](#tips)

---

## Overview

Any macOS app with an AppleScript dictionary (`.sdef` file) can be controlled from a KM macro. The universal pattern:

**KM ExecuteShellScript → `osascript` → target app's AppleScript commands**

No KM plugin or special action type is needed. All inter-app communication happens through the shell script's `osascript` call.

## How to Find an App's AppleScript Dictionary

```bash
# Find the .sdef file for any app
find /Applications -name "*.sdef" 2>/dev/null | grep -i appname

# Read it
cat /path/to/App.sdef
```

The `.sdef` XML lists every command, parameter, and class the app exposes.

## Test Before Building the Macro

Always verify the AppleScript commands work from Terminal before wiring them into XML:

```bash
osascript -l AppleScript -e '
tell application "targetApp"
    commandName parameter with "option"
end tell
'
```

## Two Integration Patterns

### Pattern A: Clipboard-based (select, copy, process, paste)

Best for processing selected text in any app. Single ExecuteShellScript action.

```bash
#!/bin/zsh
# Step 1: Copy selection
osascript -e 'tell app "System Events" to keystroke "c" using command down'
sleep 0.2

# Step 2: Process clipboard via target app
osascript -l AppleScript -e '
tell application "targetApp"
    cleanClipboard with "Some Cleaner"
end tell
' 2>/dev/null
sleep 0.1

# Step 3: Paste result back
osascript -e 'tell app "System Events" to keystroke "v" using command down'
```

### Pattern B: File-based (FinderSelection, For loop, osascript)

Best for processing selected files in Finder. Pair with the For loop.

```bash
#!/bin/zsh
file="${KMVAR_SelectedFile:-}"
[[ -z "$file" ]] && exit 0

osascript -l AppleScript -e '
tell application "targetApp"
    cleanFile (POSIX file "'"$file"'") with "Cleaner Name"
end tell
'
```

---

## Worked Example: TextSoap 9

TextSoap 9 at `/Applications/textsoap9.app`, dictionary at `/Applications/textsoap9.app/Contents/Resources/AppScripting.sdef`.

### Commands

| Command | Signature | Description |
|---------|-----------|-------------|
| `cleanText` | `cleanText "input" with "Cleaner"` | Returns cleaned text (no side effects) |
| `cleanClipboard` | `cleanClipboard with "Cleaner"` | Cleans system clipboard in place |
| `cleanFile` | `cleanFile fileRef with "Cleaner"` | Processes a file, writes to same path |
| `cleanFile` (ext) | `cleanFile fileRef with "Cleaner" destFolder "path"` | Output to different folder |
| `cleanFile` (enc) | `... readEncoding "utf-8" writeEncoding "utf-8"` | Specify encodings |
| `pickCleaner` | `pickCleaner` | Dialog to choose cleaner, returns name |
| `groupNames` | `groupNames limit to "all"` | Lists cleaner groups |
| `groupItems` | `groupItems from "Group Name"` | Lists cleaners in a group |
| `tokenizeCleanerName` | `tokenizeCleanerName "Name"` | Human name to internal token |
| `textualizeCleanerToken` | `textualizeCleanerToken "token"` | Token to human name |
| `cleanPasteboard` | `cleanPasteboard "board" with "Cleaner"` | Clean specific pasteboard |
| `makePlainPasteboard` | `makePlainPasteboard` | Strip style from clipboard |

### Cleaner Names (Standard group)

Scrub, MyScrub, Remove Extra Spaces, Remove Forwarding (>) Characters, Remove All Tabs, Make Paragraphs, Remove Extra Returns, Uppercase, Lowercase, Capitalize Sentences, Capitalize with Title Case, Capitalize Words, Capitalize Common Tech Names, Straighten Quotes, Smarten Quotes, Extract Text from HTML Source, Rewrap Text, Quote Text, Internet Friendly Text

### Testing from Terminal

```bash
# Test a cleaner on a string
osascript -l AppleScript -e '
tell application "textsoap9"
    cleanText "Hello   World" with "Remove Extra Spaces"
end tell
'

# List all cleaner groups
osascript -l AppleScript -e '
tell application "textsoap9"
    groupNames limit to "all"
end tell
'

# List cleaners in a group
osascript -l AppleScript -e '
tell application "textsoap9"
    groupItems from "Standard"
end tell
'
```

## Tips

- Use `2>/dev/null` to suppress osascript errors when the app is not yet running. KM auto-launches it.
- Always test AppleScript from Terminal first before embedding in kmmacros XML.
- The `sleep` calls prevent race conditions with the system pasteboard on clipboard-based patterns.
- For apps that need to be frontmost, use `activate` in AppleScript or KM's ActivateApplication first.
