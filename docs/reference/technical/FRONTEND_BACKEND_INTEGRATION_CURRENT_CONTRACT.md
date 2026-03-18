# Interaction And Runtime Integration

Purpose of rewrite:
- Preserve the interaction-to-runtime contract without tying it to one old React/FastAPI integration example.
- Keep this useful as a boundary document between clients and services.

Source document:
- `technical/FRONTEND_BACKEND_INTEGRATION.md`

Rewrite posture:
- local-first
- anti-drift
- no invention

## Core Integration Rule

The interaction layer and the backend runtime should communicate through clear contracts.

The interaction layer may:
- gather natural language input
- maintain session state
- present tools and results
- help shape structured action requests

The backend runtime may:
- validate and execute allowed work
- call services
- write to staging or endpoint stores through the correct path

Kaitiaki decides what is allowed.

## What The Interaction Layer Should Send

The interaction layer should prefer structured requests where possible.

A useful request may include:
- requested action
- target `pou`
- relevant `tapu_level` or profile posture
- user/session context
- payload or attached files

This reduces drift because the backend does not need to guess what the user meant if the client already knows.

## What The Runtime Should Return

A useful runtime response may include:
- result or refusal
- lane used
- storage outcome
- relevant policy decision
- references, provenance, or related context if the profile supports that

## UI/Client Replaceability

The interaction surface is replaceable.

That means the system can support:
- browser UI
- terminal UI
- local chat surface
- dev console
- mobile or desktop client

The contract should not assume one frontend framework as core architecture.

## Model And Tool Awareness

If a client model is tool-aware, it can help assemble structured action requests.
That is fine.

But the runtime still must not trust client intent blindly.
Kaitiaki must still check:
- allowed lane
- allowed action
- handling posture
- promotion rules

## Integration Boundaries

### Client / Whenua
- owns interaction
- may know the tool list
- may maintain conversational context

### Kaitiaki
- validates and routes
- blocks disallowed requests

### Runtime Services
- execute lane-specific work

### Storage
- persists staging or endpoint state as allowed

## Current Translation

The original document was a good code-heavy example of one frontend talking to one FastAPI backend. The deeper, durable lesson is:
- the interaction layer and backend need a stable contract
- structured requests are better than hidden guessing
- the UI should not become the core system
- the backend should not silently absorb UI concerns

This rewrite keeps that integration meaning while removing stack-specific code as architecture.

## Status Summary

- Keep:
  - clear integration boundary
  - structured request/response mindset
  - lane-aware integration
- Change:
  - framework-specific hooks/components into portable client-runtime contracts
- Drop:
  - old React/FastAPI example as if it defines the only integration path

## Open Questions

- Should there be a separate profile-specific client integration doc for the current implementation?
- What minimal structured action schema should all clients support?

## Historical Memory Still Valuable

- The original focus on making backend capability actually reachable from the interface.

## Not Current Runtime Truth

- old React code samples as universal interface contract
- old service endpoint list as permanent integration map
