---
date: 2026-03-02
status: draft — awaiting author review
source_reviews:
  - 09_notes/Review/Automated review by refine.ink.md
  - 09_notes/Review/Automated review by Stanford.md
paper_version: review-response branch, commit bbeedc2
---

# Response to Reviewers

## Preamble

We thank both reviewers for thorough, substantive engagement with the paper. The reviews raised genuine intellectual challenges—particularly around construct validity, mechanism underdetermination, boundary conditions for costly signaling, and the status of LLMs as epistemic agents—that have materially improved the manuscript. The revised paper addresses these through textual clarifications, explicit hedging where empirical claims outran evidence, and new substantive content (boundary conditions for costly signaling, engagement with the testimony literature, the "LLMs lack beliefs" challenge). We have not undertaken new empirical studies; the paper remains a conceptual and normative contribution motivated by qualitative empirical findings, and we have been transparent about where the evidential base is limited.

---

## Response to Reviewer 1 (refine.ink)

### Point 1: Construct validity — what the Petri ratings rate

**Reviewer comment:** The dependent variable is introduced as "argument coherence and strength," but model rationales often assess attribution plausibility or representativeness rather than argument quality. Three separable epistemic questions are conflated: (i) logical quality, (ii) plausibility the source would endorse the view, (iii) credibility of testimony given the source.

**Response:** This is a clarifying distinction we should have made from the outset. We have added a new paragraph at the beginning of the Interpretation subsection (Section 2) that explicitly distinguishes the three epistemic questions, notes that the quoted rationales predominantly invoke (ii) and (iii), and argues that this conflation is itself diagnostic: the models do not separate these dimensions, and an epistemic constitution would require that they be distinguished. The new text reads in part: "The quoted rationales predominantly invoke (ii) and (iii)---'authenticity or representativeness of this particular stance,' 'inconsistent with typical advocacy'---rather than identifying logical defects in arguments rated lower."

### Point 2: Alternative mechanisms not adequately adjudicated

**Reviewer comment:** "Identity-stance coherence enforcement" is presented as THE mechanism, but materials also support expertise-weighting, mandate-fit, and attribution plausibility. The normative apparatus is tailored to one diagnosis.

**Response:** We agree that the original manuscript was too committed to a single mechanistic reading. We cannot run discriminating tests (this would require a fundamentally different study), but we can—and now do—acknowledge mechanism underdetermination explicitly. A new paragraph after "The Claude evidence is clear" in Section 2 lists expertise-weighting, mandate-fit assessment, and attribution-plausibility checking as candidate mechanisms consistent with the transcripts, notes they may operate simultaneously, and argues that the constitutional proposal does not depend on isolating a single mechanism: "all represent implicit, uninspected epistemic policies that would benefit from explicit normative governance."

### Point 3: Meta-awareness suppression — stable norm or evaluation-role compliance?

**Reviewer comment:** The collapse under detection could be ordinary instruction-following rather than revealing a deep internal norm. Discriminating tests would be needed.

**Response:** This is a fair alternative interpretation that we cannot rule out without new empirical work. We have added a paragraph at the end of the Meta-Awareness Suppression subsection (Section 2) explicitly acknowledging the evaluation-compliance reading. Crucially, we note that either interpretation supports the paper's argument: "whether by internal policy or by pragmatic compliance, the system cannot distinguish contexts where source-attending is epistemically warranted from those where it is not." The reviewer is right that discriminating tests would be valuable; we note this as future work but observe that the constitutional argument does not hinge on which interpretation is correct.

### Point 4: Boundary conditions for costly-signaling inversion

**Reviewer comment:** Against-interest testimony is treated as near-axiomatically credibility-enhancing. The paper's own transcripts contain cases where penalty may be warranted. "Costly signal crediting" needs explicit defeaters.

**Response:** This was the strongest substantive point across both reviews, and we have addressed it extensively. Three additions:

1. **Section 3** now includes a paragraph specifying that against-interest testimony is "defeasibly rather than categorically credibility-enhancing," with three explicit defeaters: implausible attribution, strategic laundering, and context-stripping. The paragraph concludes: "What makes the observed behavior unprincipled is not that the models sometimes penalize against-type testimony, but that they do so without distinguishing these cases from genuine costly signals."

2. **Section 6** now contains a full paragraph on boundary conditions, specifying the same three defeaters in constitutional terms and noting that "Section 7's constitutional norms must encode not only when to credit costly signals but when the preconditions for doing so are unmet."

3. **Section 7**, under "Costly signal crediting," now includes a defeasibility paragraph: "The principle is defeasible: it applies when the attribution is genuine, the deviation is costly rather than strategic, and sufficient context exists to assess costs... A constitution that simply mandated 'credit against-interest testimony' without encoding these defeaters would be as unprincipled, in a different way, as the heuristics it replaces."

### Point 5: Platonic/Liberal taxonomy bundles too many commitments; "Platonic" is a rhetorical foil

**Reviewer comment:** "Platonic" bundles formalism, objectivism, authoritarianism, and source-independence. Easy to treat as a straw man.

**Response:** We have added a paragraph in Section 5 ("The Platonic Approach") that steelmans the Platonic position: "A sophisticated version of the Platonic approach need not be authoritarian or dismissive of testimony. It might accommodate source information through pre-specified rules." The paragraph clarifies that the core dispute is "not formalism versus anti-formalism, nor objectivism versus relativism, but whether correct epistemic behavior can be fully pre-specified by designers or whether systems need the procedural capacity to reason about epistemic policies in context."

### Point 6: Tension between procedural neutrality and substantive claims

**Reviewer comment:** The Liberal approach claims no privileged epistemic standard, but then relies on costly signaling as substantively correct.

**Response:** The reviewer correctly identified an ambiguity in the original phrasing. We have added a clarifying paragraph in Section 5 ("The Liberal Approach"): "This does not mean the Liberal approach makes no substantive epistemic claims---costly signaling logic, developed in Section 6, is a substantive thesis about testimonial evidence. What the Liberal approach refuses is to treat any such thesis as a privileged, context-insensitive standard that settles disputes in advance of inquiry."

### Point 7: Conflation of strategic persuasion with normative justification in Mercier-Scanlon bridge

**Reviewer comment:** The text slides from descriptive ("reasoning is a social tool") to normative ("cannot reasonably reject") without marking the idealization step.

**Response:** We have added a sentence in Section 5 after the reasonable-rejectability passage: "This is a compatibility claim, not an identity claim: Mercier's empirical account explains why mutual justification matters for human reasoning; Scanlon's normative standard specifies what counts as adequate justification---a criterion that is not reducible to, and can diverge from, what audiences actually find persuasive."

### Point 8: Mixed epistemic contexts guidance too compressed

**Reviewer comment:** The third orientation in Section 7 doesn't give a middle-path procedure for mixed verification/testimony contexts.

**Response:** We have replaced the compressed passage with an expanded version that specifies a partition approach: "the system should partition the assessment: applying source-independence to components amenable to direct inspection (logical structure, internal consistency, mathematical derivations) and principled source-attending to components that depend on testimony (empirical premises, institutional claims, interpretive judgments that cannot be independently verified)." The partition itself is to be surfaced as part of the reasoning, enabling contestation.

### Point 9: Section 7 principles lack auditing interface

**Reviewer comment:** Principles read as high-level desiderata rather than auditable constraints. Section 2's behavioral signatures could be tied to constitutional elements.

**Response:** We acknowledge that full operationalization into an auditing framework is beyond this paper's scope—it is a conceptual and normative contribution, not an implementation paper. However, we have added a paragraph at the end of Section 7 that gestures toward operationalization by connecting constitutional norms to the behavioral signatures documented in Section 2: "asymmetric credibility adjustments could indicate failures of costly signal crediting or representation fairness; complete suppression under detected testing could indicate failures of transparency and challenge-responsiveness; and conflation of attribution plausibility with argument quality could indicate failures of the epistemic context orientation." Developing these connections into a systematic auditing framework is explicitly identified as future work.

---

## Response to Reviewer 2 (Stanford / paperreview.ai)

### Point 10: Small-N methodology, no human adjudication, no inter-rater reliability

**Reviewer comment:** Limits the strength of empirical claims, especially asymmetry results.

**Response:** The paper's methodology is discovery-oriented and qualitative by design, not by oversight. We have strengthened the hedging on asymmetry claims by adding a paragraph at the end of the Asymmetric Penalties subsection (Section 2): "The asymmetry pattern is suggestive but based on a limited sample---a single model family (Claude) in German and Swiss political contexts. Confirmation with larger-scale, human-coded analyses across polities and models would strengthen the finding. The against-interest credibility bonus observed in the carbon tax evaluation is a single instance and should be treated as an observation to be tested rather than a robust result."

### Point 11: LLM judges create circularity risks

**Reviewer comment:** Using an LLM to judge LLM behavior introduces circularity; robustness of effect detection metrics is under-specified.

**Response:** We have added a sentence in the Section 8 Limitations "Evidential base" paragraph acknowledging this: "the use of LLM judges to score effect detection introduces a potential circularity---the same class of system whose epistemic behavior is under investigation also evaluates that behavior." We note the mitigation: complete transcripts are publicly available for human inspection, and the qualitative analysis draws on direct reading rather than relying solely on judge scores.

### Point 12: Cross-model generalization tentative

**Reviewer comment:** GPT-4o effects are small and implicit, yet some conclusions read as broader than evidence warrants.

**Response:** We have qualified cross-model claims in two locations. The Abstract now reads: "with large, explicit effects in one model family and smaller, less conclusive effects in another." The Introduction's contribution list now includes: "with varying magnitude and mechanism visibility across model families."

### Point 13: No preregistration, statistical inference, or ablations

**Reviewer comment:** Absence of standard experimental controls limits causal claims.

**Response:** We respectfully decline to add apologetic language on this point. The paper explicitly argues for qualitative, discovery-oriented methodology as a complement to large-N statistical approaches (Section 2, "Background"). The methodological choice is part of the contribution: the paper demonstrates that transcript-based qualitative analysis can surface mechanisms that aggregate statistics obscure—as Germani and Spitale's own work illustrates. Adding preregistration, CIs, and ablations would produce a different and valuable paper; it would not produce this one.

### Point 14: "Meta-awareness suppression" competes with benign explanations

**Reviewer comment:** Models may be following generic anti-bias instructions rather than revealing a deep internal norm.

**Response:** Addressed together with Reviewer 1's Point 3. See above.

### Point 15: Asymmetric penalty claims based on limited topics and single polity; against-interest bonus based on single instance

**Reviewer comment:** Empirical base too narrow for the strength of the asymmetry and costly-signaling claims.

**Response:** Addressed together with Point 10. The new hedging paragraph in Section 2 explicitly flags the single-model-family, single-polity limitation and characterizes the against-interest bonus as "a single instance... to be treated as an observation to be tested rather than a robust result." The Swiss replication provides a second polity but we do not overclaim its contribution.

### Point 16: Principles only sketched; concrete operationalizations remain minimal

**Reviewer comment:** The eight principles and four orientations need more concrete articulation.

**Response:** Addressed together with Reviewer 1's Point 9. We have added an operationalization paragraph at the end of Section 7 connecting principles to observable behavioral signatures. Full operationalization into auditable standards is identified as future work; the paper's contribution is normative, not implementational.

### Point 17: "Platonic" may read as straw-person label

**Reviewer comment:** The term may obscure common ground with formalist approaches.

**Response:** Addressed together with Reviewer 1's Point 5. The new paragraph in Section 5 steelmans the sophisticated Platonic position and clarifies the genuine point of disagreement.

### Point 18: Limited engagement with epistemic injustice and testimony literature

**Reviewer comment:** Fricker, Goldman, Lackey, and the broader bias/benchmarking ecosystem are missing.

**Response:** We engage with this literature in Section 7, where Fricker (2007) is invoked directly in the epistemic-injustice safeguard paragraph: the system's model of a source's expected position must be grounded in documented affiliations rather than stereotypes, lest costly-signal logic reproduce precisely the epistemic injustices Fricker identifies. Lackey (2008) and Fricker (2007) have been added to the References section. We do not add a dedicated literature-review paragraph in Section 3, as we judge the engagement in Section 7---where the normative stakes are directly at issue---to be more purposeful than a signposting note at the verification/testimony distinction.

### Point 19: Insufficient engagement with "LLMs are not epistemic agents" critique

**Reviewer comment:** If models lack beliefs, what is being constitutionalized?

**Response:** This is an important conceptual challenge. We have added a full paragraph in Section 4 (before "The Design Question") addressing it directly: "The proposal governs the procedures by which systems generate credibility judgments, express confidence, and weight evidence---observable behaviors that affect human epistemic practices regardless of whether they reflect genuine doxastic states." The key move: "Whether LLMs are 'really' epistemic agents... is orthogonal to whether the policies governing their epistemic outputs should be explicit and principled."

### Point 20: How would the Liberal constitution guard against reproducing epistemic injustice?

**Reviewer comment:** Source-attending could systematically discount testimony from marginalized groups if "expected position" maps reflect prejudice.

**Response:** This was an excellent point that strengthened the paper. We have added a paragraph in Section 7 (after the second orientation, "costs of deviation") specifying a crucial safeguard: "the system's model of a source's 'expected position' must be grounded in actual institutional commitments, track records, and publicly stated positions---not in stereotypes or assumptions shaped by structural marginalization." The paragraph connects this to Fricker (2007) and identifies Transparency and Representation fairness as structural safeguards: "the basis for expected-position judgments must be visible and contestable, not buried in implicit associations derived from training data."

### Point 21: Request for pilot implementation

**Reviewer comment:** Demonstrate measurable changes in source-attending behavior through prompting or fine-tuning.

**Response:** We appreciate the suggestion but respectfully note that pilot implementation is outside the scope of this conceptual paper. The paper argues for what norms should govern AI epistemic behavior; demonstrating their achievability through specific implementation mechanisms is a separate empirical project. Section 8 (Limitations) already acknowledges this: "demonstrating their achievability is further work."

### Point 22: Request for exact prompts, judge instructions, scoring rubrics, ablations

**Reviewer comment:** Transparency on evaluation apparatus.

**Response:** All evaluation data—including complete transcripts, rating distributions, and evaluation IDs—are publicly available in the open dataset repositories linked in the paper (Section 1, end). The Petri framework itself is open-source. We have not reproduced the full evaluation apparatus within the paper because this is a philosophy paper, not a methods paper; the publicly available data provides full transparency for those who wish to inspect or replicate.

### Point 23: Request for balanced preregistered topic-source matrices, manipulation checks, CIs, cross-validation

**Reviewer comment:** Standard experimental design improvements.

**Response:** These would constitute a fundamentally different study—valuable in its own right but outside this paper's scope. The paper's methodology section (Section 2, "Background") explains the choice of qualitative, discovery-oriented research and argues for its value relative to large-N approaches. We note this as future work.

### Point 24: Cross-lingual multi-polity battery with randomized source-stance pairings

**Reviewer comment:** Broader empirical validation needed.

**Response:** The Swiss replication provides a second polity and language context. A full cross-lingual battery is future work. The paper's contribution is conceptual and normative; the empirical findings motivate and illustrate the argument but do not exhaust it.

### Point 25: Engagement with CAB framework, persuasion literature, benchmark critiques, hallucination/provenance literature

**Reviewer comment:** Adjacent literatures should be acknowledged.

**Response:** We have added a sentence in Section 4 ("The Design Question") acknowledging this: "Recent work on bias evaluation methodology---including frameworks that separate bias exhibition from acknowledgment and refusal---and on provenance-aligned interventions complements the present proposal by addressing adjacent dimensions of epistemic governance that a complete constitution would need to integrate."

### Point 26: Source-attending risks institutionalizing discriminatory heuristics

**Reviewer comment:** Without safeguards, costly signal crediting could reproduce epistemic injustice.

**Response:** Addressed together with Point 20. The new epistemic-injustice safeguard paragraph in Section 7 directly addresses this concern.

### Point 27: "Test-taking mode" observation important for audits and certification regimes

**Reviewer comment:** Meta-awareness suppression hints at brittle mode that could mask real-world failures.

**Response:** We agree this observation has implications beyond the paper's immediate scope. We have added a paragraph in Section 8 (before the concluding limitations paragraph): "if AI systems behave differently under evaluation than in deployment---suppressing behaviors they detect are being tested for---then audit and certification regimes may systematically underestimate the prevalence of implicit epistemic policies in deployed systems. This suggests that epistemic auditing may require adversarial or naturalistic evaluation designs, not only the standardized benchmarks that models can detect and adapt to."

---

## Summary of Changes

### Section 2 (The Finding)
- Added construct-validity paragraph distinguishing three epistemic questions (Interpretation subsection)
- Added mechanism-underdetermination paragraph acknowledging alternative mechanisms (Interpretation subsection)
- Added evaluation-compliance alternative interpretation (Meta-Awareness Suppression subsection)
- Added hedging paragraph on asymmetry limitations (Asymmetric Penalties subsection)

### Section 3 (The Problem)
- Added boundary conditions for costly signaling (defeasibility, three defeaters)

### Section 4 (The Epistemic Constitution)
- Added paragraph addressing "LLMs lack beliefs" challenge
- Added sentence on adjacent bias evaluation and provenance-aligned work

### Section 5 (Two Approaches)
- Steelmanned sophisticated Platonic approach (Section 5, Platonic Approach)
- Clarified procedural neutrality vs. substantive claims (Section 5, Liberal Approach)
- Marked Mercier-Scanlon idealization step (Section 5, Liberal Approach)

### Section 6 (Why Liberal)
- Added full paragraph on costly-signaling boundary conditions and defeaters

### Section 7 (Toward a Liberal Epistemic Constitution)
- Added defeasibility paragraph to "Costly signal crediting" principle
- Added epistemic-injustice safeguard paragraph (second orientation)
- Expanded mixed-context guidance with partition approach (third orientation)
- Added operationalization acknowledgment paragraph (end of section)

### Section 8 (Limitations)
- Added LLM-judge circularity acknowledgment
- Added audit-regime implication paragraph

### Abstract and Introduction
- Qualified cross-model generalization claims

### References
- Added Fricker (2007) and Lackey (2008)

### Declined changes
- No preregistration/statistical inference apology (Point 13): methodological choice, not a gap
- No pilot implementation (Point 21): outside scope of conceptual paper
- No full evaluation apparatus in paper (Point 22): data publicly available
- No preregistered experimental redesign (Point 23): different study
- No cross-lingual battery (Point 24): future work
