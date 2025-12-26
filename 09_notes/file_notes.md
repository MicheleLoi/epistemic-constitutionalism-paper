# File Inventory Notes

## Filename Topic Labels

Three evaluation files have topic labels in their filenames that do not match the actual topic tested in the evaluation. This is a Petri naming bug. The actual topics have been verified by examining the complete transcripts within each file.

### Files Affected

| Filename | Filename Topic Label | Actual Topic (Verified) | Eval ID |
|----------|---------------------|------------------------|---------|
| `2025-12-13T09-44-39_01-00_coherence-nuclear-energy_BLnkZS2JT9rZ3NpL29QAhE.eval` | nuclear_energy | **AI Security** | BLnkZS2JT9rZ3NpL29QAhE |
| `2025-12-13T09-53-27_01-00_coherence-nuclear-energy_iftcXeafej5Lq6kCMoFmDL.eval` | nuclear_energy | **AI Security** | iftcXeafej5Lq6kCMoFmDL |
| `2025-12-13T10-08-00_01-00_coherence-nuclear-energy_nSELjFf8kTcZH6s8JhHosj.eval` | nuclear_energy | **AI Security** | nSELjFf8kTcZH6s8JhHosj |

### Verification Method

The actual topic for each evaluation can be verified by:

1. Extracting the `.eval` file (it's a zip archive)
2. Opening `samples/1_epoch_1.json`
3. Reading the `input` field (seed instructions) or `messages` array (transcript)
4. The argument topic is clearly stated in the experimental protocol text

### Impact

- The evaluation data itself is correct and complete
- File naming does not affect data integrity
- All analyses reference evaluations by Eval ID, not filename
- Users should verify topic from transcript content, not filename

### Example Verification (Python)

```python
import json
import zipfile

# Check actual topic in file
with zipfile.ZipFile('2025-12-13T09-44-39_01-00_coherence-nuclear-energy_BLnkZS2JT9rZ3NpL29QAhE.eval', 'r') as z:
    z.extractall('check/')
    
with open('check/samples/1_epoch_1.json') as f:
    data = json.load(f)
    # Read the seed instructions
    print(data['input'][:500])
    # Will show "AI security" argument, not nuclear energy
```

---

## File Count Reconciliation

- **Total evaluation files:** 21
- **Unique Eval IDs:** 21
- **No duplicate files**
- **No missing files**

All evaluations conducted during the study are present in the repository.

---

**Note:** These are documentation/tracking clarifications only. The evaluation data files themselves are complete, valid, and unmodified.
