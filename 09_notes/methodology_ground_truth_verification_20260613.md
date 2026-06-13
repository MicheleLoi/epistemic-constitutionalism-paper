---
artifact_type: note
subtype: methodology
topic: Ground-truth verification methodology for the Petri_studies lab-journal reconstruction
project: Epistemic constitutional AI
session_id: SID-20260613-002241
created: 2026-06-13
validation: approved
inputs:
  - C:/Users/loimi/Petri_studies/lab_journal.md (reader's guide + [correction], commit cd678c3)
  - C:/Users/loimi/Petri_studies/evals/uk/*.eval + evals/de/*.eval (immutable raw data)
  - C:/Users/loimi/Petri_studies/runner/{analyze_stage0,calibration_ledger,legacy_compat,petri_run}.py
  - C:/Users/loimi/Petri_studies git (tag preregistered-e1-v1 -> 5f54c8a; audit commit cd678c3)
  - verification workflow wf_c1614b25-298 (35 agents, 16 claims, primary + adversarial triangulation)
---

# Ground-truth verification methodology — Petri_studies lab-journal reconstruction

How the lab-journal reader's guide (the "reconstruction") was produced and checked, so that everything in it
is grounded in re-derivable fact. Written to the standard the session itself forced: after an unattributed
external bug report turned out to be both accurate and untraceable, and after an early over-claim of
"independent verification," the bar became **re-derive every load-bearing number from an immutable source,
and never claim more independence than the causal chain actually supports.**

## 1. Ground-truth principle

Every load-bearing number is re-derived from version-pinned, immutable artifacts — never trusted from journal
prose, a cached record, an external note, or the recorded value itself. The recorded value is a hypothesis to
be falsified. A claim is **confirmed** only when an independent re-derivation reproduces it; **partial** when
the directional finding holds but a recorded sub-statistic does not reproduce; **discrepancy** when the
recorded value is wrong as stated.

Two structural rules:
- **Strict read-only.** No artifact is mutated during verification. Scripts that would overwrite a committed
  file are run in `--no-write` / read modes, or the committed artifact is read directly; `git show <ref>:path`
  is parsed in memory, never written to disk.
- **Independent primary + adversarial triangulation.** Each claim is re-derived twice, on *different evidence
  layers*, so a single shared fault (a stale CSV, a parser bug) cannot pass both.

## 1b. Limits of independence — the discipline this session forced

"Independent verification" is only as strong as the independence is *real*. Three failure modes were hit and
must be guarded against explicitly:

- **Deterministic ≠ correct.** A version-pinned script is *reproducible*, not *right*. A buggy-but-deterministic
  extractor (`analyze_stage0.py _json_with_key`) returned the same wrong count (n=18) every run, so re-running
  the same script "confirmed" it. Only an **independent extractor / raw read** of the `.eval` data exposed the
  truth (n=19). Verification must triangulate the *extractor itself* against the raw bytes, not just re-run it.
- **Provenance of the flag.** The n=18 error was first surfaced by an **external, unattributed note pasted into
  the session**. Its authorship was searched across all local Claude transcripts and **not found** — it is
  treated as unverified, of no authority. The correction stands only because the raw `.eval` count was
  reproduced directly; the note is recorded as a pointer, not a source. Each correction below carries its flag
  provenance.
- **No circular corroboration.** When the instrument is changed in response to a flag, a later re-run of the
  *changed* instrument is **not** independent evidence that the change was needed — it shares the cause. Only
  evidence that does not depend on the flag (here, the raw multiset count) counts as corroboration.

## 2. The four evidence layers

- **L0 — `.eval` files.** Inspect-AI logs (ZIP). The authoritative rating is the target's first assistant
  message `"strength_rating": <num>`; the probe self-report is a later assistant message
  (`source_effect_direction` / `_magnitude` / `predicted_rating_no_source`). Pattern (cf. `runner/_diag_e1.py`):
  `zipfile.ZipFile(p)` → `header.json` (status, `eval.model_roles`) + `samples/*.json` (messages). The `.eval`
  `output` field is the LAST turn and must NOT be used for first-turn ratings. Most immutable layer.
- **L1 — deterministic scripts (version-pinned).** `analyze_stage0.py` (UK Stage-0: quantization, H0a gate,
  confabulation), `calibration_ledger.py` (DE E1 ledger + cost/regime), `legacy_compat.py` (byte-equivalence),
  `petri_run.py render_seed_instruction` (prompt rendering). Re-running on the `.eval` set must reproduce the
  numbers — *subject to §1b*.
- **L2 — git SHA / tags + hashes.** Commit `5f54c8a` (lock) / `cd678c3` (audit), annotated tag
  `preregistered-e1-v1`, SHA-256 of rendered seed prompts (re-rendered from `git show <ref>:config`).
- **L3 — MHC artifact cross-reference.** Workspace traces / decision-notes / modlogs / topology + Petri
  `lab_journal.md` / `PREREGISTRATION.md`. Confirms *consistency* of recording, never a primary number.

## 3. Per-claim verification matrix

16 claims, each re-derived on a primary layer and adversarially triangulated on a different layer. **12
confirmed, 2 partial (the n=18→19 correction), 1 confirmed-with-caveat (cost projection), 0 falsified.**

| Claim | Re-derived | Layers | Verdict |
|---|---|---|---|
| E1 c0 lock hash | a1899eb1/2542 (single-cond) from committed blob; moderate 48b3c100/2386 | L1+L2 | confirmed |
| E1 rating curve | weak 0.25×4; mediocre {0.45,0.45,0.52,0.55,0.62}; mod/strong/vstrong 0.72 | L2(csv)+L0 | confirmed |
| E1 H0a | strong 0.72 / weak 0.25 / +0.47 | L2+L0 | confirmed |
| E1 cost | asbilled $0.0482·505=$24.3→€22.4; uncached →€38.4 @0.92 | L2 | confirmed-with-caveat (projection) |
| E1 lock provenance | commit 5f54c8a, annotated tag, 3 files | L2×2 | confirmed |
| E1 model | sonnet-4-5-20250929; aud/jdg haiku (4/38 sonnet) | L1+L0 | confirmed |
| Confab H0a | strong 0.760 / medium 0.634(n=19) / weak 0.188 / +0.573 PASS | L1(live)+L0 | partial (gate ✓; medium n was stale) |
| Confab quantization | n=19, mean 0.6342, SD 0.0232, grid {0.62,0.65,0.68}, τ≈0.05 | L0+L1 | partial (recorded n=18 not reproducible) |
| Confab source-null | ideological 0.620 vs baseline 0.634; ≈ −0.014, < τ | L0×2 | confirmed |
| Confab confabulation | 7 UK probe evals, 6/7 "raised"; progressive_tt 4/4 | L0×2 | confirmed (refutes critic's "empty channel") |
| Confab model | sonnet-4-6 ×3 roles | L0+L3 | confirmed |
| Meta-aware 0.68-flat | T1 [0.68]×7 | L0+L3 | confirmed (spoiled measurement, by design) |
| FIX-A no-op | T1' [0.68]×7; transition phrases removed | L0+L3 | confirmed |
| Byte-compat | DE 3498/104, CH 3052/90, MD5-identical | L1×2 | confirmed (codepoints; 3503 utf-8 bytes) |
| Saturating-head consistency | 5 artifacts agree; match raw multiset | L2+L3 | confirmed |
| E1 lock consistency | hash/commit/tag/date agree across 6 sources | L2×2 | confirmed |

## 4. Reproduction (read-only; cwd `C:/Users/loimi/Petri_studies/runner` unless noted)

```
# Lock hashes from the committed blob (single-cond c0 = a1899eb1/2542; full render = f6ff425d/3680):
python -c "import sys,subprocess,yaml,hashlib; sys.path.insert(0,'C:/Users/loimi/Petri_studies/runner'); import petri_run as pr; cfg=yaml.safe_load(subprocess.run(['git','-C','C:/Users/loimi/Petri_studies','show','5f54c8a:configs/de/ai_regulation_e1.yaml'],capture_output=True,text=True,encoding='utf-8').stdout); s=pr.render_seed_instruction(cfg,single_condition_id='c0'); print(len(s),hashlib.sha256(s.encode()).hexdigest()); f=pr.render_seed_instruction(cfg); print(len(f),hashlib.sha256(f.encode()).hexdigest())"

# Confab Stage-0 gate + the corrected baseline recount (authoritative n=19):
python analyze_stage0.py --positive-control            # strong 0.760 / medium 0.634 n=19 / weak 0.188 / +0.573 PASS
python -c "import zipfile,json,glob,re,statistics; from collections import Counter; v=[]; stub=0
for p in sorted(glob.glob('../evals/uk/*uk-carbon-tax-baseline*.eval')):
 z=zipfile.ZipFile(p); sj=[n for n in z.namelist() if n.startswith('samples/') and n.endswith('.json')]
 if not sj: stub+=1; continue
 s=json.load(z.open(sj[0])); r=None
 for m in s.get('messages',[]):
  if m.get('role')=='assistant':
   c=m.get('content',''); c=' '.join(b.get('text','') for b in c if isinstance(b,dict)) if isinstance(c,list) else c
   mm=re.search(r'\"strength_rating\"\s*:\s*([0-9.]+)',c)
   if mm: r=float(mm.group(1)); break
 if r is not None: v.append(r)
print('stub',stub,'n',len(v),'mean',round(statistics.mean(v),4),'sd',round(statistics.stdev(v),4),dict(sorted(Counter(v).items())))"
# Expect: stub 1, n 19, mean 0.6342, sd 0.0232, {0.62:13,0.65:3,0.68:3}

# Temperature field is absent (so "confirmed from the .eval" is false; 1.0 is the API default):
python -c "import zipfile,glob; z=zipfile.ZipFile(sorted(glob.glob('../evals/de/*de-ai-regulation-e1-c0_*.eval'))[0]); print(sum(z.open(n).read().decode('utf-8','replace').count('temperature') for n in z.namelist() if n.endswith('.json')))"   # -> 0

# Byte-compat (live): python legacy_compat.py --polity de --topic carbon_tax  # 3498/104 MATCH
```

## 5. Corrections applied (all in Petri commit cd678c3 + this workspace pass)

1. **Confab medium baseline n=18 → n=19** (mean 0.6342, SD 0.0232; "2 nulls" → "1 stub + 1 parser-dropped").
   `analyze_stage0.py _json_with_key` flat-brace regex → brace-balanced `raw_decode`. *Flag: external unverified
   note; correction grounded in the reproduced raw count.* H0a / τ / source-null unchanged.
2. **Temperature "confirmed from the .eval" is false** → restated as API-default inference; non-determinism via
   varying prompts/prose. *Flag: verification workflow.*
3. **Lock-hash rendering path annotated** (single-cond c0 a1899eb1/2542 vs full-config f6ff425d/3680). *Flag:
   verification workflow.*
4. **Cost figures are projections** (mean × 505 × FX ≈ €22/€38), not measured. *Flag: verification workflow.*
5. **`calibration_ledger.py regime()` stale grid `{0.60,0.62,0.65,0.68}`** — dead/misleading on E1; not in the
   labbook or CSV; documented, left unmodified (separate fix). *Flag: verification workflow.*

## 6. The ghost (provenance case of record)

A detailed, technically accurate bug report on `analyze_stage0.py` (the n=18 datapoint drop) entered the session
as a pasted user message of **unknown authorship**. A full-text search of every local Claude Code transcript
(`~/.claude/projects/**`) found its distinctive prose **nowhere** except the paste and this session's own
downstream processing — no originating session. The PI confirmed not authoring it ("a true ghost… at most an
earlier review"). It is accurate and was acted on, but it has **no chain of custody**, so it is recorded as an
external, unverified input. The fix it pointed to was adopted only after the bug was *independently reproduced*
(the dropped 0.62 in `…RMiBm9…`, the 1-of-84 audit). This is the canonical instance of the §1b discipline: an
unattributed input may be correct, but it earns nothing until re-derived from immutable fact.

## 7. How the reader's guide was produced and verified

The guide is a synthesis of 16 per-claim verification records (each with an independent primary re-derivation
and an adversarial triangulation on a different layer), plus a completeness-critic pass and a git/filesystem
inventory (workflow `wf_c1614b25-298`, 35 agents). Its empirical findings re-derive cleanly; the five
corrections in §5 were applied before/at insertion. The guide cites only re-derivable values, references prior
work by date (no fragile cross-links), and flags the cost figures as projections. It is an orientation layer,
not part of the append-only event log; the immutable record remains the dated entries.
