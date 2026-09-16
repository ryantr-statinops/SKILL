---
name: documentation
description: Create or update technical documentation so users can understand, use, and verify a system or change.
category: common
subject: engineering
scope: universal
status: experimental
version: 1.0.0
---

# Documentation

## When to use
Use when documenting setup, usage, behavior, architecture, APIs, changes, or decisions.

## Workflow
1. Identify the audience, task, and source of truth.
2. Lead with the outcome and provide the shortest useful path.
3. Include prerequisites, examples, limitations, and verification.
4. Link rather than duplicate detailed documentation.
5. Check commands, paths, links, and terminology.

## Decision rules
- Prefer runnable examples and observable claims.
- Document behavior and decisions, not implementation trivia that will drift.

## Failure modes
If behavior is uncertain, mark it as an assumption or verify the source first.

## Expected output
Produce documentation appropriate to its audience with clear next actions.

## Validation
A reader can follow the documented path and reach the stated result.
