# Kaitiaki SDK Vision

Purpose of rewrite:
- Preserve the portable system vision without tying it to one stack or one exaggerated implementation claim.
- Keep this as a vision-and-capability document.

Source document:
- `guides/KAITIAKI_SDK_VISION.md`

Rewrite posture:
- local-first
- anti-drift
- no invention

## Vision

Kaitiaki should be portable.

That means the system can be carried across different implementation profiles while keeping the same core intent:
- guardian-led
- memory-aware
- lane-aware by `pou`
- culturally grounded
- local-first by default
- capable of learning through structured recall, not uncontrolled drift

## What Portability Means Here

The system should be able to run through different profiles:
- local Python/Node/local-model profile
- API-driven profile
- self-hosted profile
- lightweight embedded/client profile

What must remain stable across them:
- guardian behavior
- staging before endpoint truth
- relational memory in the correct lane
- `pou` boundaries
- `tapu_level`
- culturally grounded handling

## Seed Knowledge And Foundational Memory

The original document emphasized seeded knowledge and a grounded starting point.
That idea still matters.

When a profile spins up, it may include:
- foundational reo concepts
- relational context
- environmental or community knowledge
- governance or mission context

But seeded knowledge should be treated as:
- explicit
- reviewable
- attributable
- replaceable by profile

Not as hidden ideology embedded invisibly into the runtime.

## Memory Model

The durable vision is not “consciousness” in a mystical or agentic sense.
It is:
- persistent memory
- relational recall
- accumulating context
- grounded response through prior knowledge and current constraints

The memory lane belongs to `whakapapa`.

That means:
- summaries
- research notes
- prior interactions
- relational links
- evolving understanding

can accumulate there without pretending to be reviewed public truth.

## Spiral / Koru Model

The original koru metaphor is still useful if kept disciplined.

It means:
- the system can revisit knowledge with more context
- earlier encounters are not discarded
- understanding can deepen over time
- later recall can carry relational depth

It does not mean:
- uncontrolled self-evolution
- hidden autonomous belief formation
- bypassing human review

## SDK Shape

A portable Kaitiaki SDK or framework should expose stable capabilities:

### Guardian Interface
- validate an action
- route to the right lane
- block what is not allowed
- promote only what is cleared

### Memory Interface
- write relational notes
- retrieve prior context
- maintain provenance and handling posture

### Intake Interface
- stage new material
- run cleanup/extraction/indexing through the current profile

### Service Interface
- translation lane
- research lane
- build/change lane
- sensing/intake lane

### Interaction Interface
- attach to UI, CLI, or another client surface

## Te Reo And Language Integrity

The original document rightly emphasized:
- macrons
- proper UTF-8 handling
- reo as sovereignty

That remains current.

The durable rule is:
- preserve canonical text faithfully
- use folded or search-helper representations only for access and indexing
- never replace the original form with the folded form

## Current Translation

The original document carried a strong ambitious vision. The stable meaning inside it is not that one older stack had already “built all of it,” but that the project intended:
- portable deployment
- guarded memory
- cultural grounding
- relational recall
- seeded contextual understanding

This rewrite keeps that vision while stripping old implementation certainty and stack lock-in.

## Status Summary

- Keep:
  - portability
  - memory depth
  - cultural grounding
  - koru/spiral as a disciplined knowledge metaphor
- Change:
  - “consciousness” language into structured memory and recall language
  - old SDK examples into portable capability contracts
- Drop:
  - exaggerated build-complete claims
  - framework-specific deployment examples as if universal

## Open Questions

- Should the portable framework call itself `Kaitiaki SDK`, `Kaitiaki Framework`, or both?
- Which seed knowledge sets should be considered canonical versus profile-specific?

## Historical Memory Still Valuable

- The original insistence that Kaitiaki should remember, deepen, and stay culturally grounded.

## Not Current Runtime Truth

- old stack-specific SDK examples
- claims that every layer was already fully built
