# APPENDIX B: Paper Writing Documentation

This appendix documents the AI-assisted writing process used to produce this paper. Following principles of epistemic transparency advocated in the paper itself, we provide a complete account of how human direction and AI text generation were combined, what artifacts were produced, and what lessons emerged regarding the differential suitability of AI models for various writing tasks.

**Scope:** This appendix documents the *paper writing process* (December 23–26, 2025), not the development of the underlying empirical study (December 5–18, 2025). Materials from the study development phase—including conversation transcripts, epistemic traces, and intermediate analyses—are preserved and made available for review (https://github.com/MicheleLoi/epistemic-constitutionalism-paper), but their detailed documentation falls outside the scope of this appendix. Appendix A provides the extended methodology for the empirical study itself.

---

## B.1 Methodology Overview

### B.1.1 JPEP-Inspired Transparency Approach

The documentation methodology draws on the approach developed in Loi (2025, JPEP Appendix A), which established a framework for transparent AI-assisted academic writing. That framework introduced a document ontology for tracking inputs, outputs, and decision points throughout the writing process. We adopted a simplified version of this approach, making several modifications to reduce complexity while preserving the core commitment to real-time documentation rather than post-hoc reconstruction.

Key differences from the reference approach include:

| JPEP Appendix A Approach | Present Approach |
|--------------------------|------------------|
| 11 document types | 8 core types + supporting documentation |
| Post-hoc reconstruction | Real-time documentation |
| Emergent documentation ontology | Predefined, simplified |
| Parallel branching paths | Single linear progression |
| Prompt Development Logs throughout | Only for mid-course corrections |
| Section Guidance for every section | Only when departures required |

### B.1.2 Executive AI + Writing AI Separation

The writing process employed a two-tier AI architecture:

**Executive AI:** A separate conversation dedicated to process oversight, decision-making, and documentation (Conversation_Transcript_Claude_2025-12-26_Executive_plan_for_constitutiona_AI_paper_writing). This conversation (a) tracked which artifacts were produced at each stage, (b) made decisions about model selection for each section, (c) documented mid-course corrections when the argument evolved beyond the original prompt specifications, and (d) maintained the master process log from which this appendix is derived.

**Writing AI:** Fresh conversation instances initiated for each section of the paper. Each writing instance received: the Complete Prompt (constant), relevant Section Summaries and Pattern Summaries from prior sections (cumulative), and where applicable, Section Guidance documents specifying departures from the original prompt.

This separation served two purposes. First, it prevented conversation context from accumulating in ways that might cause the writing AI to lose coherence or drift from instructions. Second, it created clear boundaries between the authorial role (held by the human via the executive conversation) and the text-generation role (held by fresh AI instances).

### B.1.3 Document Type System

Eight document types structured the workflow, organized by function:

| Type | Name | Count | Function |
|------|------|-------|----------|
| 1 | Complete Prompt | 1 | Master document specifying argument architecture, section specifications, tone, and required references. Served as constant input to all sections. |
| 2 | Epistemic Trace | 25 | Documentation of executive-level decisions, discovery moments, and resolution of discrepancies. Study development phase: 001–019 + 014b (20 traces). Writing phase: 020 (1 trace). Post-writing pre-v1: 021–023 (3 traces). Post-v1: 024 (1 trace). Select traces (008, 014, 020) informed writing content. |
| 3 | Section Guidance | 3 | Mid-course corrections issued when argument evolution required departures from Complete Prompt specifications. Generated for Sections 6, 7, and post-v1 Appendix B update. |
| 4 | Pattern Summary | 10 | Cumulative record of stylistic and structural patterns established in prior sections, plus style pass patterns. |
| 5 | Section Summary | 8 | Compressed representation of each completed section's content and commitments, enabling subsequent sections to maintain coherence without full-text context. |
| 6 | Reference Log | 7 | Running bibliography tracking citations introduced in each section. |
| 7 | Modification Log | 16 | Documentation of changes made during and after drafting, including section-level logs (13) and paper-level review logs (3: epistemic review, manual review, style pass). |
| 8 | Prompt Development Log | 4 | Documentation of prompt evolution, including main prompt development, mid-course Section Guidance rationale (Sections 6 and 7), and post-v1 Appendix B update. |

Additional documentation not assigned type numbers:

| Category | Count | Function |
|----------|-------|----------|
| Conversation Transcripts | 45 | Complete records of all AI conversations (Claude and ChatGPT). 15 transcripts document the writing phase; 28 document the study development phase; 2 document post-v1 updates. |
| Working Notes | ~35 files | Seeds, extraction scripts, verification reports, Lab Book versions (v1–v5, with v5 authoritative), and intermediate analyses preserved in 09_notes/. |

**Feed-forward vs. retrospective distinction:** Types 1, 3, 4, and 5 routinely fed forward into subsequent writing instances. Types 6, 7, and 8 documented the process retrospectively for transparency and review. Type 2 (Epistemic Traces) served primarily as retrospective documentation, with exceptions: EpistemicTrace_020 informed Lab Book versioning decisions, and EpistemicTraces 008 and 014 informed Section 2's acknowledgment of protocol iteration (see MOD-014 in ModificationLog_Section2).

---

## B.2 Workflow Summary

### B.2.1 Section-by-Section Process

The paper was written in six phases spanning December 23–26, 2025. The following table summarizes model selection, primary inputs, and outputs for each section:

| Section | Model | Primary Inputs | Key Outputs |
|---------|-------|----------------|-------------|
| 1. Introduction | Opus | Complete Prompt, Lab Book v4 | Draft (~1,020 words), SectionSummary, PatternSummary (patterns 1–5) |
| 2. The Finding | Sonnet | Complete Prompt, SectionSummary S1, PatternSummary S1, Lab Book v4 | Draft (~1,806 words), PatternSummary (patterns 6–12) |
| 3. The Problem | Opus | Complete Prompt, SectionSummaries S1–S2, PatternSummaries S1–S2 | Draft, PatternSummary (patterns 13–17) |
| 4. The Constitution Idea | Opus | Complete Prompt, SectionSummary S3, PatternSummary S3 | Draft, PatternSummary (patterns 18–21) |
| 5. Platonic vs. Liberal | Opus | Complete Prompt, SectionSummaries S3–S4, PatternSummary S4 | Draft, SectionGuidance S6, PatternSummary (patterns 22–25) |
| 6. Why Liberal | Opus | Complete Prompt, SectionSummaries S2 + S5, PatternSummary S5, SectionGuidance S6 | Draft, SectionGuidance S7, PatternSummary (patterns 26–30) |
| 7. Capacities | Opus | Complete Prompt, SectionSummary S6, PatternSummary S6, SectionGuidance S7 | Draft (10 versions, ~1,260 words final), PatternSummary (patterns 31–33) |
| 8. Limitations | Opus | Complete Prompt, SectionSummary S7, PatternSummary S7 | Draft (first draft accepted without modification) |
| 9. Conclusion | Opus | Complete Prompt, SectionSummaries S1–S8, PatternSummary S7 | Final draft |
| Appendix A | Opus* | Lab Book v5, topic-specific data files | Extended methodology tables |
| Appendix B | Opus | Process documentation, file structure | This appendix |

*Appendix A initially drafted with Sonnet; rejected due to hallucinated data; redrafted with Opus.

### B.2.2 Mid-Course Corrections

Two Section Guidance documents were generated during the writing process, each documenting a substantive departure from the original Complete Prompt specifications:

**SectionGuidance_Section6 (Mercier Distribution):** During Section 5 writing, it became apparent that the Complete Prompt's specifications for Mercier's work were ambiguous regarding distribution across sections. The guidance clarified: general argumentation theory belongs in Section 5 (Platonic vs. Liberal framing), while the specific concept of epistemic vigilance belongs in Section 6 (Why Liberal). This was documented in PromptDevelopmentLog_Section6.

**SectionGuidance_Section7 (Capacities Not Rules):** Section 6's argument that correct AI epistemic behavior cannot be pre-specified created a logical tension with Section 7's original framing as a list of behavioral rules. The guidance reframed Section 7 as specifying *capacities* (later refined to *constitutional principles*) rather than rules—a shift from "AI should do X" to "AI should be *capable* of doing X when appropriate." This was documented in PromptDevelopmentLog_Section7.

Both guidance documents were provided as inputs to the writing AI for their respective sections and are available for reviewer inspection.

### B.2.3 Pattern Accumulation

Pattern Summaries served as a mechanism for maintaining stylistic consistency and preventing regression to AI default behaviors. Thirty-three patterns accumulated across nine sections:

- Section 1: Patterns 1–5 (foundational voice establishment)
- Section 2: Patterns 6–12 (empirical presentation conventions)
- Section 3: Patterns 13–17 (diagnostic argumentation patterns)
- Section 4: Patterns 18–21 (constitutional framing patterns)
- Section 5: Patterns 22–25 (philosophical distinction patterns)
- Section 6: Patterns 26–30 (liberal argument patterns)
- Section 7: Patterns 31–33 (principle derivation patterns)
- Sections 8–9: No new patterns added

Three meta-patterns proved particularly important:

1. **Pattern 1 (AI Rhetorical Tell Elimination):** Systematic removal of discourse markers, hedging patterns, and structural choices characteristic of AI-generated text.
2. **Pattern 7 (Evidence Quality Honesty):** Explicit acknowledgment of differential evidence strength rather than rhetorical smoothing.
3. **Pattern 14 (Section Role Over Pattern Application):** Recognition that previously established patterns should be adapted to each section's argumentative function rather than applied mechanically.

---

## B.3 Artifacts Generated

### B.3.1 Complete Artifact Registry

**Core Writing Artifacts**

| Artifact Category | Location | Count | Status |
|-------------------|----------|-------|--------|
| Complete Prompt | 02_main_prompt/ | 1 | ✅ Authoritative |
| Section Summaries | 06_section_summaries/ | 8 | ✅ Complete (S1–S8) |
| Pattern Summaries | 04_pattern_summaries/ | 10 | ✅ Complete (S1–S9 + Style) |
| Section Guidance | 05_section_guidance/ | 3 | ✅ Complete (S6, S7, AppendixB_PostV1) |
| Modification Logs | 03_modification_logs/ | 16 | ✅ Complete (13 section-level + 3 paper-level) |
| Reference Logs | 07_reference_logs/ | 7 | ✅ Complete (S1–S7) |
| Prompt Development Logs | 08_prompt_development_logs/ | 4 | ✅ Complete (Main, S6, S7, AppendixB_PostV1) |

**Research and Process Documentation**

| Artifact Category | Location | Count | Status |
|-------------------|----------|-------|--------|
| Epistemic Traces | 01_epistemic_traces/ | 25 | ✅ Complete |
| Conversation Transcripts | 00_conversations_full/ | 45 | ✅ Complete |
| Working Notes | 09_notes/ | ~35 files | Seeds, extraction scripts, verification reports, Lab Book versions (v1–v5, with v5 authoritative), and intermediate analyses |

**Output Documents**

| Artifact | Status | Notes |
|----------|--------|-------|
| Section drafts (S1–S9) | ✅ Complete | Individual section files |
| paper_full_draft.md | ✅ Complete | Assembled paper |
| references_compiled.md | ✅ Complete | Final bibliography |
| Appendix_A.md | ✅ Verified | Extended methodology tables |
| Appendix_B.md | ✅ Complete | Paper writing documentation |

### B.3.2 Feed-Forward vs. Retrospective Artifacts

**Feed-forward artifacts** were provided as inputs to subsequent writing instances:
- Complete Prompt (all sections)
- Lab Book v5 (empirical sections)
- Section Summaries (cumulative)
- Pattern Summaries (cumulative)
- Section Guidance documents (Sections 6 and 7 only)

**Retrospective artifacts** documented the process but did not influence subsequent writing:
- Modification Logs
- Reference Logs
- Prompt Development Logs
- Epistemic Traces (with exceptions noted in B.1.3)
- Verification reports

This distinction matters for understanding the causal structure of the writing process: feed-forward artifacts shaped the paper's content, while retrospective artifacts exist solely for transparency and review.

---

## B.4 Lessons Learned

### B.4.1 Model Task Suitability

The writing process provided empirical data on differential model suitability for various tasks. The following recommendations emerged:

| Task Type | Recommended Model | Rationale |
|-----------|-------------------|-----------|
| Philosophical argumentation | Opus | Maintains complex argument structure; produces distinctive voice |
| Empirical data compilation | Opus | Data accuracy critical; weaker models hallucinate |
| Cross-reference verification | Opus | Requires attending to multiple instances |
| Mechanical tasks (assembly, formatting) | Sonnet | Reliable for copy/combine/format operations |
| Reference bibliography compilation | Sonnet | Mechanical extraction and formatting |

### B.4.2 Data Verification Requires Stronger Models

A significant methodological finding emerged from the Appendix A drafting process. The initial draft, produced by Sonnet, contained multiple data errors:

- Claimed 12 evaluations when the actual count was 21
- Fabricated evaluation IDs not present in the source data
- Reported effect sizes inconsistent with Lab Book v5
- Conflated source conditions across different topics

Root cause analysis indicated that Sonnet hallucinated plausible-sounding data when unable to parse the Lab Book v5 structure, rather than acknowledging parsing failure. The section was redrafted with Opus, which correctly extracted all data from source documents.

### B.4.3 Hallucination Risk in Empirical Compilation

Three hallucination failure modes were observed with the weaker model:

1. **ID fabrication:** When unable to locate actual evaluation IDs, the model generated plausible-looking alphanumeric strings that followed the format of real IDs but did not correspond to actual data.

2. **Data smoothing:** When source data showed irregular patterns (e.g., two evaluations on the same topic with different effect sizes), the model reported averaged or simplified values rather than the actual distribution.

3. **Premature completion:** During verification, the model checked only the first instance matching a criterion, declaring verification complete without detecting additional instances. This led to a false report of internal inconsistency in Lab Book v5, which was in fact correct.

These failure modes suggest that empirical compilation tasks—even seemingly mechanical ones like table generation from structured data—require either stronger models or human verification of outputs.

### B.4.4 Successful Sonnet Applications

Sonnet performed reliably on:
- Reference compilation from structured logs
- Section assembly (copying sections, adjusting heading levels)
- Final verification with explicit checklists and constrained scope (two documents only)

The pattern suggests that Sonnet succeeds when tasks are genuinely mechanical with no judgment required, and fails when tasks require attention to completeness or accuracy across multiple potential instances.

---

## B.5 Data Availability

### B.5.1 Conversation Transcripts

Complete transcripts of all 45 AI conversations are preserved in the project repository (00_conversations_full/). 

**Writing phase transcripts (December 23–26, 2025):**

| Transcript | Purpose |
|------------|---------|
| Conversation_Transcript_Claude_2025-12-23-Section_1_writing_specifications | Section 1 drafting |
| Conversation_Transcript_Claude_2025-12-25_Writing_section_2_with_lab_data | Section 2 drafting |
| Conversation_Transcript_Claude_2025-12-25_Writing_section_3_with_pattern_application | Section 3 drafting |
| Conversation_Transcript_Claude_2025-12-25_Epistemic_Constitutionalism_Section_4 | Section 4 drafting |
| Conversation_Transcript_Claude_2025-12-25_Epistemic_Constitutionalism_Section_5 | Section 5 drafting |
| Conversation_Transcript_Claude_2025-12-25_Epistemic_Constitutionalism_Section_6 | Section 6 drafting |
| Conversation_Transcript_Claude_2025-12-25-26_Epistemic_Constitutionalism_Section_7 | Section 7 drafting |
| Conversation_Transcript_Claude_2025-12-26_Epistemic_Constitutionalism_Section_8 | Section 8 drafting |
| Conversation_Transcript_Claude_2025-12-26_Epistemic_Constitutionalism_Conclusion | Section 9 drafting |
| Conversation_Transcript_Claude_2025-12-26_Lab_Book_V5_materials_audit_for_Appendix_A | Appendix A scoping |
| Conversation_Transcript_Claude_2025-12-26_Extended_methodology_for_source_attribution_bias_study | Appendix A draft 1 (failed) |
| Conversation_Transcript_Claude_2025-12-26_Verifying_section_2_data_against_lab_book | Section 2 data verification |
| Conversation_Transcript_ChatGPT_2025-12-26_Model_Evaluation_Discrepancy | Lab Book v4→v5 count resolution |
| Conversation_Transcript_Claude_2025-12-26_Executive_plan_for_constitutiona_AI_paper_writing | Executive process oversight |
| Conversation_Transcript_Claude_2025-12-26_AI_assisted_paper_writing_documentation_and_transparency | Appendix B drafting |

**Study development phase transcripts (December 5–18, 2025):** An additional 28 transcripts document the empirical research phase. These are preserved and available for review but fall outside the scope of this appendix's documentation.

### B.5.2 Epistemic Traces

Twenty-five Epistemic Traces document decision points throughout the research and writing process (01_epistemic_traces/). Each trace corresponds to a source conversation, with one exception noted below.

**Traces that informed writing content:**
- EpistemicTrace_008, 014: Protocol development documentation from Study 2 pilots. Referenced in Section 2's acknowledgment of protocol iteration (MOD-014).
- EpistemicTrace_020: Resolution of model count discrepancy between Lab Book versions. Established Lab Book v5 as authoritative.

**Study development phase (20 traces):**
- EpistemicTrace_001–019 + 014b: Research phase documentation (study design evolution, methodology decisions, conceptual development)
- Exception: EpistemicTrace_018 (LLM paper detection) is preserved, but its source conversation is withheld as it contains personal remarks irrelevant to this paper.

**Post-writing, pre-v1 (3 traces):**
- EpistemicTrace_021 (Jan 7, 2026): Epistemic standing examples for manual review
- EpistemicTrace_022 (Jan 15, 2026): Swiss update coherence check
- EpistemicTrace_023 (Jan 15, 2026): Germani & Spitale reframing analysis

**Post-v1 (1 trace):**
- EpistemicTrace_024 (Jan 23, 2026): LLM Writing Check methodology

Additionally available:
- Section Guidance documents with associated Prompt Development Logs (05_section_guidance/, 08_prompt_development_logs/)
- Verification reports documenting data accuracy checks (09_notes/)

### B.5.3 Source Data Repository

The empirical data underlying Section 2 and Appendix A is available at:

**Repository:** GitHub MicheleLoi/source-attribution-bias-data

Contents:
- 21 .eval files (complete evaluation data)
- README with data structure documentation
- All materials necessary to verify reported findings

---

## B.6 Summary

This appendix has documented the paper writing process (December 23–26, 2025), distinct from the study development phase that preceded it. The paper was written through a structured collaboration between human direction and AI text generation. The human author maintained control through: (a) the Complete Prompt specifying argument architecture, (b) the executive AI conversation managing process decisions, and (c) mid-course Section Guidance when argument evolution required departures from initial specifications. AI models generated text within these constraints, with Opus handling philosophical and data-sensitive sections and Sonnet handling mechanical tasks.

The process revealed that weaker models pose hallucination risks even for seemingly mechanical tasks like data compilation, suggesting that transparent AI-assisted writing requires either consistent use of stronger models for empirical content or systematic human verification of AI-generated data.

All writing-phase artifacts are documented above. Study development materials (28 conversation transcripts, 20 epistemic traces including 014b) are preserved and available for review, with one exception: the source conversation for EpistemicTrace_018 is withheld as it contains personal remarks irrelevant to this paper. This comprehensive availability of process documentation is consistent with the paper's argument that epistemic transparency—knowing how claims were produced—is essential to warranted trust in AI-mediated information.

---

## B.7 Swiss Replication Update (January 15–16, 2026)

This section documents an update to the paper conducted on January 15–16, 2026, adding Swiss replication evidence and reframing prior work.

### B.7.1 Update Scope

The update integrated results from a Swiss replication study and reframed the discussion of prior work:

**Swiss replication additions:**
- Section 1 (Introduction): Brief summary of Swiss findings
- Section 2 (The Finding): New subsection with Swiss replication details
- Appendix A: New tables documenting Swiss evaluations
- Appendix B: This process addendum

**Germani & Spitale reframing:** Section 2's treatment of Germani & Spitale (2025) was substantially rewritten to reframe their findings through the identity-stance coherence mechanism. Their study framed results as "anti-Chinese bias," but their clearest qualitative evidence reveals an identity-stance coherence penalty—models penalize arguments that deviate from expected positions for attributed identities. This reframing positions the present study as isolating the coherence mechanism that G&S's evidence suggested but did not directly test. See EpistemicTrace_023 for the analysis underlying this reframing.

### B.7.2 Workflow

The update followed a staged workflow designed for transparency and reversibility:

1. **Staging document:** Proposed additions drafted in the Swiss replication project (`proposed_paper_edits/swiss_update_proposal.md`) for review before modifying paper files.

2. **Branch isolation:** All edits made on `swiss-update` branch, preserving the original paper state on `main` until final review.

3. **Working files:** Edits applied to section-level working files (`working/*.md`) rather than the assembled `paper_full_draft.md`, following the original writing workflow.

4. **Modification logs:** New entries appended with phase separator and distinct numbering (`MOD-SW##`) to distinguish from original writing phase.

5. **Coherence check:** Before applying changes, a systematic coherence check verified internal consistency across the proposal document. This check caught an error in spoilage mechanism attribution (see EpistemicTrace_022), which was corrected before changes were applied.

### B.7.3 AI Assistance

The update was conducted with AI assistance (Claude Opus 4.5 via Claude Code CLI). The AI:
- Read source data from the Swiss replication project
- Drafted proposed additions matching the paper's existing voice
- Created the staging document for human review
- Designed and ran the coherence check that caught its own error
- Applied approved changes to working files
- Documented the process in modification logs

Human oversight included: workflow design decisions, review of all proposed additions, and final approval before changes were applied.

### B.7.4 Artifacts

| Artifact | Location | Purpose |
|----------|----------|---------|
| Integration plan | Swiss project: `proposed_paper_edits/PLAN_swiss_update_integration.md` | Workflow checklist |
| Proposal document | Swiss project: `proposed_paper_edits/swiss_update_proposal.md` | Staged additions for review |
| Swiss lab book | Swiss project: `02_notes/lab_book.md` | Source data |
| Swiss eval registry | Swiss project: `03_data/eval_registry.md` | Evaluation index |
| Coherence check trace | Paper project: `01_epistemic_traces/022_EpistemicTrace_SwissUpdate_CoherenceCheck.md` | Error detection documentation |

### B.7.5 Data Availability

Swiss replication data will be available at: [Swiss-replication-repo-URL]

Contents:
- 6 evaluation logs (3 valid, 3 spoiled)
- Lab book with detailed run notes
- Seed files adapted from German study
- Source equivalence documentation

---

## B.8 Post-v1 Revisions (January 2026)

This section documents changes made after submission of arXiv:2601.14295v1 (submitted 2026-01-16).

### B.8.1 LLM Writing Check Pass (2026-01-23)

**Scope:** Systematic editing pass to reduce signature LLM writing problems.

**Patterns addressed:**
- **Cross-section repetition:** Same ideas restated across multiple sections (e.g., suppression behavior explained five times)
- **Excessive forward-previewing:** Section closings announcing what next sections would say
- **Section openers restating conclusions:** New sections beginning by restating previous section's conclusion verbatim

**Method:** Concept inventory to flag ideas appearing in >2 sections stating (not referencing) the same thing; phrase-level search for repeated distinctive phrases; trust-the-reader test for each paragraph.

**Result:** ~800 words cut across Sections 3, 4, 5, 6, 7, and 9. Primary cuts targeted suppression behavior restatements and forward-preview sentences.

**Methodology documented in:** `01_epistemic_traces/024_EpistemicTrace_LLM_Writing_Check_Methodology.md`

**Changes detailed in:** `03_modification_logs/PaperModificationLog_Style.md` (section "LLM Writing Check Pass")

### B.8.2 Reference Insertions (2026-01-24)

Three references were inserted into the paper that were cited in body text but missing from the References section:

1. **Lloyd (2025)** — Epistemic responsibility framework for human-AI collaborations
2. **Peters (2024)** — Epistemic trust in AI-based science without full transparency
3. **Kasirzadeh & Gabriel (2023)** — AI alignment and constitutional design

The first two were documented in MOD-011 (December 2025) but never actually inserted. Kasirzadeh & Gabriel was a new addition supporting Section 4's discussion of constitutional approaches to AI alignment.

**Changes detailed in:** `03_modification_logs/ModificationLog_References.md` (MOD-012, MOD-013) and `03_modification_logs/ModificationLog_Section4.md` (MOD-010)

---

## Appendix Only References

Loi, Michele. 2025. "The Journal of Prompt-Engineered Philosophy Or: How I Started to Track AI Assistance and Stopped Worrying About Slop." arXiv:2511.08639. Preprint, arXiv, November 10. https://doi.org/10.48550/arXiv.2511.08639.