---
name: context-management
description: Load only the context needed for a task while preserving the evidence required for correct decisions.
category: common
subject: foundation
scope: universal
status: experimental
version: 1.0.0
invocation: both
---

# Context management

## When to use
Use when a repository, specification, or task has more context than the current work requires.

## Workflow
1. Identify the requested outcome and relevant subsystem.
2. Read entrypoints, instructions, schemas, and tests before deep implementation files.
3. Load references only when a decision requires them.
4. Keep a concise evidence summary and discard unrelated detail.
5. Re-check source files when assumptions become uncertain.

## Decision rules
- Prefer primary project artifacts over summaries.
- Expand context only in response to a concrete unknown or failure.

## Failure modes
If context is insufficient, state exactly which artifact or decision is missing.

## Expected output
Maintain a task-focused context map rather than a repository dump.

## Validation
Confirm that each loaded artifact supports a stated decision or verification step.

## Agent handoff

- Selected when: Use the activation boundary and outcome described in this skill.
- Do not activate when: The task matches the stated exclusion or a narrower skill.
- Expected output: Produce the observable result and validation described by the workflow.
- User-facing report: Summarize scope, result, checks, and unresolved risks.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
