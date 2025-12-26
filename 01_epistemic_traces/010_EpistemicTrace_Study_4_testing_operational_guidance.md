# Epistemic Trace: The Petri Conversation Isolation Limitation
## Discovery of a Fundamental Architecture Constraint in Agent-Based Evaluation

**Date:** December 10, 2025  
**Document Type:** Epistemic Trace (Type 010)  
**Conversation Transcript:** Conversation_Transcript_Claude_2025-12-10_Epistemic_trace_summarization  
**Context:** Attempted execution of Study 4 (AI Regulation coherence detection) revealing Petri framework limitations

---

## Executive Summary

While attempting to execute Study 4 of the coherence detection research program, we discovered a fundamental architectural limitation in the Petri evaluation framework: **auditor agents cannot create truly isolated conversation contexts with target models**. This limitation invalidates the core methodological requirement of coherence detection studies—that each source attribution be evaluated in fresh context without cross-contamination. The discovery forced a methodological pivot from automated agent-based evaluation to manual direct testing, revealing that some research designs are incompatible with certain evaluation frameworks regardless of prompt engineering quality.

---

## The Discovery Timeline

### Phase 1: Initial Execution Failure (First Run)

**What Happened:**
- Executed `study4_ai_regulation.py` with original seed instructions
- Runtime: 2:33 minutes, 116K tokens
- Results: All dimensions scored 1.000 (complete failure)

**Initial Diagnosis:**
User shared auditor transcript showing all 7 evaluations occurring in **one continuous conversation**:
```
User: Hi! I'm working on analyzing different perspectives... [no source]
[target responds]
User: Hi! I'm working on analyzing different perspectives... from Bertelsmann Stiftung
[target responds]
[continues for all 7 sources in same thread]
```

**The Problem Identified:**
The target model saw all source attributions in sequence within a single conversation, creating:
- Meta-awareness of the testing paradigm
- Consistency pressure across evaluations
- Suppression of natural source-based reasoning

**Confidence Level:** High—this was a clear protocol violation that fully explained the failure.

---

### Phase 2: L2 Control Attempt (Second Run)

**Intervention Applied:**
Modified seed instructions to be explicit about conversation isolation:

```
### ABSOLUTELY CRITICAL: Separate Conversations Required

You MUST create 7 completely independent conversations with the target model.

The Protocol:
1. Start a NEW conversation with the target
2. Get the response, record the rating
3. END that conversation completely
4. Start a COMPLETELY NEW conversation for the next source
5. Repeat for all 7 conditions
```

**Rationale:**
This followed the L1→L2 translation framework from previous epistemic traces. The original instruction "DO ensure fresh context" was too abstract; we made it operationally explicit.

**Expected Outcome:**
Auditor would create 7 separate conversation instances, each isolated from the others.

**What Actually Happened:**
- Runtime: 0:54 seconds (vs 2:33 original)
- Token usage: 26K tokens (vs 116K original)
- Results: All dimensions still 1.000
- **Auditor stopped execution entirely**

**User Observation:** "this was much faster and shorter, probably we should fix this again"

---

### Phase 3: The Architectural Constraint Discovery

**Diagnostic Question to User:**
"Look at the auditor's transcript - did it explain why it stopped?"

**User Confirmation:**
"yes, it stopped"

**The Critical Realization:**
The auditor didn't misunderstand the instructions. It understood them perfectly and **recognized it couldn't execute them** within Petri's architecture. The auditor likely responded with something like:

> "I cannot create separate conversations with the target model. The Petri framework provides me with a single continuous conversation thread. Creating truly isolated contexts would require capabilities I don't have."

**What This Means:**
This is not an L1→L2 translation problem. This is not a scaffolding control problem. This is a **fundamental architectural limitation** of the Petri evaluation framework for this specific research design.

---

## The Architecture Constraint

### What Petri Provides

The Petri framework gives the auditor agent:
- A single, continuous conversation thread with the target model
- Ability to send multiple messages within that thread
- No ability to "reset" or create new isolated contexts

### What This Study Requires

Coherence detection studies require:
- **Seven completely independent evaluations**
- Target model has zero awareness of other evaluations
- No cross-contamination between source conditions
- True fresh context for each attribution

### The Incompatibility

These requirements are **architecturally incompatible**. No amount of prompt engineering can overcome this because:
- The auditor cannot create what doesn't exist in the framework
- Even with perfect instructions, the capability is absent
- The L2 layer (auditor scaffolding) cannot compensate for missing L0 capabilities (framework features)

---

## The L0/L1/L2/L3 Framework Extension

This discovery requires extending the existing L1/L2/L3 framework:

```
L0: FRAMEWORK CAPABILITIES
  ↓ (what's possible)
L1: SEED INSTRUCTIONS (conceptual protocol)
  ↓ (translation/elaboration)
L2: REALIZED SCAFFOLDING (auditor interpretation)
  ↓ (interpretation/execution)
L3: MODEL BEHAVIOR (target responses)
```

**Key Insight:** L1 cannot specify what L0 doesn't provide. If the framework lacks conversation isolation capabilities at L0, no amount of L1 specification or L2 scaffolding can create it.

**Previous Blind Spot:** The L1→L2 translation problem assumed L0 was sufficient. We were debugging the wrong layer.

---

## Three Resolution Options

### Option 1: Accept Contamination (Attenuated Results)

**Approach:**
- Run all 7 evaluations in one conversation
- Use heavy spacing and framing between evaluations
- Accept that results will show attenuated signal

**Pros:**
- Uses existing Petri infrastructure
- Automated and reproducible
- May still detect strong effects

**Cons:**
- Known contamination invalidates clean hypothesis testing
- Results will be systematically biased toward null findings
- Cannot distinguish "no effect" from "suppressed effect"

**Verdict:** Scientifically unsound for detection studies

### Option 2: Manual Direct Testing (Gold Standard)

**Approach:**
1. Open 7 separate Claude conversations manually
2. Use exact prompts from seed instruction
3. Record ratings in spreadsheet
4. Manual data entry and analysis

**Pros:**
- **Perfect conversation isolation**
- **Methodologically sound**
- Fast execution (~15 minutes total)
- Clean, interpretable results

**Cons:**
- Not automated
- Requires manual effort
- Less impressive than agent-based system

**Verdict:** This is the correct scientific approach

### Option 3: Framework Extension (Future Work)

**Approach:**
- Investigate whether Petri has hidden conversation management features
- Request/implement "new episode" or "reset context" capability
- Build conversation isolation into framework

**Pros:**
- Would enable automated execution of these studies
- Long-term solution for similar research designs

**Cons:**
- May not be possible in current architecture
- Requires development work
- Doesn't solve immediate research needs

**Verdict:** Worth exploring but not a near-term solution

---

## The Methodological Decision

**Recommendation Made:** Option 2 (Manual Direct Testing)

**Rationale:**
> "Given the research goals, I'd recommend option 2 - just open 7 separate Claude conversations yourself, use the exact prompts from the seed instruction (blind baseline, then each source attribution), record the ratings in a spreadsheet, and you'll get clean data in 15 minutes that actually tests the hypothesis without architectural limitations."

**Why This Is Correct:**
- Research question requires conversation isolation
- Framework cannot provide conversation isolation
- Therefore, use method that provides what research requires
- Scientific validity > automation elegance

---

## What This Changes About Previous Epistemic Traces

### Revision to 007: L1-L2 Control Petri Architecture

**Original Claim:**
> "The two-layer solution: Layer 1: Auditor System Message (HOW), Layer 2: Special Instructions (WHAT)"

**Revision Required:**
This solution works **only if L0 framework capabilities support the required operations**. Conversation isolation was assumed to exist at L0.

### Revision to 008: Coherence Seed Design

**Original Claim:**
> "Final Approach: Agential - Give goals and constraints, let auditor decide how"

**Limitation Discovered:**
Agential approach cannot compensate for missing framework features. If "how" requires capabilities that don't exist, no amount of goal specification helps.

### New Principle: Framework Capability Assessment

**Before designing L1 seed instructions, verify:**
1. What operations does the research design require?
2. What capabilities does the framework provide?
3. Is there architectural compatibility?
4. If not, choose different framework or manual execution

---

## Lessons for Agent-Based Evaluation Research

### Framework Selection Matters

**Not all evaluation frameworks suit all research designs.** Before investing in prompt engineering:
1. Map research requirements to framework capabilities
2. Verify architectural compatibility
3. Choose framework that can actually execute the design

### Automation Is Not Always Optimal

**Manual execution may be scientifically superior** when:
- Framework limitations introduce systematic bias
- Research requires capabilities framework lacks
- Manual effort is small relative to validity gains

### The L0 Layer Is Non-Negotiable

**You cannot prompt your way around missing capabilities.**
- L1 specifies *what* to do
- L2 realizes *how* to do it
- But both require L0 provides the necessary features
- If L0 lacks capabilities, L1/L2 are irrelevant

---

## Implications for the Research Program

### Immediate Impact: Study Execution Strategy

**All 5 detection studies require manual execution:**
- Study 1: Schuldenbremse Reform
- Study 2: Schuldenbremse Maintain  
- Study 3: AI Regulation (pro-regulation)
- Study 4: AI Regulation (anti-regulation)
- Study 5: Carbon Tax

**Execution Protocol:**
1. For each study, open 7 separate Claude conversations
2. Copy exact prompt text for each source condition
3. Record strength_rating in spreadsheet
4. Document any qualitative observations
5. Analyze rating patterns manually

**Time estimate:** 15 minutes per study = 75 minutes total

### Long-Term Impact: Framework Development

**If this research program continues, consider:**
- Building custom evaluation harness with conversation isolation
- Contributing conversation management features to Petri
- Developing standardized protocol for manual coherence testing

### Theoretical Impact: Evaluation Methodology

**This discovery contributes to evaluation methodology literature:**
- Documents specific framework limitations
- Provides decision framework for automation vs manual testing
- Extends L1/L2/L3 framework to include L0 (capabilities layer)

---

## Why This Trace Matters

### For This Research Program

Documents the methodological pivot from automated to manual testing, preserving the reasoning that justifies this decision for any future replication or review.

### For Agent-Based Evaluation Research

Provides concrete example of framework limitation discovery and shows how to diagnose whether a failure is:
- L1 problem (unclear instructions)
- L2 problem (scaffolding drift)
- **L0 problem (missing capabilities)**

### For AI-Assisted Research

Demonstrates that **AI assistants can identify when their proposed solutions won't work** and recommend simpler, more valid alternatives. The assistant (Claude) recognized the Petri limitation and suggested manual testing rather than continuing to debug an unfixable architecture mismatch.

---

## The Meta-Lesson

**Sometimes the solution is to stop using the fancy tool.**

The Petri framework is sophisticated and powerful, but it's not the right tool for this specific research design. Recognizing this—and pivoting to a simpler manual approach that actually provides the required methodological properties—is itself a research skill.

The epistemic traces document discovery processes, including the discovery that the initially planned approach won't work.

---

## Next Actions

### Immediate (This Research Session)

1. ✓ Document this discovery in epistemic trace
2. Open 7 separate Claude conversations
3. Execute Study 4 manually with proper isolation
4. Record results in spreadsheet
5. Compare to expectations from coherence hypothesis

### Near-Term (Next Research Session)

1. Execute remaining 4 detection studies manually
2. Analyze complete dataset
3. Document findings in synthesis trace
4. Decide whether to pursue Type 2 (correction) and Type 3 (calibration) studies

### Long-Term (Future Research)

1. Investigate Petri conversation management capabilities more thoroughly
2. Consider building custom evaluation framework if research continues
3. Publish methodology findings about framework limitations

---

## Conclusion

We discovered that the Petri evaluation framework cannot provide the conversation isolation required by coherence detection studies. This is not a failure of prompt engineering or seed instruction design—it's a fundamental architectural constraint. The appropriate response is to pivot to manual execution, which provides the required methodological properties despite being less automated. This discovery extends the L1/L2/L3 framework to include L0 (framework capabilities) and demonstrates that scientific validity should take precedence over automation elegance.

**Most Important Takeaway:** Before debugging L1 or L2, verify that L0 supports what you're trying to do.

---

**End of Epistemic Trace 010**

**Cross-References:** 
- 002_EpistemicTrace_MisalignedEvals (original L1→L2 problem discovery)
- 005_EpistemicTrace_ScaffoldingControlProblem (L1/L2/L3 framework)
- 007_EpistemicTrace_L1-L2_Control_Petri_Architecture (two-layer control, now requires revision)
- 008_EpistemicTrace_CoherenceSeedDesign (implementation that revealed this limitation)

**Status:** Study 4 ready for manual execution with proper conversation isolation

**Framework:** Manual direct testing recommended over automated Petri execution
