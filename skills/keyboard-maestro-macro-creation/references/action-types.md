# Keyboard Maestro Action Type XML References

## For (loop over FinderSelection)

Iterates each file selected in Finder. The variable value is accessible as `KMVAR_VarName` in nested shell scripts.

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
        <!-- nested actions, use ${KMVAR_SelectedFile:-} in shell scripts -->
    </array>
</dict>
```

## Repeat

Repeats nested actions a fixed number of times.

```xml
<dict>
    <key>MacroActionType</key>
    <string>Repeat</string>
    <key>CountExpression</key>
    <string>456</string>
    <key>Actions</key>
    <array>
        <!-- nested actions run N times -->
    </array>
</dict>
```

## SimulateKeystroke

Sends a key press to the frontmost (or targeted) app. **Modifier values differ from HotKey triggers:** 256=Cmd, 512=Shift, 1024=Option, 2048=Control.

```xml
<dict>
    <key>MacroActionType</key>
    <string>SimulateKeystroke</string>
    <key>KeyCode</key>
    <integer>36</integer>
    <key>Modifiers</key>
    <integer>0</integer>
    <key>TargetingType</key>
    <string>Front</string>
    <key>ReleaseAll</key>
    <false/>
</dict>
```

## ActivateApplication

Brings an app to front by bundle ID.

```xml
<dict>
    <key>MacroActionType</key>
    <string>ActivateApplication</string>
    <key>AllWindows</key>
    <true/>
    <key>Application</key>
    <dict>
        <key>BundleIdentifier</key>
        <string>com.amazon.Lassen</string>
        <key>Name</key>
        <string>Kindle</string>
        <key>NewFile</key>
        <string>/Applications/Amazon Kindle.app</string>
    </dict>
</dict>
```

## Pause

Waits for a duration in seconds before the next action.

```xml
<dict>
    <key>MacroActionType</key>
    <string>Pause</string>
    <key>Time</key>
    <string>1</string>
    <key>TimeOutAbortsMacro</key>
    <true/>
</dict>
```

## Open1File

Opens a file or application by path.

```xml
<dict>
    <key>MacroActionType</key>
    <string>Open1File</string>
    <key>Path</key>
    <string>/System/Applications/Calendar.app</string>
    <key>IsDefaultApplication</key>
    <true/>
</dict>
```

## InsertText (by pasting)

Types text (or token-expanded content) at the current cursor position.

```xml
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
```
