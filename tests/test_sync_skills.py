"""Regression tests for bundle-based selected sync."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

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

    def test_sync_copies_bundle_and_rejects_existing_target(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "skills"
            first = self.run_sync("--bundle", "feature-delivery", str(destination))
            self.assertEqual(first.returncode, 0, first.stderr)
            copied = destination / "common/workflow/feature-delivery/SKILL.md"
            self.assertTrue(copied.is_file())

            second = self.run_sync("--bundle", "feature-delivery", str(destination))
            self.assertNotEqual(second.returncode, 0)
            self.assertIn("already exist", second.stderr)


if __name__ == "__main__":
    unittest.main()
