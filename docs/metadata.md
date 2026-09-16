# Skill metadata

Every `SKILL.md` uses YAML frontmatter so humans and tools can discover the
skill without reading its full body.

## Required schema

```yaml
---
name: skill-name
description: What the skill does and when it applies.
category: meta
subject: skill-system
scope: repository
status: stable
version: 1.0.0
---
```

### Fields

- `name`: lowercase local skill name; it must match the final directory name. Names may repeat in different scopes; canonical path IDs must not.
- `description`: concise capability and activation boundary.
- `category`: `common`, `personal`, or `meta`; it must match the root directory.
- `subject`: lowercase topic grouping used for index sorting and discovery.
- `scope`: `universal`, `personal`, or `repository`.
- `status`: `draft`, `experimental`, `stable`, or `deprecated`.
- `version`: semantic version in `MAJOR.MINOR.PATCH` form.

The canonical skill ID is derived from the path, for example
`meta/skill-authoring`. Do not duplicate it in frontmatter.

## Generated registry

The metadata is the source of truth for `docs/skill-index.md` and
`data/skills.json`. Generate both with:

```bash
python3 scripts/generate_skill_index.py
```

Use `--check` in validation or CI to detect stale generated files.
