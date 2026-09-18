---
name: quant-research
description: Route quantitative research to alpha investigation or backtesting workflows with explicit bias and cost controls.
category: personal
subject: quant
scope: personal
status: experimental
version: 1.0.0
---

# Quant research router

| Need | Skill |
| --- | --- |
| Hypothesis and signal research | [alpha](alpha/SKILL.md) |
| Historical strategy evaluation | [backtesting](backtesting/SKILL.md) |

Separate research evidence from execution decisions and state all assumptions.

## Agent handoff

- Selected when: Route a task to the narrowest child skill listed by this router.
- Do not activate when: Do not activate when the task is outside this category or no child boundary matches.
- Expected output: Name the selected child skill(s), reason, and any supporting route.
- User-facing report: Summarize the route, excluded children, loaded resources, and validation.
- Confirmation boundary: Ask before destructive, external, or irreversible actions.
