# Agent skill ecosystem matrix

This matrix records the Phase 8 research baseline for portable skills. The
observations are separated from recommendations: a source may demonstrate a
pattern without making that pattern appropriate for this repository.

## Comparison

| Ecosystem | Discovery and loading | Portable unit | Runtime adapter | Lifecycle/distribution | Security/compatibility observation |
| --- | --- | --- | --- | --- | --- |
| [OpenAI/Codex](https://openai.com/index/introducing-the-codex-app/) | Codex uses repository guidance such as `AGENTS.md`; OpenAI also exposes a Skills API with list/get/content and version operations. | Repository instruction files and skill directories; exact local runtime conventions are separate from the API resource model. | Codex/project guidance, plugins, and MCP integrations. | The Skills API exposes explicit skill versions; this is an API product surface, not a reason to couple this filesystem library to that API. | Keep portable Markdown separate from Codex notes; treat uploaded or executable resources as reviewed code. |
| [Anthropic Skills](https://www.anthropic.com/research/skills) | Skills are loaded for relevant tasks rather than copied into every prompt. | Skill package with instructions and optional supporting resources. | Claude product/runtime conventions and tool integrations. | Skills can be customized and shared; exact consumer packaging is runtime-specific. | Preserve least privilege and keep tool/resource assumptions explicit. |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/guides/work-with-skills.md) | Compact skill listing/search precedes `skill_view`; full content and individual references are loaded on demand. | `SKILL.md` directory with optional reference files; bundled and user-local locations are supported. | Hermes commands/tools and optional skill hub. | Supports bundled, optional, local, and installable skills. | Progressive disclosure is a strong fit; Hermes-specific commands must stay out of portable core. |
| [Ponytail](https://github.com/DietrichGebert/ponytail/blob/main/docs/agent-portability.md) | Shared `skills/` content plus host-specific plugin, hook, rule, or instruction adapters. | Portable `SKILL.md` plus thin runtime adapters. | Claude, Codex, OpenCode, Gemini CLI, Cursor, Copilot, Hermes, and others. | Plugin installs, copied rules, and repository integrations coexist. | Adapter matrix and host caveats are explicit; hooks increase power and review surface. |
| [Caveman](https://github.com/JuliusBrussee/caveman) | Usually activated through a skill or host instruction file; often paired with Ponytail. | Compact behavioral skill/instruction layer. | Host-specific instruction/plugin integrations. | Commonly distributed through skill repositories or composed plugins. | Behavioral layers can conflict; composition needs explicit precedence and conflict handling. |
| [PonytailCaveman](https://github.com/iharshgandhi/PonytailCaveman) | Repo-level `AGENTS.md` plus `.agents/skills/ponytail-caveman/SKILL.md`; explicit invocation is supported. | Combined reusable skill with always-on repo guidance. | Codex, Copilot, and other adapters. | Portable core is paired with copied or host-specific files. | Demonstrates how a compact always-on layer and reusable skill can coexist; attribution and source boundaries matter. |

## Interpretation

- **Fact:** The cited projects use different host discovery paths and do not
  share one universal runtime contract.
- **Inference:** A portable library should keep its canonical skill payload
  independent from adapters, hooks, plugins, and always-on instructions.
- **Proposal for SKILLS:** Continue using path-based IDs, generated registry
  metadata, progressive disclosure, and explicit runtime notes.
- **Verified integration:** The `.agents/skills/` adapter is tested with Codex's
  repository layout and OpenCode 1.18.31's `debug skill --pure` discovery. This
  confirms loading and paths; it does not establish model quality.

## Research limitations

This is a compatibility-oriented research snapshot, not a benchmark of agent
quality. Runtime behavior changes over time; confirmed support must still be
tested with a representative consumer fixture and recorded in
`docs/compatibility.md`.
