---
name: cmux-hooks
description: Manage and understand cmux agent integration hooks. Use when setting up agent CLIs inside cmux (Claude Code, Codex, OpenCode, Agent IDE), configuring session resume for agent surfaces, or setting up notification hooks in cmux.json.
---

# cmux Hooks (Agent Integration)

`cmux hooks setup` installs one or more AI agent CLIs into cmux so they appear in the workspace surface tab bar and can be launched as agent surfaces. Hooks are cmux's agent-integration framework.

## What Hooks Do

They surface agent CLI sessions as first-class cmux surfaces (tabs with proper lifecycle, reconnection, and sidebar metadata). Not background daemons — they "hook into" the session lifecycle of each agent.

## Supported Agents

| Agent | Config Path | Notes |
|-------|------------|-------|
| Claude Code | `~/.clauderc` | Reconnects to existing sessions |
| Codex CLI | `~/.codex/claude-agit.json` | — |
| OpenCode | `~/.config/opencode/opencode.json` | Supports session resume |
| Agent IDE | `~/.config/cmux/agent-ide.json` | — |

## Setup

```bash
# Interactive — prompts for each detected agent
cmux hooks setup

# Targeted by agent name
cmux hooks setup claude
cmux hooks setup codex
cmux hooks setup opencode
cmux hooks setup agent-ide
```

The setup command:
1. Detects whether each agent CLI is installed
2. Creates (or touches) the agent's config file with cmux-compatible settings
3. Registers the agent in cmux's surface tab bar

After setup, use the surface tab bar buttons or Command Palette to launch an agent session. Each session gets its own workspace surface with reconnection support.

## What Hooks Are NOT

Not background watchers, daemons, or event listeners. No `cmux hooks watch` or `cmux hooks run`. The name refers to how cmux hooks into each agent's session lifecycle — starting, stopping, and reconnecting agent surfaces.

## Session Resume

When paired with `cmux session-restore`, agent surfaces persist across app restarts:

```bash
cmux config set session.restore true
```

On relaunch, agent surfaces reconnect to their running CLI processes. Works for Claude Code and OpenCode (both support session IDs).

## Notification Hooks (Separate Feature)

`cmux.json` also supports `notifications.hooks` — event-driven hooks for processing notifications (filtering, transforming, or posting to external services). Unrelated to agent hooks:

```jsonc
{
  "notifications": {
    "hooks": [
      {
        "type": "exec",
        "command": "/path/to/script",
        "filter": {
          "event": ["surface.finished"],
          "match": { "content": "error" }
        }
      }
    ]
  }
}
```

See `cmux docs notifications` for full API.

## Config File Changes Made by `hooks setup`

- **Claude Code**: creates/updates `~/.clauderc` with `"cmux": { "enable": true, "autoReconnect": true }`
- **Codex**: touches `~/.codex/claude-agit.json` with cmux socket path
- **OpenCode**: touches `~/.config/opencode/opencode.json` with cmux socket path

## Verification

```bash
# List hooks status
cmux hooks list
# or
cmux hooks status

# Check topology for agent surfaces
cmux identify --json
```

## Pitfalls

- Agent hooks only work for agent CLIs that support session attach/detach (Claude Code and OpenCode are known-good; Codex v1 may not fully resume)
- Notification `hooks` in cmux.json are YAML-like JSONC — keep filters tight to avoid banner noise
- `cmux hooks setup` registers agents in the surface tab bar by default; remove unwanted ones via `cmux.json` `ui.surfaceTabBar.buttons`
