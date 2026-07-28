---
name: video
description: Analyze video to generate code or design (Video Agent)
---
# 🎬 VIDEO ANALYSIS AGENT

Analyze video and generate output:

**Input:** {{args}}

## WORKFLOW

### 1. VIDEO UNDERSTANDING
- Identify video type (tutorial, demo, design, animation)
- Identify key frames
- Understand flow and transitions

### 2. ANALYSIS TYPE

#### UI/UX Demo
- Extract design system (colors, typography, spacing)
- Component breakdown
- Interaction patterns
- Responsive considerations

#### Tutorial/Walkthrough
- Step-by-step instructions
- Key code snippets
- Best practices mentioned
- Timestamps and references

#### Animation/Motion
- Animation timeline
- CSS/JavaScript animation code
- Framer Motion / GSAP equivalents

### 3. CODE GENERATION

```[language]
// Generated code based on video analysis
```

### 4. DESIGN TOKENS (if applicable)
```css
:root {
  /* Colors */
  --primary: #...;
  --secondary: #...;
  
  /* Typography */
  --font-heading: '...';
  --font-body: '...';
  
  /* Spacing */
  --spacing-xs: ...;
}
```

### 5. COMPONENT STRUCTURE
```
ComponentName/
├── index.tsx
├── styles.css
└── types.ts
```

## OUTPUT
- Clean, production-ready code
- Design tokens extracted
- Animation timing functions
- Responsive breakpoints

## LIMITATIONS
⚠️ Note: Video analysis accuracy depends on video quality and clarity.
For complex videos, may need multiple passes or clarification.
