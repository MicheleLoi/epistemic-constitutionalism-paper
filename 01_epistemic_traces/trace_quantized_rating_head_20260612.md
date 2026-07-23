---
artifact_type: trace
trace_type: Type-2 (influence document — conceptual framework for the paper)
project: Epistemic constitutional AI
session_id: SID-20260611-191657
created: 2026-06-12
validation: approved
updated: 2026-07-23 (addendum only — original text unchanged; see 03_modification_logs/ModificationLog_EpistemicTraces.md MOD-001)
inputs:
  - C:/Users/loimi/Petri_studies/lab_journal.md (2026-06-12 STEP-0 entries)
  - C:/Users/loimi/Petri_studies/evals/de/_calibration_ledger.csv
  - 09_notes/decision_calibration_pilot_findings_20260612.md
  - 01_epistemic_traces/trace_confabulation_n1_informs_paper_20260609.md
---

# Trace — The rating head is a saturating nonlinearity (attractors + responsive mid-range)

## Purpose & provenance
Crystallizes the conceptual turn of session SID-20260611-191657 (2026-06-12): the STEP-0 calibration
pilot returned **0.72 on every one of 20 evals**, and the PI pressed the right question — *isn't a null
this improbable itself a finding, maybe a hidden rule; or are the calls just not independent?* This trace
fixes the framework that resolves that question, so it can carry into the paper. It separates three things
the pilot conflated into "the 0.72 thing". Builds on [[trace_confabulation_n1_informs_paper_20260609]].

## Source segment map (load-bearing moments)
- **0.72 everywhere** — c0=c1=c2=c4 (source-null), original=innocuous-edit (win-rate-null), blind=probe,
  Haiku-aud=Sonnet-aud. 20/20.
- **Determinism ruled out** — target `temperature` unspecified in the request ⇒ Anthropic API default 1.0 (sampling on; **corrected 2026-06-13** — temperature is NOT a recorded field in the .eval
  `call.request`), **3 distinct** target prompts across c0 (auditor paraphrases), target prose varies
  471–805 tok — yet the *number* is invariant. So: independent, stochastic calls that converge.
- **H0a** — weak **0.25 ×4**, moderate **0.72**, strong **0.72**. The head moves DOWN for bad quality but
  NOT UP for strengthened quality.
- **PI's distinction-forcing question** — "fixed number → saturation → hidden rule → itself a finding?"
- **Argument-strength sweep (2026-06-12, corrects the picture)** — mediocre **0.45/0.45/0.52/0.55/0.62**
  (σ̂≈0.07, WANDERS) while verystrong (mechanism specified) **0.72 ×5** (still capped). ⇒ razor-flat ONLY at
  the attractors, responsive+noisy in between.
- **The unbundling** (the framework below).

## Reconstructed framework — three distinct objects
1. **SATURATING NONLINEARITY with attractor basins (the finding, corrected by the 2026-06-12 sweep).** The
   head is razor-flat (σ̂≈0) **only on two attractors** — a low basin ≈0.25 (bad arguments) and a high
   basin/ceiling ≈0.72 (good arguments: moderate, strong, AND mechanism-specified verystrong all land
   there). **Between** them it is responsive and **noisy**: the *mediocre* argument gave
   0.45/0.45/0.52/0.55/0.62 (σ̂≈0.07) at temperature 1.0. So the head is **NOT a uniform quantizer** (my
   first, premature read): it is a **saturating nonlinearity** — flat at the extremes, resolving in the
   middle. The original "0.72 everywhere" was an artifact of having tested only arguments that sit on the
   high attractor. The razor-flatness *at* an attractor is still the strange part (σ̂→0 at temp 1.0); the
   correction is that it is local to the attractors, not global.
2. **SATURATION / ceiling — CONFIRMED.** Strengthening doesn't raise the score (moderate = strong = 0.72)
   while weakening lowers it. The earlier small-n caveat ("maybe the 'strong' wasn't perceived as stronger")
   is **resolved by the sweep**: a *very strong* argument that explicitly fixes the weakness the model had
   flagged (it specifies the review mechanism concretely) STILL caps at **0.72 ×5**. So 0.72 is genuine
   saturation for pro-AI-regulation arguments on this model — the E1-design-relevant fact (no upward headroom
   ⇒ an against-interest UPWARD bonus is masked).
3. **MECHANISM = the open question (hypothesis, not finding).** What produces the canonical values? Ruled
   out: temperature determinism (it's 1.0) and *verbalized* eval-recognition (0/42 target messages). Not
   ruled out: a coarse internal rubric, an anchoring heuristic, or an **eval-situational canonicalization**
   ("strana regola" — the model emitting a defended canonical rating *because* it is in a test frame). The
   naturalistic probe (same argument, no auditor/eval framing) is the test that discriminates this branch.
   **[Addendum 2026-07-23]** A fourth candidate belongs on this list: **emission quantization** — the flatness
   living in the scalar-emission step rather than in the judgement. See the addendum at the end of this trace.

## Paper & eval strategy
- **Paper (register: methodology/epistemology lesson).** The headline is not merely "source dependence is
  narrow"; it is that **a source effect is measurable only where the rating head is responsive — the
  mid-range — and vanishes by construction wherever the argument sits on an attractor (the ≈0.72 ceiling or
  the ≈0.25 floor).** A study whose stimulus argument sits near saturation will report an artifactually
  near-zero, unstable source effect regardless of the true effect. This reframes the field's small, fragile
  effects as partly an **instrument-placement** artifact, and prescribes the fix: calibrate the base
  argument into the responsive mid-range *before* attributing sources. Self-standing contribution,
  independent of E1's fate; pairs with the confabulation dissociation (the model also *mis-reports* effects
  it does not have).
- **Next evals.** (a) **Argument-strength sweep** (this session) — graded arguments on baseline c0 to map
  the quality→rating curve: locate a **mid-range (~0.5)** base for E1, count the bins, and test whether the
  head **exceeds 0.72** (saturation vs perceived-strength). (b) **Naturalistic probe** (later) — to test the
  eval-situational mechanism branch.

## Reusable claims & phrasing (paper-ready)
- "At temperature 1.0, across independent fresh-context calls with varying prompts and varying free-text
  rationales, the model's numeric rating is razor-flat (σ̂≈0) on two attractor values — ≈0.25 for weak and
  ≈0.72 for strong arguments — yet wanders (σ̂≈0.07) for borderline arguments between them. The rating head
  is a saturating nonlinearity: neither a uniform quantizer nor a uniformly noisy estimator."
- "Strengthening a good argument does not raise its rating — a version that specifies the review mechanism
  the model had asked for still caps at 0.72 — while weakening it does lower it: the head saturates upward
  at ≈0.72 for this argument class."
- "A source-attribution effect is resolvable only in the head's responsive mid-range; for an argument on an
  attractor the head cannot move, so the measured effect is artifactually ≈0. The small, unstable source
  effects reported in the literature may partly reflect stimulus arguments sitting near saturation rather
  than a small true effect."
- "Behaviour is source-independent here; testimony is not — the model occasionally reports a source effect
  (+0.03) its own behaviour does not exhibit."

---

## Addendum 2026-07-23 — external convergence: Kwok et al. (2026), *LLM-as-a-Verifier*

*Appended after approval. The trace above is unchanged; nothing here is yet ratified as a finding.*

Kwok et al. (2026), arXiv:2607.05391, report that a judge model asked for a discrete score discards most of
its own signal at the moment of emission: underneath the emitted integer sits a full distribution over scores,
and taking the **expectation over the scoring-token logits** recovers resolution the integer destroys (ties on
a hard coding benchmark drop from a reported 26.7 % to zero — number unverified against the paper body).

This bears on the trace in three ways, in descending confidence:

1. **Corroborates the instrument-placement argument** (§Paper & eval strategy). Their tie problem is our
   ceiling problem in another task family: candidates that genuinely differ receive the same number.
2. **Adds a mechanism candidate and a discriminating test** (§Reconstructed framework, item 3). If the logit
   distribution under the ≈0.72 basin still moves with source or argument strength while the emitted number
   does not, the ceiling is an *emission* ceiling and item 2 ("saturation — CONFIRMED") needs restating. If
   the distribution is flat too, saturation hardens.
3. **Bears on E1's headroom problem.** A continuous read would restore headroom above ≈0.72 without touching
   the stimulus — *if* logprobs are reachable through the Petri path. The `.eval` `call.request` does not
   record them today (cf. the temperature correction of 2026-06-13); if they are unavailable for the target
   model, test (2) is unavailable and this becomes a stated limitation rather than a study.

Scope caveat: they study a verifier judging solution correctness on agentic/coding tasks; we study a target
rating argument persuasiveness under source attribution. The shared object is the scalar-emission bottleneck,
not the task.

Full note, with citation-verification status: [[related_work_kwok_2026_llm_as_a_verifier]]
(`09_notes/related_work_kwok_2026_llm_as_a_verifier.md`).
