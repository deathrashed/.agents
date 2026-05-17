# Handy Scripts

These are the local skill utilities under:
`/Users/rd/.codex/skills/typinator/scripts`

They are helper tools for larger maintenance tasks. They are not required for every Typinator change.

## Export-focused utilities

- `interactive_fix_exports.py`
  Interactive CSV/TXT export fixer for duplicate abbreviations, malformed markers, Unicode cleanup, and placeholder conversion.

- `normalize_exported_sets.py`
  Normalizes exported CSV files into cleaned copies. Useful only when format-preserving direct-export rules are not required.

- `validate_typinator_exports.py`
  Final export validator for syntax artifacts, duplicates, script references, alias use, and manifest checks.

## Menu/build utilities

- `build_master_menu.py`
  Adds or updates a master-menu row for a specific CSV file.

- `build_master_menu_includes.py`
  Convenience wrapper for building master menus against Includes-hosted exports.

## Structure and migration utilities

- `audit_typinator_tree.py`
  Produces a quick topology report of Sets and Includes. Useful during major cleanup/migration work.

- `build_script_manifest.py`
  Scans organized scripts and builds the alias-to-canonical manifest used for export validation and path migration.

- `convert_form_placeholders.py`
  Converts foreign placeholder forms such as `{form:name}` into Typinator input fields.

## Practical rule

Use these utilities when:
- cleaning exports at scale
- migrating large script trees
- generating CSV-driven menus
- validating final export deliverables

Do not default to them when:
- editing live `.tyset` rules directly
- making small one-off abbreviation changes
- adjusting a few picker/menu entries in installed sets
