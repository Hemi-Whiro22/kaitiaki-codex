# Backend Runtime Contract

Purpose of rewrite:
- Preserve the backend/runtime intent without locking it to one old FastAPI stack report.
- Keep this useful as a runtime boundary and service contract document.

Source document:
- `technical/FASTAPI_COMPLETE.md`

Rewrite posture:
- local-first
- anti-drift
- no invention

## What This Layer Owns

The backend runtime layer owns:
- APIs
- CLIs
- service execution
- runtime workers
- lane-specific operations
- health and operational endpoints

It does not own:
- system meaning and contracts
- UI behavior
- guardian ideology
- raw staging truth by itself

## Required Runtime Capabilities

A working backend profile should be able to:
- expose health and runtime readiness
- accept structured requests from a UI, CLI, or another client
- call the correct service lane
- persist to staging or endpoint storage through the right path
- return clear errors when a lane or action is blocked

## Relationship To Kaitiaki

The backend runtime executes work.
Kaitiaki decides whether that work is allowed.

That means:
- runtime services can perform useful actions
- but guardian policy determines whether those actions proceed
- the runtime must not silently override `pou` or `tapu_level`

## Service Lanes

The runtime should be organized by lane or domain responsibility.

Examples:

### Whakapapa Service
- relational memory
- research notes
- contextual recall
- lineage or relationship-oriented work

### Tikanga Service
- reviewed language lookup
- translation support from trusted data
- glossary and language-serving behavior

### Taonga / Intake Service
- staged intake
- extraction
- cleanup handoff
- candidate processing

### Whakairo Service
- build logic
- manifests
- implementation and change-oriented runtime behavior

### Rongo Service
- OCR
- sensing
- scan ingestion
- observational capture

## Guardian Gate Requirements

Before a runtime action changes state, the system should be able to answer:
- what `pou` does this belong to?
- what `tapu_level` applies?
- is this a staging write or endpoint promotion?
- is the caller/profile allowed to do this?

If those answers are missing, the action should not proceed silently.

## Health And Operational Visibility

A backend profile should expose enough to confirm:
- it is alive
- its required services are reachable
- guardian enforcement is available
- staging and endpoint stores are reachable if the profile depends on them

That can be done through health endpoints, CLI checks, or equivalent operational surfaces.

## Local-First Expectation

In a local-first posture:
- the runtime should prefer local execution
- remote providers should be optional
- storage should not assume cloud ownership
- a backend profile should still work in a minimal local mode where practical

## Current Translation

The original document was a strong delivery summary for one FastAPI implementation. The lasting meaning is:
- there should be a modular backend runtime
- lane-specific services should exist
- health and operational visibility matter
- cultural and handling rules belong in the runtime contract

This rewrite keeps that architecture meaning while dropping old counts, completion claims, and stack-specific framing as permanent truth.

## Status Summary

- Keep:
  - modular service design
  - runtime health visibility
  - lane-based backend thinking
- Change:
  - one FastAPI delivery summary into a portable backend contract
  - old endpoint counts into capability categories
- Drop:
  - “complete delivery” framing
  - old package and service inventory as universal truth

## Open Questions

- Which lane services should be documented first as their own dedicated contracts?
- Should there be a companion `CURRENT_PROFILE_BACKEND.md` for the live Python implementation only?

## Historical Memory Still Valuable

- The original insistence that the backend be modular and not just a single monolith.

## Not Current Runtime Truth

- old endpoint count
- old FastAPI/Supabase/Chroma/Redis stack as the only valid runtime
- “production-ready” delivery language
