---
name: shell-to-lua
description: Use when converting a shell script, Python script, AppleScript, or Keyboard Maestro workflow into a standalone Lua CLI script for macOS. Applies when the target is a self-contained #!/usr/bin/env lua script (not Hammerspoon, WezTerm, or Neovim config).
---

# shell-to-lua

## Overview

Convert shell scripts, Python tools, or AppleScript workflows into self-contained
`#!/usr/bin/env lua` CLI scripts. The target style is **stdlib-only Lua** (plus
`lfs` when filesystem attributes are needed) that behaves exactly like a shell
script — CLI flags, stdout/stderr, exit codes, `--dry-run` — but is portable,
easier to embed in macOS workflows, and callable from Keyboard Maestro.

Canonical reference: `~/Scripts/Utilities/Symlink/clean-broken-links-advanced.lua`

---

## Core Idioms

### Shebang & arg parsing
```lua
#!/usr/bin/env lua
-- One-line description.
-- Usage: script-name.lua [options] [args]

local options = {
  dry_run = false,
  quiet   = false,
  format  = "text",
  output  = nil,
}
local paths = {}

local index = 1
while index <= #arg do
  local v = arg[index]
  if     v == "--dry-run"  then options.dry_run = true; index = index + 1
  elseif v == "--quiet"    then options.quiet = true;   index = index + 1
  elseif v == "--output"   then options.output = arg[index + 1]; index = index + 2
  elseif v == "-h" or v == "--help" then
    print("Usage: ..."); os.exit(0)
  elseif v:sub(1,1) == "-" then
    io.stderr:write("Unknown option: " .. v .. "\n"); os.exit(2)
  else
    table.insert(paths, v); index = index + 1
  end
end
```

> **Note:** Use `arg[]` (not `{...}`) for CLI scripts. `{...}` is for functions.

---

### Shell execution
```lua
-- Fire-and-forget (returns true/false)
local function run(cmd)
  local ok, _, code = os.execute(cmd .. " 2>/dev/null")
  return ok == true or code == 0
end

-- Capture stdout
local function capture(cmd)
  local h = io.popen(cmd .. " 2>/dev/null")
  if not h then return "" end
  local out = h:read("*a") or ""
  h:close()
  return out
end
```

---

### Safe shell quoting
```lua
local function shell_quote(s)
  return "'" .. tostring(s):gsub("'", "'\\''") .. "'"
end
```
Always quote paths before interpolating into `os.execute` / `io.popen`.

---

### macOS notifications & dialogs
```lua
-- Notification (fire-and-forget)
local function notify(msg)
  run("/usr/bin/osascript -e " .. shell_quote(
    'display notification ' .. string.format('%q', msg) ..
    ' with title "My Script"'))
end

-- Modal dialog (returns button label)
local function dialog(msg, buttons, default)
  local btns = table.concat(
    (function() local t={} for _,b in ipairs(buttons) do
      t[#t+1]=string.format('%q',b) end return t end)(), ", ")
  local script = string.format(
    'button returned of (display dialog %q buttons {%s} default button %q with title "My Script")',
    msg, btns, default)
  local result = capture("/usr/bin/osascript -e " .. shell_quote(script))
  return result:match("^%s*(.-)%s*$")  -- trim
end
```

---

### Finder selection (when no CLI args given)
```lua
local function finder_selection()
  return capture([[/usr/bin/osascript -e '
tell application "Finder"
  try
    set sel to selection
    if sel is {} then return ""
    set out to ""
    repeat with anItem in sel
      set out to out & POSIX path of (anItem as alias) & linefeed
    end repeat
    return out
  on error
    return ""
  end try
end tell']])
end

-- Fallback pattern (put after arg parsing):
if #paths == 0 then
  for p in finder_selection():gmatch("[^\n]+") do
    table.insert(paths, p)
  end
end
```

---

### File output / quiet mode
```lua
local function write_output(text)
  if options.quiet and not options.output then return true end
  if options.output then
    local f = io.open(options.output, "w")
    if not f then return false end
    f:write(text)
    if text:sub(-1) ~= "\n" then f:write("\n") end
    f:close()
    return true
  end
  io.write(text)
  if text:sub(-1) ~= "\n" then io.write("\n") end
  return true
end
```

---

### Dry-run pattern
```lua
if options.dry_run then
  print("[dry-run] would delete: " .. path)
else
  run("rm -f " .. shell_quote(path))
end
```

Always implement `--dry-run` for any destructive operation.

---

## Conversion Map

| Shell / Python | Lua equivalent |
|---|---|
| `$1`, `$2` | `arg[1]`, `arg[2]` |
| `"$@"` loop | `for _, v in ipairs(arg) do` |
| `$(cmd)` | `capture("cmd")` |
| `cmd &>/dev/null` | `run("cmd")` |
| `echo "msg" >&2; exit 1` | `io.stderr:write("msg\n"); os.exit(1)` |
| `[[ -f path ]]` | `io.open(path, "r") ~= nil` |
| `[[ -d path ]]` | `lfs.attributes(path, "mode") == "directory"` |
| `[[ -L path ]]` | `lfs.symlinkattributes(path, "mode") ~= nil` |
| `mkdir -p` | `os.execute("mkdir -p " .. shell_quote(path))` |
| `osascript -e '...'` | `run("/usr/bin/osascript -e " .. shell_quote(...))` |
| `printf '%q'` | `string.format('%q', s)` |
| `local VAR=val` | `local var = val` |
| associative array | Lua table `{ key = val }` |
| bash array | `local t = {}; table.insert(t, v)` |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Using `{...}` for CLI args | Use `arg[]` — `{...}` is varargs for functions |
| `os.execute` return value | Check `ok == true or code == 0` (Lua 5.2+/5.4 differ) |
| Unquoted paths in shell strings | Always wrap in `shell_quote()` |
| `lfs` without checking it's available | Add `local ok, lfs = pcall(require, "lfs")` guard |
| Forgetting `2>/dev/null` in `io.popen` | Stderr leaks to terminal; append it |
| AppleScript heredoc with single quotes | Wrap the outer call in `shell_quote()`, not raw `'...'` |
| `string.format('%q', s)` for osascript | Correct for double-quoted AS strings; use for `display notification` |

---

## Quick Checklist

- [ ] `#!/usr/bin/env lua` shebang
- [ ] Options table with defaults before arg parsing
- [ ] `arg[]`-based flag loop with `os.exit(2)` on unknown flags
- [ ] `shell_quote()` defined and used on all interpolated paths
- [ ] `--dry-run` flag for any destructive ops
- [ ] `--help` prints usage and `os.exit(0)`
- [ ] Errors to `io.stderr:write()`, exit codes reflect success/failure
- [ ] Finder selection fallback if no paths provided (macOS workflows)
- [ ] `lfs` required only when needed (not universally available)
