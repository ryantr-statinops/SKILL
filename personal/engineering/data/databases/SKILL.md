---
name: databases
description: Choose and design personal data storage and query patterns based on workload, consistency, scale, and operational simplicity.
category: personal
subject: engineering
scope: personal
status: experimental
version: 1.0.0
invocation: both
---

# Data databases

## When to use
Use when selecting storage, schema, indexing, partitioning, or query patterns.

## Personal principles
Prefer the simplest storage that makes correctness and inspection easy.

## Workflow
Define access patterns and data lifecycle, compare storage options, model schema, test representative queries, and document trade-offs.

## Decision rules
Do not introduce distributed storage for an unmeasured local workload.

## Constraints
Include backup, migration, schema evolution, and observability in the design.

## Failure modes
If workload assumptions are unknown, measure a representative sample first.

## Expected output
Provide schema, access patterns, rationale, migration and validation plan.

## Validation
Representative queries meet correctness and stated performance expectations.

## Agent handoff

- Selected when: Use when the requested outcome matches this skill description and workflow.
- Do not activate when: Do not activate when the task matches the stated exclusion or a narrower skill.
- Expected output: Produce the observable artifact, decision, or result described by the workflow.
- User-facing report: Summarize scope, result, checks, and unresolved risks.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
