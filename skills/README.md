# Active Skill Surface (`skills/`)

This directory represents the **active runtime skill surface** scanned directly by AI agents (Codex, Claude Code, Antigravity, OpenCode, Gemini, etc.).

---

## Operating Model

1. **Lean Active Surface:**
   To keep context window usage optimal, `skills/` contains only the active skills currently loaded for active coding tasks (58 active skills).

2. **On-Demand Skill Fetching (`skill-fetch`):**
   Skills are stored in the canonical category library [`skillz/`](../skillz) or the specialized OMA suite [`.agents/skills/`](../.agents/skills).
   Use `skill-fetch` to search and symlink skills into `skills/`:
   ```bash
   skill-fetch search "react"
   skill-fetch get react-best-practices
   ```

3. **Cleanup:**
   To clear temporary skills after a task is finished:
   ```bash
   skill-fetch clear
   ```

---

## Active Skills Index

Each active skill is accessible via standard markdown instructions (`SKILL.md`) in its respective folder.
