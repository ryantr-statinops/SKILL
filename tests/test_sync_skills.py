"""Regression tests for bundle-based selected sync."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import json

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/sync_skills.py"


class SyncSkillsTests(unittest.TestCase):
    def run_sync(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_list_bundles(self) -> None:
        result = self.run_sync("--list-bundles")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("feature-delivery", result.stdout)
        self.assertIn("personal-python", result.stdout)

    def test_check_mode_does_not_copy_bundle(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "skills"
            result = self.run_sync("--bundle", "feature-delivery", "--check", str(destination))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(destination.exists())
            self.assertFalse((destination / ".skill-sync.json").exists())

    def test_sync_copies_bundle_and_rejects_existing_target(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "skills"
            first = self.run_sync("--bundle", "feature-delivery", str(destination))
            self.assertEqual(first.returncode, 0, first.stderr)
            copied = destination / "common/workflow/feature-delivery/SKILL.md"
            self.assertTrue(copied.is_file())
            manifest = destination / ".skill-sync.json"
            self.assertTrue(manifest.is_file())
            payload = json.loads(manifest.read_text(encoding="utf-8"))
            self.assertEqual(payload["bundle"], "feature-delivery")
            self.assertTrue(
                any(item["path"].endswith("feature-delivery/SKILL.md") for item in payload["files"])
            )
            for template in (
                "CONTEXT.md",
                "feature-spec.md",
                "code-review-report.md",
                "handoff.md",
            ):
                self.assertTrue((destination / "templates" / template).is_file())

            second = self.run_sync("--bundle", "feature-delivery", str(destination))
            self.assertNotEqual(second.returncode, 0)
            self.assertIn("already exist", second.stderr)

    def test_explicit_workflow_sync_includes_declared_dependencies(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "skills"
            result = self.run_sync(
                str(destination),
                "common/workflow/feature-delivery",
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(
                (destination / "common/foundation/task-planning/SKILL.md").is_file()
            )

    def test_update_check_and_local_modification_guard(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "skills"
            first = self.run_sync("--bundle", "feature-delivery", str(destination))
            self.assertEqual(first.returncode, 0, first.stderr)
            checked = self.run_sync(
                "--bundle", "feature-delivery", "--update", "--check", str(destination)
            )
            self.assertEqual(checked.returncode, 0, checked.stderr)
            skill = destination / "common/workflow/feature-delivery/SKILL.md"
            skill.write_text(skill.read_text(encoding="utf-8") + "\nlocal edit\n", encoding="utf-8")
            rejected = self.run_sync("--bundle", "feature-delivery", "--update", str(destination))
            self.assertNotEqual(rejected.returncode, 0)
            self.assertIn("modified locally", rejected.stderr)


if __name__ == "__main__":
    unittest.main()
