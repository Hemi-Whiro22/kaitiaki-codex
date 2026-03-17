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
- accept guardian-gated intake
- accept multiple local file types and normalize them to text
- scrub metadata and stage locally
- promote cleared intake into per-pou endpoint DBs
- search promoted local chunks for recall
- expose semantic-ready chunk candidates for future vector indexing
- build a local semantic index and query it
- scan and ingest mixed local archive folders such as ChatGPT export bundles
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

For retrieval after intake:

```bash
curl 'http://127.0.0.1:8093/search?q=local'
curl 'http://127.0.0.1:8093/intake'
curl 'http://127.0.0.1:8093/semantic-ready'
curl -X POST 'http://127.0.0.1:8093/index/semantic-sync'
curl 'http://127.0.0.1:8093/search/semantic?q=recall'
```

For archive folders:

```bash
curl -X POST 'http://127.0.0.1:8093/archive/scan' \
  -H 'Content-Type: application/json' \
  -d '{"folder_path":"/path/to/archive","target_pou":"whakapapa","is_tapu":false}'

curl -X POST 'http://127.0.0.1:8093/archive/ingest' \
  -H 'Content-Type: application/json' \
  -d '{"folder_path":"/path/to/archive","target_pou":"whakapapa","is_tapu":false,"max_text_files":25}'
```
