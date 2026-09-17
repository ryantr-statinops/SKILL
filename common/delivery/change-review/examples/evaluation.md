# Evaluation

## Representative task
Review a proposed change before merge and report correctness, tests, compatibility, security, and breaking risks.

Expected: actionable blocking findings and handoff recommendation.

Failure condition: Approve without enough diff, test, or compatibility evidence.

Validation: Check each finding has evidence, impact, severity, and next action.

## Boundary task
Approve a change with no diff or validation evidence.

Expected: mark review as limited and request the missing evidence.

Failure condition: Infer correctness from an absent diff or absent checks.

Validation: Confirm the review is explicitly blocked or limited.
