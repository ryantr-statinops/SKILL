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
invocation: both
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
- `invocation`: `user`, `model`, or `both`; describes whether the skill is
  explicitly selected by a user, automatically selected by an agent, or both.

- `requires`: optional list of canonical skill IDs required by this skill;
  dependency resolution is handled by the registry and sync tools.

`invocation` is portable metadata. It does not encode Claude, Codex, plugin, or
other runtime-specific commands. A `user` skill is an explicit workflow entry
point; a `both` skill may also be selected from its description and metadata.
The `model` value is reserved for skills that are intentionally agent-selected
without requiring an explicit user invocation.

The canonical skill ID is derived from the path, for example
`meta/skill-authoring`. Do not duplicate it in frontmatter.

## Generated registry

The metadata is the source of truth for `docs/skill-index.md` and
`data/skills.json`. Generate both with:

```bash
python3 scripts/generate_skill_index.py
```

Use `--check` in validation or CI to detect stale generated files.
