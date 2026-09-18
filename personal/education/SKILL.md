---
name: education
description: Route personal learning and teaching tasks to foundational R, LaTeX, statistics, probability, or stochastic-process workflows.
category: personal
subject: education
scope: personal
status: experimental
version: 1.0.0
---

# Education router

Use this router for foundational learning, explanation, study planning, or mathematical writing. Choose one child skill before loading detailed references.

| Need | Skill |
| --- | --- |
| R learning or analysis | [r](r/SKILL.md) |
| Mathematical writing | [latex](latex/SKILL.md) |
| Statistical reasoning | [statistics](statistics/SKILL.md) |
| Probability foundations | [probability](probability/SKILL.md) |
| Stochastic processes | [stochastic-processes](stochastic-processes/SKILL.md) |

Do not use this router to generate a complete textbook or make unsupported academic claims.

## Agent handoff

- Selected when: Route a task to the narrowest child skill listed by this router.
- Do not activate when: Do not activate when the task is outside this category or no child boundary matches.
- Expected output: Name the selected child skill(s), reason, and any supporting route.
- User-facing report: Summarize the route, excluded children, loaded resources, and validation.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
