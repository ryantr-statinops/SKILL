# Compatibility

`SKILLS` stores skills as plain Markdown plus optional local resources. This
makes the library portable, but each agent runtime may differ in discovery,
directory conventions, symlink support, and script execution.

## Baseline assumptions

- A skill is a directory containing `SKILL.md`.
- The runtime can read Markdown and follow relative links.
- Optional resources remain next to the skill entrypoint.
- Project-specific instructions live in the project's `.agents/AGENTS.md`.
- Scripts are not trusted automatically; review them before execution.

## Integration compatibility

When integrating into another runtime, verify:

1. Which directory the runtime scans for agent instructions and skills.
2. Whether the runtime recognizes `SKILL.md` and YAML frontmatter.
3. Whether nested `references/`, `scripts/`, `examples/`, and `assets/` paths are accessible.
4. Whether scripts need a particular interpreter or dependency.
5. How project instructions and skill instructions are prioritized.

Do not claim runtime support until a representative task has been tested in
that runtime.

## Portability rules

- Prefer relative links and standard Markdown.
- Avoid runtime-specific metadata unless documented as optional.
- Keep executable helpers self-contained and state their prerequisites.
- Separate portable procedure from personal or runtime-specific integration.

Record confirmed runtime behavior here as evidence accumulates. Keep uncertain
assumptions explicit instead of presenting them as a universal standard.
