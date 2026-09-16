---
name: code-review
description: Review a code change for correctness, maintainability, security risk, regression risk, and test adequacy.
category: common
subject: engineering
scope: universal
status: experimental
version: 1.0.0
---

# Code review

## When to use
Use when assessing a diff, pull request, patch, or proposed implementation.

## Workflow
1. Read the requested behavior and relevant surrounding code.
2. Inspect the diff for correctness, edge cases, errors, and unintended scope.
3. Check tests, contracts, security boundaries, and maintainability.
4. Report findings by severity with file and line evidence.

## Decision rules
- Prioritize concrete defects over style preferences.
- Report no issue when the evidence supports correctness; do not invent concerns.

## Failure modes
If context or tests are missing, state the review limitation explicitly.

## Expected output
Return actionable findings first, followed by residual risks and summary.

## Validation
Every finding has evidence, impact, and a clear remediation direction.
