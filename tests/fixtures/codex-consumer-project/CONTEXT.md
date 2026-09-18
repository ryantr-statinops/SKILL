# Consumer project context

## Project purpose

This fixture validates that selected portable skills can be installed into a
small coding project without copying the source repository.

## Domain vocabulary

- `consumer`: the project receiving selected skills;
- `skill root`: `.agent/skills/`;
- `artifact`: a reviewed document under `docs/agent/`.

## Architecture boundaries

The source project is intentionally small. Skill content is external to the
project and is installed only through the selected sync interface.

## Testing and verification

The test seam is `tests/test_example.py` and should remain runnable without
network access.

## Work artifacts

- Artifact root: `docs/agent/`
- Handoffs: `docs/agent/handoffs/`
