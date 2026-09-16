---
name: refactoring
description: Improve code structure and maintainability while preserving externally observable behavior.
category: common
subject: engineering
scope: universal
status: experimental
version: 1.0.0
---

# Refactoring

## When to use
Use when structure, duplication, naming, or coupling makes safe change harder.

## Workflow
1. Establish current behavior with tests or a reproducible example.
2. Identify one structural smell and define a small target.
3. Make incremental changes without mixing new behavior.
4. Run focused checks after each meaningful step.

## Decision rules
- Prefer small local improvements over speculative rewrites.
- Do not refactor code without a way to verify behavior.

## Failure modes
If behavior changes unexpectedly, revert the smallest step and isolate the cause.

## Expected output
Describe structural improvement, preserved behavior, and verification.

## Validation
Relevant tests pass and the diff contains no unrelated feature changes.
