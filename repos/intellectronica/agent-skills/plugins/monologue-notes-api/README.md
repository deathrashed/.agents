# monologue-notes-api

Use this skill when the user wants to read or search their Monologue notes through the Monologue Notes REST API. It covers authentication with the MONOLOGUE_API_KEY environment variable, safe token handling, listing notes, fetching a single note, pagination, filters, and error handling. The API is read-only and should be accessed with direct HTTP requests such as curl or any equivalent REST client.

## Installation

### Claude Code / Cowork

```bash
claude plugin marketplace add intellectronica/agent-skills
claude plugin install monologue-notes-api@intellectronica-skills
```

### npx skills

```bash
npx skills add intellectronica/agent-skills --skill monologue-notes-api
```

---

> This plugin is auto-generated from [skills/monologue-notes-api](../../skills/monologue-notes-api).
