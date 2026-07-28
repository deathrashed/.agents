#!/usr/bin/env bash
set -euo pipefail

if [[ $# -eq 0 ]]; then
  printf 'Usage: %s <keywords> [more keywords...]\n' "$0" >&2
  exit 2
fi

library_root="${SKILLZ_ROOT:-$HOME/.agents/skillz}"
repos_root="${SKILL_REPOS_ROOT:-$HOME/.agents/repos}"
plugins_root="${SKILL_PLUGINS_ROOT:-$HOME/.agents/plugins}"
query="$*"

for entry in "skillz|$library_root" "plugins|$plugins_root" "repos|$repos_root"; do
  source="${entry%%|*}"
  root="${entry#*|}"
  [[ -d "$root" ]] || continue
  {
    find "$root" -type f -name 'SKILL.md' -print 2>/dev/null |
      rg -i -- "$query" | while IFS= read -r path; do
        printf '[%s]\t%s\n' "$source" "$path"
      done || true
    rg --no-ignore --hidden --glob 'SKILL.md' --glob '!*/.git/*' --glob '!*/node_modules/*' \
      -i -l -- "$query" "$root" 2>/dev/null |
      while IFS= read -r path; do
        printf '[%s]\t%s\n' "$source" "$path"
      done || true
  }
done | sort -u
