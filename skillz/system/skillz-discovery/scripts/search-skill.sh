#!/usr/bin/env bash
set -euo pipefail

if [[ $# -eq 0 ]]; then
  printf 'Usage: %s <keywords> [more keywords...]\n' "$0" >&2
  exit 2
fi

library_root="${SKILLZ_ROOT:-$HOME/.agents/skillz}"
repos_root="${SKILL_REPOS_ROOT:-$HOME/.agents/repos}"
plugins_root="${SKILL_PLUGINS_ROOT:-$HOME/.agents/plugins}"
query_str="$*"

for entry in "skillz|$library_root" "repos|$repos_root" "plugins|$plugins_root"; do
  source="${entry%%|*}"
  root="${entry#*|}"
  [[ -d "$root" ]] || continue
  {
    # Match by directory name containing any search word
    for term in "$@"; do
      dirs="$(find "$root" -maxdepth 8 -type d -iname "*${term}*" -not -path '*/node_modules/*' -not -path '*/.git/*' 2>/dev/null || true)"
      while IFS= read -r dir; do
        [[ -z "$dir" ]] && continue
        sk="$dir/SKILL.md"
        [[ -f "$sk" ]] && printf '[%s]\t%s\t(name)\n' "$source" "$sk"
      done <<< "$dirs"
    done
    # Match by content (broader)
    rg --no-ignore --hidden --glob 'SKILL.md' --glob '!*/.git/*' --glob '!*/node_modules/*' \
      -i -l -- "$query_str" "$root" 2>/dev/null |
      while IFS= read -r path; do
        printf '[%s]\t%s\t(content)\n' "$source" "$path"
      done
  }
done | sort -u | head -60
