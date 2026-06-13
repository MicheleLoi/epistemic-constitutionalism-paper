---
artifact_type: code_modlog
context: MHC-W (framework infrastructure — archived)
session_id:
  - SID-20260604-090754
  - SID-20260604-102115
  - SID-20260612-204032
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

## MOD-002 — Propagate sandbox-removal to local `mhc-end` skill copy

- **target_repo:** N/A — file locale al workspace Epistemic, non al repo MHC-W
  - path: `C:\Users\loimi\switchdrive\CURRENTLY WORKING ON\AI - assisted papers\Epistemic constitutional AI\.claude\skills\mhc-end\SKILL.md`
- **commit_sha:** `4c0d0c2` (branch `review-response`, modlog-only — vedi nota git
  in fondo all'entry)
- **file_path:** `.claude/skills/mhc-end/SKILL.md`
- **change_type:** `refactor` (downstream sync)
- **rationale (the WHY):** Il refactor MOD-001 (sandbox→audit-based-recovery, commit
  `d4733b2` su MHC-W) ha aggiornato il **template** in
  `MHC-W/templates/skills/mhc-end/SKILL.md` rimuovendo la sezione `## Sandbox mode`.
  La **copia installata** in questo progetto era pre-refactor (83 righe, sezione
  sandbox presente) e descriveva un meccanismo (`_parallel/<SID>/`, directive
  `[MHC sandbox]`) ormai inesistente nell'infrastruttura. Il SessionStart hook
  l'ha segnalata come stale (`[MHC hint] 1 core skill out of sync: mhc-end`).
  Riallineata copiando il template fresco (68 righe). Nessuna perdita funzionale:
  il branch sandbox era dead code che non poteva più attivarsi (l'hook che emetteva
  `[MHC sandbox]` è stato rimosso). Razionale di coerenza: la doc che Claude legge
  in sessione ora corrisponde all'infrastruttura che esegue.
- **affects_evals:** `none` (skill documentation; nessun impatto su `.eval` files)
- **nota git:** Il file modificato vive in `.claude/skills/mhc-end/SKILL.md`,
  gitignored da `.gitignore:10` (`.claude/`) per design — `.claude/` è trattato come
  config locale rigenerabile, non source del progetto. Di conseguenza il commit
  che traccia MOD-002 contiene **solo questo modlog**, non il diff della skill.
  La canonical source del contenuto è già committata upstream: template MHC-W
  `templates/skills/mhc-end/SKILL.md` @ `d4733b2` (vedi MOD-001). MOD-002 è la
  registrazione disciplinare della propagazione locale; il diff effettivo è
  ispezionabile via `diff` contro il template MHC-W o ri-applicabile da template.

---

## MOD-003 — Fix stale SessionStart `jsonl_fingerprint` (one conversation behind)

- **target_repo:** `https://github.com/MicheleLoi/MHC-W.git` (private) · local clone
  `C:\Users\loimi\switchdrive\CURRENTLY WORKING ON\AI - assisted papers\MHC-W`
- **commit_sha:** `ac6591c` — **local only, non pushato** (`main` ahead of `origin/main`
  by 1; origin @ `d4733b2`). Co-authored Claude Fable 5.
- **file_path:**
  - `scripts/mhc_start.py` — nuova `resolve_session_fingerprint(payload, cwd)`: risolve
    il filename del transcript da `transcript_path` (autoritativo) → `session_id`
    (`<id>.jsonl`) → euristica mtime `get_latest_jsonl` (solo fallback legacy); registra
    `jsonl_fingerprint_method`; il restart stesso-transcript (resume/clear/compact) ora
    **riusa il SID**.
  - `scripts/mhc_end.py` — `finalize_session` riceve `transcript_path`: se il fingerprint
    di start diverge dal transcript realmente esportato, la entry di history registra il
    file vero e marca `jsonl_fingerprint_method: transcript_path_at_end`;
    `resolve_transcript_path` ora preferisce il fingerprint autoritativo memorizzato prima
    del re-resolve mtime.
  - `templates/skills/mhc-end/SKILL.md` — wording risoluzione transcript.
  - `tests/test_mhc_start.py`, `tests/test_mhc_end.py` — test di regressione.
- **change_type:** `fix`
- **rationale (the WHY):** `mhc_start` registrava `get_latest_jsonl()` (mtime-latest) come
  fingerprint, ma Claude Code scrive il transcript nuovo su disco solo *dopo* il primo
  messaggio — quindi a SessionStart il file più recente è quello della conversazione
  **precedente**. Risultato: un *lag-of-one* sistematico — ogni sessione fresca etichettata
  col JSONL della precedente. Diagnosticato forensicamente nel `session_history` di questo
  progetto il 2026-06-12: ogni `jsonl_fingerprint` = file reale della sessione precedente,
  provato via SHA-256 (il `jsonl_sha256` registrato a fine sessione descrive il file
  davvero esportato, che combacia con `source_jsonl`+`json_sha256` nel frontmatter
  dell'export, **non** col fingerprint di start). Es.: `-194458` registrava `6cf37e70` ma
  i byte sono in `643dcb69`; `-194547` registrava `643dcb69` ma i byte sono in `75bfad60`.
  Nessun contenuto perso (l'export a SessionEnd ha sempre ri-risolto il file vivo); solo
  l'*etichetta* di start era sbagliata, inquinando audit trail e euristiche di
  orphan-detection. Il fix risolve il fingerprint dal payload dell'hook (autoritativo) con
  l'euristica mtime degradata a fallback legacy, e si auto-guarisce a fine sessione via
  `transcript_path_at_end`. **Vittoria secondaria:** poiché ora il restart stesso-transcript
  riusa il SID, il fix elimina anche i *rollover di SID spuri a metà conversazione* (blip
  "silent rollover", es. `-194511`, `-204027`, e le molte entry "Continuazione silenziosa"
  nella topology) che il vecchio mismatch di fingerprint produceva.
- **data remediation (workspace):** 5 *cerotti* retroattivi alle entry 2026-06-12
  mislabeled in `.mhc-config.json` (`120921`, `194458`, `194511`, `194547`, `204027`) —
  `jsonl_fingerprint` originale preservato come record di ciò che l'hook scrisse,
  `jsonl_fingerprint_actual` aggiunto dove provato via SHA-256, `note` in prosa per entry.
  `audit_sessions` ri-verificato verde (19 indexed / 1 unprocessed = sessione viva). La
  sessione corrente `204032` lasciata auto-correggere al `/mhc-end` via
  `transcript_path_at_end` — dimostrazione live end-to-end del fix.
- **affects_evals:** `none` (MHC-W è tooling/framework, nessun `.eval`; gate = suite unit.
  **Verificato in questa sessione:** `pytest tests/` → **120 passed**, `py_compile` OK su
  tutti e quattro gli script).

---

## MOD-004 — Timeout subprocess di export 60s → 300s configurabile

- **target_repo:** stesso repo MHC-W di MOD-003.
- **commit_sha:** `ac6591c` — **stesso commit di MOD-003** (vedi *honest provenance*:
  bundled, non committato separatamente).
- **file_path:** `scripts/mhc_end.py` — `DEFAULT_EXPORT_TIMEOUT_SECONDS = 300`; nuove
  `_export_timeout(config)` (legge override `export.timeout_seconds`) e `_file_size_mb()`;
  sia `run_export` sia `recover_from_jsonl` passano dal `timeout=60` hard-coded al valore
  configurabile; diagnostica timeout/failure arricchita (dimensione file + elapsed).
- **change_type:** `fix`
- **rationale (the WHY):** Il timeout del subprocess di export era hard-coded a 60s. Un
  JSONL da ~20MB (una conversazione ripresa lungo 3.5 giorni) l'ha sforato due volte nel
  progetto **JPEP** il 2026-06-12 (`SID-20260612-155547`, `-171327`), lasciando quelle
  sessioni finalizzate con `exported: false`. Alzato il default a 300s e reso
  override-abile per progetto via `export.timeout_seconds`; l'entry hook di SessionEnd deve
  avere più wall-clock del timeout interno (gli installer scrivono `"timeout": 360`) così
  che quello interno scatti per primo e `finalize_session` registri comunque la sessione.
- **honest provenance:** questo cambio è **logicamente distinto** dal fix del fingerprint ma
  era già presente, **non committato, nel working tree** di MHC-W (origine JPEP) quando è
  stato fatto `ac6591c`, e ci è finito dentro. Il messaggio di `ac6591c` documenta **solo**
  il fix del fingerprint e non menziona affatto il timeout. MOD-004 esiste per far emergere
  la seconda concern che il commit ha confuso, così che l'audit trail dica la verità sul
  contenuto reale di `ac6591c` invece di ereditarne l'omissione.
- **affects_evals:** `none` (robustezza infra-export; `TestExportTimeout` la copre dentro
  la suite 120-verde).

---
*Code modlog opened 2026-06-04 (SID-20260604-090754); MOD-002 added 2026-06-04 (SID-20260604-102115); MOD-003 + MOD-004 added 2026-06-12 (SID-20260612-204032). Schema `code` per adapt.md.*
