---
name: service-architecture
description: Shape personal backend service architecture around ownership, boundaries, data flow, operability, and change cost.
category: personal
subject: backend
scope: personal
status: experimental
version: 1.0.0
---

# Service architecture

## When to use
Use when deciding service boundaries, modularity, communication, or deployment shape.

## Personal principles
Prefer a modular simple service before splitting into independently operated services.

## Workflow
Map domain boundaries and data flow, identify failure/ownership boundaries, compare deployment options, and define migration triggers.

## Decision rules
Do not create a distributed boundary without independent scaling, ownership, or failure justification.

## Constraints
Include observability, local development, deployment, and debugging cost.

## Failure modes
If service ownership or data consistency is unclear, keep the boundary provisional.

## Expected output
Provide architecture, trade-offs, failure modes, and evolution path.

## Validation
The design has a runnable local path and explicit operational responsibilities.
