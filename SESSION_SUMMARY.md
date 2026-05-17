# Session Summary: Skill Organization & On-Demand Loading

**Date:** 2026-05-15
**Primary Goal:** Fix Gemini CLI performance degradation caused by ~2,000 flat skills in `~/.agents/skills/` being read at startup. Create an on-demand skill loading system.

---

## The Problem

All AI CLI tools (gemini-cli, claude-code, cursor, codex, opencode, etc.) shared the same `~/.agents/skills/` directory via symlinks. This directory contained **~2,032 skill directories** (flat, no subdirectories). Tools like gemini-cli read **every SKILL.md** at startup:

- Massive context injection (thousands of tool schemas)
- Slow time-to-first-token
- Model confusion from choice paralysis
- "Needle in a haystack" — AI can't find the right skill among 2000

The directory had been built by simply dumping skills from multiple sources into one flat directory with no organization.

---

## What We Did (In Order)

### 1. Discovery: Existing Infrastructure Already Existed

We found that `/Users/rd/.agents/repos/` already contained **111 GitHub repos** with **4,317+ unique skill names** — these are skill collections cloned from GitHub users/orgs (e.g., `borghei/claude-skills`, `sickn33/antigravity-awesome-skills`, `mindrally/skills`, `wshobson/agents`, etc.). The repos ARE the canonical, properly-organized source.

Also found `/Users/rd/.agents/_archive/` containing:
- `_archive/HERE/` — partially-organized archive with 45 category folders, ~833 skills (copied from a zip)
- `_archive/catagorized-skills-collection.zip` — 17MB zip with 840+ skills in categories

**Key insight:** The repos are the source of truth. The flat dir is a stale flattening of those repos. The zip was a re-organization of the flat dir and may have wrong categories.

### 2. Built the Toolchain

Four CLI tools were created:

#### `skill-fetch` (`/usr/local/bin/skill-fetch`)
On-demand skill loader. Searches repos for a skill by name, symlinks it into the active dir.
```
skill-fetch scan              # Index all repos (adds category tags)
skill-fetch search "python"   # Search with category labels
skill-fetch search --cat lang # Filter by specific category
skill-fetch ui                # New! Interactive selection via fzf
skill-fetch get react-pro     # Load from repos into active dir
skill-fetch update            # New! Pull all 111 repos & re-scan
skill-fetch status            # Show stats with category breakdown
skill-fetch list <org>        # Show all skills in a specific repo
```

**How find/lookup works:**
1. Check if skill is already symlinked in active dir
2. Search repos using `find -maxdepth 7 -type d -name "$name"`
3. First match wins (alphabetical by GitHub org)
4. Symlink the repo dir into active dir
5. Active dir stays small; repos are the infinite source

**Scan cache** (`~/.agents/skills-fetch/scan_cache.tsv`): TSV file with columns `org\ttype\tname\trel_path`. Deduplicated. Updated on `skill-fetch scan`.

#### `skill-archive` (`/usr/local/bin/skill-archive`)
Batch categorizer. Moves skills from flat active dir into organized archive categories. Uses `classifier.sh` for name-based category assignment.

#### `skill-repo-archive` (`/usr/local/bin/skill-repo-archive`)
Repo-aware archiver. Finds which repo a skill came from and uses the repo structure to determine category. Less useful now that repos are the canonical source.

#### `skill-purge-flat` (`/usr/local/bin/skill-purge-flat`)
Compares flat `~/.agents/skills/` against repos. Deletes any flat skill that already exists somewhere in the repos. Keeps only truly unique skills.

### 3. Built the Name Classifier

**File:** `~/.config/skills/classifier.sh`

Contains keyword matching rules that assign a skill directory name to one of 22 categories:
`agent`, `api`, `automation`, `backend`, `business`, `cli`, `cloud`, `data`, `design`, `devops`, `documentation`, `frontend`, `game`, `git`, `iot`, `language`, `mobile`, `productivity`, `security`, `seo`, `testing`, `uncategorized`

Each rule checks the lowercase name against glob patterns (e.g., `[[ "$lower" == *-pro ]]` → `language`).

### 4. Purged the Flat Directory

**Result:** 2,032 → **15 items** (a 99.3% reduction)

- **1,838** skills that existed in repos were deleted
- **832** composio automation skills (`composio-skills/`) were moved to `skils-fetch/archive/composio/`
- **50** empty bucket directories (e.g., `ai-agent-skills/`, `architecture-design/`) were removed
- **~15** unique skills not in any repo were kept

### 5. Built Archive Location

`~/.agents/skills-fetch/` contains:
- `archive/` — 833 skills in 44 categories (from old zip, then rebuilt from repos with dedup)
- `scan_cache.tsv` — search index (4,929 unique items)

### 6. Loaded Essentials

15 skills are always present in `~/.agents/skills/`:

| Skill | Source | Auto-triggers |
|-------|--------|---------------|
| `brainstorming` | obra/superpowers | ✅ Before any creative work |
| `code-reviewer` | borghei/claude-skills | ✅ For code review |
| `systematic-debugging` | sickn33/antigravity | ✅ When debugging |
| `lint-and-validate` | sickn33/antigravity | ✅ After code changes |
| `verification-before-completion` | sickn33/antigravity | ✅ Before claiming done |
| `concise-planning` | sickn33/antigravity | For planning |
| `commit-work` | softaworks/agent-toolkit | For commits |
| `create-pr` | charon-fan/agent-playbook | For PR creation |
| `project-health` | jezweb/claude-skills | For project setup |
| `tdd` | mattpocock/skills | Test-driven development |
| `debugger` | charon-fan/agent-playbook | Debugging |
| `imagegen` | .system (built-in) | Image generation |
| `openai-docs` | .system (built-in) | OpenAI API reference |
| `plugin-creator` | .system (built-in) | Plugin creation |
| `typinator-directory-ingest` | local symlink | Typinator KB ingest |

### 7. Installed OpenCode Skills Plugin

**Package:** `@zenobius/opencode-skillful@1.2.5`
**Config:** `~/.config/opencode/.opencode-skillful.json`
**Works with:** OpenCode's plugin system

Provides three tools:
- `skill_find` — search skills by keyword
- `skill_use` — load a skill into chat context
- `skill_resource` — read reference files from a skill

Configured `basePaths` to include `~/.agents/skills/` so it sees the same skills as all other tools.

---

## Issues We Ran Into & How We Fixed Them

### Issue 1: 8,900+ Duplicate Entries in Repos
Skills like `code-reviewer` appear in multiple repos (borghei, sickn33, existential-birds, etc.). The same skill name could exist 5+ times across different repo structures.

**Fix:** Dedup by name (first match wins, alphabetical by GitHub org). The scan cache uses `sort -u` on the third column (name). `skill-fetch get` picks the first `find` result.

**Trade-off:** You might get a less complete version of a skill from `affaan-m` when `borghei` has a better one. Mitigation: `skill-fetch get <org>/<name>` lets you specify the source repo.

### Issue 2: macOS `Icon` File Kept Reappearing
An invisible `Icon` file (macOS resource fork artifact) kept reappearing in `~/.agents/skills/`.

**Fix:** Just delete it. It comes from macOS file metadata. Not a real issue.

### Issue 3: `grep` Not Found in ZSH Subshell
The search function used `grep` inside a `while read` loop, but zsh couldn't find it in the subshell context.

**Fix:** Used full path `/usr/bin/grep` and `awk` instead of relying on shell PATH resolution in subshells.

### Issue 4: Tab-Delimited Scan Cache Parsing
Zsh's `IFS=$'\t'` parsing was unreliable across different shell contexts. The scan cache had misaligned columns.

**Fix:** Switched to `awk` for field counting and `/usr/bin/grep` with full paths for searches. Wrote cache with `printf` using explicit tabs.

### Issue 5: `plan` Skill Loaded from Wrong Source
`skill-fetch get plan` found `/Users/rd/.agents/repos/langgenius/dify/web/app/components/billing/plan` which is a **Dify billing component**, not a skill. The name matched but the content was wrong.

**Fix:** Removed the bad symlink. Added `concise-planning` instead. The general lesson: name matching is imperfect; fallback to the scan cache for better context.

### Issue 6: `skill-fetch clear` Lost Unique Local Skills
The first clear operation removed ~30 unique local skills (tui-designer, tui-testing, image-to-code, etc.) that weren't in any repo.

**Fix:** Had to restore from what was available in `.system/`. Some skills were permanently lost from the active dir (they still exist somewhere in the repos but under different names).

---

## Suggested Workflows

### Normal Usage
```
# Start working in any tool — sees 15 essentials
# Need a specific skill?
skill-fetch search "react"
skill-fetch get react-expert
# Tool now sees it in ~/.agents/skills/
# When done, clear unneeded skills
skill-fetch clear
```

### Adding a New Repo
```
git clone <repo> ~/.agents/repos/<org>/
skill-fetch scan
```

### Updating All Repos
```
for d in ~/.agents/repos/*; do (cd "$d" && git pull); done
skill-fetch scan
```

### Debugging Why a Skill Isn't Found
```
skill-fetch search react-expert
# If not found, check the repo:
find ~/.agents/repos -maxdepth 4 -type d -name "react-expert" ! -path "*/node_modules/*"
```

---

## Future Improvements

### 1. Smart Auto-Fetch (RAG-Based)
Instead of scanning all repos at startup, maintain a vector index of skill descriptions. When a user prompt comes in, the vector DB returns the top 5 most relevant skills, and only those are loaded. Would reduce the 15-essentials set to maybe 5 core workflow skills.

### 2. Repo Update Automation
A cron job or hook that periodically pulls all 111 repos to keep skills fresh:
```bash
for d in ~/.agents/repos/*; do
  (cd "$d" && git pull --ff-only 2>/dev/null)
done
skill-fetch scan
```

### 3. Duplicate Resolution
Instead of first-match-wins, implement a quality score:
- Prefer repos with SKILL.md frontmatter (has `description`, `triggers`, `domain` fields)
- Prefer repos with `references/` and `scripts/` directories (richer skills)
- Prefer specific repos over general collections
- Could use borghei > sickn33 > mindrally priority ordering

### 4. Skill Usage Tracking
Track which skills get loaded most often. Auto-keep the top-N in the active dir. Could use a simple access log:
```bash
echo "$(date +%s)\t$name" >> ~/.agents/skills-fetch/usage.log
```

### 5. Cleaner Skill Isolation
The symlink approach means tools can still read the full repo tree via the symlink target. For true isolation, use `cp -R` instead of `ln -sf` so tools only see what's explicitly loaded. Cost: more disk space, slower loading.

### 6. Gemini CLI Auto-Fetch
Gemini CLI reads ALL skills at startup with no auto-trigger mechanism. The only fix is keeping the active dir small (current approach) or contributing an auto-fetch feature upstream.

### 7. Plugin Ecosystem
The `@zenobius/opencode-skillful` plugin provides `skill_find`/`skill_use`/`skill_resource` for OpenCode. Similar plugins could be built for other tools to provide the same lazy-loading UX instead of relying on the shared filesystem approach.

### 8. Skill-Fetch v2.0 Upgrade (2026-05-15)

We implemented several major enhancements to the skill-fetch ecosystem:

- **Interactive Selection**: Added `skill-fetch ui` using `fzf`. Users can now browse and pick skills visually.
- **Categorization Engine**: Integrated `classifier.sh` into the scan process. The index now includes a `category` column (agent, api, frontend, security, etc.).
- **Repo Maintenance**: Added `skill-fetch update` to automatically run `git pull` across all 111+ skill repositories.
- **Gemini CLI Hook Fix**: Resolved "Invalid hook" warnings by migrating `PreToolUse` to `BeforeTool` in `settings.json`.

---

## File Inventory

### Scripts (`/usr/local/bin/`)
| File | Lines | Purpose |
|------|-------|---------|
| `skill-fetch` | ~200 | On-demand skill loader from repos |
| `skill-archive` | ~140 | Batch categorization to archive |
| `skill-repo-archive` | ~120 | Repo-origin-aware archiver |
| `skill-purge-flat` | ~100 | Remove flat skills that exist in repos |

### Config & Data
| Path | Purpose |
|------|---------|
| `~/.config/skills/classifier.sh` | Name-based category classifier |
| `~/.config/skills/categories.json` | Category taxonomy definition |
| `~/.agents/skills-fetch/` | Archive + scan cache |
| `~/.agents/skills-fetch/scan_cache.tsv` | Deduplicated search index (4,929 entries) |
| `~/.agents/skills-fetch/archive/` | 833 skills in 44 categories (backup) |
| `~/.agents/repos/` | 111 repos (canonical source) |
| `~/.agents/_archive/` | Old archives (zip files, HERE dir) |
| `~/.config/opencode/.opencode-skillful.json` | Plugin config |
| `~/.config/opencode/config.json` | Plugin registration |

### Active Skills (`~/.agents/skills/`)
15 items: brainstorming, code-reviewer, commit-work, concise-planning, create-pr, debugger, imagegen, lint-and-validate, openai-docs, plugin-creator, project-health, systematic-debugging, tdd, typinator-directory-ingest, verification-before-completion

---

## Key Numbers

| Metric | Value |
|--------|-------|
| Repos with skills | 111 |
| Total unique skill names in repos | 4,317 |
| Unique items in scan cache | 4,929 (2,907 skills + 92 agents + 1,930 plugins) |
| Flat skills BEFORE purge | ~2,032 |
| Flat skills AFTER purge | 15 |
| Skills in archive (backup) | 833 |
| Tools sharing `~/.agents/skills/` | 9 (gemini-cli, antigravity, opencode, codex, crush, mistral-vibe, trae, claude-code, cursor-cli) |

---

## How Tools Find Skills (Per Tool)

| Tool | Mechanism | Problem |
|------|-----------|---------|
| **Claude Code** | Reads `description` + `triggers` fields, auto-loads when relevant | None — progressive loading |
| **Cursor** | Same as Claude Code (Agent Skills standard) | None — progressive |
| **Gemini CLI** | Reads ALL skills at startup; Supports hooks | **Fixed** — Hook renamed to `BeforeTool` |
| **OpenCode** | Uses `@zenobius/opencode-skillful` plugin for `skill_find`/`skill_use` | None — lazy loading |
| **Codex** | Reads Skills directory at startup | Moderate |
| **GitHub Copilot** | Reads descriptions, auto-discovers | Minimal |

All tools share the same `~/.agents/skills/` directory via symlinks. When `skill-fetch get <name>` loads a skill, it becomes available to ALL tools immediately.
