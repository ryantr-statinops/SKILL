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

## Agent handoff

- Selected when: Use when the requested outcome matches this skill description and workflow.
- Do not activate when: Do not activate when the task matches the stated exclusion or a narrower skill.
- Expected output: Produce the observable artifact, decision, or result described by the workflow.
- User-facing report: Summarize scope, result, checks, and unresolved risks.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
