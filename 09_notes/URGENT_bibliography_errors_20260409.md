# [RESOLVED 2026-06-02] Bibliography errors found by automated verification

> **Status:** Resolved. Primary citations corrected on 2026-04-22 (MOD-014 in `03_modification_logs/ModificationLog_References.md`) covering `paper_full_draft.md`, `Sections_frozen/references_compiled.md`, `Sections_frozen/section_1_introduction.md`, and `published/Arxiv/sources/epistemic_constitutionalism_arxiv.md`. Derivative reference logs (`07_reference_logs/ReferenceLog_Section1.md`, `_Section3.md`, `_Section7.md`) and section summary (`06_section_summaries/SectionSummary_Section1.md`) aligned 2026-06-02 (MOD-015). The seven open DOI/URL questions from the original report were addressed in the same session — see MOD-015 for the dispositions. Historical content below preserved unchanged for audit purposes.

---

**Date:** 2026-04-09 (original report)
**Source:** Automated CrossRef verification run from MHC-W prototype (SID-20260409-231226)
**Full report:** `07_reference_logs/bibliography_verification_20260409.md`

---

## Critical: Wrong authors on "The source attribution effect"

The bibliography (in `references_compiled.md`, `paper_full_draft.md`, and `section_1_introduction.md`) attributes this paper to **Van der Linden, S., Panagopoulos, C., Azevedo, F., & Jost, J. T.**

The actual authors are **Hanel, P. H. P., Wolfradt, U., Maio, G. R., & Manstead, A. S. R.**

This was confirmed by:
- CrossRef API metadata for DOI `10.1016/j.jesp.2018.07.002`
- ScienceDirect article page (PII: S0022103117304493)
- JESP Volume 79 table of contents

The title and DOI are correct. The page range should be 51–63 (not 51–59).

**Files that need fixing:**
- `paper_full_draft.md` — lines ~23, ~48 (in-text citations), ~411 (bibliography entry)
- `Sections_frozen/references_compiled.md` — line 33
- `Sections_frozen/section_1_introduction.md` — line 7

**Root cause:** Unknown — could be LLM or human. LLM path: thematic confabulation (Van der Linden et al. publish on related topics, so the model associated them with this title). Human path: misreading a table of contents — Van der Linden publishes in JESP and could appear on the same TOC page; easy to grab authors from an adjacent row while looking at the right title. Either explanation fits the evidence (correct title and DOI, wrong authors).

## Error: Germani first initial

**Germani, M.** should be **Germani, F.** (Federico). CrossRef confirms the first author is Federico Germani, not M. Same files need fixing.

## Suggested DOIs for entries without them

See full report at `07_reference_logs/bibliography_verification_20260409.md` — high-confidence DOI candidate for Mercier (2020), medium-confidence for Mercier & Sperber (2017) and Scanlon (1998).
