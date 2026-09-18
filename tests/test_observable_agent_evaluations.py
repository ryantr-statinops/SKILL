"""Deterministic checks for representative and boundary agent cases."""

import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ObservableAgentEvaluationTests(unittest.TestCase):
    def test_all_workflow_cases_have_observable_contracts(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/check_observable_evaluations.py", "--format", "json"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["total"], 8)
        self.assertEqual(report["failed"], 0)


if __name__ == "__main__":
    unittest.main()
