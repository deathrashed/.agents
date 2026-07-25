---
name: animated-svg
description: "Create animated SVG images using SMIL. Use when the user wants to generate or debug SVG animations including pulsing, rotating, moving, and path-following effects."
---

# Animated SVG

Create and debug animated SVG images using SMIL.

## Quick Start

1. Identify animation type needed (movement, rotation, pulse, path-follow)
2. Use reference templates or write from scratch
3. Test in browser - SMIL widely supported

## Animation Types

| Type | Element | Use For |
|------|---------|---------|
| Attribute change | `<animate>` | Color, position, opacity, size |
| Transform | `<animateTransform>` | Rotate, scale, translate, skew |
| Motion path | `<animateMotion>` | Following a curved path |
| State toggle | `<set>` | Delayed visibility, toggles |

## Core Attributes

- `attributeName` - what to animate
- `from` / `to` - start and end values
- `dur` - duration (e.g., `2s`, `500ms`)
- `begin` - start time or event
- `repeatCount` - number of loops (`indefinite` for infinite)
- `fill` - behavior after animation ends (`freeze` to keep final state)

## Common Patterns

**Pulsing circle:**
```svg
<animate attributeName="r" values="20;30;20" dur="1.5s" repeatCount="indefinite" />
```

**Rotating shape:**
```svg
<animateTransform attributeName="transform" type="rotate" from="0 60 60" to="360 60 60" dur="2s" repeatCount="indefinite" />
```

**Moving along path:**
```svg
<animateMotion path="M0,50 H300 Z" dur="3s" repeatCount="indefinite" rotate="auto" />
```

See [references/SVG_ANIMATION_GUIDE.md](references/SVG_ANIMATION_GUIDE.md) for detailed syntax, timing, chaining, and examples.

## Scripts

- [scripts/generate_svg.py](scripts/generate_svg.py) - Generate simple animations from config
- [scripts/validate_svg.py](scripts/validate_svg.py) - Check SVG syntax

## Assets

- [assets/templates/](assets/templates/) - Reusable SVG animation templates