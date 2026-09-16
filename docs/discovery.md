# Skill discovery

Skill discovery is the process of selecting the smallest relevant skill for a
user task without loading the whole library into context.

## Routing sequence

```text
task
  → docs/skill-index.md or data/skills.json
  → candidate descriptions and metadata
  → activation boundaries
  → selected SKILL.md
  → conditional references/scripts/assets
  → execution and validation
```

For common skills, begin with [`common/README.md`](../common/README.md) for
quick routing. Codex should also read [`common/CODEX.md`](../common/CODEX.md);
other runtimes should use only the portable skill entrypoint.

The generated index is a routing aid, not a replacement for the skill
entrypoint. After selecting a candidate, read its `SKILL.md` before following
instructions or loading supporting resources.

## Querying the index

Use `docs/skill-index.md` for human review and `data/skills.json` for tooling.
Regenerate both after changing skill metadata:

```bash
python3 scripts/generate_skill_index.py
python3 scripts/generate_skill_index.py --check
```

## Selection rules

1. Match the desired outcome, not only a technology keyword.
2. Prefer the most specific skill whose description covers the task.
3. Reject skills whose `when not to use` boundary applies.
4. Combine skills only when their responsibilities are distinct.
5. If no skill clearly applies, continue without forcing an unrelated skill.

## Writing discoverable descriptions

A description should say what the skill does and when it applies. Metadata also
provides category, subject, scope, lifecycle status, and version. The
description should be specific enough to distinguish nearby skills and should
include an exclusion when misrouting is likely.

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
