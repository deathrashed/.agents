# Gemini Configuration for Claude Code

## Project Overview
This repository contains the source code for "Claude Code," an AI-powered CLI tool. It is a multi-language project featuring a main TypeScript/Bun CLI and auxiliary Rust-based implementations.

## Directory Structure
- `claude-code/`: The primary CLI application.
  - **Runtime:** Bun.
  - **Source:** TypeScript files located in the root (with a `src` symlink).
  - **Key Modules:**
    - `mcp/`: Model Context Protocol implementation.
    - `tools/`: Built-in tools for the AI agent (Bash, FileEdit, etc.).
    - `claudemd.ts`: Implements hierarchical memory loading from `CLAUDE.md` and related files.
    - `auth.ts`: Authentication logic.
- `claw-code-main/` / `claw-code-parity/`: Rust-based workspaces.
  - `rust/`: Contains the Cargo workspace and CLI/runtime implementation.
  - `src/` / `tests/`: Rust source and validation surfaces.

## Tech Stack
- **Primary:** TypeScript (Bun), Rust.
- **Terminal UI:** Ink.
- **Validation:** Zod.
- **Ecosystem:** Integrated with Anthropic's SDK and Model Context Protocol.

## Development Workflows
- **TypeScript (claude-code):** Use Bun for execution and testing.
- **Rust (claw-code):**
  - Formatting: `cargo fmt`
  - Linting: `cargo clippy --workspace --all-targets -- -D warnings`
  - Testing: `cargo test --workspace`

## Coding Standards
- **Surgical Edits:** Prefer targeted changes to existing `.ts` and `.rs` files.
- **Instruction Precedence:** Adhere to hierarchical instructions as processed by the `claudemd` logic.
- **Environment:** Be mindful of macOS-specific configurations and hardware constraints (e.g., 8GB RAM limit).
