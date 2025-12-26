# Pattern Summary: Section 4

**Document Type:** Type 4 (Pattern Summary)  
**Section:** 4 - The Epistemic Constitution  
**Generated:** December 25, 2025  
**Source:** Modifications MOD-001 through MOD-009

---

## Generalizable Patterns Extracted

### Pattern 18: Explicit Agnosticism Over Vague Gesturing

**Trigger:** Paper makes claims that could apply to different levels (training, inference, deployment) without specifying which.

**Problem:** Vague references to "training dynamics" or "implementation" create ambiguity about what the paper claims. Reader cannot tell if author is confused or deliberately scope-limiting.

**Solution:** State agnosticism explicitly: "This paper does not address X. The contribution is Y." Then, if useful, briefly gesture at how different levels might matter—with appropriate hedging.

**Generalization:** When a paper deliberately leaves something unaddressed, say so directly. Explicit agnosticism is a form of clarity, not evasion. It prevents readers from treating gaps as oversights.

**Application scope:** Any paper with conceptual contributions that could be implemented multiple ways; any paper distinguishing what from how.

---

### Pattern 19: Acknowledge-But-Defer for Out-of-Scope Material

**Trigger:** Material is relevant to the argument but belongs in a later section per the paper's architecture.

**Problem:** Ignoring the material entirely creates apparent gaps. Developing it fully disrupts section function and creates redundancy with later sections.

**Solution:** Brief acknowledgment with explicit deferral. Example: "We note this dimension but do not develop it here... We return to this in the Limitations."

**Generalization:** Papers have architecture. Some material is relevant but belongs elsewhere. Acknowledge its existence, signal where it's addressed, move on. This respects both the material's relevance and the section's scope.

**Application scope:** All sections; especially conceptual sections that touch on material developed later.

**Relation to Pattern 13:** Pattern 13 (Forward References as Economy Device) covers concepts needed for current argument but developed later. Pattern 19 covers material relevant but deliberately deferred—not needed now, but reader shouldn't think it's forgotten.

---

### Pattern 20: Demonstrate Rather Than Explain Contribution

**Trigger:** Section includes passage explaining what the section contributes.

**Problem:** If the section works, the contribution is evident. Explaining it is redundant and suggests the section doesn't stand on its own.

**Solution:** Let the section demonstrate its contribution. If literature positioning is needed, integrate it with another function (e.g., transition to next section) rather than making it standalone.

**Generalization:** Show, don't tell—applied to academic argument. A section that needs a paragraph explaining its contribution probably needs revision, not explanation.

**Application scope:** All sections; especially sections making conceptual contributions.

---

### Pattern 21: Condense by Combining Functions

**Trigger:** Multiple short passages each serve one function; section feels padded.

**Problem:** Literature positioning paragraph + transition paragraph + contribution statement = redundancy when all three are brief.

**Solution:** Combine into single passage that does multiple things. Example: "Most work on X examines Y (literature). Our question is different: Z (contribution). Answering this requires A, which Section N develops (transition)."

**Generalization:** Academic prose often separates functions that can be combined. When passages are short, look for opportunities to merge. Leaner sections are easier to read.

**Application scope:** All sections; especially sections under word-count targets.

---

## Patterns NOT Generalized (Section-Specific)

- The ethics→epistemics extension argument—specific to this paper's Constitutional AI framing
- Three types of norms (evidence, sources, uncertainty)—specific content of this epistemic constitution
- External embedding as complementary dimension—specific to paper architecture

---

## Cumulative Pattern Index

| Pattern # | Name | Source Section |
|-----------|------|----------------|
| 1 | AI Rhetorical Tell Elimination | Section 1 |
| 2 | Citation Integration Without Genuflection | Section 1 |
| 3 | Literature Positioning as Extension | Section 1 |
| 4 | Empirical Finding as Attractor | Section 1 |
| 5 | Roadmap Without Repetition | Section 1 |
| 6 | Concrete Before Abstract | Section 2 |
| 7 | Evidence Quality Honesty | Section 2 |
| 8 | Evaluation Dimensions Made Explicit | Section 2 |
| 9 | Replication as Strengthening Evidence | Section 2 |
| 10 | Iteration as Finding, Not Failure | Section 2 |
| 11 | Eliminate Section Redundancy | Section 2 |
| 12 | Method-Question Fit, Not Apology | Section 2 |
| 13 | Forward References as Economy Device | Section 3 |
| 14 | Section Role Over Pattern Application | Section 3 |
| 15 | Scope Calibration via Prompt Review | Section 3 |
| 16 | Cite Ideas Where They Appear | Section 3 |
| 17 | Hedge Mechanisms, Not Observations | Section 3 |
| 18 | Explicit Agnosticism Over Vague Gesturing | Section 4 |
| 19 | Acknowledge-But-Defer for Out-of-Scope Material | Section 4 |
| 20 | Demonstrate Rather Than Explain Contribution | Section 4 |
| 21 | Condense by Combining Functions | Section 4 |

---

**Document Status:** Complete  
**Forward Use:** Apply Patterns 18-21 to remaining sections; patterns cumulate
