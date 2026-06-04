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
  mhc-onboard: enabled
content_schemas:
  trace:
    fields: [insights, conceptual_map, formulations, open_questions, context_forward, warnings]
  note:
    fields: [topic, content, references]
  modlog:
    fields: [decision, rationale, files_touched, references]
  pdl:
    fields: [goal, audience, constraints, draft_outline]
  output:
    fields: [type, references, metadata]
  onboard:
    fields: [project_name, project_nature, language]
migration_provenance:
  from_case: C
  mode: coexist-lightweight
  source_files_processed: [.mhc-config.json]
  source_files_preserved: [CLAUDE.md, .claude/settings.local.json, .claude/hooks/export-transcript.ps1]
  source_files_archived: [.adapt-migration-backup-2026-06-02/.mhc-config.json.orig]
  source_files_discarded: []
  migration_timestamp: 2026-06-02T10:22:55
  backup_location: .adapt-migration-backup-2026-06-02/
---

# Project Adaptation — Epistemic constitutional AI

## Language

Language: Italiano (it)

## Coesistenza con MHC-W

Questo progetto usava già **MHC-W** (l'harness con server e hook, operativo in Claude Code).
L'onboarding MHC-C ha aggiunto uno strato **standalone, filesystem-only**, senza toccare la
configurazione MHC-W:

- `CLAUDE.md` (routing comandi `MHC-*` + NOTICE errori bibliografia): **intatto**.
- Hook `SessionEnd` in `.claude/settings.local.json` (export automatico conversazioni): **intatti**.
- `.mhc-config.json`: aggiornato in modo **additivo** (aggiunti `current_session`, `onboarding`,
  `project_nature`; preservati `folders`, `export`, `project_map`).

Gli hook e i comandi `MHC-*` girano **solo in Claude Code**. Le skill MHC-C
(`/mhc-trace`, `/mhc-note`, `/mhc-modlog`, `/mhc-pdl`, `/mhc-output`, `/mhc-status`) sono
filesystem-only e funzionano ovunque, incluso Cowork.

## File Locations

| File | Path |
|------|------|
| Config | `.mhc-config.json` |
| Topology | `session_topology.yaml` |

## Folder Mappings (convenzione numerata esistente — preservata)

| Artifact type | Folder |
|---------------|--------|
| Notes | `09_notes/` |
| Traces | `01_epistemic_traces/` |
| Modification logs | `03_modification_logs/` |
| PDLs | `08_prompt_development_logs/` |
| Prompts | `02_main_prompt/` |
| Drafts (working) | `working/` |
| Conversations | `00_conversations_full/` |

Cartelle aggiuntive del progetto (transparency archive, non gestite dalle skill MHC-C ma
preservate): `04_pattern_summaries/`, `05_section_guidance/`, `06_section_summaries/`,
`07_reference_logs/`, `Sections_frozen/`, `published/`. Output primario del progetto: il paper
(`paper_full_draft.md` alla radice; sezioni assemblate manualmente).

## Content schemas — how to customize

Il blocco `content_schemas:` nel frontmatter dichiara, per ogni tipo di artefatto, i campi che la
skill di capture assembla. Sopra ci sono i **default di MHC-C**. Puoi **modificarli** per questo
progetto: la skill corrispondente leggerà l'override. Esempio, per rendere il `trace` orientato al
metodo di ricerca:

```yaml
content_schemas:
  trace:
    fields: [research_question, evidence, analysis, threats_to_validity, next_steps]
```

Il protocollo della skill resta universale; lo schema appartiene al dominio.

## Methodology

Vedi `methodology.md` per il riferimento al modello degli artefatti (come traces, PDL, draft,
modlog e note si relazionano).

---
*MHC-C — Project adaptation v0.1 — generated 2026-06-02*
