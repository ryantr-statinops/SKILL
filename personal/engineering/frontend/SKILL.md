---
name: frontend
description: Route personal frontend work to lightweight web interface workflows.
category: personal
subject: engineering
scope: personal
status: experimental
version: 1.0.0
invocation: user
---

# Frontend router

Use for small personal web interfaces where user flow, accessibility, and maintainability matter more than framework breadth.

| Need | Skill |
| --- | --- |
| Lightweight web interface | [lightweight-web](lightweight-web/SKILL.md) |

Keep framework-specific implementation details out of the router.

## Agent handoff

- Selected when: Route a task to the narrowest child skill listed by this router.
- Do not activate when: Do not activate when the task is outside this category or no child boundary matches.
- Expected output: Name the selected child skill(s), reason, and any supporting route.
- User-facing report: Summarize the route, excluded children, loaded resources, and validation.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
