---
name: skill-evaluation
description: Evaluate whether an Agent Skill produces useful, bounded, and repeatable behavior on realistic tasks.
category: meta
subject: skill-system
scope: repository
status: stable
version: 1.0.0
---

# Skill evaluation

## When to use

Use when reviewing a new or changed skill, diagnosing weak behavior, or deciding
whether a skill is ready to publish.

## Workflow

1. Choose one representative task and one boundary task.
2. Record the expected behavior, required artifacts, and validation signals.
3. Run the task with the skill available and inspect the actual output.
4. Check routing, procedure, decisions, failure handling, and context usage.
5. Record failures as a narrow change request; do not add broad rules without evidence.
6. Re-run the representative and boundary tasks after changes.

## Quality checklist

- The description activates for the intended task and excludes nearby tasks.
- The procedure is actionable without duplicating general model knowledge.
- References are loaded only when relevant.
- Scripts, if present, are deterministic and tested.
- The expected result and validation are observable.
- Failure modes lead to safe, useful behavior.

## Evaluation levels

- **Static:** structure, metadata, links, naming, and validator checks.
- **Manual:** realistic task and boundary-task review.
- **Regression:** repeat prior cases after a change.

Agent-based evaluation is optional; use it when the skill is complex enough that
independent behavioral review materially improves confidence.
