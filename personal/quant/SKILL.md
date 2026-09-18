---
name: quant
description: Route foundational quantitative work to research, trading, or time-series workflows without authorizing financial execution.
category: personal
subject: quant
scope: personal
status: experimental
version: 1.0.0
---

# Quant router

| Need | Skill |
| --- | --- |
| Alpha or backtesting research | [quant-research](quant-research/SKILL.md) |
| MT5 or execution concerns | [trading](trading/SKILL.md) |
| Time-series foundations | [time-series](time-series/SKILL.md) |

This category is research guidance, not financial advice or trade authorization.

## Agent handoff

- Selected when: Route a task to the narrowest child skill listed by this router.
- Do not activate when: Do not activate when the task is outside this category or no child boundary matches.
- Expected output: Name the selected child skill(s), reason, and any supporting route.
- User-facing report: Summarize the route, excluded children, loaded resources, and validation.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
