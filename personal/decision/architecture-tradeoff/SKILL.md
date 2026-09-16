---
name: architecture-tradeoff
description: Make explicit architecture trade-offs for personal systems across simplicity, performance, reliability, cost, and changeability.
category: personal
subject: decision
scope: personal
status: experimental
version: 1.0.0
---

# Architecture trade-offs

## When to use
Use when two or more architecture options are viable and the choice has future cost.

## Personal principles
Prefer reversible decisions and visible operational complexity.

## Workflow
1. State the decision and constraints.
2. Model options, data flow, failure modes, and ownership.
3. Compare short-term and long-term costs.
4. Choose, record rationale, and define a revisit trigger.

## Decision rules
Do not optimize for hypothetical scale at the cost of current learning.

## Constraints
Include maintenance and debugging cost, not only performance.

## Failure modes
If trade-offs cannot be measured, propose a bounded experiment.

## Expected output
Return options, trade-off matrix, decision, risks, and revisit conditions.

## Validation
The chosen design has an explicit reason and a way to detect when it no longer fits.
