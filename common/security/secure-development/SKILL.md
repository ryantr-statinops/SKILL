---
name: secure-development
description: Apply baseline secure-development practices for secrets, inputs, outputs, logging, dependencies, and access boundaries.
category: common
subject: security
scope: universal
status: experimental
version: 1.0.0
---

# Secure development

## When to use
Use while designing or changing code that handles input, secrets, identity, files, network calls, or sensitive data.

## Workflow
1. Identify trust boundaries and sensitive values.
2. Validate inputs and constrain outputs at boundaries.
3. Keep secrets out of source, logs, and artifacts.
4. Minimize permissions and inspect dependency risk.
5. Add security-focused tests for the relevant abuse cases.

## Decision rules
- Fail closed when validation or authorization is uncertain.
- Do not disable a security control as a shortcut.

## Failure modes
If risk cannot be bounded, stop and request a security review rather than guessing.

## Expected output
Describe protections, assumptions, residual risk, and verification.

## Validation
Sensitive paths have tests or review evidence covering misuse and failure behavior.
