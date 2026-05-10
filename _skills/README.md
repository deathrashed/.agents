# Skills Layout

This folder now uses category-first canonical locations.

## Canonical Buckets

Existing grouped buckets:

- `azure/`
- `breakdown/`
- `full-stack-skills/`
- `mcp/`
- `playwright/`
- `specstory/`
- `superpowers/`
- `swift/`

New grouped buckets added for the remaining standalone skills:

- `ai-agent-skills/`
- `architecture-planning/`
- `cloud-devops/`
- `content-docs/`
- `creative-media/`
- `data-platforms/`
- `developer-workflows/`
- `dotnet/`
- `git-workflows/`
- `google-platform/`
- `java-kotlin/`
- `linux-admin/`
- `microsoft-ecosystem/`
- `oracle-postgres/`
- `productivity-collaboration/`
- `quality-security/`
- `web-stack/`

## Conventions

- The bucket folders above are the canonical homes for grouped skills.
- Old top-level skill paths are preserved as symlinks to their canonical bucket location.
- Some legacy non-underscore folders still exist because they already acted as category containers or hold intentionally distinct variants.

## Why

This keeps related skills together while preserving compatibility for tools or chatbots that still expect the old top-level path.

## Duplicates

Some repeated names were intentionally left as separate variants because their `SKILL.md` content differs.
