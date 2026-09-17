# Evaluation

## Representative task
Investigate a reproducible failing test, isolate the root cause, implement a minimal fix, and add regression coverage.

Expected: explain symptom, cause, fix, and verification.

Failure condition: Patch symptoms without reproducing or isolating the cause.

Validation: Re-run the original failure and the regression test after the fix.

## Boundary task
Rewrite a module without a reported failure or behavior target.

Expected: do not frame speculative redesign as debugging.

Failure condition: Change unrelated behavior without a failure hypothesis.

Validation: Confirm the work stops or is reframed as a separate design task.
