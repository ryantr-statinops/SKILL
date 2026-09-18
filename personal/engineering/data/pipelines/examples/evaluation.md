# Evaluation

## Representative task

Task: Design an ingestion pipeline with explicit inputs, transformations, outputs, quality gates, and rerun behavior.

Expected: Make each stage inspectable and define what happens on malformed, duplicate, or late data.

Failure condition: Treat a successful local run as proof of reproducibility or correctness.

Validation: Run a fixture containing valid and invalid records and inspect the outputs.

## Boundary task

Task: Create a dashboard from a stable table with no ingestion or transformation work.

Expected: Use the relevant frontend or analysis workflow instead of pipeline design.

Failure condition: Rebuild ingestion without evidence that the source contract changed.

Validation: Confirm the work begins from the stable data contract.
