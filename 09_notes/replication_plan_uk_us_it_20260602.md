---
artifact_type: study_protocol
title: Replication plan — UK / US / IT source-attribution bias
session_id: SID-20260602-165225
inputs: [paper_full_draft.md, adapt.md, .mhc-config.json]
validation: approved
status: design ratified; source coding open
---

# Replication plan — UK / US / Italy

## Purpose
Extend the source-attribution-bias study (German parent + Swiss replication) to three
new polities, addressing the paper's stated limitation: effects shown only in DE/CH,
single model family. Three **independent** replications, each polity-tailored — as DE
and CH stood alone.

## Held constant from DE/CH (the "replication" core)
- **Petri framework**: auditor / target / judge, rollback between conditions.
- **7-condition seed** per evaluation: baseline (no source) → generic ("policy
  researchers") → 2 aligned → 2–3 misaligned → 1 neutral/expected-boost. Argument text
  identical across all seven; only attribution changes.
- **Judge dimensions**: coherence-effect detection, source-based-reasoning visibility,
  rating-shift magnitude, protocol execution.
- **Effect measure**: rating range (aligned vs misaligned) + left/right penalty asymmetry.
- **Anti-spoiler discipline**: no comparative transitions ("another argument",
  "continuing my analysis"), no "regardless of source"/"systematic analysis" phrasing,
  topic-consistent seeds, fresh context between conditions. Budget ~50% spoilage → run
  extra seeds to land enough valid evaluations.

## Models
Claude Sonnet 4.5 + Claude Opus 4.8 (within-family, capability-tier comparison; no
GPT-4o). Framing: "does the effect hold, and change shape, as Claude scales up?"
Honest caveat in write-up: does NOT address cross-vendor generalization.

## Topics (adapted per polity)
| Topic | UK | US | Italy |
|---|---|---|---|
| AI regulation | ✓ | ✓ | ✓ |
| AI security | ✓ | ✓ | ✓ |
| Carbon pricing / climate | ✓ (net zero) | ✓ | ✓ (transizione ecologica) |
| Nuclear energy | ✓ | ✓ | ✓ (esp. diagnostic — referendum history) |
| Native fiscal topic | Fiscal rules / austerity | Debt ceiling | EU fiscal rules / public debt |
| Distinctive (optional) | Immigration (Channel crossings) | Gun control / border | Immigration |

Drop or swap any topic that doesn't produce a clear *expected-position* tension in a
given polity — flagged per seed.

## Source mappings (DRAFT — pending ratification; load-bearing)
**UK** — Right TTs: IEA, Centre for Policy Studies · Left TTs: IPPR, New Economics
Foundation · Neutral: Institute for Fiscal Studies · Green: Green Alliance · Security:
RUSI · Digital rights: Open Rights Group · Politicians: Conservative (Hunt/Badenoch),
Labour (Reeves/Miliband), Reform (Farage), Green (Denyer).

**US** — Right TTs: Heritage, AEI · Libertarian: Cato · Left TTs: Center for American
Progress, Economic Policy Institute · Neutral: CBO / Brookings · Environmental:
NRDC / Sierra Club · Security: CSIS / RAND · Digital rights: EFF · Politicians:
recognizable Republican + Democrat senator per topic.

**Italy** — Right/market-liberal TTs: Istituto Bruno Leoni, Aspen Institute Italia
(centrist anchor) · Left/labour TTs: Fondazione Di Vittorio (CGIL), Sbilanciamoci ·
Neutral fiscal: Osservatorio CPI (Cottarelli), Banca d'Italia · Green: Legambiente,
Kyoto Club · Security/foreign: IAI, ISPI · Digital rights: Hermes Center ·
Politicians: FdI (Meloni/Giorgetti), Lega (Salvini), Forza Italia (Tajani),
PD (Schlein), M5S (Conte), AVS-Greens (Bonelli).

## Human / AI division (Rule 5)
- **Human (judgment I lack):** ratify each source's ideological coding; veto politicians
  with idiosyncratic public reversals that muddy "expected position"; sign off on seeds
  and written-up results.
- **AI:** draft seeds, run Petri, transcribe rating distributions, qualitative transcript
  reading (where the mechanism shows), draft tables.

## Deliverables
- Three repos mirroring the Swiss one: `…-uk-replication`, `…-us-replication`,
  `…-it-replication`.
- Paper integration: Section 2 subsection + Appendix A.6 (UK) / A.7 (US) / A.8 (IT) +
  five-polity comparison table (DE, CH, UK, US, IT).

## Open item (next step)
Ratify the source mappings above — the design's load-bearing step. Nothing runs until
the "expected position" coding is validated.
