# Skill bundles

A bundle is a named, reviewed selection of skill IDs. It is a distribution
manifest, not a second copy of skill content.

## Registry contract

The source of truth is `data/bundles.json`:

```json
{
  "schema_version": 1,
  "bundles": [
    {
      "id": "feature-delivery",
      "description": "Build a feature through planning, implementation, testing, and review.",
      "scope": "universal",
      "runtime_target": "portable",
      "allow_deprecated": false,
      "skills": ["common/workflow/feature-delivery"]
    }
  ]
}
```

Every bundle has a lowercase kebab-case `id`, a useful description, a scope,
the `portable` runtime target, an explicit deprecated-skill policy, and a list
of canonical skill IDs.

Universal bundles may contain only reusable skills. Personal bundles may add
`personal` skills but remain separate from universal distribution.

## Distribution behavior

Bundles are resolved by canonical skill ID. Sync copies each referenced skill
with its supporting resources while preserving the repository-relative layout.
It does not copy unrelated repository files.

Check mode must resolve and validate every bundle member without writing. A
normal sync reports existing target paths before replacing them. Deprecated
skills are rejected unless the bundle explicitly opts in with
`allow_deprecated: true`.

## Compatibility

Adding a bundle is additive. Removing or changing a member is a distribution
change and must be recorded in the changelog or release notes. Consumers that
need reproducibility should record the source commit or release tag together
with the bundle ID.
