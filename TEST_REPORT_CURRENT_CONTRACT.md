# Test Report

Purpose of rewrite:
- Preserve the testing intent without freezing one dated stack report as permanent truth.
- Keep this useful as a test contract and validation reference.

Source document:
- `TEST_REPORT.md`

Rewrite posture:
- local-first
- anti-drift
- no invention

## What This Document Is For

This document defines what a working implementation profile should prove before it is trusted.

It is not a permanent “done” certificate.
It is a validation frame for current and future profiles.

## Core Validation Areas

### Interaction Validation
- the chosen UI or client can submit requests
- the runtime returns answers or refusals
- the interaction layer can display context or lane outcomes if designed to do so

### Guardian Validation
- allowed actions succeed
- blocked actions are refused
- `pou` boundaries are enforced
- `tapu_level` rules are enforced
- unsafe promotion is prevented

### Staging Validation
- intake lands in shared staging
- provenance is preserved
- processing metadata is preserved
- staging is not mistaken for endpoint truth

### Endpoint Validation
- cleared records can be promoted to the correct lane
- uncleared records remain blocked
- lane reads come from the correct destination store

### Indexing And Retrieval Validation
- semantic/vector indexing only touches records allowed for that stage
- retrieval returns relevant context without changing source truth
- folded/index-helper representations do not replace canonical text

## Minimum Smoke Tests

### Request And Response
- submit a simple request through the current interaction surface
- confirm the runtime responds

### Guardian Route Check
- submit an allowed action to an allowed lane
- submit a blocked action to a blocked lane
- confirm refusal behavior is explicit

### Staging And Promotion
- stage a record
- confirm it remains in staging until cleared
- promote a cleared record
- confirm it lands in the correct destination lane

### Memory And Relational Recall
- write a relational note into the correct memory lane
- retrieve it through the correct lane
- confirm it is not misclassified as reviewed truth

### Translation Or Language Lookup
- request a language lookup against reviewed safe data
- confirm the answer comes from the approved lane or is refused if unsupported

## Optional Profile-Specific Tests

Depending on the active implementation profile, also test:
- local model integration
- Node/Python runtime coordination
- dev container startup
- API-only usage via curl
- CLI usage

These belong to a profile appendix, not to the core test contract.

## Current Translation

The original document contained valuable proof-of-work energy, but it mixed:
- one old frontend stack
- one old backend stack
- old service endpoints
- “production ready” language
- specific libraries as if they were the architecture

The durable part is the testing mindset:
- prove the flow
- prove the boundaries
- prove persistence and recall
- prove the guardian is doing its job

## Status Summary

- Keep:
  - end-to-end validation mindset
  - concrete route testing
  - emphasis on proving the system works
- Change:
  - dated stack verification into portable validation categories
  - “all pass” framing into ongoing profile validation
- Drop:
  - old service matrix as universal truth
  - permanent readiness claims

## Open Questions

- Which smoke tests are mandatory for every future profile?
- Should profile-specific test reports live beside each deployment profile?

## Historical Memory Still Valuable

- The original document’s insistence on testing complete flows, not just components in isolation.

## Not Current Runtime Truth

- old dev-container/service inventory as universal runtime
- old provider-switching details as system requirements
- “production ready” status claim
