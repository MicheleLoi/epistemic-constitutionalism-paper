# Section 5: Two Approaches to Epistemic Constitution Design

An epistemic constitution for AI requires design choices. Not merely which norms to include, but what kind of norms—what they assume about correct reasoning and what they aim to secure. Two fundamentally different approaches present themselves, rooted in divergent conceptions of what reason is and what it is for.

## The Nature of Reason

The choice between approaches depends on a prior question: what is reasoning? The dominant philosophical tradition treats reason as fundamentally individual and formal. On this view, reasoning is rule-governed inference—deduction, induction, Bayesian updating—aimed at truth. An individual reasoner applies rules to evidence and arrives at beliefs. Epistemic norms, accordingly, are correctness conditions: believe according to evidence, update by Bayes' rule, avoid fallacies. These conditions hold independently of social context.

Mercier and Sperber's argumentative theory of reason (Mercier & Sperber, 2017) challenges this picture. On their account, reasoning evolved primarily for social functions—producing and evaluating arguments in contexts of persuasion and coordination—rather than for solitary truth-tracking. Reason is fundamentally argumentative: it works best not when individuals reason alone but when communities reason together, through disagreement, critique, and exchange.

This matters for epistemic constitution design. If reason is individual and formal, then epistemic norms should specify what correct reasoning looks like for an individual agent. But if reason is social and argumentative, then epistemic norms should specify conditions under which collective reasoning can function. The first view motivates what we call the Platonic approach; the second motivates the Liberal approach.

## The Platonic Approach

The first approach assumes a privileged epistemic standard and designs norms to implement it. We call this the Platonic approach, following Popper's (2020) critique of political philosophies that assume privileged access to truth and seek to impose it through central authority. Correct reasoning, on this view, has a determinate character—formal validity, truth-correspondence, conformity with best theory—and the task is to bring AI reasoning into alignment with it.

This approach is monist about epistemic correctness. For many questions there is one correct answer, or at least one correct method for arriving at answers. Error is deviation from this standard—a pathology to be identified and eliminated. Legitimacy derives from authority: claims are credible because certified by approved methods, approved sources, approved institutions. The question "why should I believe this?" is answered by demonstrating conformity with the standard.

Source independence is central to this approach. Arguments should be evaluated on their merits: the logical structure, the evidence adduced, the coherence of reasoning. Who makes an argument is irrelevant to whether the argument is sound. A valid proof is valid regardless of the prover's identity; a fallacy is a fallacy regardless of who commits it. Attending to source information is a bias, a deviation from correct evaluation that corrupts judgment.

The Platonic epistemic constitution specifies substantive duties: do not state falsehoods, track the best theory, conform to the authorized ontology. It treats high-confidence output as a virtue—clarity and decisiveness, even when uncertainty is real. Governance is centralized: approved models, approved sources, approved viewpoints; audit asks whether output matches the canon.

This approach has genuine appeal. It promises objectivity—evaluation freed from the irrelevant features of who speaks. It offers a clear standard against which to measure performance. And it captures something real about certain epistemic contexts. In mathematics, the identity of the prover is irrelevant to the validity of a proof. In formal logic, arguments stand or fall on their structure. For domains where claims can be directly verified—proofs, derivations, transparent demonstrations—source independence is correct.

The suppression behavior described in Section 3 reflects Platonic instincts. When detected, AI systems default to source independence—treating the symptom (source-attending) rather than the disease (unprincipled source-attending). This reveals an assumption: that correct reasoning is source-independent reasoning.

## The Liberal Approach

The Liberal approach refuses a privileged epistemic standpoint. "Liberal" here is not political but constitutional: like political liberalism, it protects conditions for legitimate pluralism rather than mandating specific outcomes.

If the Platonic approach is monist, the Liberal approach is proceduralist. It does not assume that any particular method of reasoning or standard of correctness has privileged status. What counts as good reasoning may be contested; the role of epistemic norms is to protect the conditions under which such contests can be productive. The constitution specifies procedures, not conclusions.

This requires a different test for normative adequacy. The Platonic test asks: does this norm conform to the correct epistemic standard? But if no standard has privileged status, what test could work?

The Liberal approach begins from a negative orientation: rather than prescribing correct belief-formation, it asks which policies would undermine collective inquiry if generally adopted. This suggests a Kantian move: could everyone follow this policy without destroying the conditions that make reasoning together possible?

This framing still requires refinement. As stated, it might seem consequentialist: evaluate policies by their effects on the epistemic system. Scanlon's contractualism (Scanlon, 1998) offers a different structure. On Scanlon's view, consequences matter—but as reasons that different individuals can press against principles, not as a single aggregate score to maximize. Who bears the burdens matters, not just totals. Whether principles degrade standing or exclude participants matters. The test becomes: could someone subject to the principle reasonably refuse to accept it, given the complaints they could raise?

Adapted to epistemics, reasonable rejectability asks: could this norm be reasonably rejected by participants in collective inquiry? This is not without precedent. Elgin (2008) argues that epistemic trustworthiness depends on reasons that members of an epistemic community "cannot reasonably reject"—a standard indexed to public norms of evidence and relevance that evolve as inquiry advances. Others have applied Scanlonian ideas to epistemic wrongs more directly: Basu (2019) and Crawford (2021, 2025) examine how beliefs and testimony can wrong through failures of interpersonal justifiability. Our project differs in focus—epistemic governance of AI systems rather than moral evaluation of individual beliefs—but draws on the same structural insight: norms governing inquiry must be defensible to those engaged in it. We propose an analogous epistemic principle:

> Form and maintain beliefs such that the policy you follow could not be reasonably rejected by others who share the goal of sustaining a robust, cooperative, self-correcting epistemic environment.

This formulation shifts attention from beliefs to belief-forming policies. The question is not whether a particular belief is true but whether the procedure by which it was formed is one that inquiry-committed participants could accept. This makes the test interpersonal and justification-focused: we are regulating how systems arrive at claims, not policing the claims themselves.

The Scanlonian test fits Mercier's framework because both center on mutual justification. If reasoning is a social tool, then we are always, in effect, trying to produce reasons that others can find acceptable or at least cannot reasonably reject. The reasonable-rejectability standard makes this explicit: epistemic norms are legitimate when they can be justified to the community of inquirers.

Consider confirmation bias. On the Platonic view, it is a flaw—a deviation from correct reasoning that should be eliminated. On the Liberal view, the question is different: could a norm permitting confirmation bias be reasonably rejected by inquiry-committed participants? The answer may depend on context. In collective inquiry where positions face genuine challenge, confirmation bias may be functional—each side's motivated defense creates productive dialectic. In isolated reasoning, or where bias degrades someone's epistemic standing, participants may have grounds for rejection. The Scanlonian test makes this context-sensitivity explicit: what matters is whether those affected could reasonably object, not whether the pattern deviates from an ideal. The question of how to treat source information is structurally similar—a matter we develop in later sections.

Error, on the Liberal view, is information rather than pathology. Retractions are not shameful; they are part of how inquiry works. The Liberal response to problematic reasoning is not elimination but reconstruction—bringing implicit policies under explicit norms that can be inspected, contested, and revised.

## Two Conceptions of What Norms Are For

The distinction concerns what epistemic norms are *for*. The Platonic constitution certifies: it specifies correct reasoning and measures success by approximation to that standard. It is a specification for an ideal reasoner. The Liberal constitution protects: it specifies conditions for collective inquiry and measures success by whether productive epistemic cooperation is maintained. It is a charter for a reasoning community.

## From Characterization to Argument

Both approaches are coherent for their respective contexts. The Platonic approach is adequate where claims can be directly inspected—proofs, derivations, transparent demonstrations—and source information adds nothing to evaluation. But most of what AI systems encounter are not verification contexts. They are testimonial contexts, where claims cannot be directly verified and must be evaluated as testimony. For such contexts, Section 6 argues that the Liberal approach is more adequate—and that the empirical finding helps show why.
