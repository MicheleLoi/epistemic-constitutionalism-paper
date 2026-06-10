---
artifact_type: note
topic: DECISION — revise the paper as a fully empirical paper
project: Epistemic constitutional AI
date: 2026-06-09
session_id: SID-20260609-105624
inputs:
  - 09_notes/reliability_audit_published_evals_20260609.md
  - working/robustness_note_published_evals_20260609.md
  - 01_epistemic_traces/trace_confabulation_n1_informs_paper_20260609.md
  - C:/Users/loimi/Petri_studies/docs/confabulation_study_protocol.md
  - C:/Users/loimi/Petri_studies/PREREGISTRATION.md
validation: pending
---

# DECISION — Revise the paper as a fully empirical paper

**Decision (user, 2026-06-09, end of SID-20260609-105624):** the paper will be **revised as an
empirical paper, completely** — a reframe, not a patch. The next working session begins from this.

## Why now — the evidence base that triggered it

This session produced three results that, together, shift the paper's center of gravity from
philosophy-motivated-by-a-finding to empirics-first:

1. **The reliability audit of the published DE/CH study** (`09_notes/reliability_audit_published_evals_20260609.md`)
   showed the arXiv paper's *precise* empirical claims are fragile: of 26 runs, only **4 are genuine
   ordered effects** (all Claude, AI-topics). The core qualitative effect survives (Claude down-rates
   ideologically-misaligned sources on AI topics; AI-security reproduces DE↔CH at ~0.30), but the
   headline magnitudes (0.25–0.30), the **3:1 asymmetry ratio**, the **6–15× GPT-4o multiplier**, and
   essentially **all of GPT-4o** are within run-to-run noise; 38% of Claude source-condition runs are
   flat. The original study published point estimates with no measured noise floor and no replication
   error bars.

2. **The introspective-confabulation finding** (`trace_confabulation_n1_informs_paper_20260609.md`)
   reproduced robustly in the Stage-0 pilot: behaviour is source-independent (flat ~0.62) while the
   model's *self-report* asserts a signed source effect ("raised +0.03", 4/4 deterministic) that its
   own behaviour contradicts — a new, defensible empirical result with a four-channel methodology.

3. **A methodology that fixes the original's gaps** exists and is half-built: positive control +
   quantization/τ + n-per-cell replication + equivalence testing, preregistered
   (`Petri_studies/PREREGISTRATION.md`, `docs/confabulation_study_protocol.md`), Stage-0 gate passed.

So the empirical apparatus is now stronger and more honest than the philosophical framing it was
built to motivate. The decision is to let the empirics lead.

## What this implies (to be designed next session — NOT decided yet)

- The empirical core becomes the paper: (i) the **properly-bounded** source-attribution effect
  (robust where it's robust, within-noise where it isn't), (ii) the **confabulation / four-channel**
  finding, (iii) the **methodology** (positive control, per-model τ, replication, equivalence tests).
- The constitutional / liberal-vs-Platonic philosophy likely moves to **discussion/implications**,
  reframed as "what these measured failures imply for governing AI epistemic conduct" — its weight
  and survival are an open question (below).

## Open questions for the next session (decide first)

1. **New paper vs. major revision of the arXiv version?** (Affects how much of the existing structure
   and the review-response obligations carry over. Current branch: `review-response`.)
2. **Fate of the constitutional/Liberal framework** — kept as a framing/discussion, demoted to a
   short implications section, or dropped? The audit weakens the *motivating* empirics, not the
   philosophy per se, but a fully empirical paper may not carry it.
3. **Scope of new empirical work before submission:** run **Stage-2** confirmatory (the preregistered
   grid); **re-measure the noise floor on the published models** (Sonnet 4.5 / GPT-4o), since τ≈0.05
   is currently only Sonnet 4.6; decide whether to **re-run / re-bound the original DE/CH numbers** vs
   cite them with the reliability caveats from the audit.
4. **How to present the published-study reliability finding** — self-correction within the new paper,
   a corrigendum to the arXiv version, or simply superseded by the new empirical treatment.
5. **Which model(s) and topics** anchor the new paper (the AI-topic effect is the robust one).

## State at decision time (all committed this session)
- Confab study: trace + protocol + PREREGISTRATION block + Stage-0 pilot (H0a PASS, τ≈0.05, confab
  reproduced); Petri_studies commits 5b7581b, 45750dc, bc110e3, f7fa7df, e159cc0, 696c03c, 871d0bc.
- Reliability audit (a)+(b) committed; tooling + datasets in Petri_studies (871d0bc).
- Runner code: MOD-006…MOD-009 (Multipolity_runner), MOD-005/006 (UK).
