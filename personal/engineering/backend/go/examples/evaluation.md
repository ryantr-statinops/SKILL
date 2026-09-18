# Evaluation

## Representative task

Task: Implement a small Go HTTP service with configuration, tests, structured errors, and graceful shutdown.

Expected: Keep the service idiomatic, explicit, testable, and operationally inspectable.

Failure condition: Hide lifecycle or configuration behavior in global state and skip failure-path tests.

Validation: Run Go tests and verify startup, shutdown, and error behavior.

## Boundary task

Task: Build a scheduled SQL transformation with no Go service.

Expected: Route to data pipelines or orchestration.

Failure condition: Choose Go backend guidance only because the pipeline could be implemented in Go.

Validation: Confirm the route follows the requested outcome.
