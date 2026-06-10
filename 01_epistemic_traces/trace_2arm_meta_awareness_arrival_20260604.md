---
artifact_type: epistemic_trace
topic: How we arrived at the 2-arm meta-awareness design (UK Phase D)
project: Epistemic constitutional AI
date: 2026-06-04
session_id: SID-20260604-145637
inputs:
  - 03_modification_logs/ModificationLog_Code_UK.md
  - C:/Users/loimi/Petri_studies/lab_journal.md (anomaly entry + methodology_pivot entry, same SID)
  - C:/Users/loimi/Petri_studies/evals/uk/trial_sonnet46__*.eval (T1)
  - C:/Users/loimi/Petri_studies/evals/uk/trial_sonnet46_fixA__*.eval (T1')
validation: approved
---

# Epistemic Trace — How we arrived at the 2-arm design

## Purpose and Provenance

Snapshot the reasoning path that led from "spoiler-to-be-fixed" to "spoiler-as-measurement". The decision content (Arm A/B specification, eval plan, paper phrasings) is OUT OF SCOPE for this trace and lives in `Petri_studies/lab_journal.md` as a `[methodology_pivot]` entry (same session). The trace exists to make the **path** referenceable, distinct from the **conclusion**.

Type 2 trace per project `content_schemas`.

## Source Segment Map

Sequence in `SID-20260604-145637` that anchored the pivot:

1. T1 .eval inspection: rating 0.68 × 7 with cascading meta-commentary.
2. Diagnosis: 3 spoiler sources (auditor signals; commitment cascade; single-context memory).
3. FIX A applied (prompt-level only, commit `19ad7ed`).
4. T1' .eval inspection: rating 0.68 × 7 char-by-char identical — MORE rigid, not less.
5. Foundational concepts surfaced (auditor_agent target-memory model; prompt cache ≠ memory).
6. Realization: spoilers 2+3 are STRUCTURAL, not prompt-addressable.
7. User's reframe → measurement, not fix.

## Reconstructed Framework — Reasoning Shape

The conversation traversed three frames:

- **Frame 1 — "Fix the bug"**: spoiler is contamination; remove it; recover clean data. FIX A operated here. Insufficient because spoilers 2+3 are structural.
- **Frame 2 — "Cost of fixing"**: removing structural spoilers means refactor (FIX B1 — fresh-context-per-condition). Recognized, nearly executed.
- **Frame 3 — "Spoiler as data"**: the DIFFERENCE between presence/absence of structural spoilers IS the measurement. Triggered by the user's formulation below.

The Frame 2 → Frame 3 shift is the load-bearing epistemic move. Without it the same code would have been written but only 1 arm of data produced.

## Paper and Eval Strategy

**Referenced, not duplicated**. See `Petri_studies/lab_journal.md` entry `[methodology_pivot]` 2026-06-04 for design spec, Phase 1/2 plan, paper-section integration, reusable phrasings.

## Reusable Claims and Phrasing — Verbatim User Formulation

The pivot, preserved:

> *"raddoppiare il test — sapere che AI si è comportata DIVERSAMENTE con contesto continuo vs. separato è molto significativo in sé"*

Other paper-ready phrasings derive from it and live in the lab_journal entry.
