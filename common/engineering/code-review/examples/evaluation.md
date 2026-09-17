# Evaluation

## Representative task
Review a diff for correctness, edge cases, security, regression risk, and test adequacy.

Expected: findings include evidence, impact, severity, and remediation.

Failure condition: Report speculative defects as confirmed findings.

Validation: Trace each finding to a changed line or observable behavior.

## Boundary task
Invent a defect when the supplied diff and tests provide no supporting evidence.

Expected: report no finding or a clearly labeled residual risk.

Failure condition: Invent a defect without diff or test evidence.

Validation: Confirm unsupported concerns are labeled uncertainty, not blockers.
