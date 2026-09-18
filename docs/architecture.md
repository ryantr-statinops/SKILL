# SKILLS architecture

`SKILLS` is a portable Agent Skill Library. Its architecture separates
capability content from discovery, integration, and quality lifecycle tooling.

```text
SKILLS/
├── Skill library
│   ├── common/       portable workflows shared across projects
│   ├── personal/     Ryan's workflow and domain judgment
│   └── meta/         authoring, discovery, evaluation, intake, maintenance
│
├── Discovery & integration
│   ├── index          docs/skill-index.md and data/skills.json
│   ├── metadata       frontmatter and docs/metadata.md
│   ├── router         category and subject SKILL.md entrypoints
│   ├── subtree        docs/distribution.md and docs/integration.md
│   └── sync           scripts/sync_skills.py
│
└── Quality & lifecycle
    ├── validation     scripts/validate_skills.py
    ├── evaluation     scripts/run_evaluations.py and evaluation docs
    ├── regression     tests/ and evaluation fixtures
    ├── CI             .github/workflows/validate.yml
    ├── versioning     docs/versioning.md
    └── release        CHANGELOG.md and docs/ci-release.md
```

## Skill library

Every skill is a directory with a required `SKILL.md`. Optional
`references/`, `scripts/`, `examples/`, or `assets/` directories are created
only when the skill has real supporting content. The portable entrypoint keeps
the capability, boundaries, workflow, decisions, failure modes, output, and
validation close together.

- `common/` contains reusable engineering, data, security, delivery, and agent
  workflows.
- `personal/` contains Ryan's workflow preferences and domain foundations.
- `meta/` contains guidance about the skill system itself.

Use `common/README.md`, `personal/README.md`, and `meta/README.md` as curated
category navigation. Use the generated global registry for complete discovery.

## Discovery and integration

The agent should discover the smallest relevant skill before loading full
instructions:

```text
user intent
  → AGENTS.md and applicable runtime guidance
  → optional local.md project state
  → generated index and candidate descriptions
  → router SKILL.md when a category has one
  → selected leaf SKILL.md
  → conditional references/scripts/assets
  → execution, validation, and report
```

`docs/skill-index.md` is human-readable. `data/skills.json` is the machine
registry. `docs/discovery.md` defines selection rules. `docs/integration.md`
defines copy, selected sync, runtime adapters, and Git subtree integration.

## Quality and lifecycle

Quality is layered:

1. Structural metadata, paths, links, and generated files are checked by the
   validator.
2. Representative and boundary cases are checked by the evaluation harness.
3. Regression tests protect the harness and deterministic tooling.
4. GitHub Actions runs the checks on pull requests and pushes to `main`.
5. Skill SemVer and repository release tags describe lifecycle and distribution.

The architecture is intentionally portable. Runtime-specific behavior belongs
in adapters or runtime notes, not in the portable meaning of a common skill.

## Related guides

- Agent operating model will be linked here when the agent protocol guide is
  added.
- [Integration](integration.md)
- [Discovery](discovery.md)
- [Metadata](metadata.md)
- [Evaluation](evaluation.md)
- [Compatibility](compatibility.md)
- [Versioning](versioning.md)
- [CI and release](ci-release.md)
