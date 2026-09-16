# Skill authoring

Use this guide when creating or revising a skill in `SKILLS`.

## Start with the outcome

Describe the concrete task the agent should perform and the observable result.
Avoid creating a skill that is only a topic label such as `python` or `AI`.

## Required entrypoint

Every skill has a `SKILL.md` with YAML frontmatter containing at least:

```yaml
---
name: skill-name
description: What the skill does and when it applies.
---
```

The body should explain activation boundaries, scope, workflow, decision rules,
constraints, failure modes, and validation. Start from
`meta/SKILL_TEMPLATE.md` and remove sections that do not add value.

## Supporting resources

- `references/`: detailed knowledge needed only for particular modes.
- `scripts/`: deterministic operations that materially improve reliability.
- `examples/`: demonstrations, fixtures, or evaluation cases.
- `assets/`: reusable templates and output artifacts.

Do not create empty directories, copy generic manuals, or duplicate the same
knowledge across the entrypoint and references.

## Classification

- Put broadly reusable procedures in `common/`.
- Put Ryan-specific preferences and workflows in `personal/`.
- Put skill-system procedures in `meta/`.

If a skill has both reusable and personal parts, keep the reusable procedure
separate from the preference-specific extension.

## Before committing

1. Check the activation and exclusion boundaries.
2. Link every supporting resource from the relevant instruction.
3. Run `python3 scripts/validate_skills.py`.
4. Test one representative task and one nearby boundary task.
