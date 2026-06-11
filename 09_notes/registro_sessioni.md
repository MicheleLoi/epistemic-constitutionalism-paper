---
artifact_type: note
note_id: NOTE_registro_sessioni
title: Registro sessioni MHC — Epistemic constitutional AI
project: Epistemic constitutional AI
created: 2026-06-11
session_id: SID-20260611-191657
inputs:
  - .mhc-config.json
  - session_topology.yaml
  - C:/Users/loimi/Petri_studies/lab_journal.md
validated: 2026-06-11
validation: approved
---

# Registro sessioni — Epistemic constitutional AI

> **Documento vivo.** Indice cronologico leggibile delle sessioni MHC sostanziali.
> Sorgenti canoniche (machine-readable): `session_topology.yaml` (goal/inputs/artefatti per SID)
> + `.mhc-config.json` (`session_history`, export, hash). Questo file è un **derivato umano**:
> in caso di conflitto, vincono le sorgenti canoniche.
> Sono omessi gli stub di rollover (sessioni da pochi secondi, nessun boundary semantico).
>
> **Ultimo aggiornamento:** 2026-06-11 (SID-20260611-191657).

---

## 2026-06-02 — Onboarding, architettura, bibliografia

- **`SID-20260602-134807`** — Riparazione indice git + sganciamento conversazioni (cherry-pick su `main`). Onboarding MHC-W **Case C**; architettura **ibrida MHC-W + MHC-C** con `content_schemas` su misura; adozione `decision_log`; brief adattatore `mhc_harness_client → MHC-W`. → `note_sessione_architettura_mhc_ibrida_20260602.md`
- **`SID-20260602-165225`** — Piano replicazione cross-polity **UK / US / IT** dello studio source-attribution bias; design ratificato (tre studi indipendenti, Sonnet 4.5 + Opus 4.8, topic adattati per polity); source coding lasciato aperto. → `replication_plan_uk_us_it_20260602.md`
- **`SID-20260602-192019` + `-194748`** — Chiusura della verifica bibliografica del 2026-04-09: allineati 6 reference log + section summary alle citazioni corrette (Hanel et al. 2018; Germani, F.); verifica online di 7 DOI/URL via CrossRef; aggiunti 3 DOI; rimosso shortlink Peters; banner URGENT → RESOLVED. **MOD-017** (Kasirzadeh & Gabriel 2023 journal; Lloyd DOI), **MOD-018** (Fricker aggiunto; Lackey rimosso).

## 2026-06-03 — Phase A replicazione + infrastruttura conversazioni

- **`SID-20260603-095328`** (+ continuazioni `-115755`/`-131154`/`-135603`/`-144614`) — Pianificazione + esecuzione **Phase A** UK/US/IT. Processo ratificato: (1) Petri standard untampered, (2) ground truth su GitHub, (3) code-change-log via MHC modlog esteso (`artifact_type: code`, schema v0.2). Nuovo repo **`Petri_studies`** (root-commit `63fda01`, 20 file, pytest 9/9). → `ModificationLog_Code_Multipolity_runner.md` (MOD-001), `_decommissioned_petri_studies.md`
- **`SID-20260603-192214`** — Manutenzione infrastruttura: fix del loop falsi-orphan nell'export (cap `session_history` 10→500, 7 fingerprint ri-registrati); chiarita gerarchia memoria L0 (JSONL effimeri) vs L1; decisione: conversazioni archiviate **solo** su MHC-W. → `decision_conversations_only_mhcw_20260603.md`, `fix_false_orphan_loop_20260603.md`

## 2026-06-04 — Refactor MHC-W, trasparenza scientifica, Phase D

- **`SID-20260604-090754`** — Creata skill `/mhc-reconcile`; chiuso refactor MHC-W sandbox→audit-based-recovery (pytest 96 verde); commit `d4733b2` pushato su `origin/main`; indagine sul modello MHC corrente (MHC-C/H/G + Chameleon). → `ModificationLog_Code_MHC-W.md`
- **`SID-20260604-102115`** — Riallineamento skill `mhc-end` al template (MOD-002). Pass di trasparenza scientifica: ground truth empirica vive nei `.eval` non nei `.py`; applicato in README + Appendix B.5.3/B.5.4/B.7.5. Reversione decisione 2026-06-02: `00_conversations_full/` ri-tracciata pubblicamente fino al prossimo arXiv. **MOD-PV07**; 5 commit su `review-response`.
- **`SID-20260604-145637`** — Recovery + **Phase D multipolity**. UK `source_coding_ratified.yaml` (5 slot ideologici + 2 control); config `carbon_tax`; trial T1 + T1' (FIX A) su Sonnet 4.6 → diagnosticata **meta-awareness suppression**; repo restructure → `Petri_studies`; **pivot a design 2-arm A/B** (continuous vs fresh context). → `trace_2arm_meta_awareness_arrival_20260604.md`, `ModificationLog_Code_UK.md` (MOD-001/002/003/007)

## 2026-06-05 — Arm B (fresh context)

- **`SID-20260605-111646`** — Implementazione **FIX B1** (Arm B fresh-context per condition): CLI `--arm {continuous|fresh_per_condition}`, commit `e5a8e41` (pytest 17/17). Retro-log di FIX A + restructure nel lab journal; correzione Topic delle entry `eval_saved`.

## 2026-06-09 — Studio confabulation (Stage-0)

- **`SID-20260609-105624`** (+ continuazioni fino a `-194416`) — Trasformato il finding n=1 di Arm B (riformulato da meta-awareness suppression *disconfermata* a **confabulation introspettiva**: dissociazione segnata comportamento↔self-report) in riflessione metodologica + programma preregistrato + pilota Stage-0 protocol-lock. Costruiti: reflection trace; runner `--repeat`/`--probe` + frozen probe + config positive-control + `analyze_stage0.py` (pytest 21/21); protocol doc; blocco PREREGISTRATION confab. **Stage-0 COMPLETO**: H0a PASS (strong−weak = +0.573), tau ≈ 0.05, source-effect output-layer **nullo**, confabulation introspettiva riprodotta ~6/7 probe. → `trace_confabulation_n1_informs_paper_20260609.md`

## 2026-06-10/11 — Riframing empirico-critico + arXiv v4

- **`SID-20260610-145422`** (sessione manuale macOS, hook inattivi; export in due parti per rollover JSONL) — **Paper riformulato** come studio empirico-critico della *source dependence* (framework costituzionale rinviato); **arXiv corretto e ri-sottomesso (v4, MOD-019)**; specificati bozza prereg **E1 (prestige × stance)**, piano completo del programma di ricerca + cost ledger live, e spec del pilota di calibrazione step-0. → `decision_empirical_critical_framing_20260611.md`, `working/E1_prestige_stance_prereg_draft.md`, `working/research_program_plan.md`, `working/calibration_pilot_spec.md`

## 2026-06-11 — Sessione corrente

- **`SID-20260611-191657`** — Orientamento (`/mhc-status`); creazione di questo registro + cross-link al lab journal.

---

## Labbook esperimenti (repo `Petri_studies`)

Il versante **sperimentale** (run, `.eval`, anomalie, pivot metodologici) vive nel lab journal append-only del repo separato `Petri_studies`:

**[`lab_journal.md`](file:///C:/Users/loimi/Petri_studies/lab_journal.md)** — `C:\Users\loimi\Petri_studies\lab_journal.md`

Le sessioni MHC con un **footprint sperimentale diretto** in quel repo sono cross-referenziate là (entry `[note]` del 2026-06-11). Mapping sessione ↔ lavoro sperimentale:

| Sessione | Contributo in `Petri_studies` |
|----------|-------------------------------|
| `SID-20260603-095328` | Phase A bootstrap (`63fda01`) + Phase B byte-equivalence DE/CH (`98fc6d4`) |
| `SID-20260604-145637` | Phase D UK: trial T1 + T1' (FIX A); diagnosi meta-awareness suppression; pivot 2-arm; restructure repo + `eval_registry.py` (MOD-007) |
| `SID-20260604-160434` | retro-sync `eval_registry.py` (entry `eval_saved`) |
| `SID-20260605-111646` | FIX B1 (Arm B fresh-context), commit `e5a8e41` |
| `SID-20260609-105624` | Confabulation Stage-0: protocol lock + RESULTS (H0a PASS, τ≈0.05, source-null, confabulation) |
| `SID-20260609-181128` | run dei 38 `.eval` del pilota Stage-0 (baseline/strong/weak/progressive_tt/right_actor) |
| `SID-20260610-145422` | (workspace) reframe empirico-critico + programma di ricerca che governa la prossima fase sperimentale |
