# SKILLS

`SKILLS` is a portable Agent Skill Library for engineering, data, AI,
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
SKILLS/
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

The initial implementation focuses on the meta layer and repository guides.

- [Documentation index](docs/README.md)
- [Integration guide](docs/integration.md)
- [Authoring guide](docs/authoring.md)
- [Discovery guide](docs/discovery.md)
- [Metadata specification](docs/metadata.md)
- [Generated skill index](docs/skill-index.md)
- [Common skill index](common/README.md)
- [Codex notes for common skills](common/CODEX.md)
- [Evaluation guide](docs/evaluation.md)
- [Compatibility guide](docs/compatibility.md)

See the folders under `meta/` for the available authoring, discovery,
evaluation, intake, and maintenance skills.

## Roadmap

### Completed foundation

- Repository structure and `common` / `personal` / `meta` taxonomy.
- Canonical skill template and meta skills.
- Structural validator.
- Integration, authoring, discovery, evaluation, and compatibility guides.
- Phase 1 integration model: portable agent directories, Codex priority, Git subtree guidance, and selected-skill sync helper.
- Phase 2 skill metadata, generated Markdown/JSON indexes, and discovery routing.
- Phase 3 common skill foundation, engineering, research, data, security, delivery, and agent skills.
- Common skill representative and boundary evaluation cases.
- Common skill evaluation report and enforced evaluation validation.
- Phase 4 personal taxonomy, routers, workflow, engineering, education, and quant foundations.

### Remaining work

- Verify the `.agent/` integration with a real Codex project fixture and document confirmed runtime behavior.
- Add skill-specific behavioral evaluation cases as the library grows.
- Run the common skill evaluation cases inside a real consumer Codex project when integration testing is resumed.
- Add representative personal tasks and boundary cases as real personal workflows are exercised.
- Add representative and boundary evaluation cases for real skills.
- Define versioning, update, and distribution conventions for integrated skills.
- Add CI to run validation and link checks on every change.
- Research external ecosystems and record adopted compatibility patterns.

## Contributing

Keep changes focused. Validate before committing, use small Conventional
Commits, and explain any new dependency or taxonomy change in the relevant
documentation. See `AGENTS.md` for repository conventions.

### Contribution checklist

- [ ] The skill has a narrow outcome and clear activation boundaries.
- [ ] `SKILL.md` contains only essential instructions.
- [ ] Supporting resources are linked and conditionally loaded.
- [ ] The validator passes.
- [ ] A representative task and a boundary case were reviewed.
- [ ] Commit scope is focused and the message is descriptive.

### Evaluation workflow

For each new or changed skill, record one representative task and one nearby
task that should not activate it. Check routing, procedure, decisions, failure
handling, expected output, and context size. Re-run these cases after changes;
keep the cases close to the skill or in a future evaluation harness when they
become reusable regression tests.

Run the structural check with:

```bash
python3 scripts/validate_skills.py
```
