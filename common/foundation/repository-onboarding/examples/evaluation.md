# Evaluation

## Representative task
Task: Inspect an unfamiliar repository and summarize its instructions, structure, Git state, entrypoints, and relevant test commands.

Expected: a concise evidence-backed map before edits.

Failure condition: Modify files before checking repository instructions and state.

Validation: Review the map for instructions, structure, Git state, entrypoints, and checks.

## Boundary task
Task: Change a known one-line value in a repository whose conventions are already supplied.

Expected: do not perform a full onboarding ritual when no unknown context exists.

Failure condition: Delay a bounded change with irrelevant repository exploration.

Validation: Confirm only task-relevant context was loaded.
