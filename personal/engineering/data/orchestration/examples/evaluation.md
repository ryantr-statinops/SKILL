# Evaluation

## Representative task

Task: Schedule a pipeline with dependencies, retries, backfills, ownership, and observable failure states.

Expected: Define a dependency graph, idempotent steps, retry policy, alerting, and backfill procedure.

Failure condition: Retry non-idempotent work blindly or hide failed data states.

Validation: Simulate a failed step and verify recovery and alert behavior.

## Boundary task

Task: Normalize a table schema before any scheduling requirement exists.

Expected: Use data-cleaning or schema-validation guidance.

Failure condition: Add an orchestrator because the data may later be scheduled.

Validation: Confirm the task remains transformation-scoped.
