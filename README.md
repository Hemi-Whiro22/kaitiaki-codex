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

1. Read [docs/STRUCTURE_GUIDE_CURRENT_CONTRACT.md](/home/hemi-whiro/kaitiaki-codex/docs/STRUCTURE_GUIDE_CURRENT_CONTRACT.md)
2. Read [docs/QUICK_REFERENCE_CURRENT_CONTRACT.md](/home/hemi-whiro/kaitiaki-codex/docs/QUICK_REFERENCE_CURRENT_CONTRACT.md)
3. Read [docs/how_to_run_CURRENT_CONTRACT.md](/home/hemi-whiro/kaitiaki-codex/docs/how_to_run_CURRENT_CONTRACT.md)
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

## Upstream Contract

This repo is downstream of `kaitiaki-framework-101`.
It is meant to implement and support coder workflows, not redefine the canonical contracts.
