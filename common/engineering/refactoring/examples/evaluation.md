# Evaluation

## Representative task
Task: Reduce duplication in a covered module without changing public behavior.

Expected: incremental refactor with passing regression tests and no feature drift.

Failure condition: Change behavior or public contracts without declaring a new scope.

Validation: Compare behavior tests before and after the refactor.

## Boundary task
Task: Change a public API contract while calling the work a refactor.

Expected: classify it as a behavior change and require explicit scope.

Failure condition: Hide a breaking API change under a refactor label.

Validation: Confirm the proposed contract change is separately reviewed.
