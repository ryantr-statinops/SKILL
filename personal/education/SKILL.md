---
name: education
description: Route personal learning and teaching tasks to statistics, R, or LaTeX workflows.
category: personal
subject: education
scope: personal
status: experimental
version: 1.1.0
---

# Education router

Use this router for foundational learning, explanation, study planning, or mathematical writing. Choose one child skill before loading detailed references.

Statistics is maintained as the independent `personal/statistics` foundation so it can support engineering and quant work as well as education. R and LaTeX remain supporting learning/tooling routes under this category.

| Need | Skill |
| --- | --- |
| R learning or analysis | [r](r/SKILL.md) |
| Mathematical writing | [latex](latex/SKILL.md) |
| Statistical reasoning, probability, inference, regression, or time-series | [statistics](../statistics/SKILL.md) |

Do not use this router to generate a complete textbook or make unsupported academic claims.

## Agent handoff

- Selected when: Route a learning or teaching task to statistics, R, or LaTeX according to the requested outcome.
- Do not activate when: Do not activate when the task is outside this category or no child boundary matches.
- Expected output: Name the selected child skill(s), reason, and any supporting route.
- User-facing report: Summarize the route, excluded children, loaded resources, and validation.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
