---
name: context-loading
description: Select and load only the context needed for an agent task while preserving evidence for correct decisions.
category: common
subject: agent
scope: universal
status: experimental
version: 1.0.0
---

# Context loading

## When to use
Use when a task spans many files, skills, references, or tools.

## Workflow
1. Identify the outcome and immediate unknowns.
2. Read instructions, entrypoints, schemas, and tests first.
3. Select the narrowest relevant skill and load only conditional resources.
4. Summarize evidence and expand context only for a concrete unresolved question.

## Decision rules
- Prefer primary artifacts over summaries.
- Do not load an entire category when one skill answers the task.

## Failure modes
If context is insufficient, name the missing artifact or decision instead of guessing.

## Expected output
Maintain a task-focused context map and an explicit list of assumptions.

## Validation
Every loaded resource supports a stated decision, action, or verification.
