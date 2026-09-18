---
name: orchestration
description: Plan and operate personal data workflow scheduling with dependencies, retries, observability, and ownership.
category: personal
subject: engineering
scope: personal
status: experimental
version: 1.0.0
---

# Data orchestration

## When to use
Use when a data workflow needs scheduling, dependencies, retries, or operational visibility.

## Personal principles
Prefer simple explicit scheduling until operational complexity is justified.

## Workflow
Define tasks and dependencies, identify idempotency, configure retries and alerts, test failure paths, and document recovery.

## Decision rules
Do not hide a fragile script behind an orchestrator; fix its contract first.

## Constraints
Retries must not duplicate unsafe side effects.

## Failure modes
Surface failed task, partial outputs, and recovery action separately.

## Expected output
Provide workflow graph, schedule, retry policy, observability, and recovery steps.

## Validation
Success, failure, retry, and rerun paths are tested or explicitly bounded.

## Agent handoff

- Selected when: Use when the requested outcome matches this skill description and workflow.
- Do not activate when: Do not activate when the task matches the stated exclusion or a narrower skill.
- Expected output: Produce the observable artifact, decision, or result described by the workflow.
- User-facing report: Summarize scope, result, checks, and unresolved risks.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
