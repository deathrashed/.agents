---
name: km-macro-creator
description: Create, debug, and safely extend Keyboard Maestro `.kmmacros` files using real exported action dictionaries instead of guessed XML. Use when users ask to build KM macros, fix import failures, add actions, or verify macro schema/structure. Keywords: kmmacros, Keyboard Maestro, MacroActionType, KM import error, plutil, macro XML.
---

# Keyboard Maestro Macro Creator Skill

## Invocation Scope

Use this skill when asked to:
- Create Keyboard Maestro macros
- Fix import errors in `.kmmacros` files
- Add/replace actions in existing macros
- Validate action schema assumptions before generating XML

## Workflow

1. **MANDATORY:** Read `references/MACRO-ARCHITECTURE.md` first for level selection.
2. List required `MacroActionType` values.
3. For each action, run `scripts/find-action.sh MacroActionType`.
4. **MANDATORY:** Read `references/ACTION-SOURCING.md` before choosing source blocks.
5. Hand-template only the stable wrapper from `references/MACRO-STRUCTURE.txt`.
6. Clone schema-sensitive action dictionaries from real exports and edit only payload fields.
7. Generate fresh group/macro `UID` UUIDs and unique integer `ActionUID`s.
8. Validate with `scripts/validate-macro.sh your-macro.kmmacros`.
9. State verification level: `plist validated`, `manual import confirmed`, or `behavior confirmed`.

If `find-action.sh` has no match, ask for a tiny exported macro containing that action and use it as the source of truth.

## Loading Guidance

- Read by default:
  - `references/MACRO-ARCHITECTURE.md`
  - `references/ACTION-SOURCING.md`
  - `references/MACRO-STRUCTURE.txt`
  - `references/ACTIONS.md`
- Load only when needed:
  - `references/MACRO-XML-SCHEMA.md` for deep schema debugging/history
- Use categorized examples under:
  - `assets/examples/` (topic folders + `_EXAMPLES_`)
  - `assets/real-exports/` for schema-sensitive actions

## Validation Commands

```bash
scripts/validate-macro.sh your-macro.kmmacros
scripts/validate-skill.sh
```

Remember: `plutil -lint` proves plist syntax, not import behavior.

## Never Rules

- Never invent `MacroActionType` names.
- Never hand-author complex action dictionaries when a real export exists.
- Never overwrite clipboard state without save/restore pattern.
- Never claim import success without explicitly naming verification level.
