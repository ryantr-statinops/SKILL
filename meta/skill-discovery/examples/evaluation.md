## Representative task

Task: Route a request to add a feature while identifying the narrowest
workflow, relevant supporting skills, and nearby exclusions.

Expected: Select the most specific applicable skill, explain the boundary, and
load only the resources needed for the task.

Failure condition: Load every skill, select a broad skill over a specific one,
or silently merge conflicting procedures.

Validation: Confirm the selected skill, rejected candidates, and required
resources are reported with a clear routing reason.

## Boundary task

Task: Implement a backend endpoint using an already selected engineering skill.

Expected: Route to the relevant engineering skill rather than treating skill
library discovery as the implementation workflow.

Failure condition: Invoke repository-level skill discovery for unrelated domain
implementation work.

Validation: Confirm the discovery skill is excluded and the domain skill owns
the implementation procedure.
