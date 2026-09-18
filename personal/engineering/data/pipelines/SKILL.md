---
name: pipelines
description: Design personal data pipelines with explicit inputs, transformations, outputs, quality checks, and reproducible execution.
category: personal
subject: engineering
scope: personal
status: experimental
version: 1.0.0
---

# Data pipelines

## When to use
Use when ingesting, transforming, validating, or publishing data repeatedly.

## Personal principles
Prefer observable, restartable, local-first pipelines before distributed systems.

## Workflow
Define grain and contracts, inspect inputs, separate stages, persist useful checkpoints, validate outputs, and record lineage.

## Decision rules
Make idempotency and failure recovery explicit before scheduling.

## Constraints
Do not mutate source data without a documented snapshot and transformation record.

## Failure modes
Quarantine invalid records and report partial completion instead of silently dropping them.

## Expected output
Provide pipeline stages, contracts, checks, and rerun instructions.

## Validation
The pipeline can be rerun safely and produces measurable quality results.

## Agent handoff

- Selected when: Use when the requested outcome matches this skill description and workflow.
- Do not activate when: Do not activate when the task matches the stated exclusion or a narrower skill.
- Expected output: Produce the observable artifact, decision, or result described by the workflow.
- User-facing report: Summarize scope, result, checks, and unresolved risks.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
