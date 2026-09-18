# Evaluation

## Representative task

Task: Build a small R analysis that reads data, transforms it, produces a plot, and can be rerun.

Expected: Keep the analysis inspectable, separate data preparation from results, and record package/runtime assumptions.

Failure condition: Hide transformations in manual console state or overwrite source data.

Validation: Run the analysis from a clean session and compare expected artifacts.

## Boundary task

Task: Decide whether a database schema supports an ingestion workload.

Expected: Route to data engineering database guidance, not R foundations.

Failure condition: Use a plotting workflow as a substitute for system design.

Validation: Confirm the response addresses storage and workload constraints.
