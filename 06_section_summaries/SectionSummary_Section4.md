# Section Summary: Section 4 (The Epistemic Constitution)

**Document Type:** Type 5 (Section Summary)  
**Section:** 4 - The Epistemic Constitution  
**Generated:** December 25, 2025  
**Word Count:** ~950 words (target was ~1,200)

---

## Argument Structure

### Opening (Transition from Section 3)
Section 3 identified a gap: implicit policies, no explicit norms. Policies emerged from training, not design. Question: what would address this directly?

### Constitutional AI Analogy
Bai et al. (2022) introduced training against explicit principles. Key innovation: making norms explicit, therefore inspectable, contestable, revisable. Proposal: extend from ethics to epistemology.

### The Analogy's Limits
Ethical principles govern outputs (what system says/does). Epistemic constitution governs upstream: how system arrives at beliefs. More fundamental, more difficult. Ethical constraints filter outputs; epistemic norms must shape reasoning itself.

### What an Epistemic Constitution Would Contain
Three types of norms:
1. Evidence norms (what counts, how to weight, conflicting evidence)
2. Source norms (when relevant, how to reason about credibility, surfacing)
3. Uncertainty norms (calibration, expression, belief vs. establishment)

Also potentially: inference, transparency, revision norms. Point: make explicit rather than leave implicit.

### Forward Reference to Section 7
Source-attending norms developed there are one component—illustrate broader project.

### Implementation Agnosticism
Paper specifies what norms should govern, not how to implement. Training, system prompts, fine-tuning, architecture—separate question. Agnosticism deliberate: contribution is conceptual.

Different levels may have different roles:
- Training: shapes available patterns, source of problem observed
- Inference-time: can make norms explicit without retraining
- Deployment: embedding in external practices (testing, debate, feedback)

### External Dimension (Acknowledged, Not Developed)
What may make LLM reasoning incomplete: absence of safeguards (evidence, experiments, scrutiny, debate). Humans can partially supply. External embedding is part of complete epistemic constitution—but developed in Limitations, not here. Paper focuses on internal norms.

### The Design Question (Transition to Section 5)
Literature on epistemic responsibility examines responsibility *around* AI systems (Miller & Record 2017; Lloyd 2025; Peters 2024). Our question: norms *within* AI systems. Requires distinguishing approaches to constitution design.

Two visions: Platonic (formal correctness, source independence) vs. Liberal (procedural norms, collective inquiry, principled source-attending). Section 5 develops this distinction.

---

## Key Concepts Developed

| Concept | Treatment in Section 4 |
|---------|------------------------|
| Epistemic constitution | Formally introduced; defined as meta-norms for belief formation |
| Ethics→epistemics extension | Analogy to Constitutional AI; precise in some respects, inexact in others |
| Three norm types | Evidence, sources, uncertainty (sketch, not exhaustive) |
| Implementation agnosticism | Explicitly stated as paper's scope |
| External embedding | Acknowledged as complementary dimension; deferred to Limitations |

---

## Forward References Made

| To Section | Reference Content |
|------------|-------------------|
| Section 5 | "Section 5 develops this distinction" (Platonic vs Liberal) |
| Section 7 | "The source-attending norms we develop in Section 7" |
| Limitations | "We return to this in the Limitations" (external embedding) |

---

## Backward Connections

| From Section | Connection |
|--------------|------------|
| Section 3 | Opens by referencing Section 3's diagnosis (gap between implicit policies and explicit norms) |
| Section 2 | Implicit: "the problem we observed" refers to empirical findings without re-presenting them |

---

## Citations Used

| Citation | Function |
|----------|----------|
| Bai et al. 2022 | Primary anchor—Constitutional AI as model for extension |
| Miller & Record 2017; Lloyd 2025; Peters 2024 | Contrast—epistemic responsibility *around* AI vs. norms *within* AI |

---

## Unresolved Elements (Deliberate)

- Platonic vs Liberal distinction (Section 5)
- Why Liberal is more adequate (Section 6)
- Source-attending norms content (Section 7)
- External embedding development (Limitations)
- Implementation mechanisms (out of scope)

---

## Section's Contribution to Paper

Section 4 introduces the paper's central conceptual contribution: the epistemic constitution. It:
1. Names the solution to the problem diagnosed in Section 3
2. Grounds it in Constitutional AI (strategic positioning)
3. Specifies what such a constitution would contain (types of norms)
4. Scopes the paper's contribution (internal norms, implementation-agnostic)
5. Sets up the design choice developed in Section 5

---

**Document Status:** Complete  
**Purpose:** Ensure continuity when writing Sections 5-9
