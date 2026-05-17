---
name: visual-readme-taxonomy
description: Generate or update a comprehensive, highly visual README.md for a specified local path or folder while auditing project taxonomy, stale documentation references, icons, badges, demos, and repository structure. Use when the user asks to create a polished README, improve README visual structure, document a local project, audit folder organization before documentation, add README badges/diagrams/callouts, choose project icons, or align documentation with local style references.
---

# Visual README Taxonomy

Generate a polished `README.md` for a local project only after inspecting the target path and pausing at required decision points.

## Required Inputs

- Target local path or folder. If missing, ask for it before doing any other work.
- Existing project name/title, if the path does not make it obvious.

## Workflow

1. Analyze the target path.
   - Inspect the folder tree, key files, package/build configs, scripts, docs, tests, and generated artifacts.
   - Infer purpose, primary languages, runtime, install surface, important commands, and project archetype.
   - Audit taxonomy: identify misplaced files, duplicate docs, stale paths, generated/cache material, archive candidates, and missing boundaries.
   - Check existing docs for stale or broken relative path references. Offer to update those docs, but do not change them unless the user approves.

2. Read the style references.
   - Inspect these files when available and imitate their structure, visual density, badges, tables, section rhythm, and formatting patterns:
     - `/Users/rd/Scripts/Riley/audio/download/deemon/README.md`
     - `/Volumes/Apfspace/Icons/README.md`
     - `/Users/rd/.config/zsh/README.md`
   - If any reference file is missing, continue with the available references and mention the missing path.

3. Select a primary icon and pause.
   - Suggest one primary project icon after checking local assets first:
     - target project assets and existing README media
     - `/Volumes/Apfspace/Icons`
     - `https://github.com/deathrashed/iconography` only if local icon evidence is insufficient or the user asks for web-backed choices
   - Present the suggested icon, source path or URL, and reason.
   - Pause and ask the user to confirm the icon or provide an alternative before writing the final README.

4. Assess demonstration GIFs and pause when needed.
   - Search the target path for existing `.gif` demos and referenced media.
   - If no suitable GIF exists, ask whether the user wants one before README generation.
   - If yes, provide a distinct sub-workflow with terminal commands or tool recommendations for recording and converting a screen capture to GIF, then wait for the user to supply or approve media.
   - If no, continue without demo GIFs and use static diagrams/tables instead.

5. Generate `README.md`.
   - Read `references/readme-style-contract.md` before drafting.
   - Preserve accurate relative links for the README location.
   - Use project-specific commands discovered from source files, not generic placeholders.
   - Do not overwrite an existing README until you have inspected it and can preserve useful project-specific content.

## Output Rules

- Use no emojis.
- Use no raw Unicode symbols for bullets, dividers, visual accents, or status markers.
- Use Iconify-backed image tags for inline icons and decorative visual accents.
- Use standard Markdown headings: `##`, `###`, and below.
- Add a centered header with the confirmed icon and project title.
- Add clickable, theme-matched shields/badges below the title.
- Add a top-level table of contents with anchor links.
- Add repository-specific sections for prerequisites, installation, usage, configuration, commands, taxonomy, architecture/workflow, troubleshooting, and maintenance.
- Use Markdown tables for variables, dependencies, commands, arguments, and taxonomy findings.
- Use Mermaid diagrams when architecture or workflow relationships are discoverable.
- Use `<details>` and `<summary>` for verbose configuration, long command lists, large examples, or changelog-like material.
- Use GitHub alerts for critical setup, destructive commands, platform assumptions, or known limitations.
- Use strict language tags on all fenced code blocks.
- Use theme-responsive media via `<picture>` or GitHub dark/light suffixes when embedding local assets with alternate variants.

## Safety

- Do not delete, rename, or move project files during README generation.
- Do not perform taxonomy cleanup automatically. Report suggested moves separately.
- Do not fabricate URLs, badges, dependencies, commands, or screenshots.
- Prefer omission over guessed external links.
