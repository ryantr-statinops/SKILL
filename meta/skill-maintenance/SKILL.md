---
name: skill-maintenance
description: Maintain, refactor, version, and retire skills without causing routing drift or duplicated guidance.
category: meta
subject: skill-system
scope: repository
status: stable
version: 1.0.0
---

# Skill maintenance

## When to use

Use when a skill changes, overlaps another skill, becomes stale, or needs to be
split, merged, deprecated, or retired.

## Workflow

1. Inspect current usage, links, examples, and evaluation cases.
2. Identify whether the problem is routing, scope, procedure, reference depth, or validation.
3. Make the smallest coherent change and update affected links and examples.
4. Run structural validation and the relevant evaluation cases.
5. Record breaking changes in the commit and update the repository index when needed.

## Decision rules

- Prefer a narrow correction over accumulating universal rules.
- Split a skill when it has independent outcomes or activation conditions.
- Merge skills only when their outcomes, boundaries, and validation are genuinely the same.
- Retire duplicated or unused skills rather than preserving them for aesthetics.
- Treat changes to activation conditions or expected output as potentially breaking.

## Failure modes

- Stale reference: update or remove the link; do not leave silent dead paths.
- Routing drift: revise description and exclusions before changing procedure.
- Unclear compatibility: preserve the old behavior or document the migration path.

## Validation

Every maintenance change must pass the repository validator and at least one
representative task or regression case.
