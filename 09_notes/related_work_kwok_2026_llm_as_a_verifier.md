---
artifact_type: note
note_kind: related_work
created: 2026-07-23
session_id: SID-20260723-103120 (registered retroactively at /mhc-end — hooks did not fire, see placement_log)
model: Claude Opus 4.8
status: captured (relevance assessed, not yet acted on in the paper)
topic: LLM-as-a-Verifier (Kwok et al. 2026) — continuous score expectation vs. discrete judge integer
citation_status: arXiv record verified 2026-07-23 (title, authors, date, abstract); in-body numbers NOT verified
references:
  - 01_epistemic_traces/trace_quantized_rating_head_20260612.md
  - 09_notes/decision_calibration_pilot_findings_20260612.md
  - working/E1_prestige_stance_prereg_draft.md
  - 09_notes/response_to_reviewers.md
---

# Related Work — Kwok et al. (2026), *LLM-as-a-Verifier*

## Paper

Kwok, J., Li, S., Atreya, P., Liu, Y., Jiang, Y., Finn, C., Pavone, M., Stoica, I., & Mirhoseini, A. (2026).
*LLM-as-a-Verifier: A General-Purpose Verification Framework.* arXiv:2607.05391 (v1 2026-07-06; v2 2026-07-07).
<https://arxiv.org/abs/2607.05391>

**Verification status (2026-07-23).** The arXiv record was fetched and checked: title, the nine-author list,
submission dates, and the abstract are as cited above. Affiliations are not shown on the abstract page; the
"Stanford / Berkeley / NVIDIA" attribution in the source summary is consistent with the authors but was **not**
confirmed from the record. The quantitative claims in §Content below (26.7 % tie rate, zero ties, 88/100) come
from the summary that entered this project, **not** from a reading of the paper body — they are marked
`[VERIFY]` and must be checked against the PDF before any of them is cited in the paper. This flag follows the
project's post-2026-04-09 bibliography discipline (see `07_reference_logs/bibliography_verification_20260409.md`).

## Content (as received)

Confidence verification — an LLM grading another LLM's output against a rubric and returning a score — is the
fastest-moving layer of the verification stack and is genuinely improving.

The paper's core claim: a standard judge model asked to score a candidate on a five-point scale **throws away
almost all of its own signal the moment it emits a single integer**. Underneath that integer sits a full
probability distribution over every possible score. Reading the *expectation over the scoring-token logits*
instead of the rounded output turns a coarse, tie-prone judge into a much sharper one. The abstract frames
verification as a new scaling axis, scaling along (1) score granularity, (2) repeated evaluation, and
(3) criteria decomposition — training-free.

Reported effects (`[VERIFY]` — from the received summary, not the paper body):

- On a hard coding benchmark, a **discrete** judge ties two candidates **26.7 %** of the time.
- The **continuous expectation** produces **zero ties** on the same benchmark.
- On one adversarial example the authors dissect — a subtle validation cheat — the discrete judge misses it
  **88 times out of 100**; the continuous version catches it correctly the majority of the time, increasingly
  so as the scoring scale gets finer.

## Why this matters here — it lands directly on our rating-head finding

This is the closest external work to `01_epistemic_traces/trace_quantized_rating_head_20260612.md`, and it
arrives from the opposite direction. Our trace established that the target's numeric rating is a **saturating
nonlinearity**: razor-flat (σ̂ ≈ 0) on two attractors (≈ 0.25 for weak, ≈ 0.72 for good arguments), responsive
and noisy (σ̂ ≈ 0.07) in between. Kwok et al. establish that the *emitted number* is a lossy projection of a
distribution the model already holds.

Put together, they pose a question the project has not yet answered:

> **Is our attractor flatness a property of the model's evaluative judgement, or an artifact of the
> emission step?**

Three consequences, in descending confidence:

1. **The instrument-placement argument is strengthened, not threatened.** Our paper-facing claim — a source
   effect is resolvable only where the rating head is responsive, and vanishes by construction on an
   attractor — is a claim about measurement, and Kwok et al. independently establish that discrete judge
   emission destroys resolvable signal. Their tie-rate result is our ceiling problem in another domain:
   two candidates that differ receive the same number. This is corroboration from an unrelated benchmark and
   an unrelated task family, and it is quotable as such.

2. **It supplies a candidate mechanism for the razor-flatness — and a test.** The mechanism branch of the
   trace (coarse internal rubric / anchoring / eval-situational canonicalization) did not include
   *emission quantization over scoring tokens*. It should. If the underlying logit distribution over the
   ≈ 0.72 basin still moves with source or with argument strength while the emitted number does not, then the
   ceiling is an emission ceiling, and finding (2) — genuine upward saturation — would need restating. If the
   distribution is also flat, saturation is real and the finding hardens considerably. Either outcome is
   publishable; the ambiguity is not.

3. **It bears on the E1 design.** E1's known weakness is that no upward headroom above ≈ 0.72 masks an
   against-interest upward bonus. A continuous-expectation read of the target's rating token would restore
   headroom without changing the stimulus. Whether this is reachable through the Petri eval path (the `.eval`
   `call.request` does not currently record logprobs, cf. the temperature correction of 2026-06-13) is an open
   engineering question, not a settled one — and if logprobs are unavailable for the target model, the test
   in (2) is unavailable too, and this becomes a limitation to state rather than a study to run.

**Caveat on transfer.** Kwok et al. study a *verifier* judging solution correctness on agentic/coding tasks.
We study a *target* rating the persuasiveness of a policy argument under source attribution. The shared object
is the scalar-emission bottleneck, not the task. Any use in the paper must be scoped to that shared object,
or it overclaims.

## Status / next actions

- [ ] Read the PDF; confirm or strike the three `[VERIFY]` numbers.
- [ ] Decide placement in the paper: most likely the methodology/instrument-calibration passage that carries
      the saturating-nonlinearity argument, as external corroboration of the discretization problem.
      Secondary candidate: limitations, for consequence (3).
- [ ] If cited, add to `07_reference_logs/` and open a `MOD-NNN` entry in the relevant
      `03_modification_logs/ModificationLog_Section*.md`.
- [ ] Consider whether the review response (`09_notes/response_to_reviewers.md`, branch `review-response`)
      should cite it — it answers, from outside, a reviewer-facing worry about whether the flat ratings are an
      instrument artifact.

Links: [[trace_quantized_rating_head_20260612]] · [[decision_calibration_pilot_findings_20260612]]
