# Iconify And Shields Guide

Use this reference before adding icons or badges to a README.

## Local Reference Sources

Read these files when the README needs richer icon or badge treatment:

```text
/Volumes/Apfspace/Icons/iconify/ICONIFY-DOCS.md
/Volumes/Apfspace/Icons/iconify/README.md
/Users/rd/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/Iconify Documentation.md
/Users/rd/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/Utilities/Guides/Shields/_Awesome Badges.md
```

## Icon Selection Rules

Choose icons by role:

| README Element | Preferred Source | Notes |
| --- | --- | --- |
| Top logo/banner | Local image (`assets/icon.png`, `data/icon/logo.svg`) | Place inside `<div align="center">` hero block. |
| Section heading icons | Iconify API SVG URLs or readmecodegen icons | Use `## <img src="https://api.iconify.design/..." height="22">`. |
| Tech stack badges | Shields Simple Icons logos | Use dark base `#1e1e1e` or `#111111` with `style=for-the-badge`. |
| Table icons | Iconify API SVG URLs | Embedded in markdown table cells (`height="16"`). |

Do not use raw emojis or broken glyphs. Rely on Iconify SVG URLs, Shields badges, ASCII trees, and clean Markdown formatting.

## GitHub-Safe Iconify Syntax

Prefer Iconify API-generated SVG URLs in `<img>` tags:

```html
<img src="https://api.iconify.design/mdi:rocket-launch-outline.svg?color=%2301acd7" height="22" alt="Icon">
```

URL-encode colors (`#` becomes `%23`):
- `%2301acd7` (Cyan)
- `%2311c866` (Green)
- `%23ff2a1f` (Red)
- `%23faa701` (Gold)

Heading Example:

```markdown
## <img src="https://api.iconify.design/mdi:file-tree.svg?color=%2301acd7" height="22"> Project Structure
```

Table Cell Example:

```markdown
| Provider | Description |
| --- | --- |
| <img src="https://api.iconify.design/mdi:spotify.svg?color=%2301acd7" height="16"> **Spotify** | Spotify metadata provider |
```

## Shields Badge Rules

Use shields.io badges with dark background base (`#1e1e1e` or `#111111`) and `style=for-the-badge`:

```markdown
[![ZSH](https://img.shields.io/badge/shell%20—%20zsh-1e1e1e?style=for-the-badge&logo=gnu-bash&logoColor=white)](https://www.zsh.org/)
[![PLATFORM](https://img.shields.io/badge/macOS-1e1e1e?style=for-the-badge&logo=apple&logoColor=faa701)](https://apple.com)
```

Keep text short. URL-encode special characters:
- space -> `%20`
- em-dash -> `%20—%20`
- plus -> `%2B`
