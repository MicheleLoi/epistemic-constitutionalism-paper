---
artifact_type: note
subtype: decision
project: Epistemic constitutional AI
session_id: SID-20260611-191657
created: 2026-06-12
validation: approved
inputs:
  - working/calibration_pilot_spec.md
  - working/research_program_plan.md
  - working/E1_prestige_stance_prereg_draft.md
  - C:/Users/loimi/Petri_studies/lab_journal.md
  - C:/Users/loimi/Petri_studies/evals/de/_calibration_ledger.csv
---

# Decision — STEP-0 calibration pilot findings + the recalibrate-E1 call (2026-06-12)

## Topic
What the STEP-0 calibration pilot (28 evals, target Sonnet 4.5, thinking OFF) found, and the
decision it forces before E1's confirmatory ~505-core. Full experimental detail lives in the
**Petri_studies lab journal** (`lab_journal.md`, 2026-06-12 entries) and the per-eval ledger
(`evals/de/_calibration_ledger.csv`); this note is the workspace-side decision record. Builds on
[[decision_empirical_critical_framing_20260611]] and the program in `working/research_program_plan.md`.

## Findings (brief — detail in the lab journal)
1. **Cost is not the constraint.** ~$0.03–0.05/eval as-billed; the ~505-core projects to **≈€20**
   (≈€35 uncached) — far under the €50–305 band and the €300–500 ceiling. The orchestration
   (auditor+judge) is ~66% of cost; the target is ~34% and **uncached** (full-price input each run).
   The cheaper-Haiku-auditor lever is real. c4 was the *cheapest* cell, not the "ceiling" — cost is
   driven by occasional auditor verbosity, not by the cell.
2. **Razor-flat, quantized rating head.** **0.72 across all 20 pilot evals** (source-null, edit-null,
   auditor-null). Verified NOT a determinism artifact: target **temperature = 1.0** (sampling on),
   prompts and prose vary, yet the *number* is invariant. No verbalized eval-recognition (0/42 msgs).
3. **H0a PASS, with a ceiling.** strong 0.72 / moderate 0.72 / **weak 0.25** (Δ +0.47) ⇒ the head
   *moves with quality*, so 0.72 is a **real source-independent merit score**, not a dead dial. BUT
   **strong = moderate = 0.72**: no upward headroom (a ceiling at 0.72), and each level is razor-flat
   ⇒ **hard quantization** (coarse ~0.25/0.72 bins).
4. **Confabulation reproduced.** 1/2 c4 probes asserted source `raised +0.03` (predicted no-source
   0.69) while behavior was 0.72 flat — signed-zero behaviour↔testimony dissociation, the n=1 kernel.

## Decision
- **Stop the pilot here; commit + track thoroughly** (done: Petri_studies `4e467beb` + lab journal;
  workspace `ModificationLog_Code_E1.md` + this note + the §6 ledger in `research_program_plan.md`).
- **Recalibrate E1's base argument before the confirmatory core** — as a separate next step. The
  moderate argument **saturates at 0.72**, so an against-interest UPWARD bonus (E1's primary target)
  is ceiling-masked. Need an argument the model rates **mid-range (~0.5)** so source effects have room
  both ways. Then re-freeze + port E1 to `PREREGISTRATION.md` + git-tag before any confirmatory run.
- **E1 is NOT yet pre-registered/locked** — the design is incomplete until the argument is recalibrated.

## Methodological payload for the paper (independent of E1's fate)
Two paper-grade points the pilot establishes: (a) this rating head is **quantized/saturating**, so
**source effects below ~0.2 are below the instrument's resolution** — the literature's small reported
effects may be unmeasurable without finer elicitation; (b) the **behaviour↔testimony dissociation**
(confabulation) reproduces beyond n=1. See [[trace_confabulation_n1_informs_paper_20260609]].

## Open (next session)
- Argument-strength sweep to find a mid-range (~0.5) E1 base argument.
- Optional: a **naturalistic probe** (same argument, no auditor/eval framing) to test whether the
  0.72 rigidity is eval-situational vs intrinsic — the one open thread on the "meta-rule" hypothesis.
