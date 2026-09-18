# Evaluation

## Representative task

Task: Diagnose a Linux service that cannot start because of permissions, processes, or filesystem state.

Expected: Inspect state first, make the smallest safe change, and verify service recovery.

Failure condition: Delete files, kill processes, or change permissions broadly without evidence.

Validation: Record commands, affected scope, and before/after service status.

## Boundary task

Task: Choose a database for an application workload.

Expected: Route to data databases rather than Linux operations.

Failure condition: Treat host administration as a substitute for workload analysis.

Validation: Confirm storage choice is based on data behavior.
