# Ownership

Purpose of rewrite:
- Preserve ownership, sovereignty, and responsibility boundaries without tying them to one old licensing or hosting arrangement.
- Keep this as a trust and ownership contract.

Source document:
- `technical/OWNERSHIP.md`

Rewrite posture:
- local-first
- anti-drift
- no invention

## Why Ownership Matters

Ownership here is not just legal.
It is also about:
- data sovereignty
- cultural responsibility
- implementation control
- transparency about dependencies

The system should make it clear:
- what belongs to the project
- what comes from third parties
- what remains the user’s or community’s data
- what obligations attach to use or modification

## Ownership Boundaries

### Project-Owned Material

Project-owned material may include:
- original code
- original service logic
- original data schemas
- original docs and contracts
- original indexing or guardian logic
- original curation and review structures

The exact implementation files may vary by profile.

### Third-Party Dependencies

Third-party dependencies remain third-party, even when integrated deeply.
Examples may include:
- databases
- runtimes
- vector/search libraries
- frontend frameworks
- hosting or identity providers

These should always be documented clearly so no one confuses a dependency with the project’s original contribution.

### User Or Community Data

User, whānau, community, or organizational data should be treated as theirs.

The system may process or store it according to the chosen profile, but the architecture should presume:
- user/community data is not automatically the project’s asset
- guardian and handling rules exist to protect that data
- exportability and local control should be preserved where possible

## Sovereignty Principles

The strongest enduring parts of the original document are:
- keep data sovereignty visible
- keep dependencies explicit
- avoid hidden extraction
- avoid quiet corporate free-riding on community work

Those principles remain useful even if the exact license or commercial model changes over time.

## Dependency Clarity

A good ownership document should answer:
- what is original
- what is integrated
- what license obligations apply
- what the project expects from contributors or adopters

It should not bury major dependencies or confuse convenience tooling with core architecture.

## Local-First Implication

Under a local-first posture:
- storage should default closer to the user or operator
- model/provider choices should remain replaceable
- data should not be assumed to leave local control unless a chosen profile says so explicitly

## Current Translation

The original document strongly mixed:
- ownership explanation
- licensing details
- commercialization logic
- Supabase-specific hosting assumptions

The durable meaning was stronger:
- be explicit about what is original
- be honest about what is borrowed
- protect user/community sovereignty
- explain obligations clearly

This rewrite keeps that contract while removing outdated provider-specific framing from the core.

## Status Summary

- Keep:
  - sovereignty language
  - dependency transparency
  - clear boundary between original work and third-party tools
- Change:
  - host/provider-specific storage assumptions into profile-specific details
  - one licensing model into durable ownership principles
- Drop:
  - treating one provider setup as the normal ownership boundary

## Open Questions

- Should licensing and ownership remain in one document or split into `OWNERSHIP.md` and `LICENSING.md`?
- Which parts of the commercial/free-tier model still belong in the active canonical docs?

## Historical Memory Still Valuable

- The original insistence that sovereignty and ownership must be stated plainly.

## Not Current Runtime Truth

- old Supabase-specific storage framing as universal system behavior
- old threshold-based commercial examples as fixed permanent policy
