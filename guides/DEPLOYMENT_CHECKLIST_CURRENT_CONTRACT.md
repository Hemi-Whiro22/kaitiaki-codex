# Deployment Checklist

Purpose of rewrite:
- Preserve a useful deployment checklist without locking it to one old backend stack or phase plan.
- Keep this as a portable operational readiness document.

Source document:
- `guides/DEPLOYMENT_CHECKLIST.md`

Rewrite posture:
- local-first
- anti-drift
- no invention

## What This Checklist Is For

This checklist exists to confirm a profile is operationally trustworthy before wider use.

It is not:
- a dated progress report
- a permanent backlog snapshot
- proof that one old implementation is the architecture

## Core Readiness Categories

### Runtime Readiness
- backend/runtime services start cleanly
- health checks are available
- logs are readable enough to debug failures
- required dependencies for the chosen profile are documented

### Guardian Readiness
- lane validation works
- `tapu_level` rules are enforced
- blocked actions are refused clearly
- promotion from staging requires clearance

### Storage Readiness
- shared staging is reachable
- endpoint stores exist for the lanes in use
- backup and restore paths are understood
- staging and endpoint truth remain distinct

### Service Readiness
- lane-specific services respond for the capabilities the profile claims to provide
- unsupported services are explicit, not silently faked

### Interaction Readiness
- the chosen UI/client can connect to the runtime
- key user flows succeed through the correct lanes

## Minimum Deployment Checks

Before calling a profile deployable, confirm:

- health checks pass
- guardian checks pass
- a staged record can be created
- an uncleared record cannot be promoted
- a cleared record can be promoted to the correct lane
- lane retrieval reads from the correct destination
- the interaction surface can perform at least one core flow end to end

## Lane-Specific Validation

Depending on the active profile, check the lanes that are claimed to be live:

### Whakapapa
- relational notes can be written and recalled correctly

### Tikanga
- reviewed language lookup returns from trusted lane data only

### Taonga / Intake
- staged material enters shared staging with provenance

### Whakairo
- build/change work lands in the correct runtime or store

### Rongo
- sensing/OCR or capture paths write through the proper intake route

## Security And Protection Checks

Confirm:
- no secrets are committed
- access posture is documented
- sensitive or restricted material is not exposed through open flows
- guardian rules are applied consistently

## Current Translation

The original document mixed:
- a backend phase plan
- a feature backlog
- a deployment checklist
- old stack-specific tasks

The durable part is the operational mindset:
- prove readiness
- check the real path
- know what is missing
- do not confuse “implemented in theory” with “safe to run”

This rewrite keeps that deployment usefulness while removing old phase/status framing from the core.

## Status Summary

- Keep:
  - checklist form
  - readiness thinking
  - emphasis on testing the real path
- Change:
  - old phase plan into portable readiness categories
- Drop:
  - dated time estimates
  - old provider/service backlog as if permanent roadmap

## Open Questions

- Which readiness checks should be mandatory for every profile?
- Should there be one profile-specific deployment checklist per implementation later?

## Historical Memory Still Valuable

- The original drive to turn abstract backend work into something operationally testable.

## Not Current Runtime Truth

- old Supabase/FastAPI-specific task plan as universal deployment truth
- old completion markers and hour estimates
