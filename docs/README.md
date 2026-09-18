# Documentation

This directory contains the human-facing guides for using and extending the
`SKILLS` repository.

## Guides

- [Architecture](architecture.md) — map the skill library, discovery, integration, and lifecycle layers.
- [Integration](integration.md) — bring selected skills into a project's `.agents/` directory.
- [Versioning](versioning.md) — skill SemVer and repository release tags.
- [Distribution](distribution.md) — Git subtree updates and consumer boundaries.
- [CI and release](ci-release.md) — automated checks and explicit release steps.
- [Authoring](authoring.md) — create or revise a skill using repository conventions.
- [Discovery](discovery.md) — route a task to the smallest relevant skill.
- [Metadata](metadata.md) — define frontmatter fields and generated registry data.
- [Skill index](skill-index.md) — generated human-readable skill registry.
- [Common skill index](../common/README.md) — fast routing for portable skills.
- [Codex common notes](../common/CODEX.md) — Codex-only operating guidance.
- [Personal skills](../personal/README.md) — personal workflow and domain index.
- [Evaluation](evaluation.md) — test whether a skill is useful in practice.
- [Evaluation contract](evaluation-contract.md) — required representative and boundary case format.
- [Evaluation harness](evaluation-harness.md) — deterministic evaluation checks and future extensions.
- [Common evaluation report](common-evaluation-report.md) — current common-skill review results.
- [Compatibility](compatibility.md) — record assumptions about agent runtimes and layouts.
- [Ecosystem matrix](ecosystem-matrix.md) — compare external skill ecosystems.
- [Ecosystem decisions](ecosystem-decisions.md) — record adopted and deferred patterns.

The guides explain repository-level practices. The actual instructions for a
specific capability live in that capability's `SKILL.md`.
