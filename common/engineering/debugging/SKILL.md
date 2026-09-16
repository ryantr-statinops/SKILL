---
name: debugging
description: Investigate software failures by reproducing, isolating, hypothesizing, fixing, and verifying the root cause.
category: common
subject: engineering
scope: universal
status: experimental
version: 1.0.0
---

# Debugging

## When to use
Use when behavior is failing, inconsistent, unexpected, or difficult to explain.

## Workflow
1. Capture the exact symptom, environment, and reproduction.
2. Reduce the failure to the smallest useful case.
3. Form and test evidence-based hypotheses.
4. Fix the root cause with the smallest safe change.
5. Add or update a regression check and verify the original reproduction.

## Decision rules
- Change one relevant variable at a time when isolating a cause.
- Prefer evidence from logs, tests, and minimal reproductions over speculation.

## Failure modes
If reproduction is unavailable, document uncertainty and add observability before guessing.

## Expected output
Explain symptom, root cause, fix, verification, and remaining limitations.

## Validation
The original failure no longer reproduces and relevant regression checks pass.
