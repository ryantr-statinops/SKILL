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
