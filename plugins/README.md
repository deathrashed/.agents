# Categorized Plugin Extensions & Packs (`plugins/`)

This directory contains modular plugin packs that extend AI coding assistant capabilities with specialized skills, subagents, and custom configurations.

---

## Plugin Categories

| Category | Role & Description | Key Plugins |
| :--- | :--- | :--- |
| **`code-quality/`** | Static analysis, code review standards, and refactoring guidelines. | `code-review` |
| **`examples/`** | Example plugin templates and developer playground scaffolds. | `example-plugin`, `playground` |
| **`integrations/`** | Agent SDK tools and third-party platform integrations. | `agent-sdk-dev` |
| **`lsp/`** | Language Server Protocol integrations (Clangd, Pyright, Lua LSP). | `clangd-lsp`, `pyright-lsp`, `lua-lsp` |
| **`other/`** | Miscellaneous extension packs. | Plugin utilities |
| **`output-styles/`** | Custom response styling and formatting templates. | Output formatters |
| **`platform/`** | OS and platform-specific automation plugins. | macOS automation |
| **`workflow/`** | Workflow automation, loops, hooks, and skill builders. | `claudeforge-skill`, `commit-commands`, `ralph-loop`, `hookify` |

---

## Plugin Architecture

A standard plugin pack includes:
- `plugin.json`: Metadata, versioning, author, and tool declarations.
- `skills/`: Packaged skills exposed by the plugin.
- `agents/`: Domain subagents bundled with the plugin.
- `.local.md`: User-configurable plugin settings with YAML frontmatter.
