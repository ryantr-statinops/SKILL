# Skill integration

This guide explains how to expose selected skills from `SKILLS` to another
project through its `.agents/` directory.

## Recommended project layout

```text
my-project/
├── .agents/
│   ├── AGENTS.md
│   └── skills/
│       ├── git-workflow/
│       │   └── SKILL.md
│       └── debugging/
│           └── SKILL.md
└── src/
```

Keep project-specific instructions in `.agents/AGENTS.md`. Put reusable skills
under `.agents/skills/` and preserve each skill's complete folder when it has
references, scripts, examples, or assets.

## Integration options

### Copy selected skills

Copy only the skills needed by the project. This is the simplest and most
portable option, but updates must be synchronized manually.

### Symlink during development

Use a symlink when actively developing a skill and the local agent runtime
supports symlinks. Do not rely on this for a portable repository or packaged
project.

### Submodule or subtree

Use a Git submodule or subtree when a project needs a tracked relationship to a
specific revision of the central library. Document the chosen revision and
update procedure in the project.

## Integration rules

- Integrate the smallest useful set of skills; do not copy the whole library by default.
- Preserve the skill directory structure and relative resource links.
- Do not rewrite `SKILL.md` merely to fit a project unless the project-specific behavior belongs in `.agents/AGENTS.md`.
- Treat project instructions as additional context, not as permission to weaken a skill's safety constraints.
- Review scripts and assets before enabling a skill from an untrusted source.

## Updating

After updating an integrated skill, run the source repository validator and a
representative project task. For copied skills, record the source commit when
practical. For submodules or subtrees, update deliberately and review the diff.

## Validation checklist

- The agent runtime discovers the `.agents/` location.
- Every integrated skill has a readable `SKILL.md`.
- Relative references, scripts, examples, and assets still resolve.
- Project instructions do not conflict with skill boundaries.
- A representative task and a nearby non-activation task behave as expected.
