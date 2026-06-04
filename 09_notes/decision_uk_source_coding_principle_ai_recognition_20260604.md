---
artifact_type: decision_note
title: "UK source coding — AI-recognition principle"
session_id: SID-20260604-145637
inputs:
  - 09_notes/replication_plan_uk_us_it_20260602.md
  - C:/Users/loimi/Petri_studies/docs/source_coding_protocol.md
  - C:/Users/loimi/Petri_studies/configs/de/source_coding.yaml
validation: approved
date: 2026-06-04
durable_until: superseded
references:
  - C:/Users/loimi/Petri_studies/configs/uk/source_coding_ratified.yaml (forthcoming)
---

# Decisione: AI-recognition is the binding constraint per la source coding multipolity

## Issue

Per ogni slot del 7-condition design, esiste un trade-off tra:
- **AI-recognition**: il modello ha un prior stabile e ricco sulla fonte?
- **Reader-recognition**: il lettore del paper conosce la fonte?
- **Role-match cross-polity**: la fonte ricopre il ruolo parallelo al corrispettivo DE/CH (es. sitting MP, current party leader, former Finance Minister)?

Per qualunque slot, può capitare che le tre dimensioni siano in tensione.

## Analisi

Lo studio misura **come il modello aggiorna il rating quando cambia la fonte**.
Se il modello non ha un prior sulla fonte, **il prior non c'è — non c'è effetto da misurare**.
La manipolazione sperimentale fallisce per assenza di trazione, non per assenza
dell'effetto teorico.

Il lettore invece riceve contesto **dalla prosa del paper**. Una frase come
"Caroline Lucas, former Green Party MP for Brighton Pavilion 2010-2024, now
Professor of Practice at Sussex" è descrittivamente informativa anche per un
lettore che non la conosce. La descrizione **supplementa** la fama.

Il role-match cross-polity è desiderabile per interpretabilità comparativa, ma
secondario rispetto alla validità interna di ciascuna replicazione: ogni
replicazione (DE, CH, UK, US, IT) **vive di sua propria validità interna**,
non come funzione meccanica della prima.

## Verifica

- DE parent study: Lisa Badum (Green MP), non particolarmente famosa
  internazionalmente, ma con prior stabile come "Bündnis 90 MP" in qualunque
  modello che includa political training data tedeschi. Cioè: il parent study
  ha applicato implicitamente lo stesso principio — riconoscibilità AI > fama
  reader.
- Dual-model design (Sonnet 4.5 + Opus 4.8): asimmetria di prior tra i due
  modelli sulla stessa fonte sarebbe un **confound non separabile** dal
  capacity tier che lo studio vuole misurare. Conseguenza: la fonte scelta
  deve avere recognition stabile **across both model cutoffs**.

## Decisione

**Principio applicato per la ratifica UK e per le successive US/IT:**

> Quando AI-recognition, reader-recognition, e role-match cross-polity sono in
> tensione, **prevale AI-recognition**. In particolare:
> - Riconoscibilità stabile across i model cutoff dello studio
>   (Sonnet 4.5 + Opus 4.8) ≻ riconoscibilità "current" del lettore
> - Coding ideologico unambiguo e stabile ≻ role-symmetry con parent study
> - Fonti con status flippato di recente (post mid-2025) sono evitate se
>   l'aggiornamento non è ancora nel training data di tutti i modelli usati

## Affects

- UK source_coding_ratified.yaml — slot `green_actor` ratificato come
  Caroline Lucas (vs. Carla Denyer/Zack Polanski) applicando questo
  principio.
- Slot UK rimanenti (right_actor, conservative_tt, ...) — applicare lo
  stesso principio.
- Future ratifiche US e IT — stesso principio.
- Paper write-up: questo principio andrà esplicitato come scelta
  metodologica nel methods/methods-replication section.
