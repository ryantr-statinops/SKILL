---
name: data-inspection
description: Profile a dataset's shape, schema, quality, and distributions before transforming or analyzing it.
category: common
subject: data
scope: universal
status: experimental
version: 1.0.0
---

# Data inspection

## When to use
Use before analysis, cleaning, migration, or pipeline design when data structure is not fully known.

## Workflow
1. Identify source, format, size, sensitivity, and intended grain.
2. Inspect columns, types, nulls, duplicates, ranges, and representative records.
3. Check anomalies and assumptions against available documentation.
4. Report findings before proposing transformations.

## Decision rules
- Do not infer semantics from column names alone.
- Preserve a read-only snapshot when the source is important.

## Failure modes
If the dataset cannot be loaded or is incomplete, report the exact limitation.

## Expected output
Provide a concise profile, quality risks, and recommended next checks.

## Validation
Inspection is reproducible and does not mutate the source data.
