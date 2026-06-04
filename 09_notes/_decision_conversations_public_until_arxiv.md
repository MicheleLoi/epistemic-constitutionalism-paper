---
artifact_type: note
session_id: SID-20260604-102115
inputs:
  - .gitignore
  - 09_notes/decision_conversations_only_mhcw_20260603.md
  - README.md
validation: approved
date: 2026-06-04
---

# Decisione — `00_conversations_full/` tracciata pubblicamente fino al prossimo arXiv

## topic

Reversione temporanea della decisione 2026-06-02 (untracking di
`00_conversations_full/`). La cartella torna tracciata nel repo pubblico
per la durata del peer review del prossimo arXiv release, poi viene
ri-rimossa.

## content

### Decisione
- `00_conversations_full/` (51+ file, transcripts writing + study development) viene
  ri-tracciata su `github.com/MicheleLoi/epistemic-constitutionalism-paper`.
- `conversations/` (export hook dir) **resta** ignored — coerente con la
  decisione [[decision_conversations_only_mhcw_20260603]] (futuri export →
  solo archivio MHC-W).
- `06_conversations/` (legacy hook dir) resta ignored.

### Razionale
1. Il paper, in `Appendix B.5.1`, afferma che i transcript sono *"preserved
   in the project repository (00_conversations_full/)"*. La gitignore del
   2026-06-02 rendeva quell'affermazione falsa: un revisore che clonava
   il repo trovava un path inesistente.
2. La privacy concern del 2026-06-02 era nominale: i 51 file erano già
   pubblici nella storia git da `e33d351` (2025-12-26 "Add files via
   upload"). Chiunque con un `git log` poteva recuperarli. L'untracking
   non aveva impedito nulla, aveva solo creato una contraddizione
   documentale.
3. Per la durata del review, la trasparenza dei materiali AI-assistance
   è meglio servita dalla presenza visibile dei transcript che dalla
   loro assenza con un'eccezione narrata.
4. Dopo arXiv: si torna allo stato 2026-06-02 (transcripts solo in
   archivio MHC-W centrale, non duplicati nel project tree pubblico) —
   coerente con il principio di lungo periodo che MHC-W è la home
   permanente, e i project tree pubblici sono snapshot di submission.

### Trigger per la ri-rimozione
Submission del prossimo arXiv release (atteso: v2 del paper, integrazione
della multipolity replication UK/US/IT — vedi
`Petri_studies`).

### Checklist di revert (al trigger)
1. Editare `.gitignore`: ripristinare la riga `00_conversations_full/` e
   il commento di privacy.
2. `git rm -r --cached 00_conversations_full/` (untrack senza eliminare
   i file fisici, che restano in working tree per uso locale).
3. Rimuovere il banner da `CLAUDE.md`.
4. Editare `Appendix B.5.1` per dichiarare che i transcript ora vivono
   in archivio MHC-W centralizzato (ripristinare la formulazione che era
   stata proposta — e poi annullata oggi — per riallineare a quella
   versione del paper).
5. Aggiornare/chiudere questa nota e [[decision_conversations_only_mhcw_20260603]].

## references

- `.gitignore` (modificato — vedi commento testuale sul ciclo di vita).
- Decisione collegata: [[decision_conversations_only_mhcw_20260603]] (regola
  generale "exports → solo MHC-W" che resta in vigore per i futuri export;
  questa decisione di oggi è limitata al materiale storico già presente).
- Commit di re-track: `65727de` (2026-06-04, SID-20260604-102115).
- Storia git pubblica: `e33d351` (primo upload, 2025-12-26).
- README.md (re-tracking riflesso nella sezione 2 "AI-assistance transparency").
- Appendix B.5.1 (paper) — quando aggiornato, link incrociato qui.
