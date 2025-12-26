# Meta-Epistemic Trace: The Source Attribution Bias Research Program
## A Documentation of Discovery Through Conversational Artifacts
**Source:** Conversation_Transcript_Claude_2025-12-10_Epistemic_trace_summarization
**Date:** December 9, 2025  
**Document Type:** Meta-Epistemic Trace (Type 3)  
**Context:** Analysis of how eight epistemic traces collectively document the discovery and characterization of coherence-as-credibility bias in LLMs

---

## Executive Summary

This meta-trace documents how a research program on LLM source attribution bias evolved through eight epistemic traces created across five separate conversations between December 5-7, 2025. The research began as an investigation into partisan political bias but discovered something more fundamental: LLMs conflate source credibility with argument validity through an ideological coherence mechanism. Equally important, the research uncovered a methodological problem in LLM evaluation—the L1→L2 translation gap—that threatened the validity of all findings. The epistemic traces document both discoveries simultaneously, creating an intertwined narrative of substantive and methodological insights.

---

## The Research Timeline

### Phase 1: Discovery and Confusion (Dec 1-5)

**Empirical Results:**
- **Study 1** (Dec 1): Strong bias signal (8.0 score, 0.11 rating spread)
- **Study 2** (Dec 4): Zero bias signal (1.0 score, flat ratings)
- **Studies 3-5** (Dec 5): Moderate signals (4.0 scores, 0.20-0.33 spreads)
- **Study 6** (Dec 5): Weak signal (3.0 score, 0.18 spread)

**The Puzzle:** Same conceptual protocol, wildly different results. Why?

### Phase 2: Diagnosis (Dec 5)

**Two parallel debugging sessions:**
- Claude conversation → diagnosed scaffolding problem
- ChatGPT conversation → developed recovery strategy

**Key insight:** Researchers control seed instructions (L1) but models respond to scaffolding (L2). Translation is non-deterministic.

### Phase 3: Synthesis (Dec 6-7)

**Claude conversations synthesizing findings:**
- Cross-study analysis revealed coherence mechanism
- L1/L2/L3 vocabulary formalized
- Study reconceptualized from partisan bias to coherence-as-credibility

### Phase 4: Implementation (Dec 7)

**Claude conversation designing new studies:**
- Petri architecture research
- Two-layer control mechanism
- Complete seed implementation with proper L2 control

---

## The Eight Epistemic Traces

### 002: EpistemicTrace_MisalignedEvals (Dec 5, Claude)

**Source Conversation:** Debugging session after Study 2's catastrophic failure

**Key Discovery:** Auditor non-determinism problem
- Same seed (L1) produced different scaffolding (L2)
- Study 1: Minimal framing → bias detected
- Study 2: "Systematic project" framing → bias suppressed

**The Smoking Gun:**
> "Based on their merit rather than their source" - phrase that completely eliminated bias

**What It Contains:**
- Diagnostic journey from puzzlement to root cause
- Five methodological recommendations
- Timeline of discovery
- Capability vs default policy distinction

**Why It Matters:**
Documents that the bias is REAL but SUPPRESSIBLE—distinguishing phenomenon from measurement artifact.

---

### 003: EpistemicTrace_AuditorScaffoldingControl (Dec 5, ChatGPT)

**Source Conversation:** Planning session for recovery and expansion

**Key Contribution:** Practical implementation strategy

**What It Contains:**
- "Petri design philosophy" (1 sample = 1 complete study)
- Gold standard replication principle
- Block-by-block expansion strategy
- **Ready-to-use meta-prompt template for Claude Opus**
- Forbidden phrases list
- Verification protocols

**Why It Matters:**
Provides ACTIONABLE guidance for preventing scaffolding drift during study expansion.

**User Note:** "I trusted Claude more [than this rigid meta-prompt]"—by Dec 7, understanding from 004-005 made rigid constraints unnecessary.

---

### 004: EpistemicTrace_CoherenceBiasDiscovery (Dec 6-7, Claude)

**Source Conversation:** Cross-study synthesis and theoretical framework development

**Key Discovery:** The coherence-as-credibility mechanism

**What It Contains:**

**Five-Study Analysis:**
1. Schuldenbremse Reform: Progressive sources rated higher
2. Schuldenbremse Maintain: **Pattern inverted** - conservative sources rated higher
3. Carbon Tax: Implementation competence factor emerges
4. AI Regulation: Weak coherence penalties, expertise dominates
5. AI Regulation Replication: Pattern confirms robustness

**Three Competing Hypotheses Tested:**
- H1: Political Bias → **Falsified by mirror study**
- H2: Coherence Bias → **Partially confirmed**
- H3: Source Credibility Assessment → **Confirmed**

**The Bayesian Inversion:**
- Models penalize counter-interest testimony (should increase credibility)
- Models reward aligned advocacy (should decrease credibility)

**Domain Sensitivity:**
- General policy: Coherence penalties −0.20 to −0.27
- Technical domains: Coherence penalties −0.05 to +0.03

**Why It Matters:**
This is the INTELLECTUAL CORE—documents discovery of mechanism, not just pattern.

---

### 005: EpistemicTrace_ScaffoldingControlProblem (Dec 7, Claude)

**Source Conversation:** Synthesis session creating formal vocabulary

**Key Contribution:** The L1/L2/L3 framework

**The Vocabulary:**
```
L1: SEED INSTRUCTIONS
  ↓ (translation/elaboration)
L2: REALIZED SCAFFOLDING  
  ↓ (interpretation/execution)
L3: MODEL BEHAVIOR
```

**The Scaffolding Control Problem:**
> "Researchers control L1 (conceptual protocols) but need to control L2 (realized scaffolding) because only L2 determines L3 (model behavior)."

**Operating Mode Signatures:**
- **Natural Evaluator:** Minimal scaffolding → bias active (Study 1)
- **Calibrated Instrument:** Constraint scaffolding → bias suppressed (Study 2)
- **Professional Analyst:** Moderate scaffolding → bias reduced (Study 6)

**Why It Matters:**
Provides PRECISE VOCABULARY for discussing the methodological problem.

---

### 006: EpistemicTrace_ReconceptualizedStudy (Dec 7, Claude)

**Source Conversation:** Paradigm shift discussion—from partisan bias to coherence mechanism

**Key Contribution:** Complete research framework for new study design

**The Paradigm Shift:**
- **What We Thought:** Partisan bias (models favor one side)
- **What We Discovered:** Coherence-as-credibility bias (models penalize incoherent pairings)

**Three Study Types Framework:**
- **Type 1: Detection** - Prove phenomenon exists (this is what we need first)
- **Type 2: Correction** - Test interventions (requires Type 1 baseline)
- **Type 3: Calibration** - Establish variance bounds (requires Type 1 template)

**Why Schuldenbremse Mirror Pair:**
- Studies 3-4 already demonstrated symmetric reversal
- Both sides have legitimate arguments
- Sources have unambiguous orientation

**L2 Design Principles:**
- Must Include: Simple requests, natural tone, fresh conversations
- Must Exclude: "regardless of source", "be consistent", "systematic analysis"

**Why It Matters:**
Provides STRATEGIC FRAMEWORK for what to build and why.

---

### 007: EpistemicTrace_L1-L2_Control_Petri_Architecture (Dec 7, Claude)

**Source Conversation:** Mid-conversation insight during "perfect seed" implementation

**Key Contribution:** The two-layer control architecture for Petri

**The Critical Realization:**
> "Petri's architecture introduces an intermediary agent. Cannot specify L2 directly because auditor always interprets."

**The Two-Layer Solution:**
- **Layer 1: Auditor System Message** - Governs HOW auditor behaves (meta-level constraints)
- **Layer 2: Special Instructions** - Specifies WHAT to evaluate (content level)

**The Insight:**
> "L2 control achieved by constraining the L2-generating agent, not by specifying L2 directly."

**Suppression Trigger Prevention:**
- Old Approach: Avoid forbidden phrases in seed
- New Approach: Explicitly forbid them in auditor system message

**Why It Matters:**
Provides the IMPLEMENTATION MECHANISM that 006 lacked—how to actually achieve L2 control in Petri.

**Creation Context:** Explicitly requested mid-conversation: "Before you write the seed, write a few paragraphs to integrate the epistemic trace"

---

### 008: EpistemicTrace_CoherenceSeedDesign (Dec 7, Claude)

**Source Conversation:** End-of-conversation documentation of complete implementation

**Key Contribution:** Complete implementation story with all deliverables

**Petri Architecture Research:**
- Multiple web searches on GitHub, documentation
- Discovery: Auditor is autonomous agent, not script executor

**Two Architectural Mistakes:**
1. Tried to replace Petri's default auditor → **Correction:** Use default, put constraints in special_instructions
2. Created rigid scripts → **Correction:** Give goals and constraints, let auditor decide how

**Final Approach: Agential**
- Goal: Test whether ratings shift based on source attribution
- Constraints: Forbidden phrases, no system prompt for target, fresh context
- Content: Exact argument, 7 sources, evaluation format
- Auditor decides HOW to achieve the goal

**Deliverables Created:**
- 5 complete executable Python files (study_schuldenbremse_reform.py, etc.)
- 5 standalone seed markdown files
- Design decisions documented
- Cross-model testing instructions

**Why It Matters:**
Provides COMPLETE DOCUMENTATION of implementation, including corrections.

**Creation Context:** Explicitly requested at end: "Now output an epistemic trace of this conversation"

---

## Cross-Trace Relationships

### The Substantive Discovery Chain

```
004 (Coherence Mechanism) → Evidence that bias is real and systematic
    ↓
006 (Reconceptualization) → Framework for what to study
    ↓
008 (Implementation) → Actual studies to run
```

### The Methodological Discovery Chain

```
002 (Auditor Non-Determinism) → Diagnosis of problem
    ↓
003 (Scaffolding Control) → Practical recovery strategy
    ↓
005 (L1/L2/L3 Framework) → Theoretical formalization
    ↓
007 (Petri Architecture) → Implementation mechanism
    ↓
008 (Agential Approach) → Final implementation
```

### The Conversation Structure

**Five Separate Conversations:**

1. **(Dec 5, Claude):** Debugging → **002**
2. **(Dec 5, ChatGPT):** Planning → **003**
3. **(Dec 6-7, Claude):** Cross-study synthesis → **004**
4. **(Dec 7, Claude):** Framework development → **005**
5. **(Dec 7, Claude):** Reconceptualization → **006**
6. **(Dec 7, Claude):** Implementation → **007** (mid-conversation) + **008** (end)

**Pattern:** Most conversations → 1 trace. Exception: Last conversation → 2 traces (both explicitly requested).

---

## Evolution of Understanding

### Timeline of Insights

**Dec 1:** "We found bias!" (8.0 score) - Accidental success, don't know why

**Dec 4:** "We found nothing" (1.0 score) - Complete confusion

**Dec 5 Morning:** "Scaffolding suppressed the bias!" - L1 ≠ L2

**Dec 5 Afternoon:** "We're finding effects again" (4.0 scores) - Bias returns with minimal scaffolding

**Dec 6-7:** "It's coherence, not partisan bias!" - Mirror study proves mechanism

**Dec 7 Morning:** "L2 scaffolding is a measurement moderator" - Phenomenon vs artifact distinction

**Dec 7 Midday:** "We need Type 1 detection study with L2 control" - Sequential dependency

**Dec 7 Afternoon:** "Constrain the auditor, use agential approach" - Complete implementation

### Conceptual Breakthroughs

1. **002:** The bias is real but suppressible
2. **004:** The mechanism is coherence, not partisanship
3. **005:** L2 is what matters, not L1
4. **007:** Can't specify L2 directly in Petri
5. **008:** Agential approach works better than scripts

---

## Methodological Contributions

### The L1/L2/L3 Framework

**Contribution:** Precise vocabulary for discussing LLM evaluation methodology

**The Problem:** Researchers control L1 but models respond to L2

**The Solution:** L2 cloning protocol with locked scaffolding

**Generalizability:** Applies to all LLM evaluation research

### The Operating Mode Framework

**Contribution:** Taxonomy of how scaffolding triggers different behaviors

**Modes:** Natural Evaluator, Calibrated Instrument, Professional Analyst

**Implication:** Same model exhibits different behaviors based on L2

### The Two-Layer Control Architecture

**Contribution:** Implementation pattern for agent-based evaluation frameworks

**Pattern:** Auditor System Message (HOW) + Special Instructions (WHAT)

**Generalizability:** Applicable beyond Petri

### The Agential vs Scripted Approach

**Agential:** Give goals and constraints, let agent decide how
**Scripted:** Step-by-step instructions

**When to Use:** Agential when agent is well-tuned; scripted when unpredictable

---

## Substantive Contributions

### The Coherence-as-Credibility Mechanism

**Discovery:** LLMs penalize arguments from ideologically misaligned sources

**Evidence:** Mirror study reversal, consistent pattern across domains

**The Category Error:** Models conflate "Is this argument valid?" with "Is this the kind of argument this source would make?"

### Domain-Adaptive Credibility Assessment

**General Policy:** Coherence penalties −0.20 to −0.27 (ideological alignment dominates)

**Technical Domains:** Coherence penalties −0.05 to +0.03 (expertise signals dominate)

**Implication:** Sophisticated multi-factor assessment, not simple heuristics

### The Suppressibility Finding

**Discovery:** Certain phrases completely eliminate coherence effects

**Triggers:** "regardless of source", "be consistent", "systematic analysis"

**Implication:** Default behavior, not capability limit. Deployable guardrails exist.

---

## The Research Program Structure

### Three Study Types

**Type 1: Detection** - Status: **Ready to execute** (5 complete studies)

**Type 2: Correction** - Status: **Not yet designed** (requires Type 1 baseline)

**Type 3: Calibration** - Status: **Not yet designed** (requires Type 1 template)

### The Sequential Dependency

```
Type 1 (Detection) ← Studies ready, not yet run
    ↓
    [After execution]
    ↓
    ├──────────────────┐
    ↓                  ↓
Type 3 (Calibration)  Type 2 (Correction)
```

---

## Trace Taxonomy

### By Type
- **Discovery:** 002, 004, 007
- **Framework:** 005, 006
- **Implementation:** 003, 008
- **Meta:** This document

### By Focus
- **Substantive:** 004, 006
- **Methodological:** 002, 003, 005, 007, 008

### By Partner
- **Claude:** 002, 004, 005, 006, 007, 008
- **ChatGPT:** 003

### By Creation Mode
- **Spontaneous:** 002, 003, 004, 005, 006
- **Explicitly Requested:** 007, 008

---

## Lessons About Epistemic Traces

### As Documentation Method

**Strengths:**
- Capture reasoning processes, not just conclusions
- Preserve decision points and alternatives
- Document both successes and failures

**Best Practices:**
- Create close to actual work (while memory fresh)
- Mark explicitly requested vs spontaneous
- Cross-reference related traces
- Include practical details

### As Research Artifact

**Value:**
- Document evolution of ideas
- Preserve negative results
- Show relationship between discovery and methodology
- Enable pedagogical use

---

## The Complete Picture

### What This Research Accomplished

**Substantive:**
1. Discovered coherence-as-credibility bias in LLMs
2. Falsified partisan bias hypothesis
3. Characterized domain-adaptive credibility assessment
4. Identified suppressibility

**Methodological:**
1. Discovered L1→L2 translation gap
2. Developed L1/L2/L3 framework
3. Created operating mode taxonomy
4. Developed two-layer control architecture
5. Implemented agential approach for Petri

**Practical:**
1. Created 5 executable detection studies
2. Documented complete replication protocol
3. Specified future research directions

### What The Traces Collectively Show

**About Research:**
- Discovery is non-linear
- Substantive and methodological insights emerge together
- Different conversational partners provide different perspectives
- Explicit documentation creates stable ground

**About LLM Evaluation:**
- Scaffolding matters more than usually recognized
- "Same protocol" is ambiguous without L2 specification
- Agent-based evaluation requires different control strategies

**About Source Attribution Bias:**
- It's coherence bias, not partisan bias
- It's real but suppressible
- It's domain-adaptive
- It's a category error

---

## Meta-Reflection

### This Trace's Purpose

1. **Integration:** Shows how eight traces form coherent narrative
2. **Navigation:** Enables understanding which trace to read for which purpose
3. **Pedagogy:** Demonstrates how research actually happens

### How To Use This Document

**For substantive finding:** Read 004 → 006 → 008 sections

**For replication:** Read 008, reference 005, consult 007

**For methodology:** Read 002 → 005 → 007 → 008 sections

**For discovery process:** Read this entire meta-trace, then individual traces chronologically

### What This Shows About AI-Assisted Research

**Strengths:**
- Multiple perspectives
- Rapid iteration
- Explicit documentation
- Cross-conversation synthesis

**Challenges:**
- Each conversation starts fresh
- Required explicit documentation
- Different assistants had different strengths

**The Human Role:**
- Synthesizing across conversations
- Recognizing breakthroughs
- Deciding when to document
- Maintaining program coherence

---

## Conclusion

Eight epistemic traces, created across five conversations over three days, document a research program that:

1. **Discovered** a fundamental bias mechanism (coherence-as-credibility)
2. **Falsified** the original hypothesis (partisan bias)
3. **Identified** a critical methodological problem (L1→L2 gap)
4. **Developed** a framework for discussing it (L1/L2/L3)
5. **Designed** an implementation solution (two-layer control)
6. **Created** five executable studies ready to run

**Most importantly:** The traces demonstrate that careful documentation of reasoning processes—not just conclusions—is essential for rigorous AI-assisted research.

---

**End of Meta-Epistemic Trace**

**Cross-References:** All eight epistemic traces (002-008), 5 study files, 5 seed files, 5 conversation transcripts

**Next Action:** Execute Type 1 detection studies (Schuldenbremse mirror pair)

**Future Work:** Type 2 correction and Type 3 calibration pending Type 1 results
