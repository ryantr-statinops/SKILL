# Skill evaluation

Evaluation checks whether a skill improves agent behavior on realistic tasks,
not merely whether its Markdown looks complete.

## Minimum evaluation set

For every new or changed skill, define:

1. A representative task that should activate the skill.
2. A nearby boundary task that should not activate it.
3. Expected behavior and observable output.
4. Failure conditions and safe handling.
5. The validation command or review criteria.

## Evaluation levels

### Structural

Run:

```bash
python3 scripts/validate_skills.py
```

This checks names, frontmatter, placeholders, resource directories, and local
Markdown links.

### Behavioral

Run the representative task with the skill available. Confirm that the agent
uses the intended procedure, loads only relevant resources, handles failure
conditions, and produces the expected result.

### Boundary

Run the nearby task that should not activate the skill. Confirm that the skill's
description and exclusions prevent misrouting.

## Regression practice

Keep useful evaluation cases when a skill is revised. A change to activation,
scope, procedure, or expected output should trigger the representative and
boundary checks again.

Fix the narrowest demonstrated problem. Do not add broad rules based on a
single speculative failure.

## Common skill evaluation

Each common skill keeps its representative and boundary scenarios in
`examples/evaluation.md`. These scenarios test routing intent and expected
behavior; they are not a substitute for running the task in a real project.

For Codex, additionally verify that:

- `common/README.md` routes the task to the intended skill.
- `common/CODEX.md` is read as runtime guidance without leaking into portable skill semantics.
- The selected `SKILL.md` is loaded before conditional resources.
- The portable procedure still makes sense outside Codex.
