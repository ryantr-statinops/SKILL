"""Regression tests for failure recovery and incomplete-output contracts."""

import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RecoveryOutputTests(unittest.TestCase):
    def test_failure_cases_require_evidence_and_recovery_reporting(self) -> None:
        cases = json.loads(
            (ROOT / "tests/fixtures/recovery-output.json").read_text(encoding="utf-8")
        )
        for case in cases:
            skill = (ROOT / case["skill"] / "SKILL.md").read_text(encoding="utf-8")
            for term in case["required_terms"]:
                self.assertIn(term, skill, case["name"])

    def test_handoff_and_review_templates_cover_incomplete_output_fields(self) -> None:
        handoff = (ROOT / "templates/handoff.md").read_text(encoding="utf-8")
        review = (ROOT / "templates/code-review-report.md").read_text(encoding="utf-8")
        for field in (
            "Current status:",
            "Files changed:",
            "Checks run:",
            "Tests:",
            "Review result:",
            "Risk:",
            "Action:",
        ):
            self.assertIn(field, handoff)
        for field in ("Readiness:", "Unresolved risk:", "Required follow-up:"):
            self.assertIn(field, review)


if __name__ == "__main__":
    unittest.main()
