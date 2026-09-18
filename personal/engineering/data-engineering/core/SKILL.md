---
name: core
description: Apply personal data-engineering foundations for data contracts, lineage, quality, storage, and reproducible workflows.
category: personal
subject: data-engineering
scope: personal
status: experimental
version: 1.0.0
---

# Data engineering foundations

## When to use
Use before choosing pipeline, database, or orchestration details.

## Personal principles
Prefer inspectable local-first systems, explicit contracts, and measurable data quality.

## Workflow
Define grain and ownership, inspect source, specify schema and quality rules, design lineage, choose storage, and plan recovery.

## Decision rules
Do not introduce distributed infrastructure before workload and operational needs are measured.

## Constraints
Preserve source data and make transformations, checkpoints, and failures visible.

## Failure modes
If semantics or ownership are unclear, stop before building transformations.

## Expected output
Provide data contract, flow, quality checks, storage rationale, and recovery path.

## Validation
The workflow is rerunnable and output quality can be measured.

## Agent handoff

- Selected when: Use when the requested outcome matches this skill description and workflow.
- Do not activate when: Do not activate when the task matches the stated exclusion or a narrower skill.
- Expected output: Produce the observable artifact, decision, or result described by the workflow.
- User-facing report: Summarize scope, result, checks, and unresolved risks.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
