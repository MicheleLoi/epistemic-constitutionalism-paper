# Epistemic Constitutional AI: when Source Attribution Bias isn't

This repository accompanies the paper "Epistemic Constitutional AI: when Source
Attribution Bias Isn't." It supports two distinct purposes that should not be
confused.

## 1. Scientific reproducibility (primary)

The empirical claims in the paper rest on Petri-framework evaluation runs whose
**immutable `.eval` records** are the authoritative ground truth. Each `.eval`
file contains, in self-contained form: the prompts issued, the harness code as
executed, the model identifier, every model response, and timestamps.

| Study | Authoritative `.eval` records |
|---|---|
| Section 2 + Appendix A (German source-attribution-bias study) | [MicheleLoi/source-attribution-bias-data](https://github.com/MicheleLoi/source-attribution-bias-data) — 21 `.eval` files |
| Section 2 Swiss replication (Appendix B.7) | [MicheleLoi/source-attribution-bias-swiss-replication](https://github.com/MicheleLoi/source-attribution-bias-swiss-replication) — 6 `.eval` files (3 valid, 3 spoiled) |

On the Python harness scripts under `09_notes/study2_*` and `09_notes/study4_*`: see Appendix B.5.3 of the paper.

**Forthcoming work.** A preregistered cross-polity replication (UK, US, Italy) is being developed in [MicheleLoi/source-attribution-bias-multipolity](https://github.com/MicheleLoi/source-attribution-bias-multipolity), structured for direct re-execution (per-polity configs, shared single-runner, `.eval` corpus, `PREREGISTRATION.md`, `METHODOLOGY.md`, MIT license). Findings will be reported in a follow-up paper.

## 2. AI-assistance transparency (secondary)

The rest of this repository documents the process by which the paper was written
with AI assistance — conversations, decisions, corrections, iterations. This is
secondary to (1): if a reviewer can replicate the empirical findings from the
`.eval` records above, they do not need this material to evaluate the science.
It is provided for those interested in methodology, AI-assisted writing
practice, or process-level scrutiny — and because the project takes "epistemic
transparency" as a thesis, it tries to practice it.

The paper was written December 23–26, 2025 with AI assistance (Claude Opus 4.5,
Claude Sonnet 4.5) using a transparency methodology inspired by Loi (2025,
JPEP). **Appendix B of the paper** is the canonical methodological account; the
folders below are the raw materials underlying it.

---

## Repository Structure (transparency archive)

```
.
├── 00_conversations_full/      # 43 full conversation transcripts
├── 01_epistemic_traces/        # 20 decision-point documents
├── 02_main_prompt/             # Complete Prompt (master specification)
├── 03_modification_logs/       # 13 change logs
├── 04_pattern_summaries/       # 9 pattern documents (33 patterns total)
├── 05_section_guidance/        # 2 mid-course corrections
├── 06_section_summaries/       # 8 section synopses
├── 07_reference_logs/          # 7 citation tracking documents
├── 08_prompt_development_logs/ # 3 prompt evolution documents
└── 09_notes/                   # Working files, lab books v1-v5, failed drafts
```

---


## Key Entry Points

### To understand the writing methodology
→ Read **Appendix B** in the paper (B.1–B.2)

### To see model failure modes documented
→ Read **Appendix B Section B.4** or examine:
- `09_notes/Appendix_A_Extended_Methodology_draft_1.md` (Sonnet hallucination)
- `03_modification_logs/ModificationLog_AppendixA.md` (correction process)

### To verify empirical claims
→ Cross-reference:
- `09_notes/study4_lab_book_v5.md` (authoritative data)
- GitHub: MicheleLoi/source-attribution-bias-data (.eval files)

### To see how sections evolved
→ Check the relevant Section Summary, Pattern Summary, and Modification Log for each section (folders 03, 04, 06)

### To see mid-course corrections
→ `05_section_guidance/` contains SectionGuidance_Section6 and SectionGuidance_Section7

---

## Writing-Phase Conversations (December 23–26)

| Conversation | Purpose |
|--------------|---------|
| `*Executive_plan_for_constitutional_AI_paper_writing*` | Process oversight |
| `*Section_1_writing_specifications*` | Section 1 |
| `*Writing_section_2_with_lab_data*` | Section 2 |
| `*Writing_section_3_with_pattern_application*` | Section 3 |
| `*Epistemic_Constitutionalism_Section_[4-8]*` | Sections 4–8 |
| `*Epistemic_Constitutionalism_Conclusion*` | Section 9 |
| `*Extended_methodology*` | Appendix A (failed draft) |
| `*Lab_Book_V5_materials_audit*` | Appendix A scoping |
| `*Verifying_section_2_data*` | Data verification |

An additional 28 conversations document the study development phase (December 5–18).

---

## Document Type System

See **Appendix B Section B.1.3** for full explanation. Summary:

| Type | Name | Feed-Forward? |
|------|------|---------------|
| 1 | Complete Prompt | Yes (constant) |
| 2 | Epistemic Trace | No (background) |
| 3 | Section Guidance | Yes (specific section) |
| 4 | Pattern Summary | Yes (cumulative) |
| 5 | Section Summary | Yes |
| 6 | Reference Log | Yes (running) |
| 7 | Modification Log | No (retrospective) |
| 8 | Prompt Development Log | No (retrospective) |

---

## Key Lessons (detailed in Appendix B Section B.4)

- **Opus** for philosophical writing and data compilation
- **Sonnet** for mechanical tasks only (assembly, formatting)
- Sonnet hallucinated eval IDs and inflated effect sizes when parsing failed
- Ground truth verification against .eval files caught errors that AI verification missed

---

## Citation

```bibtex
@misc{loi2025epistemic,
  author = {Loi, Michele},
  title = {Epistemic Constitutional AI: Source Attribution, Coherence, and When a Bias Isn't},
  year = {2025},
  note = {Transparency materials: https://github.com/MicheleLoi/epistemic-constitutionalism-paper}
}
```

---

## License

CC-BY 4.0 for documentation materials.

## Contact

Michele Loi  
University of Milan
m.loi@icloud.com

---

*This README drafted by Claude Opus 4.5, reviewed by author.*
