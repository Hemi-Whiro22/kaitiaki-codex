# Self-Hosting

Purpose of rewrite:
- Preserve the self-hosting intent without tying it to one old Docker/Postgres setup.
- Keep this useful as a deployment-profile guide.

Source document:
- `guides/SELF_HOSTING.md`

Rewrite posture:
- local-first
- anti-drift
- no invention

## Why Self-Hosting Matters

Self-hosting matters because it supports:
- local-first operation
- data sovereignty
- reduced vendor lock-in
- community and organizational control

This remains one of the strongest enduring intentions in the project.

## What A Self-Hosted Profile Must Provide

A self-hosted profile should provide:
- runtime services
- guardian enforcement
- shared staging storage
- endpoint storage for the lanes in use
- optional indexing/search services if required
- a usable interaction surface

## Self-Hosting Is A Profile

Self-hosting is not the whole architecture.
It is one deployment profile.

That means:
- the exact container, VM, process manager, or database can vary
- the core contracts must remain the same

## Minimum Self-Hosted Guarantees

A self-hosted profile should ensure:
- data remains under operator control
- guardian rules still apply
- staging and endpoint stores remain distinct
- local models or local runtime remain possible where the profile supports them

## Deployment Choices

Different self-hosted setups may use:
- direct local process execution
- containers
- a dev container
- a VPS
- a private server
- orchestration later if scale demands it

These are deployment mechanics, not the architecture itself.

## Operational Checklist

Before treating a self-hosted profile as healthy, confirm:
- runtime services are reachable
- guardian checks are active
- staging works
- endpoint promotion works only after clearance
- lane data is stored in the correct destination
- backups and restore paths are understood

## Data And Backup Expectations

Self-hosting should preserve the ability to:
- inspect staged data
- back up endpoint stores
- restore from backup
- export or migrate where necessary

The exact storage engine can vary by profile.

## Current Translation

The original document strongly promoted sovereignty and self-hosting, which remains valuable. What changed is that one Docker/Postgres/Supabase migration path should no longer be treated as the universal self-hosting model.

This rewrite keeps the self-hosting purpose while making the deployment guidance portable.

## Status Summary

- Keep:
  - sovereignty emphasis
  - self-hosting as a first-class option
  - backup and operational thinking
- Change:
  - old setup commands into profile-specific examples
  - provider migration language into broader deployment profile language
- Drop:
  - one old Docker stack as the implied normal deployment

## Open Questions

- Which self-hosted profile should be documented first as the current recommended path?
- Should there be separate runbooks for local dev, private server, and larger self-hosted deployment?

## Historical Memory Still Valuable

- The original strong stance against vendor lock-in.

## Not Current Runtime Truth

- old Supabase-to-local migration path as universal deployment guidance
- old Docker/PostgreSQL example as the only self-hosted model
