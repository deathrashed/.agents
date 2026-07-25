# OMA (One-Man-Army) Agent & Skill Infrastructure (`.agents/`)

This directory houses the **One-Man-Army (OMA)** autonomous agent suite, execution protocols, and shared skill foundations.

---

## Directory Overview

- **`skills/`**: 33 specialized subagent skills covering end-to-end development, architecture, testing, media generation, and project management.
- **`skills/_shared/`**: Shared execution protocols, context loading rules, quality principles, and reasoning templates.

---

## OMA Skill Roster (`.agents/skills/`)

| Skill | Focus & Capabilities |
| :--- | :--- |
| **`oma-academic-writer`** | Publication-grade English drafting, anti-AI audit, prose revision. |
| **`oma-architecture`** | System architecture design, diagnostic routing, trade-off analysis (ATAM/CBAM). |
| **`oma-backend`** | REST APIs, database models, clean architecture (Repository/Service/Router). |
| **`oma-brainstorm`** | Design-first ideation, TRIZ-lite problem solving, constraint exploration. |
| **`oma-coordination`** | Multi-agent coordination for PM, Frontend, Backend, Mobile, QA via CLI. |
| **`oma-db`** | SQL/NoSQL schema modeling, index optimization, migrations, compliance. |
| **`oma-debug`** | Root cause diagnosis, bug fixing, error playbooks, regression test suites. |
| **`oma-deepsec`** | Vercel deepsec vulnerability scanning, PR security reviews, custom matchers. |
| **`oma-design`** | UX/UI design system, typography, motion design, WCAG 2.2 accessibility. |
| **`oma-dev-workflow`** | Monorepo task automation, CI/CD pipelines, release coordination. |
| **`oma-docs`** | Documentation drift detection, link verification, translation drift checks. |
| **`oma-explainer`** | Interactive HTML explainers with visual diagrams, code walkthroughs, quizzes. |
| **`oma-frontend`** | React, Next.js, Angular, FSD-lite architecture, Tailwind, shadcn/ui. |
| **`oma-hwp`** | HWP/HWPX/HWPML Korean document conversion to GFM Markdown. |
| **`oma-image`** | Parallel multi-vendor AI image generation (Codex, Antigravity, Pollinations). |
| **`oma-market`** | Pain-point extraction, SWOT/Porter's 5F analysis, competitive intelligence. |
| **`oma-mobile`** | Flutter, React Native, Swift iOS native development & optimization. |
| **`oma-observability`** | Telemetry, OpenTelemetry tracing, metrics, log analysis, SLO boundaries. |
| **`oma-orchestrator`** | Parallel multi-agent orchestration via MCP Memory and CLI subagents. |
| **`oma-pdf`** | High-fidelity PDF document parsing and Markdown extraction. |
| **`oma-pm`** | Requirement breakdown, task dependency graphs, ISO 21500 project planning. |
| **`oma-qa`** | Quality assurance, OWASP security audits, ISO 25010 testing standards. |
| **`oma-recap`** | Conversation history analysis and multi-model work summaries. |
| **`oma-refactor`** | Behavior-preserving code restructuring, code smell elimination. |
| **`oma-scholar`** | Scholarly research paper analysis, OpenAlex integration, sidecar specs. |
| **`oma-scm`** | Git workflow management, Conventional Commits, merge resolution. |
| **`oma-search`** | Intent-based trust-scored search routing (Docs, Web, Code). |
| **`oma-skill-creator`** | SSL-lite standard skill drafting and structure validation. |
| **`oma-slide`** | 1080p HTML presentation deck creation with animated transitions. |
| **`oma-tf-infra`** | Infrastructure-as-code with Terraform across AWS, GCP, Azure, Oracle. |
| **`oma-translator`** | Context-aware translation preserving technical register and tone. |
| **`oma-video`** | Short-form and explainer video generation with Remotion compositor. |
| **`oma-voice`** | On-device text-to-speech and speech-to-text via Voicebox MCP. |

---

## Execution Standards (`_shared/`)

- **`core/`**: API contracts, clarification protocols, context budget managers, quality principles, skill routing tables.
- **`runtime/`**: Execution protocols tailored for individual LLM runtimes (Antigravity, Claude Code, Codex, Grok, Qwen, Kimi, Kiro, Pi).
