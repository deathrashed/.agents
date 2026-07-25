# Categorized Slash Commands & Workflows (`commands/`)

This directory contains executable slash commands, CLI workflow scripts, and automated prompt procedures organized by operational domains.

---

## Command Categories

| Category | Role & Purpose | Key Commands |
| :--- | :--- | :--- |
| **`code-gen/`** | Automated code generation, boilerplate scaffolding, and refactoring scripts. | `react-component`, `api-endpoint`, `crud-generator` |
| **`debugging/`** | Systematic debugging, stacktrace analysis, and error diagnosis workflows. | `systematic-debugging`, `error-audit`, `log-analyzer` |
| **`docs/`** | Documentation generation, enhancement, drift checking, and README polishing. | `enhance-claude-md`, `doc-verify`, `readme-gen` |
| **`infrastructure/`** | Terraform, cloud setup, Docker containerization, and CI/CD pipelines. | `tf-deploy`, `docker-scaffold`, `ci-pipeline` |
| **`other/`** | Miscellaneous utilities, helper scripts, and multi-purpose triggers. | `utility-helpers`, `script-runner` |
| **`planning/`** | Implementation planning, PRD specs, task breakdown, and goal alignment. | `plan-feature`, `prd-breakdown`, `task-scaffold` |
| **`review/`** | Code reviews, security audits, PR checks, and quality assurance workflows. | `code-review`, `pr-review`, `security-audit` |

---

## Command Structure & Parameters

Slash commands use YAML frontmatter for trigger conditions and execution parameters:

```markdown
---
description: Run a structured code review against staged changes or target branch.
argument-hint: [branch-or-commit]
---

# Code Review Procedure
...
```

---

## Execution & Usage

- **Interactive Execution:** Trigger commands directly in compatible CLI runtimes via `/command-name` (e.g. `/plan`, `/review`).
- **Automated Workflow Integration:** Invoked programmatically by orchestrator agents (e.g. OMA orchestrators or conductor plugins).
