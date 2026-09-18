"""Regression tests for invocation metadata, registry, and discovery."""

import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from discover_skills import normalize_registry  # noqa: E402
from generate_skill_index import REGISTRY_SCHEMA_VERSION, collect, render_json  # noqa: E402
from migrate_invocation_metadata import expected_invocation, migrate_text  # noqa: E402


class InvocationContractTests(unittest.TestCase):
    def test_all_skills_have_expected_invocation(self) -> None:
        records = collect()
        self.assertEqual(len(records), 71)
        self.assertEqual({record["invocation"] for record in records}, {"user", "both"})
        for record in records:
            self.assertEqual(record["invocation"], expected_invocation(record["id"]))

    def test_migration_inserts_invocation_after_version(self) -> None:
        source = (
            "---\n"
            "name: task-planning\n"
            "version: 1.0.0\n"
            "---\n"
            "\n"
            "# Task planning\n"
        )
        migrated = migrate_text(source, "common/foundation/task-planning")
        self.assertIn("version: 1.0.0\ninvocation: user\n---\n", migrated)
        self.assertEqual(
            migrate_text(migrated, "common/foundation/task-planning"), migrated
        )

    def test_unknown_skill_requires_an_explicit_mapping(self) -> None:
        with self.assertRaises(ValueError):
            expected_invocation("common/new-skill")

    def test_registry_uses_schema_v2_and_exposes_invocation(self) -> None:
        registry = json.loads(render_json(collect()))
        self.assertEqual(registry["schema_version"], REGISTRY_SCHEMA_VERSION)
        self.assertTrue(all("invocation" in item for item in registry["skills"]))

    def test_schema_v1_defaults_legacy_records_to_both(self) -> None:
        legacy = {
            "schema_version": 1,
            "skills": [{"id": "legacy/example", "name": "example"}],
        }
        records = normalize_registry(legacy)
        self.assertEqual(records[0]["invocation"], "both")

    def test_schema_v2_rejects_invalid_invocation(self) -> None:
        current = {
            "schema_version": 2,
            "skills": [{"id": "example", "invocation": "implicit"}],
        }
        with self.assertRaises(ValueError):
            normalize_registry(current)


if __name__ == "__main__":
    unittest.main()
