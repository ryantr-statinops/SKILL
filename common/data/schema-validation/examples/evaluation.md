# Evaluation

## Representative task
Task: Validate incoming records against required fields, types, nullability, ranges, and uniqueness constraints.

Expected: deterministic violations report without mutating input.

Failure condition: Hide invalid values through silent coercion or mutation.

Validation: Run the same fixture twice and compare the violations report.

## Boundary task
Task: Silently coerce incompatible data to make validation pass.

Expected: reject or report incompatibility instead of hiding it.

Failure condition: Make validation pass by changing the input silently.

Validation: Confirm the original incompatible value remains observable.
