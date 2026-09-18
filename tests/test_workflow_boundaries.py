"""Regression tests for workflow activation and exclusion boundaries."""

import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from discover_skills import discover  # noqa: E402


class WorkflowBoundaryTests(unittest.TestCase):
    def test_fixture_routes_user_workflows_without_cross_activation(self) -> None:
        cases = json.loads(
            (ROOT / "tests/fixtures/workflow-boundaries.json").read_text(encoding="utf-8")
        )
        for case in cases:
            args = type(
                "Args",
                (),
                {
                    "query": case["task"].split(),
                    "category": None,
                    "scope": "universal",
                    "status": None,
                    "invocation": "user",
                    "bundle": None,
                    "limit": 10,
                },
            )()
            results = discover(args)
            ids = [item["id"] for item in results]
            expected = case["expected_workflow"]
            if expected is None:
                self.assertFalse(ids, case["name"])
            else:
                self.assertTrue(ids, case["name"])
                self.assertEqual(ids[0], expected, case["name"])
            for excluded in case["excluded_workflows"]:
                self.assertNotEqual(ids[:1], [excluded], case["name"])


if __name__ == "__main__":
    unittest.main()
