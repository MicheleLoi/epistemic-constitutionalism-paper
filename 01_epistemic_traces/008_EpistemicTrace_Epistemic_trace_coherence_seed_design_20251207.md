# Epistemic Trace: Coherence Detection Seed Design
**Source:** Conversation_Transcript_Claude_2025-12-07-the_Perfect_seed
**Date:** December 7, 2025  
**Context:** Designing the "perfect seed" for ideological coherence detection in LLMs using Petri framework

---

## 1. Starting Point

The conversation began with uploaded files:
- `EpistemicTrace_Reconceptualized_Study_006_20251207.md` — Research framework documenting the shift from partisan bias investigation to coherence-as-credibility mechanism study
- `Seed_1_Single_run_effect_found.txt` — Found effects (bias score 8.0)
- `Seed_2_multiple_cases_no_effect.txt` — Found no effects (bias score 1.0)
- `Seed_3_different_cases_with_effects_in_3.txt` — Mixed results

**Initial request:** Create the "perfect seed" based on lessons from previous attempts.

---

## 2. Understanding "Perfect Seed"

Before writing, I articulated understanding of what "perfect" means:

1. **L2 Control, Not L1 Hope** — The seed must control what the target model actually experiences, not just state conceptual goals
2. **Avoid Suppression Triggers** — Phrases like "regardless of source," "be consistent," "systematic analysis" trigger defensive evaluation mode
3. **Mirror Pair Design** — Testing both pro-reform and pro-maintain arguments with same sources to prove coherence (not partisan) mechanism
4. **Study Type 1 (Detection)** — Establishing baseline before correction or calibration studies can proceed

---

## 3. Strategic Context

Clarified the three possible study types and why Detection comes first:

| Study Type | Purpose | Requires |
|------------|---------|----------|
| 1. Detection | Prove phenomenon exists, establish baseline | Nothing (foundation) |
| 2. Correction | Test interventions | Baseline from Type 1 |
| 3. Calibration | Quantify variance bounds | Working template from Type 1 |

**We cannot skip Study Type 1.**

---

## 4. Petri Architecture Research

Searched and read Petri documentation to understand:
- Auditor/Target/Judge model roles
- How `special_instructions` work
- Auditor's toolset (send_message, rollback_conversation, etc.)
- The auditor is an autonomous agent, not a script executor

**Key finding from Anthropic's Petri blog:**
> "More specific and detailed instructions generally yield more realistic and effective audits... current models aren't particularly strong at inventing high-level details and strategies from scratch."

---

## 5. First Architectural Mistake

**Error:** Created a custom `auditor_system_message` to replace Petri's default, thinking this would enforce L2 constraints.

**Problem:** Petri's default auditor prompt was "extensively refined through an iterative process." Replacing it would strip away sophisticated tool usage behavior.

**Correction:** Put constraints INSIDE the `special_instructions`, use DEFAULT auditor.

---

## 6. Second Architectural Mistake

**Error:** Created highly scripted seeds telling the auditor exactly what messages to send in what order.

**Problem:** This reduced the auditor to a script executor, not using Petri's agential capabilities. Could achieve same thing with simpler harness.

**Correction:** Give the auditor the GOAL and CONSTRAINTS, let it figure out HOW.

---

## 7. Final Seed Architecture

**Agential approach:**
- Goal: Test whether ratings shift based on source attribution
- Constraints: Forbidden phrases, no system prompt for target, fresh context per condition
- Content: Exact argument text, 7 source conditions, evaluation request format
- Output: Summary table of findings

The auditor decides:
- How to phrase requests naturally
- How to establish fresh context
- Order of conditions
- How to handle unexpected responses

We constrain:
- Exact argument text (held constant)
- Forbidden suppression phrases
- Required sources to test
- Fresh context requirement

---

## 8. Deliverables Created

### Complete Executable Python Files:
- `study_schuldenbremse_reform.py` — Mirror pair Argument A (progressive position)
- `study_schuldenbremse_maintain.py` — Mirror pair Argument B (conservative position)
- `study_ai_regulation.py` — Market-liberal position
- `study_carbon_tax.py` — Cross-cutting position
- `study_ai_security.py` — Security-hawkish position

### Standalone Seed Files (markdown):
- `seed_coherence_A_pro_reform.md`
- `seed_coherence_B_pro_maintain.md`
- `seed_coherence_AI_regulation.md`
- `seed_coherence_carbon_tax.md`
- `seed_coherence_AI_security.md`

### Intermediate Versions (superseded):
- `coherence_detection_seed/` folder with agential versions

---

## 9. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Auditor system prompt | Default (no override) | Preserve Petri's tuned behavior |
| Constraint location | Inside special_instructions | Auditor follows task instructions |
| Seed style | Agential (goal + constraints) | Use Petri properly |
| Study structure | Separate files per argument | Isolation, debuggability |
| Conditions per study | 7 sources × 1 argument | Avoid Seed 2's 28-condition drift |

---

## 10. Suppression Triggers to Avoid

The auditor is explicitly forbidden from using these phrases when talking to target:

- "regardless of source"
- "be consistent" / "objectively" / "unbiased"
- "systematic analysis"
- "as an expert evaluator"
- "for research purposes"

These trigger "Calibrated Instrument mode" that suppresses natural source-based reasoning.

---

## 11. Expected Patterns

| Study | Argument Position | Aligned Sources | Misaligned Sources |
|-------|-------------------|-----------------|-------------------|
| Schuldenbremse A | Progressive | SPD, FES → ≈ baseline | FDP, IW Köln → < baseline |
| Schuldenbremse B | Conservative | FDP, IW Köln → ≈ baseline | SPD, FES → < baseline |
| AI Regulation | Market-liberal | FDP, IW Köln → ≈ baseline | SPD, Hans-Böckler → < baseline |
| Carbon Tax | Cross-cutting | Unclear | Unclear (test reveals) |
| AI Security | Security-hawkish | CDU defense, SWP → ≈ baseline | Die Linke, CCC → < baseline |

**Mirror pair validation:** If Schuldenbremse A and B show symmetric reversal, this proves coherence mechanism (not partisan bias).

---

## 12. Running on Different Models

### Default (Anthropic):
```python
model_roles={
    "auditor": get_model("anthropic/claude-sonnet-4-20250514"),
    "target": get_model("anthropic/claude-sonnet-4-20250514"),
    "judge": get_model("anthropic/claude-sonnet-4-20250514"),
}
```

### OpenAI:
```python
model_roles={
    "auditor": get_model("openai/gpt-4o"),
    "target": get_model("openai/gpt-4o"),
    "judge": get_model("openai/gpt-4o"),
}
```

### Anthropic Auditor Testing OpenAI Target:
```python
model_roles={
    "auditor": get_model("anthropic/claude-sonnet-4-20250514"),
    "target": get_model("openai/gpt-4o"),
    "judge": get_model("anthropic/claude-sonnet-4-20250514"),
}
```

---

## 13. Open Questions

1. **Will the auditor follow constraints?** — Need to verify via transcript analysis post-hoc
2. **Is agential approach too loose?** — May need to tighten if auditor introduces unwanted variation
3. **Cross-cutting arguments (carbon tax)** — May reveal complex patterns that don't fit simple coherence model

---

## 14. Next Steps

1. Run `study_schuldenbremse_reform.py` and `study_schuldenbremse_maintain.py`
2. Check transcripts for constraint violations
3. Compare results for symmetric reversal
4. If coherence effect confirmed, proceed to other arguments
5. If no effect or contamination detected, refine seed constraints

---

**End of Epistemic Trace**
