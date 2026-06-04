---
artifact_type: project_adaptation
project_name: Epistemic constitutional AI
project_nature: research_workspace
language: it
primary_output_location: working/
schema_version: 1
artifact_types:
  drafts: present
  notes: present
  traces: present
  modlogs: present
  pdl: present
  prompts: present
  conversations: present
skills:
  mhc-status: enabled
  mhc-trace: enabled
  mhc-note: enabled
  mhc-pdl: enabled
  mhc-modlog: enabled
  mhc-output: enabled
  mhc-place: enabled
  mhc-reconcile: enabled
content_schemas:
  trace:
    fields: [purpose_and_provenance, source_segment_map, reconstructed_framework, paper_and_eval_strategy, reusable_claims_and_phrasing]
  modlog:
    fields: [change_type, trigger, location, before_after, rationale, affects]
  pdl:
    fields: [issue, source_in_conversation, analysis, verification, decision, affects]
  note:
    fields: [topic, content, references]
  output:
    fields: [type, references, metadata]
  code:
    fields: [target_repo, commit_sha, file_path, change_type, rationale, affects_evals]
  onboard:
    fields: [project_name, project_nature, language]
migration_provenance:
  from_case: C
  mode: coexist-hybrid
  source_files_processed: [.mhc-config.json, 01_epistemic_traces/, 03_modification_logs/, 08_prompt_development_logs/]
  source_files_preserved: [CLAUDE.md, .claude/settings.local.json]
  source_files_archived: [.adapt-migration-backup-2026-06-02/.mhc-config.json.orig]
  source_files_discarded: []
  migration_timestamp: 2026-06-02T14:55:26
  backup_location: .adapt-migration-backup-2026-06-02/
---

# Project Adaptation — Epistemic constitutional AI

## Lingua

Lingua: Italiano (it). Le stringhe user-facing delle skill `mhc-c:` sono in italiano.

## Architettura: ibrido MHC-W + MHC-C

Questo progetto usa un **ibrido deliberato**:

- **Infrastruttura → MHC-W.** Gli hook Python (`SessionStart`/`SessionEnd`/`PreCompact`/`PreToolUse`) gestiscono sessione, SID, compattazione, blocco worktree e — soprattutto — **l'export automatico delle conversazioni** in `00_conversations_full/exported/`. `CLAUDE.md` e `.claude/settings.local.json` restano MHC-W e **non vanno toccati** da questo adattamento.
- **Cattura → MHC-C.** Gli artefatti (trace, note, modlog, pdl, output) si creano con le skill **plugin `mhc-c:`** (`/mhc-c:mhc-trace`, `/mhc-c:mhc-note`, …), filesystem-only, che leggono questo `adapt.md`. In più: `/mhc-place` (collocazione di artefatti non canonici).
- **Utility solo MHC-W:** `/mhc-end`, `/mhc-reconstruct` (di progetto, senza prefisso).

Le skill `mhc-c:` risolvono le cartelle da `.mhc-config.json` `folders.*` (vedi sotto) e gli schemi di contenuto dal blocco `content_schemas:` di questo file.

## File Locations

| File | Path |
|------|------|
| Config | `.mhc-config.json` |
| Topology | `session_topology.yaml` |
| Methodology | (vedi MHC-W `CLAUDE.md`) |

## Folder Mappings (convenzione numerata esistente — preservata)

| Tipo artefatto | Cartella |
|---------------|----------|
| Notes | `09_notes/` |
| Traces | `01_epistemic_traces/` |
| Modification logs | `03_modification_logs/` |
| PDLs | `08_prompt_development_logs/` |
| Prompts | `02_main_prompt/` |
| Drafts (working) | `working/` |
| Conversations | `00_conversations_full/` |

Cartelle aggiuntive del progetto (archivio di trasparenza, non gestite dalle skill ma preservate): `04_pattern_summaries/`, `05_section_guidance/`, `06_section_summaries/`, `07_reference_logs/`, `Sections_frozen/`, `published/`. Output primario del progetto: il paper (`paper_full_draft.md` alla radice; sezioni assemblate manualmente).

## Content schemas — su misura per questo progetto

Il blocco `content_schemas:` nel frontmatter **non** usa i default MHC-C: è stato derivato dall'evidenza degli artefatti esistenti del progetto (tracce in `01_epistemic_traces/`, modlog in `03_modification_logs/`, PDL in `08_prompt_development_logs/`) e ratificato dall'autore il 2026-06-02. Razionale per tipo:

- **`trace`** — le tracce del progetto sono *"Type 2 Epistemic Trace / influence document"*: distillano una conversazione-sorgente in un framework riusabile. Campi: `purpose_and_provenance` (dialogo-sorgente, tipo di traccia, usi previsti), `source_segment_map` (mappa dei segmenti load-bearing della sorgente), `reconstructed_framework` (ricostruzione coerente), `paper_and_eval_strategy` (strategia paper/eval), `reusable_claims_and_phrasing` (claims e frasi pronte al riuso). Evidenza: `01_epistemic_traces/001_…`, `004_…`.
- **`modlog`** — voci `MOD-NNN` per modifica. Campi: `change_type` (Creation/Content addition/Style correction/…), `trigger` (cosa l'ha richiesta), `location`, `before_after` (testo originale → revisionato), `rationale`, `affects`. Evidenza: `03_modification_logs/ModificationLog_Section1.md`.
- **`pdl`** — voci `PDL-NNN` di decisione. Campi: `issue`, `source_in_conversation` (citazione dalla conversazione), `analysis`, `verification`, `decision`, `affects`. Evidenza: `08_prompt_development_logs/PromptDevelopmentLog_Section6.md`.
- **`note`** / **`output`** — lasciati ai **default** MHC-C: le note del progetto sono eterogenee, irrigidirle in uno schema sarebbe controproducente (Ockham).
- **`code`** — modlog code-aware introdotto 2026-06-03 (SID-20260603-095328) per la replicazione multipolity (vedi piano `~/.claude/plans/as-we-go-pianifica-l-estensione-dello-serialized-pizza.md` §4bis). Campi:
  - **`target_repo`** — URL del repo + path locale del clone (es. `https://github.com/MicheleLoi/source-attribution-bias-multipolity` + `C:\Users\loimi\source-attribution-bias-multipolity\`).
  - **`commit_sha`** — SHA del commit documentato.
  - **`file_path`** — file modificato (lista se multipli).
  - **`change_type`** — uno di: `creation` / `refactor` / `feature` / `fix` / `config` / `test` / `docs` / `decommission` / `lock`.
  - **`rationale`** — il PERCHÉ. Cuore della disciplina MHC.
  - **`affects_evals`** — lista di `.eval` files la cui reproducibility dipende da questa modifica; `none (skeleton only)` per i primi commit pre-eval, `none (cosmetic)` per docs/style.

  Convenzione di file: le entry vivono in `03_modification_logs/ModificationLog_Code_<context>.md`, dove `<context>` = `Multipolity_runner` (cambiamenti al runner / template / schema condivisi) o `<polity>` (UK / US / IT — cambiamenti ai config per polity). Razionale: i modlog del paper coprono il *cervello intellettuale*; i modlog code coprono il *corpo tecnico*. Audit trail = ogni commit nel repo `source-attribution-bias-multipolity` ha entry MHC nel workspace che lo lega a un razionale + set di .eval impattati.

Per modificare uno schema in futuro: edita il blocco `content_schemas:` qui sopra — la skill corrispondente leggerà l'override. Per tornare al default: rimuovi il tipo dal blocco.

---
*MHC-C — Project adaptation v0.2 — ibrido MHC-W+MHC-C, schemi base ratificati 2026-06-02 (SID-20260602-134807); schema `code` aggiunto 2026-06-03 (SID-20260603-095328) per replicazione multipolity UK/US/IT*
