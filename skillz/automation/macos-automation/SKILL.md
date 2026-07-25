---
name: macos-automation
description: Automate macOS tasks using AppleScript, shell scripts, Shortcuts, and system commands. Use when working with macOS automation, AppleScript, Finder operations, system preferences, app automation, file management, or macOS-specific workflows.
---

# macOS Automation Skill

This skill enables automation of macOS tasks using AppleScript, shell scripts, Shortcuts, and native macOS tools.

## Overview

macOS provides multiple automation options:
- **AppleScript** - Native automation language for macOS apps
- **Shell Scripts** - Bash/zsh scripts for command-line automation
- **Shortcuts** - Visual automation workflows
- **Automator** - GUI-based automation tool
- **osascript** - Command-line AppleScript execution
- **System commands** - Native macOS utilities

## AppleScript Basics

### Basic Structure

```applescript
tell application "Finder"
    -- Your commands here
end tell
```

### Common Applications

```applescript
-- Finder
tell application "Finder"
    set desktopPath to (path to desktop folder as string)
    set fileList to every file of desktopPath
end tell

-- System Events (for UI automation)
tell application "System Events"
    tell process "Finder"
        click menu item "New Folder" of menu "File" of menu bar 1
    end tell
end tell

-- Safari
tell application "Safari"
    set currentURL to URL of current tab of front window
end tell

-- Mail
tell application "Mail"
    set unreadCount to count of (every mailbox whose unread count > 0)
end tell
```

## File Operations

### Finder Operations

```applescript
tell application "Finder"
    -- Get desktop path
    set desktopPath to (path to desktop folder as string)
    
    -- List files
    set fileList to every file of desktopPath
    
    -- Create folder
    make new folder at desktopPath with properties {name:"New Folder"}
    
    -- Move file
    move file "source.txt" of desktopPath to folder "Documents" of home
    
    -- Get file info
    set fileSize to size of file "document.pdf" of desktopPath
    set modificationDate to modification date of file "document.pdf" of desktopPath
end tell
```

### Shell Script Integration

```applescript
-- Run shell command
set result to do shell script "ls -la ~/Documents"

-- With variables
set folderPath to POSIX path of (path to desktop folder)
set result to do shell script "ls -la " & quoted form of folderPath

-- With administrator privileges
do shell script "sudo systemsetup -setremotelogin on" with administrator privileges
```

## System Operations

### System Preferences

```applescript
tell application "System Preferences"
    activate
    set current pane to pane "com.apple.preference.security"
    reveal anchor "General" of pane "com.apple.preference.security"
end tell
```

### System Information

```applescript
-- Get system version
set systemVersion to system version of (system info)

-- Get computer name
set computerName to computer name of (system info)

-- Get user info
set userName to short user name of (system info)
set homePath to path to home folder as string
```

## App Automation

### Safari Automation

```applescript
tell application "Safari"
    activate
    set currentURL to URL of current tab of front window
    set pageTitle to name of current tab of front window
    
    -- Open new tab
    tell front window
        make new tab with properties {URL:"https://example.com"}
    end tell
    
    -- Get all tabs
    set tabURLs to URL of every tab of front window
end tell
```

### Mail Automation

```applescript
tell application "Mail"
    -- Get unread count
    set unreadCount to unread count of inbox
    
    -- Get unread messages
    set unreadMessages to (every message of inbox whose read status is false)
    
    -- Mark as read
    set read status of message 1 of inbox to true
end tell
```

## Shell Scripting for macOS

### Common macOS Commands

```bash
# System information
sw_vers                    # macOS version
system_profiler SPSoftwareDataType  # Detailed system info
scutil --get ComputerName  # Computer name

# File operations
mdfind "kMDItemKind == 'PDF'"  # Spotlight search
defaults read com.apple.finder  # Read preferences
defaults write com.apple.finder ShowPathbar -bool true  # Write preferences

# Network
networksetup -listallnetworkservices  # List network services
ifconfig                              # Network interfaces

# Processes
ps aux | grep "Application"  # Find processes
killall "Application Name"    # Kill process

# Permissions
chmod +x script.sh           # Make executable
chmod 755 script.sh          # Set permissions
```

### macOS-Specific Tools

```bash
# plutil - Property list utility
plutil -convert xml1 file.plist  # Convert binary plist to XML
plutil -p file.plist             # Print plist

# open - Open files/apps
open -a "Safari" "https://example.com"  # Open URL in Safari
open -a "TextEdit" file.txt             # Open file in app
open .                                  # Open current directory in Finder

# say - Text to speech
say "Hello, world"

# pbcopy/pbpaste - Clipboard
echo "text" | pbcopy    # Copy to clipboard
pbpaste                 # Paste from clipboard

# osascript - Run AppleScript from command line
osascript -e 'tell app "Finder" to display dialog "Hello"'
```

## Shortcuts Integration

### Running Shortcuts from Scripts

```bash
# Run shortcut by name
shortcuts run "My Shortcut"

# Run shortcut with input
echo "input text" | shortcuts run "Process Text"
```

### Creating Shortcuts Programmatically

Shortcuts can be created via:
- Shortcuts app (GUI)
- Shortcuts CLI (`shortcuts` command)
- AppleScript automation

## Error Handling

```applescript
try
    tell application "Finder"
        set fileList to every file of desktop folder
    end tell
on error errorMessage number errorNumber
    display dialog "Error: " & errorMessage
end try
```

## Best Practices

1. **Use try/on error** for robust scripts
2. **Check if app is running** before automation:
   ```applescript
   if application "Safari" is running then
       tell application "Safari"
           -- commands
       end tell
   end if
   ```
3. **Use POSIX paths** when working with shell commands
4. **Request permissions** for accessibility features
5. **Test incrementally** - build scripts step by step

## Common Use Cases

### File Organization
- Organize downloads folder
- Sort files by type/date
- Clean up desktop
- Archive old files

### App Automation
- Control media playback
- Manage browser tabs
- Process emails
- Batch rename files

### System Maintenance
- Check disk space
- Monitor system resources
- Update system preferences
- Manage network settings

### Workflow Automation
- Morning routine automation
- File backup scripts
- Email processing
- Calendar management

## Resources

- [AppleScript Language Guide](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/)
- [Mac Automation Scripting Guide](https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/)
- [Shell Scripting on macOS](https://developer.apple.com/library/archive/documentation/OpenSource/Conceptual/ShellScripting/)
- [Shortcuts User Guide](https://support.apple.com/guide/shortcuts-mac/)

## Examples

### Example 1: Organize Downloads

```applescript
tell application "Finder"
    set downloadsFolder to folder "Downloads" of home
    set fileList to every file of downloadsFolder
    
    repeat with aFile in fileList
        set fileExtension to name extension of aFile
        set targetFolder to folder fileExtension of downloadsFolder
        
        try
            if not (exists targetFolder) then
                make new folder at downloadsFolder with properties {name:fileExtension}
            end if
            move aFile to targetFolder
        end try
    end repeat
end tell
```

### Example 2: Get System Info

```bash
#!/bin/bash
echo "macOS Version: $(sw_vers -productVersion)"
echo "Computer Name: $(scutil --get ComputerName)"
echo "User: $(whoami)"
echo "Home: $HOME"
```

### Example 3: Batch Rename Files

```applescript
tell application "Finder"
    set targetFolder to choose folder
    set fileList to every file of targetFolder
    
    repeat with i from 1 to count of fileList
        set currentFile to item i of fileList
        set oldName to name of currentFile
        set newName to "File " & i & "." & (name extension of currentFile)
        set name of currentFile to newName
    end repeat
end tell
```
