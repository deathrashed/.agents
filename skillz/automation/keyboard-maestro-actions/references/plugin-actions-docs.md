---
title: "Keyboard Maestro 6 Documentation: Plug In Actions"
description: "A description of how to create third party actions"
author:
source: "https://www.keyboardmaestro.com/documentation/6/pluginactions.html"
---
# Keyboard Maestro Documentation: Plug In Actions

## Plug In Actions

Keyboard Maestro adds support for user written and contributable plug in actions. You can get more plug in actions from the Keyboard Maestro web site and you can create and optionally contribute your own. You can drop a new plug in action.zip archive on the Keyboard Maestro application dock icon to install it (note that to update a plug in action you must manually remove it from the `~/Library/Application Support/Keyboard Maestro/Keyboard Maestro Actions` folder before re-installing it).

A Third Party Plug In Action consists of a folder with a name (which should generally closely match the action name), and must be made up of only ASCII alphanumerics, underscores and spaces. The folder name must be unique among all plug in actions. The folder name is stored in the Keyboard Maestro Macros.plist to reference the plugin action.

The folder contains a set of files, including:

- **Keyboard Maestro Action.plist** – an XML file describing the action.
- **A script file** whose name must be made up of only ASCII alphanumerics or underscores, plus an ASCII alphanumeric extension. It may be a shell script or an AppleScript. If it is a shell script, it will be made executable automatically.
- **An optional 64x64 png icon**.

The format of the Keyboard Maestro Action.plist is a Cocoa property list containing a dictionary with the following keys and values:

### Keyboard Maestro Action.plist Keys

- **Name**: the name of the action (which appears in the Category/Actions list)
- **Script**: the name of the script, made up of only ASCII alphanumerics or underscores, plus an ASCII alphanumeric extension.
- **Icon** [optional]: the name of the icon png file, made up of only ASCII alphanumerics or underscores plus `.png`.
- **Title** [optional]: the title displayed on the action, which can include `%Param%XYZ%` tokens. It should usually not include other tokens. If it is missing, the Name will be used.
- **Timeout** [optional number]: the default timeout in seconds. Set it to 0 if the action needs no timeout. The default is 99 hours.
- **Author** [optional]: the author of this action.
- **URL** [optional]: a URL for the author or this action.
- **Help** [optional]: a short (Tool Tip) explanation of this action.
- **HelpURL** [optional]: a URL for the Help link for the action (v11.0+)
- **Results** [optional]: what to do with the output of the script if any. Possible Values: `None`, `Window`, `Briefly`, `Large`, `Typing`, `Pasting`, `Variable`, `AppendVar`, `Clipboard`, `File`, `Asynchronously`. Multiple values can be used, separated by a bar (`|`), the first specified value is the default. If output is going to a clipboard or a file, the results can be an image.
- **Parameters** [optional]: an array of parameters to the script, each entry is a dictionary as described below.

### Parameter Keys

Each parameter in the `Parameters` array is a dictionary with the following keys:

- **Label**: the name of the parameter. The same rules as Keyboard Maestro Variable Names apply. The label is displayed to the user and used to pass the parameter to the script. Obviously, the label must be unique amongst all parameters.
- **Type**: the type of the parameter. Possible Values:
  - `String` (single line text)
  - `TokenString` (single line text with Keyboard Maestro token expansion)
  - `Calculation` (numeric or formula expression)
  - `Text` (multi-line text)
  - `TokenText` (multi-line text with Keyboard Maestro token expansion)
  - `Checkbox` (checkbox returning 0 or 1)
  - `PopupMenu` (dropdown menu selection, requires `Menu` key)
  - `Hidden` (token processed, but hidden from editor UI)
- **Default** [optional]: the default value when the action is created.
- **Menu** [required if Type is PopupMenu]: the values of the popup menu, separated by `|`.

> [!WARNING]
> XML Keys are case sensitive.

---

### Retrieving Parameters in a Script

Parameters are passed to the script via environment variables starting with `KMPARAM_`. Spaces in labels are replaced with underscores (`_`). 
*Example*: A parameter labeled `My Text` is retrieved from `KMPARAM_My_Text`.

#### AppleScript Parameter Retrieval Methods

```applescript
-- 1. Using "system attribute" (Fast, but NOT safe for international characters/emojis)
set myText to system attribute "KMPARAM_My_Text"

-- 2. Using Shell "echo" (Safe for emojis, but multi-line text is flattened to a single line)
set myText to do shell script "echo $KMPARAM_My_Text"

-- 3. Using Shell "printenv" (Safe for emojis, international chars, and multi-line formatting)
-- Note: printenv returns an error if the variable is unset, so wrap in a try block.
try
  set myText to do shell script "printenv KMPARAM_My_Text"
on error
  set myText to ""
end try
```

---

### Development Workflow

Once a plug-in is loaded, it remains in memory in both the Keyboard Maestro Editor and Engine. Changes to the `Keyboard Maestro Action.plist` will not be reflected immediately (though script edits will be). 

To force Keyboard Maestro to reload during development, run the following AppleScript:

```applescript
tell application "Keyboard Maestro" to reload
tell application "Keyboard Maestro Engine" to reload
```
