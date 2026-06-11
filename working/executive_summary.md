---
artifact_type: note
subtype: executive_summary
topic: Executive summary — empirical-critical source-dependence paper (state, plan, research steps, outcomes)
project: Epistemic constitutional AI
date: 2026-06-11
session_id: SID-20260610-145422
validation: approved
inputs:
  - working/research_program_plan.md
  - working/E1_prestige_stance_prereg_draft.md
  - working/calibration_pilot_spec.md
  - 09_notes/decision_empirical_critical_framing_20260611.md
---

# Executive summary — the source-dependence paper

**TL;DR.** We've pivoted from a philosophy paper to a **fully empirical-critical study of source dependence in frontier LLMs**, motivated by discovering that the original paper's headline numbers were mostly run-to-run noise. The thesis: *source dependence is real but narrow, easily mis-measured, hard to call "bias," and invisible to the model's own testimony.* Framing, full research program, the first experiment (E1), and a calibration pilot are specified and committed; **no new data collected yet** — execution is next.

## 1. Where we are
- **Framing decided.** Empirical-critical paper on source dependence; the constitutional/philosophy framework is *postponed* (premature claims + headwinds against AI-co-authored philosophy). Register: **carried by exemplary findings, not measures.**
- **The trigger (done, S0).** Reliability audit of the 26 published runs: only **4/26** are genuine ordered effects — all Claude, all AI-topics. Headline magnitudes, the 3:1 ratio, the 6–15× multiplier are within noise. One effect survives clean (AI-security source penalty, ~0.30). Plus an n=1 **confabulation** finding (the model asserts a source effect its behavior lacks).
- **Public paper fixed.** Corrected a miscited predecessor (Germani & Spitale — wrong models, a fabricated stat) + a stale citation; **arXiv v4 submitted**.
- **Planned & specified.** Full program (S0–S7), committed **core (~505 evals)**, **E1** fully preregisterable, and a **calibration pilot** (cost + regime) — all adversarially checked and committed.

## 2. What we're going to do
Run the committed core, then write a ~5-beat empirical-critical paper: *facts since Germani & Spitale → the audit (numbers were fragile) → the corrected, domain-bounded finding → "is it bias?" + "can its testimony tell you?" → what this means for measuring an epistemic policy*, with the **reliability methodology** (noise floors, positive controls, equivalence tests, Win-Rate) as the through-line.

## 3. The research steps — question, discovery, possible outcomes

**Step 0 — Calibration pilot** (~20 evals)
- *Q:* what does an eval cost, and is the rating head flat/quantized/wandering?
- *Discover:* a measured cost **band** over the ~505 core + the regime.
- *Outcomes:* (a) cheap + flat → run the whole core, n=5; (b) expensive tail → cut a tier first; (c) wander → richer noise model.

**S1 — Reliable re-measurement** of the surviving AI-security penalty
- *Q:* does the one survivor replicate with error bars + an ordered criterion?
- *Discover:* whether we have a real anchor effect at all.
- *Outcomes:* (a) replicates (~0.30) → solid anchor; (b) weaker/intermittent → lean more on methodology + confabulation; (c) **fails** → striking: even the survivor was noise → cautionary measurement paper.

**S2-trim — Domain-boundedness** (AI vs matched non-AI)
- *Q:* is the effect specific to AI topics?
- *Discover:* whether "AI-ness" is the boundary.
- *Outcomes:* (a) present on AI, equivalence-**absent** on non-AI → odd phenomenon confirmed; (b) present on both → general source effect, the hook weakens; (c) absent on AI control too → narrows further.

**S3-ver — Version-drift exemplar** (Sonnet 4.5 → 4.6, AI-security)
- *Q:* does it survive a model update?
- *Discover:* stable policy vs version artifact.
- *Outcomes:* (a) survives → robust policy; (b) **vanishes on 4.6** → alignment-stage artifact / suppression (strong, citable); (c) shifts → version-sensitive.

**S4 / E1 — Bias vs competence** (prestige × stance 2×2 — the conceptual payload)
- *Q:* is the against-interest credibility move reasoning or artifact?
- *Discover:* what *kind* of thing the source-sensitivity is.
- *Outcomes:* (a) **costly-signaling competence** (against-type credited even when low-prestige) → the model does something epistemically *right*; (b) **prestige-only** → the "bonus" was an artifact, only the coherence penalty is real → *bias*; (c) **coherence penalty** → *bias*; (d) **selective vigilance** (interaction) → credits costly signals only from credible sources → the sleeper, and roughly *correct*.

**S5 — Behavior–testimony dissociation** (confabulation; the completing cell)
- *Q:* can you learn the model's source policy by asking it?
- *Discover:* whether self-report tracks behavior, in both directions.
- *Outcomes:* (a) **full double dissociation** (confabulates where flat *and* misses/misreports the real one) → testimony unreliable both ways → single-channel audits fail; (b) tracks the real effect but confabulates the absent one → asymmetric; (c) tracks → dissociation narrower than n=1 suggested.

**Then —** synthesis + write-up; deferred studies (cross-model breadth, mechanism of AI-ness, human baseline) become "future work."

## 4. Why this is robust
Every step is publishable on **either branch** — a null is as informative as an effect (the whole "exemplary findings, not measures" point). The contribution is the *map* of when source-dependence is real, what kind of thing it is, and why you can't just ask the model — not a single magnitude.

## 5. Status & next action
Nothing run yet (pilot is step 0); Sonnet 4.5 confirmed available; budget €300–500, core fits even pessimistically.
**Next:** ratify the cut → run the calibration pilot on the Windows runner → fill the cost ledger → S1 → S2/S3 → S4/E1 → S5.
