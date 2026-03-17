# Kaitiaki Framework 101

This branch is an implementation profile workspace built from the canonical Kaitiaki framework docs.

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
  - local profile logs and state trail for this branch
- `Makefile`
  - common profile commands

## What This Branch Is

This is not the upstream source of meaning.
The docs remain the contract.

This branch is the first concrete profile for:
- local development
- dev container setup
- environment carving

## Start Here

1. Read [docs/STRUCTURE_GUIDE_CURRENT_CONTRACT.md](/home/hemi-whiro/kaitiaki-framework-101/docs/STRUCTURE_GUIDE_CURRENT_CONTRACT.md)
2. Read [docs/QUICK_REFERENCE_CURRENT_CONTRACT.md](/home/hemi-whiro/kaitiaki-framework-101/docs/QUICK_REFERENCE_CURRENT_CONTRACT.md)
3. Read [docs/how_to_run_CURRENT_CONTRACT.md](/home/hemi-whiro/kaitiaki-framework-101/docs/how_to_run_CURRENT_CONTRACT.md)
4. Then use the dev container or local scripts in this repo

## Current Profile Goal

Build a local-first development environment that can host:
- documentation
- Python and Node tooling
- profile scripts
- local CUDA-backed llama.cpp checks and smoke tests
- future backend/UI/runtime work

without redefining the upstream contracts.
