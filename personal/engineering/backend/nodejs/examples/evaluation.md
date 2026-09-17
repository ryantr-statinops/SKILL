# Evaluation

## Representative task

Task: Build a Node.js API with runtime configuration, request validation, tests, and a clear production start command.

Expected: Separate application code from configuration, define error behavior, and verify the runtime path.

Failure condition: Rely on undocumented local environment state or mix development and production commands.

Validation: Run the defined test and start checks in a clean environment.

## Boundary task

Task: Write a one-off Node.js script to rename local files with no service or API.

Expected: Use the smallest scripting workflow; activate Node.js backend only if service concerns appear.

Failure condition: Add API, deployment, and service architecture complexity to a local utility.

Validation: Confirm the solution remains a bounded script.
