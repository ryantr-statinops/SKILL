# Ecosystem decisions

This document turns the comparison matrix into repository decisions. It does
not claim that every source pattern is universally correct.

## Adopted patterns

- Keep one portable `SKILL.md` as the canonical behavior layer.
- Use compact metadata and an index before loading full skill content.
- Use progressive disclosure for references, scripts, and examples.
- Keep runtime adapters and always-on instructions outside portable skill
  semantics.
- Treat scripts, hooks, plugins, and MCP integrations as executable code that
  needs review and explicit boundaries.
- Record compatibility by runtime, directory layout, version, and
  representative task result.
- Keep skill identity path-based and generate machine-readable registry data.
- Support both explicit invocation and description-based discovery where the
  runtime allows it.

## Rejected or deferred patterns

- Do not require one host-specific plugin manifest for every consumer.
- Do not copy Codex, Claude, Hermes, or plugin commands into portable skills.
- Do not make always-on instruction injection the default for every skill.
- Do not treat a marketplace or hub listing as proof that a skill is safe.
- Do not add a runtime dependency graph until real compatibility cases require
  it.
- Do not couple this repository's canonical source to the OpenAI Skills API or
  any other hosted registry.
- Do not use self-reported benchmark numbers as a substitute for local
  evaluation and consumer-project testing.

## Follow-up proposals

- Add thin adapters only after a runtime fixture is tested.
- Add optional aliases or search terms only when path and description routing
  prove insufficient.
- Add conflict/preference metadata when multiple always-on or behavioral
  skills are introduced.
- Add trust levels and dependency declarations only with a concrete installer
  or execution surface that can enforce them.
