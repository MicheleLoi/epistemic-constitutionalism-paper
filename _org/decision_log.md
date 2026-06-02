---
artifact_type: decision_log
document: Cross-domain decisions — append-only ledger
project: Epistemic constitutional AI
created: 2026-06-02
---

# Decision Log — Epistemic constitutional AI

Memoria trasversale delle decisioni che fissano direzione o autorità del progetto.

**Cosa va qui:** l'**esito ratificato** — non il ragionamento. Il ragionamento (parte umana + parte AI) vive nelle tracce (`01_epistemic_traces/`) e nei modlog (`03_modification_logs/`); qui sta solo l'esito, in forma citabile, per generare autorità.

**Cosa NON ci va:** decisioni intra-sezione (→ modlog), esplorazione (→ tracce), operative reversibili in 5 minuti.

**Formato:** lead con decisione, poi contesto + alternative + rationale. Cronologico inverso.

**Hard rule:** append-only. Non si modifica il passato; una decisione obsoleta si **supersede** con nuova entry. È l'audit-trail del progetto: immutabile.

---

## 2026-06-02 SID-20260602-134807 — Architettura MHC ibrida + adozione del decision_log

**Status: RATIFIED** — founder chat 2026-06-02.

**Decisione:** (a) il progetto adotta un'architettura **ibrida**: infrastruttura MHC-W (hook, export conversazioni, ciclo sessione) + cattura via skill `mhc-c:` con `content_schemas` su misura derivati dallo storico e ratificati; (b) il progetto adotta un **decision_log** append-only.

**Alternative considerate:** solo-MHC-W (perde gli schemi MHC-C); migrazione completa a MHC-C (perde l'export automatico via hook); nessun decision_log (decisioni sparse).

**Rationale:** tracce e modlog mostrano il *ragionamento*; il decision_log registra solo l'*esito*, generando autorità citabile separata dal processo. L'ibrido tiene insieme export deterministico (MHC-W) e schemi di dominio (MHC-C).

**Conseguenze:** `adapt.md` con schemi custom; `project_name` nel config; CLAUDE.md instrada su `mhc-c:`; rimossi 5 doppioni skill; hook `artifacts_produced` in adozione; adattatore `mhc-harness-client`→MHC-W da valutare (brief in `working/`).

**Authority canon:** `adapt.md`; `00_conversations_full/exported/` (transcript deterministici come ground truth); commit git di sessione.
