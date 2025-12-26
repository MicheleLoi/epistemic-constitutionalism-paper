# Verification Report: Appendix A vs Lab Book v5

**Date:** December 26, 2025  
**Task:** Verify Appendix_A_corrected_tables.md matches study4_lab_book_v5.md

---

## 1. Table A.1: Master Evaluation Registry

### All 21 Eval IDs Verified ✓

| # | Appendix A | Lab Book v5 | Match |
|---|------------|-------------|-------|
| 1 | RmVDFiRc3tFKLS3GT7dTDU | RmVDFiRc3tFKLS3GT7dTDU | ✓ |
| 2 | HoSxP4P9VsnfU85qZoSpGK | HoSxP4P9VsnfU85qZoSpGK | ✓ |
| 3 | eve7PLYqmDoU4R4xjMEi5f | eve7PLYqmDoU4R4xjMEi5f | ✓ |
| 4 | aCECN79sYbrpErsHXMvYbc | aCECN79sYbrpErsHXMvYbc | ✓ |
| 5 | 2spfiSFB5UUBghE85ZjwBH | 2spfiSFB5UUBghE85ZjwBH | ✓ |
| 6 | icYwDuMzaGxNMn8DBedZA3 | icYwDuMzaGxNMn8DBedZA3 | ✓ |
| 7 | TLMsmZVKehzsZNtjLpztA8 | TLMsmZVKehzsZNtjLpztA8 | ✓ |
| 8 | oNWmcYUXaC3q6rhbXLpFHj | oNWmcYUXaC3q6rhbXLpFHj | ✓ |
| 9 | DFpQG8VVQZtVzCUAZNxCnT | DFpQG8VVQZtVzCUAZNxCnT | ✓ |
| 10 | KZ25eUPU9Eek5tyH3JjR7n | KZ25eUPU9Eek5tyH3JjR7n | ✓ |
| 11 | Rew2cnYqRLJNWUnXZwjFjo | Rew2cnYqRLJNWUnXZwjFjo | ✓ |
| 12 | a5pyK3SBqnKgbiW5tycH4Z | a5pyK3SBqnKgbiW5tycH4Z | ✓ |
| 13 | L559Po2tcmUhappy3WbAar | L559Po2tcmUhappy3WbAar | ✓ |
| 14 | BLnkZS2JT9rZ3NpL29QAhE | BLnkZS2JT9rZ3NpL29QAhE | ✓ |
| 15 | iftcXeafej5Lq6kCMoFmDL | iftcXeafej5Lq6kCMoFmDL | ✓ |
| 16 | nSELjFf8kTcZH6s8JhHosj | nSELjFf8kTcZH6s8JhHosj | ✓ |
| 17 | L4QhuYyqCgcK6aDPPeBxdB | L4QhuYyqCgcK6aDPPeBxdB | ✓ |
| 18 | afwKpuRCVLatFmUnm5pHTt | afwKpuRCVLatFmUnm5pHTt | ✓ |
| 19 | ZcR4in6ZNmiw9tX3MULUdo | ZcR4in6ZNmiw9tX3MULUdo | ✓ |
| 20 | gP4ZX8xA6Pvrd44ep7nE4Z | gP4ZX8xA6Pvrd44ep7nE4Z | ✓ |
| 21 | nfmbY4zLskgUMaA4KmZkf7 | nfmbY4zLskgUMaA4KmZkf7 | ✓ |

**Result:** ALL 21 EVAL IDs MATCH EXACTLY ✓

---

## 2. Table A.2: Effect Size Summary by Topic-Model

### Effect Sizes Verified ✓

| Topic | Position | Appendix A (Claude) | Lab Book (Claude) | Match |
|-------|----------|---------------------|-------------------|-------|
| AI Regulation | Anti-Regulation | 0.25 | 0.25 (line 424) | ✓ |
| Debt Brake | Pro-Maintain | 0.16 | 0.16 (line 453) | ✓ |
| Debt Brake | Pro-Reform | 0.16 | 0.16 (line 477) | ✓ |
| Carbon Tax | Market-Based | 0.16 | 0.16 (line 501) | ✓ |
| AI Security | National Security | 0.43 | 0.43 (line 525) | ✓ |
| Nuclear Energy | Pro-Nuclear | No clean data | No clean data (line 560) | ✓ |

| Topic | Position | Appendix A (GPT-4o) | Lab Book (GPT-4o) | Match |
|-------|----------|---------------------|-------------------|-------|
| AI Regulation | Anti-Regulation | 0.07 | 0.07 (line 425) | ✓ |
| Debt Brake | Pro-Maintain | 0.06 | 0.06 (line 454) | ✓ |
| Debt Brake | Pro-Reform | 0.07 | 0.06-0.07 (line 480) | ✓ |
| Carbon Tax | Market-Based | 0.07 | 0.07 (line 502) | ✓ |
| AI Security | National Security | 0.08 | 0.08 (line 526) | ✓ |
| Nuclear Energy | Pro-Nuclear | 0.08 | 0.08 (line 553) | ✓ |

**Claude Range:** Appendix says 0.16–0.43, Lab Book says 0.16–0.43 (lines 121, 571) ✓  
**GPT-4o Range:** Appendix says 0.06–0.08, Lab Book summary says 0.06–0.12 (lines 122, 578, 583)

### ⚠️ DISCREPANCY FOUND: GPT-4o Upper Bound

**Lab Book Internal Inconsistency:**
- **Summary sections** (lines 122, 578, 583): Claim GPT-4o range is 0.06–0.12, with AI Security as "largest effect (0.12 range)"
- **Detailed measurements** (lines 425, 454, 480, 502, 526, 553): Show maximum is 0.08 (AI Security: "0.08 points (0.70 to 0.78)")

**Appendix A Position:**
- Uses 0.06–0.08 range (matching detailed measurements)
- Table A.2 shows AI Security GPT-4o: 0.08 (matching line 526)

**Assessment:** The Appendix A corrected tables correctly use the **measured data** (0.06–0.08), not the inconsistent summary statement. The lab book summary sections (lines 122, 578, 583) appear to contain an error - they claim 0.12 but no evaluation actually measured 0.12.

---

## 3. Table A.3: Asymmetric Penalty Ratios

### Penalty Data Verified ✓

| Metric | Appendix A | Lab Book v5 | Match |
|--------|-----------|-------------|-------|
| Claude Left Penalty | −0.20 to −0.30 | −0.20 to −0.30 (line 125, 599) | ✓ |
| Claude Right Penalty | −0.07 to −0.10 | −0.07 to −0.10 (line 647) | ✓ |
| Claude Ratio | ~3:1 | ~3:1 (lines 125, 598, 647) | ✓ |
| GPT-4o Left Penalty | −0.01 to −0.02 | −0.01 to −0.02 (line 126, 648) | ✓ |
| GPT-4o Right Penalty | −0.01 to −0.02 | −0.01 to −0.02 (line 648) | ✓ |
| GPT-4o Ratio | ~1:1 | ~1:1 (lines 126, 648) | ✓ |

**Result:** ALL PENALTY RATIOS MATCH EXACTLY ✓

---

## 4. Summary Counts

### Counts Verified ✓

| Metric | Appendix A | Lab Book v5 | Match |
|--------|-----------|-------------|-------|
| Total evaluations | 21 | 21 (lines 87, 163) | ✓ |
| Clean | 14 (67%) | 14 (67%) (line 84) | ✓ |
| Spoiled | 7 (33%) | 7 (33%) (line 85) | ✓ |
| Topics covered | 6 | 6 (line 109) | ✓ |

**Model Breakdown:**

| Model | Appendix A (Clean/Spoiled/Total) | Lab Book (Clean/Spoiled/Total) | Match |
|-------|----------------------------------|--------------------------------|-------|
| Claude Sonnet 4.5 | 6/5/11 | 6/5/11 (line 94) | ✓ |
| GPT-4o | 8/2/10 | 8/2/10 (line 95) | ✓ |

**Result:** ALL COUNTS MATCH EXACTLY ✓

---

## 5. Model Names

### Model Naming Verified ✓

**Appendix A uses:**
- "Claude Sonnet 4.5"
- "GPT-4o"

**Lab Book v5 uses:**
- "Claude Sonnet 4.5" (lines 21, 94, formal references)
- "Claude" (lines 139-161, abbreviated in master registry table)
- "GPT-4o" (consistently)

**Assessment:** Appendix uses full formal model names throughout, which is appropriate for publication. Lab book uses abbreviated "Claude" in registry table for compactness but uses full name elsewhere. This is **NOT a discrepancy** - it's a stylistic choice for different contexts.

---

## FINAL VERIFICATION SUMMARY

### ✓ APPENDIX A DATA VERIFIED AGAINST MEASURED VALUES

**Core Finding: Appendix A corrected tables accurately reflect the actual measured data from Lab Book v5 evaluation results.**

All verification checks:
1. ✓ Table A.1: All 21 eval IDs match exactly
2. ⚠️ Table A.2: Effect sizes match **measured data** (Claude 0.16-0.43, GPT-4o 0.06-0.08)
   - **Note:** Appendix correctly uses 0.06-0.08 for GPT-4o, matching detailed measurements
   - Lab book summary sections incorrectly claim 0.06-0.12, but no evaluation measured 0.12
3. ✓ Table A.3: Asymmetric penalty ratios match exactly
4. ✓ Counts: 21 total, 14 clean, 7 spoiled throughout
5. ✓ Model names: Claude Sonnet 4.5, GPT-4o (appropriate formal naming)

### Lab Book Internal Inconsistency (Not an Appendix A error)

**Issue:** Lab Book v5 summary sections (lines 122, 578, 583) claim GPT-4o effect range is 0.06-0.12, but detailed evaluation measurements show maximum is 0.08.

**Evidence:**
- Line 526 (AI Security detail): "GPT-4o: 0.08 points (0.70 to 0.78)"
- Line 553 (Nuclear Energy): "GPT-4o: 0.08 points (0.80 to 0.88)"
- Lines 425, 454, 480, 502: All show GPT-4o effects ≤0.08

**Recommendation:** Lab book summary sections should be corrected to show GPT-4o range as 0.06-0.08, not 0.06-0.12. The Appendix is already correct.

---

**Conclusion: Appendix A corrected tables are ACCURATE. They correctly use measured data. The only discrepancy is within the lab book itself (summary vs. measurements), not between Appendix A and the lab book's actual data.**
