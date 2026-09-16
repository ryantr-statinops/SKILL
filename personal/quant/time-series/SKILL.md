---
name: time-series
description: Analyze personal time-series problems with explicit temporal structure, stationarity assumptions, leakage controls, and uncertainty.
category: personal
subject: quant
scope: personal
status: experimental
version: 1.0.0
---

# Time-series foundations

## When to use
Use for temporal data exploration, modeling, forecasting, or evaluation.

## Personal principles
Respect time order and compare against simple baselines.

## Workflow
Inspect timestamps and gaps, define forecast horizon, split chronologically, establish baseline, model, and evaluate residuals and uncertainty.

## Decision rules
Do not use random splits or future-derived features for temporal prediction.

## Constraints
Report nonstationarity, missing periods, regime change, and forecast uncertainty.

## Failure modes
If timestamp semantics or leakage risk is unclear, stop before modeling.

## Expected output
Provide temporal data contract, baseline, method, evaluation, and limitations.

## Validation
The evaluation preserves time order and beats or explains the baseline honestly.
