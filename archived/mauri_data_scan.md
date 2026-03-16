# .mauri_data Deep Scan Report

## Directory Tree (first 6 levels)

```
mauri_data/
  .mauri_data/
    copyright.json
    index.ts
    kitenga.meta.yaml
    matanga.ts
    mauri_key.json
    meta.data.kitenga.md
    tohu_logo.svg
    docs/
      BRANCHING.md
      DOCUMENTATION_INDEX.md
      FILES_CREATED_THIS_SESSION.md
      FOLDER_REORGANIZATION_COMPLETE.md
      PHASE_6_VISUAL_SUMMARY.md
      PROJECT_STATUS.md
      QUICK_REFERENCE.md
      STRUCTURE_GUIDE.md
      TEST_REPORT.md
      TRANSPARENCY.md
      how_to_run.md
      architecture/
        ARCHITECTURE.md
        DUAL_CONTAINER_ARCHITECTURE.md
        DUAL_CONTAINER_QUICK_REFERENCE.md
        KUBERNETES_READINESS.md
        OPERATIONAL_INFRASTRUCTURE.md
        WHAKAPAPA_DEPLOYMENT.md
      guides/
        CONTRIBUTING.md
        DEPLOYMENT_CHECKLIST.md
        KAITIAKI_SDK_VISION.md
        PRODUCTION_SETUP.md
        QUICK_START_PHASE_6.md
        SELF_HOSTING.md
        START_HERE_PHASE_6.md
        SUPABASE_SETUP.md
        TE_REO_WORKFLOW.md
      phase-summaries/
        BACKEND_DELIVERY_SUMMARY.md
        BACKEND_STATUS.md
        PHASE_2_SUMMARY.md
        PHASE_6_DELIVERY_MANIFEST.md
        PHASE_6_EXECUTIVE_SUMMARY.md
        PHASE_6_FINAL_STATUS.md
        PHASE_6_VISUAL_SUMMARY.md
        SESSION_6_COMPLETE.md
        SESSION_COMPLETE.md
        WHAKAPAPA_REUNIFICATION.md
      technical/
        COMMUNITY_MODEL.md
        FASTAPI_COMPLETE.md
        FREE_TIER_ELIGIBILITY.md
        FRONTEND_BACKEND_INTEGRATION.md
        KAITIAKI_SEED_GUIDE.md
        OWNERSHIP.md
        SEED_IMPLEMENTATION_SUMMARY.md
        VECTOR_INDEX_GUIDE.md
    taonga(archived)/
```

## Integrity-related files

_none detected_

## Manifest / Mauri / Trust / Policy files

- .mauri_data/copyright.json
- .mauri_data/docs/BRANCHING.md
- .mauri_data/docs/DOCUMENTATION_INDEX.md
- .mauri_data/docs/FILES_CREATED_THIS_SESSION.md
- .mauri_data/docs/FOLDER_REORGANIZATION_COMPLETE.md
- .mauri_data/docs/PHASE_6_VISUAL_SUMMARY.md
- .mauri_data/docs/PROJECT_STATUS.md
- .mauri_data/docs/QUICK_REFERENCE.md
- .mauri_data/docs/STRUCTURE_GUIDE.md
- .mauri_data/docs/TEST_REPORT.md
- .mauri_data/docs/TRANSPARENCY.md
- .mauri_data/docs/architecture/ARCHITECTURE.md
- .mauri_data/docs/architecture/DUAL_CONTAINER_ARCHITECTURE.md
- .mauri_data/docs/architecture/DUAL_CONTAINER_QUICK_REFERENCE.md
- .mauri_data/docs/architecture/KUBERNETES_READINESS.md
- .mauri_data/docs/architecture/OPERATIONAL_INFRASTRUCTURE.md
- .mauri_data/docs/architecture/WHAKAPAPA_DEPLOYMENT.md
- .mauri_data/docs/guides/CONTRIBUTING.md
- .mauri_data/docs/guides/DEPLOYMENT_CHECKLIST.md
- .mauri_data/docs/guides/KAITIAKI_SDK_VISION.md
- .mauri_data/docs/guides/PRODUCTION_SETUP.md
- .mauri_data/docs/guides/QUICK_START_PHASE_6.md
- .mauri_data/docs/guides/SELF_HOSTING.md
- .mauri_data/docs/guides/START_HERE_PHASE_6.md
- .mauri_data/docs/guides/SUPABASE_SETUP.md
- .mauri_data/docs/guides/TE_REO_WORKFLOW.md
- .mauri_data/docs/how_to_run.md
- .mauri_data/docs/phase-summaries/BACKEND_DELIVERY_SUMMARY.md
- .mauri_data/docs/phase-summaries/BACKEND_STATUS.md
- .mauri_data/docs/phase-summaries/PHASE_2_SUMMARY.md
- .mauri_data/docs/phase-summaries/PHASE_6_DELIVERY_MANIFEST.md
- .mauri_data/docs/phase-summaries/PHASE_6_EXECUTIVE_SUMMARY.md
- .mauri_data/docs/phase-summaries/PHASE_6_FINAL_STATUS.md
- .mauri_data/docs/phase-summaries/PHASE_6_VISUAL_SUMMARY.md
- .mauri_data/docs/phase-summaries/SESSION_6_COMPLETE.md
- .mauri_data/docs/phase-summaries/SESSION_COMPLETE.md
- .mauri_data/docs/phase-summaries/WHAKAPAPA_REUNIFICATION.md
- .mauri_data/docs/technical/COMMUNITY_MODEL.md
- .mauri_data/docs/technical/FASTAPI_COMPLETE.md
- .mauri_data/docs/technical/FREE_TIER_ELIGIBILITY.md
- .mauri_data/docs/technical/FRONTEND_BACKEND_INTEGRATION.md
- .mauri_data/docs/technical/KAITIAKI_SEED_GUIDE.md
- .mauri_data/docs/technical/OWNERSHIP.md
- .mauri_data/docs/technical/SEED_IMPLEMENTATION_SUMMARY.md
- .mauri_data/docs/technical/VECTOR_INDEX_GUIDE.md
- .mauri_data/kitenga.meta.yaml
- .mauri_data/mauri_key.json
- .mauri_data/meta.data.kitenga.md

## Potential secrets (needs sealing)

_none detected_

## Keys/Certificates

- .mauri_data/mauri_key.json

## .env / env-like files

_none detected_

## Policy/Tikanga docs

_none detected_

## Large text blobs (review)

_none detected_


---

### Guidance & Next Steps
- **Seal secrets**: move any API keys or credentials into a secrets store and reference via env only at runtime. Do not commit secret values.
- **Trust covenant**: ensure `integrity/trust_manifest.yaml` exists (or adopt the template I created earlier) and keep it encrypted/offline.
- **Verify carve**: add `.mauri_data/integrity/verify_carve.py` and run it before app boot. It will check presence of trust manifest and required envs.
- **Data classification**: add `tapu/noa` flags and `allowed_agents` arrays into mauri manifests for each dataset.
- **RLS**: apply Row-Level Security in your DB for all taonga tables; deny-by-default and whitelist kaitiaki service roles only.
- **Backups**: create an encrypted, offline backup of `.mauri_data` and store the checksum outside the repo.
