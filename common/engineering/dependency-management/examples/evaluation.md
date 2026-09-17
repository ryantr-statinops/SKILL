# Evaluation

## Representative task
Task: Add a package required by a feature while checking compatibility, lockfiles, license, security, and tests.

Expected: minimal synchronized dependency change with rationale.

Failure condition: Add unreviewed packages or leave lockfiles inconsistent.

Validation: Run dependency, license, security, and test checks for the changed set.

## Boundary task
Task: Upgrade every outdated dependency during a focused feature change.

Expected: avoid unrelated upgrades and scope expansion.

Failure condition: Upgrade the entire dependency graph during a focused change.

Validation: Confirm the diff contains only justified dependency changes.
