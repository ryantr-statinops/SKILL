# Skill distribution

The preferred consumer integration is Git subtree. It vendors a reviewed copy
of the library into a project while keeping the consumer usable when the
source repository is unavailable.

## Continuous updates

Use the `main` branch when the consumer wants deliberate updates from the
latest repository state:

```bash
git fetch skills main
git subtree pull --prefix=.agent/skills skills main --squash
```

Review the diff, run the source checks, and test a representative consumer task
before accepting the update.

## Reproducible updates

Use a reviewed commit or release tag when a consumer needs a reproducible
snapshot. Record the source commit/tag in the consumer's integration notes.
Do not silently update a production project to a moving branch.

## Consumer boundaries

- Keep project-specific instructions outside the subtree.
- Preserve `.agent/skills/` and relative resource paths.
- Do not edit vendored files as local overrides; change the source repository
  and pull a new reviewed snapshot instead.
- Keep secrets, private data, and project-only procedures outside the public
  library.
- Use `scripts/sync_skills.py` when a project needs a selected export instead
  of the complete library.

## Contributing back

Use subtree push only when the consumer intentionally contributes a portable
change back to SKILLS. Project-specific changes must remain in the consumer
repository. Review conflicts manually, especially for `SKILL.md`, references,
scripts, and evaluation files.
