---
name: reproducible-analysis
description: Structure data analysis so inputs, transformations, outputs, assumptions, and execution steps can be repeated and audited.
category: common
subject: data
scope: universal
status: experimental
version: 1.0.0
---

# Reproducible analysis

## When to use
Use for analysis that must be rerun, reviewed, shared, or compared over time.

## Workflow
1. Identify and preserve input versions and assumptions.
2. Separate ingestion, transformation, analysis, and presentation.
3. Make parameters and random seeds explicit where relevant.
4. Record execution environment and produce inspectable outputs.
5. Re-run from a clean starting point and compare results.

## Decision rules
- Prefer deterministic pipelines and versioned artifacts.
- Never rely on undocumented manual steps for a material result.

## Failure modes
If exact reproduction is impossible, identify the missing input, environment, or nondeterminism.

## Expected output
Deliver analysis, method, inputs, assumptions, and reproduction instructions.

## Validation
A second run from the documented inputs produces equivalent results within stated tolerance.
