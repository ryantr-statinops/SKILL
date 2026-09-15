# SKILL

`SKILL` is a portable Agent Skill Library for engineering, data, AI,
quantitative research, and personal workflows.

This repository is not a prompt dump. A skill encodes operational knowledge:
when to act, how to act, which decisions matter, and how to validate the result.

## Mental model

| Component | Role |
| --- | --- |
| Model | Reasoning engine |
| Agent | Orchestration |
| Skill | Knowledge, procedure, and judgment |
| Workflow | A concrete execution sequence |
| Tool / MCP | Capability or interface exposed to the agent |
| Memory | Persistent context |
| Reference | Deeper knowledge loaded when needed |
| Script | Deterministic execution |
| Evaluation | Evidence that a skill works |

Skills can guide an agent's use of tools and MCPs, but neither contains the
other conceptually.

## Architecture

```text
SKILL/
├── common/       # broadly reusable skills
├── personal/     # Ryan's workflows and domain judgment
├── meta/         # skills about the skill system
├── README.md     # map and guide
├── AGENTS.md     # repository working conventions
└── LICENSE
```

Each skill is a folder with a required `SKILL.md` and optional resources:

```text
<skill>/
├── SKILL.md
├── references/   # deep, conditional knowledge
├── scripts/      # deterministic helpers
├── examples/     # demonstrations and fixtures
└── assets/       # reusable output templates or artifacts
```

Do not create empty resource folders. Keep the entrypoint small and disclose
detail progressively.

## Discovery model

```text
user task
  → repository/category index
  → skill description and boundaries
  → SKILL.md
  → only relevant references/scripts/assets
  → execution
  → validation and output
```

The agent should reject a skill when the task is outside its activation
conditions. Overlapping skills should be resolved by scope, specificity, and
explicit exclusions rather than by loading everything.

## Taxonomy

- `common/` contains practices that should transfer between users and repos.
- `personal/` contains preferences, conventions, and domain workflows that
  reflect Ryan's actual way of working.
- `meta/` contains authoring, discovery, evaluation, intake, and maintenance
  guidance for this library itself.

See `meta/skill-authoring/SKILL.md` and `meta/skill-intake/SKILL.md` before
adding a skill.

## Creating a skill

1. Start from the canonical structure in `meta/skill-authoring/`.
2. Define a narrow capability and explicit `when to use` / `when not to use`.
3. Put only essential instructions in `SKILL.md`.
4. Move conditional depth into linked references.
5. Add scripts only for repeatable deterministic operations.
6. Add examples or evaluation cases when they improve confidence.
7. Run the repository validator and review the skill against a real task.

## Quality bar

A useful skill has bounded scope, discriminating activation conditions,
actionable procedure, decision rules, failure handling, progressive disclosure,
and observable validation. Avoid generic textbook material, giant prompts,
duplicated documentation, vague triggers, unnecessary abstractions, and skills
that attempt to solve an entire domain.

## Current index

The initial implementation focuses on the meta layer. See the folders under
`meta/` for the available authoring, discovery, evaluation, intake, and
maintenance guidance.

## Contributing

Keep changes focused. Validate before committing, use small Conventional
Commits, and explain any new dependency or taxonomy change in the relevant
documentation. See `AGENTS.md` for repository conventions.
