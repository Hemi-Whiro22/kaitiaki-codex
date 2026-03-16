# Dual Container Profile

Purpose of rewrite:
- Preserve the idea of dual development profiles without treating two old containers as the architecture itself.
- Keep this as a development-profile document.

Source document:
- `architecture/DUAL_CONTAINER_ARCHITECTURE.md`

Rewrite posture:
- local-first
- anti-drift
- no invention

## What This Document Is

This document describes one style of development profile:
- one profile for full-system visibility
- one profile for focused individual work

That approach can still be useful.
It is not the core architecture.

## Durable Meaning

The original document had a strong practical idea:
- one environment optimized for full-system view
- one environment optimized for focused carving and iteration

That pattern remains useful across different implementations.

## Full-System Profile

A full-system development profile should help with:
- viewing runtime services together
- integration testing
- operational visibility
- guardian behavior in context
- end-to-end flow checks

It is best used when you need to:
- verify service interaction
- test staging-to-endpoint flow
- inspect system health
- see multiple lanes together

## Focused Development Profile

A focused development profile should help with:
- fast feedback
- targeted code changes
- lane-specific work
- debugging one service or client at a time

It is best used when you need to:
- change one service
- adjust UI/client behavior
- tune indexing or lane-specific logic
- work quickly without full-system overhead

## Profile Rules

No matter how the profiles are implemented:
- the guardian remains the guardian
- staging remains distinct from endpoint truth
- `pou` boundaries remain explicit
- profile convenience must not redefine system responsibilities

## Possible Implementations

The dual-profile idea may be realized through:
- dev containers
- multiple local run scripts
- separate compose files
- separate workspaces
- local service groups

Those are implementation details, not architecture.

## Current Translation

The original document was a detailed comparison of two old container setups. The lasting value was the distinction between:
- a whole-system view
- a focused builder view

This rewrite keeps that useful split while removing old port and container-path assumptions from the core.

## Status Summary

- Keep:
  - dual-profile development idea
  - full-system vs focused-work distinction
- Change:
  - old container map into portable profile language
- Drop:
  - old container directories and ports as if they define the system

## Open Questions

- Should the current live implementation still keep two separate development profiles?
- If yes, what are the current names for those profiles in the evolved structure?

## Historical Memory Still Valuable

- The original recognition that building and operating often need different working views.

## Not Current Runtime Truth

- old `.devcontainer` / `.devcontainer-whakairo` layout as the permanent model
- old port map as the current default
