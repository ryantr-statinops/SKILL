# Promotion and distribution lifecycle

`status` describes a skill's lifecycle: `draft`, `experimental`, `stable`, or
`deprecated`. Promotion is a separate distribution decision and is recorded in
`data/promoted.json` rather than duplicated in every `SKILL.md`.

## Promoted skill contract

A promoted skill must be:

- stable in its frontmatter;
- documented in the public repository guides;
- covered by the required evaluation contract;
- included in at least one supported bundle;
- valid under the repository metadata, link, and invocation checks.

Promotion does not move or copy skill content. It makes an existing skill an
explicitly supported entry point for consumer projects.

## Lifecycle meanings

- `experimental`: usable, but still seeking evidence and feedback from real
  workflows;
- `stable`: the skill contract is mature and changes follow the versioning
  policy;
- `deprecated`: excluded from new bundles and workflows unless a reviewed
  compatibility exception explicitly allows it.

A skill may remain `stable` without being promoted when it is repository-only
or has not yet been selected for supported consumer distribution.

## Promotion review

Before adding a skill to `data/promoted.json`, review its activation boundary,
evaluation cases, supporting links, bundle membership, and consumer behavior.
Promotion should be a small reviewed set rather than an automatic conversion
of the entire library.
