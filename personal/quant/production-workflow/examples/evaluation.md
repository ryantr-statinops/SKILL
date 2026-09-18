## Representative task

Task: Turn a validated quantitative research artifact into a monitored, reproducible production workflow with data freshness checks, versioned features, recovery, rollback, and human approval.

Expected: Define the research handoff, data/feature contract, reproducible versions, batch or online boundary, monitoring, failure recovery, audit trail, risk gate, and explicit human approval point.

Failure condition: Treat a passing backtest as production readiness, omit freshness or recovery checks, or propose automatic account/order execution.

Validation: Review reproducibility, data-quality and freshness checks, monitoring, recovery/rollback, auditability, and no-execution boundaries.

## Boundary task

Task: Formulate and test a new signal hypothesis with out-of-sample splits and transaction costs.

Expected: Route to `personal/quant/research`; production workflow may identify a future handoff but should not design deployment before research evidence exists.

Failure condition: Add production infrastructure before the hypothesis, baseline, timing, leakage, and evaluation design are established.

Validation: Confirm the primary route is quant research and production concerns remain conditional.
