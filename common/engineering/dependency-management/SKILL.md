---
name: dependency-management
description: Safely inspect, add, update, or remove software dependencies while considering compatibility, security, and reproducibility.
category: common
subject: engineering
scope: universal
status: experimental
version: 1.0.0
---

# Dependency management

## When to use
Use when changing package dependencies, lockfiles, runtime versions, or build inputs.

## Workflow
1. Inspect manifests, lockfiles, supported runtimes, and current usage.
2. Define why the dependency change is needed.
3. Check compatibility, license, security, transitive impact, and maintenance.
4. Make the smallest update and regenerate lock data with the project tool.
5. Run tests and build checks.

## Decision rules
- Prefer existing dependencies when they already solve the need.
- Keep lockfiles synchronized and never silently upgrade unrelated packages.

## Failure modes
If a version cannot satisfy constraints, report the conflict and alternatives.

## Expected output
Report dependency rationale, version impact, checks, and residual risk.

## Validation
Manifest and lockfile agree, installation is reproducible, and relevant checks pass.
