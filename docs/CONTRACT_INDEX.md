# Contract Index

This is the active documentation entry point for `kaitiaki-codex`.

Its job is simple:
- make the current contract readable
- reduce drift from overlapping docs
- keep older material visible without letting it compete with the active working rules

## Precedence

Use this order of truth:

1. [AGENTS.md](/home/hemi-whiro/kaitiaki-codex/AGENTS.md)
   Repo-level agent operating contract.
2. project-local `manifest.yaml`
   Project shape and boundary.
3. project-local `TODO_AUTONOMOUS.md`
   Current phase and next work.
4. project-local `README.md`
   Project usage and local operation.
5. profile manifests under `profiles/`
   Environment/profile only.
6. `docs/reference/`
   Reference, history, and older contract material.

## Active Reading Path

For repo work:
- [AGENTS.md](/home/hemi-whiro/kaitiaki-codex/AGENTS.md)
- [README.md](/home/hemi-whiro/kaitiaki-codex/README.md)
- [profiles/devcontainer-local/manifest.yaml](/home/hemi-whiro/kaitiaki-codex/profiles/devcontainer-local/manifest.yaml)

For a project under `projects/`:
1. project `manifest.yaml`
2. project `TODO_AUTONOMOUS.md`
3. project `README.md`
4. then only dip into `docs/reference/` if needed

## Why This Exists

The repo accumulated a large documentation set.

That is good for transparency.
It is bad for day-to-day clarity if every file sounds equally authoritative.

So this index keeps:
- transparency
- history
- browsability

without turning older docs into silent competing rulebooks.

## Reference

Older current-contract rewrites, phase summaries, architecture notes, technical guides, and lineage material are now kept under:

- [docs/reference/](/home/hemi-whiro/kaitiaki-codex/docs/reference)

Those files still matter.
They are just no longer the first operational authority for active work.
