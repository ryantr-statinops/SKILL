---
name: skill-discovery
description: Select the smallest relevant skill for a task using descriptions, boundaries, and progressive disclosure.
category: meta
subject: skill-system
scope: repository
status: stable
version: 1.1.0
invocation: both
---

# Skill discovery

## When to use

Use when routing a user task to one or more skills in this library or to the
installed catalog exposed by a consumer runtime.

## Workflow

1. Extract the task outcome, domain, artifacts, and risk.
2. Select the registry source: the repository registry for authoring work, or
   the consumer `.skill-catalog.json` / runtime skill list for installed work.
3. Scan category and skill descriptions; do not load every skill.
4. Reject candidates whose `when not to use` boundary matches.
5. Select the narrowest skill that covers the outcome; combine skills only when responsibilities are distinct.
6. Read its `SKILL.md`, then load only linked resources required by the task.
7. Validate the result using the selected skill's stated checks.

## Decision rules

- Specific scope beats broad scope.
- A technology mention alone is not sufficient activation.
- If two skills overlap, prefer the one with the more specific outcome and record the boundary.
- If no skill clearly applies, proceed without forcing an unrelated skill and consider a future intake request.

## Failure modes

- Too many candidates: narrow by desired output and exclusions.
- Missing context: inspect the repository or ask for the minimum required input.
- Conflicting procedures: stop and surface the conflict instead of silently merging them.

## Agent handoff

- Selected when: The task changes authoring, discovery, evaluation, intake, or maintenance of this skill library.
- Do not activate when: The task is domain implementation unrelated to the skill system.
- Expected output: Produce a bounded skill-system decision, artifact, or validation result.
- User-facing report: Summarize the rule applied, files or registry affected, checks, and risks.
- Confirmation boundary: Ask before destructive repository changes, external writes, or irreversible lifecycle actions.
