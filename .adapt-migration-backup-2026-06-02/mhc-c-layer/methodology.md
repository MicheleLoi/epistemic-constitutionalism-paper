---
artifact_type: methodology
document: MHC-C — Methodology and Artifact Model
project: Epistemic constitutional AI
describes: The mental model for MHC-C artifact types; the authoritative-spec status of SKILL.md files
created: 2026-06-02
---

# MHC-C — Methodology

## The mental model

Gli artefatti MHC-C sono una **catena di ragionamento che rende un progetto verificabile fino alla
sua origine**.

Il deliverable da solo non basta. Per lavoro che conta — ricerca, consulenza, ingegneria, scrittura
accademica — ciò che vale è che un lettore futuro (tu fra un mese, un collega, un revisore) possa
ricostruire all'indietro dall'output *perché ha la forma che ha*. Ogni tipo di artefatto cattura un
momento di quella ricostruzione.

## The artifact types

### Primary outputs — what you are making

**`working/`** — gli output primari del progetto. In questo workspace di ricerca il deliverable
finale è il paper (`paper_full_draft.md`, assemblato manualmente dalle sezioni); `working/` ospita
le bozze di lavoro che confluiscono nel paper. Usa `/mhc-output` per salvare un output con metadati
strutturati; non scrivere mai direttamente nella cartella di output primario senza metadati.

### Exploration and specification — what feeds a primary output

**`09_notes/`** — quick capture, ricerca, materiale di riferimento. Usa `/mhc-note`.

**`01_epistemic_traces/`** — pensiero cristallizzato dopo sessioni esplorative. Usa `/mhc-trace`.

**`08_prompt_development_logs/`** — PDL che documentano **cosa** un draft deve contenere. Usa
`/mhc-pdl`, mentre scrivi il prompt o retrospettivamente.

**`02_main_prompt/`** — prompt AI finiti derivati da un PDL.

### Revision — what records changes to a primary output

**`03_modification_logs/`** — log delle decisioni di revisione per modifiche a draft o prompt. Usa
`/mhc-modlog`. I draft non cambiano in silenzio.

### Auto-managed

**`00_conversations_full/`** — conversazioni di sessione esportate.

## How the artifact types relate

- Un *trace* esplora una domanda; può portare a un *PDL* che specifica cosa generare; il PDL produce
  un *prompt*; il prompt genera un *draft* (output primario).
- Una *note* è leggera — materiale di riferimento, un'idea, una scoperta. Può diventare uno dei
  precedenti, o restare così.
- Un *modlog* documenta cosa è cambiato in un draft e perché. Può essere scritto prima, durante o
  dopo la modifica — conta la cattura, non l'ordine.

Non ogni draft ha un trace e un PDL a monte. I draft ad-hoc vanno bene. Ma la catena esiste quando
serve, e renderla esplicita nel campo `references:` mantiene la provenienza verificabile.

## The single question this model answers

*Un lettore a freddo, aprendo il progetto fra sei mesi, può ricostruire perché il deliverable ha la
forma che ha?*

Se sì, la metodologia funziona. Se no, qualcosa nella catena manca o è rotto — è lì che guardare.

## Skills are the specifications

Lo `SKILL.md` di ogni tipo di artefatto è la **specifica autoritativa** per quel tipo. Prima di
creare o modificare un trace, PDL, note, draft, modlog o prompt, leggi direttamente lo `SKILL.md`
pertinente. Non dedurre il formato dai file esistenti — potrebbero essere errati.

## Content schemas — universality + configurability

Ogni skill di capture (`mhc-note`, `mhc-trace`, `mhc-modlog`, `mhc-pdl`, `mhc-output`) legge
`content_schemas.<type>.fields` dal frontmatter di `adapt.md`. Se dichiarato, la skill usa quei
campi. Se assente, ricade sul default hardcoded (retrocompatibilità).

Questo schema permette di rimodellare il **contenuto** di ogni tipo di artefatto per progetto senza
forkare la skill. La skill è universale — il protocollo è invariante (leggi config, esponi scelte,
assembla oggetto tipizzato, valida con l'utente, scrivi). Lo schema appartiene al dominio.

Per personalizzare: modifica il blocco `content_schemas:` in `adapt.md`. Per tornare ai default:
elimina il blocco (subentra il fallback hardcoded in ogni skill).

## Boundaries of MHC-C (vs MHC-W/MHC-H)

MHC-C è il **Core standalone**: skill di capture (note, trace, modlog, pdl, output, onboard) +
orientamento leggero (status) + operatività filesystem-only. Niente server, niente rete, niente
memoria cross-sessione oltre a ciò che `.mhc-config.json` registra localmente, niente catena di
audit, niente orchestrazione di sessione.

In questo progetto MHC-C **coesiste** con il setup MHC-W esistente (harness con hook e routing
comandi, operativo in Claude Code). MHC-C non rimpiazza MHC-W: aggiunge uno strato leggero usabile
anche fuori da Claude Code (es. Cowork). Gli hook `SessionEnd` e i comandi `MHC-*` restano definiti
in `CLAUDE.md` / `.claude/` e si attivano solo dentro Claude Code.
