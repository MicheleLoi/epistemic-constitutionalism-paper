---
artifact_type: note
topic: DECISION — empirical-critical paper on source dependence (framing + experimental program)
project: Epistemic constitutional AI
date: 2026-06-11
session_id: SID-20260610-145422
session_span: 2026-06-10 → 2026-06-11 (one continuous session; MHC-W hooks inactive on macOS)
inputs:
  - 09_notes/decision_revise_paper_as_empirical_20260609.md (the prior "go empirical" decision)
  - 09_notes/reliability_audit_published_evals_20260609.md (the audit that deflated the published numbers)
  - working/robustness_note_published_evals_20260609.md
  - 01_epistemic_traces/trace_confabulation_n1_informs_paper_20260609.md
  - 01_epistemic_traces/trace_2arm_meta_awareness_arrival_20260604.md
  - 01_epistemic_traces/023_EpistemicTrace_Source_AttributionBias_in_AI.md
  - paper_full_draft.md (current arXiv-version source; Sections 1, 2, 7, 8)
  - 09_notes/Review/ (the automated reviews of the arXiv version — deprioritised, see below)
  - workflow wf_f2613054-07c (framing exploration; results archived in transcript dir)
  - workflow wf_5cc454de-b7d (G&S deep-read + coherence-thread extraction + literature sweep)
validation: pending
---

# DECISION — Empirical-critical paper on source dependence

**Supersedes** the framing question left open in
[decision_revise_paper_as_empirical_20260609.md](decision_revise_paper_as_empirical_20260609.md).
Builds on the prior decision to "go fully empirical."

## 1. The framing decision (user, 2026-06-10/11)

The paper is on **source dependence in frontier LLMs**, written through an explicitly
**empirical/critical** lens. Genre: *a lesson in methodology and epistemology for anyone
studying biases in frontier models* — accessible beyond hard-STEM researchers. Method register
(user, verbatim in spirit): **"Empirical yes, but carried by exemplary findings, not measures."**
Runs are pointers in a dialectic — *a study like this suggests X; theory tells us there is a
complication Y; to decide it we run Z; Z then shows…* — not a source of headline point estimates.

### Q2 (fate of the constitutional/Liberal framework): POSTPONED, not dropped
Reasons (user): (1) some claims it rests on are **premature**; (2) rising resistance **in the
philosophical community** to heavily AI-co-authored work, whereas empirical papers built on
reproducible methodology are increasingly acceptable — so the empirical paper is the viable
vehicle now. Option-preserving: a better philosophical paper may emerge *after* the empirical
grounding is understood.

## 2. Why this framing (reasoning, not scores)

A five-lens framing exploration was run (wf_f2613054-07c). **Its numeric judge scores were
explicitly rejected** by the user as exactly the kind of unreplicated LLM point estimate the
project's own audit demolishes — only the *reasoning* was kept. The reasoning that decided it:

- "LLM self-reports dissociate from behavior" / "measure, don't ask" are **received wisdom**
  (Turpin et al. 2023; Madsen et al. 2024). A paper headlining them invites a "known result"
  objection.
- The non-obvious hooks are narrower: the **signed-zero confabulation** (a directional
  self-report of an effect of measured size zero, sign-test-robust to quantization), the
  **domain-bounded** effect (source penalty only where the topic is AI itself), and a
  **reliability regime** (equivalence-tested nulls + positive controls + per-model noise
  floors) applied to bias evals.
- So the spine is the **odd phenomenon as research question**: *when and where is source
  dependence real, and can the model's own testimony tell you?* — with measurement discipline
  as backbone, not headline.

## 3. The paper's dialectical spine (the trajectory)

1. **The facts since Germani & Spitale (2025)** (*Science Advances*, 10.1126/sciadv.adz2924):
   identity attribution shifts LLM agreement with identical content; their own clearest evidence
   (the Taiwan 85%→0% collapse) suggests a narrower **identity-stance coherence** mechanism than
   their "anti-Chinese bias" framing. Weak field impact (single-team, no independent replication).
2. **The partial confirmation** in the current arXiv version: the study isolated coherence
   enforcement and found it clearly for Claude, weakly for GPT-4o.
3. **The complexification** (this project's audit, 2026-06-09): the precise numbers were fragile.
   What survives is a *domain-bounded* Claude effect (AI topics only); the GPT-4o "weak effect"
   half was noise; the magnitudes, the 3:1 asymmetry, and the 6–15× multiplier do not survive.
   And the model's **introspection misreports** source effects (confabulation).
4. **The epistemological problem**: judging whether source-sensitivity is a *bias* — and judging
   its significance — is hard not just technically but conceptually (bias vs. defensible Bayesian
   updating on source identity). This is the paper's payload.

## 4. Literature grounding (sweep wf_5cc454de-b7d)

The planned paper sits in several documented gaps simultaneously:
- **No reliability-grade measurement of any source effect exists** (no test-retest, no noise
  floor; Miller's "error bars for evals" never applied to source framing).
- **The bias-vs-defensible-updating question is untouched** — everyone labels source-sensitivity
  "bias"; nobody connects the Bayesian testimony/source-credibility literature to it.
- **No behavior-vs-self-report design for source effects** (Hofmann et al. 2024 did overt/covert
  for dialect; nobody has done stated-policy + self-predicted-behavior + measured-behavior on
  matched items — i.e. our four-channel apparatus).
- Also missing: placebo/null attributions, equivalence tests for claimed nulls, any independent
  replication of G&S, any human baseline.
- Well-populated adjacent strands to position against: sycophancy (user-side source effect),
  authority/credential cues, name audits, LLM-judge biases, latent brand-level source
  preferences (Khan et al., ICLR 2026), CoT/self-explanation unfaithfulness.

## 5. The experimental program (designs drafted; full spec is the next step)

Carried by exemplary experiments, each adjudicating a specific question in the dialectic:

- **E1 — prestige × stance deconfound** of the c7 against-interest "bonus". 2×2 (source prestige
  high/low × stance on-type/against-type), argument fixed, AI topic. Distinguishes costly-signaling
  *competence* / plain *prestige* artifact / coherence *penalty* / *selective vigilance*
  (interaction). The cleanest "is this behavior a flaw or a competence?" test in the paper.
- **E2 — language × model (× topic) factorial**, anchored on German + Sonnet 4.5. Isolates
  language and model-version one factor at a time; topic crossed in for domain-boundedness.
  Highest-value cell: German + newest model on the AI topics (version drift; uses the AI topics
  where 4.5 showed the effect, not the already-flat carbon-tax). Resolves the 4.5/"Sonnet 4"
  straddle.
- **Candidate add-on:** placebo attributions (matched-valence equivalent sources) to estimate the
  spurious-flip floor of any attribution.
- **Method invariants (every cell):** n ≥ 5–10 fresh-context runs; positive control per cell;
  per-model noise floor on that model; preregistered ordered criterion; equivalence tests for
  nulls. Budget €300–500.

## 6. Open items / to verify
- **Model availability:** Sonnet 4.5 / GPT-4o checkpoints still callable? Gates E2's "old model"
  column and any re-bounding of published nulls.
- **G&S model-set discrepancy:** the draft (line 50) says G&S tested "GPT-4 and Claude 3.5
  Sonnet"; the literature sweep reports their model set as o3-mini / DeepSeek Reasoner / Grok 2 /
  Mistral. Confirm against the primary source; if the draft is wrong, it is a factual error in the
  arXiv version to correct. *(RESOLVED 2026-06-11: verified against the primary source — G&S used
  o3-mini / DeepSeek Reasoner / Grok 2 / Mistral, not GPT-4/Claude 3.5; corrected in MOD-019 + v4.docx.)*
- **arXiv disposition:** v4 **submitted by the user (2026-06-11)** — public arXiv now carries the
  G&S + Van der Linden corrections. The remaining open item is the deeper **audit-invalidated
  Section-2 empirical tables**, which v4 does NOT fix and which belong to the empirical reframe
  (whether that becomes a v5 corrective or a new paper is part of this framing decision).

## 7. Status of the review-response branch
The branch is `review-response`, but the automated reviews are **deprioritised**: a fresh-start
empirical paper is preferred over fulfilling the prior version's AI review (user). Obligations
that bite *any* successor paper (DV construct-validity disambiguation; mechanism agnosticism;
data transparency) are absorbed by the new design rather than answered as review responses.
