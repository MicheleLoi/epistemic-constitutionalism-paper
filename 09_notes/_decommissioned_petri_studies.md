# Decommissione di ~/Petri_studies/ (2026-06-03)

Il codice Python che generava gli `.eval` per le iterazioni DE e CH del source-attribution-bias study viveva in `C:\Users\loimi\Petri_studies\` — circa 50 script Python, **NON git-versionati**, organizzati con il pattern per-topic + suffissi `_patched` / `_fixed` / `_simplified` / `_v1`.

Dal **2026-06-03** (SID-20260603-095328, plan §5 Fase C):

- La cartella è stata rinominata in `C:\Users\loimi\Petri_studies.archived_2026-06-03\` per togliere l'ambiguità su quale sia la sorgente viva.
- Un `README_LEGACY.md` è stato aggiunto dentro l'archivio per dichiarare il suo status non autoritativo.
- Il codice canonico per la replicazione (UK / US / IT più legacy compat DE+CH byte-equivalente) vive ora in `C:\Users\loimi\source-attribution-bias-multipolity\` (vedi `_org/external_repos.md`).
- Il legacy compat è dimostrato sui topic DE+CH carbon_tax via `runner/legacy_compat.py` con MATCH 3498/104 (DE) e 3052/90 (CH) — `MOD-002` nel modlog code.

## Cosa NON è cambiato

- I due repo GitHub esistenti (`source-attribution-bias-data` e `source-attribution-bias-swiss-replication`) restano intoccati come archivio storico degli `.eval` pubblicati.
- I file `09_notes/study4_*` in questo workspace sono **copie / annotazioni storiche** dei file del Petri_studies originale; restano qui come riferimento ma sono **non autoritativi**.

## Cosa fare se servono file dall'archivio

- **Per leggere/copiare:** navigare in `~/Petri_studies.archived_2026-06-03/`.
- **Per modificare il comportamento di un esperimento:** modifica `source-attribution-bias-multipolity/configs/<polity>/<topic>.yaml` (e crea un `MOD-NNN` nel modlog code).
- **Per riprodurre uno script storico al modo originale (se davvero serve):** `mv` indietro a `~/Petri_studies/` temporaneamente, fai il lavoro, rinomina di nuovo a `archived_*`, annota nell'operations log qui sotto.

## Operations log

| Date | Action | Reference |
|---|---|---|
| 2026-06-03 (SID-20260603-095328) | Decommissionato. mv `~/Petri_studies/` → `~/Petri_studies.archived_2026-06-03/`. README_LEGACY.md scritto. Ledger entry creata. | Plan §5 Fase C #5 |
