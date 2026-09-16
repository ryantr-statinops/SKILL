---
name: skill-intake
description: Decide whether to adopt, adapt, rebuild, or create a skill from an external repository or a new personal need.
category: meta
subject: skill-system
scope: repository
status: stable
version: 1.0.0
---

# Skill intake

## When to use

Use when importing an existing skill, studying an ecosystem, or turning a
repeated personal workflow into a new skill.

## Workflow

1. State the target task and the evidence that the skill is needed.
2. Inspect the source structure, license, dependencies, scope, and validation.
3. Choose one disposition: reference, copy, adapt, rebuild, or reject.
4. Classify the result as `common`, `personal`, or `meta`.
5. Normalize the entrypoint to this repository's conventions.
6. Preserve attribution and license obligations, then validate with a realistic task.

## Disposition rules

- **Reference:** learn a pattern without importing implementation.
- **Copy:** use only when the license permits it and the skill already matches this repository's scope and format.
- **Adapt:** retain useful procedure but rewrite routing, boundaries, and conventions for this library.
- **Rebuild:** use when the source is complex, incompatible, overly generic, or tightly coupled to another agent/runtime.
- **Reject:** use when the scope is unclear, redundant, unsafe, unmaintained, or not useful to a real task.

For a one-file Markdown skill, inspect and adapt it directly if its procedure is
clear. For a complex skill with scripts, references, or runtime assumptions,
extract the design pattern and rebuild the minimum useful subset.

## Classification rules

- `common`: transferable procedure with no Ryan-specific preference.
- `personal`: depends on Ryan's tools, projects, conventions, or domain judgment.
- `meta`: changes how skills are authored, routed, evaluated, or maintained.

If a skill is both common and personal, keep the reusable core in `common/`
and put the preference-specific extension in `personal/`.

## Failure modes

- License unclear: do not copy; request review or rebuild from observed behavior.
- Source is a documentation dump: extract decisions and workflows instead.
- Scope overlaps an existing skill: extend the existing skill or document a clear boundary.
