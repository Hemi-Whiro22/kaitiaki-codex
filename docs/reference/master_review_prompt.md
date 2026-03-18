Review this document for anti-drift translation into the current Kaitiaki architecture.

Rules:
- Do not edit or overwrite the original document.
- Create a new rewritten document beside it.
- Preserve the original meaning where it still fits.
- Strip or replace stale mechanics that no longer fit the current system.
- Do not invent missing architecture, services, or rules.
- If something is unclear, mark it as uncertain instead of guessing.
- Preserve useful architectural meaning even if implementation details changed.

Core system assumptions:
- local-first is the default posture
- guardian/kaitiaki validates and routes; it is not a reasoning engine
- `pou` boundaries matter
- `tapu_level` is a real handling boundary
- shared staging comes before endpoint storage
- UI/model/provider/framework are replaceable edges, not the core system
- the documents should remain portable across different implementation stacks

Use role/realm language first:
- meta/contracts/config
- backend runtime/guardian/services
- interaction surfaces
- storage/staging/endpoint data
Only mention current repo mappings as a secondary implementation example when useful.

For each major section in the document, include:
- Original summary
- Current translation
- Status: Keep / Change / Drop
- Reason

At the top of the new document include:
- Purpose of the rewrite
- Source document path
- Rewrite posture: local-first / anti-drift / no invention

At the end include:
- Open questions
- Items still valuable as historical memory
- Items that should not be treated as current runtime truth

Naming:
- Name the new file something clear like:
  - `<original_name>_LOCAL_FIRST.md`
  - or `<original_name>_CURRENT_CONTRACT.md`

Additional anti-drift rules:
- The rewritten document must remain useful as a standalone working document, not just a commentary layer.
- Do not replace operational content with disclaimers or references to other docs unless absolutely necessary.
- Preserve the original document's function:
  - if it was a guide, rewrite it as a guide
  - if it was a contract, rewrite it as a contract
  - if it was a summary, rewrite it as a useful summary
- Prefer stable roles and responsibilities over framework names.
- Do not lock the rewrite to one framework, provider, port layout, or deployment mode unless the document is explicitly an implementation profile.
- If implementation details are still useful, place them under a clearly marked section such as:
  - `Current Implementation Example`
  - `Historical Implementation Example`
  - `Deployment Profile`
- The goal is to produce architecture-source documents that can support multiple implementations later.

Do the rewrite conservatively.
When in doubt, preserve meaning, preserve usefulness, and flag mechanics for review.
