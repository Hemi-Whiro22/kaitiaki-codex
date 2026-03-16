# Contributing

Purpose of rewrite:
- Preserve contribution guidance without tying it to one old frontend stack or one narrow contribution path.
- Keep this useful as a contributor contract.

Source document:
- `guides/CONTRIBUTING.md`

Rewrite posture:
- local-first
- anti-drift
- no invention

## Why Contribution Needs A Contract

Contribution should help the system grow without distorting its shape.

That means contributors need to know:
- what kinds of work are welcome
- how to make changes safely
- how to avoid architecture drift
- how review should be done

## Ways To Contribute

Valid contributions include:
- runtime code
- documentation
- tests
- language review
- cultural review
- research and curation
- accessibility and usability review
- security review

This project should not treat code as the only meaningful contribution.

## Before Changing Anything

Read the core docs first:
- structure
- quick reference
- branching
- ownership
- current contract docs where available

The goal is to understand the shape before changing it.

## Contribution Rules

### Preserve Layer Boundaries
- do not move responsibilities between layers silently
- do not collapse guardian, runtime, UI, and storage concerns together

### Preserve Pou Boundaries
- keep lane responsibilities explicit
- do not let one lane impersonate the whole system

### Preserve Language And Handling Rules
- do not flatten canonical text into folded helper forms
- do not ignore `tapu_level`
- do not promote staging material into endpoint truth without the right checks

### Keep Docs And Implementation Aligned
- if behavior changes, the docs should be updated
- if the docs define a contract, implementation should not quietly violate it

## Workflow

1. create a focused branch
2. make a coherent change
3. review it against the architecture and docs
4. test the relevant path
5. merge only when the change preserves the shape

## Review Standard

Review should ask:
- is the change understandable?
- does it preserve the system roles?
- does it keep guardian logic bounded?
- does it respect staging vs endpoint truth?
- does it preserve `pou` and `tapu_level` handling?

## Current Translation

The original document was a practical contribution guide, but it leaned heavily on one old Node/TypeScript setup and one older workflow. The durable meaning is stronger:
- contributions are welcome
- different kinds of contribution matter
- changes should be small, reviewable, and respectful of the system’s shape

This rewrite keeps that contributor contract while removing stack-specific assumptions from the core.

## Status Summary

- Keep:
  - welcoming tone
  - clear workflow
  - review and quality expectations
- Change:
  - old toolchain-specific checks into architecture-preserving contribution rules
- Drop:
  - one old stack as the implied default contribution path

## Open Questions

- Should there be separate contribution guides for docs-only, runtime, and cultural review changes?
- Which automated checks should become mandatory once this doc set is versioned in git?

## Historical Memory Still Valuable

- The original insistence that community contribution matters and should be made practical.

## Not Current Runtime Truth

- old npm/TypeScript workflow as the only contribution path
