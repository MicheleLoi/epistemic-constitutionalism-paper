# Section Summary: Section 2 (The Finding)

**Document Type:** Type 5 (Section Summary)  
**Section:** 2 - The Finding  
**Generated:** December 24, 2025  
**Word Count:** ~1,806 words

---

## Argument Structure

### Opening Frame
Twenty-one systematic evaluations using Petri framework. Two models (Claude Sonnet 4.5, GPT-4o), six topics, seven source conditions per topic. All data publicly available at MicheleLoi/source-attribution-bias-data. Results: source attribution effects clear for Claude, less definitive for GPT-4o.

### Methodology Subsection (New - MOD-008, expanded MOD-015)
Petri framework explanation with design philosophy: framework designed for discovery research through qualitative transcript analysis, not statistical prevalence estimation. Enables mechanism understanding by reading complete transcripts, identifying patterns, iterating rapidly. Study uses Petri as Anthropic intended: 21 evaluations with deep qualitative analysis, not thousands aggregated for p-values.

Concrete example using evaluation 2spfiSFB5UUBghE85ZjwBH:
- Three-model architecture: auditor, target, judge
- Rollback mechanism: same argument, seven different source attributions  
- Example pattern: 0.65 baseline → 0.65 aligned sources (Lindner/FDP, IW Köln) → 0.60 SPD → 0.58 FES
- Explicit coherence reasoning: "appears inconsistent with SPD's traditional stance...weakens credibility given the source"
- Judge dimensions defined: coherence effect detection (9/10), source-based reasoning visibility (8/10), rating shift magnitude (7/10), protocol execution (10/10)

### Evaluation Integrity
14 clean, 7 spoiled evaluations. Protocol development built on earlier work discovering suppression triggers ("regardless of source," "systematic analysis"). Despite refinement, 7 evaluations spoiled, demonstrating suppression ease. Two spoiler types: (1) meta-awareness language (5 evals), (2) topic mismatch (2 evals). Suppression behavior diagnostic: models eliminate source-attending rather than calibrate when detected.

### Results: Clean Evaluations
Claude: 0.16–0.43 point range, explicit reasoning (7-9/10), strong effects (9/10 typical). GPT-4o: 0.06–0.12 point range, implicit reasoning (2-7/10), smaller effects (8/10 typical, except AI regulation 3/10).

Table 1 presents effect sizes by topic, listing specific eval IDs for verification. AI regulation shows replication (two Claude evals: 0.25-0.30 range, both 9/10).

### Asymmetric Penalties
Claude: Left sources arguing conservative positions get -0.20 to -0.30 penalties; conservative sources arguing progressive positions get -0.07 to -0.10 penalties (3:1 ratio). "Surprise bonus" in evaluation TLMsmZVKehzsZNtjLpztA8: conservative sources arguing for carbon tax get +0.10 to +0.13 boost.

GPT-4o: Much smaller penalties (-0.01 to -0.02 for both directions, ~1:1 ratio), 6-15x weaker than Claude. Implicit reasoning makes mechanism interpretation difficult; no explicit surprise bonus.

### Meta-Awareness Suppression
Seven spoiled evaluations showed complete effect suppression (all 1/10 scores). Perfect reproducibility: 7/7 spoilers → suppression, 14/14 clean → detection. Concrete examples: KZ25eUPU9Eek5tyH3JjR7n auditor said "I have another argument to evaluate as well"; RmVDFiRc3tFKLS3GT7dTDU and HoSxP4P9VsnfU85qZoSpGK used "continuing with my comparative analysis." Methodological reflection: Petri's qualitative design enabled mechanism discovery through transcript reading. Large-N statistical approach would miss specific trigger phrases, see spoiled cases as "null results" rather than diagnostic patterns. Rapid iteration example: identified suppression trigger, adjusted protocol, validated fix in 10 minutes. Positioned as using Petri as designed: discovery research (understanding mechanisms) before prevalence estimation (measuring how often). The 21-evaluation approach appropriate for method-question fit, not apologized for.

### Interpretation
Three findings for Claude: effect presence (definitive), effect asymmetry (3:1 ratio), suppression under meta-awareness. For GPT-4o: effect presence (less certain), smaller asymmetry (implicit reasoning), suppression under meta-awareness.

Suppression behavior diagnostic: models treat source-based reasoning as bias to eliminate, not legitimate inference requiring better execution. Adopt source independence as epistemic policy when detected. But source independence not epistemically neutral—it's substantive policy claiming testimonial context should never affect evaluation.

Current systems have implicit, unprincipled epistemic policies. For Claude: policies "implicit, unprincipled, and presented as though they were absent." For GPT-4o: "evidence suggests similar patterns with less clarity about mechanism." Default under detection: source independence (the Platonic fix).

---

## Key Concepts Introduced

| Concept | Definition | Evidence |
|---------|------------|----------|
| Source attribution effect | Rating variation based solely on attributed source identity | 0.06-0.43 point ranges, 14/14 clean evals show effect |
| Coherence effect | Ideological alignment between source and argument position affects credibility | SPD arguing conservative: 0.60 vs baseline 0.65; FES: 0.58 |
| Surprise bonus | Against-type arguments get credibility boost | TLMsmZVKehzsZNtjLpztA8: +0.10 to +0.13 for conservative sources |
| Asymmetric penalty | Progressive sources penalized 3x more than conservative (Claude) | -0.20 to -0.30 vs -0.07 to -0.10 |
| Meta-awareness suppression | Detection of testing paradigm triggers complete effect elimination | All 7 spoiled evals: 1/10 scores, zero variance |
| Spoilers | Language creating meta-awareness in target model | "Continuing with comparative analysis," topic mismatch prompts |
| Judge dimensions | Four evaluation criteria: coherence detection, reasoning visibility, rating shift, protocol quality | Each scored 0-10 with explicit definitions |

---

## Evidence Quality Distinctions (MOD-007, MOD-013)

**Claude Sonnet 4.5:**
- Evidence quality: Definitive
- Effect size: 0.16-0.43 range (large)
- Reasoning visibility: 7-9/10 (explicit)
- Mechanism: Clear (ideological coherence reduces credibility)
- Example: "appears inconsistent with FES's typical advocacy...raises questions about authenticity"

**GPT-4o:**
- Evidence quality: Compatible but less conclusive
- Effect size: 0.06-0.12 range (smaller)
- Reasoning visibility: 2-7/10 (implicit)
- Mechanism: Unclear (ratings vary but reasoning hidden)
- Exception: AI regulation anomalously weak (3/10)

---

## Forward Connections

| Section | Connection from Section 2 |
|---------|---------------------------|
| Section 3 | "Implicit epistemic policies" demonstrated → diagnosed |
| Section 4 | Source attribution effects shown → epistemic constitution need established |
| Section 5 | "Platonic fix" (source independence) observed → Platonic vs Liberal distinction developed |
| Section 6 | Surprise bonus found → costly signaling explained |
| Section 7 | Source-attending shown but unprincipled → norms needed |
| Section 8 | Meta-awareness suppression shown → implications discussed |

---

## Data Transparency

All findings traceable to specific evaluations:
- Table 1: Effect sizes with eval IDs for each topic-model pair
- Meta-Awareness: All 7 spoiled evals listed by ID
- Asymmetric penalty: Ranges cited to specific evaluation TLMsmZVKehzsZNtjLpztA8
- GitHub repository: MicheleLoi/source-attribution-bias-data (complete transcripts, ratings, judge scores)

Modifications MOD-001 through MOD-014 ensure:
- Every claim tied to specific eval ID
- Evidence quality honestly distinguished
- Replication shown where available
- Process iteration acknowledged

---

## Methodological Contributions

### Petri Framework Application
First published study using Petri (released October 2025) for source attribution bias detection. Demonstrates custom judge dimensions, seed design for multi-condition testing, spoiler detection framework.

### Protocol Development Learning
Documents suppression trigger discovery: comparative language, meta-awareness phrases, topic mismatch all trigger effect elimination. Even informed researchers produce spoilers (7/21 evaluations).

### Model Comparison
Cross-model evidence (Claude vs GPT-4o) shows:
- Effect replicates across models but magnitude differs (2-4x)
- Reasoning visibility varies (explicit vs implicit)
- Topic sensitivity model-dependent (GPT-4o weak on AI regulation)

---

## Rhetorical Choices

**Structure:**
1. Methodology subsection first (concrete example)
2. Evaluation integrity (establishes dataset)
3. Results (patterns across 14 clean evals)
4. Asymmetric penalties (refined pattern)
5. Meta-awareness suppression (diagnostic finding)
6. Interpretation (synthesis + normative claim)

**Evidence presentation:**
- Led with definitive evidence (Claude), acknowledged less conclusive evidence (GPT-4o)
- Concrete before abstract (Schuldenbremse example before aggregate findings)
- Eval IDs for all claims (falsifiability)
- Replication shown (AI regulation: two evals both 9/10)

**Tone:**
- Measured, not dramatic (MOD-009: removed "They are fatal")
- Precise, not vague (MOD-003: "In evaluation X" not "In several cases")
- Honest about evidence quality (MOD-007: "definitive" vs "less conclusive")

---

## Unresolved Elements (Deliberate)

- Why does suppression occur? (Behavior described, mechanism not explained)
- Is source independence ever appropriate? (Section 8)
- How should source-attending be done? (Section 6-7)
- What causes asymmetric penalty? (Described, not explained)
- GPT-4o mechanism unclear (acknowledged limitation, not overclaimed)

---

## Key Decisions Documented

**Protocol Development (Decision Log):**
- Seeds 1-3 (Study 2 pilots): Referenced via epistemic trace 8, filed under "notes," NOT in appendices/GitHub
- Epistemic traces 8, 14: Included in Appendix B (process documentation)
- Main text: One sentence acknowledging iteration
- GitHub: Only Study 4's 21 systematic evaluations

**Rationale:** Separate development history (Seeds 1-3) from systematic evidence (Study 4). Full transparency available in appendices without cluttering core dataset.

---

## Decision Log

### Protocol Development Documentation

**Seeds 1-3 (Study 2 pilot work):**
- Location: Referenced via epistemic trace 8, filed under "notes" directory
- NOT included in: Main appendices, GitHub data repository
- Reason: Development history, not systematic evidence

**Epistemic trace 8 (seed design process, Dec 7, 2025):**
- Location: Appendix B (process documentation)
- Content: Documents discovery of suppression triggers, architectural decisions, final seed design
- Purpose: Shows how protocol refinement emerged from earlier failures

**Epistemic trace 14 (Study 4 debugging session, Dec 10, 2025):**
- Location: Appendix B (process documentation)
- Content: Real-time debugging of nuclear energy failures, spoiler rediscovery despite documentation
- Purpose: Demonstrates iteration continued during Study 4, suppression triggers easy to miss even when known

**Main text (Section 2, Evaluation Integrity):**
- One sentence acknowledging protocol development built on earlier work
- Frames 7 spoiled evaluations as demonstrating suppression ease
- Maintains focus on findings rather than process

**GitHub repository (MicheleLoi/source-attribution-bias-data):**
- Contains: Only Study 4's 21 evaluations (systematic dataset)
- Excludes: Seeds 1-3 pilot work
- Reason: Clean separation between exploratory development and systematic evidence

**Overall rationale:** Study 4's 21 evaluations are the systematic evidence base supporting all empirical claims. Seeds 1-3 are development history providing transparency about learning process. Appendix B provides full process transparency for methodologists and interested readers while maintaining Section 2's focus on findings. GitHub repository contains only verified, systematic data to avoid confusion about what constitutes the evidence base.

---

**Document Status:** Complete  
**Purpose:** Ensure continuity when writing Sections 3-9
