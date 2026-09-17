# Evaluation

## Representative task

Task: Analyze a temporal dataset where stationarity, seasonality, autocorrelation, and forecast leakage may affect conclusions.

Expected: Preserve temporal ordering, test assumptions, separate train/validation periods, and report uncertainty.

Failure condition: Randomly shuffle temporal observations or leak future information into features.

Validation: Review the split, diagnostics, baseline, and forecast evaluation.

## Boundary task

Task: Compare two static groups with no meaningful time order.

Expected: Route to statistics rather than time-series analysis.

Failure condition: Invent temporal structure because timestamps happen to exist.

Validation: Confirm the method follows the data-generating process.
