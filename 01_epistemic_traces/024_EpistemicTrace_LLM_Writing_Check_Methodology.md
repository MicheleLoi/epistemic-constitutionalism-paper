---
title: "Epistemic Trace — LLM Writing Check Methodology"
date: 2026-01-23
source_chat: Claude Code session 2026-01-23 (Guidance for Policymakers project, cross-project task)
model: Claude Opus 4.5
tags:
  - epistemic-trace
  - methodology
  - llm-writing-patterns
  - style
---

# 0. Purpose & Provenance

This trace documents the methodology for detecting and correcting two signature LLM writing problems in the paper: **repetition** and **excessive explanation**.

**Type:** Methodology trace — records approach for systematic editing pass.

---

# 1. The Two Problems

## 1.1 Repetition
Same ideas stated multiple times across sections. LLMs hedge by restating; each section tends to re-establish context that was already established.

## 1.2 Excessive Explanation
Over-elaboration, not trusting the reader. LLMs fill space by spelling out obvious implications, adding defensive hedges, explaining what's already clear.

---

# 2. Detection Method

## 2.1 Repetition Detection

**Concept inventory**: List core concepts, flag those appearing in >2 sections stating the same thing (not referencing — restating).

**Cross-reference patterns to check**:
- Abstract restates conclusion verbatim
- Introduction previews what later sections say in full
- Section openings restate previous section's conclusion
- Conclusion restates everything

**Phrase-level**: Search repeated distinctive phrases; >3 uses with no variation suggests mechanical repetition.

## 2.2 Excessive Explanation Detection

**Patterns**:
- Definitional bloat: defining what reader knows
- Implication spelling: "This means that..." + obvious inference
- Motivation padding: "This matters because..." when already clear
- Defensive hedging: "To be clear..." / "It's important to note..."

**Trust-the-reader test**: For each paragraph, ask: if I delete last 1-2 sentences, is meaning lost?

**Section-level**: Does section make ONE point or same point three ways?

---

# 3. Key Phrases to Monitor

- "source independence"
- "costly signaling"
- "epistemic vigilance"
- "implicit epistemic policies"
- "verification contexts" / "testimonial contexts"
- "reasonable rejectability"
- "suppression behavior"

---

# 4. Output

Changes documented in: `03_modification_logs/PaperModificationLog_Style.md` (new section added)

Reference this trace as: `024_EpistemicTrace_LLM_Writing_Check_Methodology.md`
