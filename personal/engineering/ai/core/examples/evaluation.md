# Evaluation

## Representative task

Task: Design an LLM application with retrieval, structured output, tool boundaries, evaluation, monitoring, and a fallback path.

Expected: Define the user outcome and deterministic baseline, separate model/context/retrieval/tool/application boundaries, specify structured-output and tool validation, include representative and boundary evaluations, and state production constraints and human approval boundaries.

Failure condition: Treat a demo as production evidence, grant broad tool permissions, or omit evaluation, cost, privacy, rate-limit, fallback, and side-effect controls.

Validation: Confirm the response includes system boundaries, evaluation cases, permission controls, monitoring, fallback, and unresolved risks.

## Boundary task

Task: Debug an ordinary Python function that does not use AI.

Expected: Use common debugging or personal Python guidance, not AI core.

Failure condition: Introduce model or agent concepts into an unrelated bug.

Validation: Confirm the selected skill matches the actual implementation.
