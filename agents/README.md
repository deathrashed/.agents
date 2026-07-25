# Categorized Agent Definitions (`agents/`)

This directory contains specialized AI agent definitions, roles, and subagent persona specifications organized by domain categories.

---

## Domain Architecture

| Category | Description | Sample Agents & Roles |
| :--- | :--- | :--- |
| **`ai/`** | Ethics, governance, AI architecture, quantum computing, and model specialists. | AI Ethics Governance Specialist, Quantum Expert, Gemini Specialist |
| **`data/`** | Database administration, data science, performance optimization, analytics, and DAX/Power BI. | SQL Query Optimizer, Database Specialist, PostgreSQL DBA, Data Analyst |
| **`design/`** | UI/UX designers, accessibility architects, spatial design, and vision specialists. | UI Designer, UX Researcher, Vision Specialist |
| **`devops/`** | Infrastructure automators, Docker/K8s experts, monitoring/SRE, and release coordination. | DevOps Automator, Docker Expert, Monitoring/SRE Specialist, Rate Limiter |
| **`engineering/`** | Backend/Frontend engineers, fullstack devs, API designers, refactoring, and language experts (Python, Go, Java, C#, Swift). | Backend Architect, Frontend Developer, API Designer, Code Reviewer, Python Expert |
| **`other/`** | General subagents, research spikes, brand strategists, support responders, and cross-functional utilities. | Technical Writer, Brand Guardian, Research Spike Agent, Support Responder |
| **`product/`** | Product managers, PRD specialists, sprint prioritizers, B2B shippers, and growth hackers. | PRD Specialist, Sprint Prioritizer, Product Manager Advisor, B2B Project Shipper |
| **`security/`** | Security auditors, auth specialists, compliance automation, CORS, and legal advisors. | Security Auditor, Auth Expert, Compliance Automation Specialist, Legal Advisor |
| **`testing/`** | QA testing, Playwright automation, form validation, accessibility auditing, and unit test generation. | Quality Assurance Engineer, Playwright Tester, Unit Test Generator, Accessibility Auditor |

---

## Agent Specification Format

Each agent folder follows standard agent plugin or standalone Markdown structure:

1. **Manifest / Metadata (`.claude-plugin/plugin.json` or `manifest.json`):**
   Defines the agent name, version, description, and subagent routing attributes.

2. **Agent Definition File (`agents/<agent-name>.md` or `AGENT.md`):**
   Contains YAML frontmatter and detailed system instructions:
   ```markdown
   ---
   name: backend-architect
   description: Architecture specialist for APIs, databases, microservices, and clean architecture.
   ---
   
   # Backend Architect Persona & Guidelines
   ...
   ```

---

## Integration & Runtime Usage

- **Claude Code & Antigravity (AGY):** Subagents can be invoked dynamically via subagent routing tools (`invoke_subagent`).
- **Custom Workflows:** Agents can be loaded into specific subagent execution pipelines or paired with domain skills in `.agents/skills/`.
