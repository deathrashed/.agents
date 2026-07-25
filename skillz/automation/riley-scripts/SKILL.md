---
name: riley-scripts
description: >
  Expert knowledge of Riley's ~/Scripts documentation workflow. Use this skill
  whenever working on scripts in /Users/rd/Scripts, creating or updating script
  documentation in the Obsidian vault, categorizing scripts, naming files,
  renaming badly named scripts, reviewing script code, organizing folders,
  refactoring scripts, debugging failures, or optimizing shell-based workflows.
  Use it for both documentation and code-maintenance work in ~/Scripts. Also
  use when asked to document a script, suggest improvements to a script, find
  gaps in a script category, decide where a new script should live, clean up a
  scripts folder, or align repo structure with the vault. Trigger immediately
  if the user mentions ~/Scripts, Obsidian script docs, _docs symlinks,
  CLAUDE.md, CATEGORY_RULES, FILENAME_RULES, script documentation, script
  organization, or script cleanup in any form — even casually.
---

# Riley's Scripts Documentation — Skill

## Overview

Scripts live in `/Users/rd/Scripts`. Canonical end-user documentation lives in
the Obsidian vault at:
`/Users/rd/Library/Mobile Documents/iCloud~md~obsidian/Documents/Scripts/`

The repo is now intentionally doc-light:
- Per-script documentation belongs in the vault, not beside the script
- Many repo folders contain `_docs`, a symlink to the matching vault folder
- Repo-local Markdown should be structural or operational, not duplicate
  end-user script docs

This skill covers both:
- Documentation workflow for the canonical vault docs
- Code-maintenance workflow for organizing, refactoring, debugging, and
  optimizing scripts inside `~/Scripts`

**Document precedence when guidance conflicts:**
1. `AGENTS.md` — workflow and process
2. `CLAUDE.md` — documentation template and structure
3. `_docs/CATEGORY_RULES.md` — category routing
4. `_docs/FILENAME_RULES.md` — naming conventions
5. `README.md` — overview only

---

## Naming Rules

Follow the current authoritative rules in the repo/vault references first:
- `/Users/rd/Scripts/.docs/FILENAME_RULES.md`
- `/Users/rd/Library/Mobile Documents/iCloud~md~obsidian/Documents/Scripts/_docs/FILENAME_RULES.md`

There is historical conflict between older documentation and the current repo
layout. Do not mass-rename scripts just because this skill describes a cleaner
scheme. Treat renames as an explicit refactor with user approval.

### Preferred long-term pattern

This skill still prefers a clean split:
- Executable scripts: shell-friendly names
- Documentation files: Smart Sentence Case

But the live repo may contain mixed conventions. Preserve working paths unless
the task is explicitly about naming cleanup.

### Script files → kebab-case
All executable scripts use kebab-case regardless of language. Spaces in
filenames cause constant escaping problems in shell and automation tools.

```
extract-urls-from-text.applescript  ✓
extract_urls_from_text.applescript  ✗  (snake_case)
Extract URLs from Text.applescript  ✗  (spaces)
```

### Documentation files → Smart Sentence Case
All `.md` files use Smart Sentence Case — the readable, menu-command name.

```
Extract URLs from Text.md  ✓
extract-urls-from-text.md  ✗
```

### Kebab → Doc name conversion (mechanical rule)
Strip extension → split on hyphens → apply Smart Sentence Case → uppercase
acronyms → add `.md`

```
extract-urls-from-text.applescript  →  Extract URLs from Text.md
convert-json-to-csv.py              →  Convert JSON to CSV.md
get-current-weather.sh              →  Get Current Weather.md
run-ocr-on-image.sh                 →  Run OCR on Image.md
```

### Smart Sentence Case rules
- Capitalise main words
- Keep these lowercase **unless first**: `a an the and or but for nor on at to from by of in with vs via per`
- Acronyms always fully uppercase: `URL HTML CSV JSON XML SQL PDF UUID API OCR DNS HTTP SSH GPU CPU VPN`
- Prefer spaces — never `snake_case` or `kebab-case` in doc names
- Names must read like clear menu commands

### Extensions
All file extensions lowercase: `.applescript .scpt .sh .py .js .md .json .yaml .csv`

### Never encode in filenames
These belong in script headers and docs — not the filename:
- Execution method (CLI, Finder, Menu, KM)
- Input source (Clipboard, Selection)
- Output destination (Desktop, Temp)
- UI hints (Dialog, Popup)

### Existing bad names — what to do
If a script already has a bad name (spaces, snake_case, wrong case):
1. **Suggest the rename to the user** before documenting
2. If approved: rename the script file, update any references, then document
3. If not approved: document with a note in the Improvements section flagging
   the naming issue for future cleanup
4. Never silently leave a bad name undocumented — surface it

---

## Action Taxonomy (MANDATORY)

Every script must have one **primary action** reflected in its name. Use these
verbs consistently — agents should not invent new action words:

| Verb group | Use for |
|------------|---------|
| `Get / Fetch / Download` | Retrieves data or files from external sources |
| `Show / List / Inspect` | Read-only display of information |
| `Convert / Format / Normalize` | Transforms format or representation |
| `Create / Generate / Scaffold` | Produces new output |
| `Update / Modify / Apply` | Mutates existing state |
| `Clean / Strip / Remove` | Destructive removal |
| `Run / Execute / Start / Stop` | Operational control |
| `Search / Find / Extract` | Locates or pulls out data |
| `Manage / Maintain` | Lifecycle operations |
| `Upload / Send / Share` | Pushes data out |

If a script does more than one thing, name it for the **primary** action.
When uncertain between two verbs, pick the one that describes the outcome the
user cares about, not the mechanism.

---

## Directory Structure

```
~/Scripts/
├── Apps/           # Actions targeting specific apps
├── Dev/            # Developer tools — see subfolder rules below
├── Languages/      # Language experiments (not yet general tools)
├── Media/          # Image, audio, video content
├── Productivity/   # Tasks, notes, reminders, time, finance
├── Riley/          # Personal/experimental scripts
├── System/         # macOS, hardware, network, processes, settings
├── Text/           # Text as primary subject
│   ├── Case/
│   ├── Convert/
│   ├── Filename/
│   ├── Format/
│   ├── Markdown/
│   ├── Regex/
│   │   ├── Extract/
│   │   ├── Clean/
│   │   └── Strip/
│   └── Utilities/
├── Utilities/      # Generic calculators, converters, generators
├── Web/            # APIs, downloads, search, scraping
└── ∗new/           # Staging — MUST be sorted before documenting
```

### Subfolder rule
Create subfolders only if 3+ scripts share a stable, durable concept.
Prefer clear names over deep trees.

### `∗new/` rule
Nothing in `∗new/` may be documented until it is sorted into the correct tree.
If you encounter scripts in `∗new/`, suggest the correct location to the user
before proceeding with anything else.

---

## Category Rules

| Category | What goes here |
|----------|---------------|
| `Apps/` | Actions targeting specific app windows |
| `Dev/` | Git, brew, build tools, lint, scaffold, DevOps — **see below** |
| `Languages/` | Language experiments, not yet general tools |
| `Media/` | Image/audio/video content operations |
| `Productivity/` | Tasks, notes, reminders, time, finance |
| `Riley/` | Personal/experimental scripts |
| `System/` | macOS, hardware, network, processes, settings, security |
| `Text/` | Text as primary subject: case, regex, filenames, Markdown |
| `Utilities/` | Generic calculators, converters, generators, dashboards |
| `Web/` | APIs, downloads, search, bookmarks, scraping |
| `∗new/` | Staging — sort before documenting |

### Dev/ subfolders (CRITICAL — this tree is functional, not tool-based)

| Subfolder | Use for |
|-----------|---------|
| `Dev/Build/` | Build, bundle, compile, release |
| `Dev/Format/` | Format code files (JSON, Python, shell etc) |
| `Dev/Lint/` | Lint and validate code |
| `Dev/Inspect/` | Read-only status checks (git status, dependency list) |
| `Dev/Manage/` | Restart servers, clear caches, lifecycle ops |
| `Dev/Scaffold/` | Create new projects, generate templates, README |
| `Dev/Brew/` | Homebrew install/upgrade/manage |
| `Dev/Git/` | Git operations and GitHub integrations |
| `Dev/Docker/` | Docker and container ops |
| `Dev/DevOps/` | AWS, Cloudflare, CI/CD, infrastructure |

### Tie-breakers

| Uncertain between | Choose | Reason |
|------------------|--------|--------|
| System vs Utilities | Utilities | Generic tools, not OS-specific |
| Apps vs Productivity | Apps | Targets specific app windows |
| Text vs Utilities | Text | Text/document is primary subject |
| Dev vs Languages | Dev | Developer tools vs language experiments |
| Dev/Inspect vs Dev/Manage | Inspect | Read-only → Inspect; mutates state → Manage |

### Enforcement rule (HARD)
If a script does not fit a folder → the folder is wrong, not the script.
If a script does not fit a name → the name is wrong.
**Do not bend rules. Fix the structure.**

---

## Documentation Workflow

### Step 1 — Destructive check FIRST
Before reading anything else: does this script modify or delete files?
If yes, mark `destructive: true` in the frontmatter and add the warning callout
to the Notes section. Do this now — it's easy to miss once you're in the code.

Scripts that are destructive: anything using `rm`, `mv`, `overwrite`, bulk
rename, file organisation, clearing caches, emptying trash.

### Step 2 — Read and analyse
1. Read the **entire** script — do not skip or skim
2. Understand functionality by analysing the code
3. Identify all dependencies from imports/requires/brew checks
4. Note issues, bad naming, and improvements

### Step 3 — Check naming
Is the script filename following kebab-case?
Is the name following the Action Taxonomy?

If no → suggest the correct name to the user before proceeding.
Get approval, rename, update references, then continue.

### Step 4 — Sort if in `∗new/`
If the script is in `∗new/`, suggest the correct category to the user.
Do not document until it is sorted.

### Step 5 — Suggest improvements to user FIRST
Before writing a single line of docs, present your findings:
```
While reviewing this script, I found some opportunities:
- **Bug**: [description] — should I fix it?
- **Enhancement**: [description] — would this be useful?
- **Rename**: [current] → [suggested] — follows naming conventions
- **Optimisation**: [description] — worth implementing?
```
**Wait for approval before making any changes.**

### Step 6 — Backup before any changes
```bash
cp "script.sh" "script.sh.bak.$(date +%Y%m%d-%H%M%S)"
```
Keep latest 3 backups per script. Clean up older `.bak.*` files.

### Step 7 — Make approved changes

### Step 8 — Test after changes
```bash
bash -n script.sh                    # Bash
osascript -s o script.applescript    # AppleScript
python3 -m py_compile script.py      # Python
node --check script.js               # JavaScript
swiftc -syntax-only script.swift     # Swift
```
If tests fail → restore from backup and reassess. Do not document broken code.

### Step 9 — Suggest alternatives to user
```
While documenting this script, I noticed:
- Have you considered [built-in tool]? Simpler because [reason]
- [Other script] in the repo does something similar
- Modern alternative: [tool] could replace this
```

### Step 10 — Identify category gaps, suggest to user
```
While documenting [category], I noticed some gaps:
- This category could use [script idea] — it would [benefit]
- No scripts for [app] integration yet
- The [toolkit] is missing [feature] — would complete it
```

### Step 11 — Create documentation
- Create `Script Name.md` (Smart Sentence Case) alongside the script
- Follow the documentation structure below exactly
- Source code must be exact and complete — no truncation

### Step 12 — Mirror to Obsidian
```bash
VAULT="/Users/rd/Library/Mobile Documents/iCloud~md~obsidian/Documents/Scripts"
mkdir -p "$VAULT/Category/Subcategory"
cp "Script Name.md" "$VAULT/Category/Subcategory/Script Name.md"
```
Use **capitalised folder names** and **Smart Sentence Case filenames** in Obsidian.

### Step 13 — Final verify
- [ ] Script filename is kebab-case
- [ ] Doc filename is Smart Sentence Case (correct conversion from kebab)
- [ ] Category is correct — not bent to fit
- [ ] `destructive: true` set if applicable
- [ ] Path uses `~/Scripts/` format (never `~/.scripts/`)
- [ ] Source code matches actual script exactly
- [ ] Improvements section populated
- [ ] Mirrored copy exists in Obsidian vault

---

## Documentation Structure

Every script doc must include these sections in order:

### 1. YAML Frontmatter
```yaml
---
title: "Script Name"
description: "Brief one-line description (max 80 chars)"
author: riley
category: [Category Name]
language: [bash|applescript|python|ruby|javascript|swift]
path: "~/Scripts/Category/script-name.ext"
destructive: true  # ONLY if script modifies or deletes files
tags:
  - script
  - [language]
  - [category]
  - [relevant-tags]
---
```

Note: `path` uses the kebab-case script filename, not the doc filename.

### 2. Title (H1)
```markdown
# Script Name
```

### 3. Overview (H2)
2–4 sentences: what it does, when to use it, key benefits. Be specific — no
generic descriptions that could apply to any script.

### 4. Features (H2)
3–5 actual features pulled from the code. Not generic. Not aspirational.
```markdown
## Features
- **Feature 1**: Description of what the code actually does
- **Feature 2**: Description
```

### 5. Dependencies (H2, if applicable)
```markdown
## Dependencies
**Tool Name** — what it's used for

Installation:
```bash
brew install tool-name
```
```

### 6. Usage (H2)
```markdown
## Usage

### Basic Usage
```bash
~/Scripts/Category/script-name.sh [arguments]
```

### With Options
[Additional examples — test these before writing them]
```

### 7. Script Details (H2)
```markdown
## Script Details
**File Path:** `~/Scripts/Category/script-name.ext`
**Language:** [language]
**Category:** [category]
```

### 8. Source Code (H2)
Complete, exact script content. No truncation. No paraphrasing. No "..." gaps.

### 9. Examples (H2)
Working examples. If you haven't tested them, say so.

### 10. Improvements (H2) — REQUIRED, always populated
```markdown
## Improvements

### Changes Made in This Pass
- **Fixed**: [what was wrong] → [what was fixed]
- **Renamed**: [old-name.sh] → [new-name.sh] — [reason]

### Future Suggestions
- **High priority**: [description and why]
- **Medium priority**: [description]
- **Naming**: [flag bad name if not fixed in this pass]
```

Must be populated. If nothing was changed and nothing needs improving, that
itself is worth stating. "No changes needed in this pass — script is clean."

### 11. Notes (H2) — REQUIRED for destructive scripts
```markdown
## Notes

> [!warning] Destructive Operation
> This script modifies or deletes files. Test on sample data first.

- Any other important caveats
- Known limitations or edge cases
```

### 12. Related Scripts (H2)
```markdown
## Related Scripts
- `Related Script Name.md` — brief description of relationship
- Other scripts in `~/Scripts/Category/`
```

---

## Code Review Checklist

Run this during Step 2. Surface issues in Step 5.

**Functionality**
- [ ] Does what it claims
- [ ] Edge cases handled (empty input, missing files, no network)
- [ ] Error conditions managed with useful messages

**Code Quality**
- [ ] Descriptive variable names
- [ ] Readable structure
- [ ] Comments explain complexity, not the obvious
- [ ] No redundant or dead code

**Modern Practices**
- [ ] Current macOS APIs (not deprecated)
- [ ] Language best practices followed
- [ ] Appropriate tool for the job (fd not find, rg not grep etc)

**Security**
- [ ] No hardcoded credentials or API keys
- [ ] Safe input handling
- [ ] Safe file operations (no `rm -rf` without confirmation)
- [ ] Minimal permissions

**Performance**
- [ ] Efficient for typical use case
- [ ] No unnecessary work or redundant calls
- [ ] Batch operations where possible

**UX**
- [ ] Clear error messages that explain what went wrong
- [ ] Progress indicators for long operations
- [ ] Sensible defaults — minimal required arguments
- [ ] Easy to modify and extend

---

## Enhancement Types (for Improvements section)

**Feature additions** — flags/options, additional input sources, output
formats, integrations with related tools

**Quality improvements** — input validation, better error messages, usage/help
text, edge case handling

**Performance** — parallel processing for batches, caching repeated calls,
more efficient algorithms

**UX** — progress indicators, confirmations before destructive actions,
coloured output, interactive mode vs script mode

---

## Quick Reference

### Syntax test commands
```bash
bash -n script.sh                    # Bash
osascript -s o script.applescript    # AppleScript
python3 -m py_compile script.py      # Python
node --check script.js               # JavaScript
swiftc -syntax-only script.swift     # Swift
```

### Backup
```bash
cp "script.sh" "script.sh.bak.$(date +%Y%m%d-%H%M%S)"
```

### Mirror to Obsidian
```bash
VAULT="/Users/rd/Library/Mobile Documents/iCloud~md~obsidian/Documents/Scripts"
mkdir -p "$VAULT/Category"
cp "Script Name.md" "$VAULT/Category/Script Name.md"
```

### Destructive warning callout
```markdown
> [!warning] Destructive Operation
> This script modifies or deletes files. Test on sample data first.
```

### Kebab → Doc name (quick examples)
```
get-current-weather.sh       →  Get Current Weather.md
extract-urls-from-text.sh    →  Extract URLs from Text.md
convert-json-to-csv.py       →  Convert JSON to CSV.md
run-ocr-on-image.applescript →  Run OCR on Image.md
toggle-dark-mode.applescript →  Toggle Dark Mode.md
upload-to-imgur.sh           →  Upload to Imgur.md
```

---

## Critical Rules (summary)

1. **Naming**: script files kebab-case, doc files Smart Sentence Case — always
2. **Action taxonomy**: every script name leads with an approved action verb
3. **Bad names**: surface to user, get approval, rename, then document
4. **`∗new/`**: sort before documenting — no exceptions
5. **Destructive check**: do this first, before reading the code
6. **Suggest first**: improvements to user → approval → backup → change → test → document
7. **Path format**: always `~/Scripts/` never `~/.scripts/`
8. **Source code**: exact copy, no truncation
9. **Improvements section**: always populated, always honest
10. **Structure is fixed**: if script doesn't fit → fix structure, don't bend rules
