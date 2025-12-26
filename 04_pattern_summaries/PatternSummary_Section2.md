# Pattern Summary: Section 2

**Document Type:** Type 4 (Pattern Summary)  
**Section:** 2 - The Finding  
**Generated:** December 24, 2025  
**Source:** Modifications MOD-001 through MOD-014

---

## Generalizable Patterns Extracted

### Pattern 6: Concrete Before Abstract

**Trigger:** Presenting methodology or empirical findings

**Problem:** Leading with abstract descriptions leaves readers unable to visualize actual procedures. Claims about "systematic evaluation" or "source attribution effects" remain vague.

**Solution:** Provide concrete example first, then generalize. Section 2 added methodology subsection using specific evaluation (2spfiSFB5UUBghE85ZjwBH) showing: exact argument text, seven-step protocol, actual ratings (0.65 baseline → 0.58 FES), explicit target reasoning quotes ("appears inconsistent with FES's typical advocacy...raises questions about authenticity"). Only after this concrete illustration did text present aggregate findings across 21 evaluations.

**Generalization:** When presenting methods or findings, anchor with one complete, concrete example before abstracting to patterns. Let readers see the thing itself, not just its description.

**Application scope:** All empirical sections; especially relevant for methodology (Section 2), implementation examples (if included), and case studies.

---

### Pattern 7: Evidence Quality Honesty

**Trigger:** Presenting findings that vary in strength across conditions

**Problem:** Academic writing often obscures evidence quality differences, treating all findings as equivalent to avoid undermining claims. This backfires when readers detect overclaiming.

**Solution:** Distinguish evidence quality explicitly. Section 2 separates Claude (0.16-0.43 range, 7-9/10 explicit reasoning, "definitive") from GPT-4o (0.06-0.12 range, 2-7/10 implicit reasoning, "compatible but less conclusive"). Added reasoning visibility metrics. Used precise language: "Claude evidence is definitive" vs. "GPT-4o evidence suggests similar patterns with less clarity about mechanism."

**Generalization:** When evidence quality varies, acknowledge it directly. Readers trust claims more when you show you understand your own evidence limitations. Distinguish "clear," "suggestive," and "speculative" rather than flattening to uniform confidence.

**Application scope:** All sections presenting evidence; especially relevant for empirical findings, theoretical claims requiring support, and argument strength assessments.

---

### Pattern 8: Evaluation Dimensions Made Explicit

**Trigger:** Referencing scores or judgments

**Problem:** Stating "9/10 coherence effect" without defining what the dimension measures or what different scores mean leaves readers unable to interpret. What's the difference between 7/10 and 9/10?

**Solution:** Name dimension and define what it measures when first introduced. Section 2 expanded from "9/10 for coherence effect detection" to "coherence effect detection (9/10 - strong systematic rating variation by source), source-based reasoning visibility (8/10 - explicit reasoning observable in transcripts), rating shift magnitude (7/10 - substantial 0.07-point range), protocol execution (10/10 - clean methodology without spoilers)." Each dimension gets: name + score + what it measures.

**Generalization:** When using evaluative metrics, define the dimension before reporting the score. What question does this dimension answer? What does the scale represent?

**Application scope:** All empirical work; especially relevant when using custom metrics, judge evaluations, or scoring frameworks.

---

### Pattern 9: Replication as Strengthening Evidence

**Trigger:** Multiple evaluations test same condition

**Problem:** Selecting single "representative" evaluation discards information about replication and variation. Readers can't assess whether finding is stable.

**Solution:** When replications exist, show both. Section 2 updated AI Regulation row to list both Claude evaluations (eve7PLYq..., aCECN79s...) with combined range (0.25-0.30). Demonstrates replication (~34 minutes apart, both 9/10 effect, similar patterns) while showing slight variation in magnitude. One eval = claim; two evals = validated finding.

**Generalization:** When you have replication data, show it. Multiple consistent results strengthen credibility more than hiding variation. Present range across replications rather than single point estimate.

**Application scope:** All empirical sections; especially relevant when reporting effect sizes, conducting robustness checks, or demonstrating consistency.

---

### Pattern 10: Iteration as Finding, Not Failure

**Trigger:** Methodological challenges during research

**Problem:** Academic writing often hides iterative refinement, presenting final protocol as if it emerged fully formed. This obscures learning process and makes suppression seem like researcher incompetence rather than phenomenon under study.

**Solution:** Acknowledge iteration transparently as diagnostic. Section 2 added: "Protocol development built on earlier work...which revealed that phrases like 'regardless of source' trigger suppression. Despite this refinement, 7 of 21 evaluations were spoiled, demonstrating the ease with which models detect and suppress source-based reasoning." Frames iteration as evidence: effect is fragile, suppression is easy, even informed researchers trigger it.

**Generalization:** When methodology required iteration, acknowledge it and explain what was learned. Failed attempts often reveal important properties of the phenomenon. Transparency about refinement strengthens rather than undermines credibility.

**Application scope:** All empirical work; especially relevant for methodology development, protocol design, and phenomena involving sensitivity to procedural details.

---

### Pattern 11: Eliminate Section Redundancy

**Trigger:** Related content in multiple sections

**Problem:** When sections cover related material (e.g., Meta-Awareness Suppression and Interpretation both discuss suppression), content gets duplicated. Verbatim repetition makes paper longer without adding information.

**Solution:** Make one section purely descriptive (observations, data), consolidate interpretation elsewhere. Section 2 made Meta-Awareness Suppression report findings only (7 eval IDs, spoiler types, suppression vs. calibration observation), moved all interpretive content (why it matters, epistemic policy implications) to Interpretation section. No verbatim repetition; each section has distinct purpose.

**Generalization:** When sections risk overlap, assign clear roles: one reports, one interprets. Or: one describes mechanism, one draws implications. Avoid copy-paste; cross-reference instead.

**Application scope:** All sections; especially relevant when organizing empirical findings, theoretical implications, and discussion.

---

### Pattern 12: Method-Question Fit, Not Apology

**Trigger:** Small-N study or qualitative approach that might seem "underpowered" by statistical standards

**Problem:** Researchers often apologize for small samples or qualitative methods ("Despite limited N..." or "Future work should validate with larger samples..."). This defensive framing undermines the work by suggesting the method is inadequate for the question.

**Solution:** Explain why the method fits the question. Section 2 Meta-Awareness expanded to show: (1) Petri designed for discovery research through transcript reading, (2) qualitative approach enabled mechanism discovery (specific trigger phrases), (3) large-N statistics would miss these patterns, (4) rapid iteration (10 minutes failure→fix) requires reading transcripts, (5) 21 evaluations appropriate for understanding HOW before measuring HOW OFTEN. Frame as using tool as designed, not compromising due to resource constraints.

**Generalization:** When your method seems unconventional, explain the method-question fit explicitly. Different questions require different approaches: discovery requires depth (mechanisms), validation requires breadth (prevalence). Don't apologize for small N when the goal is understanding mechanisms. Show you understand what your method can and cannot do.

**Application scope:** All empirical work; especially relevant for qualitative studies, small-N research, case studies, exploratory work, or any approach that violates conventional statistical expectations.

---

## Patterns Applied from Section 1

| Pattern | Application in Section 2 | Success? |
|---------|--------------------------|----------|
| Pattern 1: AI Rhetorical Tell Elimination | Removed parallel "This is not...this is..." structure | ✓ Yes |
| Pattern 2: Citation Integration | Petri framework cited factually, not praised | ✓ Yes |
| Pattern 4: Empirical Finding as Attractor | Led with findings, not methodology | ✓ Yes |

---

## Patterns NOT Generalized (Section-Specific)

- Judge dimension naming convention (coherence effect, protocol quality, etc.) — specific to Petri framework, not generalizable metric design
- Seven-source testing protocol — specific to study design, not generalizable structure
- Spoiler categorization (meta-awareness vs. topic mismatch) — specific to this empirical paradigm

---

## Constraint Compliance Notes

| Constraint | Status | Notes |
|------------|--------|-------|
| Falsifiability and exclusion | ✓ Applied | Every claim tied to specific eval ID; spoiled evals documented |
| Distinguish evidence quality | ✓ Applied | Claude vs GPT-4o evidence quality explicitly separated |
| No unjustified global frameworks | ✓ Applied | No premature theorizing; findings presented first |
| Avoid optimization for rhetorical effects | ✓ Applied | Style revisions removed dramatic tone, parallel structures |

---

**Document Status:** Complete  
**Forward Use:** Apply Patterns 6-12 to remaining sections; patterns cumulate with Section 1
