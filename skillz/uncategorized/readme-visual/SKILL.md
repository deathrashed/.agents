---
name: readme-visual
description: Use when creating or updating a README.md file for any repository, project, environment, tool, pipeline, knowledge base, or CLI app to generate a visually stunning, polished README matching local design standards.
---

# README Visual

Generate high-impact, beautifully formatted `README.md` files modeled directly on the 6 canonical local workspace README standards (`Mp3tag`, `Zsh`, `KB`, `go-genres`, `blogger-pipeline`, `clipped`).

---

## When to Use

Use this skill whenever:
- Asked to create, write, generate, improve, refactor, or polish a project `README.md`.
- Documenting a local project, CLI utility, shell config, automation pipeline, desktop app, or knowledge base.
- Adding visual structure (hero blocks, badges, Iconify headers, directory trees, interactive tables, collapsible sections, or video/image showcase grids) to project documentation.

Do NOT use when:
- Writing pure inline code comments or non-README documentation files.
- Generating plain unformatted raw text files without Markdown/HTML formatting.

---

## Visual Design Standard (The 6 Archetypes)

Every generated README must follow one of the 6 canonical visual archetypes detailed in `references/local-visual-archetypes.md`:

| Archetype | Primary Focus | Signature Elements |
| --- | --- | --- |
| **1. Mp3tag Collection** | Modular bundles & collections | Centered hero block, `# 𝗠𝗣𝟯𝗧𝗔𝗚` title, dark `#1e1e1e` shields with gold `#faa701` logo accents, inline dot navigation `·`, collapsible `<details><summary>` blocks with horizontal dividers `────────`. |
| **2. Zsh Shell Config** | Environments & shell configs | Banner hero image, dark shields, feature list with Unicode glyph accents (`- **ϟ Fast**`, `- **⁂ Modular**`), ASCII load order diagram, performance benchmark tables. |
| **3. KB System Base** | Knowledge bases & infrastructure | System architecture matrix (`Layer \| Detail`), storage volume strategy table (`Volume \| Path \| FS \| Size \| Role`), domain mapping matrix. |
| **4. Go CLI Utility** | Go binaries & multi-provider CLI apps | Cyan badges (`#01acd7`), pipe navigation `\|`, Iconify API SVG section headers (`## <img src="..."/>`), provider table with embedded cell icons. |
| **5. Blogger Pipeline** | Python/Shell API automation & bots | Centered logo icon, black badges (`black`), readmecodegen or animated SVG section header icons, dependency tables, security & verification checklists. |
| **6. Clipped Toolkit** | Multimedia toolkits & desktop apps | Centered logo asset (`width="144"`), green Iconify SVG table of contents header (`%2311c866`), HTML showcase grid table with side-by-side video/image previews (`<table width="100%">`), Keyboard Maestro macro table. |

---

## Mandatory Visual Elements Checklist

Every README generated using this skill MUST include:

1. **Centered Header Hero Block (`<div align="center">`)**:
   - Project logo, SVG icon, or banner graphic.
   - Styled or uppercase Title (`# 𝗠𝗣𝟯𝗧𝗔𝗚`, `<h1>GO·GENRES</h1>`, `# BLOGGER PIPELINE`, `# CLIPPED`, or `# Project`).
   - One-sentence bold summary statement of core utility.
   - Shields.io badge row with dark base (`#1e1e1e` or `#111111`), `style=for-the-badge`, and custom accent logo colors (`logoColor=white` or `logoColor=faa701`).
   - Quick navigation bar (`[Quick Start](#quick-start) • [Features](#features) ...` or HTML/Markdown links).

2. **Iconify or SVG Section Headers**:
   - `## <img src="https://api.iconify.design/mdi:rocket-launch-outline.svg?color=%2301acd7" height="22"> Quick Start`
   - Use URL-encoded color hexes (`#` becomes `%23`): Cyan `%2301acd7`, Green `%2311c866`, Red `%23ff2a1f`, Gold `%23faa701`.

3. **Quick Start Code Block**:
   - Positioned immediately near the top for instant onboarding (clone, build, execute).

4. **Structured Data Tables**:
   - Tables for configuration variables, CLI flags, tools, providers, modules, dependencies, and macros.

5. **Visual ASCII Directory Trees**:
   - Fenced code block ASCII trees with inline comments explaining file responsibilities.

6. **Collapsible Reference Cards (`<details><summary>`)**:
   - Detailed setups, layout presets, MTA guides, deep reference material, or verbose command lists wrapped inside styled details cards.

7. **GitHub Alerts**:
   - Use `> [!TIP]`, `> [!NOTE]`, `> [!WARNING]`, or `> [!CAUTION]` for critical setup notes or warnings.

---

## Workflow

1. **Inspect Codebase**:
   - Scan target repository for entrypoints, configuration files, directory hierarchy, scripts, commands, dependencies, and existing assets/icons.

2. **Select Visual Archetype**:
   - Match the project to one of the 6 canonical archetypes (Modular Collection, Shell Config, Knowledge Base, Go CLI, Automation Pipeline, Multimedia Toolkit).
   - Read `references/local-visual-archetypes.md` and `references/readme-style-contract.md` for exact templates.

3. **Draft Visual README**:
   - Assemble centered hero block, shields badges, quick nav bar, Iconify section headers, tables, ASCII directory tree, collapsible details cards, and alerts.
   - For badge/icon syntax details, consult `references/icons-and-shields.md`.

4. **Verify Quality**:
   - Confirm no plain, basic Markdown headers without icons or styling.
   - Confirm dark badge palette (`#1e1e1e` / `#111111`) and accurate relative file links.

---

## Red Flags & Rationalization Table

| Rationalization | Reality |
| --- | --- |
| *"A plain `# Title` header is enough."* | Untested plain READMEs look amateur. Always use the `<div align="center">` hero block with badges and nav bar. |
| *"Standard GitHub badges are fine."* | Shields default badges lack visual punch. Use dark `#1e1e1e` / `#111111` base with `style=for-the-badge` and custom logo colors. |
| *"Plain Markdown headings don't need SVG icons."* | Section headers with inline Iconify SVG icons (`height="22"`) create high visual contrast and polish. |
| *"Emojis are okay for section headers."* | Emojis render inconsistently across OSs. Use Iconify API SVG URLs or readmecodegen SVG icons. |
| *"I'll list files as a bulleted text list instead of a tree."* | Fenced codeblock ASCII directory trees with file comments are far easier to scan and understand. |
| *"This setup step is too long, I'll just paste 50 lines inline."* | Wrap verbose steps or secondary guides inside `<details><summary>` collapsible cards to keep the document concise. |

---

## Reference Files

- [local-visual-archetypes.md](file:///Users/rd/.agents/skills/readme-visual/references/local-visual-archetypes.md) — Detailed templates and design tokens for the 6 canonical local README styles.
- [readme-style-contract.md](file:///Users/rd/.agents/skills/readme-visual/references/readme-style-contract.md) — Core formatting contract, HTML structures, and visual rules.
- [icons-and-shields.md](file:///Users/rd/.agents/skills/readme-visual/references/icons-and-shields.md) — Shields.io badge formulas, Iconify API syntax, and color hex encoding.
