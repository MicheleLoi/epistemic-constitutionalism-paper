---
artifact_type: work_item_brief
titolo: Adattatore mhc-harness-client → MHC-W (libreria-ponte discipline-grade)
progetto: Epistemic constitutional AI
data: 2026-06-02
stato: parcheggio (non per esecuzione immediata)
origine_sessione: SID-20260602-134807
authority: _org/decision_log.md 2026-06-02 §"Architettura MHC ibrida + adozione del decision_log"
---

# Adattatore `mhc-harness-client` → MHC-W

## Cos'è (e cosa vuol dire "shim")

Uno **shim** è uno **strato adattatore**: una piccola libreria che espone l'interfaccia
attesa da un consumatore, traducendone le chiamate verso un backend diverso da quello
originariamente previsto. Qui: le skill MHC-C "harness-aware" (`mhc-place`, `mhc-reconcile`)
sono scritte per chiamare la libreria `mhc-harness-client`, il cui backend *previsto* è il
server custode cieco di **MHC-H** (inesistente). L'adattatore implementa la stessa interfaccia
ma con backend **MHC-W** (git + hook + `session_topology.yaml` + transcript deterministici).

Effetto: le skill harness-aware si "accendono" e offrono le garanzie che MHC-W *può* dare,
invece di degradare a filesystem-only.

## Scopo — continuità di funzione attraverso harness diverse

Lo scopo primario dell'adattatore è rendere le skill **harness-agnostiche**: dipendono da
un'**interfaccia stabile** (`mhc-harness-client`), non da una harness specifica. Il backend
sotto può cambiare senza toccare le skill.

```
            interfaccia stabile (mhc-harness-client)
skill mhc-c ─────────────────────────────────────────► [ backend ]
                                                          ├─ nessuno  → degrade filesystem-only
                                                          ├─ MHC-W    → adattatore (oggi)
                                                          └─ MHC-H    → server custode (domani)
```

- **Percorso downgrade:** MHC-H assente → le skill funzionano via MHC-W.
- **Percorso upgrade:** MHC-H arriva → si sostituisce il backend, stessa interfaccia, skill invariate.

**Distinzione vincolante:** è continua la *funzione*, non il *grado di garanzia*. `reconcile()`
gira con entrambi i backend, ma con MHC-W coglie *"l'artefatto è fedele al transcript?"*
(discipline/provenance-grade), con MHC-H coglie anche *"qualcuno ha manomesso il record?"*
(adversarial/crittografica). Stessa funzione; la garanzia **scala con la harness**, non con
l'adattatore.

## Premessa di principio (perché ha senso)

MHC-W produce record in modo **deterministico** (hook macchina-generati, non agente-generati)
e versionato (git). Questo dà **indipendenza di provenienza**: un *ground truth* contro cui
verificare gli artefatti dell'agente. È esattamente il principio già sancito nel `decision_log`
(2026-06-02): *"il numero dichiarato da un agente non è evidenza; il git diff lo è"*.

Quello che MHC-W **non** dà: tamper-evidence crittografica, dimostrabilità a terzi, cross-machine.
Quello resta dominio di MHC-H. L'adattatore quindi copre il livello **discipline/provenance-grade**,
non l'adversarial.

## Mappa delle affordance (cosa copre l'adattatore)

| API `mhc-harness-client` | Backend MHC-H | Backend MHC-W (adattatore) | Coperto |
|---|---|---|---|
| `register(artifact, type, sid)` | append su server cieco + HMAC | append a `artifacts_produced` (hook) + git | ✅ discipline-grade |
| `get_session()` | sessione server | `current_session` da `.mhc-config.json` | ✅ |
| `list_artifacts(sid)` | query server | scan cartelle / `session_topology.yaml` | ✅ |
| `reconcile(sid)` | drift vs log server | drift vs transcript/git (ground truth) | ✅ prende il drift dell'agente; ❌ non adversarial |
| `encrypt / decrypt / derive_key` | argon2id + ciphertext | — | ❌ solo MHC-H |
| `verify_signature` | HMAC su catena | hash commit git (analogo debole) | ⚠️ parziale |

## Regola di onestà (vincolante)

- `reconcile()` si etichetta **discipline-grade** e dichiara il limite (come già fa la skill:
  *"filesystem-only; MHC-H aggiungerebbe il custode indipendente"*). Non spaccia indipendenza
  adversarial.
- Le funzioni crypto (`encrypt`/`decrypt`/`derive_key`/`verify_signature`) sono **no-op che
  dichiarano "richiede MHC-H"** — mai implementazioni finte che simulino una garanzia assente.
- `register()` scrive solo dove MHC-W è autorevole (artifacts_produced + git), mai duplica
  contenuto di conversazione nel progetto (vincolo: solo metadati/pointer).

## Scope tecnico

- Pacchetto Python `mhc_harness_client` importabile nell'ambiente in cui girano le skill.
- Implementare: `register`, `get_session`, `list_artifacts`, `reconcile` su backend MHC-W.
- Stub dichiarativi per: `encrypt`, `decrypt`, `derive_key`, `verify_signature` (sollevano/loggano
  "MHC-H required").
- `reconcile(sid)`: confronta gli artefatti dichiarati/registrati con il **transcript
  deterministico** della sessione (`00_conversations_full/exported/<SID>...`) e con il git diff;
  ritorna un dict conforme al contratto già atteso dalle skill (`status`, `drift_detected`,
  `drift_details`, ...).

## Acceptance gate

- `register()` aggiorna `session_topology.yaml` (o delega all'hook) in modo idempotente.
- `reconcile()` rileva un drift sintetico iniettato (artefatto che afferma una decisione assente
  dal transcript) → `drift_detected: True`.
- Import assente / backend non configurato → le skill degradano come oggi (nessuna regressione).
- Le funzioni crypto non restituiscono mai un esito che sembri una garanzia adversarial.

## Confini

- È **codice nuovo** (un piccolo build), non una configurazione: work-item a sé, in parcheggio.
- Non tocca le skill plugin `mhc-c:` (restano universali); l'adattatore è esterno e opt-in.
- Non sostituisce MHC-H: ne è il sostituto *discipline-grade* finché MHC-H non esiste; se un
  domani MHC-H arriva, lo stesso contratto può puntare al server senza cambiare le skill.

---
*Brief di parcheggio — origine SID-20260602-134807. Esecuzione solo su ratifica founder.*
