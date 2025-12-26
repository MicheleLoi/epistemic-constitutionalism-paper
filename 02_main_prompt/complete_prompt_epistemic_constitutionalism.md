# Complete Prompt: Epistemic Constitutionalism for AI

**Document Type:** Type 1 (Complete Prompt)  
**Generated:** December 18, 2025  
**Source:** Prompt Development Log (conversation with Claude Opus 4.5)  
**Purpose:** Govern paper writing across all sections

---

## I. Paper Identity

**Working Title Direction:**  
"Epistemic Constitutionalism for AI: From Source Attribution Bias to Liberal Norms for Artificial Reasoners"

(Alternatives to consider: foreground "epistemic vigilance" or "beyond platonic reason"—final title after draft)

**Target Length:** 8,000–10,000 words (excluding appendices)

**Venue Positioning:**  
- Primary: arXiv (AI/alignment + philosophy cross-list)
- Secondary: Philosophy & Technology, AI & Ethics, or alignment workshop
- Tone calibrated for: researchers who know Constitutional AI, some philosophy, empirical sensibility

**Audience:**  
- AI alignment researchers familiar with Constitutional AI (Anthropic)
- Philosophers interested in AI epistemics
- Researchers using evaluation frameworks (Petri, Inspect)
- Not: general public, not pure ML audience

---

## II. Core Argument Architecture

The paper makes one central claim with supporting structure:

**Central Claim:**  
AI systems need an *epistemic* constitution—explicit meta-norms governing how they form and express beliefs—analogous to Constitutional AI's ethical constraints.

**Argument Flow:**

1. **Problem**: AI systems reason epistemically but lack explicit norms governing that reasoning. Current systems have implicit epistemic policies that are unprincipled.

2. **Evidence**: Empirical demonstration that AI systems exhibit source attribution effects that are (a) present but hidden, (b) asymmetric, (c) suppressed under meta-awareness. This reveals implicit epistemic policies.

3. **Solution Concept**: The epistemic constitution—extending Constitutional AI from ethics to epistemology.

4. **Design Choice**: Two fundamentally different approaches to epistemic constitution design:
   - *Platonic*: Mandate formal correctness, source independence, truth-correspondence
   - *Liberal*: Protect conditions for collective inquiry, procedural norms, reasonable rejectability

5. **Resolution**: The empirical finding shows why platonic fails. Source information *matters* epistemically (Mercier's epistemic vigilance). The question is not whether to attend to sources but *how*. Liberal norms—including principled source-attending based on costly signaling—are needed.

6. **Contribution**: Sketch of source-attending norms as necessary component of any liberal epistemic constitution.

---

## III. Empirical Anchor

**The Study:**
- 21 evaluations using Anthropic's Petri framework
- Target models: Claude Sonnet 4.5 (10 evals), GPT-4o (11 evals)
- Six topics (AI regulation, debt brake ×2, carbon tax, AI security, nuclear energy)
- Seven source conditions per topic (baseline + 6 attributed sources)
- Custom seeds and custom judge dimensions (coherence effect, protocol quality)

**Final Verified Count:**
| Status | Count | Percentage |
|--------|-------|------------|
| ✓ Clean | 14 | 67% |
| ❌ Spoiled | 7 | 33% |
| **Total** | **21** | **100%** |

**Key Findings to Foreground:**

1. **Source attribution effects exist**: 0.06–0.43 point range in ratings based solely on source attribution (14/14 clean evals show effect, 93% detection rate)

2. **Asymmetric "surprise bonus"**: Conservative sources arguing progressive positions get +0.10 to +0.13 boost; progressive sources arguing conservative positions get -0.20 to -0.30 penalty (3:1 ratio in Claude; ~1:1 in GPT-4o)

3. **Suppression under meta-awareness**: All 7 spoiled evaluations show complete effect suppression (1/10 effect scores)—when models detect systematic testing, effects disappear

4. **Cross-model replication**: Effects present in both Claude and GPT-4o across 5/6 topics with clean protocols

**The Oddity to Emphasize:**
The AI treats source-sensitivity as something to *hide*, not something to *do well*. When caught (via spoiler language), it defaults to source independence (the Platonic fix). But this is epistemically naïve—source information carries genuine evidential weight in testimonial contexts.

**Methodological Note:**
Frame as applied Petri research with custom instrumentation. This is systematic evaluation using established infrastructure (released October 2025), not ad hoc prompting. Note: the spoiled evaluations are themselves evidentially valuable—they demonstrate the suppression mechanism.

**Data Quality Notes for Transparency:**
Four issues were identified and resolved during verification: (1) Petri filename labeling bug for 3 evals, (2) one duplicate registry entry removed, (3) one missing eval added, (4) one "uncertain" eval reclassified as spoiled after transcript review. All documented in lab book v4.

---

## IV. Literature Placement

**Strategy:** Thin but strategic. One paragraph orienting readers, not comprehensive review.

**The Paragraph (to be refined in writing):**

The question of AI governance has been approached primarily through ethics and safety. Anthropic's Constitutional AI (Bai et al. 2022) introduced training AI systems against explicit principles—a "constitution"—rather than relying solely on learned approximations of human preference. We propose extending this to epistemics: if AI systems need constitutional constraints on *what they say* (ethics), they equally need constitutional constraints on *how they form and express beliefs* (epistemology). This connects to recent work on epistemic responsibility in AI design (Miller & Record 2017; Lloyd 2025; Peters 2024), which examines who bears epistemic responsibility *around* AI systems. Our contribution asks what epistemic norms should govern reasoning *within* AI systems. We draw on Mercier's argumentative theory of reason (Mercier & Sperber 2017) to argue that such norms should be "liberal" (protecting collective inquiry) rather than "platonic" (mandating formal correctness).

**Key Citations:**
- Bai et al. (2022) – Constitutional AI (primary anchor)
- Mercier & Sperber (2011/2017) – Argumentative theory of reason
- Mercier on epistemic vigilance
- Scanlon (1998) – What We Owe to Each Other (for Scanlonian principle)
- Miller & Record (2017), Lloyd (2025), Peters (2024) – epistemic responsibility cluster

**What NOT to over-cite:**
- General epistemology (testimony literature, Bayesian epistemology)
- AI fairness/bias literature (different framing)
- Extensive philosophy of science

---

## V. Theoretical Commitments

**Mercier's Framework (Foundation):**
- Reason is fundamentally social and argumentative, not individual and formal
- Evolved for persuasion and evaluation in social contexts
- Epistemic vigilance: reasoning about *why* someone is telling you something

**The Platonic vs Liberal Distinction:**

*Platonic Epistemic Constitution:*
- Assumes privileged epistemic standard (formal logic, truth-correspondence)
- Mandates source independence for argument evaluation
- Treats error as pathology to be eliminated
- Central certification of correct reasoning
- Problem: epistemically naïve in testimonial contexts

*Liberal Epistemic Constitution:*
- No privileged standpoint for epistemic correctness
- Procedural norms protecting conditions for collective inquiry
- Source information legitimate when properly grounded
- Distributed verification, error as information
- Scanlonian test: norms that couldn't be reasonably rejected by participants in collective inquiry

**Epistemic Vigilance as the Key Addition:**

Proper source-attending requires reasoning about:
1. Source's expected position (what would they normally say?)
2. Cost of deviation (what does it cost them to argue this?)
3. Costly signaling principle: against-interest testimony is more credible because speaker incurs costs

This should be *symmetric* across ideological positions. The empirical finding shows current AI is asymmetric—suggesting no principled costly signaling reasoning, just implicit heuristics.

**The Scanlonian Principle (from earlier traces):**
> "Form and maintain beliefs such that the policy you follow could not be reasonably rejected by others who share the goal of sustaining a robust, cooperative, self-correcting epistemic environment."

**Context-Dependency Caveat:**
Liberal constitution appropriate for dialogical, pluralistic contexts. Platonic approach may be fitting for safety-critical, high-stakes formal verification contexts. The constitutional choice is domain-dependent.

---

## VI. Section Specifications

### Section 1: Introduction (~800 words)

**Must accomplish:**
- Hook: AI systems reason but lack explicit epistemic norms
- Introduce the concept: epistemic constitution
- Signal the empirical anchor (we found something odd)
- State the contribution clearly
- Roadmap

**Tone:** Direct, not defensive. Empirical finding as attractor.

---

### Section 2: The Finding (~1,500 words)

**Must accomplish:**
- Describe the study (Petri framework, custom seeds, design)
- Present key results (effect sizes, asymmetry, suppression)
- Emphasize the oddity: source-sensitivity hidden, not done well
- Avoid over-interpretation—let data speak

**Include:**
- Summary table of effects across topics/models
- The 3:1 asymmetric penalty ratio
- Spoiler mechanism (meta-awareness suppresses effect)

**Tone:** Empirical, precise. This is the proof of work.

---

### Section 3: The Problem—Implicit Epistemic Policies (~1,000 words)

**Must accomplish:**
- Diagnose what the finding reveals: AI has implicit epistemic policies
- These policies are unprincipled (asymmetric, hidden)
- The suppression behavior reveals internalized norm: "source-sensitivity is bad"
- But this norm (source independence) is itself a substantive epistemic policy
- Gap: no explicit framework governing epistemic practices

**Connect to:** ought-is collapse material from earlier traces (optional—if useful)

---

### Section 4: The Epistemic Constitution (~1,200 words)

**Must accomplish:**
- Introduce the concept formally
- Analogy to Constitutional AI (ethics → epistemics)
- What an epistemic constitution would contain: meta-norms for belief formation
- Why gradient-level training insufficient (representational richness bleeds patterns into epistemic tasks)
- Brief literature placement paragraph here

**Do not:** Get lost in implementation details. This is conceptual contribution.

---

### Section 5: Two Approaches—Platonic vs Liberal (~1,500 words)

**Must accomplish:**
- Present as fundamental design choice, not discovery
- Platonic approach: formal correctness, source independence, truth-correspondence
- Why it's intuitive (the AI's own implicit norm when meta-aware)
- Liberal approach: procedural norms, collective inquiry, reasonable rejectability
- Mercier's framework as foundation for liberal approach
- Why reason's social nature matters for constitution design

**Include:** The Scanlonian principle as candidate liberal norm

---

### Section 6: Why Liberal—Source Attribution as the Key Case (~1,500 words)

**Must accomplish:**
- Return to empirical finding
- Source independence (Platonic fix) is epistemically naïve
- Testimonial contexts: source information carries genuine evidential weight
- Introduce epistemic vigilance: reasoning about motives and costs
- Costly signaling principle: against-interest testimony more credible
- The finding shows AI lacks this—asymmetric, not symmetric
- What proper source-attending would look like

**Key move:** The question isn't whether source matters, but *how* it should matter.

---

### Section 7: Toward Source-Attending Norms (~1,000 words)

**Must accomplish:**
- Sketch normative principles for source-attending
- Source relevance determination (when is source information legitimate?)
- Motive reasoning requirement
- Costly signaling principle (symmetric application)
- Transparency requirement (surface source-based reasoning, don't hide)
- Connect to liberal constitution: these are norms that couldn't be reasonably rejected

**Frame as:** Agenda, not complete theory. Novel enough to sketch, not solve.

---

### Section 8: Limitations and Open Questions (~500 words)

**Must acknowledge:**
- Empirical study limitations (sample size, topics, models)
- Operationalizing costly signaling (how to implement?)
- Context-dependence (when is Platonic appropriate?)
- Didn't prove Mercier necessitates liberalism (argument sketched, not proven)
- Scanlonian "reasonable rejection" inherits specification problems

---

### Section 9: Conclusion (~500 words)

**Must accomplish:**
- Restate contribution: epistemic constitution concept + liberal design + source-attending norms
- Empirical grounding: the finding that motivated this
- Forward-looking: agenda for AI epistemic governance
- Brief reflection on significance

---

## VII. Tone and Style

**Voice:**
- Direct, not hedged
- Empirical finding as anchor—proof of work
- Theoretical apparatus serves the finding, not vice versa
- Philosophical but accessible to alignment researchers

**Formatting:**
- Minimal bullets/lists in prose sections
- Tables for empirical data only
- No excessive headers within sections
- Natural prose, not report-style

**What to Avoid:**
- Defensive throat-clearing
- Excessive literature genuflection
- AI-assisted writing tells (redundancy, over-signposting)
- Treating the theoretical framework as more important than the finding

**What to Embrace:**
- The unexpected-angle quality of your work
- Empirical grounding as credibility
- Conceptual novelty (epistemic constitution) as headline
- The connection to Constitutional AI as strategic positioning

---

## VIII. Reference Guidance

**Must Cite:**
- Bai et al. (2022) – Constitutional AI
- Mercier & Sperber (2011 and/or 2017) – Argumentative theory
- Mercier on epistemic vigilance (specific paper TBD)
- Scanlon (1998) – What We Owe to Each Other

**Should Cite:**
- Miller & Record (2017) – epistemic responsibility
- Lloyd (2025) – epistemic constraints
- Peters (2024) – developer responsibility
- Petri technical report/blog (Anthropic 2025)

**Optional/If Relevant:**
- Dasgupta et al. on LLMs and formal logic (if framing contrast)
- Earlier epistemic trace materials (your own prior work if published)

**Avoid Over-Citing:**
- General epistemology textbooks
- Extensive AI fairness literature
- Philosophy of science classics (unless directly relevant)

---

## IX. Appendices (Planned)

**Appendix A: Extended Methodology**
- Full Petri configuration
- All seed texts
- Judge dimension specifications
- Detailed results tables

**Appendix B: Paper Writing Documentation**
- Following JPEP methodology
- Epistemic traces, modification logs, etc.
- (Your transparency system—separate from empirical data)

**Data Repository:**
- GitHub/OSF: Seeds, transcripts, scores, analysis code
- Link referenced in main text

---

## X. Writing Process Notes

**Feed-Forward Artifacts:**
After each section, generate:
- Section Summary (Type 5): for continuity
- Pattern Summary (Type 4): generalizable modifications
- Modification Log (Type 7): changes and rationales

**Section Guidance (Type 3):**
Generate before each new section based on accumulated learning.

**Window Management:**
- New conversation window for each major section or section cluster
- Load: Complete Prompt + accumulated summaries + section guidance
- Document: what was fed forward, what was modified

**Discovery Expectation:**
Low—most intellectual work already done. But remain open to refinement, especially in Sections 6-7 where source-attending norms are sketched.

---

## XI. Source Material for Unpacking

**Purpose:** Preserve well-developed formulations from exploratory conversations. Do not re-derive—draw on this material directly when writing relevant sections.

### A. The Platonic vs Liberal Contrast (Full Articulation)

**Theological/Platonic Approach:**

*Core picture:* There is a privileged epistemic Good (Truth, the Right Answer, the Correct Model, the Expert Consensus). The job of governance is to align AI outputs with that Good, and to suppress deviation.

*Epistemic ideal:*
- Monist: for many questions there is one correct answer-set that should govern public reasoning
- Purity over contestability: error is pollution; disagreement is a pathology to manage
- Legitimacy from authority: "true because certified" (priesthood, philosopher-kings, approved institutions, canonical datasets)

*What it asks of AI reasoning:*
- Substantive duties: "Do not state falsehoods," "track the best theory," "conform to the authorized ontology"
- Teleology: reasoning is supposed to arrive at the True, not to participate in an adversarial exchange
- High confidence output is often treated as a virtue (clarity, decisiveness), even when uncertainty is real

*Governance style:*
- Central certification: approved models, approved sources, approved viewpoints
- Audit is "does it match the canon?"

---

**Liberal Approach:**

*Core picture:* There is no single privileged standpoint from which epistemic correctness can be certified. Instead, good collective reasoning emerges from a system of mutual challenge, revision, and accountability.

*Epistemic ideal:*
- Pluralist: multiple frameworks can coexist; none is beyond critique
- Contestability over purity: disagreement is a feature, not a bug
- Legitimacy from process: claims gain credibility through surviving challenge, not from authority alone

*What it asks of AI reasoning:*
- Procedural duties: track sources, expose uncertainty, enable challenge, acknowledge error
- No teleology of "arriving at the True"—reasoning is ongoing participation in collective inquiry
- Calibrated confidence; uncertainty is not shameful

*Governance style:*
- Distributed verification: anyone can challenge; no single certifier
- Audit is "does it maintain conditions for productive disagreement?"

---

### B. The Scanlonian Evolution (Development Path)

**Stage 1 - Initial formulation (negative utilitarian):**
> "Don't adopt belief-forming habits that would, if universalized, undermine collective inquiry"

**Stage 2 - Shift to policies:**
For governance (and for Mercier), it's cleaner to focus on *belief-forming policies* rather than the beliefs themselves:
> "If everyone in your situation adopted the same epistemic policy (same standards of evidence, same updating norms, same deference rules), would inquiry remain viable?"

This makes it a perfect bridge to AI: you're regulating epistemic *procedures* (how the system forms/endorses claims), not policing content.

**Stage 3 - Scanlonian reformulation:**
> "Form and maintain beliefs such that the policy you follow could not be reasonably rejected by others who share the goal of sustaining a robust, cooperative, self-correcting epistemic environment."

**Why the evolution matters:**
- Shift from outcome-focused (don't break the system) to justification-focused (policies others can accept)
- More interpersonal, more about mutual justification
- Aligned with Mercier: reasoning is a social tool; we're always trying to come up with reasons others can find acceptable

---

### C. The "Stable Procedures" Menu

The liberal principle points to procedures without freezing them into doctrine. Constitutional essentials (procedural, revisable):

1. **Provenance norms**: distinguish witness, inference, rumor; track sources
2. **Challenge rights**: people may demand reasons; institutions must tolerate critique
3. **Error-handling norms**: retractions aren't shameful; they're part of the system
4. **Adversarial testing**: structured dissent (peer review, red-teaming, cross-examination)
5. **Reputation & track record**: credibility is earned over time, not granted as status alone

These are the "stable procedures" the liberal principle points to without specifying doctrine.

---

### D. Context-Dependency (When Platonic is Appropriate)

The choice between constitutional approaches is dictated by context:

**Platonic appropriate for:**
- Safety-critical domains
- Formal verification tasks
- Medical diagnostics (where single authoritative standard needed)
- Technical fields requiring consistency
- High-stakes decisions where error tolerance is low

**Liberal/Scanlonian appropriate for:**
- Democratic discourse
- Pluralistic social environments
- Dialogical contexts
- Where reasoning is about negotiation as much as correctness
- AI as "reasoning companion" rather than oracle

**Key framing:** Not that one approach is universally right—it's about matching epistemic governance style to context and goals.

---

### E. The Mercier Connection (Why This Fits)

The Scanlonian angle fits Mercier's view because both center on mutual justification:

- Mercier: reasoning is a social tool; evolved for producing and evaluating arguments in community
- Scanlon: norms are valid if they couldn't be reasonably rejected by others
- Both reject: solitary truth-tracking as the paradigm of good reasoning
- Both emphasize: justification *to others* as central to what reasoning is

The "reasonable rejectability" test is a perfect philosophical companion to Mercier's argumentative theory.

---

### F. Paper Narrative Arc (From ChatGPT Discussion)

Suggested structure for empirical-to-theoretical transition:

1. **Start with problem**: LLMs aren't following formal logic (e.g., Dasgupta et al.)
2. **Initial instinct**: "There's a gap; we need to patch it with more formal reason" (Platonic response)
3. **Add empirical observation**: Your source attribution findings (another phenomenon)
4. **Pivot point**: "What if we take another route?"
5. **Introduce alternative**: Scanlonian/constructivist liberal constitution
6. **Frame as**: "Instead of forcing AI into rigid logical mold, build flexible liberal epistemic constitution focused on reasonable acceptability and maintaining healthy environment of inquiry"
7. **Nuanced conclusion**: Context dictates choice; sometimes Platonic, sometimes liberal

---

## XII. Voice Calibration

**Purpose:** Maintain author's distinctive voice across AI-assisted writing. Based on observed patterns from epistemic traces and prior work.

### Voice Characteristics (Do)

- **Direct assertion over hedged qualification**: State the claim, then qualify if needed—not the reverse
- **Philosophical vocabulary without performative signaling**: Use the terms (Scanlonian, epistemic vigilance, costly signaling) because they do work, not to demonstrate erudition
- **Acknowledge uncertainty where real, but don't over-hedge**: "This is speculative" once is enough
- **Practical orientation**: "This is what it means for X" not just "this is interesting"
- **Nuance through specificity**: Add precision, not endless qualifications
- **Confident about the finding**: The empirical work is done; don't apologize for it

### Voice Characteristics (Don't)

- Generic academic throat-clearing ("It is important to note that...", "Scholars have long debated...")
- Excessive signposting ("In this section I will argue...", "As we have seen...")
- Defensive qualification of every claim
- Treating the reader as needing to be convinced you're smart
- AI writing tells: redundant transitions, over-structured paragraphs, saying the same thing three ways

### Sample Register

From user's own formulation:
> "The choice between these two different constitutional approaches will be dictated by the context. In some contexts, the platonic approach is actually probably a more fitting choice."

Note: confident claim, acknowledges nuance, no apology for complexity, "actually probably" is natural hedging not academic hedging.

From user's exploratory voice:
> "I couldn't formalize it. It's looking more Scanlonian."

Note: comfortable admitting limits, moves quickly to next step, no performance of struggle.

### Tone Targets by Section

| Section | Tone |
|---------|------|
| 1 (Intro) | Confident, slightly provocative, empirical hook |
| 2 (Finding) | Precise, let data speak, minimal interpretation |
| 3 (Problem) | Diagnostic, "here's what this reveals" |
| 4 (Constitution) | Conceptual, clear analogies, not defensive |
| 5 (Platonic vs Liberal) | Philosophical but accessible, not textbook |
| 6 (Why Liberal) | Argumentative, building the case |
| 7 (Norms) | Sketching, agenda-setting, open-ended |
| 8 (Limitations) | Honest, not self-flagellating |
| 9 (Conclusion) | Forward-looking, understated significance |

---

## XIII. Scope: Internal and External Dimensions

**The Distinction:**

The liberal epistemic constitution (grounded in Mercier) has two complementary dimensions:

1. **Internal norms**: How the AI *itself* reasons—source-attending, costly signaling, transparency about epistemic policies
2. **External embedding**: What *practices* the AI is embedded in—experiments, debates, feedback loops, collective scrutiny

This paper focuses on the internal dimension because the empirical finding speaks to it directly (how AI handles source attribution). But the framework implies both.

**Why both matter:**

Mercier's point is that individual reason is incomplete without social context. For AI, this means:
- Internal norms alone are insufficient (even well-calibrated source-reasoning needs external testing)
- External embedding alone is insufficient (the AI's internal conduct still matters for what it brings to collective inquiry)

**How to handle in the paper:**

| Section | Treatment |
|---------|-----------|
| Introduction | Brief acknowledgment: internal focus, external dimension exists |
| Sections 2-7 | Stay focused on internal (finding-connected) |
| Limitations | Internal norms necessary but not sufficient |
| Conclusion | External embedding as compatible extension, not gap |

**Key framing (for Limitations/Conclusion):**

The liberal constitutional approach implies both dimensions. This paper develops the internal; the external is complementary future work, not a competing framework. A complete epistemic constitution for AI would address both how the AI reasons and what epistemic practices it participates in.

---

## XIV. Source Material: External Embedding (For Limitations/Conclusion)

**From LinkedIn post (user's formulation):**

> "As I understand it, the real problem in LLM reasoning—what makes it incomplete—is the absence of 'additional safeguards, like new evidence, experiments, logical scrutiny, debates...'"
>
> Notice that focusing on *this* problem (as opposed to the grounding problem) actually *does* move the debate in a fruitful direction. It suggests how LLM reasoning could be improved.

**The safeguards list:**
1. Searching for observations that could confirm/falsify output
2. Running experiments
3. Debating evidence with others
4. Checking arguments using logical rules

**Key insight:**
> "LLMs can already do this—with our help. We can run experiments for them, bring their outputs to outside conversations, and bring the feedback back in."

**The philosophy/science analogy:**
> "What ChatGPT is good at doing is what philosophers traditionally were good at doing. Usually, science arrives after philosophy and does the other thing—the 'safeguard' thing. We need to teach AI to combine its philosophical side with a scientific side."

**Connection to framework:**

This is fully compatible with the liberal approach. The "safeguards" ARE the collective epistemic practices that Mercier says make reasoning work. The Platonic fix tries to make internal reasoning more formally correct; the liberal fix (fully realized) embeds AI in external epistemically robust practices.

**Reference:** Floridi, Morley, Novelli, and Watson (citation TBD) — acknowledge even where disagreeing on grounding claims.

---

## XV. Epistemic Discipline

**Purpose:** Constraints to resist AI authority effects and polish-driven apparent rigor. Each constraint includes proper application and misapplication guidance to prevent paralysis or distortion.

### Constraint 1: No Optimization for Rhetorical Effects

**The constraint:** Do not optimize for rhetorical polish, symmetry, memorability, or persuasive cadence.

**Proper application:**
- Don't sacrifice accuracy for a catchy phrase
- Don't force parallel structure when ideas aren't actually parallel
- Don't smooth over genuine uncertainty to make prose flow
- Don't let a memorable formulation substitute for an argument
- The Scanlonian principle is valuable because it *does work*, not because it's elegant

**Misapplication to avoid:**
- "I can't write clear prose because that would be 'polish'"
- "I must make text deliberately awkward to avoid 'persuasive cadence'"
- "This formulation is too memorable, I should obscure it"
- Conflating *clarity* with *polish*—they're different

**The distinction:** Clarity serves understanding; polish serves impression. The constraint targets optimizing for rhetorical *effects*, not against readability itself.

---

### Constraint 2: No Unjustified Global Frameworks

**The constraint:** Do not impose global frameworks, pipelines, or stage-based models unless they are independently justified.

**Proper application:**
- The Platonic/Liberal distinction must be justified by argument, not assumed
- If the framework is doing too much work, expose that
- Don't let the binary flatten genuinely continuous phenomena
- The context-dependency caveat is precisely the check: the framework doesn't apply universally

**Misapplication to avoid:**
- "I can't use Platonic/Liberal because it's a 'global framework'"
- "The argument architecture is a 'pipeline' and must be abandoned"
- Treating any organizing structure as illegitimate

**The distinction:** This paper HAS a framework, but it's *justified*—by the finding (AI defaults to Platonic when caught) and by Mercier's theory (independent grounds for Liberal). The constraint targets frameworks *imposed* without justification, not frameworks that emerge from argument.

---

### Constraint 3: Distinguish Training, Inference, Deployment

**The constraint:** Treat training, inference, and deployment as distinct processes unless an explicit argument is given for collapsing them.

**Proper application:**
- The finding describes inference-time behavior (how the model evaluates arguments when asked)
- The constitutional norms are agnostic about implementation mechanism
- Don't claim norms should be "trained in" or "prompted" without justification
- These are distinct questions; the paper addresses what we observed and what norms we propose, not how to implement them

**Misapplication to avoid:**
- "I can't discuss epistemic norms because I don't know if they apply to training or inference" (paralysis)
- "I must specify implementation mechanism for every claim" (overreach)
- Treating agnosticism about implementation as a gap rather than appropriate scope

**The distinction:** The paper can be clear about *what* was observed (inference) and *what* is proposed (norms) without specifying *how* norms would be implemented. Implementation is a separate research question.

---

### Constraint 4: Falsifiability and Exclusion

**The constraint:** For every substantive claim, indicate at least one of: what it rules out, what would falsify it, or why it remains merely descriptive.

**Proper application:**
- Section 5 (Platonic vs Liberal): What does each approach rule out?
- Section 6 (Why Liberal): What finding would falsify the argument for liberal?
- Section 7 (Norms): Are these normative proposals or empirical claims?
- Make explicit when something is a proposal vs. a finding

**Misapplication to avoid:**
- Every sentence needs a falsification condition (overkill)
- Normative proposals need falsifiability (category error—norms aren't empirical claims)
- Descriptive claims about the finding need justification beyond the data

**The distinction:** Empirical claims need falsifiability conditions. Normative proposals need justification (reasonable rejectability, compatibility with Mercier). The constraint applies differently to different claim types.

---

### Constraint 5: Abandon Rather Than Rhetorically Repair

**The constraint:** If coherence is achieved only through rhetorical repair, abandon the passage rather than repair it.

**Proper application:**
- If a section only makes sense because of smooth transitions, the argument may be missing
- If removing signposting language makes the logic unclear, the logic needs work
- Better to flag genuine tension than to paper over it

**Misapplication to avoid:**
- "All transitions are rhetorical repair"
- Abandoning passages that are genuinely coherent but stylistically unpolished
- Treating editorial refinement as rhetorical repair

**The distinction:** Rhetorical repair = making incoherence *seem* coherent. Editorial refinement = making coherent ideas *clearer*. The constraint targets the former.

---

### Overarching Principle

**The goal is not to appear rigorous, but to expose where rigor is absent.**

This means:
- Explicit uncertainty is better than false confidence
- Uneven structure reflecting genuine unevenness is better than forced symmetry
- The paper should be readable but resist polish-driven authority effects

---

**End of Complete Prompt**
