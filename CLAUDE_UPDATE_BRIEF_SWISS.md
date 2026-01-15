# Claude Code brief — Swiss replication evidence update

## Edit targets (ONLY these)
- working/intro_for_claude.md
- working/section2_for_claude.md
- working/appendixA_for_claude.md
- working/appendixB_for_claude.md

Also append short natural-language entries to:
- 03_modification_logs/ModificationLog_Section2.md
- 03_modification_logs/ModificationLog_AppendixA.md
- 03_modification_logs/ModificationLog_Appendix_B.md

Do NOT edit paper_full_draft.md (I will reintegrate manually).

## Git workflow constraints (you must follow this)
- Assume I am working on branch `swiss-update`.
- Before you start, tell me to run `git status` and confirm it says `On branch swiss-update`.
- Make your edits first. After edits, instruct me to:
  1) run `git status` (to see exactly which files changed)
  2) run `git diff` (optional quick review)
  3) stage only the intended files:
     - `git add working/intro_for_claude.md working/section2_for_claude.md working/appendixA_for_claude.md working/appendixB_for_claude.md`
     - `git add 03_modification_logs/ModificationLog_Section2.md 03_modification_logs/ModificationLog_AppendixA.md 03_modification_logs/ModificationLog_Appendix_B.md`
  4) commit with a clear message like:
     - `git commit -m "Swiss replication update in working files + modlogs"`
  5) push the branch:
     - `git push`
- Do not instruct me to merge into `main` yet. The merge happens only after I manually reintegrate into `paper_full_draft.md` and review.

## Goal
Integrate Swiss replication evidence (data-release-only) into the Intro, Section 2, Appendix A (eval details), and Appendix B (process reconstruction) while preserving the paper’s existing voice and not adding new empirical claims beyond the facts below.

## VERIFY-FIRST GATE (no edits before this)
1) Ask me to paste `git status`.
2) Confirm branch = `swiss-update`, and list any dirty files.
3) Restate in one line: targets + constraints + intended outputs; ask me to reply “OK”.
Only then proceed.

## TASK SPEC (compressed)
DISCOVER: briefly scan BOTH projects to orient:
- this repo: *Epistemic constitutional AI* (paper + modlogs)
- Swiss data repo: *Source attribution bias – Swiss replication* (data-release README/log list)
Goal of scan: locate (a) where Intro/S2/AppA/AppB live in working files + corresponding modlogs; (b) the exact Swiss `.eval` filenames + statuses + effect ranges to cite; (c) where to reference the Swiss data release (repo + commit/tag if available).

EDIT SCOPE: modify ONLY:
- working/intro_for_claude.md
- working/section2_for_claude.md
- working/appendixA_for_claude.md
- working/appendixB_for_claude.md
+ append short entries to:
- 03_modification_logs/ModificationLog_Section2.md
- 03_modification_logs/ModificationLog_AppendixA.md
- 03_modification_logs/ModificationLog_Appendix_B.md
NEVER edit `paper_full_draft.md` or anything else.

CONTENT BOUNDS: no new empirical claims beyond Swiss replication records; must distinguish VALID vs SPOILED; SPOILED = target meta-awareness → suppressed variance/flat scoring. (brief in Intro/S2; detailed in AppA). Include the carbon-tax fresh-context note only if already present in Swiss records.

OUTPUT SHAPE (minimum):
- Intro: reconcile “empirical evidence” summary with Swiss addition (2 VALID effects; 3 SPOILED; optional carbon-tax fresh-context note).
- Section 2: add concise Swiss replication paragraph + pointer to AppA.
- App A: add Swiss replication subsection + compact mapping table (5 `.eval` logs → seed/topic/status) + spoilage note + effect ranges for valid seeds.
- App B: add a short “Swiss update” process addendum: new data-release repo + AI-assisted edit workflow + artifacts (working files + modlogs).

POST-EDIT: instruct me to run exactly:
- `git status`
- (optional) `git diff`
- stage only intended files:
  - `git add working/intro_for_claude.md working/section2_for_claude.md working/appendixA_for_claude.md working/appendixB_for_claude.md`
  - `git add 03_modification_logs/ModificationLog_Section2.md 03_modification_logs/ModificationLog_AppendixA.md 03_modification_logs/ModificationLog_Appendix_B.md`
- `git commit -m "Swiss replication update in working files + modlogs"`
- `git push`
No merge to `main`.