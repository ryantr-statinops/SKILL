---
name: quant
description: Route personal quantitative work to research or production-engineering workflows without authorizing financial execution.
category: personal
subject: quant
scope: personal
status: experimental
version: 1.0.0
---

# Quant router

| Need | Skill |
| --- | --- |
| Alpha, backtesting, or model evaluation research | [quant-research](quant-research/SKILL.md) |
| Time-series foundations | [statistics](../statistics/SKILL.md) |

This category is engineering and research guidance, not financial advice or trade authorization. Production workflow guidance must stop at system design, monitoring, and human approval boundaries.

## Agent handoff

- Selected when: Route a task to the narrowest child skill listed by this router.
- Do not activate when: Do not activate when the task is outside this category or no child boundary matches.
- Expected output: Name the selected child skill(s), reason, and any supporting route.
- User-facing report: Summarize the route, excluded children, loaded resources, and validation.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
