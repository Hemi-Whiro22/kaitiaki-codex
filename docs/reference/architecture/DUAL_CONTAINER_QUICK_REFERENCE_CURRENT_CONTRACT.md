# Dual Profile Quick Reference

Purpose of rewrite:
- Preserve a fast reference for the dual-profile development idea.
- Remove old container/path/port assumptions from the core.

Source document:
- `architecture/DUAL_CONTAINER_QUICK_REFERENCE.md`

Rewrite posture:
- local-first
- anti-drift
- no invention

## What This Quick Reference Covers

This quick reference is for the dual-profile development pattern:
- one profile for whole-system view
- one profile for focused work

It is not the architecture itself.

## Profile A: Whole-System View

Use this profile when you need:
- integration testing
- operational visibility
- system-wide checks
- lane interaction verification

Typical purpose:
- start the major runtime pieces together
- inspect guardian behavior in context
- confirm the end-to-end path works

## Profile B: Focused Work

Use this profile when you need:
- fast feedback
- feature work
- lane-specific debugging
- local iteration

Typical purpose:
- work on one client or service
- debug one path without the weight of the full system

## Decision Shortcut

If you are:
- checking the whole flow, use the whole-system profile
- changing one thing, use the focused profile

## What Must Stay The Same In Both

- guardian rules still apply
- `pou` boundaries still apply
- staging is not endpoint truth
- profile convenience does not redefine responsibilities

## Current Translation

The original document was a visual quick reference for two old container setups. The lasting value is the fast distinction between:
- system view
- focused development view

This rewrite keeps that quick-reference function while removing old implementation specifics from the core.

## Status Summary

- Keep:
  - quick comparison
  - rapid “which profile do I use?” guidance
- Change:
  - old container details into portable profile guidance
- Drop:
  - old directory and port layout as current truth

## Open Questions

- Should the current implementation eventually have one companion quick-reference file with exact commands for the live profile names?

## Historical Memory Still Valuable

- The original clarity of showing two different working modes side by side.

## Not Current Runtime Truth

- old visual/container map as the permanent working model
