---
name: schema-validation
description: Validate data structure, types, constraints, and compatibility before analysis, transfer, or loading.
category: common
subject: data
scope: universal
status: experimental
version: 1.0.0
---

# Schema validation

## When to use
Use when accepting, transforming, migrating, or publishing structured data.

## Workflow
1. Identify the authoritative schema and intended version.
2. Validate required fields, types, nullability, ranges, uniqueness, and relationships.
3. Separate schema errors from record-level quality errors.
4. Report all actionable failures without mutating the source.

## Decision rules
- Reject incompatible data at the boundary rather than corrupting downstream state.
- Treat schema changes as compatibility decisions, not incidental fixes.

## Failure modes
If no authoritative schema exists, generate an observed profile and mark it provisional.

## Expected output
Provide pass/fail status, violations, affected records, and compatibility impact.

## Validation
Validation is deterministic and can be rerun against the same input.
