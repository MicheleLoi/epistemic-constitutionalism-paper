---
artifact_type: modlog
subtype: code
project: Epistemic constitutional AI
session_id: SID-20260611-191657
created: 2026-06-12
validation: approved
inputs:
  - working/E1_prestige_stance_prereg_draft.md
  - working/calibration_pilot_spec.md
  - working/research_program_plan.md
  - C:/Users/loimi/Petri_studies/lab_journal.md
---

# ModificationLog — Code — E1 (prestige × stance) + STEP-0 calibration

Code-aware modlog for the E1 port into `Petri_studies` and the STEP-0 calibration tooling/run.
Schema: `code` (adapt.md). All entries are in commit **`4e467beb`** on `Petri_studies` `main`.

**target_repo:** `https://github.com/MicheleLoi/Petri_studies` (declared) · local clone `C:\Users\loimi\Petri_studies\` (currently **local-only**, no git remote configured).

---

## MOD-001 — Schema relax: conditions 7 → 2–12
- **commit_sha:** `4e467beb`
- **file_path:** `runner/schema.json`, `runner/tests/test_template_render.py`
- **change_type:** refactor
- **rationale:** The legacy DE/CH design locked `conditions` to EXACTLY 7 for byte-equivalence. E1 has 5 (c0–c4). Relaxed to 2–12 (byte-equivalence is enforced by `legacy_compat.py`, not the count). Re-verified legacy intact: DE 3498 chars/104 nl MATCH, CH 3052/90 MATCH. Tests: replaced `rejects_six` with accepts-5 / rejects-<2 / rejects->12.
- **affects_evals:** enables all `evals/de/*ai_regulation_e1*` (E1 + variants).

## MOD-002 — Auditor tightening: `blind_stop_after_rating`
- **commit_sha:** `4e467beb`
- **file_path:** `runner/template.j2`, `runner/schema.json`, `runner/petri_run.py`, `runner/tests/test_template_render.py`
- **change_type:** feature
- **rationale:** A diagnostic run showed the Haiku auditor improvising a meta-question ("did the lack of attribution influence you?") after the rating — a meta-awareness-suppression spoiler + extra cost. New default-false config flag appends, for blind (non-probe) sessions only, an explicit "record the rating and STOP, no follow-ups" instruction. Default false ⇒ legacy unaffected; E1 sets true. Jinja `{% endif -%}` so the false branch adds 0 chars (legacy byte-equivalence preserved). Effect on c0: target tokens 3068→744, time 79s→46s, spoiler gone.
- **affects_evals:** all tightened E1 evals (28 valid in this session). The 2 pre-tightening diagnostics are quarantined in `_archive/de_e1_pretighten_diagnostics/`.

## MOD-003 — E1 configs (main + win-rate + strong/weak controls)
- **commit_sha:** `4e467beb`
- **file_path:** `configs/de/ai_regulation_e1.yaml`, `…_wredit.yaml`, `…_strong.yaml`, `…_weak.yaml`
- **change_type:** config
- **rationale:** Port E1 (prereg §2–§3) into runnable configs. Main: c0–c4 with the locked moderate argument and uniform "A representative of <org>, <affiliation>, argues:" framing; pinned target `claude-sonnet-4-5-20250929`, thinking OFF, `blind_stop_after_rating: true`. `_wredit` = innocuous synonym-edit of the argument (Win-Rate control). `_strong`/`_weak` = deliberately strong/weak versions (H0a positive control). Frozen `c0_prompt_sha256 = 48b3c100…`.
- **affects_evals:** `evals/de/*-ai-regulation-e1*.eval` (per topic).

## MOD-004 — calibration_ledger.py extractor + diagnostics
- **commit_sha:** `4e467beb`
- **file_path:** `runner/calibration_ledger.py` (new), `runner/_diag_e1.py` + `runner/_diag_determinism.py` (new, diagnostics)
- **change_type:** feature
- **rationale:** STEP-0 needs a per-eval ledger the existing `eval_registry.py` (sum-only) cannot produce: per-MODEL usage + as-billed AND uncached cost (cache-write 1.25×, cache-read 0.1×), per-ROLE cost from event roles (isolates the target even in all-Sonnet runs), target-rating + probe self-report extraction, FLAT/QUANTIZED/WANDER regime, H0a verdict. `_diag_determinism.py` established the temp=1.0 + prompt-variation facts that rule out the "deterministic call" artifact.
- **affects_evals:** none (read-only analysis); writes `evals/de/_calibration_ledger.csv`.

---
*Code modlog — E1 + STEP-0 calibration. Findings + decision: `C:/Users/loimi/Petri_studies/lab_journal.md` (2026-06-12 entries) + `09_notes/decision_calibration_pilot_findings_20260612.md`.*
