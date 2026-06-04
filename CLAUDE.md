# NOTE: Bibliography verification (2026-04-09) — RESOLVED
#
# Primary fix applied 2026-04-22 (MOD-014): Van der Linden → Hanel et al. (2018);
# Germani, M. → Germani, F. in paper_full_draft.md, Sections_frozen/, published/Arxiv/.
# Derivative reference logs + section summaries aligned 2026-06-02 (MOD-015).
# Archived trail: 03_modification_logs/ModificationLog_References.md (MOD-014, MOD-015);
# historical verification report: 07_reference_logs/bibliography_verification_20260409.md.

# Epistemic constitutional AI

This project uses **MHC-W** (Meaningful Human Control — Workbench) for documented AI-assisted work.

## How It Works

MHC-W hooks handle session infrastructure automatically (SID generation, config, export). Your job is to follow the five rules in MHC-W's `CLAUDE.md`.

At session start, the SessionStart hook prints a `[MHC-W startup]` directive into your context with a numbered checklist. **Follow it step by step** — step 1 is to read MHC-W's `CLAUDE.md` (the path is in the directive). If no directive is visible (hook failed or not installed), read MHC-W's `CLAUDE.md` manually: find `mhc_w_path` in `.mhc-config.json`, or use the sibling `../MHC-W/` convention.

**Read `adapt.md`** — it is this project's capture authority and declares the project-specific `content_schemas` the capture skills use.

## Architecture — hybrid MHC-W + MHC-C

- **Infrastructure → MHC-W:** the hooks in `.claude/settings.local.json` handle session, SID, compaction, worktree-block, and the automatic export of conversations to `00_conversations_full/exported/`. Do not remove them.
- **Capture → MHC-C:** create artifacts with the prefixed plugin skills, which read `adapt.md`'s `content_schemas`:
  - `/mhc-c:mhc-trace`, `/mhc-c:mhc-note`, `/mhc-c:mhc-modlog`, `/mhc-c:mhc-pdl`, `/mhc-c:mhc-output`, `/mhc-c:mhc-status`
  - `/mhc-place` — guided placement for artifacts without a canonical type.
  - `/mhc-reconcile` — delta from last state registration + harness cross-check (drift detection). Harness-aware via `mhc_harness_client.py`; degrades to filesystem-only if absent.
- **MHC-W-only utilities:** `/mhc-end` (session wrap-up), `/mhc-reconstruct` (build artifacts retrospectively from old conversations or source material).

Note: the unprefixed capture commands (`/mhc-trace`, …) were removed in favour of the `mhc-c:` versions. Use the prefixed names.

---

*MHC-W v5.0 — hybrid with MHC-C capture skills (adapt.md authority)*
