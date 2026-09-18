---
name: backend
description: Route personal backend work through service foundations to API, architecture, runtime, and operations workflows.
category: personal
subject: engineering
scope: personal
status: experimental
version: 1.0.0
invocation: user
---

# Backend router

Choose the implementation language only after clarifying service boundaries, interfaces, persistence, and operational needs. Use `core` first when those foundations are not yet explicit, then load API, architecture, and runtime-specific guidance as needed.

| Need | Skill |
| --- | --- |
| Backend foundations | [core](core/SKILL.md) |
| Go backend | [go](go/SKILL.md) |
| Python backend | [python](python/SKILL.md) |
| Node.js backend | [nodejs](nodejs/SKILL.md) |
| API design | [api-design](api-design/SKILL.md) |
| Service architecture | [service-architecture](service-architecture/SKILL.md) |

## Agent handoff

- Selected when: Route a task to the narrowest child skill listed by this router.
- Do not activate when: Do not activate when the task is outside this category or no child boundary matches.
- Expected output: Name the selected child skill(s), reason, and any supporting route.
- User-facing report: Summarize the route, excluded children, loaded resources, and validation.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
