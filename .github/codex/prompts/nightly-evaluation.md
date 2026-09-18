Run the full observable workflow evaluation for this SKILLS repository.

Evaluate all four workflows (`feature-delivery`, `bug-fixing`,
`research-decision`, and `data-analysis`) using both the representative and
boundary cases in `tests/fixtures/observable-agent-evaluations.json`. Inspect
the consumer fixture under `tests/fixtures/codex-consumer-project` and the
installed catalog/sync behavior. Run:

- `python3 scripts/check_observable_evaluations.py --format json`
- `python3 scripts/run_evaluations.py --format json`
- `python3 -m unittest discover -s tests -p 'test_*.py'`

Return a structured report separating infrastructure failures (missing tools or
credentials), runtime failures (the command or adapter failed), and behavior
failures (the expected artifact, boundary, or test result is absent). Include
the exact file and command evidence for every case. Do not claim success from
your narrative alone and do not edit the repository.
