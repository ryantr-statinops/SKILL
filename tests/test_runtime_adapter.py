"""Tests for the native runtime adapter layout."""

import subprocess
import tempfile
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/export_runtime_adapter.py"


class RuntimeAdapterTests(unittest.TestCase):
    def test_check_is_non_mutating_and_export_uses_unique_flat_names(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / ".agent/skills"
            (source / "common/engineering/debugging").mkdir(parents=True)
            (source / "personal/debugging").mkdir(parents=True)
            for directory in (source / "common/engineering/debugging", source / "personal/debugging"):
                (directory / "SKILL.md").write_text("---\nname: debugging\n---\n", encoding="utf-8")
            destination = root / ".agents/skills"
            check = subprocess.run(
                ["python3", str(SCRIPT), "--check", str(source), str(destination)],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertIn("common-engineering-debugging", check.stdout)
            self.assertFalse(destination.exists())
            subprocess.run(["python3", str(SCRIPT), str(source), str(destination)], check=True)
            first = destination / "common-engineering-debugging"
            second = destination / "personal-debugging"
            self.assertTrue(first.is_symlink())
            self.assertTrue(second.is_symlink())
            self.assertTrue((first / "SKILL.md").is_file())
            self.assertEqual(
                subprocess.run(
                    ["python3", str(SCRIPT), "--check", str(source), str(destination)],
                    check=True,
                    capture_output=True,
                    text=True,
                ).stdout,
                "",
            )


if __name__ == "__main__":
    unittest.main()
