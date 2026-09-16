---
name: security-review
description: Review a change or system for concrete threats involving authentication, authorization, data, injection, dependencies, and access.
category: common
subject: security
scope: universal
status: experimental
version: 1.0.0
---

# Security review

## When to use
Use when explicitly requested or when a change materially expands a security boundary.

## Workflow
1. Map assets, actors, trust boundaries, and attack surface.
2. Inspect authentication, authorization, input handling, output handling, secrets, and dependencies.
3. Evaluate abuse cases and failure behavior.
4. Rank findings by impact and likelihood, with evidence and remediation.

## Decision rules
- Prioritize exploitable, concrete findings over generic best-practice lists.
- Do not claim a system is secure; state review scope and residual risk.

## Failure modes
If source, deployment, or threat context is missing, limit conclusions explicitly.

## Expected output
Return prioritized findings, evidence, impact, remediation, and limitations.

## Validation
Findings are reproducible or supported by a clear threat argument.
