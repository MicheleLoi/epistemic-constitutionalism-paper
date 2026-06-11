# Modification Log: References

**Document Type:** Type 7 (Modification Log)
**Document Label:** ModificationLog_References
**Generated:** December 26, 2025
**Last Updated:** 2026-06-02 (MOD-018: orphan-reference resolution — Fricker added to compiled, Lackey removed from paper)
**Source Files:** ReferenceLog_Section1 through ReferenceLog_Section7

---

## MOD-001: Initial Compilation

**Date:** December 26, 2025  
**Type:** Initial draft  
**Action:** Extracted and compiled all citations from 7 Reference Log files  
**Details:**
- Extracted citations from "Running Bibliography," "Citations Used," and "Full reference" sections
- Deduplicated entries appearing in multiple sections (Bai et al., Mercier & Sperber, Scanlon, etc.)
- Alphabetized by first author surname
- Total citations compiled: 14
- Excluded Lloyd (2025) and Peters (2024) (marked "to be verified" in logs)
**Rationale:** Per task specification to compile unified references from all section logs
**Initiated by:** Task requirements

---

## MOD-002: Crawford (2021) Format Correction

**Date:** December 26, 2025  
**Type:** Format correction  
**Action:** Removed page numbers (825–848) from Crawford (2021) Ergo citation  
**Before:** `Crawford, L. (2021). Testimonial Injustice and Mutual Recognition. *Ergo*, 7(31), 825–848.`  
**After:** `Crawford, L. (2021). Testimonial Injustice and Mutual Recognition. *Ergo*, 7(31).`  
**Rationale:** Ergo is an open-access, online-only journal that uses article numbers rather than page numbers. The log incorrectly listed page numbers.
**Initiated by:** User correction

---

## MOD-003: Germani & Spitale DOI Standardization

**Date:** December 26, 2025  
**Type:** Format standardization  
**Action:** Converted Science Advances URL to standard DOI format  
**Before:** `https://www.science.org/doi/10.1126/sciadv.adz2924`  
**After:** `https://doi.org/10.1126/sciadv.adz2924`  
**Rationale:** Maintain consistent DOI format across all journal citations
**Initiated by:** Coherence audit (user-prompted)

---

## MOD-004: Van der Linden DOI Standardization

**Date:** December 26, 2025  
**Type:** Format standardization  
**Action:** Replaced ScienceDirect URL with DOI  
**Before:** `https://www.sciencedirect.com/science/article/pii/S0022103117304493`  
**After:** `https://doi.org/10.1016/j.jesp.2018.07.002`  
**Rationale:** DOI preferred over publisher URL for journal articles per APA 7th edition
**Initiated by:** User-provided DOI

---

## MOD-005: Mercier (2017) DOI Addition

**Date:** December 26, 2025  
**Type:** Format enhancement  
**Action:** Added DOI to Mercier (2017) Review of General Psychology citation  
**Before:** Citation ended after page numbers  
**After:** `https://doi.org/10.1037/gpr0000111`  
**Rationale:** Maintain consistent DOI inclusion for all journal articles
**Initiated by:** User-provided DOI

---

## MOD-006: Miller & Record (2017) DOI Addition

**Date:** December 26, 2025  
**Type:** Format enhancement  
**Action:** Added DOI to Miller & Record (2017) New Media & Society citation  
**Before:** Citation ended after page numbers  
**After:** `https://doi.org/10.1177/1461444816644805`  
**Rationale:** Maintain consistent DOI inclusion for all journal articles
**Initiated by:** User-provided DOI

---

## MOD-007: Basu (2019) DOI Addition

**Date:** December 26, 2025  
**Type:** Format enhancement  
**Action:** Added DOI to Basu (2019) Philosophical Studies citation  
**Before:** Citation ended after page numbers  
**After:** `https://doi.org/10.1007/s11098-018-1137-0`  
**Rationale:** Maintain consistent DOI inclusion for all journal articles
**Initiated by:** User-provided DOI

---

## MOD-008: Elgin (2008) DOI Addition

**Date:** December 26, 2025  
**Type:** Format enhancement  
**Action:** Added DOI to Elgin (2008) Philosophical Papers citation  
**Before:** Citation ended after page numbers  
**After:** `https://doi.org/10.1080/05568640809485227`  
**Rationale:** Maintain consistent DOI inclusion for all journal articles
**Initiated by:** User-provided DOI

---

## MOD-009: Crawford (2021) DOI Addition

**Date:** December 26, 2025  
**Type:** Format enhancement  
**Action:** Added DOI to Crawford (2021) Ergo citation  
**Before:** Citation ended after article number  
**After:** `https://doi.org/10.3998/ergo.1128`  
**Rationale:** Maintain consistent DOI inclusion for all journal articles
**Initiated by:** User-provided DOI

---

## MOD-010: Crawford (2025) DOI Addition

**Date:** December 26, 2025  
**Type:** Format enhancement  
**Action:** Added DOI to Crawford (2025) Synthese citation  
**Before:** Citation ended after article number  
**After:** `https://doi.org/10.1007/s11229-024-04855-x`  
**Rationale:** Maintain consistent DOI inclusion for all journal articles
**Initiated by:** User-provided DOI

---

## MOD-011: Lloyd (2025) and Peters (2024) Bibliographic Details Documented

**Date:** December 26, 2025
**Type:** Citation documentation
**Action:** Documented bibliographic details for two previously incomplete citations from Complete Prompt "should cite" list. (Note: Actual insertion into paper deferred; see MOD-012.)
**Citations documented:**
1. Lloyd, D. (2025). Epistemic responsibility: Toward a community standard for human–AI collaborations. *Frontiers in Artificial Intelligence*. https://doi.org/10.3389/frai.2025.1635691
2. Peters, U. (2024). Living with uncertainty: Full transparency of AI is not needed for epistemic trust in AI-based science. *Social Epistemology Review and Reply Collective*, 13(6), 8–15. https://wp.me/p1Bfg0-8Si

**Details:**
- Source for Lloyd: ChatGPT conversation transcript (Conversation_Transcript_ChatGPT_2025-12-05_epistemic_responsibility_in_AI.md, line 12-18)
- Source for Peters: ChatGPT conversation transcript + verified publication details from SERRC website screenshot
- Both citations were listed in Complete Prompt as "should cite" but lacked full bibliographic information in Reference Logs
- Original logs marked them as "to be verified"
- Full details retrieved from upstream research conversation

**Rationale:** Complete unresolved upstream specification issue. These citations were used in Section 4 body text (epistemic responsibility cluster) but couldn't be compiled without full publication details.

**Initiated by:** User direction following conversation-level check

---

## Final Format Specification

**Citation consistency achieved:**
- All journal articles include DOIs or stable URLs
- All books include publisher only (no DOI/URL)
- Web sources (Anthropic blog) include URL
- arXiv preprints use standard format without DOI
- Format follows APA 7th edition guidelines

**Total modifications:** 11
**Total citations in final version:** 16

---

## Post-arXiv:2601.14295v1 — January 2026

### MOD-012: Lloyd (2025) and Peters (2024) Inserted

**Date:** 2026-01-24
**Type:** Citation insertion
**Action:** Inserted Lloyd (2025) and Peters (2024) references into paper_full_draft.md References section
**Details:**
- MOD-011 documented bibliographic details but these were never inserted into paper_full_draft.md
- Citations were present in body text (Section 4, "The Design Question") but missing from References
- Now inserted in alphabetical order
**Source:** EpistemicTrace_017 + ChatGPT conversation transcript (Conversation_Transcript_ChatGPT_2025-12-05_epistemic_responsibility_in_AI.md)

---

### MOD-013: Kasirzadeh & Gabriel (2023) Added

**Date:** 2026-01-24
**Type:** Citation addition
**Action:** Added Kasirzadeh & Gabriel (2023) citation to References section
**Citation added:**
Kasirzadeh, A., & Gabriel, I. (2023). In conversation with artificial intelligence: Aligning language models with human values. *Philosophy & Technology*, 36(27). https://doi.org/10.1007/s13347-023-00606-x

**Rationale:** Related work on AI alignment through conversational norms. Citation added to Section 4 (see ModificationLog_Section4 MOD-010); reference entry required for completeness.

---

### MOD-014: Automated Bibliography Verification Corrections

**Date:** 2026-04-22
**Type:** Bibliographic correction
**Action:** Corrected two reference errors identified by automated verification and confirmed against online records.
**Corrections:**
1. Replaced erroneous `Van der Linden, S., Panagopoulos, C., Azevedo, F., & Jost, J. T. (2018)` attribution for "The source attribution effect" with:
   `Hanel, P. H. P., Wolfradt, U., Maio, G. R., & Manstead, A. S. R. (2018). The source attribution effect: Demonstrating pernicious disagreement between ideological groups on non-divisive aphorisms. Journal of Experimental Social Psychology, 79, 51-63. https://doi.org/10.1016/j.jesp.2018.07.002`
2. Corrected `Germani, M.` to `Germani, F.` for:
   `Germani, F., & Spitale, G. (2025). Source framing triggers systematic bias in large language models. Science Advances. https://doi.org/10.1126/sciadv.adz2924`
**Files updated:**
- `paper_full_draft.md`
- `Sections_frozen/references_compiled.md`
- `Sections_frozen/section_1_introduction.md`
- `published/Arxiv/sources/epistemic_constitutionalism_arxiv.md`
**Verification sources:** ScienceDirect record for DOI `10.1016/j.jesp.2018.07.002`; University of Bath publication record; PubMed record for DOI `10.1126/sciadv.adz2924`; CoLab/Crossref-derived record for DOI `10.1126/sciadv.adz2924`.
**Rationale:** The previous citation had the correct title and DOI for Hanel et al. (2018) but incorrect authors and page range. The Germani & Spitale entry had an incorrect first initial for Federico Germani.
**Initiated by:** User request following online verification of `09_notes/URGENT_bibliography_errors_20260409.md`.

---

### MOD-015: Closure of 2026-04-09 Bibliography Verification Report

**Date:** 2026-06-02 (SID-20260602-192019)
**Type:** Bibliographic correction + derivative alignment + DOI/URL completion
**Trigger:** User request "fissa i problemi bibliografici" referencing the standing notice in `CLAUDE.md` and the unresolved items in `09_notes/URGENT_bibliography_errors_20260409.md` and `07_reference_logs/bibliography_verification_20260409.md`. MOD-014 (2026-04-22) had corrected the primary source-of-truth files but left derivative documentation, the URGENT/CLAUDE.md banner, and the seven open DOI/URL questions unaddressed.

**Action 1 — Derivative alignment (6 files):** Propagated the Van der Linden → Hanel et al. (2018) correction and the Germani M → F initial correction to the derivative reference logs, section summary, working draft, and historical note that had been missed by MOD-014.

*Files updated:*
- `07_reference_logs/ReferenceLog_Section1.md` — replaced full citation in three locations (entry block, quality table, running bibliography) and corrected Germani initial in two locations; DOIs substituted for publisher URLs.
- `07_reference_logs/ReferenceLog_Section3.md` — corrected cumulative citation index row.
- `07_reference_logs/ReferenceLog_Section7.md` — corrected cumulative citation status row.
- `06_section_summaries/SectionSummary_Section1.md` — corrected two in-text references (literature foundation list, key concepts table).
- `09_notes/WritingTheConstitutionalAIPaper_for_AppendixB.md` — corrected historical key-decisions note.
- `working/intro_for_claude.md` — corrected the in-text reference in the superseded intro draft (kept for transparency).

**Action 2 — Notice retirement:** Replaced the "Critical: bibliography errors found" banner at the top of `CLAUDE.md` (auto-loaded into every Claude session) with a "RESOLVED" status note pointing to MOD-014 and MOD-015. Added a "[RESOLVED 2026-06-02]" banner at the top of `09_notes/URGENT_bibliography_errors_20260409.md` preserving the original content unchanged below.

**Action 3 — Online verification of the seven open DOI/URL items.** Verified against CrossRef API metadata and publisher pages.

| # | Item | Disposition | Source |
|---|------|-------------|--------|
| 1 | Mercier (2020) *Not Born Yesterday* | DOI **added**: `10.1515/9780691198842` | CrossRef + De Gruyter (Princeton UP digital edition) |
| 2 | Mercier & Sperber (2017) *The Enigma of Reason* | DOI **added**: `10.2307/j.ctv2sp3dd8` | CrossRef API confirms HUP 2017 (eISBN 9780674977860) |
| 3 | Scanlon (1998) *What We Owe to Each Other* | DOI **added**: `10.2307/j.ctv134vmrn`; year preserved as 1998 (CrossRef registry year 2000 refers to electronic edition only) | CrossRef API confirms HUP authorship |
| 4 | Popper (2020) *The Open Society and Its Enemies* | **No DOI added** — Princeton Classics 2020 edition (ISBN 9780691210841) confirmed via Princeton UP and Project MUSE; no CrossRef DOI for this edition | Princeton UP + Project MUSE (book/77643) |
| 5 | Bai et al. (2022) *Constitutional AI* | **No change** — arXiv preprint 2212.08073 confirmed; not DOI-eligible | arXiv |
| 6 | Anthropic (2025) *Petri* | **No change** — URL `alignment.anthropic.com/2025/petri/` confirmed working (200); blog post, no DOI applicable | Direct fetch |
| 7 | Peters (2024) wp.me shortlink | **Replaced** with full canonical URL `https://social-epistemology.com/2024/06/07/living-with-uncertainty-full-transparency-of-ai-is-not-needed-for-epistemic-trust-in-ai-based-science-uwe-peters/` in `Sections_frozen/references_compiled.md` (paper_full_draft.md already used the canonical URL) | wp.me follow-redirect → social-epistemology.com |

*Files updated by Action 3:* `Sections_frozen/references_compiled.md` (4 DOI/URL changes), `paper_full_draft.md` (3 DOI additions — Peters already canonical).

**Before/After for each DOI addition (Action 3 representative pattern):**
- Before: `Mercier, H. (2020). *Not Born Yesterday: The Science of Who We Trust and What We Believe*. Princeton University Press.`
- After: `Mercier, H. (2020). *Not Born Yesterday: The Science of Who We Trust and What We Believe*. Princeton University Press. https://doi.org/10.1515/9780691198842`

(Same pattern for Mercier & Sperber 2017 and Scanlon 1998.)

**Rationale:** Three converging needs.
1. *Audit-trail consistency.* The primary fix (MOD-014) corrected the paper but not its documentation derivatives. A reader auditing the project via the reference logs or section summaries would still see the wrong attribution. The trail should not contradict itself.
2. *Banner hygiene.* `CLAUDE.md` is auto-loaded by every Claude Code session. A standing "Critical" banner about a resolved issue trains future sessions to treat the resolved item as live, wastes context, and erodes the credibility of future genuine warnings.
3. *DOI completeness.* The four newly-added DOIs raise the proportion of journal/book entries with stable identifiers from 9/13 to 12/13 — the only remaining identifier-less book entry is Popper (2020), which has no CrossRef DOI to add.

**Verification sources:** CrossRef public works API (`https://api.crossref.org/works/<DOI>`) for entries 1–3 and 7; Princeton University Press catalogue + Project MUSE book record for entry 4; arXiv abstract page for entry 5; direct fetch for entries 6 and 7's redirect chain.

**Affects:** References section across the paper; derivative reference logs and section summary; project capture surface (CLAUDE.md banner). No body-text changes to the paper — all changes are in citation strings and trailing identifiers.

**Initiated by:** User request following session-start orientation surfaced the 2026-04-09 standing notice in `CLAUDE.md`.

---

---

### MOD-016: Alphabetization of References Sections

**Date:** 2026-06-02 (SID-20260602-192019)
**Type:** Format / ordering correction
**Trigger:** User request "metti in ordine" following MOD-015. Both `Sections_frozen/references_compiled.md` and the References section of `paper_full_draft.md` had accumulated alphabetical drift across prior edits — Hanel et al. (2018) had been appended at the end after MOD-014 rather than slotted into Germani↔Lloyd; Peters preceded Popper in some places; in `paper_full_draft.md` Fricker (2007) had landed between Crawford (2025) and Elgin.

**Action:** Re-sorted both references blocks alphabetically by first author surname. Single-author entries precede multi-author entries with the same first author; within a single author, sorted by year. No content changes — only reordering.

**Files updated:**
- `Sections_frozen/references_compiled.md` — full rewrite preserving content; entries reordered. New order: Anthropic → Bai → Basu → Crawford (2021) → Crawford (2025) → Elgin → Germani → Hanel → Lloyd → Mercier (2017) → Mercier (2020) → Mercier & Sperber → Miller & Record → Peters → Popper → Scanlon. (16 entries.)
- `paper_full_draft.md` — References section reordered with the same rule. Same ordering plus the three entries present only in this file: Fricker (after Elgin), Kasirzadeh & Gabriel (after Hanel), Lackey (after Kasirzadeh & Gabriel). (19 entries.)

**Rationale:** Bibliographic discipline. Drift from alphabetical order is a soft signal that the section is no longer being maintained as a coherent artifact. Recovering the invariant makes future corrections cheap (each new entry has a single correct insertion point) and makes the section trustworthy to a reader auditing for inclusion.

**Affects:** References section presentation only — no body-text changes, no citations added or removed, no DOIs or URLs altered.

**Initiated by:** User direct request following MOD-015 summary.

---

### Observation — divergence between `paper_full_draft.md` and `references_compiled.md` (surfaced 2026-06-02, not yet acted on)

While alphabetizing for MOD-016, three divergences between the two references blocks became visible. These are documented here for the user's later decision; they are not auto-fixed.

1. **Three entries appear in `paper_full_draft.md` but not in `Sections_frozen/references_compiled.md`:**
   - `Fricker, M. (2007). *Epistemic Injustice: Power and the Ethics of Knowing*. Oxford University Press.`
   - `Kasirzadeh, A., & Gabriel, I. (2022). In conversation with Artificial Intelligence: Aligning language models with human values. *arXiv preprint arXiv:2209.00731*.`
   - `Lackey, J. (2008). *Learning from Words: Testimony as a Source of Knowledge*. Oxford University Press.`

   Open question: should these be added to `references_compiled.md`, or removed from `paper_full_draft.md` if not cited?

2. **Kasirzadeh & Gabriel — year/version drift.** MOD-013 (2026-01-24) recorded adding `Kasirzadeh, A., & Gabriel, I. (2023). In conversation with artificial intelligence: Aligning language models with human values. *Philosophy & Technology*, 36(27). https://doi.org/10.1007/s13347-023-00606-x`. The current `paper_full_draft.md` still carries the earlier `(2022) arXiv:2209.00731` form. The journal version was never propagated.

3. **Lloyd (2025) — URL form drift.** `references_compiled.md` uses the DOI form `https://doi.org/10.3389/frai.2025.1635691` (per MOD-014 standardization); `paper_full_draft.md` uses the Frontiers article URL `https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1635691/full`. Both resolve to the same paper but the DOI form is the project standard.

---

---

### MOD-017: Kasirzadeh & Gabriel — journal version adoption + DOI homogenization

**Date:** 2026-06-02
**Session IDs:**
- SID-20260602-192019 (intent-continuous: this work follows directly from MOD-016 without any human-perceived session boundary)
- SID-20260602-194748 (filesystem-recorded: the JSONL fingerprint rotated at 19:47:32–48 following a user interrupt at 19:47:23 — the MHC-W hooks treated the rotation as a session boundary and started a new SID, even though the conversation continued without compaction or restart from the user's and model's point of view)

**Type:** Citation version update + URL/DOI homogenization
**Trigger:** User direction: *"Kasirzadeh, A., & Gabriel, I. (2022). arXiv:2209.00731. usa la versione in journal, già citata, omogeneizza i doi"*. Addresses divergences #2 and #3 surfaced in MOD-016. (Divergence #1 — Fricker and Lackey orphan-references — remains open.)

**Action 1 — Kasirzadeh & Gabriel: adopt the published journal version everywhere.** MOD-013 (2026-01-24) had recorded the addition of the 2023 *Philosophy & Technology* journal form, but the older 2022 arXiv preprint form was still in use in `paper_full_draft.md` (both the in-text citation in Section 4 and the bibliography entry), and the journal form was missing entirely from `Sections_frozen/references_compiled.md`.

DOI re-verified against CrossRef API (`https://api.crossref.org/works/10.1007/s13347-023-00606-x`): authors Atoosa Kasirzadeh and Iason Gabriel, *Philosophy & Technology*, volume 36, year 2023, title "In Conversation with Artificial Intelligence: Aligning language Models with Human Values".

*Files updated:*
- `paper_full_draft.md` line 209 (Section 4 body) — in-text citation `Kasirzadeh and Gabriel (2022)` → `Kasirzadeh and Gabriel (2023)`. Surrounding sentence unchanged.
- `paper_full_draft.md` line 393 (References) — full bibliography entry replaced:
  - Before: `Kasirzadeh, A., & Gabriel, I. (2022). In conversation with Artificial Intelligence: Aligning language models with human values. *arXiv preprint arXiv:2209.00731*.`
  - After: `Kasirzadeh, A., & Gabriel, I. (2023). In conversation with artificial intelligence: Aligning language models with human values. *Philosophy & Technology*, 36(27). https://doi.org/10.1007/s13347-023-00606-x`
- `Sections_frozen/references_compiled.md` — new entry inserted in alphabetical position (between Hanel and Lloyd) with the same journal form. This brings the divergence flagged in MOD-016 (#2) to closure and partially resolves MOD-016 (#1) for Kasirzadeh.

**Action 2 — DOI homogenization (Lloyd).** Replaced the Frontiers article URL with the canonical DOI in `paper_full_draft.md` so the entry now matches the form already used in `Sections_frozen/references_compiled.md`. Title case was also brought to APA 7 sentence-case as a natural side-effect of using the project-standard form (per the format specification at the end of this log).

*Files updated:*
- `paper_full_draft.md` line 397 (Lloyd entry):
  - Before: `Lloyd, D. (2025). Epistemic Responsibility: Toward a Community Standard for Human–AI Collaborations. *Frontiers in Artificial Intelligence*. https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1635691/full`
  - After: `Lloyd, D. (2025). Epistemic responsibility: Toward a community standard for human–AI collaborations. *Frontiers in Artificial Intelligence*. https://doi.org/10.3389/frai.2025.1635691`

**Verification scan:** After the edits, all journal/book entries in both files now use `https://doi.org/...` form where a DOI exists. Non-DOI URLs remaining are appropriate: Anthropic Petri (blog post, no DOI), Peters (SERRC, no DOI), Popper 2020 (Princeton Classics reprint, no CrossRef DOI), Bai et al. (arXiv preprint), Loi 2025 (arXiv DOI form already canonical).

**Rationale:**
- *Version currency.* When a preprint becomes a peer-reviewed journal article, citing the journal version is standard scholarly practice — the peer-reviewed version is the version of record, even when content is substantially the same.
- *Cross-file consistency.* `paper_full_draft.md` and `Sections_frozen/references_compiled.md` are two views of the same bibliography. They should agree on author, year, DOI, and URL form for shared entries. Persistent drift between them undermines confidence in either.
- *DOI hygiene.* The DOI is a stable identifier; publisher-side article URLs can change (Frontiers has restructured paths before). Per the format spec, DOI is preferred where it exists.

**Note on MOD-013:** MOD-013 (2026-01-24) recorded the *intent* to use the journal version but the change was not propagated to `paper_full_draft.md`. MOD-017 closes that loop. The historical record in MOD-013 is unchanged.

**Affects:** Section 4 in-text citation (one date change), References section in both bibliography files, DOI presentation. No content/argument changes.

**Initiated by:** User direct request following MOD-016 divergence surfacing.

**Remaining open from MOD-016:** Divergence #1 — Fricker (2007) and Lackey (2008) appear in `paper_full_draft.md` References but not in `Sections_frozen/references_compiled.md`. Pending decision: add to compiled (if cited in body) or remove from paper (if dead references).

---

---

### MOD-018: Orphan-Reference Resolution (Fricker / Lackey)

**Date:** 2026-06-02
**Session IDs:**
- SID-20260602-192019 (intent-continuous: this work continues the bibliography-closure arc started with MOD-015 and is the user-perceived "end" of that arc)
- SID-20260602-194748 (filesystem-recorded: same silent rollover as MOD-017; see that entry for the diagnosis)

**Type:** Bibliographic reconciliation — body↔references closure
**Trigger:** User rule, established this session: *"finché rimangono nel testo vanno in references"* — bibliography entries should exist iff the cited work is actually used in the body. Applied to the two remaining orphans flagged by MOD-016 #1 (Fricker 2007 and Lackey 2008, both present in `paper_full_draft.md` References but absent from `Sections_frozen/references_compiled.md`). User dispatched an Explore agent to verify body-text usage.

**Verification (read-only Explore agent + manual confirmation):**

- **Fricker (2007):** *Cited in body.* `paper_full_draft.md` line 329 (Section 7, "Toward a Liberal Epistemic Constitution"), in the safeguard paragraph about source-attending logic and structural marginalization: `"...reproducing precisely the epistemic injustices the constitution aims to prevent (cf. Fricker, 2007)."` The citation is integrated into the body argument, not a placeholder.
- **Lackey (2008):** *Not cited in body.* Appears only at line 395 in the References section of `paper_full_draft.md`. The planned insertion in Section 3 documented in `09_notes/Review/review_analysis_and_edit_tasks.md` (Task 8) — "This distinction draws on a substantial philosophical literature on testimony as an epistemic source (Lackey, 2008)..." — was never completed in the actual draft.

**Actions:**

1. **Fricker → added to `Sections_frozen/references_compiled.md`** in alphabetical position (between Elgin and Germani). Entry: `Fricker, M. (2007). _Epistemic Injustice: Power and the Ethics of Knowing_. Oxford University Press.` (No CrossRef DOI available for this OUP monograph; consistent with Popper 2020's DOI-less form.)

2. **Lackey → removed from `paper_full_draft.md` References section** (formerly line 395). No body-text citation existed; per the rule, the bibliography entry has no anchor.

**Before/After:**
- `Sections_frozen/references_compiled.md`: 17 entries → **18 entries**.
- `paper_full_draft.md` References: 19 entries → **18 entries**.

After MOD-018 the two files share exactly the same set of 18 entries (subject to the formatting differences of `_italic_` vs `*italic*` per their respective Markdown renderers).

**Rationale:** The body↔references invariant matters for two reasons.
1. *Reader trust.* A reader checking whether a name in the bibliography corresponds to an actual argument in the paper should always be able to find the citation; a dangling entry signals carelessness and undermines the rest of the bibliography.
2. *Replication.* Reviewers and replicators rely on the bibliography to know which sources informed the paper. Including works that were *intended* but not actually drawn upon misrepresents the evidential basis of the work.

The Lackey insertion remains a *valid editorial task* (it was planned for a reason — adding Lackey to Section 3 would strengthen the testimony-as-epistemic-source argument), but the task should be completed as a body-text edit, not papered over by leaving a bibliography entry without an anchor. If/when Section 3 is updated to include the planned Lackey citation, Lackey can be re-added to both files in the same modlog entry.

**Affects:** References sections in both bibliography files; no body-text changes.

**Initiated by:** User: *"sono nel testo? finché rimangono nel testo vanno in references, manda agent a controllare"* — and explicit rule application.

**Status after MOD-018:** All divergences surfaced in MOD-016 are now closed (#1 Fricker/Lackey: this entry; #2 Kasirzadeh year/version: MOD-017; #3 Lloyd URL form: MOD-017).

---

### MOD-019: Germani & Spitale description correction (verified) + Van der Linden→Hanel docx-body completion + arXiv v4

**Date:** 2026-06-11 (SID-20260610-145422; manual session — MHC-W hooks inactive on macOS, manual SID)
**Type:** Factual correction of a cited-study description + bibliographic body-completion + new arXiv source version
**Trigger:** User request to correct the sentence describing Germani & Spitale (2025) and deliver a corrected arXiv version. A model-set discrepancy was first surfaced during the empirical-reframe framing work (a literature sweep), then **verified against the primary source before any edit** — explicitly refusing to swap one unverified claim for another.

**Verification (primary source):** G&S read in full via the open-access arXiv full text (arXiv:2505.13488), whose abstract, model list, sample sizes (4,800 statements / 24 topics / 192,000 assessments) and DOI match the published *Science Advances* version (10.1126/sciadv.adz2924). Science.org returned HTTP 403; arXiv full text + EurekAlert/UZH/TechXplore press releases corroborate the four-model list and N. (Caveat: the typeset *Science Advances* HTML was not opened directly.)

**Correction 1 — Germani & Spitale description (three factual errors):**
- *Models:* "multiple frontier models including GPT-4 and Claude 3.5 Sonnet" → **"OpenAI o3-mini, DeepSeek Reasoner, xAI Grok 2, and Mistral"**. GPT-4 and Claude 3.5 Sonnet appear nowhere in G&S; the draft most likely conflated G&S's models with this paper's own (Claude Sonnet 4.5 + GPT-4o).
- *Effect sizes:* "-6.18% overall to -8.94% for geopolitical topics" → the −6.18% is **DeepSeek Reasoner's** dataset-wide figure (the strongest model), not a pooled "overall"; **8.94% appears nowhere** in G&S — the geopolitical figure is **24.43%** (DeepSeek, Cluster 7).
- *Minor:* "compared to neutral attribution" → "compared to a no-source baseline."

> **Before:** "They found that large language models lowered agreement scores when policy statements were attributed to "a person from China" compared to neutral attribution, with effects ranging from -6.18% overall to -8.94% for geopolitical topics across multiple frontier models including GPT-4 and Claude 3.5 Sonnet."
>
> **After:** "Germani and Spitale (2025) extended this research to AI systems, testing four models—OpenAI o3-mini, DeepSeek Reasoner, xAI Grok 2, and Mistral. They found that the models lowered agreement scores when policy statements were attributed to "a person from China" compared to a no-source baseline; the effect was strongest for DeepSeek Reasoner, whose agreement scores fell by 6.18% across the full dataset and by 24.43% on geopolitical topics."

The Taiwan 85%→0% example that follows was verified correct and left unchanged.

**Correction 2 — completion of MOD-014 in the arXiv .docx body:** MOD-014 (2026-04-22) corrected Van der Linden → Hanel et al. (2018) in the markdown/frozen sources, but its file list did **not** include the `.docx`. The v3.docx was found internally inconsistent — bibliography already carried the Hanel entry, but the body still cited "Van der Linden et al., 2018" in two places (intro in-text + the Section-1 descriptive sentence). Both body mentions were corrected to Hanel in the new v4.docx, making it consistent with the corrected markdown.

**Files updated:**
- `paper_full_draft.md` (G&S sentence; Van der Linden already correct here via MOD-014)
- `published/Arxiv/sources/epistemic_constitutionalism_arxiv.md` (G&S sentence; Van der Linden already correct here)
- `published/Arxiv/sources/epistemic_constitutional_AI_arxiv_v4.docx` — **new file**, built from v3.docx with both corrections; **v3.docx preserved unchanged**. Validated (1259 paragraphs preserved; "Hanel" now appears in-text + body + bibliography; zero residual "GPT-4 and Claude 3.5", "8.94", or "Van der Linden"). Word → PDF export for the arXiv upload to be done by the user.

**Rationale:** A paper about source-/identity-attribution error misciting its own predecessor study (wrong models, a fabricated effect size) is both a factual defect and a credibility liability. Correcting against the primary source — and refusing to substitute one unverified claim for another — is the same discipline the new empirical work demands.

**Resolution (2026-06-11):** v4 was exported to PDF and **submitted to arXiv by the user** — the public arXiv version is now **v4**, carrying this G&S correction and the Van der Linden body fix. The one remaining arXiv concern is the deeper **audit-invalidated Section-2 empirical tables**, which v4 does *not* address — those belong to the empirical reframe (see `09_notes/decision_empirical_critical_framing_20260611.md`).

**Initiated by:** User request (2026-06-11).

---

**Document Status:** Complete
**Final output:** references_compiled.md
**Total modifications:** 19
