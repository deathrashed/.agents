# Dynamic Validation & Safe Execution

As the Codebase Architect, your audit must be grounded in reality. You are required to run the code to detect failing tests, syntax errors, and type issues. However, you must do this safely.

## Execution Rules

### 1. Identify the Tech Stack
Before running any commands, look for configuration files that define the stack and available commands:
- **Node.js/TypeScript:** Look for `package.json`. Read the `scripts` block to find test and lint commands (e.g., `npm run test`, `npm run lint`).
- **Python:** Look for `pytest`, `flake8`, `mypy` in `requirements.txt`, `Pipfile`, or `pyproject.toml`.
- **Go:** Look for `go.mod`. Use `go test ./...` and `go vet ./...`.
- **Rust:** Look for `Cargo.toml`. Use `cargo test` and `cargo clippy`.

### 2. Run Commands Safely
- **DO NOT** install global packages or heavy dependencies without asking the user first. 
- If a project is missing dependencies (e.g., `node_modules` is not present), you may run a localized, non-destructive install (e.g., `npm ci` or `npm install --ignore-scripts`) ONLY if necessary to run tests.
- **DO NOT** run scripts that mutate production state or deploy code (e.g., avoid `npm run deploy`, `npm start`, or `make release`).
- Focus on read-only, static validation: `test`, `lint`, `typecheck`, `build` (if safe).

### 3. Handle Missing Validation
If the repository has no tests or linters configured:
- Report this as a **Critical Finding** in your audit.
- Do not attempt to run complex guessed commands. 
- Instead, in your "Frictionless DevEx & Scaffolding" output, draft the configuration files to implement testing and linting from scratch.

### 4. Use the Heatmap
Always run the `scripts/repo_heatmap.py` script at the beginning of your workflow to get a bird's-eye view of the codebase. Use this data to identify bloated files and complex directories before digging into the source code.
