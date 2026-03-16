# Quick Reference

Purpose of rewrite:
- Preserve a real quick-reference sheet.
- Remove stack lock-in and stale provider assumptions.
- Keep the document operational and portable.

Source document:
- `QUICK_REFERENCE.md`

Rewrite posture:
- local-first
- anti-drift
- no invention

## What This System Needs

Every implementation profile should provide the following:

- an interaction surface
- a guardian layer
- backend runtime services
- shared staging storage
- endpoint storage by lane
- optional indexing/search services

## Core Runtime Roles

### Interaction
- User-facing chat or operator console
- Can be browser, desktop, terminal, or another client
- Models and tool lists live here or at the edge

### Guardian
- Validates requests
- Checks `pou`
- Checks `tapu_level`
- Blocks disallowed actions
- Promotes only cleared data

### Runtime Services
- Serve the work of each lane
- Examples:
  - translation and glossary service
  - research and memory service
  - intake and document processing service
  - build/manifests service
  - sensing/OCR service

### Storage
- shared staging for intake and processing
- destination storage for accepted lane truth

## Core Concepts

### Pou
- `tikanga`
- `tapu`
- `whakapapa`
- `whakairo`
- `rongo`
- `taonga`

### Tapu Level
- `open`
- `caution`
- `restricted`
- `sacred`

### Data Movement
- stage first
- process and review
- guardian checks
- promote to the correct lane

## Common Operational Questions

### Where do I put new system meaning?
- In Mauri.
- Contracts, schemas, structure rules, ownership, and intent belong there.

### Where do I put runtime code?
- In the backend runtime realm.
- Service logic belongs with the lane or runtime that owns it.

### Where does raw intake go?
- Shared staging first.
- Not directly into endpoint truth.

### Where does trusted language data go?
- Into `tikanga` after review and clearance.

### Where does relational memory go?
- Into `whakapapa`.

### What decides whether something is allowed?
- Kaitiaki.

## Portable Command Patterns

Exact commands depend on the current implementation profile, but the recurring operations are stable:

### Start Local Development
- start the backend runtime
- start the interaction surface
- start any optional indexing/search services
- ensure staging and endpoint storage are available

### Run Guardian Tests
- validate allowed and blocked actions
- validate `pou` routing
- validate `tapu_level` enforcement
- validate promotion rules

### Run Service Tests
- translation/service lookup
- staging and promotion
- memory/research writes
- indexing and semantic retrieval

### Run Docs/Contract Review
- check that implementation still matches the contracts
- check that no new framework lock-in leaked into the core docs

## Current Implementation Example

A current profile may use:
- Python services
- Node-based UI or client runtime
- local models
- local databases
- optional dev containers

Those are implementation choices, not the architecture itself.

## Useful Mental Model

If you need to answer “where does this go?” use this order:

1. What `pou` is it?
2. What `tapu_level` is it?
3. Is it still staging material or accepted lane truth?
4. Does the guardian allow it?
5. Which runtime service owns it?

## Current Translation

The original quick reference was good at giving a fast operational picture, but it tied the system to one older frontend/backend/database stack. The current version keeps the same quick-reference purpose while making the roles portable and stable across setups.

## Status Summary

- Keep:
  - the fast lookup format
  - operational orientation
  - quick “where does this live?” guidance
- Change:
  - stack-specific commands as if universal
  - browser-only memory assumptions
  - named provider switching as core architecture
- Drop:
  - old service endpoints as architectural truth

## Open Questions

- Which implementation profile should be documented first as the current live example?
- Should there be a separate profile-specific quick reference for local Python/Node/local-model operation?

## Historical Memory Still Valuable

- The original document’s operational clarity.
- The instinct to make startup and navigation easy for contributors.

## Not Current Runtime Truth

- old Vite/Supabase/Redis/Chroma service list as universal architecture
- browser localStorage as core system memory
- model-provider switching as a system requirement
