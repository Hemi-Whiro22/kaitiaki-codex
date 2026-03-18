# Branching

Purpose of rewrite:
- Preserve a clear branching workflow without tying it to one momentary implementation setup.
- Keep this practical and light.

Source document:
- `BRANCHING.md`

Rewrite posture:
- local-first
- anti-drift
- no invention

## Branching Strategy

Use a lightweight branching model that keeps the documentation and implementation reviewable.

### Main
- always the trusted integration branch
- should stay readable and recoverable

### Feature Branches
- use for focused changes
- one concern per branch where practical

Recommended examples:
- `feature/<short-description>`
- `docs/<short-description>`
- `chore/<short-description>`
- `fix/<short-description>`

### Release Branches
- optional
- only needed if a profile or deployment flow benefits from them

## Recommended Workflow

1. Create a focused branch from `main`.
2. Make small, coherent changes.
3. Review against the docs/contracts, not just whether the code runs.
4. Merge back into `main` when the change preserves the system shape.
5. Delete the branch after merge if it is no longer needed.

## What Review Must Check

Before merging, confirm:
- the change did not move responsibilities between layers without saying so
- the guardian did not become smarter than intended
- staging and endpoint storage are still distinct
- `pou` boundaries still hold
- docs still match the implementation

## Version Control Guidance

Because the docs are meant to become an architecture source:
- version the docs alongside meaningful changes
- avoid rewriting history to hide drift
- keep branch names and commit messages readable

If the docs later become their own repo:
- the same branching rules still apply
- implementation repos should align back to the docs, not silently diverge from them

## Current Translation

The original document already had the right instinct: keep branching simple and readable. This rewrite keeps that function while making the review standard stronger so branches are judged against architectural fidelity, not just passing builds.

## Status Summary

- Keep:
  - lightweight workflow
  - protected `main`
  - focused branches
- Change:
  - review criteria so architecture drift is part of merge decisions
- Drop:
  - implementation-only framing

## Open Questions

- Should doc-only changes require the same review standard as runtime changes?
- Should there be a dedicated branch naming pattern for profile-specific implementation work?

## Historical Memory Still Valuable

- The original preference for simple workflows over bureaucratic branching.

## Not Current Runtime Truth

- none in a major way; the old document was already relatively portable
