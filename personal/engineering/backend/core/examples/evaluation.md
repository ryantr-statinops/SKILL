# Evaluation

## Representative task

Task: Start a backend service and decide its boundary, persistence contract, error model, tests, and operational checks.

Expected: Define consumers and ownership, service boundary, API inputs/outputs/errors, persistence and consistency, security boundaries, side effects, async/retry behavior, tests, health, observability, and the smallest implementation path.

Failure condition: Begin coding without a contract or ownership boundary, expose persistence accidentally, or omit security, failure, testing, and operational behavior.

Validation: Review the service contract, security and side-effect boundaries, failure matrix, test plan, health/observability plan, and smallest meaningful validation.

## Boundary task

Task: Add a CSS change to a frontend page.

Expected: Route to lightweight web guidance, not backend core.

Failure condition: Introduce backend persistence or service boundaries for a presentation-only change.

Validation: Confirm no backend foundation work is required.
