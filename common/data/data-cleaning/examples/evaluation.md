# Evaluation

## Representative task
Task: Clean duplicate and invalid records with documented rules, preserved input, and before/after quality metrics.

Expected: traceable output and explicit exclusions.

Failure condition: Mutate the source or silently discard records.

Validation: Compare preserved input, rules, counts, and output metrics.

## Boundary task
Task: Drop ambiguous records without a domain rule.

Expected: stop and request the missing decision.

Failure condition: Invent a domain rule for ambiguous records.

Validation: Confirm the ambiguous records and missing decision are reported.
