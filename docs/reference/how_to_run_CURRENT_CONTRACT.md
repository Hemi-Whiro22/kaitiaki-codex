# How To Run

Purpose of rewrite:
- Turn the old status-heavy run guide into a durable run contract.
- Keep it usable without tying it to one old stack.
- Remove completion language and stale operational claims.

Source document:
- `how_to_run.md`

Rewrite posture:
- local-first
- anti-drift
- no invention

## Running The System

The system should be runnable through a chosen implementation profile, but every profile must satisfy the same core flow:

1. Start the backend runtime.
2. Start the interaction surface.
3. Ensure shared staging storage is available.
4. Ensure endpoint storage is available for the lanes in use.
5. Start optional supporting services only if the profile requires them.
6. Confirm the guardian is enforcing `pou` and `tapu_level`.

## Minimum Local-First Run Conditions

Before calling a setup “running,” confirm:

- the guardian is reachable
- the backend runtime can answer health requests
- the interaction surface can connect to the runtime
- staging accepts new records
- endpoint promotion is blocked until clearance conditions are met
- lane-specific reads come from the correct destination store

## Required Capabilities

A working profile should support these basic operations:

### Interaction
- submit a request through a UI, terminal, or client
- receive an answer or refusal
- see which lane or posture applied if the profile exposes that

### Guardian
- accept or reject structured actions
- enforce lane boundaries
- enforce `tapu_level`
- prevent unsafe promotion

### Staging
- receive intake
- hold extracted or processing state
- keep provenance and review metadata

### Endpoint Lanes
- accept promoted records only after clearance
- serve trusted lane data back to the interaction layer or services

## Suggested Run Sequence

### Step 1: Start Mauri And Config
- load the current contracts and runtime config
- confirm the active implementation profile

### Step 2: Start Runtime Services
- start backend services needed for the lanes in use
- start indexing or semantic retrieval services only if required by the profile

### Step 3: Start Kaitiaki
- bring up guardian validation and routing
- confirm policy rules are loaded

### Step 4: Start Whenua
- run the chosen interaction surface
- connect it to the guardian/runtime

### Step 5: Validate The Core Flow
- stage a record
- confirm the record remains in staging until cleared
- promote a cleared record to the correct lane
- confirm reads come from the correct destination store

## Portable Smoke Tests

Any implementation should be able to answer these tests:

### Guardian Test
- allowed action to allowed lane succeeds
- disallowed action to disallowed lane is blocked

### Staging Test
- new intake lands in shared staging
- provenance and handling metadata are preserved

### Promotion Test
- uncleared material cannot be promoted
- cleared material lands in the correct endpoint store

### Retrieval Test
- trusted lane data can be recalled from the correct lane
- staging data is not mistaken for endpoint truth

## Current Implementation Example

A current profile may use:
- Python backend services
- Node-based interaction runtime
- local models
- optional dev containers
- local databases

If that profile is used, add the exact commands in a profile-specific appendix or companion document.

## What This Document Does Not Assume

This run guide does not assume:
- one frontend framework
- one backend framework
- one model provider
- one database engine
- one deployment target

Those are profile details, not the core run contract.

## Current Translation

The original document mixed:
- test results
- setup shortcuts
- old service endpoints
- stack-specific claims
- “complete/ready” status language

The current version keeps the useful purpose:
- how to think about bringing the system up
- what “running” must actually mean
- what must be validated before trusting it

## Status Summary

- Keep:
  - the practical startup focus
  - the operational testing mindset
  - the desire for a short path to “it works”
- Change:
  - stack-specific service lists into profile examples
  - completion claims into concrete validation steps
- Drop:
  - “production ready” language
  - provider-specific assumptions as core system truth

## Open Questions

- Should there be one dedicated `RUN_PROFILE_LOCAL.md` documenting the current Python/Node/local-model implementation?
- Which smoke tests should be treated as mandatory before accepting any future profile?

## Historical Memory Still Valuable

- The original document’s emphasis on testing routes and proving that core flows actually work.

## Not Current Runtime Truth

- old service endpoint list as universal architecture
- old credentials and devcontainer-only setup path
- “all tested” and “production ready” status claims
