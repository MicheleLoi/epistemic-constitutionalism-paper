---
artifact_type: note
note_id: NOTE_sessione_mhc_ibrida_20260602
title: Sessione 2026-06-02 — riparazione git + architettura MHC ibrida
project: Epistemic constitutional AI
created: 2026-06-02
session_id: SID-20260602-134807
inputs: []
validated: 2026-06-02
validation: approved
---

# NOTE — Sessione 2026-06-02 — architettura MHC ibrida

## Topic

Riepilogo del ragionamento e delle decisioni della sessione SID-20260602-134807. L'**esito** sta nel `decision_log`; questa nota cattura il **percorso** (parte umana + parte AI) che ci ha portati lì.

## Content

**1. Riparazione git.** Indice `.git/index` corrotto + 3 lock a 0 byte. Rimossi i lock, indice ricostruito da HEAD (`git reset`), HEAD confermato `f0aed8f`, working tree integro. Diagnosi prima dell'intervento (Fides).

**2. Sganciamento conversazioni.** `00_conversations_full/` tolto dal tracking (commit `8795b5d` su review-response, locale) e portato su `main` via cherry-pick (`4a8ea3e`, pushato). Principio fissato: i transcript restano locali; i derivati ne tengono solo **metadati/pointer**, mai copia.

**3. Onboarding MHC-W Case C.** CLAUDE.md legacy v3.32 → v5 (NOTICE bibliografia reinserito), config con blocco onboarding + `mhc_w_path`, 8 skill MHC-W installate.

**4. Architettura ibrida MHC-W + MHC-C.** Scelta deliberata: infrastruttura MHC-W (hook/export) + cattura MHC-C (`mhc-c:`). Snodo chiave: l'onboarding MHC-C precedente era stato *generato e parcheggiato in `.adapt-migration-backup/mhc-c-layer/`, mai installato* — per questo nessun adattamento era attivo. Scoperto inoltre che gli schemi MHC-C non si *derivano* dallo storico per design (il design vieta di inferire la forma dai file esistenti). Soluzione coerente: derivazione **evidence-informed + ratifica umana**. Schemi `content_schemas` su misura (trace/modlog/pdl) derivati da `01_epistemic_traces`/`03_modification_logs`/`08_prompt_development_logs` e ratificati. `adapt.md` scritto, `project_name` aggiunto, routing CLAUDE.md su `mhc-c:`, 5 doppioni skill rimossi, `mhc-place` tenuta.

**5. Governance e harness.** Conceduta l'obiezione: gli hook deterministici di MHC-W danno **indipendenza di provenienza** (transcript macchina-generati ≠ artefatti agente-generati), sufficiente per cogliere il drift dell'agente — non adversarial (quello resta MHC-H). Conseguenze: hook `artifacts_produced` (filesystem-derived); `decision_log` adottato (esito → autorità, separato dal ragionamento); brief dell'**adattatore `mhc-harness-client`→MHC-W** (continuità di funzione attraverso harness diverse; la funzione è continua, la garanzia *scala* con la harness).

## References

- `_org/decision_log.md` — esito ratificato (2026-06-02)
- `working/brief_adattatore_mhc_harness_client_mhc_w_20260602.md` — spec adattatore (parcheggio)
- `adapt.md` — schemi `content_schemas` su misura
- `00_conversations_full/exported/` — transcript della sessione (ground truth)
