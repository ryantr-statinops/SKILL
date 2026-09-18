---
name: docker
description: Design and troubleshoot personal Docker images and compose environments with reproducibility and minimal operational complexity.
category: personal
subject: engineering
scope: personal
status: experimental
version: 1.0.0
invocation: both
---

# Docker workflow

## When to use
Use for containerization, image builds, local services, and compose environments.

## Personal principles
Prefer small deterministic images, explicit configuration, and easy local inspection.

## Workflow
Inspect app/runtime needs, define image boundary, build with pinned inputs, run health checks, and verify logs/network/volumes.

## Decision rules
Do not containerize complexity that the project does not need.

## Constraints
Keep secrets out of images and make persistence explicit.

## Failure modes
Distinguish image build, startup, network, volume, and application failures.

## Expected output
Provide Dockerfile/compose changes, commands, configuration, and checks.

## Validation
Build and startup are reproducible and health checks pass.

## Agent handoff

- Selected when: Use when the requested outcome matches this skill description and workflow.
- Do not activate when: Do not activate when the task matches the stated exclusion or a narrower skill.
- Expected output: Produce the observable artifact, decision, or result described by the workflow.
- User-facing report: Summarize scope, result, checks, and unresolved risks.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
