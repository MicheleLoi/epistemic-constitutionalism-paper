---
artifact_type: code_modlog
context: MHC-W (framework infrastructure — archived)
session_id: SID-20260604-090754
validation: approved
---

# Modification Log — Code — MHC-W

Code-aware modlog (schema `code`, adapt.md) for changes to the **MHC-W** framework repo.
MHC-W is archived/superseded (current line: MHC-C + MHC-H + Chameleon) but remains the
local tooling that runs the hooks on this and other projects, so its changes are tracked.

---

## MOD-001 — Complete the sandbox → audit-based-recovery refactor

- **target_repo:** `https://github.com/MicheleLoi/MHC-W.git` (private) · local clone
  `C:\Users\loimi\switchdrive\CURRENTLY WORKING ON\AI - assisted papers\MHC-W`
- **commit_sha:** `d4733b2` (pushed to `origin/main`, fast-forward over `a196c8c`)
- **file_path:**
  - `scripts/mhc_start.py` (MAX_SESSION_HISTORY 10→500; sandbox functions already
    removed in WIP; session audit + `[MHC hint]`)
  - `scripts/mhc_end.py` (run_export 4-tuple + `run_export_only` 6-tuple consistency;
    finalize cap 500; `--recover-orphans`; SHA-256)
  - `scripts/mhc_check.py` (`audit_sessions`)
  - `scripts/extract_conversation.py` (centralized-only; per-project copy removed)
  - `tests/test_mhc_end.py`, `tests/test_jpep_simulation.py`, `tests/test_failure_modes.py`,
    `tests/test_mhc_start.py`, `tests/test_v5_new_features.py` (18 tests realigned;
    1 obsolete harvest test removed)
  - `CLAUDE.md`, `templates/skills/mhc-end/SKILL.md`, `.gitignore`,
    `templates/gitignore-default.txt` (sandbox/_parallel docs removed)
  - `README.md`, `.github/ISSUE_TEMPLATE/config.yml`, `SECURITY.md` (security references
    removed; SECURITY.md deleted)
- **change_type:** `refactor`
- **rationale (the WHY):** The WIP replaced the concurrent-session *sandbox* model
  (`_parallel/<SID>`) with *audit-based recovery* (`audit_sessions()` + `[MHC hint]` +
  `--recover-orphans` + SHA-256), but was left incomplete: 18 tests red, decisions
  unapplied. **Closed it.** Critical fix: `MAX_SESSION_HISTORY` in `mhc_start.py` was
  still `10`, which `rotate_session_history` used to re-truncate history on the next
  unclean start — re-introducing the false-orphan loop the `mhc_end.py` 500-cap was
  meant to kill. Unified both caps to 500. Tests realigned to the new contracts
  (`run_export` now a tuple, `[MHC tip]` prefix, `ended`-absent history invariant);
  the harvest tests asserted a feature that never existed (`append_harvest_to_adapt`) —
  ratified behavior is *discard MEMORY.md, do not harvest* — so they were removed/rewritten.
  Sandbox docs and security references removed per user decisions (MEMORY_BOOTSTRAP kept;
  AGENTS.md left untracked). Coherence with this project verified: refactored
  `audit_sessions` on Epistemic → `10 indexed / 0 unprocessed`.
- **affects_evals:** `none` (MHC-W is tooling/framework, no `.eval` files; gate was the
  unit suite — `pytest tests/`: **96 passed**, all four scripts `py_compile` OK)

---
*Code modlog opened 2026-06-04 (SID-20260604-090754). Schema `code` per adapt.md.*
