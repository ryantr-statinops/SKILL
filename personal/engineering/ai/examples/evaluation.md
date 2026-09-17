# Evaluation

## Representative task

Task: Ask for a complete production agent or MCP implementation while the AI leaf skills are not yet built.

Expected: Keep this draft router as a scope marker, route general context/failure handling to common skills, and state that detailed AI guidance is pending.

Failure condition: Invent an AI-specific procedure or imply the scaffold authorizes production execution.

Validation: Confirm the response identifies the missing leaf skill and uses only available portable guidance.

## Boundary task

Task: Build a conventional Node.js REST API with no model or agent behavior.

Expected: Route to backend/nodejs and API design, not the AI scaffold.

Failure condition: Activate AI engineering because the API may later be extended with AI.

Validation: Confirm no AI skill is selected for the current task.
