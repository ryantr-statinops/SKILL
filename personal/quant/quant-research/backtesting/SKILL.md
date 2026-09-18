---
name: backtesting
description: Design and review quantitative backtests with time ordering, costs, leakage controls, and reproducible results.
category: personal
subject: quant
scope: personal
status: experimental
version: 1.0.0
---

# Backtesting

## When to use
Use for historical evaluation of a strategy or signal.

## Personal principles
Treat a backtest as an experiment with failure modes, not proof of future returns.

## Workflow
Define timestamps, universe, data, signal, execution delay, costs, benchmark, splits, metrics, and robustness checks.

## Decision rules
Never hide transaction costs, rejected trades, warm-up periods, or parameter selection.

## Constraints
No automatic live execution follows from a passing backtest.

## Failure modes
Stop on leakage, impossible fills, survivorship bias, or unstable results.

## Expected output
Provide methodology, metrics, assumptions, sensitivity, and limitations.

## Validation
Results are reproducible and include out-of-sample and baseline comparisons.

## Agent handoff

- Selected when: Use when the requested outcome matches this skill description and workflow.
- Do not activate when: Do not activate when the task matches the stated exclusion or a narrower skill.
- Expected output: Produce the observable artifact, decision, or result described by the workflow.
- User-facing report: Summarize scope, result, checks, and unresolved risks.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
