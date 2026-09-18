---
name: personal-debugging
description: Apply Ryan's evidence-first debugging workflow to reproduce, isolate, fix, and verify a personal project failure.
category: personal
subject: workflow
scope: personal
status: experimental
version: 1.0.0
invocation: both
---

# Personal debugging workflow

## When to use
Use for failures in personal projects when a reproducible root-cause investigation is needed and the fix must preserve the project's local conventions.

## When not to use
Do not use for selecting a technology, planning a new project, or reviewing a completed diff; use the matching decision, project, or review skill.

## Personal principles
Prefer minimal reproduction, explicit hypotheses, and a verified small fix.

## Workflow
1. Capture exact symptom and environment.
2. Inspect recent changes and reduce the reproduction.
3. Test hypotheses with focused evidence.
4. Fix, add regression coverage, and verify the original case.

## Decision rules
Do not rewrite surrounding code before isolating the failure.

## Constraints
Keep unrelated cleanup out of the debugging change.

## Failure modes
If reproduction is missing, add observability or request the missing evidence.

## Expected output
Report root cause, minimal fix, verification, and remaining uncertainty.

## Validation
The original failure no longer reproduces and the relevant regression check passes.

## Agent handoff

- Selected when: Use when the requested outcome matches this skill description and workflow.
- Do not activate when: Do not activate when the task matches the stated exclusion or a narrower skill.
- Expected output: Produce the observable artifact, decision, or result described by the workflow.
- User-facing report: Summarize scope, result, checks, and unresolved risks.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
