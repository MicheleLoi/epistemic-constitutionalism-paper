# Reference Log: Section 2

**Document Type:** Type 6 (Reference Log)  
**Section:** 2 - The Finding  
**Last Updated:** December 24, 2025

---

## Citations Used in Section 2

### Petri Framework

**Anthropic (2025) - Petri**  
- Full citation: Anthropic. (2025, October 6). Petri: An open-source auditing tool to accelerate AI safety research. *Alignment Research Blog*. https://alignment.anthropic.com/2025/petri/
- Alternative URL: https://www.anthropic.com/research/petri-open-source-auditing
- GitHub: https://github.com/safety-research/petri
- Release date: October 6, 2025
- Usage: Core methodological framework for all evaluations
- Context: "The evaluations used Petri, an alignment auditing framework released by Anthropic in October 2025."
- Key points referenced:
  - Three-model architecture (auditor, target, judge)
  - Rollback mechanism for condition testing
  - Design philosophy: "rapid hypothesis testing," "discover misaligned behaviors," "automated auditing"
  - Built on UK AISI's Inspect framework
  - Default 36-dimension scoring rubric
- Full description from source: "Petri (Parallel Exploration Tool for Risky Interactions), an open-source framework for automated auditing that uses AI agents to test the behaviors of target models across diverse scenarios."
- Design philosophy: "Petri is designed for rapid hypothesis testing, helping researchers quickly identify misaligned behaviors that warrant deeper investigation" and "makes it possible to test many individual hypotheses about how a model might behave in some new circumstance with only minutes of hands-on effort."
- Status: **Citation complete**

---

## Data and Code Availability

### GitHub Repository

**Our repository:**
- Location: MicheleLoi/source-attribution-bias-data
- Contents: All 21 evaluation files (.eval format), complete transcripts, rating distributions, judge scores, extraction scripts
- Status: Publicly available, referenced in text but not formally cited
- Usage: "All evaluation data are publicly available at the GitHub repository MicheleLoi/source-attribution-bias-data"

**Note:** This is our own data repository, not a citation to external work. Standard practice is to include data availability statement but not cite your own data as a reference.

---

## Internal Documentation (Not Cited)

### Lab Book
- File: study4_lab_book_v5.md
- Status: Internal research documentation
- Disposition: Not included in formal references; documented in research materials

### Epistemic Traces
- Trace 8: Protocol development (December 7, 2025)
- Trace 14: Study 4 debugging session (December 10, 2025)
- Status: Research process documentation
- Disposition: Will be included in Appendix B but not formal references

### Extraction Scripts
- extract_data.py: Verification script for rating distributions
- extract_petri.py: Methodology illustration script
- Status: Available in GitHub repository
- Disposition: Code availability, not citations

---

## Citations from Section 1 Referenced in Section 2

None directly cited, but Section 2 builds on:
- Germani & Spitale (2025) - mentioned in Introduction as predecessor study
- Mercier's epistemic vigilance - will be developed in later sections

---

## Running Bibliography (APA Format)

Anthropic. (2025, October 6). Petri: An open-source auditing tool to accelerate AI safety research. *Alignment Research Blog*. https://alignment.anthropic.com/2025/petri/

---

**Document Status:** Complete  
**Next Update:** After Section 3
