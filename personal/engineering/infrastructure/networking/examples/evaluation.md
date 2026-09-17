# Evaluation

## Representative task

Task: Diagnose why a service can resolve a hostname but cannot connect to the expected port.

Expected: Separate DNS, routing, listener, firewall, and application-layer evidence.

Failure condition: Change firewall or routes before collecting evidence and preserving rollback.

Validation: Reproduce the connection test from the relevant network location and document the fixed layer.

## Boundary task

Task: Fix a malformed JSON response from a reachable API.

Expected: Route to backend/API debugging rather than network diagnostics.

Failure condition: Change network configuration for an application serialization bug.

Validation: Confirm the failure remains reachable and is tested at the API layer.
