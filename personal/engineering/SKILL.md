---
name: engineering
description: Route personal engineering work through shared foundations to data, AI, backend, infrastructure, or lightweight frontend workflows.
category: personal
subject: engineering
scope: personal
status: experimental
version: 1.0.0
---

# Engineering router

Use for engineering decisions that should reflect Ryan's preferences. Start with `core` when the task involves shared computational or systems reasoning, then route to the narrowest domain or implementation skill.

| Need | Skill |
| --- | --- |
| Algorithms, optimization, or systems foundations | [core](core/SKILL.md) |
| Go, Python, or Node.js backend | [backend](backend/SKILL.md) |
| Data pipelines or storage | [data-engineering](data-engineering/SKILL.md) |
| AI and agent engineering | [ai](ai/SKILL.md) |
| Linux, Docker, or networking | [infrastructure](infrastructure/SKILL.md) |
| Lightweight web UI | [frontend](frontend/SKILL.md) |

Keep generic engineering guidance in `common/` and personal preferences here.

## Agent handoff

- Selected when: Route a task to the narrowest child skill listed by this router.
- Do not activate when: Do not activate when the task is outside this category or no child boundary matches.
- Expected output: Name the selected child skill(s), reason, and any supporting route.
- User-facing report: Summarize the route, excluded children, loaded resources, and validation.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
