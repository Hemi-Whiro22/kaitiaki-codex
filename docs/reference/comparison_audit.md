# Comparison Audit

Purpose:
- compare original docs against the current-contract versions
- verify intent preservation
- identify where anti-drift succeeded
- identify where usefulness was weakened by over-correction

Scope:
- canonical original/current-contract pairs in `kaitiaki-framework-101`
- excludes `lineage/`
- excludes legacy-only archived files

## Overall Judgment

The audit result is strong.

What clearly worked:
- architecture/source intent was preserved across the corpus
- framework, provider, and mode lock-in were removed successfully
- kaupapa, `pou`, `tapu_level`, guardian/staging/endpoint distinctions, and local-first posture survive clearly
- governance, sovereignty, ownership, and transparency docs are materially stronger and cleaner now

What still needs attention:
- several operational guides became too abstract after the anti-drift pass
- the main failure mode is not intent loss, but **operational thinning**
- the fix is not another rewrite cycle from scratch
- the fix is targeted additions of **profile-specific appendices** to restore practical usefulness

## Highest-Signal Findings

### 1. Intent Preserved Best

The strongest rewrites are:
- `STRUCTURE_GUIDE_CURRENT_CONTRACT.md`
- `architecture/ARCHITECTURE_CURRENT_CONTRACT.md`
- `guides/TE_REO_WORKFLOW_CURRENT_CONTRACT.md`
- `technical/OWNERSHIP_CURRENT_CONTRACT.md`
- `technical/KAITIAKI_SEED_GUIDE_CURRENT_CONTRACT.md`
- `phase-summaries/WHAKAPAPA_REUNIFICATION_CURRENT_CONTRACT.md`

Why:
- they preserve kaupapa clearly
- they remain useful as standalone docs
- they carry the evolved local-first frame without becoming vague

### 2. Main Weakness: Over-Correction Into Abstraction

The docs most affected by over-correction are:
- `QUICK_REFERENCE_CURRENT_CONTRACT.md`
- `how_to_run_CURRENT_CONTRACT.md`
- `guides/DEPLOYMENT_CHECKLIST_CURRENT_CONTRACT.md`
- `guides/PRODUCTION_SETUP_CURRENT_CONTRACT.md`
- `guides/QUICK_START_PHASE_6_CURRENT_CONTRACT.md`
- `technical/FASTAPI_COMPLETE_CURRENT_CONTRACT.md`
- `technical/FRONTEND_BACKEND_INTEGRATION_CURRENT_CONTRACT.md`
- `technical/VECTOR_INDEX_GUIDE_CURRENT_CONTRACT.md`
- `architecture/OPERATIONAL_INFRASTRUCTURE_CURRENT_CONTRACT.md`

Why:
- they now preserve the architecture correctly
- but they lost too much of the “show me how this works today” utility

These do **not** need structural rewriting again.
They need:
- one concrete current profile appendix each
- a small “current implementation example” section
- one or two real commands/schemas/examples where appropriate

### 3. No Major Kaupapa Loss Found

I did not find a major case where the core kaupapa was inverted or stripped away.

The main risk is softer:
- some vivid purpose got generalized
- some operational sharpness got removed along with stale mechanics

That is a much safer failure mode than the earlier drift.

## Priority Revisions

### High Priority

These should get light appendices next:
- `QUICK_REFERENCE_CURRENT_CONTRACT.md`
- `how_to_run_CURRENT_CONTRACT.md`
- `guides/DEPLOYMENT_CHECKLIST_CURRENT_CONTRACT.md`
- `guides/PRODUCTION_SETUP_CURRENT_CONTRACT.md`
- `guides/QUICK_START_PHASE_6_CURRENT_CONTRACT.md`
- `technical/FASTAPI_COMPLETE_CURRENT_CONTRACT.md`
- `technical/FRONTEND_BACKEND_INTEGRATION_CURRENT_CONTRACT.md`
- `technical/VECTOR_INDEX_GUIDE_CURRENT_CONTRACT.md`
- `architecture/OPERATIONAL_INFRASTRUCTURE_CURRENT_CONTRACT.md`
- `guides/KAITIAKI_SDK_VISION_CURRENT_CONTRACT.md`

### Medium Priority

These are sound, but could be sharpened later:
- `DOCUMENTATION_INDEX_CURRENT_CONTRACT.md`
- `FOLDER_REORGANIZATION_COMPLETE_CURRENT_CONTRACT.md`
- `architecture/DUAL_CONTAINER_ARCHITECTURE_CURRENT_CONTRACT.md`
- `architecture/DUAL_CONTAINER_QUICK_REFERENCE_CURRENT_CONTRACT.md`
- `guides/SUPABASE_SETUP_CURRENT_CONTRACT.md`
- `TEST_REPORT_CURRENT_CONTRACT.md`

### Low Priority

These are safe to keep as-is:
- governance docs
- most phase summaries
- the main structure/architecture docs
- te reo and seed docs

## Carry-Forward Recommendations

### For Operational Docs

Add a short appendix section titled one of:
- `Current Profile Example`
- `Current Local Profile`
- `Example Commands`

That restores utility without reintroducing lock-in.

### For Runtime Docs

Add one concrete example of:
- a structured action
- a guardian decision
- a staging-to-endpoint promotion path

### For Indexing Docs

Add one current indexing profile note:
- canonical text
- folded helper text
- vector/index backend in the active profile

## Final Judgment By Corpus

- safe to keep as-is:
  - most docs
- needs light revision:
  - a defined subset of operational/runtime docs
- needs substantial revision:
  - none

That means the corpus is fit to act as the canonical upstream source now.

The next step is refinement, not reconstruction.
