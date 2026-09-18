# SKILLS

`SKILLS` is a portable Agent Skill Library for engineering, data, AI,
quantitative research, and personal workflows.

**Current release: `v0.1.0`**

## What SKILLS provides

Skills encode operational knowledge: when to act, how to act, which decisions
matter, and how to validate the result. Workflows provide outcome-oriented
entry points, while bundles provide reviewed capability sets for consumer
projects.

Portable Markdown is the source of truth. The `.agent/skills/` directory is the
runtime-independent baseline for Codex-compatible agents and other runtimes
with thin adapters.

## Start here

From a checkout of this repository, preview the portable baseline before
installing it into a consumer project:

```bash
python3 scripts/sync_skills.py \
  --bundle portable-agent-baseline \
  --check \
  /path/to/project/.agent/skills

python3 scripts/sync_skills.py \
  --bundle portable-agent-baseline \
  /path/to/project/.agent/skills
```

Check mode does not write files. A normal sync preserves the repository-relative
skill layout and stops before overwriting an existing target path.

Copy [`templates/CONTEXT.md`](templates/CONTEXT.md) into the consumer project
when the agent needs shared vocabulary, architecture boundaries, test seams, or
artifact paths. Record the source tag `v0.1.0` or a reviewed commit in the
consumer project's integration notes.

## Choose by outcome

| Outcome | Bundle | Purpose |
| --- | --- | --- |
| Agent context and recovery | `portable-agent-baseline` | Establish portable context, onboarding, requirements, recovery, and discovery. |
| General engineering | `engineering-core` | Support repository work, implementation, testing, review, and handoff. |
| Build a feature | `feature-delivery` | Coordinate requirements, planning, vertical slices, testing, review, and handoff. |
| Fix a defect | `bug-fixing` | Reproduce, isolate, fix, regression-test, review, and hand off a defect. |
| Make a research decision | `research-decision` | Compare alternatives with evidence, trade-offs, and uncertainty. |
| Analyze data | `data-analysis` | Inspect, clean, validate, analyze, and report data reproducibly. |
| Python backend workflow | `personal-python` | Apply Ryan's Python backend, API, testing, debugging, and review practices. |

List available bundles with:

```bash
python3 scripts/sync_skills.py --list-bundles
```

See [bundle documentation](docs/bundles.md) for the registry contract and
distribution behavior.

## Supported status

- **Promoted/stable** — the supported set recorded in
  [`data/promoted.json`](data/promoted.json); each skill is documented,
  evaluated, and included in a supported bundle.
- **Experimental** — usable skills that are still collecting evidence and
  feedback from real workflows.
- **Personal** — Ryan-specific preferences, conventions, and domain workflows.
- **Deprecated** — excluded from new bundles and workflows unless explicitly
  requested through a reviewed compatibility path.

The promoted set is intentionally smaller than the full library. See the
[promotion policy](docs/promotion.md) for lifecycle and distribution rules.

## How an agent uses SKILLS

```text
user outcome
  → discover a bundle or skill
  → inspect project context
  → load SKILL.md
  → execute the workflow
  → validate and hand off
```

For integration and runtime layout, read the [integration guide](docs/integration.md).
For routing, read the [discovery guide](docs/discovery.md). For coordinated
outcomes, read the [workflow guide](docs/workflows.md). For consumer validation,
read the [consumer smoke test](docs/consumer-smoke-test.md).

## Repository map

```text
common/     reusable skills
personal/   Ryan-specific workflows
meta/       skill-system skills
data/       generated registries
scripts/    discovery, sync, validation, evaluation
docs/       detailed guides
templates/  context and artifact templates
```

## Documentation and contribution

Start with the [documentation index](docs/README.md). Contributors should
review the [authoring guide](docs/authoring.md), [evaluation contract](docs/evaluation-contract.md),
[promotion policy](docs/promotion.md), and [versioning policy](docs/versioning.md).

A contribution should keep each skill narrow, define explicit activation and
exclusion boundaries, include representative and boundary evaluation cases,
and pass repository validation before commit.

## License

See [LICENSE](LICENSE).
