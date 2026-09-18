---
name: project-init
description: Initialize a personal software project with a minimal structure, conventions, validation path, and documentation baseline.
category: personal
subject: workflow
scope: personal
status: experimental
version: 1.0.0
invocation: both
---

# Project initialization

## When to use
Use when starting a new personal repository or a new project component.

## Personal principles
Start with a small inspectable skeleton and make the first runnable path explicit.

## Workflow
1. Confirm purpose, scope, runtime, and repository state.
2. Create only necessary structure and configuration.
3. Add README, instructions, validation, and a minimal runnable example.
4. Run checks and document the next step.

## Decision rules
Do not create speculative folders, dependencies, or abstractions.

## Constraints
Preserve existing project conventions when initializing inside a repository.

## Failure modes
If tooling or scope is unclear, stop after documenting the decision needed.

## Expected output
Provide a runnable, documented, validated project skeleton.

## Validation
The project can be installed or started using the documented command.

## Agent handoff

- Selected when: Use when the requested outcome matches this skill description and workflow.
- Do not activate when: Do not activate when the task matches the stated exclusion or a narrower skill.
- Expected output: Produce the observable artifact, decision, or result described by the workflow.
- User-facing report: Summarize scope, result, checks, and unresolved risks.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
