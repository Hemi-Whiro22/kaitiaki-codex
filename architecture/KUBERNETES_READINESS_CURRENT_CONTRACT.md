# Scaling And Orchestration Readiness

Purpose of rewrite:
- Preserve the scaling-readiness thinking without tying the architecture to Kubernetes or one old capacity model.
- Keep this as a scaling-profile document.

Source document:
- `architecture/KUBERNETES_READINESS.md`

Rewrite posture:
- local-first
- anti-drift
- no invention

## What This Document Is

This document is about readiness for larger-scale orchestration.

It is not:
- proof that the system requires Kubernetes
- a statement that the current architecture is cloud-first
- the definition of the core system

## Durable Meaning

The original document was useful because it asked:
- when does single-host stop being enough?
- what changes when scale arrives?
- how do we move without losing the shape?

Those are still the right questions.

## Scaling Triggers

Scaling or orchestration should be considered when:
- concurrent usage grows beyond the comfort of the current profile
- operational downtime becomes unacceptable
- one host becomes a bottleneck for runtime, indexing, or storage
- backup, recovery, or resilience expectations increase

The trigger is not fashion.
The trigger is operational need.

## What Must Survive Scaling

If the system scales out, these must still remain true:
- Kaitiaki remains the guardian
- `pou` boundaries remain explicit
- `tapu_level` remains a real handling boundary
- staging and endpoint truth remain distinct
- scaling convenience does not redefine system ownership

## Possible Scaling Profiles

Future scaling profiles might use:
- multiple service processes
- container orchestration
- replicated databases
- separate indexing nodes
- regional failover

These are operational profiles, not architectural replacements.

## Cost And Complexity Warning

Large-scale orchestration increases:
- operational overhead
- complexity
- observability needs
- deployment discipline requirements

That means it should be chosen only when the simpler profiles no longer fit.

## Current Translation

The original document contained a detailed Kubernetes migration and sizing plan for one older deployment shape. The durable value was the readiness thinking:
- know when to scale
- know what scaling changes
- avoid premature complexity

This rewrite keeps that value while removing Kubernetes as an implied destination requirement.

## Status Summary

- Keep:
  - scaling-readiness thinking
  - migration trigger awareness
  - caution against premature complexity
- Change:
  - Kubernetes-specific plan into a broader scaling-profile contract
- Drop:
  - old resource and user-count projections as permanent truth
  - Kubernetes as the implied end-state architecture

## Open Questions

- Which scale indicators should the project actually track in practice?
- Should there be a separate current scaling profile document only if and when the live system needs it?

## Historical Memory Still Valuable

- The original effort to think ahead without immediately forcing the system into unnecessary orchestration.

## Not Current Runtime Truth

- old k8s resource model and user thresholds as current capacity truth
- Kubernetes as a required architectural destination
