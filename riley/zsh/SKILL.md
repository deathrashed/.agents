---
name: riley-zsh-config
description: >
  Expert knowledge of Riley's personal Zsh configuration at ~/.config/zsh.
  Use this skill whenever working on any file in this repository — aliases,
  functions, git helpers, config, prompt, or the lazy loader. Also use when
  asked to add new aliases, write new functions, debug shell behaviour, extend
  the fzf interface, modify the module structure, or update documentation.
  If the user mentions any module by name (aliases.zsh, functions.zsh,
  extras.zsh, lazy.zsh, git.zsh, config.zsh, starship.toml) or references
  any function or alias from the config, use this skill immediately.
---

# Riley's Zsh Config — Skill

## Machine & Environment

- **Hardware**: MacBook Air 15-inch M3, 8GB RAM
- **OS**: macOS Sequoia
- **Terminal**: Ghostty
- **Prompt**: Starship (`~/.config/zsh/prompt/starship.toml`)
- **Shell**: Zsh 5.9 via Homebrew
- **Config root**: `~/.config/zsh/` (`ZDOTDIR` set in `~/.zshenv`)

---

## Repository Structure

```
~/.config/zsh/
├── .zshenv              # ZDOTDIR, early XDG env
├── .zprofile            # Login shell shim
├── .zshrc               # Entry point — plugins, fzf, runtime tools
├── .gitignore           # Secrets, history, .zwc, sessions excluded
├── AGENTS.md            # AI agent instructions
├── README.md
├── modules/
│   ├── aliases.zsh      # All aliases + directory shortcuts + path vars
│   ├── config.zsh       # XDG, PATH, OMZ, completions, history, lazy inits
│   ├── functions.zsh    # Daily-use functions — eager loaded
│   ├── extras.zsh       # Infrequent functions — lazy loaded via lazy.zsh
│   ├── git.zsh          # Git aliases, TUI, dual-remote helpers
│   └── lazy.zsh         # Two-tier lazy loader stubs
└── prompt/
    └── starship.toml    # Starship prompt config
```

---

## Module Roles & Load Order

```
.zshenv → .zprofile → .zshrc
  └── config.zsh        (immediate)
  └── aliases.zsh       (immediate)
  └── git.zsh           (deferred via zsh-defer)
  └── lazy.zsh          (deferred via zsh-defer)
       ├── stubs → functions.zsh  (loads on first call)
       └── stubs → extras.zsh    (loads on first call, independent)
```

**Critical**: `lazy.zsh` has two independent symbol lists. A call to a `functions.zsh` stub never triggers loading of `extras.zsh`. Keep them separate.

---

## Core Design Principles

### 1. Consistent fzf interface
Every interactive fzf call follows the same pattern. Do not deviate:

```zsh
fzf \
  --exact \
  --height=50% \
  --prompt="context > " \
  --header="^O:Open ^R:Reveal ^Y:Copy ^/:Toggle | Enter:Action" \
  --preview='...' \
  --preview-window='top:40%:wrap' \
  --bind="ctrl-/:toggle-preview" \
  --bind="ctrl-o:execute(open {})+abort" \
  --bind="ctrl-r:execute(open -R {})+abort" \
  --bind="ctrl-y:execute(echo {} | pbcopy)+abort"
```

**Never repeat** color, border, pointer, marker, separator, scrollbar — those come from `FZF_DEFAULT_OPTS` in `.zshrc`. Only define what differs from the default.

### 2. Lazy loading pattern
When adding a new function to `extras.zsh`, always add it to `__functions_extra_symbols` in `lazy.zsh`. Same for `functions.zsh` → `__functions_symbols`.

```zsh
# In lazy.zsh — add to the correct list:
typeset -ga __functions_extra_symbols=(
  ...
  new_function_name
)
```

### 3. Functions that must NOT be lazy loaded
- `_fzf_alias_widget` — zle widget, needed at startup for `bindkey`
- `_gitquick_repo` — called by gitquick_* before stubs can intercept
- `zseed` — called during zoxide init
- Any function used by another eager-loaded function

### 4. No emoji in function output
Functions use plain text or Unicode symbols (`✓`, `✗`, `⚠`, `→`). No emoji unless the function predates this convention and is explicitly kept as-is.

### 5. Alias naming conventions
- `///name` — open module in micro (terminal)
- `//name` — open module in VSCode
- `bat-name` — bat preview of module
- `z*` — zoxide quick-jump aliases
- `f*` — Finder openers (`fdl`, `faudio` etc)
- `g*` — git aliases
- `b*` — Homebrew aliases
- `py-*` — Python aliases
- `dc*` — Docker Compose

---

## Key Functions Reference

### Daily use (`functions.zsh`)

| Function | Signature | Notes |
|----------|-----------|-------|
| `ab` | `ab` | fzf alias+function browser, `print -z` output |
| `_fzf_alias_widget` | zle widget | `ctrl-a` binding, `LBUFFER` append |
| `fza` | `fza [dir]` | Multi-select file manager, 18 actions |
| `msearch` | `msearch [query]` | Music library fzf, uses `$MUSIC_DIR` |
| `fkill` | `fkill` | Process killer with ps preview |
| `offload` | `offload` | iCloud eviction, `brctl evict` |
| `imgbb` | `imgbb [file\|dir]` | Upload → clipboard |
| `mvln` | `mvln src dest` | Move + symlink |
| `bak` | `bak` | Interactive backup with timestamp |
| `clean_files` | `clean_files [dir] [--dry-run]` | kebab-case rename |
| `qn` | `qn text` | Append to `~/notes.md` |
| `oqn` | `oqn text` | Append to Obsidian Note.md |
| `gqz/gqo/gqa` | `gqz` | Quick commit+push per repo |
| `fkill` | `fkill` | fzf process killer |
| `soundsfucked` | `soundsfucked` | Reset Core Audio |
| `xmount` | `xmount` | Unmount all non-protected volumes |
| `y` | `y [path]` | Yazi with cwd-on-exit |

### Infrequent (`extras.zsh`)

| Function | Notes |
|----------|-------|
| `find-cover` | COVIT cover art finder |
| `svg2png` | rsvg-convert wrapper, recursive |
| `svg2icons` | Simple Icons → black/white PNG |
| `conv-jxl` / `conv-avif` | Batch image conversion |
| `cleanname` | Filename cleanup with revert log |
| `clean_installers` | Strip version/arch suffixes |
| `deezer` / `spotify` | DeemixKit wrappers |
| `splink` | Spotify album resolver |
| `odesli` | Universal song link → clipboard |
| `fco` / `fga` | fzf git checkout / add |
| `git-nuke` | Delete branch everywhere |
| `wifipass` | Keychain WiFi password lookup |
| `server` | `python3 -m http.server` + open |
| `sysinfo` | Gum-powered system info |
| `commit` | Gum-powered conventional commit |

---

## Environment Variables

```zsh
MUSIC_DIR="/Volumes/Eksternal/Audio"   # Used by msearch, sa, fa, qa, aur, eks
EKSTERNAL="/Volumes/Eksternal"
APFSPACE="/Volumes/Apfspace"
AUDIO="$EKSTERNAL/Audio"
OBSIDIAN="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian"
ICLOUD="$HOME/Library/Mobile Documents/com~apple~CloudDocs"
DOWNLOAD_DIR="$HOME/Downloads"
CONFIG="$HOME/.config"                 # typeset -g, not exported (breaks Nushell)
IMGBB_API_KEY                          # In secrets.zsh
```

**Important**: `CONFIG` must use `typeset -g` not `export` — exporting it breaks Nushell's `$env.config` record.

---

## fzf Configuration

Defined in `.zshrc` FZF CUSTOMIZATION section:

```zsh
# Global defaults — never repeat these in individual functions:
# --color, --border, --pointer, --marker, --separator, --scrollbar
# --bind ctrl-/  (toggle preview)
# --bind ctrl-o  (open)
# --bind ctrl-r  (reveal in Finder)
# --bind ctrl-y  (copy to clipboard)

# Key bindings:
ctrl-f    → fzf history search (remapped from ctrl-r)
ctrl-t    → file picker
alt-c     → directory jump
ctrl-a    → alias/function browser (_fzf_alias_widget)
```

**History**: `source <(fzf --zsh)` followed by `bindkey -r '^R'` and `bindkey '^F' fzf-history-widget`. The `ctrl-r` bind in `FZF_DEFAULT_OPTS` is for Reveal in Finder inside file pickers — it does NOT conflict because history uses `ctrl-f`.

---

## Starship Prompt

Config at `~/.config/zsh/prompt/starship.toml`. Key settings:
- Path color: `bold #1D9AF3`
- Character: `❯` purple/red
- Git branch: `󰊢` grey
- `[custom.loc_*]` modules for colored location indicators (Apfspace, Eksternal, iCloud)
- `[directory_substitutions]` for icon+name replacements
- Right prompt: language versions + cmd duration + time

---

## Naming & Style Rules

When writing new code for this config:

1. **Zsh idioms** — use `[[ ]]`, `(( ))`, `${param}` expansions. No `[ ]` or `test`.
2. **No bashisms** — no `$()` with `let`, no `[[` with `=~` using unquoted patterns containing `|&` (use `==` glob patterns instead).
3. **Error handling** — `[[ condition ]] || { echo "msg"; return 1; }` on one line for guards.
4. **Local variables** — always `local` inside functions.
5. **Function definitions** — `function name() {` style (not `name() {`).
6. **Comments** — `# ── SECTION NAME ──` for inline section headers inside functions.
7. **No hardcoded `/Users/rd`** where `$HOME` works — use `$HOME` or env vars.
8. **Avoid `find`** — use `fd` instead. Faster, respects `.gitignore`, better defaults.
9. **Avoid `ls`** in scripts — use `eza` or `fd`.
10. **No `readonly`** on color variables — use `typeset -g`. `readonly` breaks on re-source.

---

## Common Patterns

### Adding a new daily function
1. Write function in `functions.zsh`
2. Add name to `__functions_symbols` in `lazy.zsh`
3. Add alias in `aliases.zsh` if it needs one
4. Add `///funcname` and `//funcname` edit shortcuts in `aliases.zsh` if significant

### Adding a new infrequent function
1. Write function in `extras.zsh`
2. Add name to `__functions_extra_symbols` in `lazy.zsh`

### Adding a new fzf function
Follow the standard interface. Minimal example:
```zsh
function myfunc() {
  local selected
  selected=$(fd -t f . "$SOME_DIR" | fzf \
    --exact \
    --height=50% \
    --prompt="context > " \
    --header="^O:Open ^Y:Copy | Enter:Action" \
    --preview='bat --color=always {}' \
    --preview-window='top:40%')
  [[ -n "$selected" ]] && open "$selected"
}
```

### Adding a git quick-push repo
```zsh
# In functions.zsh:
function gitquick_myrepo() { _gitquick_repo "/path/to/repo" "Label" "Label commit message: "; }
alias gqx="gitquick_myrepo"

# In lazy.zsh __functions_symbols:
gitquick_myrepo
```

---

## Known Quirks & Gotchas

- **`alias xattr=...`** was removed — it shadowed the `xattr` command. Use `unquarantine` or `rmq` instead.
- **`alias date="gdate"`** was removed — breaks scripts. Use `gdt` alias instead.
- **`alias glow='glow -p'`** must be `alias glow='command glow -p'` — without `command` it recurses infinitely.
- **`alias cask="brew cask"`** removed — `brew cask` is deprecated.
- **OMZ `aliases` plugin** removed — conflicts with the custom `ab` widget.
- **Perl deferred exports** don't work with `zsh-defer` — exports in deferred subshells don't reach the parent. Perl init runs synchronously (only when `~/perl5` exists).
- **`CONFIG` variable** — must NOT be exported. Exporting it breaks Nushell.
- **`zobs-Visual Studio Code`** was an invalid alias name — spaces break alias names. Renamed to `zobs-vscode`.

---

## Secrets

`~/.config/zsh/secrets/secrets.zsh` — git-ignored, loaded when present.
Contains: `IMGBB_API_KEY`, Spotify API credentials, and other tokens.
Never hardcode API keys. Never add secrets to tracked files.
