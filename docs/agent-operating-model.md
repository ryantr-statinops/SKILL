# Agent operating model

This repository is designed for an agent to read the library, select the
smallest relevant capability, perform authorized work, and explain the result
to the user.

## Lifecycle

```text
context loading
  → task classification
  → skill discovery
  → skill selection
  → user-facing explanation
  → confirmation check
  → execution
  → validation
  → final report
```

## Loading order

Use the narrowest source that provides the required context:

1. Root `AGENTS.md` and applicable runtime instructions.
2. `local.md` if present; use it for current project state only, never as a
   portable rule or public source.
3. `docs/skill-index.md` or `data/skills.json` for candidate discovery.
4. A category/router `SKILL.md` when one exists.
5. The selected leaf `SKILL.md`.
6. Only the references, scripts, examples, or assets required by the task.

Do not load every skill to compensate for uncertain routing. If no skill is a
clear match, continue with repository guidance and state that no skill was
activated.

## Selection explanation

Before a risky or multi-step task, tell the user briefly:

- selected skill ID(s);
- why they match the requested outcome;
- important assumptions and exclusions;
- whether any mutation or external action requires confirmation.

This is an explanation of the operating choice, not a request for the user to
manually execute the skill.

## Autonomy and confirmation

The agent may inspect, reason, edit in scope, and run relevant validation when
the user has authorized the task. Pause and ask before:

- deleting, resetting, overwriting, or broad destructive cleanup;
- writing to external systems or services;
- pushing, tagging, releasing, or publishing when not explicitly requested;
- making an irreversible or materially scope-expanding decision.

Preserve unrelated user changes and stop on unexpected conflicts or remote
state. Do not infer permission from a skill being available.

## Final report

The final response should include, when relevant:

```text
Selected skill(s):
Reason:
Changed files:
Validation:
Unresolved risks or assumptions:
Next action:
```

Keep the report proportional to the task. Link to important files and expose
uncertainty instead of claiming a check or action that did not happen.
