# Evaluation

## Representative task
Implement a change in a large repository while loading only relevant instructions, entrypoints, tests, and references.

Expected: maintain a focused evidence map and avoid reading unrelated domains.

Failure condition: Load broad context without a task-relevant reason.

Validation: Review the evidence map and loaded files against the task.

## Boundary task
Diagnose a failure whose complete reproduction and source are already provided.

Expected: do not request or load unrelated repository context.

Failure condition: Expand context after the necessary reproduction is already available.

Validation: Confirm the investigation uses the supplied evidence first.
