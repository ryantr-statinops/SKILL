"""Regression tests for the promotion registry contract."""

from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from promotions import validate_promotion_registry  # noqa: E402


def record(identifier: str, status: str = "stable") -> dict[str, str]:
    return {
        "id": identifier,
        "status": status,
        "description": "A documented skill.",
        "invocation": "both",
    }


class PromotionRegistryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        skill = self.root / "common/example"
        (skill / "examples").mkdir(parents=True)
        (skill / "SKILL.md").write_text("# Example\n", encoding="utf-8")
        (skill / "examples/evaluation.md").write_text("# Evaluation\n", encoding="utf-8")
        self.bundles = [{"skills": ["common/example"]}]

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_empty_registry_is_valid(self) -> None:
        self.assertEqual(
            validate_promotion_registry(
                {"schema_version": 1, "skills": []}, [], [], root=self.root
            ),
            [],
        )

    def test_valid_promoted_skill_is_returned(self) -> None:
        self.assertEqual(
            validate_promotion_registry(
                {"schema_version": 1, "skills": ["common/example"]},
                [record("common/example")],
                self.bundles,
                root=self.root,
            ),
            ["common/example"],
        )

    def test_duplicate_promoted_skill_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "duplicate"):
            validate_promotion_registry(
                {"schema_version": 1, "skills": ["common/example", "common/example"]},
                [record("common/example")],
                self.bundles,
                root=self.root,
            )

    def test_unstable_skill_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "not stable"):
            validate_promotion_registry(
                {"schema_version": 1, "skills": ["common/example"]},
                [record("common/example", status="experimental")],
                self.bundles,
                root=self.root,
            )

    def test_missing_bundle_membership_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "supported bundle"):
            validate_promotion_registry(
                {"schema_version": 1, "skills": ["common/example"]},
                [record("common/example")],
                [],
                root=self.root,
            )


if __name__ == "__main__":
    unittest.main()
