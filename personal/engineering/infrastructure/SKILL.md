---
name: infrastructure
description: Route personal infrastructure work to Linux, Docker, or networking workflows.
category: personal
subject: engineering
scope: personal
status: experimental
version: 1.0.0
---

# Infrastructure router

| Need | Skill |
| --- | --- |
| Host and shell operations | [linux](linux/SKILL.md) |
| Containers and images | [docker](docker/SKILL.md) |
| Connectivity and services | [networking](networking/SKILL.md) |

Inspect the current environment before changing infrastructure.

## Agent handoff

- Selected when: Route a task to the narrowest child skill listed by this router.
- Do not activate when: Do not activate when the task is outside this category or no child boundary matches.
- Expected output: Name the selected child skill(s), reason, and any supporting route.
- User-facing report: Summarize the route, excluded children, loaded resources, and validation.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
