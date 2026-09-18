---
name: latex
description: Create maintainable LaTeX documents for mathematical, technical, and educational writing.
category: personal
subject: education
scope: personal
status: experimental
version: 1.0.0
---

# LaTeX foundations

## When to use
Use for structured mathematical or technical documents.

## Personal principles
Prefer semantic structure, readable source, reusable macros, and reproducible builds.

## Workflow
Define document structure, choose minimal packages, write content semantically, build early, and inspect warnings/output.

## Decision rules
Do not fix layout symptoms with arbitrary spacing before understanding structure.

## Constraints
Keep source portable and document required tools.

## Failure modes
If compilation fails, isolate the smallest failing document.

## Expected output
Provide source, build command, and rendered verification.

## Validation
The document builds cleanly enough for its purpose and has no unresolved references.

## Agent handoff

- Selected when: Use when the requested outcome matches this skill description and workflow.
- Do not activate when: Do not activate when the task matches the stated exclusion or a narrower skill.
- Expected output: Produce the observable artifact, decision, or result described by the workflow.
- User-facing report: Summarize scope, result, checks, and unresolved risks.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
