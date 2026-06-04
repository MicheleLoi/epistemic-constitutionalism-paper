---
artifact_type: placement_log
purpose: "Append-only log of placement decisions for non-canonical artifacts. Written by /mhc-place at save time. Used to review routing convention quality over time: recurring placements in unexpected locations signal gaps in the routing rules worth amending."
schema_version: 1
created: 2026-06-02
created_in_session: SID-20260602-165225
---

# Placement log

Append-only. One line type:

- `placement:` — written by /mhc-place at save time. Fields: date, SID, artifact description, path chosen, predicted tier, pointer (yes/no).

Nota: in questo progetto il log vive in `09_notes/` (convenzione cartelle numerate) anziché nel default `notes/methodology/` — non esiste `notes/methodology/`.

## Log entries

placement: 2026-06-02 SID-20260602-165225 | Piano di replicazione UK/US/IT (protocollo studio multi-polity, decisioni ratificate) | path: 09_notes/replication_plan_uk_us_it_20260602.md | tier: 2 | pointer: yes
