## Representative task

Task: Analyze a time-series dataset, inspect quality, clean invalid records with traceability, validate the schema, produce reproducible results, and report limitations.

Expected: Use data-analysis to define the question and contract, inspect before transforming, clean and validate, reproduce the analysis, and report uncertainty and limitations.

Failure condition: Transform or summarize data without inspection, hide invalid records, omit the reproduction path, or overstate the findings.

Validation: Confirm the report includes inputs, schema, transformations, validation results, reproduction instructions, assumptions, and limitations.

## Boundary task

Task: Fix an application crash caused by a malformed request and add a regression test.

Expected: Route to bug-fixing or debugging rather than data-analysis.

Failure condition: Treat an application defect as a dataset analysis workflow.

Validation: Confirm the data workflow is rejected and the narrower bug workflow is recommended.
