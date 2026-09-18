# Evaluation

## Representative task

Task: Establish foundations for a data workflow with a source contract, lineage, quality checks, storage, and reproducible execution.

Expected: Define grain, ownership, source semantics, contract, quality gates, lineage, storage rationale, idempotency, rerun/recovery behavior, and observability before selecting tools.

Failure condition: Choose a platform before identifying data semantics, quality measures, lineage, or failure recovery, or silently discard invalid records without documenting the impact.

Validation: Review the data contract, quality checks, lineage, storage rationale, reproducibility plan, and recovery path.

## Boundary task

Task: Tune an API response schema without changing the underlying dataset.

Expected: Use API design guidance rather than data core.

Failure condition: Add lineage and pipeline infrastructure to a presentation contract change.

Validation: Confirm the change is evaluated at the API boundary.
