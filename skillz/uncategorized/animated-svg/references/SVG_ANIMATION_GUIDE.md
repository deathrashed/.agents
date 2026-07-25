# SVG Animation Guide

Detailed reference for SMIL-based SVG animation.

## The Four Animation Elements

### `<set>`

Changes an attribute to a new value at a specific time, usually without interpolation. Useful for toggles, delayed visibility changes, or switching states.

```svg
<svg viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
  <rect x="20" y="20" width="60" height="60" fill="royalblue">
    <set attributeName="fill" to="tomato" begin="2s" />
  </rect>
</svg>
```

### `<animate>`

Changes a single attribute over time (cx, y, opacity, fill, r, etc.).

```svg
<svg viewBox="0 0 300 100" xmlns="http://www.w3.org/2000/svg">
  <circle cx="20" cy="50" r="15" fill="royalblue">
    <animate attributeName="cx" from="20" to="280" dur="3s" repeatCount="indefinite" />
  </circle>
</svg>
```

### `<animateTransform>`

Animates the transform attribute - rotate, scale, skew, or translate.

```svg
<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <polygon points="60,30 90,90 30,90" fill="goldenrod">
    <animateTransform
      attributeName="transform"
      type="rotate"
      from="0 60 70"
      to="360 60 70"
      dur="2s"
      repeatCount="indefinite" />
  </polygon>
</svg>
```

### `<animateMotion>`

Moves an element along a path. Use `rotate="auto"` to follow path direction.

```svg
<svg viewBox="0 0 300 100" xmlns="http://www.w3.org/2000/svg">
  <circle r="10" fill="royalblue">
    <animateMotion path="M 0 50 H 300 Z" dur="3s" repeatCount="indefinite" />
  </circle>
</svg>
```

## Attribute Reference

| Attribute | Meaning | Notes |
|-----------|---------|-------|
| `attributeName` | The attribute to animate | Used by `<animate>` and `<set>` |
| `from` | Starting value | Often paired with `to` |
| `to` | Ending value | Defines final state |
| `dur` | Duration | Use `2s`, `500ms` |
| `begin` | Start time | Can be delayed, event-based, or chained |
| `repeatCount` | Number of repeats | Number or `indefinite` |
| `fill` | Post-animation behavior | `freeze` keeps final value |
| `type` | Transform type | `rotate`, `scale`, `translate`, `skewX`, `skewY` |
| `path` | Motion path | Used by `<animateMotion>` |
| `rotate` | Rotation while moving | `auto` follows path tangent |
| `values` | Multiple values for keyframe | `values="20;30;20"` |

## Timing Behavior

- `repeatCount="indefinite"` - loop forever
- `begin="2s"` - start after delay
- `begin="otherAnim.end"` - start after another animation

```svg
<animate attributeName="x" from="0" to="100" dur="1s" repeatCount="3" />
<animate attributeName="x" from="0" to="100" dur="1s" repeatCount="indefinite" />
```

## Chaining Animations

```svg
<svg viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
  <rect x="20" y="20" width="40" height="40" fill="teal">
    <animate attributeName="x" from="20" to="120" dur="1s" begin="0s" fill="freeze" />
    <animate attributeName="fill" from="teal" to="orange" dur="1s" begin="1s" fill="freeze" />
  </rect>
</svg>
```

## Transform Types

- `translate` - move
- `scale` - resize
- `rotate` - rotate (include center point: `from="0 60 60"`)
- `skewX`, `skewY` - skew

## Path-Following with Rotation

```svg
<svg viewBox="0 0 300 120" xmlns="http://www.w3.org/2000/svg">
  <path d="M20,100 C80,20 220,20 280,100" fill="none" stroke="lightgray" />
  <circle r="8" fill="crimson">
    <animateMotion dur="4s" repeatCount="indefinite" rotate="auto" path="M20,100 C80,20 220,20 280,100" />
  </circle>
</svg>
```

## Minimal Examples

### Pulsing Circle

```svg
<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <circle cx="60" cy="60" r="20" fill="royalblue">
    <animate attributeName="r" values="20;30;20" dur="1.5s" repeatCount="indefinite" />
  </circle>
</svg>
```

### Rotating Triangle

```svg
<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <polygon points="60,20 90,90 30,90" fill="goldenrod">
    <animateTransform attributeName="transform" type="rotate" from="0 60 60" to="360 60 60" dur="2s" repeatCount="indefinite" />
  </polygon>
</svg>
```

### Moving Square

```svg
<svg viewBox="0 0 300 80" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="20" width="20" height="20" fill="crimson">
    <animate attributeName="x" from="0" to="280" dur="2s" repeatCount="indefinite" />
  </rect>
</svg>
```

## CSS vs SMIL

- **CSS**: Simple visual effects (opacity, basic movement, hover states)
- **SMIL**: SVG-native attributes, motion paths, complex timing
- **JavaScript**: Interactivity, state logic, dynamic generation

## Practical Rules

- Use `viewBox` for clean scaling
- Keep animated elements simple for smoother rendering
- Use `fill="freeze"` when you want final value to persist
- Use `<animateTransform>` for movement/rotation instead of manual attribute changes
- Test in target browsers - SMIL widely supported but edge cases exist