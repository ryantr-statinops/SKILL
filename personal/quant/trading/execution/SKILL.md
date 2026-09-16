---
name: execution
description: Review quantitative execution and risk controls without independently placing, modifying, or cancelling orders.
category: personal
subject: quant
scope: personal
status: experimental
version: 1.0.0
---

# Execution and risk

## When to use
Use for execution design, position sizing, order validation, or risk review.

## Personal principles
Make risk constraints explicit and fail closed when state or authorization is uncertain.

## Workflow
Validate instrument and account state, define exposure and order constraints, simulate checks, and report whether the plan is ready for human review.

## Decision rules
No valid risk state means no execution recommendation.

## Constraints
Never infer authorization to send an order.

## Failure modes
Stop on stale prices, unknown positions, missing limits, or tool ambiguity.

## Expected output
Provide risk checks, rejected conditions, assumptions, and human approval points.

## Validation
All constraints are testable and no external execution occurred.
