# Operational Infrastructure

Purpose of rewrite:
- Preserve the operational integration intent without locking it to one old session summary or one provider-backed backend plan.
- Keep this as an operations and service-integration document.

Source document:
- `architecture/OPERATIONAL_INFRASTRUCTURE.md`

Rewrite posture:
- local-first
- anti-drift
- no invention

## What Operational Infrastructure Covers

Operational infrastructure covers:
- runtime integration
- operational visibility
- persistent system memory where appropriate
- configuration handling
- administrative or operator surfaces
- backup and audit support

It should describe how the system operates, not just what one session built.

## Durable Operational Concerns

### Session And Message Continuity
- interaction history may need persistence
- relational memory must remain in the correct lane
- continuity should not silently become public truth

### Configuration Management
- runtime configuration should be visible and reviewable
- version history can be useful
- config storage should not become a hidden control surface

### Operator Visibility
- admins/operators may need health, logs, backups, and audit views
- those views must remain bounded by role and handling rules

### Auditability
- important changes should be traceable
- protected operations should leave accountable traces where appropriate

## Relationship To Kaitiaki

Operational infrastructure does not replace the guardian.

It supports the guardian by making it possible to:
- observe what happened
- inspect runtime state
- back up or recover
- manage configuration responsibly

## Storage Considerations

Operational data may include:
- session history
- audit records
- config versions
- backup metadata
- runtime health indicators

These must still respect:
- lane ownership
- `tapu_level`
- staging vs endpoint truth

## Current Translation

The original document mixed:
- new router/session work
- old backend session-summary detail
- provider-specific table and endpoint planning
- scaling notes

The lasting meaning is:
- operational visibility matters
- continuity and audit matter
- config and admin surfaces should be deliberate, not ad hoc

This rewrite keeps that operational meaning while removing old implementation counts and session-specific delivery framing from the core.

## Status Summary

- Keep:
  - operational visibility
  - continuity/audit thinking
  - config management as a real concern
- Change:
  - old router/session report into a portable operational infrastructure contract
- Drop:
  - session-delivery framing
  - old provider-specific migration tables as core truth

## Open Questions

- Which operational data belongs in `whakapapa` versus a separate ops/admin store?
- Should operator-facing docs be split from service-integration docs?

## Historical Memory Still Valuable

- The original push to make operations visible instead of implicit.

## Not Current Runtime Truth

- old router counts/endpoints as the permanent ops shape
- old Supabase-specific migration flow as universal operational infrastructure
