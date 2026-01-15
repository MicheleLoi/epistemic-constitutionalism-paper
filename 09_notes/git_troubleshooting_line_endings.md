# Git Troubleshooting: Line Ending Errors

**Date:** 2026-01-15
**Context:** Swiss replication update merge

---

## The Error

When trying to switch branches (`git checkout main`), git refused:

```
error: Your local changes to the following files would be overwritten by checkout:
    working/appendixA_for_claude.md
    working/intro_for_claude.md
    working/section2_for_claude.md
Please commit your changes or stash them before you switch branches.
```

---

## What It Means

Git detected uncommitted changes in those files. It refused to switch branches because switching would overwrite those changes — git was protecting you from losing work.

---

## Diagnosing the Problem

**Step 1:** Check what changed
```
git status
```
Shows which files have uncommitted changes.

**Step 2:** Check the actual differences
```
git diff --stat
```
In this case, result showed only line-ending warnings — no actual content changes.

---

## What Are Line Endings?

- **Unix/Mac** uses `LF` (line feed) to end lines
- **Windows** uses `CRLF` (carriage return + line feed)
- When files are edited on Windows, they may get saved with different line endings
- Git sees this as "changes" even though the content is identical

The warnings look like:
```
warning: in the working copy of 'file.md', LF will be replaced by CRLF the next time Git touches it
```

---

## The Fix

**If the changes are just line endings (no real content):**
```
git restore <filename>
```
This resets the file to match the last commit, discarding the line-ending differences.

**In this case:**
```
git restore working/appendixA_for_claude.md working/intro_for_claude.md working/section2_for_claude.md
```

Then proceed with the original command (`git checkout main`, `git merge`, etc.).

---

## When NOT to Use This Fix

If `git diff` shows actual content changes (not just line-ending warnings), don't blindly restore — you'd lose real work. Instead:
- Commit the changes first, or
- Stash them (`git stash`), switch branches, then recover (`git stash pop`)

---

## Prevention

To avoid line-ending issues on Windows, you can configure git:
```
git config --global core.autocrlf true
```
This tells git to automatically handle line-ending conversions.
