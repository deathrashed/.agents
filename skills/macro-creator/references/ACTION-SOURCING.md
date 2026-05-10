# Keyboard Maestro Action Sourcing Map

Use this file before creating or editing action dictionaries. The rule is simple: find a real export with the action, clone the full action dictionary, and edit only the payload fields that are safe for the requested macro.

Run:

```bash
scripts/find-action.sh MacroActionType
```

## Canonical Sources

| Action Type | First Source To Check | Safe Fields To Edit | Do Not Touch Without Another Export |
|---|---|---|---|
| `ExecuteShellScript` | `assets/real-exports/text-transformer.kmmacros`, then `assets/real-exports/backup-macros.kmmacros` | Script text, shell path when the source action already has one | result handling shape, timeout fields, execution mode fields |
| `ExecuteAppleScript` | `assets/real-exports/text-transformer.kmmacros`, then `assets/real-exports/backup-macros.kmmacros` | AppleScript source text | execution/result keys not relevant to the payload |
| `PromptForUserInput` | `assets/real-exports/calculate.kmmacros`, then `assets/real-exports/text-transformer.kmmacros` | title, prompt text, variable names/defaults while preserving each variable dict shape | `Variables` array structure, button/result behavior |
| `SetVariableToText` | `assets/examples/text-case.kmmacros`, then `assets/real-exports/text-transformer.kmmacros` | `Variable`, `Text` | action type spelling, action wrapper keys |
| `SetVariableToCalculation` | `assets/real-exports/calculate.kmmacros` | variable name, calculation expression | calculation action shape |
| `SetClipboardToText` | `assets/examples/text-case.kmmacros`, then `assets/real-exports/clipboard-history.kmmacros` | `Text` | clipboard action structure |
| `ClipboardHistorySwitcher` | `assets/real-exports/clipboard-history.kmmacros` | display/paste options only if present in source | switcher-specific keys |
| `PasteByName` | `assets/real-exports/clipboard-history.kmmacros` | named clipboard reference | action shape |
| `OCRImage` | `assets/real-exports/ocr-clipboard-image.kmmacros` | image source/output variable fields that already exist | OCR option structure |
| `IfThenElse` | `assets/real-exports/backup-macros.kmmacros`, then `assets/real-exports/text-transformer.kmmacros` | condition values, variable names, nested cloned actions | condition dict shape, `ThenActions`/`ElseActions` layout |
| `Switch` | `assets/real-exports/text-transformer.kmmacros` | case values and nested cloned actions | case array structure |
| `For`, `While`, `Repeat`, `Until` | `assets/real-exports/backup-macros.kmmacros` | loop variable/value fields | nested loop schema |
| `TryCatch` | `assets/real-exports/backup-macros.kmmacros` | nested cloned actions | error handling layout |
| `ExecuteSubroutine` | `assets/real-exports/backup-macros.kmmacros` | subroutine macro name/UID fields when present | parameter structure |
| `Semaphore` | `assets/real-exports/backup-macros.kmmacros` | semaphore name | locking/action layout |
| `SimulateKeystroke` | `assets/real-exports/insert-text-into-restricted-field.kmmacros` | key and modifier values only | keystroke dictionary shape |
| `InsertText` | `assets/real-exports/insert-text-into-restricted-field.kmmacros` | inserted text | insertion mode fields |
| `ActivateApplication` | run `scripts/find-action.sh ActivateApplication` and use the closest export | application name/path fields | activation flags |
| `SelectMenuItem` | run `scripts/find-action.sh SelectMenuItem` and use the closest export | menu path values | menu item dict shape |
| `MouseMoveAndClick` | run `scripts/find-action.sh MouseMoveAndClick` and use the closest export | coordinates/button values | coordinate mode and click structure |
| `OpenURL` | `assets/real-exports/tinyurl.kmmacros` | URL string or variable token | URL action shape |
| `Notification`, `Alert`, `Display` | run `scripts/find-action.sh Notification`, `Alert`, or `Display` | title/body text | display/action option keys |
| `File`, `ReadFile`, `WriteFile`, `Open1File` | `assets/real-exports/backup-macros.kmmacros` | paths, variable names, file text | file action mode fields |
| `ShowPaletteOfMacros` | `assets/real-exports/symbols.kmmacros` | [Auto-indexed] | check schema carefully |
| `GetFileAttribute` | `assets/examples/Find Latest File.kmmacros` | [Auto-indexed] | check schema carefully |
| `SearchReplace` | `assets/examples/Add 5 Seconds to to HH-MM-SS time.kmmacros` | [Auto-indexed] | check schema carefully |
| `SetKeychainPasswordToText` | `assets/examples/Password Store.kmmacros` | [Auto-indexed] | check schema carefully |
| `SearchRegEx` | `assets/examples/Fix 12 Hour Date in 24 Hour Locales.kmmacros` | [Auto-indexed] | check schema carefully |
| `DrawImage` | `assets/examples/Draw a Face.kmmacros` | [Auto-indexed] | check schema carefully |
| `NewImage` | `assets/examples/Draw a Face.kmmacros` | [Auto-indexed] | check schema carefully |
| `DisplayImage` | `assets/examples/Draw a Face.kmmacros` | [Auto-indexed] | check schema carefully |
| `Pause` | `assets/examples/Finder Selection Bug.kmmacros` | [Auto-indexed] | check schema carefully |
| `Cancel` | `assets/examples/Find Matching File.kmmacros` | [Auto-indexed] | check schema carefully |
| `Filter` | `assets/examples/Fix TWo 2.kmmacros` | [Auto-indexed] | check schema carefully |
| `HiliteLocation` | `assets/examples/Highlight Mouse.kmmacros` | [Auto-indexed] | check schema carefully |
| `SetSafariFieldToText` | `assets/examples/Web Login With Keychain.kmmacros` | [Auto-indexed] | check schema carefully |
| `SetVariableToKeychainPassword` | `assets/examples/Web Login With Keychain.kmmacros` | [Auto-indexed] | check schema carefully |
| `SafariControl` | `assets/examples/Web Login With Keychain.kmmacros` | [Auto-indexed] | check schema carefully |
| `ApplyStyle` | `assets/examples/Display Large Text.kmmacros` | [Auto-indexed] | check schema carefully |
| `ResizeImage` | `assets/examples/Resize Selected Images.kmmacros` | [Auto-indexed] | check schema carefully |
| `QuitSpecificApp` | `assets/examples/Finder Show Hidden Files.kmmacros` | [Auto-indexed] | check schema carefully |
| `PauseUntil` | `assets/examples/Insert Numbered List.kmmacros` | [Auto-indexed] | check schema carefully |
| `ExecuteJavaScript` | `assets/examples/Get Multiple Results from Execute JavaScript.kmmacros` | [Auto-indexed] | check schema carefully |
| `SetActionDelay` | `assets/examples/Set Action Delay Example.kmmacros` | [Auto-indexed] | check schema carefully |
| `SetNetworkLocation` | `assets/examples/Set Network Location to Work.kmmacros` | [Auto-indexed] | check schema carefully |
| `GetImageSize` | `assets/examples/Resize Proportionately.kmmacros` | [Auto-indexed] | check schema carefully |
| `Substring` | `assets/examples/Create Link.kmmacros` | [Auto-indexed] | check schema carefully |
| `PlugIn` | `assets/examples/Set Finder Files Labeled Red.kmmacros` | [Auto-indexed] | check schema carefully |
| `Comment` | `assets/examples/Print to PDF in Mail.kmmacros` | [Auto-indexed] | check schema carefully |
| `ScreenCapture` | `assets/examples/Save screenshot if notification pops up.kmmacros` | [Auto-indexed] | check schema carefully |
| `Log` | `assets/examples/Find Last Added.kmmacros` | [Auto-indexed] | check schema carefully |
| `SpeakText` | `assets/examples/Timer via Trigger Macro by Name .kmmacros` | [Auto-indexed] | check schema carefully |
| `ManipulateWindow` | `assets/examples/Move Window while Command Key is Down.kmmacros` | [Auto-indexed] | check schema carefully |
| `SetFileAttribute` | `assets/examples/Tag Selected Files Red.kmmacros` | [Auto-indexed] | check schema carefully |
| `NewFolder` | `assets/examples/Periodic Screenshots.kmmacros` | [Auto-indexed] | check schema carefully |
| `PlaySound` | `assets/examples/Variable Repeat.kmmacros` | [Auto-indexed] | check schema carefully |
| `CutCopyPaste` | `assets/examples/com.literatureandlatte.scrivener3.kmmacros` | [Auto-indexed] | check schema carefully |
| `ExecuteJavaScriptForAutomation` | `assets/examples/com.apple.Notes.kmmacros` | [Auto-indexed] | check schema carefully |
| `Group` | `assets/examples/com.toketaware.ithoughtsx.kmmacros` | [Auto-indexed] | check schema carefully |
| `DeletePastClipboard` | `assets/examples/com.cocoatech.PathFinder.kmmacros` | [Auto-indexed] | check schema carefully |
| `ExecuteMacro` | `assets/examples/tasks | 10 Assemble backup report.kmmacros` | [Auto-indexed] | check schema carefully |
| `SplitPath` | `assets/examples/subs | 10 Settings manager.kmmacros` | [Auto-indexed] | check schema carefully |
| `SetNextEngineWindow` | `assets/examples/subs | 10 Settings manager.kmmacros` | [Auto-indexed] | check schema carefully |
| `PromptForFile` | `assets/examples/subs | 10 Settings manager.kmmacros` | [Auto-indexed] | check schema carefully |
| `PromptWithList` | `assets/examples/subs | 10 Settings manager.kmmacros` | [Auto-indexed] | check schema carefully |
| `SetMacroEnable` | `assets/examples/subs | 01 First run of version.kmmacros` | [Auto-indexed] | check schema carefully |
| `DisplayProgress` | `assets/examples/tasks | 04 Analyze backups.kmmacros` | [Auto-indexed] | check schema carefully |
| `Return` | `assets/examples/dbase | 10 Run database action.kmmacros` | [Auto-indexed] | check schema carefully |
| `HideSpecificApp` | `assets/examples/•main | MacroBackerUpper.kmmacros` | [Auto-indexed] | check schema carefully |
| `ExecuteJavaScriptForCustomPrompt` | `assets/examples/•main | MacroBackerUpper.kmmacros` | [Auto-indexed] | check schema carefully |
| `CustomPrompt` | `assets/examples/•main | MacroBackerUpper.kmmacros` | [Auto-indexed] | check schema carefully |
| `OpenFinderSelection` | `assets/examples/Open Video In VLC or Quicktime.kmmacros` | [Auto-indexed] | check schema carefully |
| `PressButton` | `assets/examples/Save image as....kmmacros` | [Auto-indexed] | check schema carefully |
| `iTunesControl` | `assets/examples/Play music .kmmacros` | [Auto-indexed] | check schema carefully |
| `ClipboardSwitcherMacroAction` | `assets/examples/Select Next Word.kmmacros` | [Auto-indexed] | check schema carefully |
| `MailSendMessage` | `assets/examples/Send Boss Daily Image.kmmacros` | [Auto-indexed] | check schema carefully |
| `SwitchToLastApplication` | `assets/examples/Paste Selection Into Last Application.kmmacros` | [Auto-indexed] | check schema carefully |
| `HideCurrent` | `assets/examples/Hide Front Application.kmmacros` | [Auto-indexed] | check schema carefully |
| `SwitchToNextApplication` | `assets/examples/Activate Next Application.kmmacros` | [Auto-indexed] | check schema carefully |
| `SystemAction` | `assets/examples/5 Time of Day.kmmacros` | [Auto-indexed] | check schema carefully |
| `DarkMode` | `assets/examples/22 Wake.kmmacros` | [Auto-indexed] | check schema carefully |
| `QuitAll` | `assets/examples/23 Sleep.kmmacros` | [Auto-indexed] | check schema carefully |
| `SystemVolume` | `assets/examples/20 Unlock.kmmacros` | [Auto-indexed] | check schema carefully |
| `SendMIDIMessage` | `assets/examples/28 MIDI.kmmacros` | [Auto-indexed] | check schema carefully |
| `SetFileIcon` | `assets/examples/- Set Icon of Selected Items.kmmacros` | [Auto-indexed] | check schema carefully |
| `UseVariable` | `assets/examples/Paste Back from Default Text Editor.kmmacros` | [Auto-indexed] | check schema carefully |
| `MacroGroupToggle` | `assets/examples/- Global Macros -.kmmacros` | [Auto-indexed] | check schema carefully |
| `QuickMacro` | `assets/examples/Quick Macro for ⌥F1.kmmacros` | [Auto-indexed] | check schema carefully |
| `PromptForRect` | `assets/examples/OCR Screen.kmmacros` | [Auto-indexed] | check schema carefully |
| `HideOthers` | `assets/examples/Finder & Hide Others.kmmacros` | [Auto-indexed] | check schema carefully |
| `Search` | `assets/examples/Google Image Search.kmmacros` | [Auto-indexed] | check schema carefully |
| `TriggerByName` | `assets/examples/Search Macros.kmmacros` | [Auto-indexed] | check schema carefully |
| `HideAll` | `assets/examples/Hide All .kmmacros` | [Auto-indexed] | check schema carefully |
| `ExecuteShortcut` | `assets/examples/AI Dictation.kmmacros` | [Auto-indexed] | check schema carefully |
| `DebuggerAction` | `assets/examples/User Input Creates Collection of Folders.kmmacros` | [Auto-indexed] | check schema carefully |
| `ShowAll` | `assets/examples/- Apps Palette -.kmmacros` | [Auto-indexed] | check schema carefully |
| `ApplicationsPaletteToggle` | `assets/examples/- Apps Palette -.kmmacros` | [Auto-indexed] | check schema carefully |
| `SimulateHardwareKey` | `assets/examples/QuickTime Actions.kmmacros` | [Auto-indexed] | check schema carefully |
| `QuickTimePlayerControl` | `assets/examples/QuickTime Actions.kmmacros` | [Auto-indexed] | check schema carefully |
| `ScrollWheelEvent` | `assets/examples/Mouse Control.kmmacros` | [Auto-indexed] | check schema carefully |
| `SimulateModifiers` | `assets/examples/Interface Control Actions.kmmacros` | [Auto-indexed] | check schema carefully |
| `CopyClipboard` | `assets/examples/( ).kmmacros` | [Auto-indexed] | check schema carefully |
| `SetDictionaryToJSON` | `assets/examples/Insert Text Into Restricted Field.kmmacros` | [Auto-indexed] | check schema carefully |
| `SetDictionaryValue` | `assets/examples/Insert Text Into Restricted Field.kmmacros` | [Auto-indexed] | check schema carefully |
| `ClipboardSwitcherPaste` | `assets/examples/Insert Text Into Restricted Field.kmmacros` | [Auto-indexed] | check schema carefully |
| `SetClipboardToImage` | `assets/examples/Icon Manager.kmmacros` | [Auto-indexed] | check schema carefully |
| `ApplicationLauncher` | `assets/examples/Activate Application Launcher.kmmacros` | [Auto-indexed] | check schema carefully |
| `ProgramSwitcher` | `assets/examples/Activate Application Switcher.kmmacros` | [Auto-indexed] | check schema carefully |
| `WindowSwitcher` | `assets/examples/Activate Window Switcher.kmmacros` | [Auto-indexed] | check schema carefully |
| `TransformImage` | `assets/examples/Rotate 180°.kmmacros` | [Auto-indexed] | check schema carefully |
| `SetClipboardToPastClipboard` | `assets/examples/Paste Previous Clipboard.kmmacros` | [Auto-indexed] | check schema carefully |

## If The Action Is Not Listed

1. Run `scripts/find-action.sh ActionType`.
2. Prefer `assets/real-exports/` over `assets/examples/` for schema-sensitive actions.
3. If no local export exists, create a tiny Keyboard Maestro macro with only that action and export it.
4. Add the new export or a note here after it imports successfully.

## Completion Standard

When delivering a macro, say exactly which level was verified:

- `plist validated`: `plutil -lint` passed only.
- `manual import confirmed`: Keyboard Maestro imported the file.
- `behavior confirmed`: The macro imported and was run successfully.
