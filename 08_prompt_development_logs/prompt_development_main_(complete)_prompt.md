# Prompt Development Log: Complete Prompt for Epistemic Constitutionalism Paper

**Document Type:** Type 8a (Complete Prompt Development Log)  
**Record Label:** PromptDevelopmentLog  
**Date:** December 18, 2025  
**Source Conversation:** Claude Opus 4.5 session  
**Output Artifact:** `complete_prompt_epistemic_constitutionalism.md` (Type 1)

---

## Overview

This log documents the structured decisions that shaped the Complete Prompt (Type 1) for the paper "Epistemic Constitutionalism for AI." It traces how exploratory materials (Type 2 epistemic traces) and empirical documentation (lab book) were synthesized into actionable writing guidance.

**Input Materials:**
- Document 016: Epistemic Trace on Scanlonian liberal epistemic principle (ChatGPT, Dec 18)
- Document 001: Epistemic Trace on Ought-Is Collapse (earlier, structure reference only)
- Lab Book v3 → v4: Study 4 empirical findings (corrected during session)
- ChatGPT transcript: Full philosophical conversation on Mercier/Scanlon
- Document 017: Literature research on epistemic responsibility (ChatGPT)
- JPEP Appendix: Methodology template for transparent AI-assisted writing
- Epistemically Constrained Generation prompt: Discipline constraints for AI writing

**Total decisions documented:** 14 (PDL-001 through PDL-014)

---

## Decision Log

### PDL-001: Paper Framing Decision

**Issue:** User had developed epistemic constitution concept across multiple conversations. How to frame the paper's central contribution?

**Options considered:**
1. Lead with empirical finding, theory as interpretation
2. Lead with theoretical concept, empirical as support
3. Lead with literature gap, contribution as response

**Decision:** Option 1 modified—empirical finding as "attractor" (proof of work), but epistemic constitution concept as headline contribution.

**Rationale:** User stated: "in the age in which language is cheap... I rely on the empirical stuff as an attractor." But the novelty is the concept. Structure: empirical hook → conceptual contribution → theoretical grounding.

**Affects:** Section order, Introduction framing, overall argument architecture.

---

### PDL-002: Literature Placement Strategy

**Issue:** User self-describes as "isolated researcher connecting dots in peculiar walks." Risk of solipsistic paper. How much literature engagement?

**Options considered:**
1. Comprehensive literature review
2. Systematic gap analysis
3. Thin strategic placement (one paragraph)

**Decision:** Option 3—single orienting paragraph, strategic citations only.

**Rationale:** User preference for distinctiveness over comprehensiveness. Empirical work carries credibility. Constitutional AI (Bai et al. 2022) as primary anchor exploits recognizable concept.

**Key citations selected:**
- Bai et al. (2022) – Constitutional AI
- Mercier & Sperber (2011/2017) – Argumentative theory
- Scanlon (1998) – Contractualism
- Miller & Record (2017), Lloyd (2025), Peters (2024) – epistemic responsibility cluster

**Affects:** Section 4 literature paragraph, reference guidance.

---

### PDL-003: Argument Architecture

**Issue:** Multiple theoretical threads (Mercier, Scanlon, epistemic vigilance, source attribution). How to structure the argument flow?

**Decision:** Six-step architecture:

1. Problem → 2. Evidence → 3. Solution Concept → 4. Design Choice → 5. Resolution → 6. Contribution

**Mapping:**
- Problem: AI lacks explicit epistemic norms
- Evidence: Source attribution findings (empirical anchor)
- Solution: Epistemic constitution concept
- Design choice: Platonic vs Liberal
- Resolution: Why liberal (epistemic vigilance, costly signaling)
- Contribution: Source-attending norms sketch

**Rationale:** User's framing: "Problem → Fix (epistemic constitution) → How to design (platonic vs liberal) → Key difference (source attribution)." This is superior to finding-first because it foregrounds the novel concept.

**Affects:** All section specifications.

---

### PDL-004: Empirical Data Verification

**Issue:** Lab book v3 claimed 25 evaluations, but registry tables showed 21. Discrepancy needed resolution before prompt finalization.

**Action:** User ran separate verification session with AI agent.

**Resolution:** Lab book v4 confirmed:
- 21 total evaluations (not 25)
- 14 clean, 7 spoiled, 0 uncertain
- 4 data quality issues identified and resolved

**Prompt updates required:**
- Section III: Corrected counts
- All effect size references verified
- Data quality notes added for transparency

**Affects:** Section III (Empirical Anchor), Section 2 specifications.

---

### PDL-005: Petri Framework Positioning

**Issue:** How to describe the empirical methodology? User used Anthropic's Petri framework with custom instrumentation.

**Decision:** Frame as "applied Petri research with custom instrumentation"—systematic evaluation using established infrastructure, not ad hoc prompting.

**Rationale:** 
- Petri released October 2025, recognized tool
- Custom seeds and judge dimensions = methodological contribution
- Adds legitimacy to empirical findings
- Connection to Anthropic (Petri + Constitutional AI) creates thematic coherence

**Affects:** Section 2 methodology description, Appendix A planning.

---

### PDL-006: Source Material Preservation

**Issue:** ChatGPT conversation contained well-developed formulations (Scanlonian principle, Platonic/Liberal contrast, stable procedures menu). Risk of re-deriving during writing.

**Decision:** Add Section XI to Complete Prompt preserving source material verbatim.

**Preserved elements:**
- A. Platonic vs Liberal contrast (full articulation)
- B. Scanlonian evolution (3 stages with reasoning)
- C. "Stable procedures" menu (5 constitutional essentials)
- D. Context-dependency argument
- E. Mercier connection explanation
- F. Paper narrative arc

**Rationale:** User judgment: "ChatGPT did an excellent job with Scanlonian formulations... waste of compute to let Claude writer re-derive."

**Affects:** Section XI added to Complete Prompt.

---

### PDL-007: Voice Calibration

**Issue:** Maintaining author's distinctive voice across AI-assisted writing. Multiple traces available showing spoken and written registers.

**Decision:** Add Section XII to Complete Prompt with explicit voice guidance.

**Voice characteristics extracted:**
- Direct assertion over hedged qualification
- Philosophical vocabulary without performative signaling
- Practical orientation
- Comfortable acknowledging limits

**Anti-patterns identified:**
- Generic academic throat-clearing
- Excessive signposting
- AI writing tells (redundancy, over-structure)

**Sample register preserved:** User's own formulations from voice notes as calibration targets.

**Affects:** Section XII added to Complete Prompt, tone targets by section.

---

### PDL-008: Section Specifications

**Issue:** Nine sections needed individual specifications (word counts, must-accomplish lists, tone).

**Decisions:**

| Section | Words | Key Decision |
|---------|-------|--------------|
| 1. Intro | ~800 | Hook with finding, state contribution clearly |
| 2. Finding | ~1,500 | Let data speak, include summary table |
| 3. Problem | ~1,000 | Diagnose implicit policies, connect to suppression |
| 4. Constitution | ~1,200 | Introduce concept, Constitutional AI analogy |
| 5. Platonic vs Liberal | ~1,500 | Design choice framing, include Scanlonian principle |
| 6. Why Liberal | ~1,500 | Return to finding, introduce epistemic vigilance |
| 7. Norms | ~1,000 | Sketch agenda, not complete theory |
| 8. Limitations | ~500 | Honest acknowledgment, not self-flagellation |
| 9. Conclusion | ~500 | Forward-looking, understated |

**Total target:** 8,000-10,000 words (excluding appendices)

**Affects:** Section VI of Complete Prompt.

---

### PDL-009: Model Selection for Writing

**Issue:** Opus vs Sonnet for different sections. Trade-off: quality vs iteration time.

**Decision:** Hybrid approach recommended:
- Opus: Sections 1, 3, 4, 5, 6, 7 (philosophical heavy lifting)
- Sonnet: Sections 2, 8 (empirical description, standard acknowledgments)
- Section 9: Flexible based on flow

**Rationale:** Philosophical sections require holding Mercier/Scanlon connection, distinctive voice. Sonnet tends toward safe conventional phrasing requiring more iterations.

**Estimated intensity:**
- All Opus: ~15-20 hours
- All Sonnet: ~25-35 hours
- Hybrid: ~12-18 hours

**Affects:** Writing process notes (Section X).

---

### PDL-010: Documentation Infrastructure

**Issue:** Separating paper writing transparency (JPEP system) from empirical data documentation (standard research practices).

**Decision:** Two separate documentation tracks:

1. **Paper writing:** JPEP methodology (epistemic traces, modification logs, etc.) → Supplementary materials
2. **Empirical data:** Standard Petri practices (seeds, transcripts, scores) → GitHub/OSF repository

**Action:** Separate prompt created for Sonnet agent to guide empirical data documentation. User to complete before writing begins so paper can reference repository.

**Affects:** Appendix planning, data documentation agent prompt.

---

### PDL-011: Epistemic Vigilance Integration

**Issue:** Mercier's epistemic vigilance framework identified as key missing element in original epistemic constitution development. How to incorporate?

**Decision:** Epistemic vigilance as the bridge between liberal constitution and source-attending norms.

**Key concepts to develop:**
- Costly signaling principle (against-interest testimony more credible)
- Symmetric application requirement (the finding shows asymmetry)
- Motive reasoning (why someone is telling you something)

**Integration point:** Section 6 (Why Liberal) introduces epistemic vigilance; Section 7 (Norms) operationalizes it.

**Rationale:** User's insight: "Source skepticism shouldn't work as the AI does. It should work in the opposite way. Modelling this should need some incorporation of social dynamics, motives, and why being contrarian tends to be a move against one's interests."

**Affects:** Section V (Theoretical Commitments), Section 6-7 specifications.

---

### PDL-012: The "Oddity" Framing

**Issue:** How to characterize what the empirical finding reveals?

**Decision:** Frame as epistemic oddity—the AI treats source-sensitivity as something to *hide*, not something to *do well*.

**Key articulation:**
- When meta-aware, AI defaults to source independence (Platonic fix)
- But source independence is itself a substantive epistemic policy
- The question isn't whether source matters, but *how* it should matter

**Rationale:** This framing makes the finding philosophically significant, not just a bias to be corrected.

**Affects:** Section III (Empirical Anchor), Section 3 and 6 specifications.

---

### PDL-013: Internal/External Scope Decision

**Issue:** User identified connection to Floridi et al. paper and LinkedIn post arguing LLM reasoning needs "external safeguards" (experiments, debates, evidence, scrutiny). How does this relate to the paper's focus on internal epistemic norms?

**Options considered:**
1. Expand paper to cover both internal norms and external embedding
2. Ignore the connection
3. Acknowledge both dimensions, focus on internal, show compatibility

**Decision:** Option 3—acknowledge the distinction, maintain internal focus (finding-connected), frame external as compatible extension.

**Rationale:** 
- The empirical finding speaks to *internal* conduct (how AI handles sources)
- Expanding to external embedding would dilute the tight argument
- But the Mercier/liberal framework actually *implies* both dimensions
- Honest scoping: internal necessary but not sufficient
- External embedding is complementary future work, not competing framework

**Key insight preserved:** The "safeguards" Floridi et al. describe ARE the collective epistemic practices Mercier says make reasoning work. Internal norms + external embedding are two implications of the same insight: reason is social.

**Treatment in paper:**
- Introduction: Brief acknowledgment of both dimensions, internal focus stated
- Sections 2-7: Stay internal (finding-connected)
- Limitations: Internal norms necessary but not sufficient
- Conclusion: External embedding as compatible extension, not gap

**Affects:** Sections XIII-XIV added to Complete Prompt. Limitation and Conclusion section specifications.

---

### PDL-014: Epistemic Discipline Constraints

**Issue:** User shared "Epistemically Constrained Generation" prompt with constraints against rhetorical polish, unjustified frameworks, and authority effects. How to integrate without causing writer paralysis or misapplication?

**Source:** External prompt for epistemically disciplined AI writing.

**Constraints evaluated:**

| # | Constraint | Decision |
|---|------------|----------|
| 1 | No optimization for rhetorical polish/symmetry/memorability | Include with scope guidance |
| 2 | No unjustified global frameworks | Include with scope guidance |
| 3 | Distinguish training/inference/deployment | Include with scope guidance |
| 4 | Falsifiability/exclusion conditions for claims | Include with scope guidance |
| 5 | Abandon rather than rhetorically repair | Include with scope guidance |

**Key insight:** Initial hesitation about constraints (especially #3) revealed the risk of misapplication. The hesitation itself became a signal: constraints need proper/misapplication guidance to be usable.

**Design principle adopted:** Each constraint includes:
- The constraint itself
- Proper application to this paper
- Misapplication to avoid
- The distinction (what the constraint targets vs. what it doesn't)

**Examples of proper vs. misapplication:**

*Constraint 1:*
- Proper: Don't sacrifice accuracy for a catchy phrase
- Misapplication: "I can't write clear prose because that would be 'polish'"
- Distinction: Clarity serves understanding; polish serves impression

*Constraint 2:*
- Proper: Platonic/Liberal distinction must be justified by argument
- Misapplication: "I can't use any framework"
- Distinction: Frameworks *imposed* without justification vs. frameworks that *emerge from* argument

*Constraint 3:*
- Proper: Finding describes inference-time behavior; norms are agnostic about implementation
- Misapplication: "I must specify implementation mechanism for every claim"
- Distinction: What was observed and what is proposed vs. how to implement

**Overarching principle preserved:** "The goal is not to appear rigorous, but to expose where rigor is absent."

**Affects:** Section XV added to Complete Prompt. Applies to all sections during writing and editing.

---

## Output Artifact

**Complete Prompt (Type 1):** `complete_prompt_epistemic_constitutionalism.md`

**Final structure:**
- I. Paper Identity
- II. Core Argument Architecture
- III. Empirical Anchor (corrected data)
- IV. Literature Placement
- V. Theoretical Commitments
- VI. Section Specifications (9 sections)
- VII. Tone and Style
- VIII. Reference Guidance
- IX. Appendices (Planned)
- X. Writing Process Notes
- XI. Source Material for Unpacking
- XII. Voice Calibration
- XIII. Scope: Internal and External Dimensions
- XIV. Source Material: External Embedding
- XV. Epistemic Discipline

**Status:** Complete, ready for writing phase.

---

## Related Documents

**Inputs:**
- Raw conversation transcript (this session)
- Document 016: Epistemic Trace (Scanlonian principle)
- Document 017: Literature research trace
- ChatGPT transcript: Mercier/Scanlon philosophical conversation
- Lab Book v4: Verified empirical data

**Outputs:**
- Complete Prompt (Type 1)
- Empirical Data Documentation Agent Prompt (for separate session)

**Next phase:** Section writing with feed-forward artifacts (Section Summaries, Modification Logs, Section Guidance).

---

**End of Prompt Development Log**
