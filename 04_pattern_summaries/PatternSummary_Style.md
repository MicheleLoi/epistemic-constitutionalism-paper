# Pattern Summary: Style (De-Claude-ification)

**Document Type:** Pattern Summary
**Scope:** Whole paper
**Generated:** January 15, 2026
**Status:** Active reference during style pass

---

## Purpose

Identify AI-writing patterns that make prose sound "Claude-like" and specify improvement strategies. Patterns logged once here; not repeated in section logs.

---

## Identified Patterns

### Pattern S1: Choppy Declarative Openers/Closers

**Description:** Very short sentences used for dramatic emphasis, especially at paragraph starts or ends.

**Examples:**
- "AI systems reason."
- "It is not."
- "How they do this matters."

**Problem:** Creates staccato rhythm; reads as assertion-list rather than flowing argument.

**Fix:** Join to adjacent sentence with colon, semicolon, or dash. Or fold into previous sentence as clause.

| Before | After |
|--------|-------|
| "AI systems reason. They construct..." | "AI systems reason: they construct..." |
| "...neutral default. It is not." | "...neutral default, which it is not." |

---

### Pattern S2: Colon-Then-Fragment

**Description:** Colon followed by short phrase or imperative, rather than full clause.

**Examples:**
- "The reflexive answer is: eliminate it."
- "The question then becomes: what kind of epistemic constitution?"

**Problem:** Creates punchy, listicle feel. Fine occasionally; tiresome when repeated.

**Fix:** Convert to full sentence or use infinitive construction.

| Before | After |
|--------|-------|
| "The reflexive answer is: eliminate it." | "The reflexive answer is to eliminate it entirely." |
| "The question then becomes: what kind..." | "The question, then, is what kind of epistemic constitution to design." |

---

### Pattern S3: Missing Connectives

**Description:** Sentences follow each other without logical connectors (however, moreover, rather, consequently, on this view, in other words).

**Examples:**
- "Yet their belief-forming behavior..." (could be "And yet")
- "Source information can legitimately inform..." (could be "On this view, source information...")

**Problem:** Prose reads as sequence of independent assertions rather than connected argument.

**Fix:** Add light connectives where logical relationship exists.

| Relationship | Connectives to consider |
|--------------|------------------------|
| Contrast | "and yet," "but," "however," "rather" |
| Addition | "moreover," "furthermore," "in addition" |
| Consequence | "consequently," "as a result," "thus" |
| Clarification | "in other words," "that is," "on this view" |
| Concession | "granted," "to be sure," "admittedly" |

---

### Pattern S4: Parallel Triads

**Description:** Three-item lists with parallel structure, often verbs or noun phrases.

**Examples:**
- "they evaluate arguments, assign credibility, and express confidence"
- "implicitly, asymmetrically, and in ways they suppress"

**Problem:** Signature AI rhythm. Not always wrong, but overuse is diagnostic.

**Fix:** Varies by case. Options:
- Keep if genuinely three distinct items
- Collapse to two items if third is padding
- Rephrase without list structure
- Vary list length (two items, four items) across paper

**Note:** Not always a problem. Use judgment. Fix only when it feels mechanical.

---

### Pattern S5: Repetitive Sentence Structure

**Description:** Multiple sentences with same Subject-Verb-Object or "The X approach..." pattern.

**Examples:**
- "The Platonic approach mandates... The Liberal approach refuses..."
- Sequences of "This [noun]..." openers

**Problem:** Creates monotonous rhythm.

**Fix:** Vary sentence openers. Use:
- Subordinate clauses first ("Drawing on Mercier's theory,...")
- Prepositional phrases ("On this view,...")
- Participle phrases ("Rather than mandating...,")

---

## Improvement Strategies

### Strategy 1: Join choppy sentences
Use colons, semicolons, dashes, or subordination to connect related short sentences.

### Strategy 2: Add light connectives
Insert "and yet," "rather," "on this view," "in other words" where logical relationships exist but aren't marked.

### Strategy 3: Vary punctuation
Alternate between colons, dashes, semicolons, and commas to avoid monotony. Each has different weight:
- Colon: announces, sets up
- Dash: interrupts, adds
- Semicolon: balances, parallels
- Comma: flows, subordinates

### Strategy 4: Fold fragments
Short dramatic sentences often work better as clauses within adjacent sentences.

### Strategy 5: Vary sentence openers
Start some sentences with subordinate clauses, prepositional phrases, or adverbs rather than always Subject-Verb.

---

## Non-Problems (Do Not Fix)

- **Clarity over elegance:** If a short sentence is genuinely clear and emphatic, keep it.
- **Technical precision:** Don't sacrifice accuracy for flow.
- **Analytic style:** The goal is not literary prose; connectives should be functional, not ornamental.
- **Occasional triads:** Three-item lists are fine when genuinely three items.

---

## Usage

When editing each section:
1. Scan for patterns S1-S5
2. Apply relevant fix
3. Log in PaperModificationLog_Style.md
4. Do not re-document the pattern; reference this summary
