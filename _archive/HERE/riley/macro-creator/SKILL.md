---
name: macro-creator
description: Use when creating or fixing Keyboard Maestro .kmmacros files, especially when import errors or schema uncertainty mean the macro must be grounded in real exports instead of guessed XML.
trigger: kmmacros, keyboard maestro macro, km macro
---

# Keyboard Maestro Macro Creator Skill

## When Invoked

Use this skill when asked to:
- Create Keyboard Maestro macros
- Edit .kmmacros files
- Fix import errors in KM macros
- Add actions to existing macros

## The Solution

The core challenge identified in the Keyboard Maestro (KM) forum is that **LLMs fail to generate valid XML** because there is no public schema, and the internal action names often differ from what you see in the UI.

### The Fix

To overcome this, you must analyze authentic exports. We’ve archived real examples in three formats at the following paths:

- **.kmmacros**: `/Users/rd/.config/keyboard-maestro/macros/kmmacros/Data`
- **.xml**: `/Users/rd/.config/keyboard-maestro/macros/xml/Data`
- **.json**: `/Users/rd/.config/keyboard-maestro/macros/json/Data`

### Implementation Strategy

1. **Prioritize .kmmacros**`.kmmacros`: This is the only functional format for imports; the others serve strictly as reference material.
2. **Native Actions First**: Maximize the use of native Keyboard Maestro actions rather than relying on a single monolithic `ExecuteShellScript` or `ExecuteAppleScript` action to do all the work. Native actions are more efficient, easier to debug, and fit the KM paradigm better. Only use scripts for logic that is impossible or highly impractical with native actions. **Check `references/ACTIONS.md` for a comprehensive list of all available 96+ native actions** (e.g., `IfThenElse`, `Switch`, `SearchReplace`, `SetVariableToText`, `PromptForUserInput`, `For`, `While`, `ReadFile`, etc.), and use `scripts/find-action.sh` to see how they are structured.
3. **Pattern Matching**: Model your generated code after the syntax found in these working files.
4. **Validation**: Always verify your output using the command: `plutil -lint`.

## Construction Rule

Use a two-level approach:

1. Hand-template only the stable outer wrapper:
   - root `<array>`
   - macro group
   - macro dict
   - simple `StatusMenu` trigger
2. Clone real exported action blocks for schema-sensitive actions.

Never hand-author complex action bodies when you have a real export available.

## Always Validate

```bash
plutil -lint your-macro.kmmacros
```

If validation fails:
- Root must be `<array>`, not `<dict>`
- Use real export structure
- Check all keys are correct

Important: `plutil -lint` checks plist syntax only. It does not prove KM will import the file.

For the whole skill package, run:

```bash
scripts/validate-skill.sh
```

## Available Examples

The working macros are in this folder:
- `examples/text-case.kmmacros` - Uppercase clipboard
- `examples/extract-links.kmmacros` - Extract URLs
- `examples/sort-lines.kmmacros` - Sort + unique lines
- `examples/count-lines.kmmacros` - Count lines

See references:
- `references/MACRO-STRUCTURE.txt` - Template
- `references/ACTIONS.md` - Action names
- `references/ACTION-SOURCING.md` - where to clone common action blocks from

## How to Create

1. List the required actions by `MacroActionType`.
2. For each action, run `scripts/find-action.sh MacroActionType`.
3. Read `references/ACTION-SOURCING.md` and choose the closest real export.
4. Copy full action dictionaries for any schema-sensitive action.
5. Modify payload fields only.
6. Generate fresh UUIDs for macro/group `UID` values.
7. Generate unique integer `ActionUID` values within each macro.
8. Validate plist syntax with `plutil -lint`.
9. Compare action shape with the source export before claiming success.
10. State verification level: plist validated, manual import confirmed, or behavior confirmed.

## Documentation

See skill folder:
- `README.md` - Quick start and layout
- `docs/MACRO-GUIDE.md` - Full guide
- `docs/TROUBLESHOOTING.md` - Process notes
- `docs/TLDR.md` - Short reference
- `templates/status-menu-wrapper.xml` - safe wrapper only; add cloned actions
- `scripts/find-action.sh` - locate real exports containing an action type
- `scripts/validate-skill.sh` - validate bundled examples and doc references

### Official Wiki Documentation
When you need to understand the syntax or behavior of Keyboard Maestro primitives, refer to these official wiki pages. Use a web fetching tool to read them:
- **Actions:** https://wiki.keyboardmaestro.com/manual/Macro_Actions
- **Variables:** https://wiki.keyboardmaestro.com/manual/Variables
- **Tokens:** https://wiki.keyboardmaestro.com/manual/Tokens
- **Calculations:** https://wiki.keyboardmaestro.com/manual/Calculations
- **Conditions:** https://wiki.keyboardmaestro.com/manual/Conditions
- **Collections:** https://wiki.keyboardmaestro.com/manual/Collections
- **Dictionaries:** https://wiki.keyboardmaestro.com/manual/Dictionaries
- **JSON:** https://wiki.keyboardmaestro.com/manual/JSON
- **Filters:** https://wiki.keyboardmaestro.com/manual/Filters
- **Triggers:** https://wiki.keyboardmaestro.com/manual/Macro_Triggers

## Anti-Patterns

DON'T:
- Generate from "knowledge"
- Guess action names
- Fall back to monolithic shell/AppleScript actions when native KM actions can achieve the same result
- Skip validation
- Assume structure is simple
- Use simplified shell/prompt/keystroke/app-activation examples as authoritative
