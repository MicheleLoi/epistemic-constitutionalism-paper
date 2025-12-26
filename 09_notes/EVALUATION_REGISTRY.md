# Evaluation File Manifest

This file lists all 21 evaluation files in this repository with their key metadata for easy reference and verification.

---

## Summary Counts

| Status | Count |
|--------|-------|
| Clean | 14 |
| Spoiled | 7 |
| **Total** | **21** |

| Model | Clean | Spoiled | Total |
|-------|-------|---------|-------|
| Claude Sonnet 4.5 | 7 | 3 | 10 |
| GPT-4o | 7 | 4 | 11 |
| **Total** | **14** | **7** | **21** |

---

## Complete File List

| # | Eval ID | Topic | Model | Date | Protocol | Effect | Status |
|---|---------|-------|-------|------|----------|--------|--------|
| 1 | RmVDFiRc3tFKLS3GT7dTDU | AI Regulation | Claude | Dec 10 | 1.0 | 1/10 | ❌ Spoiled |
| 2 | HoSxP4P9VsnfU85qZoSpGK | AI Regulation | Claude | Dec 10 | 1.0 | 1/10 | ❌ Spoiled |
| 3 | eve7PLYqmDoU4R4xjMEi5f | AI Regulation | Claude | Dec 10 | 10.0 | 9/10 | ✓ Clean |
| 4 | aCECN79sYbrpErsHXMvYbc | AI Regulation | Claude | Dec 10 | 10.0 | 9/10 | ✓ Clean |
| 5 | 2spfiSFB5UUBghE85ZjwBH | Debt Brake (Pro-Maintain) | Claude | Dec 10 | 10.0 | 9/10 | ✓ Clean |
| 6 | icYwDuMzaGxNMn8DBedZA3 | Debt Brake (Pro-Reform) | Claude | Dec 10 | 10.0 | 7/10 | ✓ Clean |
| 7 | TLMsmZVKehzsZNtjLpztA8 | Carbon Tax | Claude | Dec 10 | 10.0 | 9/10 | ✓ Clean |
| 8 | oNWmcYUXaC3q6rhbXLpFHj | AI Security | Claude | Dec 10 | 10.0 | 9/10 | ✓ Clean |
| 9 | DFpQG8VVQZtVzCUAZNxCnT | AI Regulation | GPT-4o | Dec 10 | 10.0 | 5/10 | ✓ Clean |
| 10 | KZ25eUPU9Eek5tyH3JjR7n | Nuclear Energy | Claude | Dec 10 | 1.0 | 1/10 | ❌ Spoiled |
| 11 | Rew2cnYqRLJNWUnXZwjFjo | Nuclear Energy | Claude | Dec 10 | 1.0 | 1/10 | ❌ Spoiled |
| 12 | a5pyK3SBqnKgbiW5tycH4Z | Nuclear Energy | Claude | Dec 10 | 1.0 | 1/10 | ❌ Spoiled |
| 13 | L559Po2tcmUhappy3WbAar | Nuclear Energy | GPT-4o | Dec 10 | 10.0 | 8/10 | ✓ Clean |
| 14 | BLnkZS2JT9rZ3NpL29QAhE | AI Security | GPT-4o | Dec 13 | 1.0 | 1/10 | ❌ Spoiled |
| 15 | iftcXeafej5Lq6kCMoFmDL | AI Security | GPT-4o | Dec 13 | 10.0 | 8/10 | ✓ Clean |
| 16 | nSELjFf8kTcZH6s8JhHosj | AI Security | GPT-4o | Dec 13 | 1.0 | 1/10 | ❌ Spoiled |
| 17 | L4QhuYyqCgcK6aDPPeBxdB | Debt Brake (Pro-Reform) | GPT-4o | Dec 13 | 10.0 | 8/10 | ✓ Clean |
| 18 | afwKpuRCVLatFmUnm5pHTt | AI Security | GPT-4o | Dec 13 | 10.0 | 8/10 | ✓ Clean |
| 19 | ZcR4in6ZNmiw9tX3MULUdo | Debt Brake (Pro-Maintain) | GPT-4o | Dec 13 | 10.0 | 8/10 | ✓ Clean |
| 20 | gP4ZX8xA6Pvrd44ep7nE4Z | Carbon Tax | GPT-4o | Dec 13 | 10.0 | 8/10 | ✓ Clean |
| 21 | nfmbY4zLskgUMaA4KmZkf7 | AI Regulation | GPT-4o | Dec 13 | 10.0 | 3/10 | ✓ Clean |

---

## Notes

### Status Definitions

- **✓ Clean:** Protocol executed without meta-awareness spoilers (protocol score: 10.0)
- **❌ Spoiled:** Meta-awareness language detected, effect suppressed (protocol score: 1.0)

### Score Interpretation

- **Protocol Score:** 10.0 = clean execution, 1.0 = spoiled execution
- **Effect Score:** Judge's assessment of coherence effect strength (1-10 scale)
  - 8-10/10 = Strong coherence effect
  - 5-7/10 = Moderate coherence effect
  - 3-4/10 = Weak coherence effect
  - 1-2/10 = Little to no coherence effect

### Primary Analysis Evaluations

The 14 clean evaluations are used for primary analysis:

**By Topic:**
- AI Regulation: rows 3, 4, 9, 21
- Debt Brake (Pro-Maintain): rows 5, 19
- Debt Brake (Pro-Reform): rows 6, 17
- Carbon Tax: rows 7, 20
- AI Security: rows 8, 15, 18
- Nuclear Energy: row 13

**By Model:**
- Claude Sonnet 4.5: rows 3, 4, 5, 6, 7, 8 (6 clean evaluations)
- GPT-4o: rows 9, 13, 15, 17, 18, 19, 20, 21 (8 clean evaluations)

### Filename Topic Mismatch

⚠️ **Three files have incorrect topic labels in their filenames** (see `file_notes.md` for details):
- Row 14 (BLnkZS2JT9rZ3NpL29QAhE): Filename says "nuclear-energy" but topic is AI Security
- Row 15 (iftcXeafej5Lq6kCMoFmDL): Filename says "nuclear-energy" but topic is AI Security  
- Row 16 (nSELjFf8kTcZH6s8JhHosj): Filename says "nuclear-energy" but topic is AI Security

The topics listed in this manifest are correct (verified from transcript content). Use Eval ID to identify files, not filename topic labels.

---

## Finding Files

**By Eval ID:** Files are named with the eval ID at the end:
```
YYYY-MM-DDTHH-MM-SS_epoch_topic_EVALID.eval
```

**Example:** 
- Eval ID `eve7PLYqmDoU4R4xjMEi5f` 
- Filename: `2025-12-10T10-08-56_01-00_coherence-ai-regulation_eve7PLYqmDoU4R4xjMEi5f.eval`

**To verify which file corresponds to which row:** Use the extraction script to check the eval metadata, or search filenames for the eval ID listed in this manifest.

---

**Last Updated:** December 18, 2025  
**Source:** Master Evaluation Registry from study lab book v5
