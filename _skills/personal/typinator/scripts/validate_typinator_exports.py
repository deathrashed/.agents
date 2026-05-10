#!/usr/bin/env python3
"""Validate Typinator exported CSV sets and script references.

Checks:
- CSV parse + round-trip structural stability
- duplicate abbreviations per file
- syntax artifacts ({Shell/, {form:...}, <Skip if null>)
- script reference resolution (including backtick snippets)
- no symlink targets for referenced scripts
- optional abbreviation word-count policy
- interactive script detection for expansion-time safety
- newline style visibility (CRLF/LF mixed files)
- Exported/exported directory consistency warnings
"""

from __future__ import annotations

import argparse
import csv
import io
from pathlib import Path
import re
from typing import Iterable


SYNTAX_PATTERNS = [
    (re.compile(r"\{Shell/"), "malformed shell marker ({Shell/)"),
    (re.compile(r"\{form:[^}]+\}"), "non-native placeholder ({form:...})"),
    (re.compile(r"<Skip if null>"), "artifact (<Skip if null>)"),
]

INTERACTIVE_PATTERNS = [
    re.compile(r"\bdisplay dialog\b", re.IGNORECASE),
    re.compile(r"\bdisplay alert\b", re.IGNORECASE),
    re.compile(r"\bchoose from list\b", re.IGNORECASE),
    re.compile(r"\bchoose file\b", re.IGNORECASE),
    re.compile(r"\bchoose folder\b", re.IGNORECASE),
]

FORBIDDEN_SCRIPT_NAME_CHARS = {"|", "{", "}"}


def load_manifest_aliases(path: Path | None) -> set[str]:
    if path is None or not path.exists():
        return set()
    aliases: set[str] = set()
    with path.open(encoding="utf-8", newline="") as fh:
        rows = csv.DictReader(fh)
        for row in rows:
            alias = (row.get("alias_path") or "").strip()
            status = (row.get("status") or "").strip().lower()
            if alias and status in {"deprecated", "alias"}:
                aliases.add(alias)
    return aliases


def find_script_references(text: str, includes_root: Path) -> tuple[list[str], list[str]]:
    """Return (resolved_paths, unresolved_snippets)."""
    resolved: list[str] = []
    unresolved: list[str] = []
    i = 0
    while True:
        i = text.find("Scripts/", i)
        if i == -1:
            break
        tail = text[i:]
        found = None
        # Longest-prefix matching against real filesystem path.
        for end in range(len(tail), len("Scripts/") - 1, -1):
            candidate = tail[:end].rstrip(" \t\r\n`}|")
            if not candidate.startswith("Scripts/"):
                continue
            if (includes_root / candidate).exists():
                found = candidate
                break
        if found is None:
            unresolved.append(tail[:120])
            i += len("Scripts/")
            continue
        resolved.append(found)
        i += len(found)
    return resolved, unresolved


def newline_style(path: Path) -> str:
    raw = path.read_bytes()
    has_crlf = b"\r\n" in raw
    has_lf = b"\n" in raw
    if has_crlf and has_lf:
        # if only CRLF, has_lf is also true, so distinguish mixed manually
        mixed = b"\r\n" in raw and b"\n" in raw.replace(b"\r\n", b"")
        if mixed:
            return "mixed"
        return "crlf"
    if has_lf:
        return "lf"
    return "none"


def parse_rows(path: Path) -> list[list[str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        return [list(row) for row in csv.reader(fh)]


def roundtrip_equal(rows: list[list[str]]) -> bool:
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerows(rows)
    buf.seek(0)
    parsed = [list(row) for row in csv.reader(io.StringIO(buf.getvalue()))]
    return parsed == rows


def warn_exported_directory_case(includes_root: Path) -> list[str]:
    msgs: list[str] = []
    d1 = includes_root / "Exported"
    d2 = includes_root / "exported"
    if d1.exists() and d2.exists():
        msgs.append(
            "Both Includes/Exported and Includes/exported exist. Consolidate to one runtime source."
        )
    return msgs


def iter_script_files(scripts_root: Path) -> Iterable[Path]:
    exts = {".applescript", ".scpt", ".sh", ".py", ".rb", ".swift", ".js"}
    for p in sorted(scripts_root.rglob("*")):
        if p.is_file() and not p.is_symlink() and p.suffix.lower() in exts:
            yield p


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--includes-root",
        default="/Users/rd/.config/typinator/Sets/Includes",
        help="Typinator Includes root",
    )
    ap.add_argument(
        "--export-dir",
        default=None,
        help="Export directory (defaults to Includes/Exported)",
    )
    ap.add_argument(
        "--manifest",
        default=None,
        help="Optional alias manifest CSV (alias_path,canonical_path,status,...)",
    )
    ap.add_argument(
        "--max-abbr-words",
        type=int,
        default=None,
        help="Optional max words allowed in abbreviations",
    )
    args = ap.parse_args()

    includes_root = Path(args.includes_root).expanduser().resolve()
    export_dir = (
        Path(args.export_dir).expanduser().resolve()
        if args.export_dir
        else includes_root / "Exported"
    )
    manifest_path = (
        Path(args.manifest).expanduser().resolve() if args.manifest else None
    )
    alias_paths = load_manifest_aliases(manifest_path)

    errors: list[str] = []
    warnings: list[str] = []

    if not export_dir.exists():
        print(f"ERROR: export directory not found: {export_dir}")
        return 2

    warnings.extend(warn_exported_directory_case(includes_root))

    interactive_hits: dict[str, list[str]] = {}
    script_name_hits: list[str] = []

    csv_files = sorted(export_dir.glob("*.csv"))
    for csv_file in csv_files:
        style = newline_style(csv_file)
        if style == "mixed":
            warnings.append(f"{csv_file.name}: mixed newline style")

        try:
            rows = parse_rows(csv_file)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{csv_file.name}: CSV parse error: {exc}")
            continue

        if not roundtrip_equal(rows):
            errors.append(f"{csv_file.name}: CSV round-trip structural mismatch")

        abbr_to_rows: dict[str, list[int]] = {}
        for idx, row in enumerate(rows, start=1):
            if not row:
                continue
            abbr = row[0].strip()
            if abbr:
                abbr_to_rows.setdefault(abbr, []).append(idx)
                if args.max_abbr_words is not None and len(abbr.split()) > args.max_abbr_words:
                    errors.append(
                        f"{csv_file.name}:{idx}: abbreviation exceeds max words "
                        f"({args.max_abbr_words}): {abbr!r}"
                    )

            for cell in row[1:]:
                for pattern, label in SYNTAX_PATTERNS:
                    if pattern.search(cell):
                        errors.append(f"{csv_file.name}:{idx}: {label}")

                refs, unresolved = find_script_references(cell, includes_root)
                for snippet in unresolved:
                    errors.append(
                        f"{csv_file.name}:{idx}: unresolved script reference near: {snippet!r}"
                    )
                for ref in refs:
                    p = includes_root / ref
                    if p.is_symlink():
                        errors.append(
                            f"{csv_file.name}:{idx}: script ref points to symlink alias: {ref}"
                        )
                    if ref in alias_paths:
                        errors.append(
                            f"{csv_file.name}:{idx}: script ref points to deprecated alias from manifest: {ref}"
                        )

                    # Interactive script detection (warning only).
                    if p.suffix.lower() in {".applescript", ".scpt", ".sh", ".py", ".rb", ".swift", ".js"}:
                        try:
                            src = p.read_text(errors="ignore")
                        except Exception:  # noqa: BLE001
                            src = ""
                        found_labels = []
                        for pat in INTERACTIVE_PATTERNS:
                            if pat.search(src):
                                found_labels.append(pat.pattern)
                        if found_labels:
                            interactive_hits.setdefault(ref, []).extend(found_labels)

        duplicates = {k: v for k, v in abbr_to_rows.items() if len(v) > 1}
        if duplicates:
            errors.append(f"{csv_file.name}: duplicate abbreviations ({len(duplicates)})")

    # Filename safety gate for script files.
    scripts_root = includes_root / "Scripts"
    if scripts_root.exists():
        for script_file in iter_script_files(scripts_root):
            rel = script_file.relative_to(scripts_root).as_posix()
            if any(ch in rel for ch in FORBIDDEN_SCRIPT_NAME_CHARS):
                script_name_hits.append(rel)

    if script_name_hits:
        errors.append(
            "Script filenames with marker-conflicting characters found: "
            + ", ".join(script_name_hits[:20])
        )

    for ref, pats in sorted(interactive_hits.items()):
        pat_list = ", ".join(sorted(set(pats)))
        warnings.append(f"Interactive script pattern in {ref}: {pat_list}")

    print(f"Validated {len(csv_files)} CSV files in {export_dir}")
    if warnings:
        print(f"WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")
    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("All checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

