# Codex Notes for Common Skills

These notes apply only when common skills are used through Codex. They are
runtime guidance, not portable skill instructions.

## Before starting

1. Inspect `git status`, current branch, and recent commits.
2. Read the repository-level `AGENTS.md` if present.
3. Check `.agent/`, `.agents/`, `.codex/`, or other configured runtime directories.
4. Preserve unrelated uncommitted changes.

## Loading

- Use `common/README.md` for quick routing.
- Read only the selected skill's `SKILL.md`.
- Load references, scripts, examples, and assets only when the selected workflow needs them.
- Use the global `docs/skill-index.md` or `data/skills.json` for broader search.

## Safe execution

- Inspect before modifying.
- Keep changes within the user's requested scope.
- Avoid destructive commands unless explicitly authorized.
- Run the repository's validator and relevant tests before reporting completion.
- Keep diffs and commits focused.

## Portability warning

Do not copy these Codex assumptions into portable common `SKILL.md` files as
universal rules. Runtime adapters may use different directories, tools, or
instruction precedence.
