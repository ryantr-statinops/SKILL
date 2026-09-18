---
name: trading
description: Route personal trading-related analysis to MT5 integration or execution-risk workflows without placing trades.
category: personal
subject: quant
scope: personal
status: experimental
version: 1.0.0
---

# Trading router

| Need | Skill |
| --- | --- |
| MT5 account or market integration | [mt5](mt5/SKILL.md) |
| Execution and risk controls | [execution](execution/SKILL.md) |

Never infer authorization to place, modify, or cancel an order from a research request.

## Agent handoff

- Selected when: Route a task to the narrowest child skill listed by this router.
- Do not activate when: Do not activate when the task is outside this category or no child boundary matches.
- Expected output: Name the selected child skill(s), reason, and any supporting route.
- User-facing report: Summarize the route, excluded children, loaded resources, and validation.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
