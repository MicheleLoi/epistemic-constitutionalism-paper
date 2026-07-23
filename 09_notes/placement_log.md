---
artifact_type: placement_log
purpose: "Append-only log of placement decisions for non-canonical artifacts. Written by /mhc-place at save time. Used to review routing convention quality over time: recurring placements in unexpected locations signal gaps in the routing rules worth amending."
schema_version: 1
created: 2026-06-02
created_in_session: SID-20260602-165225
---

# Placement log

Append-only. One line type:

- `placement:` — written by /mhc-place at save time. Fields: date, SID, artifact description, path chosen, predicted tier, pointer (yes/no).

Nota: in questo progetto il log vive in `09_notes/` (convenzione cartelle numerate) anziché nel default `notes/methodology/` — non esiste `notes/methodology/`.

## Log entries

placement: 2026-06-02 SID-20260602-165225 | Piano di replicazione UK/US/IT (protocollo studio multi-polity, decisioni ratificate) | path: 09_notes/replication_plan_uk_us_it_20260602.md | tier: 2 | pointer: yes

placement: 2026-07-23 SID-20260723-103120 (SID registrato retroattivamente a /mhc-end: il SessionStart hook non è partito — `mhc_w_path` in .mhc-config.json punta ancora all'installazione Windows `C:\Users\loimi\...`, inesistente su questo Mac) | Nota related-work su Kwok et al. 2026 "LLM-as-a-Verifier" (arXiv:2607.05391) — expectation continua sui logit di scoring vs. intero discreto del judge; tocca direttamente il finding del rating head saturante | path: 09_notes/related_work_kwok_2026_llm_as_a_verifier.md | tier: 2 | pointer: yes (back-pointer aggiunto in 01_epistemic_traces/trace_quantized_rating_head_20260612.md come addendum datato, su richiesta del PI 2026-07-23; edit registrato in 03_modification_logs/ModificationLog_EpistemicTraces.md MOD-001)
