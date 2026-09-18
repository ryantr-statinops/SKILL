---
name: core
description: Apply personal backend foundations for service boundaries, contracts, persistence, errors, tests, and operations.
category: personal
subject: backend
scope: personal
status: experimental
version: 1.0.0
---

# Backend foundations

## When to use
Use before choosing a backend language or implementing a service boundary.

## Personal principles
Prefer explicit contracts, simple components, observable failures, and testable behavior.

## Workflow
Define inputs/outputs, ownership, persistence, errors, configuration, health, and validation before implementation.

## Decision rules
Separate domain logic from transport and infrastructure concerns.

## Constraints
Keep secrets out of source and make side effects explicit.

## Failure modes
If contract or ownership is unclear, stop before selecting a framework.

## Expected output
Provide service boundaries, contracts, risks, and a minimal implementation path.

## Validation
The service can be tested at its boundary and its failure behavior is observable.

## Agent handoff

- Selected when: Use when the requested outcome matches this skill description and workflow.
- Do not activate when: Do not activate when the task matches the stated exclusion or a narrower skill.
- Expected output: Produce the observable artifact, decision, or result described by the workflow.
- User-facing report: Summarize scope, result, checks, and unresolved risks.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
