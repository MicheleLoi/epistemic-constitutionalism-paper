---
date: 2026-03-02
purpose: MHC-refine session starter — review-response workflow
branch: review-response (commit 464ffcc)
inputs:
  - paper_full_draft.md (tracked changes, {+inserted+} / ~~deleted~~ notation)
  - 09_notes/response_to_reviewers.md (draft response, awaiting author review)
  - 09_notes/Review/review_analysis_and_edit_tasks.md (Opus analysis, 27 points, 21 tasks)
---

# MHC-Refine Workflow: Review Response

## What this document is

A structured session starter for refining the review response and revised paper.
Use this when you want to: revise specific tracked changes, rework the response-to-reviewers
language, accept/reject individual edits, or prepare a clean final version for submission.

---

## Current state (as of 2026-03-02)

| Artifact | Location | Status |
|----------|----------|--------|
| Revised paper (tracked changes) | `paper_full_draft.md` on `review-response` branch | Draft — awaiting author review |
| Response to reviewers | `09_notes/response_to_reviewers.md` | Draft — awaiting author review |
| Analysis + task list | `09_notes/Review/review_analysis_and_edit_tasks.md` | Complete |
| Original reviews | `09_notes/Review/Automated review by refine.ink.md` | Committed |
| | `09_notes/Review/Automated review by Stanford.md` | Committed |
| Pre-revision baseline | `paper_full_draft.md` on `main` at `ef52ee2` | Preserved in git |

---

## Session start instructions (for any future Claude session)

1. Run `git checkout review-response` to get the revised paper
2. Read `09_notes/Review/review_analysis_and_edit_tasks.md` for the full analysis
3. Read `09_notes/response_to_reviewers.md` for the current response draft
4. Read `paper_full_draft.md` — tracked changes are marked `{+...+}` and `~~...~~`
5. The user will direct which of the following workflows to run:

---

## Workflow A: Author reviews tracked changes

**Goal**: User reads the tracked-changes paper and accepts or rejects individual edits.

**Process**:
- User identifies a change they want to modify or reject (by task number or text quote)
- Claude reverts or adjusts that specific `{+...+}` / `~~...~~` block
- Repeat until satisfied
- When all changes accepted: run **Workflow C** (clean version)

---

## Workflow B: Refine the response to reviewers

**Goal**: User wants to adjust the tone or content of `09_notes/response_to_reviewers.md`.

**Process**:
- User identifies a reviewer response to rework (by point number or reviewer)
- Claude revises that section of the response document
- Cross-reference with `review_analysis_and_edit_tasks.md` for the classification rationale
- Commit updated response to `review-response` branch

**Useful prompts to start this workflow**:
- "Rework the response to R1 point 4 — the boundary conditions response is too concessive"
- "Strengthen the pushback on R2 point 13 (preregistration)"
- "The preamble is too apologetic — revise it"

---

## Workflow C: Accept all changes — produce clean final version

**Goal**: Strip tracked-changes notation from `paper_full_draft.md`, producing a clean revised draft.

**Process**:
1. Claude reads `paper_full_draft.md`
2. For each `{+inserted text+}`: keep the inserted text, remove the `{+` and `+}` markers
3. For each `~~deleted text~~ {+new text+}`: remove the deleted text and markers entirely, keep only the new text (minus markers)
4. For any `~~deleted text~~` with no replacement: remove the deleted text entirely
5. Write clean version back to `paper_full_draft.md`
6. Commit: `git commit -m "Accept all tracked changes — clean revision"`
7. Merge `review-response` → `main`: `git merge review-response`
8. Update MEMORY.md: set Pending Workflow status to COMPLETE

**To start this workflow**: tell Claude "accept all tracked changes and produce clean version"

---

## Workflow D: Selective accept/reject then clean

**Goal**: Accept some changes, reject others, then produce clean version.

**Process**:
1. User specifies which task numbers to REJECT (all others accepted by default)
2. Claude reverts rejected tasks first
3. Then runs Workflow C

**To start**: "Reject tasks [N, M, ...] and accept the rest"

---

## Workflow E: Respond to a specific reviewer point with new argument

**Goal**: User wants to add a substantive point not in the current response, or strengthen a pushback.

**Process**:
1. User describes the point and their argument
2. Claude drafts the addition to `response_to_reviewers.md`
3. If the argument requires a corresponding paper edit: Claude identifies the location, drafts the edit, applies it to `paper_full_draft.md` with tracked-changes notation
4. Commit both

---

## Key reference: classification summary

| Class | Meaning | Count | Paper action |
|-------|---------|-------|--------------|
| A | Accommodate — textual revision | 12 | Change made |
| B | Hedge — qualifying language | 10 | Hedge added |
| C | Decline + push back | 2 | No edit; response argues back |
| D | Empirical study needed — decline | 3 | No edit; noted as future work |

Points classified C (decline): #13 (preregistration demand), #22 (full prompts in paper)
Points classified D (decline): #21 (pilot implementation), #23 (preregistered matrices), #24 (cross-lingual battery)

---

## Git workflow summary

```bash
# Current state
git branch          # should show: * review-response
git log --oneline   # recent commits on this branch

# To see what changed vs. main
git diff main review-response -- paper_full_draft.md

# To merge when ready
git checkout main
git merge review-response

# To abandon and start over from baseline
git checkout main
git branch -D review-response  # only if you want to discard all work
```

---

## MEMORY.md update (run at session end)

Update the Pending Workflow table in MEMORY.md to reflect which steps are complete.
Step 8 (MHC-refine workflow) is now DONE. Step 9 (merge) is pending user review.
