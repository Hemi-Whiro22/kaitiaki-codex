# Vector And Semantic Indexing Guide

Purpose of rewrite:
- Preserve the indexing and semantic search intent without tying it to one specific old database/index implementation.
- Keep this useful as an indexing and retrieval contract.

Source document:
- `technical/VECTOR_INDEX_GUIDE.md`

Rewrite posture:
- local-first
- anti-drift
- no invention

## Why Semantic Indexing Exists

Semantic indexing exists to improve recall.

It helps the system:
- find related material beyond exact keyword matches
- surface useful context from prior records
- support relational recall in memory, intake, or reviewed language lanes

It is a support layer.
It is not the source of truth by itself.

## Indexing Contract

Indexing should respect the same architecture boundaries as the rest of the system.

That means:
- canonical text remains canonical
- folded/search-helper forms are helpers only
- staging and endpoint data are not automatically the same thing
- guardian clearance matters before promotion or endpoint trust

## What The Indexer May Work On

Depending on the current profile, the indexer may process:
- staged records marked ready for indexing
- endpoint records approved for lane recall
- extracted chunks
- folded/search-helper variants
- vector representations

It should not silently turn raw, uncleared, or protected material into public-serving truth.

## Canonical Text And Folded Text

For Māori and other language material:
- preserve the canonical form
- keep macrons and proper spelling
- derive folded or normalized forms only for matching and access

This means:
- `Māori` stays `Māori`
- a helper index may also include `maori`
- returned truth should still use the canonical form

## Retrieval Pattern

A useful retrieval flow is:

1. select the correct lane
2. filter by handling posture and lane rules
3. search semantic/vector indexes if the profile supports them
4. return related context
5. let the caller or model use that context without mutating source truth

## Approximate Search

Different profiles may use different ANN strategies or vector stores.
That is fine.

The durable rule is:
- retrieval speed is useful
- approximation is acceptable if the tradeoff is explicit
- the indexing strategy should not be mistaken for architecture

## Role In The System

Indexing belongs closer to intake, retrieval, and recall support than to the guardian itself.

The guardian decides whether a record may progress.
The indexer helps organize and recall allowed material.

## Current Translation

The original document gave a clear explanation of one IVFFlat implementation. The lasting meaning is stronger than that one setup:
- semantic retrieval matters
- indexing needs explicit tradeoffs
- canonical text must be preserved
- retrieval should support the system without replacing the source of truth

This rewrite keeps that meaning while making the indexing contract portable across implementations.

## Status Summary

- Keep:
  - semantic retrieval explanation
  - indexing tradeoff awareness
  - practical performance thinking
- Change:
  - one IVFFlat/PostgreSQL deep dive into a portable indexing contract
- Drop:
  - one exact indexing backend as if universal architecture

## Open Questions

- Which current indexing profile should be documented as the live implementation example?
- Should staging indexes and endpoint indexes be documented separately?

## Historical Memory Still Valuable

- The original effort to explain vector search clearly instead of hiding it behind jargon.

## Not Current Runtime Truth

- old `pgvector`/IVFFlat configuration as the only valid indexing path
- old pack-based examples as the permanent data model
