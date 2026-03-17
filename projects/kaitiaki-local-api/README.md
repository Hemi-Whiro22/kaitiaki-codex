# kaitiaki-local-api

First local-first implementation project carved from `kaitiaki-codex`.

## Purpose

This project is a small Python API and FastMCP service surface that stays
local-first and downstream of the Kaitiaki contracts.

## Current Shape

- `manifest.yaml`
  - project contract and runtime choices
- `api/`
  - FastAPI and FastMCP entrypoints
- `services/`
  - guardian and local inference adapters
- `app/`
  - settings and shared models
- `scripts/`
  - local helpers
- `tests/`
  - project checks

## Ports

- API: `8093`
- MCP: `8172`
- Inference upstream: `8090`

## Start Goal

Get to a minimal local service that can:
- return health
- report profile/runtime configuration
- expose a small MCP surface
- stay aligned with the local-first Kaitiaki posture

## Bootstrap

```bash
make bootstrap-project
source .venv/bin/activate
make test
make run-api
```

For the MCP surface:

```bash
source .venv/bin/activate
make run-mcp
```
