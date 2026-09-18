---
name: mt5
description: Analyze MT5 account, market, and integration workflows without placing or modifying trades automatically.
category: personal
subject: quant
scope: personal
status: experimental
version: 1.0.0
---

# MT5 foundations

## When to use
Use for MT5 data, account-state, symbol, or integration analysis.

## Personal principles
Inspect account and market state before discussing any action.

## Workflow
Validate connection and environment, inspect symbol/account state, check data quality, and report observations.

## Decision rules
A research or analysis request never authorizes an order.

## Constraints
Keep credentials private and require explicit confirmation for any execution action.

## Failure modes
If account, symbol, or market state is stale or unavailable, stop and report it.

## Expected output
Provide observed state, timestamp, assumptions, and safe next options.

## Validation
Observations are tied to verified data and no unintended trade side effect occurred.

## Agent handoff

- Selected when: Use when the requested outcome matches this skill description and workflow.
- Do not activate when: Do not activate when the task matches the stated exclusion or a narrower skill.
- Expected output: Produce the observable artifact, decision, or result described by the workflow.
- User-facing report: Summarize scope, result, checks, and unresolved risks.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
