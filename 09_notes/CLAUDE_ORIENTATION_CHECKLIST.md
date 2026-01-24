---
date: 2026-01-24
purpose: Quick orientation for Claude sessions
---

# Claude Orientation Checklist

Before exploring blindly, check these in order:

## 1. Git (authoritative timeline)
```bash
git log --oneline -20
git log --format="%h %ad %s" --date=short -30
```

## 2. Briefs (operational task specs)
```bash
ls *BRIEF*.md
ls *PLAN*.md
```

## 3. Notes (operational documentation)
- `09_notes/` contains working materials, lab books, integration docs
- `09_notes/swiss_replication/` has Swiss update workflow
- Check for subdirectories with `integration_docs/` or `source_data/`

## 4. Modification logs (what changed)
- `03_modification_logs/PaperModificationLog_*.md` for paper-level changes
- `03_modification_logs/ModificationLog_Section*.md` for section changes
- Look for phase headers (e.g., "Swiss Replication Update — January 2026")

## 5. README (navigation, but may be stale)
- Check counts against actual folder contents
- Cross-reference with git for current state
