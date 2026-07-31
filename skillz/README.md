# Categorized Skill Source Library (`skillz/`)

This directory serves as the canonical source library for all skill definitions, reference documents, and helper scripts organized into domain category folders with sub-categories.

---

## Category Subfolders

| Category | Description | Sub-categories |
| :--- | :--- | :--- |
| **`ai-agent-skills`** | Meta-skills about building agents, commands, plugins, hooks, and skills. | agents, commands, hooks, plugins, skills, ecosystem |
| **`ai-ml`** | AI/ML model development, LLMs, RAG, embeddings, and evaluation. | llm, rag-embeddings, frameworks, training, evaluation |
| **`automation`** | Workflow automation, n8n, browser automation, and API integrations. | n8n, integrations, browser-automation, platforms |
| **`business`** | Business functions: sales, marketing, SEO, ads, HR, legal, finance, strategy. | sales-crm, marketing, seo, ads, hr-people, legal, finance, strategy |
| **`cloud-devops`** | Cloud infrastructure, CI/CD, observability, and platform engineering. | aws, azure, gcp, kubernetes, ci-cd, iac, observability |
| **`coding`** | Programming language and framework patterns. | typescript, python, rust, go, java, dotnet, cpp |
| **`communication`** | Professional writing, email, meetings, and presentations. | writing, email, meetings, presentations |
| **`creative-media`** | Image, video, audio, 3D, animation, and design tools. | image, video, audio, 3d, animation, design-tools |
| **`data`** | Databases, analytics, ETL, data science, and spreadsheets. | databases, analytics, etl, data-science, spreadsheets |
| **`design`** | UI/UX design, design systems, CSS, accessibility, brand, and prototyping. | ui-ux, design-systems, css, accessibility, brand, prototyping |
| **`dev-workflows`** | Code review, refactoring, TDD, debugging, profiling, and dev productivity. | code-review, refactoring, tdd, debugging, profiling, productivity |
| **`documentation`** | Documentation engineering: API docs, project docs, ADRs, changelogs, knowledge. | api-docs, project-docs, adr, changelog, knowledge |
| **`game-dev`** | Game development, engines, 2D, 3D, and game design. | engines, 2d, 3d, design |
| **`git`** | Version control workflows, commits, pull requests, and tooling. | workflows, commits, pr, tools |
| **`google`** | Google ecosystem: Gemini API, Google Cloud, Workspace. | gemini, cloud, workspace |
| **`linux`** | Linux administration, shell scripting, networking, and security. | administration, shell, networking, security |
| **`mcp`** | Model Context Protocol: servers, tools, configuration, and patterns. | servers, tools, configuration, patterns |
| **`mobile`** | Mobile development for iOS, Android, and cross-platform frameworks. | ios, android, cross-platform |
| **`planning`** | Product planning, project management, roadmaps, and estimation. | prd, project-management, roadmap, estimation |
| **`platform`** | Platform/tool-specific skills (OMX, SpecStory, RepoPrompt, etc.). | opencode, specstory, repo-prompt, ecosystem, cursor, brave-search |
| **`productivity`** | Personal knowledge management, time management, workflows, and goals. | knowledge, time, workflows, goals |
| **`security`** | Security auditing, penetration testing, web/cloud security, compliance, auth. | auditing, pentesting, web-security, cloud-security, compliance, auth |
| **`testing`** | Software testing: unit, integration, E2E, performance, and QA. | unit, integration, e2e, performance, qa |
| **`utilities`** | File processing, formatting, regex, conversion, and CLI tools. | file-processing, formatting, regex, conversion, cli |
| **`web`** | Web development: frontend, frameworks, APIs, browser, performance, state. | frontend, frameworks, api, browser, performance, state |

### Internal / Platform Categories

These ship with specific tools or are personal infrastructure, not general-purpose skills:

| Category | Description |
| :--- | :--- |
| **`oh-my-codex`** | OMX system commands (`plan`, `doctor`, `code-review`, etc.). |
| **`codex`** | OpenCode/Codex runtime internals. |
| **`superpowers`** | Superpowers plugin skills (brainstorming, TDD, worktrees). |
| **`riley`** | Personal macOS automation (macro-creator, zsh, etc.). |
| **`system`** | Skill library infrastructure (skillz-discovery, find-skills). |

## Operating Mechanics

- **Source Library:** `skillz/` holds the permanent skill code, templates, and reference materials.
- **Runtime Surface:** `skills/` contains active flat symlinks pointing to items in `skillz/` or `.agents/skills/`.
- **Search & Read:** Use the always-on `skillz-discovery` skill to search `skillz/`, plugin-internal `skills/` trees under `plugins/`, and `repos/`, then read the selected `SKILL.md` directly. Do not symlink a skill into `skills/` just to use it.
- **Optional Activation:** `skill-fetch` remains available for intentionally maintaining the active surface. It scans both `skillz/` (curated, priority) and `repos/` (upstream), so `skill-fetch search` and `skill-fetch get` resolve curated skills first.
