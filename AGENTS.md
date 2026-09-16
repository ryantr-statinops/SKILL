# Repository Guidance

## Purpose

`SKILLS` is a portable library of agent skills: concise operational knowledge,
procedures, and judgment for engineering, data, AI, quantitative, and personal
workflows.

## Working rules

- Inspect the repository state before changing files.
- Keep each skill narrowly scoped and explicit about activation boundaries.
- Put essential routing and procedure in `SKILL.md`; defer deep context to linked references.
- Use scripts only when deterministic execution materially improves reliability.
- Do not create empty resource directories or copy generic documentation.
- Validate skills and links before committing.
- Avoid destructive Git commands and preserve unrelated user changes.

## Repository taxonomy

- `common/`: broadly reusable skills.
- `personal/`: Ryan's workflow, preferences, and domain-specific practices.
- `meta/`: skills about authoring, discovering, evaluating, and maintaining skills.

## Change discipline

Use focused commits with imperative Conventional Commit messages. Run the
relevant validation and `git diff --check` before committing.
