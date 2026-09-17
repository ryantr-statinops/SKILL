# Evaluation

## Representative task

Task: Decide whether a personal backend should remain one service or split a boundary around an independently changing workload.

Expected: Identify ownership, data flow, failure isolation, operations, and change cost before choosing a boundary.

Failure condition: Split services without independent ownership or operational justification.

Validation: Review the boundary diagram and explicit cost/benefit assumptions.

## Boundary task

Task: Rename a private helper inside one module.

Expected: Use refactoring guidance unless the change reveals a real service boundary problem.

Failure condition: Propose distributed architecture for a local symbol change.

Validation: Confirm the solution remains module-scoped.
