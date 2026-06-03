---
artifact_type: note
session_id: SID-20260603-192214
inputs:
  - .mhc-config.json
  - ../MHC-W/scripts/mhc_end.py
  - ../MHC-W/scripts/mhc_check.py
  - session_topology.yaml
  - conversations/exported/
validation: approved
date: 2026-06-03
---

# Nota operativa — Fix del loop di "falsi orphan" nell'export conversazioni

## topic

L'hint `[MHC hint] N past sessions not yet exported` ricompariva a ogni apertura
di sessione e, eseguendo `--recover-orphans`, produceva ogni volta file di export
duplicati con nome basato su timestamp. Spreco ricorrente e crescente. Risolto il
2026-06-03 (SID-20260603-192214).

## content

### Sintomo
A ogni `/mhc-start` l'hook contava 6–7 "sessioni non esportate". Lanciando il
recovery si creavano duplicati (`Epistemic_constitutional_AI_<timestamp>.md`) di
export SID-based già esistenti in `conversations/exported/`. La diagnosi andava
rifatta da capo ogni volta.

### Causa radice (verificata nel codice MHC-W)
1. `audit_sessions` (`mhc_check.py`) decide cosa è "orphan" confrontando i JSONL
   fisici **solo** con i `jsonl_fingerprint` presenti in `session_history`.
2. `finalize_session` (`mhc_end.py`) troncava `session_history` alle **ultime 10**
   (`history[-10:]`). Ogni sessione che usciva dalla finestra ridiventava "orphan",
   pur essendo già stata esportata.
3. `--recover-orphans` esporta con nome-timestamp e **non scrive mai** in
   `session_history` → i recuperati restavano orphan in eterno → loop perpetuo,
   per giunta in crescita (più sessioni si fanno, più JSONL escono dalla finestra).

Aggravante: i JSONL del progetto sono pochi ma enormi e sovrapposti (uno da
~1.8 MB copre dal 26/05 al 02/06). La relazione file-fisico ↔ SID è molti-a-molti;
il `session_history` per-SID troncato non riusciva a rappresentarla.

### Fix applicato (cerotto ratificato — non la fix-script completa)
- **`MHC-W/scripts/mhc_end.py`**: troncamento `10 → 500` (di fatto nessun
  troncamento nell'uso normale; commento esplicativo inline datato).
- **`.mhc-config.json`**: registrati i 7 fingerprint orphan storici in
  `session_history`, marcati `reconstructed: true` + `reconstructed_in` + `note`,
  ciascuno legato alla sua sessione reale già esportata (`export_file` di prova).
  La sessione corrente (`a41b8793` → SID-20260603-192214) è esclusa: la finalizza
  `/mhc-end`.

### Verifica
`audit_sessions` post-fix: **9 indexed, 1 unprocessed** — e l'unico unprocessed è
la sessione viva (corretto). Nessun falso orphan residuo.

### Nessuna memoria persa
La cancellazione dei 7 duplicati timestamp NON ha toccato memoria: i JSONL grezzi
(fonte di verità) sono tutti presenti, gli export SID-based intatti, gli artefatti
distillati (modlog/trace/topology) intatti. Un export `.md` è una vista
ri-generabile dal JSONL, non l'originale.

## references / cosa NON rifare

- **Non** eseguire `--recover-orphans` se l'audit segnala come orphan sessioni che
  hanno già un export SID-based in `conversations/exported/`: è un falso positivo.
  Verificare prima l'esistenza del file SID-based.
- L'unico orphan legittimo da esportare è una sessione **senza** export SID-based
  (tipicamente una sessione mai finalizzata via hook).
- Config drift collaterale ancora aperto (non bloccante): `.mhc-config.json`
  dichiara `folders.conversations_exported = "00_conversations_full/exported"` ma
  gli export reali finiscono in `conversations/exported/`. Da allineare quando si
  riprende il tema infrastruttura.
- Fix-script "definitiva" non adottata (scelta utente: cerotto). Se il problema
  riemerge in forma nuova, la fix vera è rendere `audit_sessions` idempotente
  rispetto a un indice di fingerprint persistente, indipendente da `session_history`.

File toccati: `MHC-W/scripts/mhc_end.py`, `.mhc-config.json`, questa nota.
