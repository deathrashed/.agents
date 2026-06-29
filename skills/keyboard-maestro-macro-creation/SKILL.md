---
name: keyboard-maestro-macro-creation
description: Creates, updates, and verifies Keyboard Maestro macros programmatically via AppleScript XML import.
version: 1.2.0
metadata:
  agent:
    tags:
      - keyboard-maestro
      - macro-automation
      - applescript
      - macos-automation
      - cross-app
    category: automation
    related_skills: []
    requires_toolsets:
      - terminal
      - files
    required_environment_variables: []
config: {}
---

## When to Use
- Use when creating a new Keyboard Maestro macro programmatically.
- Use when updating an existing macro's trigger, action, or token content.
- Use when moving macros between groups or verifying macro structure.
- Use when controlling another macOS app from KM via AppleScript.
- Do NOT use for macros that need GUI recording or manual editing in the Keyboard Maestro editor.

---

## Quick Reference

| Step | Action | Notes |
|------|--------|-------|
| 1 | Identify target group, generate UUIDs | Each macro and group needs a unique UUID |
| 2 | Assemble kmmacros XML | Wrapped in `<array><dict>` group format |
| 3 | Import via AppleScript | `importMacros` always creates a new group |
| 4 | Move macro to target group | `move m to end of macros of destGroup` |
| 5 | Verify trigger and action XML | Read back via `xml of first trigger/action` |

---

## Routing

- For action type XML examples (Repeat, SimulateKeystroke, ActivateApplication, Pause, Open1File, InsertText, For FinderSelection), see `references/action-types.md`.
- For the full list of KM tokens available in text fields, load `references/tokens.md`.
- For cross-app AppleScript control from KM (any app with an .sdef dictionary), see `references/cross-app-control.md`. Includes the TextSoap 9 API as a worked example.

---

## Procedure

### Step 1: Understand the XML format
Macros use plist XML. A kmmacros file wraps groups in an `<array>`:

- **Group:** `Name`, `UID`, `Macros` array, `Activate`
- **Macro:** `Name`, `UID`, `Triggers` array, `Actions` array, `CreationDate`, `ModificationDate`
- **HotKey trigger:** `MacroTriggerType` = "HotKey", `KeyCode` (integer), `Modifiers` (bitmask), `FireType` = "Pressed"
- **Action types:** Open1File, InsertText, ExecuteShellScript, For, Repeat, SimulateKeystroke, ActivateApplication, Pause — see `references/action-types.md`.

### Step 2: Generate UUIDs
`python3 -c "import uuid; print(str(uuid.uuid4()).upper())"`

### Step 3: Assemble the XML
Basic template:

```xml
<array>
    <dict>
        <key>Activate</key>
        <string>Normal</string>
        <key>Name</key>
        <string>ImportGroup</string>
        <key>UID</key>
        <string>{group-uuid}</string>
        <key>Macros</key>
        <array>
            <dict>
                <key>Name</key>
                <string>Macro Name</string>
                <key>UID</key>
                <string>{macro-uuid}</string>
                <key>CreationDate</key>
                <real>788799921.428457</real>
                <key>ModificationDate</key>
                <real>788799921.428457</real>
                <key>Triggers</key>
                <array>
                    <dict>
                        <key>MacroTriggerType</key>
                        <string>HotKey</string>
                        <key>KeyCode</key>
                        <integer>69</integer>
                        <key>Modifiers</key>
                        <integer>4096</integer>
                        <key>FireType</key>
                        <string>Pressed</string>
                    </dict>
                </array>
                <key>Actions</key>
                <array>
                    <dict>
                        <key>MacroActionType</key>
                        <string>InsertText</string>
                        <key>Action</key>
                        <string>ByPasting</string>
                        <key>ActionUID</key>
                        <integer>10001</integer>
                        <key>Text</key>
                        <string>%SystemClipboard%</string>
                    </dict>
                </array>
            </dict>
        </array>
    </dict>
</array>
```

**HotKey modifiers:** Control=4096, Command=256, Option=2048, Shift=8192. Combine by adding.  
**SimulateKeystroke modifiers (different):** 256=Cmd, 512=Shift, 1024=Option, 2048=Control.

**Common key codes:** Keypad_0=82, Keypad_Plus=69, F1=122, Return=36, Space=49, Escape=53, Tab=48, RightArrow=124, LeftArrow=123, Delete=51. Letters use macOS virtual codes (A=0, S=1, D=2, C=8, E=14, U=32).

### Step 3a: ExecuteShellScript — KMVAR_ variable rule
`%Variable%VarName%` tokens do NOT expand inside shell script text. Use `IncludedVariables: ["9999"]` and `KMVAR_VarName`:

```xml
<dict>
    <key>MacroActionType</key>
    <string>ExecuteShellScript</string>
    <key>Text</key>
    <string>#!/bin/zsh
file="${KMVAR_SelectedFile:-}"
/opt/homebrew/bin/qpdf ... "$file"</string>
    <key>UseText</key>
    <true/>
    <key>IncludedVariables</key>
    <array><string>9999</string></array>
</dict>
```

### Step 3b: For loop over FinderSelection
Pair with ExecuteShellScript using KMVAR_:

```xml
<dict>
    <key>MacroActionType</key>
    <string>For</string>
    <key>Variable</key>
    <string>SelectedFile</string>
    <key>Collections</key>
    <dict>
        <key>CollectionList</key>
        <array>
            <dict>
                <key>CollectionType</key>
                <string>FinderSelection</string>
            </dict>
        </array>
    </dict>
    <key>Actions</key>
    <array>
        <!-- nested action uses ${KMVAR_SelectedFile:-} -->
    </array>
</dict>
```

### Step 3c: KM tokens in text fields
`%SystemClipboard%` and other tokens expand in InsertText, SetVariableToText fields. See `references/tokens.md`. Use `%%` for a literal `%`.

### Step 3d: Cross-app AppleScript control
KM can control any macOS app with an .sdef file. The pattern is always:

**ExecuteShellScript → osascript → target app's commands**

Always test the AppleScript from Terminal before embedding in XML:

```bash
osascript -l AppleScript -e '
tell application "targetApp"
    commandName parameter with "option"
end tell
'
```

Clipboard-based pattern (select text anywhere, process, paste back):
```bash
#!/bin/zsh
osascript -e 'tell app "System Events" to keystroke "c" using command down'
sleep 0.2
osascript -l AppleScript -e '
tell application "targetApp"
    cleanClipboard with "Cleaner Name"
end tell
' 2>/dev/null
sleep 0.1
osascript -e 'tell app "System Events" to keystroke "v" using command down'
```

File-based pattern (FinderSelection + For loop):
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

For full details and the TextSoap 9 API reference, load `references/cross-app-control.md`.

### Step 4: Import via AppleScript
```applescript
tell application "Keyboard Maestro"
    set filePath to (POSIX file "/tmp/km_macro.kmmacros") as alias
    importMacros filePath
end tell
```

Via Python:
```python
r = subprocess.run(["osascript", "-e", script])
```

### Step 5: Move macro to an existing group
```applescript
tell application "Keyboard Maestro"
    set allMacros to every macro
    set target to missing value
    repeat with m in allMacros
        if name of m is "Macro Name" then
            set target to m
            exit repeat
        end if
    end repeat
    set destGroup to first macro group whose name is "target-group"
    move target to end of macros of destGroup
end tell
```

### Step 6: Update an existing macro's action
Set the `xml` property:
```applescript
tell application "Keyboard Maestro"
    set allMacros to every macro
    set target to missing value
    repeat with m in allMacros
        if name of m is "Macro Name" then
            set target to m
            exit repeat
        end if
    end repeat
    set newXML to "<?xml version=\"1.0\"..."
    set xml of first action of target to newXML
end tell
```

To escape shell script for AppleScript string: `text.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")`

---

## Pitfalls
- **Cannot use `make new trigger` or `make new action`:** Those classes lack the `make` command. Use `importMacros` or set `xml` property.
- **Cannot edit Macros.plist directly:** KM Engine holds a lock.
- **Duplicate macro names:** Iterate `every macro` and check properties.
- **importMacros creates new groups:** Use unique import group names, then move.
- **InsertText ByPasting needs text focus:** Precede with ActivateApplication.
- **`%Variable%VarName%` fails in ExecuteShellScript.** Use `"${KMVAR_VarName:-}"`.
- **Modifier values differ:** HotKey uses 4096/2048/256/8192. SimulateKeystroke uses 256/512/1024/2048.
- **PromptForUserInput missing:** Use inline osascript dialogs instead.
- **Cross-app AppleScript needs testing first:** Run the osascript command from Terminal before embedding in KM XML.
- **App must have an .sdef file:** Not all apps support AppleScript. Check with `find /Applications -name "*.sdef"`.

---

## Verification
- [ ] Import script exits code 0
- [ ] `xml of first trigger` shows correct key code and modifier
- [ ] `xml of first action` shows correct action type and parameters
- [ ] Macro appears in the intended group
- [ ] Hotkey trigger does not conflict with existing system or KM macros
- [ ] Cross-app AppleScript commands tested from Terminal before macro build
