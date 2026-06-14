---
artifact_type: note
subtype: executive_summary
topic: Executive summary — verifica ground-truth e correzioni del labbook (2026-06-13)
project: Epistemic constitutional AI
session_id: SID-20260613-002241
created: 2026-06-13
validation: approved
inputs:
  - 09_notes/methodology_ground_truth_verification_20260613.md (metodologia completa + comandi di riproduzione)
  - C:/Users/loimi/Petri_studies/lab_journal.md (reader's guide + [correction], commit cd678c3)
  - Petri commit cd678c3 + tag preregistered-e1-v1 (5f54c8a); workspace commit 9e51c68
  - verification workflow wf_c1614b25-298 (35 agenti, 16 claim, primario + triangolazione avversariale)
---

# Executive summary — verifica e correzione del labbook (2026-06-13)

**In una riga:** la ricostruzione del lab journal (la "reader's guide") è stata sottoposta a verifica
ground-truth completa — **16 claim ricontrollati, 0 falsificati** — e tutte le imprecisioni sono state
corrette e messe in sicurezza in git, con ogni numero ri-derivato da fonti immutabili e provenienza
dichiarata onestamente. Dettaglio + comandi di riproduzione: [[methodology_ground_truth_verification_20260613]].

## 1. Il problema
La reader's guide pretendeva di "enunciare la ground truth". Un bug report **esterno, non attribuito**
("il ghost") ha segnalato un errore statistico. Decisione: non fidarsi né del ghost né della prosa del
journal — **ri-derivare ogni numero load-bearing da una fonte immutabile**.

## 2. Il sistema di verifica
Quattro livelli di evidenza indipendenti, ognuno per triangolare gli altri:
- **L0** — i file `.eval` (dati grezzi, ZIP immutabili)
- **L1** — gli script deterministici, version-pinned (ri-eseguiti)
- **L2** — git SHA / tag / hash dei prompt
- **L3** — coerenza incrociata fra gli artefatti MHC

Eseguito come workflow a **35 agenti** (`wf_c1614b25-298`): 16 claim, ciascuno ri-derivato (primario) +
ri-controllato in modo avversariale su un layer diverso. **Esito: 0 claim falsificati.** I risultati
empirici reggono (entrambi i gate H0a, la rating-head satura, la confabulation, la byte-compat, il lock E1).
La verifica è stata **read-only**: nessuna nuova run `.eval` generata — solo ri-derivazione su evals esistenti,
ri-esecuzione di script e check git/hash.

## 3. Cosa è emerso — 5 correzioni
| # | Correzione | Impatto |
|---|---|---|
| 1 | **Confab medium baseline n=18 → n=19** (mean 0.6342, SD 0.0232). Un bug del parser flat-brace scartava 1 rating valido (0.62). | Gate H0a (strong 0.760 / weak 0.188 / +0.573 PASS), τ, source-null **invariati** |
| 2 | **Temperatura "confermata dal .eval" = FALSO**: il `.eval` non registra alcun campo temperature; 1.0 è il default API (inferenza). | Non-determinismo regge, su altra evidenza |
| 3 | **Hash di lock non annotato**: `a1899eb1` è il render a singola condizione (c0); il full-config è diverso (`f6ff425d`). | Evita un falso mismatch in riproduzione |
| 4 | **Costi €20/€35 = proiezioni**, non dati misurati (≈€22/€38 @0.92). | La tesi "il costo non è il vincolo" regge |
| 5 | **Difetto latente `regime()`** (griglia stale {0.60–0.68}, non vede gli attrattori 0.25/0.72). | Non-load-bearing; documentato, fix rinviato |

## 4. Il punto epistemico (il più importante)
- **Il ghost è tracciato e archiviato come ciò che è:** esterno, non attribuito, **senza origine locale**
  (cercato in tutti i transcript) → nessuna autorità. La correzione **non poggia sul ghost**, ma sul
  conteggio grezzo dei `.eval` riprodotto direttamente.
- **Lezione resa metodo:** *deterministico ≠ corretto.* Uno script buggato ma deterministico riproduce il
  numero sbagliato ogni volta — solo una lettura grezza indipendente lo smaschera. E: **non rivendicare
  indipendenza quando la corroborazione condivide la causa**. Scritto nella sezione *limits of independence*
  della metodologia.

## 5. Cosa è stato messo in sicurezza
- **Petri `cd678c3`** (main): fix del parser + reader's guide + voce `[correction]` + annotazioni; sopra il
  lock E1 `5f54c8a` / tag `preregistered-e1-v1`.
- **Workspace `9e51c68`** (review-response): documento di metodologia, MOD-010, MOD-005, correzione
  temperature nel trace, flag costi/proiezioni, topology.

## 6. Stato finale
La ricostruzione del labbook è **grounded**: ogni numero ri-derivabile, provenienza onesta, metodologia
ri-eseguibile da chiunque. **Residui non bloccanti (registrati):** `.mhc-config.json` (hook); fix `regime()`;
rigenerazione `_wredit` Win-Rate dalla base mediocre; `.gitignore` per `.obsidian/` in Petri; nessun push
(solo commit locali); 1 sessione da esportare → `/mhc-end`.
