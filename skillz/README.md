# Categorized Skill Source Library (`skillz/`)

This directory serves as the canonical source library for all skill definitions, reference documents, and helper scripts organized into domain category folders.

---

## Category Subfolders

| Category Bucket | Description |
| :--- | :--- |
| **`agent-browser`** | Browser automation CLI & browser control skills. |
| **`ai-agent-skills`** | Agent development, command creation, and plugin structure. |
| **`automation`** | Workflow automation & n8n patterns. |
| **`cloud-devops`** | Cloud deployment, incident management, trace observability, and entropy reduction. |
| **`codex`** | OpenAI Codex specific rules and execution specs. |
| **`coding`** | React, Angular, Python PPTX, OpenAPI, Zustand, and framework patterns. |
| **`communication`** | Professional writing, technical communication, and feedback. |
| **`content-docs`** | Documentation engineering & content creation. |
| **`creative-media`** | Image generation, video composition, and audio tools. |
| **`cursor`** | Cursor IDE specific rules and skills. |
| **`design`** | UI/UX design systems, accessibility, and CSS patterns. |
| **`dev-catagory`** | Development category classification tools. |
| **`dev-stack`** | Technology stack specific guidelines. |
| **`dev-workflows`** | Code review, refactoring, TDD, and Git workflows. |
| **`documentation`** | Documentation writing and API specs. |
| **`git`** | Conventional commits, branching, worktree strategies. |
| **`google`** | Gemini API dev & Google Cloud platform. |
| **`inbox-staged`** | Newly imported or staged skills pending full categorization. |
| **`linux`** | Linux administration and shell scripting. |
| **`mcp`** | Model Context Protocol server configuration & tool skills. |
| **`openai`** | ChatGPT apps SDK, Assistants API, and OpenAI skill mirrors. |
| **`planning`** | PRD planning, project management, and task breakdown. |
| **`productivity`** | Planning with files, NotebookLM, PRD planning, and time management. |
| **`riley`** | Macro creator, Keyboard Maestro, and custom Mac automation scripts. |
| **`security`** | Dependency auditing, web security testing, OWASP, and site audit. |
| **`skills-cursor`** | Additional Cursor rulesets. |
| **`specstory`** | SpecStory project statistics and file organization skills. |
| **`superpowers`** | Superpowers plugin skills (TDD, worktrees, plan execution, parallel agents). |
| **`system`** | macOS system automation and shell configuration. |
| **`uncategorized`** | Standalone skills awaiting category assignment. |
| **`utilities`** | File organization, code formatting, and general utilities. |
| **`web`** | Web APIs, scraping, Zustand state, Next.js, and frontend patterns. |

---

## Operating Mechanics

- **Source Library:** `skillz/` holds the permanent skill code, templates, and reference materials.
- **Runtime Surface:** `skills/` contains active flat symlinks pointing to items in `skillz/` or `.agents/skills/`.
- **Search & Read:** Use the always-on `skillz-discovery` skill to search `skillz/`, plugin-internal `skills/` trees under `plugins/`, and `repos/`, then read the selected `SKILL.md` directly. Do not symlink a skill into `skills/` just to use it.
- **Optional Activation:** `skill-fetch` remains available for intentionally maintaining the active surface, but it is not required for ordinary skill discovery.
