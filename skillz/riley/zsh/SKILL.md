---
name: riley-zsh-config
description: >
  Comprehensive expert context for Riley's macOS Zsh config at ~/.config/zsh.
  Use for any work on startup flow, module architecture, aliases/functions,
  lazy-loading, fzf UX conventions, git helpers, prompt config, shell debugging,
  or the repo's decorative file banners, Nerd Font section icons, separators,
  code comments, and visual formatting conventions.
---

# Riley Zsh Config Skill (Comprehensive + Personal Preferences)

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

## Current Repository Map

Treat this as an orientation map, not a substitute for `rg --files` and the
active `load_module`/`source` calls in `.zshrc`.

```text
~/.config/zsh/
├── .zshenv / .zprofile / .zshrc
├── README.md
├── assets/
│   ├── graf-banner.png
│   └── zsh.png
├── completions/
│   └── _<command>          # repo-local Zsh completion definitions
├── docs/
│   ├── AGENTS.md / SKILL.md
│   ├── ARCHITECTURE.md / PERFORMANCE.md
│   └── INSTALLATION.md / CUSTOMIZATION.md
├── modules/
│   ├── colors.zsh
│   ├── data/
│   │   ├── material.zsh
│   │   └── pantone-coated.zsh
│   ├── config.zsh
│   ├── aliases.zsh
│   ├── functions.zsh
│   ├── coolshit.zsh
│   ├── antigravity.zsh
│   ├── git.zsh
│   ├── lazy.zsh
│   ├── loader.zsh
│   └── ghostty.zsh
├── prompt/
│   ├── starship.toml
│   └── starship-terminal.toml
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

## Visual Language and Formatting

Treat presentation as part of this repo's maintained interface. Preserve the
stylized, glyph-rich house style when adding or reorganizing Zsh code.

### Inspect before formatting

1. Read the full target file and one recently formatted sibling module.
2. Reuse the target file's existing width, icon, spacing, and header variant.
3. Use a Nerd Font-capable view when judging alignment; ordinary character
   counts do not reliably measure private-use glyph display width.
4. Format the code touched by the task. Do not restyle unrelated legacy
   sections or replace a deliberate banner variant unless asked.
5. If a nearby block is visibly malformed, duplicate-free repair is safe only
   when it is directly adjacent to the requested edit; otherwise report it.

### File mastheads

Use a full decorative masthead at the top of substantial config and module
files. A module masthead contains:

- an optional `#!/usr/bin/env zsh` shebang as the literal first line;
- the boxed `Z S H   M O D U L E` or `C O N F I G U R A T I O N` label;
- one meaningful Nerd Font icon repeated in the header and update footer;
- a spaced module name such as `A L I A S E S`;
- centered FIGlet-style module-name art;
- `https://github.com/deathrashed/zsh`;
- one concise purpose line;
- a centered keyword line separated with bullets;
- a boxed `L A S T  U P D A T E D` footer and current edit date.

Do not generate a new masthead from memory. Copy the complete masthead from the
closest canonical sibling, then change the module name, icon, art, purpose,
keywords, and date while preserving its visual width. Keep every border line
commented and ensure there is no accidental leading space before `#`.

Do not add a large masthead to tiny bootstrap, generated, secret, or compatibility
files merely for uniformity. Match their established local style.

### Header hierarchy

Use one visual level per semantic level. Do not stack two equivalent headers
for the same block.

#### Major section: default

Use this for a category containing multiple aliases, functions, or related
settings:

```zsh
#══════════════════════════════════════════════════════════════════════════════════════════
# 󰯃 SCRIPT HUB
# - A collection of custom scripts and utilities,
#   organized in one central location.
#══════════════════════════════════════════════════════════════════════════════════════════
```

- Choose a Nerd Font icon that identifies the category.
- Write the title in uppercase.
- Add a short `# -` description that explains scope or purpose.
- Wrap long descriptions onto aligned `#   ` continuation lines.
- Keep the top and bottom rule the same width as neighboring sections.

#### Major introduction: expanded

Use the existing expanded form for a file's opening content section when it
includes descriptive metadata:

```zsh
#══════════════════════════════════════════════════════════════════════════════════════════
# 󰘳 ALIASES & SHORTCUTS
#─────────────────────────────────────────────────────────────────────────────
# A large collection of aliases for common commands and workflows.
# Organized by category and kept separate for easy editing.
#─────────────────────────────────────────────────────────────────────────────
```

Preserve optional `Updated:` metadata only where that file already uses it.
Do not add duplicate descriptions or dates.

#### Compact structural section

Use the bullet-capped form where the surrounding file already uses it for
high-level startup/configuration phases:

```zsh
#•═══════════════════════════════════════════════════════════════════════════════════════════•
#  CORE ENVIRONMENT
#•═══════════════════════════════════════════════════════════════════════════════════════════•
```

Do not mix compact and default major headers arbitrarily. Follow the target
file's hierarchy.

### Subsections and item comments

Use a thin rule for a named subsection or a visually distinct action:

```zsh
#─────────────────────────────────────────────────────────────────────────────
# 󰈮 Run all scripts from one interactive TUI
#─────────────────────────────────────────────────────────────────────────────
alias hub='$HOME/Scripts/.hub/script-hub.sh'
```

Use a plain intent comment followed by a thin rule when several neighboring
lines share one explanation:

```zsh
# Clean default: icons and names without metadata clutter.
#─────────────────────────────────────────────────────────────────────────────
alias ls='eza ...'
```

Apply these rules:

- Add an icon to meaningful named actions/categories, not every incidental note.
- Keep the comment immediately attached to the code it documents.
- Use sentence case for prose and uppercase only for section titles.
- Avoid decorative `─` prefixes inside prose when the enclosing thin rule
  already supplies the visual structure.
- Leave enough blank space between major sections to make scanning easy, while
  avoiding large accidental whitespace runs.

### Comments inside complex functions

Document multi-stage functions at the level a maintainer needs to navigate
them. Explain state transitions, destructive actions, non-obvious Zsh
expansions, external side effects, and why a branch exists.

Use compact internal phase labels for long interactive functions:

```zsh
  # ── FILE PICKER ───────────────────────────────────────
  local selected_files

  # ── ACTION PICKER ─────────────────────────────────────
  local action
```

Use ordinary sentence comments for local decisions:

```zsh
    # Audio files open in Swinsian; other formats use their default app.
```

Do not:

- narrate every assignment or obvious command;
- turn every line into a decorated subsection;
- preserve stale comments after behavior changes;
- use comments to excuse unsafe or unclear code.

### Nerd Font and output symbols

- Prefer existing repo glyphs for related concepts before introducing a new one.
- Keep a section's icon semantically consistent across its header and nearby
  success/warning output where appropriate.
- Use the established status language: `󰄬` success, `󰀪` warning, `󰅖` failure,
  unless the local helper has a more specific established symbol.
- Keep a plain-text explanation beside icons; never make meaning depend on the
  glyph alone.
- Do not substitute emoji for established Nerd Font symbols in a formatted module.

### General code style

1. Use `function name() { ... }` consistently.
2. Keep guard clauses explicit and readable.
3. Explain intent, assumptions, side effects, and tradeoffs rather than syntax.
4. Keep interactive output consistent with existing glyph-rich messaging.
5. Keep code practical and maintainable rather than terse for its own sake.

For docs and skill text, prefer explicit headings, grouped sections, practical
checklists, and concrete examples.

---

## Architecture & Load Model

### Shell startup chain

```text
.zshenv -> .zprofile -> .zshrc
```

### Module loading in `.zshrc`

1. `colors.zsh` loads first and sources the palette data files.
2. `config.zsh` loads next for environment, PATH, framework, and completions.
3. `aliases.zsh`, `functions.zsh`, `coolshit.zsh`, and `antigravity.zsh`
   load eagerly.
4. `git.zsh` and `loader.zsh` use `zsh-defer` when available.
5. `loader.zsh` registers stubs; the first stub call sources `lazy.zsh`.
6. `ghostty.zsh` is sourced directly later in `.zshrc`, outside `load_module`.

### Lazy loading contract

- `loader.zsh` discovers top-level function declarations in `lazy.zsh` and
  builds `__functions_symbols` dynamically.
- generated `gitquick_*` names are appended from `GITQUICK_REPOS`.
- each symbol is stubbed to `__functions_stub` -> `__load_functions`
- `__load_functions` sources `lazy.zsh` once

**Hard rule:** keep lazy functions as parseable top-level declarations using
`function name() {` or `name() {`, then verify the generated stub. Do not
reintroduce a manually maintained symbol list.

---

## Module Responsibilities

### `modules/colors.zsh` and `modules/data/*.zsh`
- Define shared terminal status colors and named color lookup/sample helpers
- Source the Material and Pantone associative-array datasets
- Load before modules that consume shared presentation primitives

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

### `modules/coolshit.zsh`
- Eager aliases/functions for terminal visuals, screensavers, and system candy
- Keep optional command dependencies guarded where practical

### `modules/antigravity.zsh`
- Sources the central AI-tool environment hub when it exists
- Keep it lightweight and tolerant of the external include being absent

### `modules/lazy.zsh`
- heavy and infrequent functions loaded on demand
- fzf file manager, media tools, git utilities, note helpers, misc utilities

### `modules/loader.zsh`
- Discover lazy declarations, generate stubs, and dispatch the first call
- Keep discovery compatible with the declaration styles used in `lazy.zsh`

### `modules/git.zsh`
- standalone git aliases and helper functions
- `git-tui`/`gtui` interactive helper stack

### `modules/ghostty.zsh`
- Direct-sourced Ghostty helpers, diagnostics, captures, and keybind lookup
- Do not assume it follows the normal `load_module` ordering

### `completions/_*`
- Repo-local completion definitions added to `fpath`
- Name each file after its command and validate it with Zsh completion syntax

Files present in `modules/` are not automatically active. Confirm a file is
sourced before treating it as part of runtime behavior; for example, alternate
or work-in-progress copies such as `aliased.zsh` may exist without being loaded.

---

## Non-Negotiable Guardrails

1. Do **not** export `CONFIG`; keep `typeset -g CONFIG=...` behavior intact.
2. Do **not** use `readonly` for re-source-sensitive shared color vars; use `typeset`.
3. Do **not** create recursive alias patterns like `alias glow='glow ...'` (must use `command glow ...`).
4. Do **not** hardcode secrets in tracked files.
5. Do **not** introduce eager loads for heavyweight tools that are intentionally lazy.
6. Do **not** break fzf keybinding conventions and global/default option layering.
7. Do **not** add bashisms where zsh-native syntax is expected.
8. Do **not** add lazy declarations that the loader's discovery patterns cannot parse.

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
2. Use a declaration form recognized by `loader.zsh`
3. Add an alias in `modules/aliases.zsh` if needed
4. Verify discovery creates the stub and the first call resolves the function

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
- [ ] file masthead still has the shebang first, fully commented borders, aligned
      box art, consistent icon, and an accurate update date
- [ ] new sections use the target file's established header width and hierarchy
- [ ] comments describe intent and remain attached to the code they document
- [ ] no accidental leading spaces before top-level `#` banner lines
- [ ] lazy declarations are discovered and their generated stubs resolve
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
4. visual hierarchy and comments match the surrounding file,
5. syntax passes,
6. behavior is consistent with Riley's formatting/tooling/workflow conventions.
