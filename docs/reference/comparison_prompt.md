Run a full-corpus intent preservation audit across the documentation set.

Goal:
- compare each original document with its corresponding current-contract document
- verify that important intent, kaupapa, boundaries, useful operational guidance, and document function were preserved
- identify where the current-contract version became too vague, too generic, too meta, or lost important meaning
- produce both:
  1. a detailed comparison report for each document
  2. a CSV summary with one row per comparison

Rules:
- do not rewrite documents yet
- do not invent missing architecture
- do not assume the current-contract version is correct
- do not assume the original is correct in all mechanics
- treat originals as historical source memory
- treat current-contract docs as active contract candidates
- focus on:
  - preserved intent
  - weakened intent
  - lost intent
  - correctly removed stale mechanics
  - accidentally lost practical guidance
  - over-correction into vagueness or commentary
  - culturally important meaning that may have been flattened

For each document pair, produce a detailed comparison with these sections:

1. Intent Preserved
2. Intent Weakened
3. Intent Lost
4. Stale Mechanics Correctly Removed
5. Useful Operational Content Lost By Mistake
6. Over-Correction
7. Carry Forward Recommendations
8. Final Judgment
   - safe to keep as-is
   - needs light revision
   - needs substantial revision

Also produce a CSV file with one row per document using these columns:

- original_path
- current_contract_path
- document_type
- function_preserved
- intent_preserved_score
- intent_weakened_score
- intent_lost_score
- operational_usefulness_score
- anti_drift_success_score
- cultural_integrity_score
- stale_mechanics_removed
- over_corrected
- needs_revision
- final_judgment
- priority
- notes

Scoring guidance:
- use 0-5 for the score columns
- 5 = strong / fully preserved
- 0 = absent / badly lost

Field guidance:
- document_type:
  - contract
  - guide
  - summary
  - governance
  - technical
  - archival
- function_preserved:
  - yes
  - partial
  - no
- stale_mechanics_removed:
  - yes
  - partial
  - no
- over_corrected:
  - yes
  - partial
  - no
- needs_revision:
  - no
  - light
  - substantial
- priority:
  - low
  - medium
  - high
  - critical

Important:
- preserve architecture-source quality
- preserve portability
- preserve document usefulness
- preserve kaupapa
- prefer stable roles over framework names
- flag anything culturally important that was flattened, weakened, or generalized too far

Output requirements:
- create one markdown audit report
- create one CSV summary
- keep findings concrete and document-specific
- if a current-contract doc is too generic to replace the original’s function, say so explicitly
