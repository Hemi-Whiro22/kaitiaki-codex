# Quick Start

Purpose of rewrite:
- Preserve a short start path without tying it to one old phase, stack, or dev environment.
- Keep this as a portable quick-start guide.

Source document:
- `guides/QUICK_START_PHASE_6.md`

Rewrite posture:
- local-first
- anti-drift
- no invention

## What Quick Start Means

Quick start should answer one question:

How do I get a chosen profile running far enough to prove the core flow works?

It should not pretend:
- the whole system is complete
- one old phase defines the architecture
- one dev environment is mandatory

## Minimum Quick Start Flow

1. Choose the current implementation profile.
2. Start the runtime services needed by that profile.
3. Start or connect the interaction surface.
4. Confirm the guardian is available.
5. Run one staging flow and one retrieval flow.

## First Things To Check

### Runtime
- runtime starts
- health check answers

### Guardian
- at least one allowed request succeeds
- at least one blocked request is refused

### Storage
- staging accepts a record
- uncleared material cannot be promoted

### Retrieval
- a lane can return trusted data from the correct destination

## What To Learn First

To understand the system quickly, read in this order:
- structure guide
- quick reference
- how to run
- ownership
- relevant lane or workflow docs

## Profile Examples

Different quick starts may exist for:
- local Python/Node/local-model profile
- self-hosted profile
- API-only profile
- docs-only architecture review path

Those should be treated as profile examples, not as the architecture itself.

## Current Translation

The original document was a quick operational entry point for one older phase and stack. The durable intent is still right:
- lower the friction to get started
- point people to the most important next steps
- make the first operational path obvious

This rewrite keeps that quick-start function while removing old phase-specific framing from the core.

## Status Summary

- Keep:
  - short onboarding path
  - practical first steps
- Change:
  - old phase-specific startup into portable quick-start flow
- Drop:
  - one old environment as the mandatory start path

## Open Questions

- Which current profile should get the first concrete quick-start appendix?
- Should docs-only readers get a separate “start here for architecture” quick path?

## Historical Memory Still Valuable

- The original instinct that people need an obvious starting point, not just a pile of documents.

## Not Current Runtime Truth

- old “phase 6” framing as the current system state
- old dev-environment assumptions as the only start path
