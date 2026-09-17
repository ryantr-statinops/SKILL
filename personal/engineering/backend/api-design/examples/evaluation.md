# Evaluation

## Representative task

Task: Design a public API for creating and retrieving a resource with validation, errors, and backward compatibility.

Expected: Define request/response contracts, validation, error semantics, idempotency where relevant, and compatibility checks.

Failure condition: Describe endpoints only by URL names without a usable contract.

Validation: Review example requests/responses and contract tests.

## Boundary task

Task: Refactor an internal function with no API boundary.

Expected: Use refactoring guidance and do not create an API contract unnecessarily.

Failure condition: Turn an internal code cleanup into public interface design.

Validation: Confirm no external contract was invented.
