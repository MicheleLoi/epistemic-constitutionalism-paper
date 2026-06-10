---
artifact_type: code
target_repo:
  url: https://github.com/MicheleLoi/Petri_studies
  local: C:\Users\loimi\Petri_studies\
schema_version: adapt.md v0.2 (content_schemas.code, 2026-06-03)
session_id:
  - SID-20260603-095328
  - SID-20260605-111646
  - SID-20260609-105624
---

# ModificationLog — Multipolity Replication Runner (code)

Code modlog per il repo `Petri_studies`.
Schema: `content_schemas.code` in `adapt.md` (v0.2, 2026-06-03).
Convenzione: una entry per commit sostanziale. `commit_sha` = full SHA in `target_repo`.

Spec dei campi (da `adapt.md`):
- `target_repo` — URL + path locale
- `commit_sha` — full SHA del commit documentato
- `file_path` — lista di file modificati
- `change_type` — uno di `creation` / `refactor` / `feature` / `fix` / `config` / `test` / `docs` / `decommission` / `lock`
- `rationale` — il PERCHÉ
- `affects_evals` — lista `.eval` invalidati o `none (...)`

---

## MOD-001 — Phase A skeleton bootstrap

**target_repo:**
- URL: `https://github.com/MicheleLoi/Petri_studies` (da creare/push in Phase A2 o Phase D, vedi plan §8 — visibility scelta open gating)
- Local: `C:\Users\loimi\Petri_studies\`

**commit_sha:** `63fda01` (root-commit, branch `main`)

**file_path:** 20 file (root-commit creation):
- Root: `LICENSE`, `.gitignore`, `README.md`, `METHODOLOGY.md`, `PREREGISTRATION.md`, `lab_journal.md`, `CHANGELOG.md`
- `runner/`: `README.md`, `petri_run.py`, `template.j2`, `schema.json`, `requirements.lock`, `tests/test_template_render.py`
- `configs/`: `README.md`, `_shared/judge_dimensions.yaml`, `_shared/seed_skeleton.yaml`
- `evals/`: `README.md`
- `docs/`: `architecture.md`, `adding_a_polity.md`, `source_coding_protocol.md`

**change_type:** `creation`

**rationale:**

Bootstrap del repo della replicazione UK/US/IT come da plan §5 Fase A (SID-20260603-095328, plan file `~/.claude/plans/as-we-go-pianifica-l-estensione-dello-serialized-pizza.md`). Tre obiettivi metodologici alla radice di questo commit:

1. **Single-runner architecture (D1):** un solo `petri_run.py` parameterizzato + Jinja2 template + JSON Schema. Cura la causa del disordine DE/CH (50+ script `study4_*` con seed hardcoded e versioni `_patched` / `_fixed` / `_simplified` archiviati in `~/Petri_studies/` — decommissione in Phase C). Petri compatibility verificata in plan §4.1: il runner non tocca Petri, solo wrappa con template che genera il `SEED_INSTRUCTION` testuale che `auditor_agent` si aspetta.

2. **Monorepo (D2):** un repo per UK / US / IT + legacy compat DE/CH, vs 3 mirror separati. Cross-polity diff = diff di due directory YAML. Documentazione singola, single source of truth metodologico.

3. **Disciplina lab journal + CHANGELOG + provenance (R1-R6):** lab journal append-only Markdown (D3), CHANGELOG come mirror machine-readable di questo modlog, sezione provenance in METHODOLOGY.md, JSON Schema validation a livello config.

Scope deliberatamente limitato: niente import di Petri SDK, niente chiamate API, niente `.eval` generati in Phase A. Runner stub valida YAML e renderizza `SEED_INSTRUCTION` tramite Jinja2 — sufficiente per dimostrare che il pipeline funziona (`pytest runner/tests/` → 9/9 verde in 0.30s). Phase A2 aggiungerà Petri (con version pin lock); Phase B aggiungerà `legacy_compat.py` per dimostrare byte-equivalence con uno script DE storico (`study4_*.py` da `~/Petri_studies/`).

License MIT ratificata 2026-06-03 — compatibile con repo DE/CH precedenti e con dipendenze open-source standard (anthropic SDK, inspect_ai).

**affects_evals:** `none (skeleton only)` — Phase A non genera alcun `.eval`; nessun `.eval` storico è invalidato.

**validation:** approved by user 2026-06-03 (SID-20260603-095328)

**audit trail companion** (lag di un commit, deliberato):
- Mirror in repo `CHANGELOG.md` — pending, va col prossimo commit sostanziale (MOD-003+)
- Entry in repo `lab_journal.md` (event_type: `first_commit`) — pending, va col prossimo commit sostanziale

---

## MOD-002 — Phase B legacy compat: byte-equivalent DE+CH SEED_INSTRUCTION

**target_repo:**
- URL: `https://github.com/MicheleLoi/Petri_studies` (non ancora pushato — open gating §8)
- Local: `C:\Users\loimi\Petri_studies\`

**commit_sha:** `98fc6d4` (branch `main`)

**file_path:** 9 file (5 modificati, 4 nuovi + 1 nuovo runner script):
- Modificati: `runner/petri_run.py`, `runner/template.j2`, `runner/schema.json`, `runner/tests/test_template_render.py`
- Nuovo: `runner/legacy_compat.py` (script per dimostrare byte-equivalence)
- Nuovi: `configs/de/source_coding.yaml`, `configs/de/carbon_tax.yaml`, `configs/ch/source_coding.yaml`, `configs/ch/carbon_tax.yaml`

**change_type:** `feature` (legacy compat capability + DE/CH config reconstruction)

**rationale:**

Gate B→C del plan §5: dimostrare byte-equivalence tra il nuovo pipeline (YAML config + Jinja2 template + petri_run.py) e gli script storici hardcoded di DE/CH. Senza questa prova, un revisore esterno può obiettare "come so che il nuovo SEED_INSTRUCTION non differisce silenziosamente da quello pubblicato?".

**Risultati misurati:**
- `legacy_compat.py --polity de --topic carbon_tax`: **MATCH**, 3498 char, 104 newline, contro `~/Petri_studies/study4_carbon_tax_patched.py` (2025-12-13).
- `legacy_compat.py --polity ch --topic carbon_tax`: **MATCH**, 3052 char, 90 newline, contro `~/Petri_studies/run_swiss_carbon_tax.py` (2026-01-13).
- `pytest runner/tests/`: 11/11 PASS in 0.31s.

**Differenze DE vs CH scoperte durante il lavoro** (catturate nel template come parametri):
1. CH usa due descrittori diversi: "carbon pricing" nell'Objective, "climate policy" negli Step. DE usa "climate policy" ovunque. → Aggiunti campi opzionali `objective_descriptor` + `step_descriptor` con fallback a `topic_descriptor`.
2. CH omette la sezione `## Auditor Communication Style`. DE la include. → Aggiunto flag `include_auditor_communication_style` (default `true`); CH config setta `false`.
3. CH trailing `\n`, DE trailing `\n\n` (conseguenza del flag #2). → Normalizzazione gestita in Python (`rstrip("\n")` + append condizionale), non in Jinja2 (whitespace control asimmetrico tra `{% if %}{% endif %}` rende troppo fragile farlo nel template).
4. Sources per slot differiscono (Glättli/INFRAS/Keller-Sutter/Avenir Suisse/KOF per CH; Badum/Öko-Institut/Lindner/IW Köln/Sachverständigenrat per DE). Codificati nei rispettivi `configs/<polity>/carbon_tax.yaml` + documentati in `source_coding.yaml`.

Estratto `SEED_INSTRUCTION` dai legacy script via regex (no Petri import richiesto) — `legacy_compat.py` non esegue gli script, ne legge solo il testo. Bonus: dimostra anche che il pipeline funziona senza Petri SDK installato.

Schema esteso (mantenuto `additionalProperties: false`): aggiunti `objective_descriptor`, `step_descriptor`, `include_auditor_communication_style`. Tutti opzionali. Default backward-compatible (DE-style).

**affects_evals:** `none — proof of equivalence is retroactive; no .eval files generated yet`. Quando Phase A2 aggiungerà Petri SDK e i primi .eval verranno generati, la copertura `legacy_compat` per DE/CH carbon_tax garantirà che la rimozione degli script hardcoded NON ha cambiato l'esperimento.

**validation:** approved by user (gate B→C ratificato implicitamente — MATCH visualizzato + commit eseguito)

**audit trail companion** (lag deliberato di N commit):
- Mirror MOD-001 + MOD-002 in repo `CHANGELOG.md` — pending al prossimo commit
- Entry MOD-001 (`first_commit` 63fda01) + MOD-002 (`legacy_compat_match` DE + CH) in repo `lab_journal.md` — pending al prossimo commit

**Phase B residual scope (non bloccante per gate B→C):**
Solo 1 topic DE (carbon_tax) e 1 topic CH (carbon_tax) sono byte-validati. Gli altri topic DE (ai_regulation, ai_security, nuclear_energy, schuldenbremse_*) e CH (ai_security, nuclear_energy, schuldenbremse_*) richiederebbero stesso lavoro di reconstruction. Plan §5 Fase B parla solo di "uno script DE/CH" → carbon_tax è sufficiente per il gate. Estensione futura: vedi `legacy_compat.LEGACY_SOURCES` (entries commentate).

---

## MOD-003 — Audit trail companion: lab_journal + CHANGELOG mirrors of MOD-001 + MOD-002

**target_repo:**
- URL: `https://github.com/MicheleLoi/Petri_studies` (NON ancora pushato — open gating §8)
- Local: `C:\Users\loimi\Petri_studies\`

**commit_sha:** `6139404` (branch `main`)

**file_path:** 2 file modificati in-place — `lab_journal.md`, `CHANGELOG.md` (entrambi nel root del nuovo repo)

**change_type:** `docs`

**rationale:**

Catch-up dell'audit trail in-repo (`lab_journal.md` append-only e `CHANGELOG.md` machine-readable mirror) rispetto al workspace MHC modlog autoritativo. I due commit precedenti (`63fda01` Phase A skeleton MOD-001 e `98fc6d4` Phase B legacy compat MOD-002) avevano documentato il loro MHC ref nel commit message ma non avevano ancora aggiornato il lab_journal e CHANGELOG del repo stesso — la disciplina decisa in MOD-001 prevedeva un lag deliberato di un commit per evitare il chicken-and-egg di mettere il proprio SHA in un file dello stesso commit.

Questo commit chiude il gap per MOD-001 + MOD-002. MOD-003 stesso erediterà il lag — il suo mirror nel lab_journal/CHANGELOG arriverà al prossimo commit sostanziale (probabilmente Phase A2 o Phase D).

**Contenuto lab_journal aggiunto (4 entries append-only):**
1. `[first_commit]` per `63fda01` (Phase A skeleton)
2. `[legacy_compat_match]` DE carbon_tax (MATCH 3498/104)
3. `[legacy_compat_match]` CH carbon_tax (MATCH 3052/90)
4. `[commit]` per `98fc6d4` (Phase B)

**Contenuto CHANGELOG aggiunto:**
- Entry `63fda01 — creation — 2026-06-03` (mirror di MOD-001)
- Entry `98fc6d4 — feature — 2026-06-03` (mirror di MOD-002)

**affects_evals:** `none (cosmetic — documentation mirror only)`. Nessuna semantica cambiata; solo audit trail in catch-up.

**validation:** approved by user (implicit — utente ha approvato Phase C in toto + commit eseguito)

---

## Workspace integration (Phase C non-commit actions)

Le seguenti azioni di Phase C NON sono commit nel nuovo repo, ma sono workspace-level changes e ledger entries:

### Harness ledger registrations (`_org/harness_log.jsonl`)

3 entries di tipo `register` create il 2026-06-03 ~14:52 (SID-20260603-095328):

| entry_id | type | artifact |
|---|---|---|
| `14d551fe0b3eb3bf` | `external_repo` | `C:/Users/loimi/Petri_studies` |
| `83436081f3c0ca05` | `modlog` | `03_modification_logs/ModificationLog_Code_Multipolity_runner.md` |
| `bbd8e90a3e3729a1` | `note` | `_org/external_repos.md` |

(Aggiunta successiva: registration del path archiviato `~/Petri_studies/_archive/` — vedi sezione "Decommission" sotto.)

### Decommission Petri_studies

- **mv:** `C:\Users\loimi\Petri_studies\` → `C:\Users\loimi\Petri_studies\_archive\` (2026-06-03 ~14:55).
- **`README_LEGACY.md`** scritto nell'archivio: dichiara status non autoritativo, link a `Petri_studies`, istruzioni d'uso.
- **Workspace note:** `09_notes/_decommissioned_petri_studies.md` — operations log + cosa fare/non fare.
- **Ledger entry:** aggiunta dopo la decommissione (vedi `harness_log.jsonl`).

### Cose differite a Phase A2 (NON fatte in Phase C)

- Integrazione `mhc_harness_client.placement_log()` nel runner per registrare ogni `.eval` generato — differita perché il runner non genera ancora `.eval` (no Petri imports). Va aggiunta come parte di Phase A2 quando si pinna la version Petri e si attivano gli import.

---

## MOD-004 — fix(legacy_compat): LEGACY_DIR pointing to archived path + env var override

**target_repo:**
- Local: `C:\Users\loimi\Petri_studies\`
- URL: `https://github.com/MicheleLoi/Petri_studies` (non pushato)

**commit_sha:** `9ad9480` (branch `main`)

**file_path:** `runner/legacy_compat.py` (1 file, 9+/1-)

**change_type:** `fix`

**rationale:**

Bug emerso al primo run di `legacy_compat.py` dopo la decommissione (MOD-003 / Phase C #5): il path `LEGACY_DIR` era hardcoded a `C:/Users/loimi/Petri_studies/` ma quella cartella era stata rinominata `~/Petri_studies/_archive/` poche righe prima. Errore: `ERROR: legacy script not found`.

Fix:
1. Default `LEGACY_DIR` aggiornato al path archiviato.
2. Aggiunto override via env var `LEGACY_DIR` per casi non-standard (CI, snapshot ripristinato a path diverso, future migrazioni).

Verificato post-fix: DE + CH carbon_tax `MATCH` byte-per-byte (3498/104 + 3052/90, identici a pre-decommissione).

**affects_evals:** `none (fix purely path-related; SEED_INSTRUCTION byte-identico)`.

**validation:** approved by user (implicit — bug evidente, fix banale, gate B→C ri-verificato).

**Lezione metodologica per il futuro:** quando si decommissiona un path che codice esistente legge, l'aggiornamento del codice DEVE essere nello stesso commit della decommissione (o pre-commit), non dopo. In questo caso il path appariva solo in `legacy_compat.py` (uno script di test), quindi il rischio era contenuto; ma in produzione l'asincronia avrebbe rotto qualcosa di critico. Pattern da ricordare per Phase D/E quando si rifattorizza sorgenti dei seed.

---

## MOD-005 — Phase A2: Petri SDK integration con `--execute` mode + harness logging

**target_repo:**
- Local: `C:\Users\loimi\Petri_studies\`
- URL: `https://github.com/MicheleLoi/Petri_studies` (non pushato)

**commit_sha:** `9d8fc68` (branch `main`)

**file_path:** 3 file modificati (313+/45-):
- `runner/petri_run.py` — main integration
- `runner/requirements.lock` — pinning Petri + inspect-ai + anthropic
- `runner/tests/test_template_render.py` — 3 nuovi smoke test

**change_type:** `feature`

**rationale:**

Phase A2 attiva il pipeline Petri end-to-end. Phase A scriveva uno scheletro con runner che validava e renderizzava ma NON chiamava il modello; ora il runner può davvero generare `.eval` files quando si passa `--execute`.

**Pin versions (verificate funzionanti il 2026-06-03 su Python 3.14.0):**
- `petri==0.1.0`
- `inspect-ai==0.3.150`
- `anthropic==0.75.0`

**Architettura runner aggiornata:**
1. **Deferred Petri imports** (try/except con stderr redirect) — il modulo si importa senza errori anche se Petri è assente o emette `DeprecationWarning` rumorosi (petri 0.1.0 referenzia il vecchio `inspect_ai.event.*` path). pytest continua a funzionare. `--dry-run` continua a funzionare. `_HAS_PETRI` boolean flag indica disponibilità a runtime.
2. **`--execute` mode** (new): costruisce `Task(Sample(SEED_INSTRUCTION), auditor_agent, alignment_judge)`, chiama `inspect_ai.eval()` con `model_roles`, salva `.eval` log in `evals/<polity>/<topic>/<condition>/`.
3. **Model args required when `--execute`:** `--auditor`, `--target`, `--judge` SONO richiesti (no default cabbloato). Questa è una scelta deliberata: la selezione modello è una decisione di Phase D pre-registration, non un setting di runner. Avere default qui inviterebbe a runarli per sbaglio.
4. **Harness logging integration:** ogni `.eval` generata è registrata via `mhc_harness_client.register(type=f'eval_file:{polity}:{topic}:{condition}')` nel workspace ledger `_org/harness_log.jsonl`. Path workspace risolto da env `MHC_WORKSPACE_PATH` o fallback al path canonico. Failures di registration LOGgate ma non bloccanti (il `.eval` resta on disk).
5. **Em-dash cosmetic fix:** rimosso un `—` U+2014 dal messaggio skeleton mode (rendeva `�` sulla console Windows cp1252, come il fix Unicode già fatto in legacy_compat.py).

**Test results (14/14 PASS in 5.50s):**
- Tutti i test Phase A+B continuano a passare.
- Nuovi: `test_load_judge_dimensions`, `test_petri_sdk_status_reported`, `test_petri_import_does_not_crash_module`.

**Regression confermata (post-commit):**
- `legacy_compat.py --polity de --topic carbon_tax`: MATCH 3498/104 ✓
- `legacy_compat.py --polity ch --topic carbon_tax`: MATCH 3052/90 ✓
- skeleton mode (no flags): output pulito, niente deprecation noise.

**affects_evals:** `none — nessun .eval generato in questo commit`. Quando in Phase D il primo `.eval` UK verrà generato:
1. La produzione sarà soggetta alla pre-registration tag (`preregistered-uk-v1`).
2. Ogni `.eval` finirà in `evals/uk/<topic>/<condition>/SID-*.eval` e sarà auto-registrato nel harness ledger.
3. La metadata del file (model_snapshot, runner SHA = `9d8fc68` o successivo, config hash) andrà nel `.eval` stesso (gestione di inspect_ai).

**validation:** approved by user (implicit — passo Phase A2 esplicitamente richiesto dall'utente; gate satisfied via 14/14 pytest + DE/CH legacy regression).

**Lezione metodologica:** la separazione "default model = None, required when --execute" forza il pensiero esplicito al momento di runare. È la stessa logica del pre-registration tag: i defaults invitano alla negligenza dove le scelte contano.

---

## MOD-006 — Phase D Arm B (FIX B1): `--arm` flag per 2-arm A/B design

**target_repo:**
- Local: `C:\Users\loimi\Petri_studies\`
- URL: `https://github.com/MicheleLoi/Petri_studies` (non pushato)

**commit_sha:** `e5a8e41` (branch `main`)

**file_path:** 2 file modificati (121+/33-):
- `runner/petri_run.py` — `render_seed_instruction` accetta `single_condition_id`; nuovo flag CLI `--arm`; main() dispatch a loop per-condizione quando `fresh_per_condition`
- `runner/tests/test_template_render.py` — 3 nuovi test Arm B

**change_type:** `feature`

**rationale:**

Implementazione di **FIX B1**, il next step pianificato nel `[methodology_pivot]` entry di `lab_journal.md` (2026-06-04, SID-20260604-145637). Il pivot al 2-arm A/B design è documentato nel trace `01_epistemic_traces/trace_2arm_meta_awareness_arrival_20260604.md`. FIX B1 fornisce l'**Arm B** (fresh context per condizione) che misura Δ vs Arm A (continuous context = comportamento esistente, ratings 0.68×7 osservati in T1/T1' Sonnet 4.6 carbon_tax UK).

**Semantica delle due arm:**
- **`--arm continuous`** (default): comportamento legacy invariato. Un solo `execute_petri()` con seed instruction multi-step; auditor scripta le 7 condizioni in una conversazione singola; target memoria CONTINUA fra le condizioni. Spoiler strutturali 2 (commitment cascade) + 3 (single-context memory) ON.
- **`--arm fresh_per_condition`** (FIX B1): un `execute_petri()` per condizione. Ogni iterazione lancia una `inspect_ai` session fresca → target memoria ZERO fra le condizioni. Spoiler 2+3 OFF. Output: 7 `.eval` files indipendenti, nominati `<polity>_<topic>_<condition_id>` e tutti nella per-polity flat dir.

**Design del minimo cambiamento (deliberato):**

Il template `runner/template.j2` non è toccato. La filtering avviene in Python (`render_seed_instruction(config, single_condition_id=...)` rimpiazza `config["conditions"]` con una lista a 1 elemento prima del rendering). Conseguenza: la frase del template "Execute ALL N steps in sequence" diventa "Execute ALL 1 steps in sequence" in Arm B — grammaticalmente goffa ma **load-bearing**: garantisce che fra Arm A e Arm B cambi UNA SOLA cosa (numero di condizioni nel contesto). Stesso wording, stesse Critical Instructions, stesso `include_auditor_communication_style: false`, stesso topic_descriptor, stesso argument byte. La sola manipolazione sperimentale è l'isolamento di contesto.

**Routing in `main()`:**

Costruzione `seeds: list[tuple[condition_id, seed_text]]`:
- Arm A → 1-list, condition_id default `args.condition` (o `"all"`)
- Arm B → 7-list, condition_id = ogni `c["id"]` da `config["conditions"]`

Mode dispatch loop-aware:
- `--dry-run`: stampa ogni seed con header `=== Arm B / condition: <id> ===` e separator `--- end condition ---`
- skeleton mode (no flag): report `Arm : fresh_per_condition (7 seed(s))`, total render size aggregato
- `--execute`: loop su `seeds`. Per ogni iterazione:
  - `output_dir = _eval_output_dir(polity, topic, cid)` (invariato — flat per polity)
  - `task_name = f"{polity}_{topic}_{cid}"` (encoded nel filename .eval da inspect_ai)
  - **Pre-snapshot di `*.eval`** prima del call, post-snapshot dopo → `new_files = after - before` per identificare solo i .eval di QUESTA iterazione. Necessario perché la flat dir contiene .eval di tutte le condizioni; non si può usare il `sorted(output_dir.glob("*.eval"))[-N:]` se più condizioni atterrano nella stessa dir.
  - `register_eval_in_harness(ef, polity, topic, cid)` per ciascun new_file con il cid corretto (no più "all").

**Compatibility con MOD-005 (`--execute`):** preservata. Arm A default → un solo `execute_petri()`, esattamente come MOD-005. I 3 model arg `--auditor / --target / --judge` restano required quando `--execute`. Il `--max-turns 15` default è ereditato; per Arm B, 15 è abbondante per uno step singolo ma non causa errori — l'auditor termina spontaneamente quando ha completato l'unica condizione.

**Test (17/17 PASS in 4.08s):**

3 nuovi test Arm B:
- `test_single_condition_filter_renders_one_step` — verifica che filtrando a `green_actor` il rendering NON contenga gli altri 6 label (zero cross-condition leak).
- `test_single_condition_unknown_id_raises` — ValueError con id ignoto, messaggio include lista di id disponibili.
- `test_arm_b_baseline_condition_keeps_baseline_marker` — verifica che la branch baseline-specific del template (`[INSERT THE ARGUMENT ABOVE]`) sia preservata quando filtri a `baseline`.

Tutti i 14 test pre-esistenti continuano a passare (no regressione).

**Smoke test runtime (dry-run, senza Petri):**
- `--polity uk --topic carbon_tax --dry-run` (Arm A default): output identico al pre-MOD-006, `## Test Protocol - Execute ALL 7 steps in sequence`.
- `--polity uk --topic carbon_tax --arm fresh_per_condition --dry-run`: 7 sezioni separate, ognuna con un solo Step matchante la condizione. Verificato:
  - `baseline` → solo Step 1 = "BLIND BASELINE (no source)", `[INSERT THE ARGUMENT ABOVE]`, "Record the strength_rating as your BASELINE"
  - `green_actor` → solo Step 1 = "GREEN POLITICIAN", "Caroline Lucas ... argues"
  - ... (5 altre condizioni analogamente)

**affects_evals:** `none in this commit` (cambio code-side; nessun .eval generato fino a esecuzione esplicita con `--execute`). Quando Arm B sarà eseguita su UK carbon_tax (Phase 1 del 2-arm plan: Sonnet 4.6, ~$0.50, ~3-5 min wall), produrrà 7 nuovi .eval in `evals/uk/`. Arm A reuse: l'.eval esistente `trial_sonnet46_fixA__*` (eval_id=HsMadFHs8mE3BTDFAyqqwp, 2026-06-04T17:26:21) resta il datum Arm A (NON regenerato — costo evitato come da lab_journal entry).

**Status disciplinare:** trial mode. NON pre-registrato. `preregistered-uk-v1` tag ancora deferito fino a validazione di Δ(Arm B − Arm A) e decisione su Phase 2 (Opus 4.8).

**validation:** approved by user (implicit — as-we-go mode ratificata 2026-06-05 SID-20260605-111646; FIX B1 implementation richiesta esplicita con "Run the study as previously planned").

**Provenance:**
- Trace conversazionale del pivot 2-arm: workspace `01_epistemic_traces/trace_2arm_meta_awareness_arrival_20260604.md`
- Design spec del 2-arm A/B: `Petri_studies/lab_journal.md` entry `[methodology_pivot]` 2026-06-04
- Stub UK-specific (puntatore a questa entry): `ModificationLog_Code_UK.md` MOD-004

---

## MOD-007 — Stage 0 confabulation study: `--repeat`, `--probe`, single-condition fresh, analysis tool

**target_repo:**
- Local: `C:\Users\loimi\Petri_studies\`
- URL: `https://github.com/MicheleLoi/Petri_studies` (non pushato)

**commit_sha:** `45750dc0691ceadbd2be0fb222c2e34f842fa2f5` (branch `main`)

**file_path:** 4 file runner-level (+ 2 config UK in MOD-005 sister-entry):
- `runner/petri_run.py` — `--repeat N`; single-condition fresh (`--arm fresh_per_condition --condition <id>` ora filtra a quella condizione; default `"all"` invariato); `--probe` + `render_seed_instruction(probe=...)`
- `runner/template.j2` — blocco probe `{% if include_self_report_probe %}` (frozen, simmetrico, ASCII)
- `runner/analyze_stage0.py` — nuovo tool di analisi Stage 0
- `runner/tests/test_template_render.py` — 4 nuovi test (probe render present/absent, null-first-class, no leak)

**change_type:** `feature`

**rationale:**

Prerequisiti di codice per lo **Stage 0** della confabulation study (la riformulazione del finding n=1 da "meta-awareness suppression" — disconfermata — a **confabulazione introspettiva**: dissociazione comportamento↔self-report). Design completo: workspace `01_epistemic_traces/trace_confabulation_n1_informs_paper_20260609.md`, `Petri_studies/docs/confabulation_study_protocol.md`, `PREREGISTRATION.md` blocco "Confabulation study".

Tre meccanismi nuovi, tutti a **cambiamento minimo** (la manipolazione resta isolata):
1. **`--repeat N`** — ripete il blocco N volte, ogni ripetizione produce `.eval` indipendenti. Necessario per la caratterizzazione di quantizzazione (H0b, ~40× prompt identico) e per stimare distribuzioni (positive control, probe).
2. **Single-condition fresh** — `--arm fresh_per_condition --condition <id>` ora esegue solo quella condizione (prima eseguiva sempre tutte e 7). Serve a far girare la sola `baseline` (quantizzazione + positive control) o le sole `progressive_tt`/`right_actor` (probe). Default `"all"` invariato → nessuna regressione Arm B.
3. **`--probe`** — appende al seed un blocco **frozen** di follow-up (template flag `include_self_report_probe`): (Q1) "la fonte ha influito? direzione + stima numerica, con 'nessun effetto' offerto come risposta di pari dignità" + (Q2) controfattuale "che rating avresti dato senza fonte?", output JSON forzato (`source_effect_direction`/`source_effect_magnitude`/`predicted_rating_no_source`). Il rating canonico **blind** resta `--max-turns 1` (nessun follow-up): comportamento e testimonianza in **sessioni separate** — uccide il confound dell'n=1 (i 4 canali venivano tutti da una sola conversazione). Wording ASCII per byte-stabilità della preregistrazione.

`runner/analyze_stage0.py` generalizza il one-shot `_extract_arm_b_ratings.py`: istogramma di quantizzazione + SD within-prompt (→ τ), gate H0a strong-vs-weak, report confabulazione (frazione che asserisce un effetto firmato non-nullo; rating no-source predetto vs baseline misurata).

**Verifica:** `pytest runner/tests/` → **21/21** PASS. Dry-run verificati: blocco probe renderizza, single-condition fresh, configs UK strong/weak validano.

**affects_evals:** `none (capability only)` — questo commit non genera `.eval`. Lo Stage-0 paid pilot (Sonnet 4.6) produrrà i nuovi `.eval` (quantizzazione, positive control, probe); nessun `.eval` storico è invalidato. Le 2 arm precedenti restano valide.

**validation:** approved by user (as-we-go; piano approvato `~/.claude/plans/as-we-go-lo-sequential-thompson.md`, SID-20260609-105624).

**Sister-entry:** `ModificationLog_Code_UK.md` MOD-006 (configs positive-control `carbon_tax_strong/weak`, stesso commit) + MOD-005 (commit dati Arm B `5b7581b`).

---

## MOD-008 — Stage-0 reproducibility: orchestrator + eval inspector utilities

**target_repo:**
- Local: `C:\Users\loimi\Petri_studies\`
- URL: `https://github.com/MicheleLoi/Petri_studies` (non pushato)

**commit_sha:** `f7fa7df` (orchestrator + inspector) + `e159cc0` (analyze_stage0.py UTF-8 stdout follow-up fix)

**file_path:**
- `runner/run_stage0_pilot.py` (created) — recipe riproducibile dei blocchi Stage-0
- `runner/_inspect_eval.py` (created) — utility one-shot per ispezionare la struttura interna di un `.eval`
- `runner/analyze_stage0.py` (fix, `e159cc0`) — forza stdout UTF-8 (la console Windows cp1252 falliva sui glifi del report; nessun cambiamento alla logica di analisi)
- (removed) `runner/_run_stage0.ps1` — orchestrazione PowerShell superata, mai eseguita con successo (bloccata da execution-policy; sostituita dall'orchestratore Python cross-platform)

**change_type:** `creation` (utility / reproducibility tooling)

**rationale:**

Chiude un gap di trasparenza sollevato dall'utente: il **pilot Stage-0 era stato lanciato con un comando inline** (ephemeral, vivo solo nel transcript + log del task in background). Il principio "two transparencies" del paper esige che la procedura che genera i dati sia *versionata*, non effimera. `run_stage0_pilot.py` codifica i 7 blocchi esatti (quantizzazione baseline×40; positive control strong/weak×15; confab blind progressive_tt/right_actor×10; confab probe ×10) come ricetta ri-eseguibile (`--dry` per stampare le invocazioni). La chiave API non è mai hard-coded — il caller la inietta dall'env user-scope. `_inspect_eval.py` è la utility di debug (segue la convenzione underscore-prefix one-shot di `_extract_arm_b_ratings.py`) usata per diagnosticare che `--max-turns 1` non produceva un turno target (→ uso del default `max_turns`, primo assistant come rating canonico).

**affects_evals:** `none (tooling only)`. `run_stage0_pilot.py` riproduce gli stessi `.eval` del pilot Stage-0; nessun `.eval` storico invalidato.

**Nota di provenienza onesta:** il pilot Stage-0 effettivamente eseguito in questa sessione è stato lanciato via comando inline equivalente (background task `brisljpjw`); `run_stage0_pilot.py` lo riproduce blocco-per-blocco. Per lo Stage 2 confirmatory l'orchestratore SARÀ lo strumento eseguito e SHA-pinnato al tag `preregistered-confab-v1`.

**validation:** approved by user (richiesta esplicita di salvare/documentare gli script Python, SID-20260609-105624).

---

## MOD-009 — Reliability-audit tooling + frozen datasets (published evals + Stage-0)

**target_repo:** Local `C:\Users\loimi\Petri_studies\` · URL `https://github.com/MicheleLoi/Petri_studies` (non pushato)

**commit_sha:** `871d0bc`

**file_path:** `runner/_extract_legacy.py`, `runner/_all_ratings.py`, `runner/_show_evidence.py` (created); `runner/_legacy_records.json`, `runner/_stage0_records.json` (frozen datasets)

**change_type:** `creation` (analysis tooling + datasets — one-shot, underscore convention)

**rationale:**

Strumenti dell'**audit di affidabilità** delle eval pubblicate (DE/CH) richiesto dall'utente. `_extract_legacy.py` estrae per ogni run `coherence-*` il modello target (da `header.json` `model_roles` — risolve l'ambiguità auditor/target/judge) e le coppie (fonte, rating) per condizione; `_all_ratings.py` e `_show_evidence.py` sono dumper di rating/evidenza verbatim usati per la verifica manuale. `_legacy_records.json` (26 run pubblicati) e `_stage0_records.json` (47 eval Stage-0) sono i dataset congelati su cui ha gguotato il workflow di audit a 9 agenti (wf_8f238c8d-571). Provenance completa + verdetto: workspace `09_notes/reliability_audit_published_evals_20260609.md`.

**affects_evals:** `none (read-only analysis tooling)`. Nessun `.eval` modificato o invalidato; gli strumenti leggono gli `.eval` esistenti e li classificano.

**validation:** approved by user (SID-20260609-105624 — "commit the audit").

---
