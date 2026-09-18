# Evaluation

## Representative task

Task: Route a request to ingest source files, validate data, store results, and schedule the workflow.

Expected: Select data core plus pipelines, databases, or orchestration according to the actual outcome.

Failure condition: Load every data skill without distinguishing ingestion, storage, and scheduling needs.

Validation: Confirm the route names the primary workflow and optional supporting skills.

## Boundary task

Task: Design an HTTP API that returns already-prepared records.

Expected: Route to backend/API design unless ingestion or transformation is part of the request.

Failure condition: Treat data access through an API as a full pipeline design.

Validation: Confirm the route follows the system boundary.
