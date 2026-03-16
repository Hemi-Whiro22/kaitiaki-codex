# Architecture

Purpose of rewrite:
- Preserve the system architecture in stable role-based terms.
- Remove framework, container, and provider lock-in from the core architectural description.

Source document:
- `architecture/ARCHITECTURE.md`

Rewrite posture:
- local-first
- anti-drift
- no invention

## Core Architecture

The system has a familiar shape with culturally grounded naming layered over it.

### Mauri
- meta
- contracts
- schemas
- governance
- intent

### Kaitiaki
- guardian
- validation
- routing
- blocking
- promotion
- protection

### Runtime / Services
- lane-specific execution
- APIs
- CLIs
- workers
- backend logic

### Rongohia
- intake
- extraction
- cleanup
- chunking
- indexing
- retrieval preparation

### Whenua
- interaction surfaces
- UI
- console
- chat clients
- other client applications

### Maunga
- shared staging storage
- endpoint lane storage
- backup/export concerns

## Core Rules

### Guardian Rule
Kaitiaki validates and routes.
It is not a conversational model and not a freeform reasoning layer.

### Storage Rule
Shared staging and endpoint lane storage are not the same thing.

### Lane Rule
`pou` define responsibility boundaries.
One lane should not silently impersonate the whole system.

### Handling Rule
`tapu_level` is real and must affect how data moves and what it may become.

### Replaceable Edge Rule
UI, model, provider, runtime framework, and deployment profile are replaceable edges.

## Data Flow

1. intake enters staging
2. Rongohia or related processing prepares material
3. Kaitiaki checks lane, posture, and promotion conditions
4. cleared records move into the correct endpoint lane
5. interaction and service layers read from the correct source for the task

## Memory And Recall

### Whakapapa
- relational memory
- research notes
- summaries
- continuity

### Tikanga
- reviewed language truth
- glossary and trusted translation records

### Taonga
- staged or sensitive material intake

The architecture depends on keeping these roles distinct.

## Indexing And Semantic Search

Indexing is a support layer.
It may use:
- vectors
- folded text
- normalized helper forms
- chunked representations

But:
- canonical text remains canonical
- helpers remain helpers
- retrieval does not replace source truth

## Deployment Profiles

The architecture may be realized through different profiles:
- local Python/Node/local-model profile
- hosted provider profile
- self-hosted profile
- containerized dev profile

These are profiles.
They are not the architecture itself.

## Current Translation

The original document contained a detailed old stack diagram showing one dev-container-centered implementation. The lasting meaning was:
- clear layer separation
- explicit data flows
- understandable interaction between UI, runtime, and storage

This rewrite preserves that architectural intent while lifting it above one old React/Postgres/Redis/Chroma/container stack.

## Status Summary

- Keep:
  - layer separation
  - explicit flow thinking
  - visibility of indexing and interaction relationships
- Change:
  - old implementation diagram into stable architecture roles
- Drop:
  - one dev environment as the system definition

## Open Questions

- Which Maori realm names should be treated as the final canonical top-level architecture labels?
- Should there be a separate current-profile architecture diagram later for the live implementation only?

## Historical Memory Still Valuable

- The original effort to make the system legible with diagrams and flows.

## Not Current Runtime Truth

- old React/Vite/Postgres/Redis/Chroma dev-container diagram as universal architecture
- old packs/memory/localStorage data model as the permanent system shape
