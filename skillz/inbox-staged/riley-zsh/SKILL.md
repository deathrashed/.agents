---
name: riley-zsh
description: >
  Comprehensive expert context for Riley's macOS Zsh config at ~/.config/zsh.
  Use for any work on startup flow, module architecture, aliases/functions,
  lazy-loading, fzf UX conventions, git helpers, prompt config, and shell debugging.
---

# Riley Zsh Config Skill (Comprehensive + Personal Preferences)

## When to Use This Skill

Activate this skill whenever a task touches any of:

- `.zshenv`, `.zprofile`, `.zshrc`
- `modules/*.zsh` (especially `config.zsh`, `functions.zsh`, `lazy.zsh`, `loader.zsh`, `git.zsh`, `aliases.zsh`)
- `prompt/starship.toml`
- `docs/AGENTS.md` and repo behavior docs
- alias/function additions, startup regressions, load-order bugs, fzf behavior, PATH issues

If uncertain, **use this skill by default** for repo-local zsh changes.

---

## Riley Environment Profile

### Hardware / OS / Shell
- Machine: MacBook Air 15-inch M3
- OS: macOS Sequoia
- Shell: Zsh 5.9
- Config root: `~/.config/zsh` (`ZDOTDIR` model)

### Terminal / Prompt Preferences
- Preferred terminal: **Ghostty**
- Also used: VS Code integrated terminal
- Prompt engine: **Starship** via `prompt/starship.toml`

### Core Tool Preferences (day-to-day)
- Editor: `micro` (with VS Code openers as needed)
- File listing: `eza` (preferred over plain `ls` in workflows)
- File search: `fd` (preferred over `find` where practical)
- Text search: `rg`
- Fuzzy selection: `fzf`
- Preview: `bat`
- Directory jump: `zoxide`
- Runtime manager: `mise`
- File manager: `yazi`

### High-use ecosystem tools found in config
- git + gitea CLI (`tea`)
- Homebrew
- ffmpeg / yt-dlp / librsvg / imagemagick
- gum/charm helpers

---

## Current Repository Map

```text
~/.config/zsh/
├── .zshenv
├── .zprofile
├── .zshrc
├── README.md
├── docs/
│   ├── AGENTS.md
│   └── SKILL.md
├── modules/
│   ├── aliases.zsh
│   ├── config.zsh
│   ├── functions.zsh
│   ├── git.zsh
│   ├── lazy.zsh
│   └── loader.zsh
├── prompt/
│   └── starship.toml
└── secrets/
    ├── APIs.csv
    ├── iterm2-integration.zsh
    └── secrets.zsh
```

---

## Paths Riley Uses Frequently

- Zsh repo root: `~/.config/zsh`
- Modules dir: `~/.config/zsh/modules`
- Prompt config: `~/.config/zsh/prompt/starship.toml`
- Secrets file: `~/.config/zsh/secrets/secrets.zsh`
- Obsidian vault path (used by note helpers):
  - `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian`
- iCloud root:
  - `~/Library/Mobile Documents/com~apple~CloudDocs`
- External media volume paths used by aliases/functions:
  - `/Volumes/Eksternal`
  - `/Volumes/Apfspace`

When editing functions, prefer existing env vars (`$MUSIC_DIR`, `$ICLOUD`, `$OBSIDIAN`, etc.) over repeating absolute paths.

---

## Formatting & Style Preferences

This repo favors **structured, readable, high-signal formatting**:

1. Boxed section banners and clear section separators in zsh files.
2. Comments explain **intent and tradeoffs**, not obvious syntax.
3. Consistent function declaration style: `function name() { ... }`.
4. Guard clauses are explicit and readable.
5. Keep interactive output style visually consistent with existing glyph-heavy messaging.
6. Keep code practical, not minimalistic-for-its-own-sake.

For docs/skill text:
- Prefer explicit headings and grouped sections.
- Include practical checklists and playbooks.
- Favor concrete examples over abstract guidance.

---

## Architecture & Load Model

### Shell startup chain

```text
.zshenv -> .zprofile -> .zshrc
```

### Module loading in `.zshrc`

1. `config.zsh` loads first (env/path/framework/completions)
2. `aliases.zsh` and `functions.zsh` load eagerly
3. heavier modules are deferred when possible (notably `git.zsh`, `loader.zsh`)
4. `loader.zsh` registers stubs; first stub call sources `lazy.zsh`

### Lazy loading contract

- `loader.zsh` owns `__functions_symbols`
- each symbol is stubbed to `__functions_stub` -> `__load_functions`
- `__load_functions` sources `lazy.zsh` once

**Hard rule:** if you add/remove/rename a function in `lazy.zsh`, sync `__functions_symbols` in `loader.zsh` in the same change.

---

## Module Responsibilities

### `modules/config.zsh`
- Startup-sensitive core: XDG vars, PATH assembly, OMZ plugin setup, completion config
- Lazy tool init patterns (e.g. NVM, pyenv wrappers)
- History and completion behavior

### `modules/aliases.zsh`
- High-volume aliases and directory vars
- naming systems (e.g., `///name`, `//name`, `bat-name`, `z*`, `g*`, etc.)
- frequent UX shortcuts for file ops and macOS workflows

### `modules/functions.zsh`
- Eager, startup-safe functions
- includes `_fzf_alias_widget` and `ab` behavior
- keep minimal and low-cost

### `modules/lazy.zsh`
- heavy and infrequent functions loaded on demand
- fzf file manager, media tools, git utilities, note helpers, misc utilities

### `modules/loader.zsh`
- the lazy function dispatcher and symbol registry
- must stay synchronized with `lazy.zsh`

### `modules/git.zsh`
- standalone git aliases and helper functions
- `git-tui`/`gtui` interactive helper stack

---

## Non-Negotiable Guardrails

1. Do **not** export `CONFIG`; keep `typeset -g CONFIG=...` behavior intact.
2. Do **not** use `readonly` for re-source-sensitive shared color vars; use `typeset`.
3. Do **not** create recursive alias patterns like `alias glow='glow ...'` (must use `command glow ...`).
4. Do **not** hardcode secrets in tracked files.
5. Do **not** introduce eager loads for heavyweight tools that are intentionally lazy.
6. Do **not** break fzf keybinding conventions and global/default option layering.
7. Do **not** add bashisms where zsh-native syntax is expected.
8. Do **not** add functions to `lazy.zsh` without updating `loader.zsh`.

---

## Coding Standards (Zsh)

- Prefer `function name() { ... }`
- Use `[[ ... ]]`, `(( ... ))`, `${var}` expansions
- Use `local` variables inside functions
- Guard early with explicit `return 1` when input/preconditions fail
- Send errors to stderr where appropriate (`>&2`)
- Avoid absolute `/Users/rd` when `$HOME` or existing env vars are correct
- Keep comments intent-focused (why/tradeoff), not noise

---

## fzf UX Conventions

Global style lives in `.zshrc` (`FZF_DEFAULT_OPTS`, ctrl bindings, theme). In per-function pickers:

- define only context-specific differences (`--prompt`, `--header`, `--preview`, etc.)
- preserve expected control affordances where applicable:
  - open
  - reveal
  - copy
  - toggle preview
- do not duplicate global color/border/pointer/marker defaults unless intentionally overriding

---

## Change Playbooks

### Add a new eager function

1. Implement in `modules/functions.zsh`
2. Keep startup footprint small
3. Add alias entry in `modules/aliases.zsh` if needed
4. Validate syntax and binding behavior

### Add a new lazy function

1. Implement in `modules/lazy.zsh`
2. Add symbol to `__functions_symbols` in `modules/loader.zsh`
3. Add alias in `modules/aliases.zsh` if needed
4. Verify stub resolves function after first call

### Add/modify alias

1. Place in correct section in `modules/aliases.zsh`
2. Check for naming collisions (`alias <name>`, `type <name>`)
3. Ensure no accidental override of critical commands

### Touch startup-sensitive config

1. Edit `modules/config.zsh` (or `.zshrc`) carefully
2. preserve lazy-load patterns and ordering
3. measure startup if relevant (`PROFILE_ZSH_STARTUP=true zsh`)

### Adjust prompt

- keep prompt changes in `prompt/starship.toml`
- avoid coupling prompt logic into unrelated module files

---

## Validation Checklist (Before Finishing)

- [ ] syntax check touched zsh files (`zsh -n <file>`)
- [ ] lazy function + loader symbol list synchronized
- [ ] no secrets added, no sensitive values echoed in commits
- [ ] no regressions to keybindings/interactive behavior
- [ ] no unnecessary hardcoded absolute home path
- [ ] docs updated when behavior contract changes

---

## Practical Test Commands

```bash
# Syntax checks
zsh -n ~/.config/zsh/.zshrc
zsh -n ~/.config/zsh/modules/config.zsh
zsh -n ~/.config/zsh/modules/functions.zsh
zsh -n ~/.config/zsh/modules/lazy.zsh
zsh -n ~/.config/zsh/modules/loader.zsh

# Reload shell
exec zsh -l

# Startup profiling (when relevant)
PROFILE_ZSH_STARTUP=true zsh

# Verify alias/function visibility
alias <name>
type <function_name>
```

---

## Frequent Risk Areas

- forgetting loader symbol updates after lazy function changes
- introducing startup regressions by moving heavy work into eager paths
- accidental command-shadowing via broad aliases
- fzf option duplication that drifts from global defaults
- changing long-standing key behavior (history vs reveal/open bindings)

---

## Completion Standard

A change is complete only when:

1. the edit is in the correct module,
2. lazy/eager boundaries remain intentional,
3. loader synchronization is correct,
4. syntax passes,
5. behavior is consistent with Riley's formatting/tooling/workflow conventions.
