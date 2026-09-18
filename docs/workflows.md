# Workflow skills

Workflow skills orchestrate narrow primitive skills around one user outcome.
They are user-invoked entry points with `scope: universal` and
`invocation: user`.

## Required contract

Every workflow skill defines:

- activation and exclusion conditions;
- the primitive skills it reads or recommends;
- decision points and optional branches;
- expected artifacts;
- confirmation boundaries before side effects;
- failure and recovery behavior;
- terminal validation;
- an agent handoff section.

Workflow skills may direct the agent to read a `both` skill. They must not
silently delegate to another user-invoked workflow. A workflow is an
orchestration layer, not a replacement for the domain skills it composes.

## Context and artifacts

Before starting, a workflow reads `CONTEXT.md` when the consumer project has
one. Artifact paths come from its work-artifact section. When paths are absent,
the workflow uses this default root:

```text
docs/agent/
├── specs/
├── diagnostics/
├── decisions/
├── reports/
└── handoffs/
```

The workflow should present the intended artifact path before writing a new
document when the project has not already authorized that output.

## Supported workflows

- `feature-delivery`: align, plan, implement in vertical slices, test, review,
  and hand off a feature.
- `bug-fixing`: reproduce, minimize, hypothesize, fix, regression-test, review,
  and hand off a bug fix.
- `research-decision`: define a decision, gather high-trust evidence, compare
  alternatives, and record uncertainty.
- `data-analysis`: inspect, contract, clean, validate, analyze reproducibly,
  and report limitations.

Each workflow keeps its entrypoint concise and links to shared artifact
templates instead of duplicating long formats.
