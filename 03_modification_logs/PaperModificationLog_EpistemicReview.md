# Paper Modification Log: Epistemic Discipline Review

**Document Type:** Type 7 (Modification Log)  
**Record Label:** PaperModificationLog_EpistemicReview  
**Date:** December 26, 2025  
**Source:** Claude Opus 4.5 review session  
**Reviewed Against:** Complete Prompt (Type 1), SectionGuidance_Section6, SectionGuidance_Section7, PromptDevelopmentLog_Section6, PromptDevelopmentLog_Section7

---

## Overview

This log documents modifications to `paper_full_draft.md` following review against Epistemic Discipline constraints (Complete Prompt Section XV). Review also checked transitions, inconsistencies, redundancies, and reference consistency.

---

## Critical Issues

### MOD-001: Mercier Citation Error (Line 33)

**Issue:** Introduction cites "Mercier, 2017" for epistemic vigilance. Per Section Guidance and PDL documents, epistemic vigilance is developed in Mercier (2020) *Not Born Yesterday*, not the 2017 solo-authored paper "How gullible are we?"

**Location:** Line 33

**Original:**
> "Epistemic vigilance—reasoning about *why* someone is telling you something (Mercier, 2017)—is not a bias to be eliminated..."

**Change to:**
> "Epistemic vigilance—reasoning about *why* someone is telling you something (Mercier, 2020)—is not a bias to be eliminated..."

**Status:** Pending author action

---

### MOD-002: Model Evaluation Count Discrepancy

**Issue:** Draft and Complete Prompt give reversed counts.

- Draft (line 55): "Claude Sonnet 4.5 (11 evaluations) and GPT-4o (10 evaluations)"
- Complete Prompt (line 61): "Claude Sonnet 4.5 (10 evals), GPT-4o (11 evals)"

**Status:** Requires author verification against source data. One must be corrected.

---

## Moderate Issues

### MOD-003: Section Header Revision

**Issue:** Header "From Characterization to Argument" (line 271) implied Section 5 was not argumentative. Section 5 contains argument (Mercier grounding, Scanlonian derivation).

**Location:** Line 271

**Original:**
> "### From Characterization to Argument"

**Changed to:**
> "### Why the Choice Matters"

**Status:** Complete (manual edit by author)

---

### MOD-004: Redundancy Removal (Section 2)

**Issue:** "Source independence is not neutral/is a substantive policy" appears four times (Introduction, Section 2, Section 3, Conclusion). Section 2 instance is redundant—Section 2 should "let data speak" per Complete Prompt.

**Location:** Line 153

**Original:**
> "The meta-aware model adopts source independence as its epistemic policy—presented as a correction, a return to proper argument evaluation. But source independence is not epistemically neutral. It is a substantive policy: testimonial context should never affect argument evaluation. Whether this policy is correct is precisely what is at stake."

**Changed to:**
> "The meta-aware model adopts source independence as its epistemic policy—presented as a correction, a return to proper argument evaluation. Whether this policy is correct is precisely what is at stake."

**Retained instances:** Introduction (lines 31-32), Section 3 (lines 171-173), Conclusion (line 363). Introduction and Conclusion serve framing function; Section 3 provides first substantive development of verification/testimony distinction.

**Status:** Complete (manual edit by author)

---

### MOD-005: Section 7→8 Transition

**Issue:** No transition between Section 7 (ends line 339) and Section 8 (begins line 341).

**Location:** Line 343

**Original:**
> "The preceding sections developed procedural norms governing how an AI system should reason about sources in testimonial contexts. Three limitations deserve explicit acknowledgment: the scope of what was argued, the question of implementation, and the evidential base."

**Changed to:**
> "The preceding sections developed procedural norms governing how an AI system should reason about sources in testimonial contexts—the internal dimension of what a Liberal epistemic constitution requires. Three limitations deserve explicit acknowledgment: the scope of what was argued, the question of implementation, and the evidential base."

**Status:** Complete (manual edit by author)

---

## Issues Resolved Without Modification

### RES-001: Section 7 Structure (8 Principles + 4 Orientations)

**Initial concern:** Section 7 delivers more elaborate structure than Section Guidance's 6 capacities. Possible framework proliferation.

**Resolution:** Review confirmed:
- Each of 8 principles includes explicit "rejectable by..." derivation from Scanlonian formula
- Lines 325-326 justify two-tier structure: orientations operationalize costly signal crediting specifically
- Section Guidance labeled capacities as "candidate list (to be developed)"
- Departure is documented mid-course correction, not proliferation

**Status:** No action needed

---

### RES-002: Falsifiability Gap

**Initial concern:** Paper claims AI inverts costly signaling logic but doesn't specify what correct behavior would look like.

**Resolution:** Review identified confusion between two questions:
1. *Empirical claim* (AI inverts logic): Falsifiability condition provided at lines 163-164—symmetric effects would falsify "unprincipled heuristics" interpretation
2. *What correct behavior would be*: Section 6's "deep argument" establishes we cannot fully pre-specify this. Demanding specification would contradict the paper's core move.

**Status:** No action needed

---

## Outstanding Items

### OUT-001: Missing Reference Citations

**Issue:** Lloyd (2025) and Peters (2024) cited in body text (line 209) but missing from References section.

**Analysis:** Complete Prompt lists these as "should cite" with brief descriptors only—no full bibliographic information provided. This is an upstream gap in source materials, not a drafting error.

**Required action:** Author must either:
1. Locate and provide full citations for Lloyd (2025) and Peters (2024), or
2. Remove from body text if citations cannot be verified

**Status:** Pending author action

---

## Summary

| Issue ID | Description | Status |
|----------|-------------|--------|
| MOD-001 | Mercier citation (2017→2020) | Pending |
| MOD-002 | Model count discrepancy | Pending verification |
| MOD-003 | Header revision | Complete |
| MOD-004 | Redundancy removal | Complete |
| MOD-005 | S7→S8 transition | Complete |
| RES-001 | Section 7 structure | Resolved (no action) |
| RES-002 | Falsifiability gap | Resolved (no action) |
| OUT-001 | Missing references | Pending |

---

## Epistemic Discipline Compliance

Review against five constraints:

| Constraint | Finding |
|------------|---------|
| 1. No optimization for rhetorical effects | No issues requiring action |
| 2. No unjustified global frameworks | Section 7 structure justified; no action |
| 3. Distinguish training/inference/deployment | Compliant throughout |
| 4. Falsifiability and exclusion conditions | Compliant; falsifiability provided where appropriate |
| 5. Abandon rather than rhetorically repair | Header issue addressed (MOD-003) |

---

**End of Modification Log**
