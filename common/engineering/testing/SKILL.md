---
name: testing
description: Design, run, and evaluate tests that verify intended behavior, boundaries, and regression risk.
category: common
subject: engineering
scope: universal
status: experimental
version: 1.0.0
---

# Testing

## When to use
Use when adding behavior, fixing a bug, changing a contract, or assessing regression risk.

## Workflow
1. Identify the behavior and its public contract.
2. Choose focused unit, integration, or end-to-end coverage.
3. Cover success, boundary, invalid, and failure cases.
4. Run the smallest relevant checks, then the broader suite when justified.
5. Investigate failures instead of weakening assertions.

## Decision rules
- Test observable behavior rather than implementation details.
- Prefer deterministic, fast tests for repeated feedback.

## Failure modes
Do not report success when tests were skipped, flaky, or unrelated to the changed behavior.

## Expected output
Report tests run, results, coverage of risk, and known limitations.

## Validation
The new or changed behavior has a passing test and an appropriate boundary case.
