#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

printf 'Validating bundled Keyboard Maestro macro exports...\n'
if find assets/examples assets/real-exports -name '*.kmmacros' -print -quit | grep -q .; then
  find assets/examples assets/real-exports -name '*.kmmacros' -print0 | xargs -0 -n1 plutil -lint
else
  printf 'No .kmmacros files found under assets/examples/ or assets/real-exports/.\n' >&2
  exit 1
fi

printf '\nChecking for stale lowercase/old documentation references...\n'
stale_refs='actions\.md|macro-structure\.txt|KEYBOARD_MAESTRO_MACRO_GUIDE|TROUBLESHOOTING_AND_PROCESS|tldr\.md'
if rg -n "$stale_refs" SKILL.md references assets; then
  printf '\nStale references found. Update them before relying on this skill.\n' >&2
  exit 1
fi

printf '\nChecking required reliability files...\n'
required=(
  "references/ACTIONS.md"
  "references/ACTION-SOURCING.md"
  "references/MACRO-STRUCTURE.txt"
  "references/MACRO-ARCHITECTURE.md"
  "references/MACRO-XML-SCHEMA.md"
  "assets/templates/status-menu-wrapper.xml"
  "scripts/find-action.sh"
)
for path in "${required[@]}"; do
  if [[ ! -f "$path" ]]; then
    printf '\nMissing required file: %s\n' "$path" >&2
    exit 1
  fi
done
printf ' OK\n'

printf '\nSkill validation passed. Remember: plutil proves plist syntax only, not Keyboard Maestro import behavior.\n'
