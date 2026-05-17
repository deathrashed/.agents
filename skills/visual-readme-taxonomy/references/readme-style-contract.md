# README Style Contract

Use this reference while generating the final README.

## Iconify Syntax

Use Iconify through image URLs so the README works in GitHub-flavored Markdown without scripts:

```html
<img src="https://api.iconify.design/lucide:folder-tree.svg?color=%2388C0D0" width="18" height="18" alt="Folder tree icon">
```

For centered project headers:

```html
<p align="center">
  <img src="https://api.iconify.design/lucide:box.svg?color=%2388C0D0" width="96" height="96" alt="Project icon">
</p>

<h1 align="center">Project Name</h1>
```

For local icon assets, prefer HTML images with fixed dimensions:

```html
<p align="center">
  <img src="./assets/icon.svg" width="96" height="96" alt="Project icon">
</p>
```

For dark and light variants:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/icon-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/icon-light.svg">
  <img src="./assets/icon-light.svg" width="96" height="96" alt="Project icon">
</picture>
```

Do not use emoji, raw Unicode symbols, decorative glyph dividers, or symbol bullets. For visual bullets, use small Iconify image tags inside table cells or paragraphs.

## Badge Pattern

Use shields.io badges with relevant logos and clickable links:

```markdown
[![Shell](https://img.shields.io/badge/Shell-zsh-4EAA25?logo=gnubash&logoColor=white)](https://www.zsh.org/)
[![Docs](https://img.shields.io/badge/Docs-README-2F81F7?logo=readthedocs&logoColor=white)](#usage)
```

Choose badge color, logo, and destination based on discovered project context. Use Simple Icons slugs where available through shields.io `logo=`.

## Recommended README Skeleton

```markdown
<p align="center">
  <img src="ICON" width="96" height="96" alt="PROJECT icon">
</p>

<h1 align="center">PROJECT</h1>

<p align="center">
  BADGES
</p>

## Index

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Architecture](#architecture)
- [Taxonomy Notes](#taxonomy-notes)
- [Troubleshooting](#troubleshooting)
- [Maintenance](#maintenance)

## Overview

## Prerequisites

## Installation

## Usage

## Configuration

## Project Structure

## Architecture

## Taxonomy Notes

## Troubleshooting

## Maintenance
```

Adapt the skeleton to the project. Do not include empty sections.

## Taxonomy Table Pattern

```markdown
| Area | Current Role | Status | Recommendation |
| --- | --- | --- | --- |
| `src/` | Runtime source | Active | Keep as source boundary |
| `tmp/` | Generated files | Review | Move to ignored cache or archive |
```

## Command Table Pattern

```markdown
| Command | Purpose | Notes |
| --- | --- | --- |
| `npm run build` | Build production assets | Requires dependencies installed |
| `npm test` | Run test suite | Use before publishing changes |
```

## Mermaid Pattern

Use Mermaid only when it clarifies discovered workflow or architecture:

```mermaid
flowchart TD
  A[Input Path] --> B[Audit Structure]
  B --> C[Generate README]
  C --> D[Validate Links]
```

## GitHub Alert Pattern

```markdown
> [!IMPORTANT]
> Run `command` from the repository root so relative paths resolve correctly.
```

Use alerts sparingly and only for real project risks or setup requirements.

## GIF Workflow

If the target has no demo GIF and the user wants one, provide a separate workflow before final README generation:

```bash
# Record a short screen capture with a native recorder or a tool such as Kap.
# Convert MOV/MP4 to GIF with ffmpeg.
ffmpeg -i demo.mov -vf "fps=12,scale=1280:-1:flags=lanczos" -loop 0 assets/demo.gif
```

If the project has no `assets/` or `media/` folder, suggest creating one, but wait for user approval before editing.
