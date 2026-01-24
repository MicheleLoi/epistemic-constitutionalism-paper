---
created: 2026-01-24
source_chat: Claude Code session (cross-project from Guidance for Policymakers)
model: Claude Opus 4.5
status: completed
---

# Related Work Analysis: Kasirzadeh & Gabriel (2022)

## Paper
Kasirzadeh, A., & Gabriel, I. (2022). In conversation with Artificial Intelligence: Aligning language models with human values. *arXiv preprint arXiv:2209.00731*.

## Summary
K&G develop a framework for AI alignment through conversational norms—applying Gricean maxims (quantity, quality, relation, manner) and speech act theory (assertives, directives, expressives, performatives, commissives) to specify how AI systems should communicate.

## Relationship to This Paper

### Apparent Overlap
Both papers:
- Address norms for AI systems
- Use "constitution" framing
- Concern belief/assertion behavior

### Actual Distinction
The papers address different questions:

| Dimension | Kasirzadeh & Gabriel | This paper |
|-----------|---------------------|------------|
| Focus | Output norms (communication) | Input norms (belief formation) |
| Question | How should AI speak? | How should AI form beliefs? |
| Framework | Gricean maxims, speech acts | Epistemic vigilance, costly signaling |
| Domain | Conversational cooperation | Testimonial evaluation |

### Priority Claim
Epistemic constitution is prior to conversational norms: you cannot speak well about what you have not thought well about. An AI that follows perfect Gricean maxims while forming beliefs through unprincipled source-attending would be a fluent speaker of badly-formed judgments.

### Complementarity
The frameworks are complementary, not competing:
- K&G: how to express beliefs appropriately
- This paper: how to form beliefs appropriately
- Both needed for complete alignment

## Accommodation Strategy
Citation added to Section 4 ("The Design Question") acknowledging K&G's conversational norms approach while positioning epistemic constitution as the foundational framework that must precede conversational norms.

**Note:** This is a post-publication change. Original paper published as arXiv:2601.14295v1 on 2026-01-24.

## Edit Made
See: `03_modification_logs/ModificationLog_Section4.md` (MOD-010)
