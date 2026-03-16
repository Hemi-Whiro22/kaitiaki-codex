# Production Setup

Purpose of rewrite:
- Preserve production setup intent without tying it to one old stack or claiming readiness by default.
- Keep this as a profile-aware operations guide.

Source document:
- `guides/PRODUCTION_SETUP.md`

Rewrite posture:
- local-first
- anti-drift
- no invention

## What Production Means Here

Production does not mean:
- one framework stack
- one database choice
- one deployment provider

Production means:
- the chosen profile is stable enough to run for real work
- the guardian is enforcing boundaries
- storage and recovery are understood
- operational risks are visible

## Production Requirements

A production-capable profile should define:
- runtime services
- guardian enforcement
- storage layout
- backup and restore
- logging and operational visibility
- access/security posture

## Minimum Production Conditions

Before treating a profile as production-ready, confirm:

- health and readiness checks are available
- guardian lane and `tapu_level` rules are active
- secrets handling is documented
- staging and endpoint stores are backed up appropriately
- restore has been tested or at least dry-run documented
- unsupported features are clearly marked

## Profile-Specific Setup

Production setup will vary by profile.

Examples of profile variables:
- Python or Node runtime mix
- local or remote models
- local database or hosted database
- containerized or direct process execution
- reverse proxy, firewall, and TLS strategy

These belong in profile-specific appendices or companion docs.

## Security Expectations

At minimum, a production profile should define:
- secret handling
- authentication/authorization where applicable
- network exposure
- auditability for important actions
- restricted handling for protected lanes

## Operational Visibility

A production profile should make it possible to answer:
- is it up?
- is guardian enforcement working?
- what failed?
- what lane is affected?
- can we recover?

## Git And Version Control

Version control is part of production discipline.

That means:
- keep docs and implementation reviewable
- do not commit secrets
- tag stable releases or milestones where useful
- preserve the history of meaningful architectural changes

## Current Translation

The original document was a broad setup guide for one old implementation and mixed local dev, deployment, security, and git onboarding into one document. The durable meaning is:
- production requires discipline
- operational readiness should be explicit
- version control and deployment posture matter

This rewrite keeps that usefulness while removing the old stack as the implied permanent production shape.

## Status Summary

- Keep:
  - practical setup mindset
  - deployment discipline
  - emphasis on security and version control
- Change:
  - old setup commands into profile-aware production requirements
- Drop:
  - “everything is ready” framing
  - one stack/provider list as the production contract

## Open Questions

- Which production profile should be documented first as the live example?
- Should production runbooks live separately from general setup docs?

## Historical Memory Still Valuable

- The original insistence that setup should be understandable and repeatable.

## Not Current Runtime Truth

- old FastAPI/React/Postgres/Redis stack as universal production setup
- old “ready” checklists as permanent truth
