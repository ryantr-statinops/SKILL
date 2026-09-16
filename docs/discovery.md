# Skill discovery

Skill discovery is the process of selecting the smallest relevant skill for a
user task without loading the whole library into context.

## Routing sequence

```text
task
  → desired outcome and constraints
  → category and candidate descriptions
  → activation boundaries
  → selected SKILL.md
  → conditional references/scripts/assets
  → execution and validation
```

## Selection rules

1. Match the desired outcome, not only a technology keyword.
2. Prefer the most specific skill whose description covers the task.
3. Reject skills whose `when not to use` boundary applies.
4. Combine skills only when their responsibilities are distinct.
5. If no skill clearly applies, continue without forcing an unrelated skill.

## Writing discoverable descriptions

A description should say what the skill does and when it applies. It should be
specific enough to distinguish nearby skills and should include an exclusion
when misrouting is likely.

Prefer:

```yaml
description: Debug Python package installation and metadata problems; not for general Python application development.
```

Avoid:

```yaml
description: Python development helper.
```

## Overlap and conflicts

Resolve overlap through narrower scope, explicit exclusions, and clear expected
outputs. If two skills give conflicting procedures, stop and surface the
conflict rather than silently merging them.
