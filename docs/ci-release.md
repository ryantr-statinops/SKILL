# CI and release workflow

## Continuous validation

GitHub Actions runs on pull requests and pushes to `main`. The workflow checks
skill metadata, generated indexes, evaluation contracts, local Markdown links,
and whitespace. It does not require network access for external URLs.

Run the same checks locally:

```bash
pytest -q
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/validate_skills.py
python3 scripts/generate_skill_index.py --check
python3 scripts/run_evaluations.py --format json
python3 scripts/check_markdown_links.py
git diff --check
```

## Release preparation

CI does not create tags, publish packages, or push to any remote. A release is
an explicit maintainer action after a reviewed batch is ready:

1. Confirm the validation workflow is green.
2. Review the diff and the generated registry.
3. Review skill SemVer changes and update `CHANGELOG.md`.
4. Record compatibility, subtree, and breaking-change notes.
5. Create and push a `vMAJOR.MINOR.PATCH` tag.
6. Publish a release report containing commit, tag, skill count, checks, and
   known limitations.

External URL checks are manual and opt-in:

```bash
python3 scripts/check_markdown_links.py --external
```

Network failures from this optional command must not be confused with local
documentation failures.
