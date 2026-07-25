---
name: repo-taxonomy-architect
description: Use when cleaning up a repository, reorganizing files or folders, auditing project taxonomy, fixing inconsistent naming, managing legacy/archive files, structuring a project/monorepo/dotfiles repo, or generating safe repository refactoring and migration plans.
---

# Repository Taxonomy & Organization Architect

## Overview
Deeply analyze, map, and restructure repositories to improve discoverability, consistency, developer ergonomics, and long-term maintainability without breaking functionality.

## When to Use

### Trigger Symptoms & Use Cases
- **File & Directory Chaos:** Duplicated files (`utils-final`, `utils-new-2`), bloated root directory (20+ files in root), or confusing duplicate file basenames (`index.js`).
- **Unclear Boundaries:** Business logic mixed with static assets, generated build output committed alongside source code, or clutter in active directories.
- **Refactoring & Scaling:** Transitioning from unstructured scripts to structured projects, or migrating from layer-based to feature-based architectures as codebase grows.
- **Repository Setup & Governance:** Structuring a new or existing monorepo, dotfiles repo, CLI, SDK, or multi-language application.

### When NOT to Use
- Single-file quick scripts or trivial line edits within an established file.
- Routine code refactoring that does not change file locations, naming conventions, or directory structures.

## 5 Universal Architectural Principles

1. **Predictability:** File locations should be intuitive; if you have to guess where a file belongs, taxonomy has failed.
2. **Separation of Concerns:** Keep business logic, configuration, static assets, and generated artifacts in distinct domains.
3. **Scalability:** The layout must support growth from 5 files to 500+ files without structural breakdown.
4. **Consistency Over Creativity:** Use standard, boring folder names (`config/`, `modules/`, `tests/`) over custom or ambiguous ones (`stuff/`, `chaos/`).
5. **Progressive Structuring:** Start simple and add directories only as needed ("scale when it hurts"). Premature over-structuring is premature optimization.

## Universal & Archetype Structures

### Universal Baseline Structure (90% of Projects)
```cs
project/
├── src/
│   ├── core/         # Shared business logic & primitives
│   ├── modules/      # Feature modules or domain logic
│   ├── utils/        # Generic, reusable helper functions
│   ├── config/       # Environment & runtime configuration
│   └── main.*        # Primary application entry point
├── tests/            # Test suites (unit, integration, e2e)
├── public/           # Static assets, images, public files
├── scripts/          # Build, CI/CD, and operational tooling
├── docs/             # Technical & architectural documentation
├── .env / .gitignore
├── README.md
└── [package.json | Cargo.toml | go.mod | pyproject.toml | pom.xml]
```

### Small / Lightweight Version
For utility tools, small CLI scripts, or early-stage projects:
```cs
project/
├── src/
│   └── main.*
├── tests/
└── README.md
```

### Architectural Scaling Styles for Large Projects

#### Feature-Based Architecture (Recommended for Growing Apps)
Groups by domain/feature rather than technical layer to keep related logic self-contained and co-located:
```cs
src/
├── auth/          # controller, service, model, routes, tests
├── user/          # controller, service, model, routes, tests
└── dashboard/     # controller, service, model, routes, tests
```

#### Layer-Based Architecture (Classic)
Groups by technical layer (`controllers/`, `services/`, `models/`, `routes/`). Clean initially, but can become unmanageable in large apps. Transition to Feature-Based when layer directories grow too large.

## Operational Rules & Safety Mandate

*   **Inspect & Map First:** Map the complete repository tree before proposing changes. Infer existing naming standards and preserve project style.
*   **Reference Integrity Check:** NEVER rename or move files without scanning and updating imports, scripts, configs, docs, and build manifests.
*   **Safe Execution:**
    *   Prefer dry-runs and explicit user approval before executing file operations.
    *   Always use `git mv` (or VCS equivalents) to preserve file history.
    *   Move legacy/deprecated items to `archive/` or `.trash-review/` instead of hard deletion.

## File Classification & Taxonomy Audit

Classify repository files into distinct operational tiers:
- **Active Source & Docs:** `src/`, `lib/`, `app/`, `docs/`, `scripts/`
- **Configuration:** `config/`, `.env`, build manifests
- **Static Assets & Templates:** `public/`, `assets/`, `templates/`
- **Quality & Lifecycle:** `tests/`, `fixtures/`, `archive/`, `deprecated/`
- **Generated & Transient:** `dist/`, `build/`, `cache/`, `logs/` (ensure isolated & gitignored)

### Common Violations to Resolve
- Generated artifacts, build output, or logs committed in source trees.
- Root folder clutter (keep root restricted to standard configs and top-level manifests).
- Over-reliance on generic `/helpers` or `/utils` as junk drawers.
- Mixing environment secrets (`.env`) or config files into domain source code.

## Output Deliverables

When invoked, generate a **Taxonomy & Organization Audit Report**:
1. **Repository Map & Archetype Assessment:** Current structure, identified archetype, and inferred conventions.
2. **Taxonomy Audit:** Misplaced files, taxonomy violations, root clutter, and junk-drawer folders.
3. **Restructuring Plan:** Proposed target directory layout (Baseline, Feature-Based, or Archetype-Specific).
4. **Action & Migration Plan:** Step-by-step `git mv` plan, reference update list, `.gitignore` updates, and rollback instructions.

## Next Steps Gating
1. Present the Audit Report to the user.
2. Request explicit user approval for proposed file moves and refactoring steps.
3. Execute approved changes using `git mv` while simultaneously updating all affected file references.