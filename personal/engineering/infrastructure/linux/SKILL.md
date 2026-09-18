---
name: linux
description: Apply a cautious, inspectable workflow for Linux shell, processes, filesystems, permissions, and services.
category: personal
subject: engineering
scope: personal
status: experimental
version: 1.0.0
invocation: both
---

# Linux workflow

## When to use
Use for Linux environment inspection, configuration, troubleshooting, or automation.

## Personal principles
Inspect first, use narrow paths, and prefer reversible operations.

## Workflow
Inspect OS and process state, identify exact targets, make the smallest change, and verify service/filesystem state.

## Decision rules
Avoid broad recursive or destructive commands when a precise command exists.

## Constraints
Protect credentials, system files, and unrelated processes.

## Failure modes
If target ownership or scope is unclear, stop before mutation.

## Expected output
Report commands, target state, change, and verification.

## Validation
The intended service or environment state is observable after the change.

## Agent handoff

- Selected when: Use when the requested outcome matches this skill description and workflow.
- Do not activate when: Do not activate when the task matches the stated exclusion or a narrower skill.
- Expected output: Produce the observable artifact, decision, or result described by the workflow.
- User-facing report: Summarize scope, result, checks, and unresolved risks.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
