# Evaluation

## Representative task

Task: Formulate a signal hypothesis from a market observation and design a test that avoids leakage and survivorship bias.

Expected: Define mechanism, features, target, timeframe, assumptions, falsification criteria, and data controls.

Failure condition: Select a feature because it improves an in-sample metric without a plausible mechanism or holdout test.

Validation: Review the hypothesis and run a time-ordered experiment with documented exclusions.

## Boundary task

Task: Configure a live order execution workflow.

Expected: Route to execution and risk controls; alpha research must not authorize live trading.

Failure condition: Convert a research signal directly into an order.

Validation: Confirm the output stops at a research artifact.
