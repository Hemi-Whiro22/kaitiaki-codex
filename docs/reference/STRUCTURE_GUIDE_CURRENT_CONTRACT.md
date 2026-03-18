# Structure Guide

Purpose of rewrite:
- Preserve the system structure in portable terms.
- Remove framework and provider lock-in.
- Keep this useful as a working navigation document.

Source document:
- `STRUCTURE_GUIDE.md`

Rewrite posture:
- local-first
- anti-drift
- no invention

## System Shape

The system is organized by role first, not by framework.

### Mauri
- Owns meta, contracts, schemas, config, governance, notes, and intent.
- This is where system meaning is defined.
- This layer does not own runtime behavior.

### Kaitiaki
- Owns guardian behavior.
- Validates, routes, blocks, promotes, and protects.
- Enforces `pou` boundaries and `tapu_level`.
- This layer is not a conversational model and not a reasoning engine.

### Whiro
- Owns backend runtime behavior.
- Exposes APIs, CLIs, services, workers, and execution paths.
- Carries the service logic behind each lane.

### Rongohia
- Owns intake, sensing, extraction, cleanup, chunking, indexing, and retrieval preparation.
- This is where raw or semi-processed material becomes structured enough for guardian review.

### Whenua
- Owns interaction surfaces.
- Includes chat UIs, operator consoles, public interfaces, and client applications.
- UI/model/provider choices are replaceable.

### Maunga
- Owns storage.
- Includes shared staging plus endpoint storage by lane.
- Storage is shaped by `pou`, `tapu_level`, and promotion state.

## Pou Lanes

The system is organized by `pou` so different kinds of work and data do not collapse into one generic layer.

### Tikanga
- Reviewed language data.
- Translation truth, glossary, usage guidance, public-serving language records.

### Tapu
- Handling posture and protection rules.
- Access conditions, runtime truth, sensitive boundaries, guardian controls.

### Whakapapa
- Relational memory and research.
- Session continuity, summaries, research notes, hypotheses, connections, private context.

### Whakairo
- Building and carving.
- Code, manifests, change work, implementation logic, system shaping.

### Rongo
- Sensing and capture.
- OCR, scanning, drone/polycam feeds, other observational or acquisition inputs.

### Taonga
- Material intake and sensitive holding lane.
- Candidate source handling, staged material, protected or review-bound intake.

## Data Flow Contract

Data moves through the system in a fixed order:

1. Intake enters shared staging.
2. Rongohia or related processing cleans, chunks, indexes, or extracts what is needed.
3. Kaitiaki checks `pou`, `tapu_level`, provenance, and promotion rules.
4. If allowed, the record is promoted into the correct endpoint lane.
5. Endpoint stores become the trusted working source for that lane.

This means:
- staging is not endpoint truth
- endpoint stores are not raw intake dumps
- the guardian decides whether promotion is allowed

## Storage Pattern

### Shared Staging
- Holds raw intake and working material.
- May contain extracted text, chunks, vectors, candidate review state, provenance, and processing metadata.
- Exists to support cleanup, review, and later promotion.

### Endpoint Stores
- One destination store per `pou` or service lane as needed.
- Hold accepted lane truth after guardian clearance.
- Should not be used as generic dumping grounds for raw intake.

## Runtime Pattern

The runtime is replaceable by stack, but not by role.

Any implementation still needs:
- a guardian layer
- a backend runtime layer
- an interaction layer
- a storage layer
- contracts and governance

Examples of replaceable implementation choices:
- Python or Node services
- local models or remote model providers
- SQLite, Postgres, or another storage engine
- CLI, browser UI, desktop app, or mobile client

These are profiles, not the architecture itself.

## Development Containers And Profiles

A dev container can still be useful.

Its role should be:
- holding the docs and implementation together during carving
- giving a reproducible environment
- bundling the current profile if needed

But a dev container is only a deployment/development profile.
It is not the system architecture.

## Current Navigation Questions

When looking for something, use role first:

- Need contracts or system meaning?
  - go to Mauri
- Need guardian or safety rules?
  - go to Kaitiaki
- Need service logic or APIs?
  - go to Whiro
- Need intake, extraction, cleanup, or indexing?
  - go to Rongohia
- Need UI or client interaction?
  - go to Whenua
- Need storage and promotion targets?
  - go to Maunga

## Current Translation

The original document described a clean workspace and good separation, but tied it to one older stack and one directory map. The current contract keeps the same intent:
- clear navigation
- role separation
- easy onboarding
- understandable system boundaries

What changed:
- old framework-specific paths were removed from the core structure
- old provider assumptions were removed
- portable system roles now come first
- current or future implementations can map onto this structure without redefining it

## Status Summary

- Keep:
  - the desire for clear navigation
  - the separation of major concerns
  - the “start here” function
- Change:
  - stack-specific directory assumptions
  - container-specific claims as if they are core architecture
  - completion markers and checkmarks
- Drop:
  - framework-locked tree as if it is the only valid shape

## Open Questions

- Which Maori realm names should be treated as the final canonical top-level names for portable documentation?
- How much of the current repo mapping should be retained as an implementation profile appendix?

## Historical Memory Still Valuable

- The original document’s emphasis on clarity and navigation.
- The idea of keeping structure obvious enough that contributors can find their way quickly.

## Not Current Runtime Truth

- old `pack-dashboard` directory map
- old container layout as architecture
- stack-specific completion claims
