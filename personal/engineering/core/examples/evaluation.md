## Representative task

Task: Compare two implementations of a hot data-processing path under a defined workload, then recommend an optimization based on measurements.

Expected: Define correctness and workload constraints, establish a baseline, identify the likely bottleneck, compare complexity and operational trade-offs, and propose a benchmark plus correctness verification before selecting an implementation.

Failure condition: Recommend a change from intuition or Big-O notation alone without a workload, baseline, correctness check, or discussion of memory/I/O/concurrency effects.

Validation: Confirm the response contains a problem model, baseline, bottleneck hypothesis, candidate comparison, benchmark plan, and explicit trade-offs.

## Boundary task

Task: Build a production data pipeline with schema validation, lineage, retries, and data-quality monitoring.

Expected: Route to `personal/engineering/data/core` and its narrower pipeline/orchestration skills; use this skill only for any underlying computational or systems trade-off.

Failure condition: Provide a complete pipeline design while ignoring data contracts, lineage, quality, or orchestration concerns.

Validation: Confirm the response identifies the data-engineering route and explains why the engineering foundation alone is insufficient.
