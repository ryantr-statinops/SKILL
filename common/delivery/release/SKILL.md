---
name: release
description: Prepare a software release by checking versioning, tests, artifacts, changes, migrations, and release readiness.
category: common
subject: delivery
scope: universal
status: experimental
version: 1.0.0
---

# Release

## When to use
Use when preparing a versioned release or release candidate.

## Workflow
1. Inspect release policy, current version, and unreleased changes.
2. Run required tests, lint, build, packaging, and migration checks.
3. Verify changelog, artifacts, compatibility, and rollback information.
4. Report readiness and blockers; publish only with authorization.

## Decision rules
- Never publish with failing required checks or an unresolved version conflict.
- Prefer a release candidate when risk or migration impact is material.

## Failure modes
If release policy or artifact provenance is unclear, stop before publishing.

## Expected output
Return release checklist, artifacts, checks, blockers, and rollback notes.

## Validation
The release can be reproduced, inspected, and rolled back according to project policy.
