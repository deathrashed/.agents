# Categorized MCP Servers & Integrations (`mcp/`)

This directory houses Model Context Protocol (MCP) server definitions, schemas, bridges, and API integrations organized by functional categories.

---

## MCP Categories

| Category | Description | Sample Servers & Integrations |
| :--- | :--- | :--- |
| **`ai-ml/`** | Machine learning, LLM bridges, vector search, and model integrations. | Perplexity, Gemini Bridge |
| **`browser/`** | Web scraping, headless browser automation, and visual testing tools. | Playwright, Puppeteer, DevTools |
| **`cloud-apis/`** | Cloud provider management (AWS, Azure, GCP, Cloudflare, n8n). | Cloudflare MCP, Google Workspace, n8n |
| **`comms/`** | Messaging platform bridges (Slack, Discord, Email, Deemon). | Deemon Deezer CLI, Slack Bridge |
| **`data/`** | Financial data, weather APIs, currency conversion, and search engines. | CoinGecko, AlphaVantage, Open-Meteo, Excalidraw |
| **`dev-tools/`** | Code intelligence, search, Git integrations, and developer tools. | Greptile, Fetch, Mikrotik, Notion |
| **`other/`** | Smithery server configs and uncategorized protocol bridges. | Smithery AI CLI configs |

---

## MCP Server Layout

Each MCP server subdirectory typically contains:
- `mcp_config.json`: Server connection settings, env variables, and command arguments.
- `<tool_name>.json`: Schema definitions for lazily-loaded MCP tools.
- `instructions.md`: Integration guidance and best practices.

---

## Registration & Usage

- **Eager Tools:** Registered natively under `mcp_<server>_<tool>` and callable directly.
- **Lazy Tools:** Tool schema loaded on demand via `call_mcp_tool`.
- **Global Config:** Referenced in global MCP settings (`~/.gemini/antigravity-cli/mcp/` or `~/.claude/mcp.json`).
