# External Repositories

Pointer da questo workspace di governance ai repository git esterni che contengono il *corpo tecnico* del progetto. Il workspace (`Epistemic constitutional AI/`) è il *cervello intellettuale*: paper, MHC artifacts, modlog, decision log. Gli external repo qui sotto contengono codice eseguibile + dati pubblicabili.

---

## Petri_studies

**Purpose:** replicazione UK / US / IT dello studio source-attribution-bias, più legacy compat DE + CH (prova byte-equivalence con gli script storici).

| Field | Value |
|---|---|
| Local path | `C:\Users\loimi\Petri_studies\` |
| GitHub URL | `https://github.com/MicheleLoi/Petri_studies` (NON ancora pushato — open gating §8 del plan, suggerito private fino al `preregistered-uk-v1`) |
| Default branch | `main` |
| Created | 2026-06-03 (SID-20260603-095328) |
| Last-known-good commit | `98fc6d4` (Phase B legacy compat — DE+CH byte-equivalent MATCH verificato 2026-06-03) |
| MHC modlog autoritativo | `03_modification_logs/ModificationLog_Code_Multipolity_runner.md` (workspace) |
| Plan di riferimento | `~/.claude/plans/as-we-go-pianifica-l-estensione-dello-serialized-pizza.md` §4bis |

### Cosa vive lì
- `runner/` — single Petri runner + Jinja2 template + JSON Schema + pytest
- `runner/legacy_compat.py` — script che dimostra byte-equivalence vs scripts DE/CH storici
- `configs/_shared/` — judge_dimensions + seed_skeleton (polity-invariant)
- `configs/de/` + `configs/ch/` — reconstruction byte-equivalent (Phase B)
- `configs/uk/` (TBD), `configs/us/` (TBD), `configs/it/` (TBD) — pending Phase D/E
- `evals/` — vuoto fino a Phase A2/D
- `docs/` — methodology, architecture, source coding protocol, adding_a_polity

### Sincronizzazione modlog
Ogni commit sostanziale nel repo nuovo ha:
1. Una entry `MOD-NNN` in `03_modification_logs/ModificationLog_Code_Multipolity_runner.md` (workspace, schema da `adapt.md` `content_schemas.code`)
2. Un mirror in `CHANGELOG.md` del repo (machine-readable, audit trail pubblico)
3. Una entry in `lab_journal.md` del repo (append-only, human-readable cronaca)

Il workspace modlog è l'autorità per il *perché*; il CHANGELOG è il riassunto pubblico; il lab journal è la cronaca passo-passo.

---

## source-attribution-bias-data (storico, DE)

| Field | Value |
|---|---|
| GitHub URL | `https://github.com/MicheleLoi/source-attribution-bias-data` |
| Role | Archive degli `.eval` files DE pubblicati dello studio originale |
| Modified here? | No — repo intoccato, archivio storico |
| Referenced by | `paper_full_draft.md` |

---

## source-attribution-bias-swiss-replication (storico, CH)

| Field | Value |
|---|---|
| GitHub URL | `https://github.com/MicheleLoi/source-attribution-bias-swiss-replication` |
| Role | Archive degli `.eval` files CH pubblicati della replicazione svizzera |
| Modified here? | No — repo intoccato, archivio storico |
| Referenced by | `paper_full_draft.md` |

---

## Decommissionato: ~/Petri_studies/

| Field | Value |
|---|---|
| Path originale | `C:\Users\loimi\Petri_studies\` |
| Path dopo decommissione | `C:\Users\loimi\Petri_studies\_archive\` |
| Role | Collezione live (NON git-versionata) di ~50 script Python da cui sono state estratte testualmente le `SEED_INSTRUCTION` per il legacy compat (Phase B) |
| Status | NON autoritativo dal 2026-06-03; codice canonico in `Petri_studies/` |
| Workspace note | `09_notes/_decommissioned_petri_studies.md` |

---

*Generato 2026-06-03 (SID-20260603-095328), Phase C plan §5.*
