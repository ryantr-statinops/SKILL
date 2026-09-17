# Evaluation

## Representative task

Task: Containerize a service with reproducible dependencies, safe configuration, health checks, and a local compose setup.

Expected: Keep image/runtime boundaries explicit and avoid embedding secrets or host assumptions.

Failure condition: Copy local credentials into an image or claim containerization proves production readiness.

Validation: Build the image, run the health check, and inspect the resulting configuration.

## Boundary task

Task: Diagnose a DNS record that fails outside containers.

Expected: Use networking guidance unless a container network is part of the evidence.

Failure condition: Add Docker configuration without isolating the failing layer.

Validation: Confirm the diagnosis tests the actual DNS path.
