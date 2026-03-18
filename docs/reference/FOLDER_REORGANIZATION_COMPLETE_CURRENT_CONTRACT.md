# Folder Reorganization

Purpose of rewrite:
- Preserve the useful structure lessons without freezing one old folder reorganization as permanent truth.
- Convert this into a role-based structure note.

Source document:
- `FOLDER_REORGANIZATION_COMPLETE.md`

Rewrite posture:
- local-first
- anti-drift
- no invention

## What This Document Means Now

The important outcome of any reorganization is not the exact folder names.
It is that the system remains clearly separated by role and ownership.

## Reorganization Goals

A good structure should make these things obvious:

- where system meaning lives
- where guardian behavior lives
- where runtime logic lives
- where intake and indexing live
- where interaction lives
- where storage lives

If those are clear, the exact folder names can evolve without breaking the architecture.

## Stable Structural Rules

### Meta And Contracts
- keep structure rules, ownership, schemas, governance, and intent together
- this is the Mauri layer

### Guardian
- keep validation, routing, protection, and promotion rules together
- this is the Kaitiaki layer

### Runtime Services
- keep backend execution logic with the services or lanes that own it

### Intake And Indexing
- keep cleanup, chunking, vector/index work, and retrieval preparation together

### Interaction
- keep UI/client surfaces separate from runtime logic

### Storage
- keep shared staging distinct from endpoint lane storage

## What A Good Reorganization Should Avoid

- mixing runtime code with contracts
- mixing raw intake with accepted lane truth
- mixing UI behavior with guardian enforcement
- renaming roles in ways that change responsibility without saying so
- tying the structure to one framework or container setup

## Development Containers

A dev container may still be useful as part of a current implementation profile.

Its role is:
- reproducible local setup
- shared environment during carving
- packaging the current implementation profile

Its role is not:
- defining the core architecture

## Current Translation

The original document celebrated one specific reorganization. The durable meaning inside it was stronger than the exact folder map:
- reduce chaos
- make navigation clearer
- separate roles
- support both full-system and focused development

This rewrite keeps that structural intent while removing old status language and old stack assumptions.

## Status Summary

- Keep:
  - the push for clarity
  - the separation of major work areas
  - the idea that structure should reduce cognitive load
- Change:
  - exact old folder moves into general structural rules
  - dev-container details into profile-specific usage
- Drop:
  - “complete” framing as if one reorganization finished the architecture permanently

## Open Questions

- Which Maori realm names should become the canonical portable structure headings?
- Should there be one dedicated document mapping current folder names to portable system roles?

## Historical Memory Still Valuable

- The original effort to stop root-folder chaos.
- The instinct to colocate related materials for easier navigation.

## Not Current Runtime Truth

- old `pack-dashboard` reorganization as a final structure
- old container paths as the permanent architecture
