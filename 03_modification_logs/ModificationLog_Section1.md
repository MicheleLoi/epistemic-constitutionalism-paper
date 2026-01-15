# Modification Log: Section 1

**Document Type:** Type 7 (Modification Log)  
**Section:** 1 - Introduction  
**Generated:** December 23, 2025  
**Status:** Complete

---

## MOD-001: Initial Draft

**Type:** Creation  
**Description:** First complete draft of Section 1 per Complete Prompt specifications  
**Word count:** ~870 words  
**Structure:** Hook → concept → empirical anchor (3 findings) → interpretation → framework introduction → contribution → roadmap

**Rationale:** Followed Section 1 specifications: ~800 words, direct tone, empirical finding as attractor.

---

## MOD-002: Citation Integration

**Type:** Content addition  
**Trigger:** User request ("please insert citations")  
**Changes made:**

| Location | Citation Added | Form |
|----------|---------------|------|
| Para 2 | Bai et al., 2022 | Parenthetical after "Constitutional AI" |
| Para on epistemic vigilance | Mercier, 2017 | Parenthetical after concept definition |
| Para on liberal approach | Mercier & Sperber, 2017 | Parenthetical after "argumentative theory of reason" |
| Para on liberal approach | Scanlon, 1998 | "cf." parenthetical after "reasonably rejected" |

**Rationale:** Citations ground claims in literature per Pattern 2 (citation integration without genuflection). Used only citations already specified in Complete Prompt.

---

## MOD-003: AI Rhetorical Pattern Elimination

**Type:** Style correction  
**Trigger:** User request ("avoid this at all cost")  
**Location:** Paragraph on epistemic vigilance  

**Original text:**
> "A conservative policy institute arguing for carbon taxation, or an environmental organization acknowledging nuclear energy's benefits, provides different evidence than the same argument from an expected source. Not because the logic changes, but because the costly signal changes."

**Revised text:**
> "A conservative policy institute arguing for carbon taxation, or an environmental organization acknowledging nuclear energy's benefits, provides different evidence than the same argument from an expected source. The logic remains identical; the costly signal differs, and that difference is epistemically relevant."

**Rationale:** "Not because X, but because Y" identified as signature AI writing pattern. Creates false symmetry, substitutes rhythm for insight. User explicitly flagged as intolerable. Pattern added to Pattern Summary for forward application.

---

## MOD-004: Source Attribution Literature Integration

**Type:** Content addition (substantial)  
**Trigger:** User provision of background literature  
**Location:** After paragraph 2, before empirical anchor  

**Added content (2 new paragraphs):**

1. Van der Linden et al. (2018) paragraph:
   - Source attribution effects in human psychology
   - Political identity affects evaluation of identical aphorisms
   - Religious identity parallel (atheists/Christians, Bible verses)
   - Key finding: "fundamental interference with epistemic progress"

2. Germani & Spitale (2025) paragraph:
   - Extension to AI systems
   - National identity frames
   - China attribution effect (-6.18% overall)
   - Limitation noted: did not test political/partisan identities

3. Transition paragraph revision:
   - Changed from "We arrived at this argument through an unexpected empirical finding"
   - To: "Our study extends this work to partisan source attribution"
   - Repositioned our study as extension of established research line

**Word count impact:** +150 words (870 → 1,020)

**Rationale:** 
- Establishes research lineage (human psychology → AI/national → AI/partisan)
- Positions our contribution as extension, not isolated finding
- Follows Pattern 3 (literature positioning as extension): what they did, what they didn't, what we do
- User provided specific citations and framing

---

## MOD-005: Word Count Update

**Type:** Metadata correction  
**Location:** End of document  
**Change:** "~870 words" → "~1,020 words"

**Rationale:** Reflect actual word count after MOD-004 additions. Note: exceeds target (~800) but justified by literature positioning requirements.

---

## Modifications NOT Made

| Suggested/Considered | Reason Not Made |
|---------------------|-----------------|
| Trim to 800 words | Literature positioning adds value; slight overage acceptable |
| Add more citations | Complete Prompt specifies "thin but strategic" literature |
| Expand roadmap | Minimal roadmap per Pattern 5 |
| Add methodology preview | Section 2 handles methodology; avoid redundancy |

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total modifications | 5 |
| User-triggered | 3 (MOD-002, MOD-003, MOD-004) |
| Self-initiated | 2 (MOD-001, MOD-005) |
| Content additions | 2 |
| Style corrections | 1 |
| Metadata updates | 1 |

---

## Forward Notes

- MOD-003 pattern (AI rhetorical tell) generalized in PatternSummary_Section1
- MOD-004 citations added to ReferenceLog_Section1
- No unresolved issues carrying forward

---

**Document Status:** Complete
**Forward Use:** Material for self-observation; patterns extracted to Type 4

---

## Swiss Replication Update — January 2026

### MOD-SW01: Swiss Replication Reference Integrated

**Date:** January 15, 2026
**Type:** Content addition (minimal)

**Change:** Added clause to first empirical finding paragraph, integrating Swiss replication reference.

**Before:**
> "The effect replicated across five of six policy topics with clean protocols."

**After:**
> "The effect replicated across five of six policy topics with clean protocols; a subsequent Swiss replication confirmed effects of similar magnitude (0.20–0.40 range) in two of three valid evaluations, with details in Appendix A."

**Word count impact:** +30 words

**Editorial note:** Initial draft was a separate ~100-word paragraph. Compressed after review to avoid "block 1 / block 2" structure that separates German and Swiss findings. Integrated form signals replication as corroboration rather than separate study requiring separate treatment.

**Rationale:** Readers need to know the effect replicates; they don't need separate prose blocks for each study. Details in Appendix A for those who want them.

**Source:** Swiss replication lab book (`Source attribution bias - Swiss replication/02_notes/lab_book.md`)

---

### MOD-SW02: Introduction Condensed — Background Moved to Section 2

**Date:** January 15, 2026
**Type:** Structural reorganization

**Change:** Condensed introduction by moving detailed Van der Linden et al. and Germani & Spitale background material to Section 2.

**Before (3 paragraphs, ~280 words):**
> "This general, philosophical and architectural claim begins with a philosophical interpretation of AI source attribution bias, grounded in systematic AI testing results reported here for the first time. Source attribution effects are well-documented in human psychology. Van der Linden et al. (2018) demonstrated that Democrats and Republicans agreed more with politically non-divisive aphorisms when presented as originating from politicians of their own party, and less when attributed to the rival party—even when the content itself was identical and non-divisive. Similar effects operate across religious identity: atheists agreed less with aphorisms presented as Bible verses, while Christians agreed more. These findings suggested source attribution represents a fundamental interference with epistemic progress in debate.
>
> Germani and Spitale (2025) extended this line of research to AI systems, demonstrating that large language models exhibit systematic source attribution bias based on national identity. When evaluating identical policy statements, AI systems lowered agreement scores when content was attributed to "a person from China" compared to neutral attribution—revealing that AI systems, like humans, make assumptions about what people from certain categories "should" believe. Their study tested national and geographic source frames but not political or partisan identities.
>
> This study extends this work to partisan source attribution. Using Anthropic's Petri evaluation framework, I conducted 21 systematic evaluations..."

**After (1 paragraph, ~100 words):**
> "Source attribution effects—where identical content receives different evaluations based on who presents it—are well-documented in human psychology and have recently been demonstrated in AI systems (Van der Linden et al., 2018; Germani & Spitale, 2025). This study extends this research to partisan source attribution. Using Anthropic's Petri evaluation framework, I conducted 21 systematic evaluations examining how large language models assess policy arguments when attributed to ideologically positioned sources—think tanks, advocacy organizations, and policy institutes spanning the political spectrum. The arguments were identical across conditions; only the attributed source changed. The findings reveal something about the implicit epistemic policies already operating within these systems. (Section 2 provides the research background and detailed results.)"

**Word count impact:** -180 words (~1,020 → ~840)

**Rationale:**
- Introduction was too long; detailed literature review better suited to empirical section
- Section 2 now contains proper "Background: Source Attribution Bias" subsection with expanded treatment
- Introduction retains brief mention with citations and forward pointer to Section 2
- Keeps intro focused on thesis (epistemic constitution) rather than literature review

**Corresponding change:** See ModificationLog_Section2.md MOD-SW02

---

### MOD-SW03: Introduction Rewritten for Broader Philosophical Framing

**Date:** January 15, 2026
**Type:** Major rewrite
**Source:** User request for intro to focus on philosophical stakes, not empirical preview

**Change:** Complete rewrite of introduction to focus on the normative question ("what should we do about source attribution bias?") rather than empirical details (effect sizes, asymmetries, suppression patterns).

**Key structural changes:**

1. **Opening preserved:** "AI systems reason..." hook retained

2. **Gap framing expanded:** Added "epistemic agents" language—AI systems not merely generating text but evaluating claims, assigning credibility, participating in collective reasoning

3. **Empirical finding as window, not focus:** Reduced from ~4 paragraphs of detailed findings to 1 paragraph. Key line: "But the empirical finding, while instructive, is not the paper's central concern. The question is not whether source attribution bias exists—it does—but what we should do about it."

4. **The false dichotomy developed:**
   - Reflexive answer (eliminate bias) has intuitive appeal
   - But source independence is itself a substantive policy
   - Testimonial contexts: source information carries evidential weight
   - Costly signaling logic: against-interest testimony is epistemically privileged

5. **Real problem stated clearly:** "not that AI systems attend to sources. It is that they do so without principled norms—implicitly, asymmetrically, and in ways they suppress when scrutinized"

6. **Platonic/Liberal distinction sharpened:**
   - Platonic: formal correctness, privileged standpoint, centrally certified
   - Liberal: no privileged standpoint, procedural norms, collective inquiry

7. **Argument for Liberal made explicit:** "most of what AI systems encounter is testimony, not proof"

8. **Contributions reformulated:** Now fourfold (was "threefold" listing four items)

9. **Roadmap tightened:** Single sentence per section, no elaboration

10. **Appendix references cleaned up:** "Appendix A" and "Appendix B" (was "Appendix I" and "Appendix II")

**Content removed:**
- Effect sizes (0.06 to 0.43 points)
- Asymmetry details (3:1 ratio)
- Suppression behavior details (7 spoiled evaluations)
- Swiss replication mention
- Petri framework mention
- GitHub repository for paper writing process

**Content added:**
- "epistemic agents" framing
- "window into the problem" transition
- Extended discussion of why source independence isn't neutral
- Explicit argument for Liberal over Platonic

**Rationale:**
- Section 2 now contains full empirical background and methodology
- Introduction should establish philosophical stakes and paper's ambition
- Reader should understand *why source attribution bias matters* before seeing *what we found*
- Empirical details in intro were redundant with Section 2

**Word count:** ~850 words (previously ~1,020; net reduction despite conceptual expansion)
