---
name: change-review
description: Review a proposed change for correctness, scope, regression risk, tests, and readiness to hand off.
category: common
subject: delivery
scope: universal
status: experimental
version: 1.0.0
invocation: both
---

# Change review

## When to use
Use when a completed change needs a final scope, readiness, or handoff decision before merging, handing off, or publishing.

## When not to use
Do not use for line-by-line defect finding; use `code-review`. Do not use before the change has a reviewable artifact.

## Workflow
1. Read the requested behavior and inspect the complete diff.
2. Check correctness, edge cases, compatibility, tests, security, and documentation.
3. Identify breaking changes and residual risk.
4. Prepare actionable findings and a concise change summary.

## Decision rules
- Block handoff on correctness or security defects; separate style suggestions.
- Verify changed behavior instead of trusting a green unrelated test suite.
- Choose this skill when the output is a release or handoff decision with explicit follow-up ownership.

## Failure modes
If the diff or validation context is incomplete, report the review as limited.

## Expected output
Provide findings by severity, validation evidence, and handoff recommendation.

## Validation
All blocking findings are resolved or explicitly accepted by the responsible owner.

## Agent handoff

- Selected when: Use the activation boundary and outcome described in this skill.
- Do not activate when: The task matches the stated exclusion or a narrower skill.
- Expected output: Produce the observable result and validation described by the workflow.
- User-facing report: Summarize scope, result, checks, and unresolved risks.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
