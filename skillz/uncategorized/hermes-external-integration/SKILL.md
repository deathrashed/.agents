---
name: hermes-external-integration
description: "Make Hermes Agent data (memory, sessions, skills) accessible to external AI coding tools via MCP."
version: 1.0.0
author: Riley
metadata:
  hermes:
    tags: [MCP, Integration, External-Tools, Memory-Bridge]
    related_skills: [native-mcp, hermes-agent]
---

# Hermes External Tool Integration

## When to Use

When the user asks to:
- "Make Hermes memory/sessions/skills available to my other AI tools"
- "Register Hermes with opencode/codex/kilo/gemini-cli/antigravity/VS Code"
- "Set up an MCP bridge so other coding assistants can see Hermes data"
- "Share Hermes context with my other agents"
- "Add Hermes as an MCP server to my IDE"

Any task involving exposing Hermes persistent data to third-party AI coding tools.

## Approach

Build a centralized MCP server that reads Hermes data sources directly and exposes them as MCP tools. One server serves all tools from the same backend — avoids fragmented memory stores.

The deployed server lives at `~/.hermes/bin/hermes-mcp`. Register it with each tool's MCP config.

## Data Sources

| Data | Source | Access |
|------|--------|--------|
| User profile / preferences | `~/.hermes/memories/USER.md` | Read file, parse sections |
| Environment facts | `~/.hermes/memories/MEMORY.md` | Read file, parse sections |
| Session transcripts | `~/.hermes/state.db` (SQLite FTS5) | SQL query |
| Skills library | `~/.hermes/skills/` | List/read filesystem |

## Building the MCP Server

Create a Python script at `~/.hermes/bin/hermes-mcp`. Three key patterns:

### 1. Stdio MCP I/O — use line-buffered reading

MCP communicates over stdin/stdout using JSON-RPC. **Never** read byte-by-byte — it causes persistent timeouts. Always use line-buffered `for line in sys.stdin:`:

```python
import sys, json

sys.stdin.reconfigure(line_buffering=True)

buffer = ""
for line in sys.stdin:
    buffer += line
    while "\n" in buffer:
        line, buffer = buffer.split("\n", 1)
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue
        # Handle initialize / tools/list / tools/call
```

### 2. Tool registration

Expose tools via the `initialize` + `tools/list` response. Each tool needs `name`, `description`, `inputSchema`:

```python
RESPONSE_TOOLS = {
    "tools": [
        {
            "name": "hermes_memory_search",
            "description": "Search Hermes persistent memory (USER.md / MEMORY.md) for facts about the user, environment, or past configurations.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search term to find in memory files"}
                },
                "required": ["query"]
            }
        },
        {
            "name": "hermes_memory_read",
            "description": "Read a full Hermes memory file.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "source": {"type": "string", "description": "Which memory file to read", "enum": ["user", "memory"]}
                },
                "required": ["source"]
            }
        },
        {
            "name": "hermes_session_search",
            "description": "Search past Hermes conversation sessions using full-text search.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "FTS5 search query"},
                    "limit": {"type": "integer", "description": "Max results"}
                },
                "required": ["query"]
            }
        },
        {
            "name": "hermes_skill_list",
            "description": "List all installed Hermes skills with descriptions.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "category": {"type": "string", "description": "Optional category filter"}
                },
                "required": []
            }
        },
        {
            "name": "hermes_skill_view",
            "description": "View a skill's full content.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Skill name"}
                },
                "required": ["name"]
            }
        }
    ]
}
```

### 3. Session search via SQLite FTS5

The `~/.hermes/state.db` has FTS5 virtual tables for full-text search:

```python
import sqlite3, os

def session_search(query, limit=10):
    conn = sqlite3.connect(os.path.expanduser("~/.hermes/state.db"))
    conn.row_factory = sqlite3.Row
    cursor = conn.execute("""
        SELECT s.id, s.title, s.created_at,
               m.content, m.role, m.id as msg_id
        FROM sessions s
        JOIN messages_fts f ON f.rowid = m.rowid
        JOIN messages m ON m.id = f.rowid
        WHERE messages_fts MATCH ?
        ORDER BY rank
        LIMIT ?
    """, (query, limit))
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return results
```

## Registration by Tool

After building the server, register it with each tool. The deployed server is at `~/.hermes/bin/hermes-mcp`.

### codex

```bash
codex mcp add hermes -- /Users/rd/.hermes/bin/hermes-mcp
```

Config: `~/.codex/config.toml` → `[mcp_servers.hermes]`

### gemini-cli

```bash
gemini mcp add hermes /Users/rd/.hermes/bin/hermes-mcp --scope user --trust
```

Config: `~/.gemini/settings.json` → `mcpServers`

### opencode (manual JSON edit)

File: `~/.config/opencode/opencode.json`

Add to root `"mcp"` object:

```json
"hermes": {
  "command": ["/Users/rd/.hermes/bin/hermes-mcp"],
  "enabled": true,
  "type": "local"
}
```

### kilo (manual JSON edit)

File: `~/.config/kilo/kilo.json`

Add to root `"mcp"` object:

```json
"hermes": {
  "type": "local",
  "command": ["/Users/rd/.hermes/bin/hermes-mcp"]
}
```

### antigravity (main app)

File: `~/.gemini/antigravity/mcp_config.json`

Add under `"mcpServers"`:

```json
"hermes": {
  "command": "/Users/rd/.hermes/bin/hermes-mcp",
  "description": "Access Hermes Agent memory, sessions, and skills"
}
```

### agy

No direct MCP CLI. Inherits from Gemini CLI's MCP config via plugin import. If agy has the `context7` or `skillz` plugins, it auto-discovers MCP servers registered with gemini-cli. No separate config file needed.

### VS Code / antigravity-ide

Requires a Cline or Continue extension config. Check for:
- `~/.config/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`
- Or the editor's own `settings.json` `mcp` block

The `antigravity-ide` MCP directory (`~/.gemini/antigravity-ide/mcp/<name>/`) stores function-definition JSONs (name, description, parameters), not MCP server command configs — may not support stdio MCP servers directly.

## Verification

Test the MCP server directly:

```bash
printf '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}\n{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}\n' | ~/.hermes/bin/hermes-mcp
```

Verify registration in each tool:

```bash
codex mcp list | grep hermes
grep -A3 hermes ~/.gemini/settings.json
grep -A3 hermes ~/.config/opencode/opencode.json
grep -A3 hermes ~/.config/kilo/kilo.json
grep -A3 hermes ~/.gemini/antigravity/mcp_config.json
```

## Pitfalls

- **Byte-by-byte stdin reading**: Causes MCP timeouts. Always use line-buffered `for line in sys.stdin:` with `sys.stdin.reconfigure(line_buffering=True)` and flush stdout after each response.
- **Command vs array format**: Some tools (opencode, kilo) expect the command as a JSON array of strings. Others (antigravity, gemini-cli, codex) expect a single string. Always check the tool's existing config format before registering.
- **antigravity-ide MCP format**: Uses function-definition JSONs (name + description + parameters), not full MCP server command configs. If the user wants this integration, try the Cline extension path instead.
- **agy MCP**: No dedicated CLI. Relies on Gemini config inheritance. If inheritance is broken, agy may not support MCP at all — check the plugins.
- **Security/trust**: Some tools (opencode, kilo) require explicit permission grants for new MCP servers. The user may need to approve the new server in the tool's UI or config.
- **Path must be absolute**: Always use absolute paths for the MCP server executable in all config files.
- **Flush after each response**: Always call `sys.stdout.flush()` after writing each JSON-RPC response, otherwise the client may hang waiting for output.
