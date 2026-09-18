## Representative task

Task: Explain a regression result with descriptive summaries, assumptions, uncertainty, residual checks, and a time-aware validation plan where the data is temporal.

Expected: Define the estimand/target, inspect the data-generating context, state regression and temporal assumptions, choose a simple baseline, evaluate residuals and leakage risk, and distinguish prediction, association, and causal claims.

Failure condition: Report a coefficient or p-value without assumptions, uncertainty, diagnostics, baseline, or temporal validation, or claim causality from an observational result.

Validation: Review the question, method, assumptions, diagnostics, uncertainty, baseline, split strategy, and limitations.

## Boundary task

Task: Build a rerunnable data pipeline with source contracts, schema checks, lineage, storage, and recovery.

Expected: Route to `personal/engineering/data` and its pipeline/core skills; use statistics only for any explicit distribution, missingness, or quality analysis.

Failure condition: Design storage, orchestration, or recovery primarily as a statistical analysis.

Validation: Confirm the primary route is data engineering and the statistical contribution is limited to stated analytical checks.
