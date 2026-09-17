# Evaluation

## Representative task

Task: Implement a maintainable Python backend endpoint with typed boundaries, configuration, tests, and clear errors.

Expected: Keep business logic testable, dependencies explicit, and runtime behavior reproducible.

Failure condition: Depend on hidden interpreter state or skip validation of failure paths.

Validation: Run the project test command and inspect the clean-start path.

## Boundary task

Task: Explore a CSV interactively to understand its columns.

Expected: Use data-inspection or R guidance rather than backend service workflow.

Failure condition: Create service layers for exploratory analysis.

Validation: Confirm the output is an inspection result, not an API.
