# Keyboard Maestro XML Schema Guide

## The Historical Context: Why LLMs Fail at KM Macros

For years, chatbots could not create importable Keyboard Maestro macros. The breakthrough from a KM forum post revealed why: LLMs generate what a response "would look like" rather than the correct undocumented schema. 
* Original forum post proving the fix: https://forum.keyboardmaestro.com/t/chatgpt-built-a-working-exportable-macro-that-imported-to-keyboard-maestro-without-errors/49936

LLMs hallucinate KM's internal XML schema because:
1. KM uses a complex, undocumented binary/XML plist structure.
2. No public schema is available for training data.
3. UI names differ significantly from internal `MacroActionType` names (e.g., `Execute Shell Script` in the UI is `ExecuteShellScript` in XML).
4. Small typos in keys cause complete, silent import failures. A file can pass `plutil -lint` (which only checks valid plist formatting) and still completely fail to import into Keyboard Maestro.

**The Solution:** You MUST show the LLM real exports first. Analyze real exports, copy working patterns, and distinguish between the stable outer wrapper and schema-sensitive action blocks.

## Anatomy of a .kmmacros File

### 1. Root Structure (Always Array)
A `.kmmacros` file must ALWAYS have an `<array>` at the root, containing `<dict>` objects for the macro groups.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<array>
    <dict>
        <!-- Macro Group Starts Here -->
        <key>Activate</key><string>Normal</string>
        <key>Macros</key><array>
            <dict>
                <!-- Macro Starts Here -->
                <key>Actions</key><array>
                    <!-- Actions Here -->
                </array>
                <key>Name</key><string>My Macro Name</string>
                <key>Triggers</key><array>
                    <dict><key>MacroTriggerType</key><string>StatusMenu</string></dict>
                </array>
                <key>UID</key><string>UNIQUE-MACRO-ID-HERE</string>
            </dict>
        </array>
        <key>Name</key><string>Global Macro Group</string>
        <key>UID</key><string>UNIQUE-GROUP-ID-HERE</string>
    </dict>
</array>
</plist>
```

### 2. Required Keys
**Group Level:** `Activate`, `Macros` (array), `Name`, `UID`
**Macro Level:** `Actions` (array), `Name`, `Triggers` (array), `UID`

### 3. Action Structure
Every single action MUST have:
- `ActionUID` - A completely unique integer (e.g., 1001, 1002).
- `MacroActionType` - The KM internal action name (e.g., `ExecuteShellScript`, `SetVariableToText`).

## Safe and Unsafe Examples

**SAFE to use as a hand-written guide:**
- Root plist structure
- Group-level and Macro-level keys
- Simple status menu trigger shape
- `SetVariableToText` and `SetClipboardToText` (these are simple enough to template).

**UNSAFE to use as authoritative (MUST CLONE FROM `assets/real-exports/`):**
- `ExecuteShellScript`
- `PromptForUserInput`
- `ActivateApplication`
- `SimulateKeystroke`
- `IfThenElse` / `Switch` / `TryCatch`

For unsafe actions, you must copy the action dictionary from a real export and modify ONLY the payload (like the script text or variable name). DO NOT invent the dictionary structure.

## Common Mistakes to Avoid

| Mistake | Fix |
|---------|-----|
| Using `<dict>` at root | Use `<array>` at root |
| Missing `MacroActionType` | Every action needs this exact key |
| Guessing action names | Run `scripts/find-action.sh` to find real exports |
| Missing `ActionUID` | Give each action a unique integer |
| Forgetting `<key>` tags | Every key needs `<key>` tag |
| Wrong variable syntax | Use `%Variable%Name%` format |

## Validation Commands

```bash
# Validate plist syntax
plutil -lint Macro.kmmacros

# Convert to XML for viewing
plutil -convert xml1 Macro.kmmacros -o - | less

# Validate the entire skill package
scripts/validate-skill.sh
```

Remember: passing `plutil -lint` means "well-formed plist", not "safe to import in Keyboard Maestro".
