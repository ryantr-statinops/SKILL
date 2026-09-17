# Evaluation

## Representative task
Task: Package an analysis with versioned inputs, parameters, transformations, outputs, and rerun instructions.

Expected: a clean second run produces equivalent results within stated tolerance.

Failure condition: Depend on undocumented manual state or mutable inputs.

Validation: Run twice from a clean environment and compare declared outputs.

## Boundary task
Task: Present a manually edited result with no input or method record as reproducible.

Expected: disclose the reproducibility gap.

Failure condition: Present an unrecorded manual result as reproducible.

Validation: Confirm missing inputs, parameters, and method steps are listed.
