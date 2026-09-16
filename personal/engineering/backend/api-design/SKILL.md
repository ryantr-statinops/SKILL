---
name: api-design
description: Design personal service APIs with explicit contracts, validation, errors, compatibility, and usable client behavior.
category: personal
subject: backend
scope: personal
status: experimental
version: 1.0.0
---

# API design

## When to use
Use when creating or changing an HTTP, RPC, event, or internal service contract.

## Personal principles
Prefer boring explicit contracts and predictable errors over clever interfaces.

## Workflow
Define consumers and operations, model inputs/outputs/errors, set compatibility rules, document examples, and test boundary cases.

## Decision rules
Design for the actual consumer and lifecycle; do not expose internal storage accidentally.

## Constraints
Validate input, minimize sensitive output, and document breaking changes.

## Failure modes
If consumer expectations are unknown, clarify them before freezing the contract.

## Expected output
Provide contract, examples, errors, compatibility policy, and tests.

## Validation
Representative and invalid requests produce documented behavior.
