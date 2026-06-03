---
artifact_type: note
session_id: SID-20260603-192214
inputs:
  - ../MHC-W/scripts/extract_conversation.py
  - ../MHC-W/scripts/mhc_end.py
  - ../MHC-W/.gitignore
  - .mhc-config.json
validation: approved
date: 2026-06-03
---

# Nota / Decisione — Conversazioni archiviate SOLO su MHC-W

## topic

Decisione presa il 2026-06-03 (SID-20260603-192214): le conversazioni esportate
non vengono più duplicate nella cartella del progetto-paper. L'unica destinazione
è l'archivio centralizzato MHC-W. Decisione già richiesta in passato ma andata
persa — questa nota la fissa con il *perché* e il *come non riperderla*.

## content

### Decisione
L'export delle conversazioni scrive **solo** nell'archivio centralizzato MHC-W
(`MHC-W/00_full_conversations/exported/raw/` = JSONL ground truth +
`.../md/` = markdown). **Nessuna** copia in `<progetto>/conversations/exported/`.

### Razionale
- **MHC-W non sarà mai reso pubblico** (progetto archiviato in quella forma) →
  tenere lì i transcript di ricerca è sicuro; non c'è rischio di leak da release.
- I tree per-progetto sono invece potenzialmente condivisi/pubblicabili: i
  transcript non devono finirci.
- Elimina la duplicazione che, tra l'altro, alimentava il loop di falsi-orphan
  (vedi [[fix_false_orphan_loop_20260603]]).
- La ground truth resta comunque ridondante e permanente: `raw/` conserva il
  JSONL grezzo anche dopo che Claude Code cancella l'originale locale (~30 giorni).

### Modifica tecnica applicata
`MHC-W/scripts/extract_conversation.py`:
- Rimosso il blocco "Copy MD to project folder" (ex righe 418–435): niente più
  `shutil.copy` verso `<progetto>/conversations/exported/`.
- Docstring aggiornato: archivio MHC-W = unica destinazione.
- La copia centralizzata MHC-W (`raw/` + `md/`) è invariata.
- **Non rompe `mhc_end.py`**: non trovando più la riga `Project copy:`, usa il
  fallback `Exported N messages to: <md_dest>` → l'`export_path` del record di
  sessione punta alla copia MHC-W centralizzata. Verificato nel codice.

### Stato e come NON riperderla
- La modifica è nel **working tree** di MHC-W, insieme a un refactor WIP più ampio
  (extract_conversation.py, mhc_end.py, mhc_check.py, mhc_start.py, ecc.) — **non
  committata**.
- **Causa della perdita precedente**: la modifica non fu propagata al remoto
  (`github.com/MicheleLoi/MHC-W`, privato) → un checkout/pull successivo ripristinò
  il blocco. **Rimedio**: `git add scripts/extract_conversation.py` → commit →
  **`git push`**. Finché resta solo locale, può svanire di nuovo.

## references

- `MHC-W/scripts/extract_conversation.py` (modifica), `MHC-W/scripts/mhc_end.py`
  (fallback path-anchoring, righe ~187/377), `MHC-W/.gitignore` (00_full_conversations
  = keep local only), archivio `MHC-W/00_full_conversations/exported/` (260 raw + 261 md).
- Cartella `<progetto>/conversations/exported/` esistente (16 export SID-based)
  lasciata in sede: sono duplicati dell'archivio MHC-W, `untracked` in git. Da
  rimuovere quando si vuole — non urgente.
- Nota correlata: [[fix_false_orphan_loop_20260603]].
