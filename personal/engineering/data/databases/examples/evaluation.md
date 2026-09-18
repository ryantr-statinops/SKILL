# Evaluation

## Representative task

Task: Choose storage and indexing for a growing dataset with known query patterns and modest operations capacity.

Expected: Compare workload, consistency, scale, backup, migration, and operational simplicity.

Failure condition: Choose a database from popularity without workload evidence.

Validation: Review representative queries, constraints, and a migration/backup plan.

## Boundary task

Task: Decide when a failed scheduled job should retry.

Expected: Route to orchestration guidance unless the retry decision depends on storage semantics.

Failure condition: Treat scheduling policy as a database selection problem.

Validation: Confirm the response focuses on dependencies and retry safety.
