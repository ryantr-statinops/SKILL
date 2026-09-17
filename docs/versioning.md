# Versioning and releases

SKILLS has two version layers: a version for each skill and a release version
for the repository as a distributable library.

## Skill versions

Every `SKILL.md` uses `MAJOR.MINOR.PATCH` in frontmatter.

- `PATCH`: typo, link, clarification, validation, or wording change that does
  not change activation or expected behavior.
- `MINOR`: new capability, example, or supporting resource that remains
  backward compatible.
- `MAJOR`: changed activation boundary, output contract, path, safety rule, or
  behavior that can invalidate an existing consumer.

When a change affects multiple skills, bump each affected skill independently.
Generated indexes must be regenerated after metadata changes.

## Repository releases

Repository releases use Git tags in the form `vMAJOR.MINOR.PATCH`. A release
represents a reviewed, release-ready batch rather than every individual skill
commit.

Before creating a tag:

1. Run structural validation, evaluation checks, generated-index checks, and
   local Markdown link checks.
2. Review skill version changes and breaking behavior.
3. Update `CHANGELOG.md` with Added, Changed, Fixed, Deprecated, or Removed
   entries as applicable.
4. Confirm subtree consumers can pull the batch and identify the source tag.
5. Create and push the tag only after the batch is approved.

The repository tag does not replace skill versions. The tag identifies a
coherent distribution snapshot; frontmatter identifies the lifecycle of each
skill inside it.

## Release report

A release report should record the tag, source commit, total skill count,
validator result, evaluation result, metadata changes, link-check result, and
any breaking-change note. Release automation must be explicit; ordinary CI
must never create or push tags.
