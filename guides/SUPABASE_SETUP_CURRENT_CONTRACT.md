# Hosted Database Profile

Purpose of rewrite:
- Preserve the useful hosted-database setup guidance without treating one provider as the architecture.
- Keep this as an implementation-profile document.

Source document:
- `guides/SUPABASE_SETUP.md`

Rewrite posture:
- local-first
- anti-drift
- no invention

## What This Document Is

This is a profile-specific setup guide for using a hosted PostgreSQL-style platform with vector support.

It is not:
- the system architecture
- the required storage model
- the only supported deployment path

## Why This Profile Existed

This profile existed because it provided:
- managed PostgreSQL
- vector support
- hosted operational convenience
- a fast path for earlier implementation work

Those are still valid reasons to use such a profile, if chosen deliberately.

## What Must Still Remain True

Even on a hosted database profile:
- canonical text remains canonical
- guardian rules still apply
- staging and endpoint stores remain conceptually distinct
- provider convenience does not redefine the architecture

## Hosted Profile Responsibilities

If a hosted database profile is used, document:
- what data lives there
- what does not
- how `pou` or lane separation is represented
- how `tapu_level` is enforced or modeled
- backup/export path
- migration path away from the provider if needed

## Vector And Search Support

Hosted vector support can be useful for:
- indexing
- similarity search
- retrieval support

But the presence of vector support does not make the hosted provider the source of system meaning.

## Current Translation

The original document was a concrete provider setup guide. The durable meaning is:
- some profiles may use managed storage with vector support
- profile docs should explain how to enable and verify that setup
- hosted convenience must remain subordinate to the system contracts

This rewrite keeps the profile role while making it explicit that provider choice is optional and secondary.

## Status Summary

- Keep:
  - provider-specific setup value as a profile
  - vector/search capability guidance
- Change:
  - universal setup framing into profile-specific deployment framing
- Drop:
  - assumption that this provider defines the normal architecture

## Open Questions

- Should this file be renamed later to something like `HOSTED_POSTGRES_PROFILE.md` if the provider becomes interchangeable?
- Which hosted profile, if any, is still actively supported?

## Historical Memory Still Valuable

- The original practical explanation of enabling vector support in a managed PostgreSQL environment.

## Not Current Runtime Truth

- hosted provider as the core architecture
- old packs/supabase schema as the universal data model
