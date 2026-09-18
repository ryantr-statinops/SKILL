---
name: lightweight-web
description: Build small maintainable web interfaces for personal projects without unnecessary frontend infrastructure.
category: personal
subject: engineering
scope: personal
status: experimental
version: 1.0.0
invocation: both
---

# Lightweight web

## When to use
Use for simple dashboards, portfolio surfaces, internal tools, or project interfaces.

## Personal principles
Prefer clear user flows, accessible HTML, minimal dependencies, and fast feedback.

## Workflow
Define the user path, choose the smallest stack, build semantic structure, add responsive styling, connect data, and verify behavior.

## Decision rules
Do not introduce a large frontend framework for a static or small interactive surface without evidence.

## Constraints
Keep loading, accessibility, security, and maintenance visible.

## Failure modes
If backend contract or user outcome is unclear, clarify it before polishing UI.

## Expected output
Provide a usable interface, run instructions, and behavior verification.

## Validation
Core flow works on a narrow viewport and keyboard-accessible path.

## Agent handoff

- Selected when: Use when the requested outcome matches this skill description and workflow.
- Do not activate when: Do not activate when the task matches the stated exclusion or a narrower skill.
- Expected output: Produce the observable artifact, decision, or result described by the workflow.
- User-facing report: Summarize scope, result, checks, and unresolved risks.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
