---
name: typinator
description: General Typinator skill for syntax, forms, scripts, pickers, exports, Includes resources, and direct .tyset editing. Use when working on Typinator abbreviations, sets, scripts, menus, exports, documentation, or Typinator package structure.
---

# Typinator Skill

## Goal

Work correctly with Typinator as a whole:
- expansion syntax
- input forms and pickers
- Includes scripts, reference assets, and text resources
- exported CSV/TXT sets when they are explicitly in scope
- direct `.tyset` rule-set editing
- organized script/reference architecture

This is a general Typinator skill first, not just an export-auditing skill.

## Environment assumptions

- Typinator Includes path:
`/Users/rd/.config/typinator/Sets/Includes`
- Typinator local docs and resources are maintained in Includes:
`/Users/rd/.config/typinator/Sets/Includes`

## Source-of-truth locations

Prioritize these in this order when both exist:
1. Local Typinator documentation and runtime resources in Includes:
`/Users/rd/.config/typinator/Sets/Includes`
2. Direct Typinator exports (format authority for import-compatible CSV/TXT shape):
`/Users/rd/.config/typinator/Sets/Includes/Exported/Direct Exports`

Interpretation:
- For Typinator behavior and syntax, prefer `Includes/Documentation`.
- For runtime source assets referenced by abbreviations, pickers, and lookup scripts, prefer `Includes/Reference`.
- For reusable insertable text and templates, prefer `Includes/Text`.
- For import-compatible exported file format, prefer `Direct Exports`.
- Ignore old vault/Obsidian references unless the user explicitly asks for them.

## Documentation model

Treat the local Includes tree as three layers:
- `Includes/Documentation`
  Canonical reference material, user guides, scripting docs, regex docs, and long-form reference.
- `Includes/Reference`
  Runtime CSV/TXT assets and lookup sources that abbreviations, pickers, and scripts reference.
- `Includes/Text`
  Curated reusable insertable text resources, examples, and templates.

Current interpretation:
- prefer `Includes/Documentation` for formal behavior and feature rules
- use `Includes/Reference` for CSV/search/terminal/runtime lookup material
- use `Includes/Text` for snippets, template fragments, and include-friendly text
- do not merge these categories blindly; organize by purpose

## Mandatory doc-first read

Before generating or editing non-trivial expansions, read these files in Includes:

1. Canonical scripting behavior:
- `/Users/rd/.config/typinator/Sets/Includes/Documentation/Canonical/Creating-Typinator-Scripts.md`
- `/Users/rd/.config/typinator/Sets/Includes/Documentation/Canonical/Typinator™ Scripting Guide.md`

2. Canonical regex behavior:
- `/Users/rd/.config/typinator/Sets/Includes/Documentation/Canonical/Typinator™ Regular Expressions.md`

3. Operational references and user-facing patterns:
- `/Users/rd/.config/typinator/Sets/Includes/Documentation/Guides/0 - Introduction for AI Models.md`
- `/Users/rd/.config/typinator/Sets/Includes/Documentation/Guides/1 - Typinator Complete Reference.md`
- `/Users/rd/.config/typinator/Sets/Includes/Documentation/Guides/2 - Advanced Features & Techniques.md`
- `/Users/rd/.config/typinator/Sets/Includes/Documentation/Guides/3 - Quick Search & Productivity Tips.md`
- `/Users/rd/.config/typinator/Sets/Includes/Documentation/Guides/4 - Text Formatting & Hyperlinks.md`
- `/Users/rd/.config/typinator/Sets/Includes/Documentation/Guides/5 - Tips Tricks & Workflows.md`
- `/Users/rd/.config/typinator/Sets/Includes/Documentation/Guides/Typinator User's Guide.md`
- `/Users/rd/.config/typinator/Sets/Includes/Documentation/Reference/*.md`
- `/Users/rd/.config/typinator/Sets/Includes/Reference/**/*.md`
- `/Users/rd/.config/typinator/Sets/Includes/Reference/**/*.txt`
- `/Users/rd/.config/typinator/Sets/Includes/Reference/**/*.csv`
- `/Users/rd/.config/typinator/Sets/Includes/Text/**/*.md`
- `/Users/rd/.config/typinator/Sets/Includes/Text/**/*.txt`

When guidance conflicts, prefer Ergonis-origin scripting/regex docs above all derivative notes.

## Core rules

1. Output valid Typinator syntax only.
2. Keep UI tokens compact to avoid blank-line leakage.
3. Use readable labels for form fields.
4. Avoid giant inline option payloads when values are complex.
5. Prefer menu/picker patterns for large sets, but keep them maintainable.
6. For reference-backed lookup menus, prefer a small Includes script with one parameter over large inline `{/Shell ...}` heredocs inside the expansion.
7. Menu-returned reference text is inserted verbatim; do not expect fetched text to be re-expanded by Typinator. Use literal placeholders like `<SOURCE>` in reference files instead of `{{?...}}`.
8. Default to keeping original exports untouched and writing cleaned copies, except when the user explicitly targets `Direct Exports` for in-place content-only edits.
9. Use canonical script paths in exports and live rules.
10. If abbreviation length constraints are requested, enforce them globally.
11. Edit content only unless explicitly asked otherwise: do not change file type, extension, delimiter, quoting mode, encoding, BOM, newline convention, or export dialect.
12. When working from Direct Exports, preserve exact import format and only modify abbreviation/expansion text content.
13. For `.tyset` updates, do not edit package internals directly (`Index`, `X*` files); use Typinator's AppleScript dictionary to create/update rule sets and rules safely.
14. Treat scripts with spaces in filenames as unsafe for direct Typinator placeholders when parameters are involved; prefer no-space wrapper scripts or renamed canonical script files.
15. Prefer direct `.tyset` editing for live sets when the user wants the installed Typinator sets changed.
16. Use exported CSV/TXT files when the user explicitly wants import/export artifacts changed.

## Script correctness rules

1. Script invocation format:
- `{folder/scriptName argument}` with optional single argument.
- Typinator supports one argument only; split it inside the script when multiple values are needed.

2. Parameter hint comments must match language syntax exactly:
- AppleScript: `-- parameter: ...`
- JavaScript: `//-- parameter: ...`
- Shell/Python/etc.: `#-- parameter: ...`
- Swift: `//-- parameter: ...`

3. Runtime and UX constraints:
- AppleScript should complete in under about one second when possible.
- Other script types are hard-terminated at about five seconds.
- Do not show dialogs/alerts in scripts unless the user explicitly wants an interactive helper.

4. File and interpreter rules:
- JavaScript for Typinator must be compiled `.scpt`.
- Shell/Python/Ruby/Swift scripts must be executable and use a valid shebang.
- If a script filename contains spaces and the placeholder also needs a parameter, prefer a wrapper/alias with no spaces in the filename.

5. Prefer Unicode-safe environment access:
- In AppleScript, use `on expand(str, env)` when Unicode fidelity matters.

6. Special return behaviors:
- Use `{{cancelExpansion=yes}}` to abort expansions when prerequisites are missing.
- Use `{{bs=N}}` to consume typed prefix characters when implementing prefix-driven transforms.
- Return assignments as `{{var=value}}...` when persisting state.

## Workflow

1. Decide the target format first.
- Live installed set change: update the `.tyset` through Typinator scripting.
- Import/export artifact change: update exported CSV/TXT safely.
- Includes/runtime capability change: update scripts, reference assets, docs, and text resources under `Includes`.

2. Read the relevant local docs before editing non-trivial syntax or scripts.

3. Audit exports only when exports are actually involved.
- Use `scripts/interactive_fix_exports.py` and `scripts/normalize_exported_sets.py` for export cleanup.
- For `Direct Exports`, do not run transformations that alter dialect/line endings unless explicitly requested.

4. Fix syntax quality.
- Convert `{form:name}` to `{{?name}}` where needed.
- Remove artifacts like `<Skip if null>`.
- Fix malformed markers such as `{Shell/`.

5. Add enhancements.
- Add high-value snippets or picker rules.
- Add master menus only when they actually improve usability.

6. Canonicalize script references before finalizing exports or live rules.
- Rewrite alias-style references to canonical organized script paths.
- Prefer no-space wrapper scripts when Typinator placeholder parsing would otherwise break.

7. Validate script semantics when applicable.
- Verify marker forms, argument count assumptions, and parameter comments.
- Ensure scripts are non-interactive when used as plain expansion helpers.
- Verify the actual placeholder path is Typinator-safe.

8. Document changes.
- Update or add a concise guide in the same folder.
- List new abbreviations and behavior notes.

9. When user targets a `.tyset` package directly.
- Treat `.tyset` as application-managed package storage.
- Perform edits through `osascript` and Typinator scripting classes (`rule set`, `rule`) using `make`, `set`, `delete`, and lookups by set/rule.
- Verify by re-reading rule counts and sample abbreviations from Typinator after changes.
- Rule descriptions/comments are part of the live set and should be updated along with expansions when they clarify behavior.
- Live `.tyset` editing is the default path for installed-set changes.

10. When exports are involved, run final validation before claiming completion.
- Use `scripts/validate_typinator_exports.py`.
- Treat validator errors as blockers for export-focused work.

## When to use references

- Syntax and dialog patterns: `references/syntax-and-ux.md`
- Master menu architecture: `references/master-menu-patterns.md`
- Set-specific enhancement ideas: `references/set-enhancement-ideas.md`
- Runtime structure and source-of-truth paths: `references/runtime-structure.md`
- Local documentation map: `references/documentation-map.md`
- Documentation cleanup strategy: `references/documentation-cleanup.md`
- Live set editing and `.tyset` operations: `references/live-set-editing.md`
- Set grouping and naming strategy: `references/set-taxonomy.md`
- Scripts, wrappers, and placeholder-safe paths: `references/scripts-and-placeholders.md`
- Handy local utility scripts: `references/handy-scripts.md`
- Required validation checks: `references/quality-gates.md`
- End-to-end task playbooks: `references/workflows.md`
- Deep-read canonical Typinator doc notes: `references/core-doc-notes.md`
- Export validator usage and pass criteria: `references/export-validation.md`
- Canonical alias-to-path mapping policy: `references/script-manifest.md`

## Utilities

- `scripts/audit_typinator_tree.py`
Generates a topology audit of the Typinator tree. Useful for large cleanup or migration work, not required for ordinary rule authoring.

- `scripts/build_master_menu.py`
Builds/updates a one-abbreviation master menu for a CSV set.

- `scripts/build_master_menu_includes.py`
Builds a master menu using Includes-hosted exports/resources by default.

- `scripts/build_script_manifest.py`
Builds a canonical script manifest for organized Includes scripts and deprecated aliases.

- `scripts/convert_form_placeholders.py`
Converts non-Typinator placeholder styles to Typinator input fields.

- `scripts/interactive_fix_exports.py`
Interactive fixer for exported CSV sets.

- `scripts/normalize_exported_sets.py`
Creates cleaned copies with line-ending and Unicode cleanup. Export-focused utility.

- `scripts/validate_typinator_exports.py`
Runs strict export validation. Export-focused utility.

## Deliverables

When editing Typinator assets, provide what matches the target:
- Live `.tyset` changes when the installed set was edited
- Updated CSV/TXT files when export artifacts were edited
- Added/updated Includes scripts/docs/text resources when runtime support changed
- A short change summary with exact abbreviations, rules, scripts, or docs changed
