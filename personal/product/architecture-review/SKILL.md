---
name: architecture-review
description: Review a personal project architecture for fit, simplicity, boundaries, operability, and future change cost.
category: personal
subject: product
scope: personal
status: experimental
version: 1.0.0
---

# Architecture review

## When to use
Use before committing to a major architecture or when complexity is blocking progress.

## Personal principles
Prefer boring, inspectable components and reversible decisions until scale requires otherwise.

## Workflow
1. Restate requirements, constraints, and expected load.
2. Map components, data flow, boundaries, failure modes, and operations.
3. Identify complexity, coupling, lock-in, and unvalidated assumptions.
4. Compare simpler alternatives and record the decision.

## Decision rules
Do not introduce distributed infrastructure to solve an unmeasured local problem.

## Constraints
Separate current requirements from speculative future scale.

## Failure modes
If operational ownership is unclear, treat the design as incomplete.

## Expected output
Return architecture, trade-offs, risks, alternatives, and decision rationale.

## Validation
The architecture maps to current requirements and has an explicit failure strategy.
