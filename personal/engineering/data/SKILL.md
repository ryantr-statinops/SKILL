---
name: data
description: Route personal data engineering work to core, pipeline, database, or orchestration workflows.
category: personal
subject: engineering
scope: personal
status: experimental
version: 1.0.0
---

# Data engineering router

| Need | Skill |
| --- | --- |
| Ingestion and transformation | [pipelines](pipelines/SKILL.md) |
| Storage and query design | [databases](databases/SKILL.md) |
| Scheduling and operations | [orchestration](orchestration/SKILL.md) |
| Data engineering foundations | [core](core/SKILL.md) |

Prefer the smallest reliable local design before introducing distributed infrastructure.

## Agent handoff

- Selected when: Route a task to the narrowest child skill listed by this router.
- Do not activate when: Do not activate when the task is outside this category or no child boundary matches.
- Expected output: Name the selected child skill(s), reason, and any supporting route.
- User-facing report: Summarize the route, excluded children, loaded resources, and validation.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
