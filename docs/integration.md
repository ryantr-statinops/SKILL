# Skill integration

This guide explains how to expose selected skills from `SKILLS` to another
project through a runtime-specific agent directory. Codex is the priority
runtime; the integration remains portable by using the same skill payload under
`.agent/`, `.claude/`, `.codex/`, or another documented adapter directory.

## Recommended project layout

```text
my-project/
├── .agent/
│   ├── AGENTS.md
│   └── skills/
│       ├── common/
│       └── personal/
└── src/
```

Keep project-specific instructions in `.agent/AGENTS.md`. Put reusable skills
under `.agent/skills/` and preserve each skill's complete folder when it has
references, scripts, examples, or assets.

For a runtime that requires a different directory, keep the same internal
layout and document the adapter, for example `.claude/skills/` or
`.codex/skills/`.

## Integration options

### Copy selected skills

Copy only the skills needed by the project. This is the simplest and most
portable option, but updates must be synchronized manually.

### Symlink during development

Use a symlink when actively developing a skill and the local agent runtime
supports symlinks. Do not rely on this for a portable repository or packaged
project.

### Git subtree (recommended)

Use a Git subtree when a project should vendor skills into its own history
without requiring a second checkout. The project can pull updates from
`SKILLS`, review them normally, and keep working even if the source repository
is temporarily unavailable.

#### Add the subtree

Run these commands from the target project root:

```bash
git remote add skills https://github.com/ryantr-statinops/SKILLS.git
git fetch skills main
git subtree add --prefix=.agent/skills skills main --squash
```

The initial command imports the complete library. If the project only wants a
small subset, use the sync helper described below to stage selected paths
before committing, or maintain a dedicated export branch in the source repo.

#### Pull updates

```bash
git fetch skills main
git subtree pull --prefix=.agent/skills skills main --squash
```

Review the resulting diff, run the source validator where available, and test
one representative project task before accepting the merge.

#### Push project-local changes back

Only push changes back when the project is intentionally contributing to the
central library. Keep project-specific instructions outside the subtree.

```bash
git subtree push --prefix=.agent/skills skills main
```

Do not use subtree push for local overrides that should remain private to the
project.

#### Subtree rules

- Keep the subtree prefix stable once chosen.
- Do not edit vendored files casually; prefer changes in `SKILLS` followed by a pull.
- Review conflicts manually, especially `SKILL.md`, references, and scripts.
- Record the source repository and update command in the target project's documentation.
- Use `--squash` for ordinary consumer projects unless preserving source history is required.

## Integration rules

- Integrate the smallest useful set of skills; do not copy the whole library by default.
- Use `.agent/` as the portable baseline and add runtime-specific adapters only when verified.
- Preserve the skill directory structure and relative resource links.
- Do not rewrite `SKILL.md` merely to fit a project unless the project-specific behavior belongs in `.agents/AGENTS.md`.
- Treat project instructions as additional context, not as permission to weaken a skill's safety constraints.
- Review scripts and assets before enabling a skill from an untrusted source.

## Updating

After updating an integrated skill, run the source repository validator and a
representative project task. For subtrees, fetch and pull deliberately, review
the diff, and record the resulting source commit when practical. The helper
`python3 scripts/sync_skills.py` can validate a selected export before it is
committed to the target project.

## Validation checklist

- The target runtime discovers the selected agent directory.
- Every integrated skill has a readable `SKILL.md`.
- Relative references, scripts, examples, and assets still resolve.
- Project instructions do not conflict with skill boundaries.
- A representative task and a nearby non-activation task behave as expected.
