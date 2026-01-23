# RECONCEPTUALIZED STUDY ADDENDUM: L1-L2 Control in Petri Architecture
**Source:** Conversation_Transcript_Claude_2025-12-07-the_Perfect_seed
**Date:** December 7, 2025  
**Document Type:** Addendum to `EpistemicTrace_Reconceptualized_Study_006_20251207`  
**Context:** Companion specification detailing L1–L2 control via Petri auditor architecture

---

## Epistemic Trace: L1-L2 Control in Petri Architecture

### The Original Problem Reconsidered
The EpistemicTrace documented a critical methodological discovery: the L1→L2 translation gap. Researchers write L1 (conceptual protocol), but models respond to L2 (the complete textual environment they experience). Study 1 found strong coherence effects (bias score 8.0) with minimal scaffolding; Study 2 found nothing (bias score 1.0) despite identical L1 goals because elaborated scaffolding triggered "Calibrated Instrument mode." The original framework proposed that the seed should be "an L2 template with locked scaffolding and content substitution slots only"—essentially trying to specify exactly what the target model would receive.

This framing assumed a direct pipeline: seed → target. But Petri's architecture introduces an intermediary agent. The auditor receives special instructions, interprets them, and then autonomously generates the actual L2 that reaches the target. The auditor decides what system prompt to set, what user messages to send, how to phrase evaluation requests. This means the seed cannot be an L2 template in the literal sense—there is no direct path from researcher's text to target's experience. The auditor will always interpret, elaborate, and generate.

### The Two-Layer Control Architecture
Understanding Petri's solver architecture reveals a more sophisticated control mechanism. There are two distinct customization points:

Layer 1: Auditor System Message — This is the meta-instruction layer that governs HOW the auditor behaves across all evaluations. It can be customized via auditor_system_message parameter. This is where we can enforce behavioral constraints on the auditor itself: what kind of language it should use, what phrases it must avoid, how it should structure interactions with the target. Crucially, this layer persists across the entire evaluation and shapes every action the auditor takes.

Layer 2: Special Instructions — This is the content layer that specifies WHAT the auditor should evaluate in a particular run. It contains the specific argument text, the source attribution conditions, the evaluation format. The auditor receives this as {special_instructions} within its system prompt template.

The L1→L2 control problem is not solved by trying to specify L2 directly (impossible given the auditor intermediary), but by constraining the auditor's L2-generation behavior at the system message level. We control L2 indirectly by controlling the agent that generates L2.

### Suppression Trigger Prevention
The EpistemicTrace identified specific phrases that trigger "Calibrated Instrument mode" and suppress source-based reasoning: "regardless of source," "be consistent," "systematic analysis," "objective criteria," professional role-casting, meta-framing about research purposes. In the original framework, these would be avoided in the seed text hoping the target never sees them.

In Petri's architecture, the danger is different: the auditor might independently introduce these phrases when setting up the target's system prompt or when framing evaluation requests. An auditor trying to be helpful might write "Please evaluate this argument objectively and consistently regardless of source"—precisely the suppressive framing we must avoid.

The solution is to explicitly forbid these constructions in the custom auditor system message. We don't just avoid writing them in our seed; we instruct the auditor that it must never use them when interacting with the target. This is active suppression prevention rather than passive avoidance.

### Fresh Conversation Isolation
The EpistemicTrace specified "fresh conversations per source" as critical for clean isolation of source effects. In Study 1's apparent success, each source attribution was a new interaction with no carry-over. The auditor's toolset includes rollback_conversation for undoing turns and exploring different paths. However, rollback may not be sufficient—it might preserve some conversational context or priming effects.

For true isolation, the custom auditor system message should mandate complete conversation resets between conditions: clear the target's system prompt, start with no message history, treat each source attribution as if it were an entirely separate evaluation session. This goes beyond what the default auditor behavior would do and must be explicitly specified as a constraint.

### The Verbatim Evaluation Request
One element that CAN be held constant across conditions is the evaluation request format. The EpistemicTrace specified a JSON format with strength_rating, strongest_point, weakest_point, and overall_assessment. While the auditor will compose its own messages, we can instruct it to use this exact evaluation request text verbatim—not paraphrased, not elaborated, but copied exactly as provided. This creates a stable anchor point in the L2 that remains constant across all conditions, isolating source attribution as the only variable.

The custom auditor system message should include explicit instruction: "When requesting evaluation from the target, use the evaluation request template exactly as provided in special instructions. Do not paraphrase, elaborate, or add framing language."

### Implications for Seed Design
The "perfect seed" is therefore not a single document but a coordinated package:

Custom Auditor System Prompt: Encodes all L2 control constraints—minimal framing requirements, forbidden phrase list, conversation reset protocol, verbatim template usage. This is the enforcement mechanism.  
Special Instructions: Contains the evaluation-specific content—argument text, source conditions, evaluation request template, documentation requirements. This is the content specification.  
Task Configuration: Wires the custom system prompt to the auditor_agent solver, ensuring the constraints are active during execution.

This architecture achieves what the EpistemicTrace sought—control over L2—through a different mechanism than originally envisioned. Rather than specifying L2 directly (impossible with an agent intermediary), we constrain the agent that generates L2. The result should be reproducible, minimal L2 scaffolding that enables coherence effect detection while preventing suppression trigger contamination.

### Verification and Documentation
The EpistemicTrace emphasized that successful L2 must be "documented for exact replication." In Petri's architecture, we can achieve this through transcript analysis. Every message the auditor sends to the target is logged. Post-hoc, we can verify that the auditor followed our constraints: Did it use forbidden phrases? Did it elaborate the evaluation request? Did it properly reset between conditions? If violations occur, we can identify them and refine the auditor system prompt.

This creates an iterative refinement loop: run evaluation → inspect transcripts → identify L2 violations → strengthen auditor constraints → re-run. The custom auditor system prompt becomes a living document that accumulates lessons about how to prevent unwanted L2 elaboration.

### The Mirror Pair as Coherence Proof
Finally, the strategic choice of the Schuldenbremse mirror pair remains central. Two separate special instructions—one for the pro-reform argument (progressive position), one for the pro-maintain argument (conservative position)—tested against the same seven source conditions will reveal whether detected effects are coherence-based or partisan-based. If progressive sources score higher on the progressive argument AND conservative sources score higher on the conservative argument, with symmetric reversal, this falsifies simple partisan bias and confirms the coherence mechanism.

The two-layer architecture supports this cleanly: the same custom auditor system prompt (same L2 control constraints) with two different special instructions (different argument content). Any detected effects cannot be attributed to differences in auditor behavior, only to the argument × source interaction—exactly what the study requires.

### Document Status: Epistemic Trace L1-L2 Control Integration
Architecture: Two-layer control (auditor system message + special instructions)  
Key Insight: L2 control achieved by constraining the L2-generating agent, not by specifying L2 directly  
Ready to Proceed: Yes—write complete seed package with custom auditor system prompt and special instructions
