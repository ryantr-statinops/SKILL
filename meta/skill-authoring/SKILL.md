---
name: skill-authoring
description: Design or revise a narrowly scoped Agent Skill with explicit routing, progressive disclosure, and validation.
category: meta
subject: skill-system
scope: repository
status: stable
version: 1.0.0
---

# Skill authoring

## When to use

Use when creating, restructuring, or reviewing a skill in this repository.

## When not to use

Do not use this as a substitute for domain-specific implementation guidance.

## Workflow

1. Define the user task, desired outcome, and activation boundary.
2. Decide whether the knowledge belongs in `SKILL.md`, a reference, a script, an example, or an asset.
3. Write the smallest useful entrypoint using `meta/SKILL_TEMPLATE.md`.
4. Add decision rules, failure modes, and observable validation.
5. Run the repository validator and test the skill against a realistic task.

## Decision rules

- Prefer one skill per coherent outcome, not one skill per technology keyword.
- Keep generic facts out unless they change an agent decision.
- Use a reference for conditional depth and a script for deterministic repeated work.
- Keep automatic discovery enabled unless explicit-only invocation is required.

## Constraints

Names use lowercase letters, digits, and hyphens. Do not create empty resource
directories or copy external documentation wholesale.

## Failure modes

- Vague description: narrow the trigger and add exclusions.
- Giant `SKILL.md`: move conditional detail to references.
- No validation: add a concrete expected result and test task.

## Validation

Run `python3 scripts/validate_skills.py` from the repository root after the
validator is available.
