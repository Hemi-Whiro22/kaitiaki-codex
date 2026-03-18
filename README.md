# Kaitiaki Codex

This repo is a standalone coder and dev profile built downstream from the canonical Kaitiaki framework docs.

## What This Repo Holds

- `docs/`
  - canonical current-contract documentation
  - lineage anchors
  - audit prompts and audit results
- `.devcontainer/`
  - reproducible local development profile
- `scripts/`
  - local bootstrap and start helpers
- `var/`
  - local profile logs and state trail for this repo
- `Makefile`
  - common profile commands

## What This Repo Is

This is not the upstream source of meaning.
The docs remain the contract.

This repo is the first concrete coder profile for:
- local development
- dev container setup
- environment carving
- local draft generation with a local model
- transparent local inference logging

## Start Here

1. Read [AGENTS.md](/home/hemi-whiro/kaitiaki-codex/AGENTS.md)
2. Read [docs/CONTRACT_INDEX.md](/home/hemi-whiro/kaitiaki-codex/docs/CONTRACT_INDEX.md)
3. Read [profiles/devcontainer-local/manifest.yaml](/home/hemi-whiro/kaitiaki-codex/profiles/devcontainer-local/manifest.yaml)
4. Then use the dev container or local scripts in this repo

## Current Profile Goal

Build a local-first development environment that can host:
- documentation
- Python and Node tooling
- profile scripts
- local CUDA-backed llama.cpp checks and smoke tests
- local draft generation for first-pass stubs
- future backend/UI/runtime work

without redefining the upstream contracts.

## Codex QoL Tooling

This repo also holds codex-only quality-of-life helpers for the co-dev workflow.

Examples:
- `make project-recall PROJECT=maungatapu-database`
- `make phase-check PROJECT=maungatapu-database`
- `make verify-all TARGET=maungatapu-database`

These tools are for:
- reducing context loss
- checking contract/phase anchors quickly
- making test-running a default instead of a reminder

They are agent-side helpers only.
They are not runtime dependencies of project services or databases.

## Upstream Contract

This repo is downstream of `kaitiaki-framework-101`.
It is meant to implement and support coder workflows, not redefine the canonical contracts.
