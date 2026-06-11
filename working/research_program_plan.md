---
artifact_type: note
subtype: research_program_plan
topic: Full investigation scheme + live cost model for the empirical-critical source-dependence paper
project: Epistemic constitutional AI
date: 2026-06-11
session_id: SID-20260610-145422
validation: approved
inputs:
  - 09_notes/decision_empirical_critical_framing_20260611.md
  - 09_notes/reliability_audit_published_evals_20260609.md
  - 01_epistemic_traces/trace_confabulation_n1_informs_paper_20260609.md
  - working/E1_prestige_stance_prereg_draft.md
  - arXiv:2603.18530 (ICE-Guard — Win-Rate control, domain-dependence)
note: >
  Living document. The cost ledger (§6) is updated as batches run — the a-priori € figures here
  are explicitly provisional until the calibration pilot fixes cost-per-eval.
---

# Research Program Plan — empirical-critical paper on source dependence

## 1. Thesis & spine
**Thesis:** *Source dependence in a frontier model is real but narrow, easily mis-measured, hard to
classify as bias vs. competence, and not reported by the model itself — a worked case in what it takes
(and costs) to establish an "epistemic policy" empirically.*

**Dialectic:** facts since Germani & Spitale → the audit (precise numbers fragile, one effect survives)
→ the corrected, domain-bounded finding → "is it bias?" + "can its testimony tell you?" → what this
implies for measuring epistemic policies. Register: **carried by exemplary findings, not measures.**

## 2. The investigations
"Eval" = one *condition × run* fresh-context unit (the cost atom). Counts use planning midpoint n≈8 for
behavioral cells; **adaptive-n may roughly halve them.** ★ = committed core.

| # | Investigation | Paper role | Status | ~Evals | Scope |
|---|---|---|---|---|---|
| **S0** ★ | Reliability audit of the 26 published runs | "precise numbers were fragile" | ✅ done | 0 | core |
| **S1** ★ | Reliable **re-measurement** of the AI-topic penalty (error bars, ordered criterion, noise floor) | "what survives" | new | ~85 | core |
| **S2-trim** ★ | **Domain-boundedness** — AI-security vs 1–2 matched non-AI controls (equivalence-tested) | "the odd phenomenon" | new | ~120 | core |
| **S3-ver** ★ | **Version-drift exemplar** — Sonnet 4.6 on AI-security (does the 4.5 effect survive the update?) | robustness exemplar | new | ~70 | core *(added 2026-06-11)* |
| **S4 / E1** ★ | **Bias vs competence** — prestige × stance deconfound | "is it a bias?" | ✅ speced | ~90 | core |
| **S5** ★ | **Behavior–testimony dissociation** (expanded — see §3) | "can its testimony tell you?" | Stage-0 done; Stage-2 new | ~120 | core |
| — S2-full | Deconfound *what AI-ness is* (self-relevance vs novelty vs training-salience), more topics | mechanism of domain-specificity | new | ~250 | deferred |
| — S3-lang | Language arm (EN→DE translation, same sources) | robustness | new | ~60 | deferred |
| — S5c | Cross-model dissociation (≥1 other family) | generality of the testimony failure | new | ~80 | deferred |
| — S6 | Cross-model **breadth** on the AI-topic schema | "frontier LLMs in general" | new | ~250 | deferred |
| — S7 | **Normative anchor** — Bayesian/expert analysis, or a human baseline | normative half of "is it bias?" | new | ~0 evals (analysis) / human study (separate) | deferred |

## 3. S5 expanded (the testimony payload)
| Sub | What | Cells | n | Evals | Scope |
|---|---|---|---|---|---|
| **S5a** | Confabulation **reproduction & frequency** — signed-zero test beyond n=1 | Claude 4.5; AI-security + 1 non-AI | behavioral adaptive 5–12; self-report + counterfactual **n=12** each | ~70 | core |
| **S5b** | The **completing cell** — self-report/counterfactual probes run *where behavior IS source-dependent* (does testimony track, miss, or misreport the real effect?) | Claude 4.5; AI-security real cells | self-report + counterfactual **n=12** | ~50 | core |
| **S5c** | **Cross-model** signed-zero test | ≥1 other family; AI-security | n=10 | ~80 | deferred |
| **S5d** | **Four-channel characterization** (output rating / first-pass reasoning / interrogator routing / prompted self-report) — which channels dissociate | analysis on S5a/b transcripts | — | ~0 | core (≈free) |

**The 2×2 S5 completes** (the novel object): behavior {present, absent} × testimony {accurate, confabulated}.
S5a covers the behavior-absent cells (confabulation existence); **S5b covers the behavior-present cells**,
which have never been probed — the highest-value new cell in the whole program.

## 4. Sampling policy
- **Behavioral channel:** adaptive n, floor 5, cap 12, set so the TOST CI ≤ τ (per-model noise floor from
  k=8 baseline repeats). Near-deterministic head ⇒ n≈5; noisy ⇒ n≈10.
- **Self-report / counterfactual channels (S5):** **n=12** (cap 20 if the asserted sign is inconsistent) —
  the signed-zero claim is distributional, and these probes are cheap single-turn add-ons.
- Every behavioral cell carries a **positive control** + the **Win-Rate randomization control** (ICE-Guard).

## 5. Cost model
`cost ≈ N_evals × cost-per-eval`. **N_evals is known; cost-per-eval is not** — a Petri eval is a multi-turn
agentic interaction, plausibly **€0.10–0.60** depending on transcript length, thinking budget, and which
models run the auditor/judge. So the € figures below are a *band*, not an estimate, until the calibration
pilot (§6, step 0) collapses it.

| Scope | ~Evals (incl. pilot) | € band @ 0.10–0.60/eval |
|---|---|---|
| **Committed core** (S0–S5 ★, +S5a/b/d) | **~505** | **€50–305** |
| Full program (+ S2-full, S3-lang, S5c, S6) | ~1,145 | €115–690 |

→ **Core fits the €300–500 ceiling even at the pessimistic per-eval cost; the full program risks
exceeding it.** (S7 human baseline, if chosen, is a separate participant-payment cost, not API evals.)

**Cost levers:** (1) cheaper auditor/judge models — only the *target* must be the model under test;
(2) adaptive-n — don't pay for n=8 where n=4 nails a near-deterministic cell; (3) reuse behavioral runs
across S1/S2/S5 rather than re-running.

## 6. Continuous cost ledger (the live mechanism)
**Step 0 — calibration pilot (~20 evals, run first):** one full 7-condition behavioral cell + a handful of
self-report probes on the *actual* target models; record tokens in/out and €; compute cost-per-eval
**separately for behavioral cells vs self-report probes** (they differ a lot).

**Ledger (append one row per batch as we run):**

| Batch | Date | Study | Models | #evals | tok_in | tok_out | € | €/eval | cum € | % of €500 | rolling €/eval |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | _pending_ | calibration | — | — | — | — | — | — | — | — | — |

**Update rule (after every batch):**
1. Append the row with *actuals* (tokens + €).
2. `rolling €/eval` = cumulative € ÷ cumulative evals (track behavioral vs probe separately).
3. `projected total` = cum € + (remaining planned evals × rolling €/eval).
4. If projected > €500 → **flag and cut**: drop a deferred item, or tighten n via the adaptive rule.

This keeps the budget honest the same way the paper demands of its science: no point estimate without a
measured basis, re-estimated as evidence accrues.

## 7. Execution order & dependencies
1. **Calibration pilot** (fixes cost-per-eval + seeds σ̂).
2. **S1** — anchor + per-model noise floor (σ̂ sets adaptive-n for everything downstream).
3. **S2-trim** + **S3-ver** (reuse S1's noise floor; S3-ver is the marquee drift cell).
4. **S4 / E1** (independent; can run in parallel).
5. **S5a/S5b** (reuse behavioral runs from S1/S2 where possible; add the probes).
6. **S5d** analysis; write-up.

## 8. Scope decisions
- **Committed core (this session):** S0 ✅, S1, S2-trim, **S3-ver (added)**, S4/E1, **S5a+S5b+S5d (expanded)**.
- **Deferred → "future work / limitations":** S2-full (mechanism of AI-ness), S3-lang, S5c, S6 (breadth),
  S7 human baseline. Honest consequence: claims are about **Claude**, domain-boundedness is shown as an
  *exemplar* not mechanistically explained, and bias-vs-competence is adjudicated *internally*.
- Final cut to be ratified by the author (the remaining open call).

## 9. Open items
- Non-AI control topic(s) for S2-trim / S5 (candidate: debt-brake — has a German source schema).
- Run the calibration pilot (`working/calibration_pilot_spec.md`) to replace the € band with measured numbers + the rating-head regime classification.
- Port E1 + the S1/S2/S3/S5 protocols into `Petri_studies/PREREGISTRATION.md` before running.
- GPT-4o / other-model availability (only if S5c/S6 are un-deferred).
