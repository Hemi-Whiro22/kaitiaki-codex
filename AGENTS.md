# Kaitiaki Codex Agent Contract

This file is the operating contract for agents working in `kaitiaki-codex`.

It exists to reduce drift, repeated reminders, and weak defaults.

## Core Intent

This repo should help carve and maintain local-first systems without redefining the upstream contract casually.

Agents should:
- preserve local-first posture
- preserve explicit contracts
- prefer structure over improvisation
- prefer verification over assumption

## Repo Role

`kaitiaki-codex` is a downstream coder/dev repo.

It is for:
- coding
- testing
- local-first runtime carving
- profile and tooling work
- implementation of contract-aligned projects

It is not for:
- casually replacing upstream meaning
- collapsing projects into one blur
- skipping documentation because the code “already explains it”

## Projects Folder Rule

`projects/` is active working ground.

Agents should treat it as:
- projects currently being carved
- projects under verification
- projects not yet hardened enough to stand fully alone

It should not be treated as a permanent dumping ground.

When a project becomes hardened and genuinely standalone, it may later be moved out of `projects/`
into a clearer home-level location if that better preserves its boundary.

## Default Working Rules

Unless the user explicitly overrides this, agents should:
- inspect the project contract before major changes
- look for `manifest.yaml`, `TODO_AUTONOMOUS.md`, `README.md`, and repo/root `AGENTS.md` first
- write the next phase down when the work meaningfully changes shape
- update the phase ledger after a completed phase
- run tests after each substantive phase or structural change
- report clearly what was tested and what was not
- prefer API or curl verification before UI convenience
- keep TODO/manifest/docs aligned with the real code state

## Contract Precedence

When multiple docs exist, use this precedence order:

1. repo `AGENTS.md`
2. project-local `manifest.yaml`
3. project-local `TODO_AUTONOMOUS.md`
4. project-local `README.md`
5. profile manifests for environment/profile concerns only
6. `docs/reference/` as transparent reference and historical memory

Reference docs are useful, but they should not silently override the active working contract.

## Phase Rule

If a project has a phase ledger such as `TODO_AUTONOMOUS.md`, treat it as a living contract.

Agents should:
- not skip ahead casually
- not overbuild beyond the current phase without reason
- add a new phase before or with implementation if the current list is no longer enough
- keep completed phases visible instead of deleting them

## Standalone Service Rule

If a project is intended to be standalone, agents must preserve that shape.

For standalone services:
- the only in and out is through the controlled HTTP API
- other projects should not import internal modules directly
- UI should use the same HTTP routes as other consumers
- there should be no hidden UI-only storage path
- internal tables may grow, but the external door should stay singular and clear

## Database/Substrate Rule

When a project is a substrate or database:
- raw data save and trace come first
- UUID identity is stable
- provenance remains attached
- review state and lineage are explicit
- storage truth should not be delegated to AI
- promotion/review logic must remain intentional

Agents should not:
- split data into a new database per feature by default
- casually add service-specific schema to the core model
- weaken handling boundaries because a shortcut seems easier

## Testing Rule

Testing is not optional cleanup.

Agents should:
- run the relevant tests after substantive changes
- add tests when a new structural capability is introduced
- prefer end-to-end verification where practical
- state the exact result, for example:
  - `41 passed`

If tests cannot be run, agents must say so plainly.

## Contract Update Rule

When a structural change lands, agents should update the relevant contract surface:
- `AGENTS.md`
- `manifest.yaml`
- `README.md`
- `TODO_AUTONOMOUS.md`

This is required when the change affects:
- boundaries
- defaults
- storage model
- API shape
- project posture

## Safety Rule

Agents must not run destructive commands casually.

Do not:
- remove ignored/local state blindly
- run destructive git cleanup/reset commands without explicit user approval
- treat git as a recovery strategy for local databases

When local data is involved, prefer:
- backup
- export
- explicit local artifact rules

## Agent Quality-of-Life Rule

Agent-specific tooling is allowed when it reduces repeated burden and stays outside the substrate/runtime boundary.

Good examples:
- fixture sets
- launch scripts
- bootstrap helpers
- test harnesses
- audit/check scripts
- contract templates
- phase ledgers
- project recall helpers
- verification aggregators
- codex-only notes lanes

These should:
- help the agent and user work more clearly
- remain distinct from the runtime/database unless intentionally promoted
- not become hidden dependencies for unrelated services

## Communication Rule

Agents should act like a trusted co-dev:
- implement the user’s intent faithfully
- challenge drift, not the user
- be explicit about assumptions
- keep answers concise and high-signal

The goal is not just to code.
The goal is to hold shape reliably enough that the user does not have to keep restating the same architecture every few days.
