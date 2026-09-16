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
