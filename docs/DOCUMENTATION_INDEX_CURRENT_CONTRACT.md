# Documentation Index

Purpose of rewrite:
- Preserve a useful documentation map.
- Re-index the docs around stable system roles instead of one old product stack.
- Keep this as a navigation document, not a status note.

Source document:
- `DOCUMENTATION_INDEX.md`

Rewrite posture:
- local-first
- anti-drift
- no invention

## What This Documentation Set Covers

This documentation set describes a portable Kaitiaki system.

It is organized around:
- system intent
- guardian behavior
- data ownership and sovereignty
- interaction surfaces
- runtime services
- staging and endpoint storage
- deployment profiles

It should be readable without assuming one exact framework or provider.

## Read By Question

### What is this system?
- Start with:
  - `STRUCTURE_GUIDE.md`
  - `QUICK_REFERENCE.md`
  - `how_to_run.md`

### Who owns what?
- Read:
  - `technical/OWNERSHIP.md`
  - `guides/CONTRIBUTING.md`
  - `guides/KAITIAKI_SDK_VISION.md`

### How does data move?
- Read:
  - `technical/VECTOR_INDEX_GUIDE.md`
  - `technical/FRONTEND_BACKEND_INTEGRATION.md`
  - `guides/TE_REO_WORKFLOW.md`

### How does the guardian work?
- Read:
  - `technical/FASTAPI_COMPLETE.md`
  - `phase-summaries/BACKEND_STATUS.md`
  - `phase-summaries/BACKEND_DELIVERY_SUMMARY.md`

### How do deployment choices fit in?
- Read:
  - `guides/SELF_HOSTING.md`
  - `guides/DEPLOYMENT_CHECKLIST.md`
  - `guides/SUPABASE_SETUP.md`
    - historical/mechanical reference only if still relevant to a chosen profile

### What are the business, governance, or trust docs?
- Read:
  - `technical/OWNERSHIP.md`
  - `technical/COMMUNITY_MODEL.md`
  - `TRANSPARENCY.md`
  - `technical/FREE_TIER_ELIGIBILITY.md`

## Read By Role

### Builder
- `STRUCTURE_GUIDE.md`
- `QUICK_REFERENCE.md`
- `technical/FASTAPI_COMPLETE.md`
- `technical/FRONTEND_BACKEND_INTEGRATION.md`
- `guides/CONTRIBUTING.md`

### Guardian/Operator
- `how_to_run.md`
- `technical/OWNERSHIP.md`
- `guides/DEPLOYMENT_CHECKLIST.md`
- `phase-summaries/BACKEND_STATUS.md`

### Researcher / Knowledge Worker
- `guides/TE_REO_WORKFLOW.md`
- `technical/VECTOR_INDEX_GUIDE.md`
- `guides/KAITIAKI_SDK_VISION.md`

### Decision Maker / Partner
- `STRUCTURE_GUIDE.md`
- `technical/OWNERSHIP.md`
- `TRANSPARENCY.md`
- `technical/COMMUNITY_MODEL.md`

## Read By System Layer

### Mauri
- contracts
- structure
- ownership
- governance

Primary docs:
- `STRUCTURE_GUIDE.md`
- `technical/OWNERSHIP.md`
- `TRANSPARENCY.md`

### Kaitiaki
- guardian behavior
- policy enforcement
- protected routing

Primary docs:
- `technical/FASTAPI_COMPLETE.md`
- `phase-summaries/BACKEND_STATUS.md`

### Runtime / Services
- service logic
- integration boundaries
- current operating shape

Primary docs:
- `technical/FRONTEND_BACKEND_INTEGRATION.md`
- `phase-summaries/BACKEND_DELIVERY_SUMMARY.md`

### Rongohia / Indexing / Intake
- ingestion
- vector indexing
- search
- extraction and recall patterns

Primary docs:
- `technical/VECTOR_INDEX_GUIDE.md`
- `guides/TE_REO_WORKFLOW.md`

### Whenua
- interaction patterns
- UI/runtime connection

Primary docs:
- `technical/FRONTEND_BACKEND_INTEGRATION.md`
- `guides/KAITIAKI_SDK_VISION.md`

## Document Types

### Core Contract Docs
- describe what the system is
- define roles, boundaries, and ownership

### Operational Docs
- explain how to run, test, or deploy a profile

### Technical Deep Dives
- explain how a subsystem works

### Historical Summaries
- capture phase history, delivery shape, or decisions from earlier states

### Governance And Trust Docs
- explain ownership, transparency, community, and responsibility

## Current Translation

The original index was useful but centered one older product identity and one older stack. This rewrite keeps the same navigation purpose while indexing the docs by stable role, question, and function so the set can support multiple implementations later.

## Status Summary

- Keep:
  - question-based navigation
  - role-based reading order
  - visibility of governance and trust docs
- Change:
  - product-stack references into system-role references
  - cloud/provider assumptions into optional profile references
- Drop:
  - single-stack file-tree as the implied only truth

## Open Questions

- Which docs should be treated as the core canonical contract set?
- Which older setup docs should be explicitly marked as profile-specific or historical?

## Historical Memory Still Valuable

- The original instinct to make the documentation browsable by user intent.

## Not Current Runtime Truth

- old product name as the only framing
- old stack map as the only valid organization
