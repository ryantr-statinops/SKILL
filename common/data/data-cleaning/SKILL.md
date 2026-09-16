---
name: data-cleaning
description: Clean invalid, duplicate, missing, or inconsistent records while preserving traceability and stated assumptions.
category: common
subject: data
scope: universal
status: experimental
version: 1.0.0
---

# Data cleaning

## When to use
Use when a dataset needs controlled preparation before analysis or loading.

## Workflow
1. Profile the input and define quality rules.
2. Preserve the original and record every transformation.
3. Handle missing, duplicate, invalid, and inconsistent values explicitly.
4. Measure before/after row counts and quality changes.
5. Validate the cleaned output against its intended schema.

## Decision rules
- Never silently drop records or impute values without documenting the rule.
- Prefer reversible transformations and quarantine irreconcilable records.

## Failure modes
If the correct cleaning rule is ambiguous, stop and request a domain decision.

## Expected output
Return cleaned data plus transformation summary, exclusions, and quality results.

## Validation
The source is unchanged and the output satisfies documented quality rules.
