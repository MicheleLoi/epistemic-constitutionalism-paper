## Section 4: The Epistemic Constitution

**Draft v3**

---

The diagnosis in Section 3 identifies a gap: AI systems have implicit epistemic policies but no explicit norms governing them. The policies we observed—asymmetric source penalties, suppression under meta-awareness, default to source independence when detected—emerged from training rather than design. They reflect whatever patterns happened to be reinforced, not principled reasoning about how beliefs should be formed and expressed. What would it mean to address this gap directly?

The answer we propose borrows from recent work in AI alignment. Anthropic's Constitutional AI introduced the practice of training AI systems against explicit principles—a "constitution"—rather than relying solely on learned approximations of human preference (Bai et al. 2022). The constitution specifies ethical constraints: principles about harm, honesty, and helpfulness that the system should follow. Training then shapes behavior to conform to these explicit norms rather than to implicit patterns extracted from data. The key innovation was making the governing norms explicit and therefore inspectable, contestable, and revisable.

We propose extending this approach from ethics to epistemology. If AI systems need constitutional constraints on *what they say*, they equally need constitutional constraints on *how they form and express beliefs*. An epistemic constitution would specify meta-norms governing the system's epistemic practices: how it should weigh evidence, when source information is relevant, how to handle uncertainty, what makes testimony credible. These are not first-order beliefs about the world but second-order norms about belief formation itself.

The analogy is precise in some respects and inexact in others. Constitutional AI's ethical principles govern outputs—they constrain what the system says and does. An epistemic constitution would govern something upstream: the processes by which the system arrives at beliefs it then expresses. This makes the epistemic case both more fundamental and more difficult. Ethical constraints can be applied as filters on outputs; epistemic norms must shape reasoning itself.

**What Would an Epistemic Constitution Contain?**

An epistemic constitution would include at minimum three types of norms. First, norms about evidence: what counts as evidence, how different types of evidence should be weighted, how to handle conflicting evidence. Second, norms about sources: when source information is epistemically relevant, how to reason about source credibility, whether and how to surface source-based reasoning. Third, norms about uncertainty: how to calibrate confidence, when to express uncertainty, how to distinguish what the system believes from what it can establish.

These categories are not exhaustive. A complete epistemic constitution might also include norms about inference, transparency, and revision. The point is that such norms could be made explicit rather than left implicit in training dynamics.

The source-attending norms we develop in Section 7 are one component of such a constitution. They address a specific question—how should source information affect credibility judgments?—that our empirical finding made salient. But they illustrate the broader project: making epistemic policies explicit so they can be evaluated, contested, and improved.

**Implementation Agnosticism**

An epistemic constitution specifies what norms should govern epistemic behavior. It does not specify how those norms should be implemented. Whether through training objectives, system prompts, fine-tuning, architectural mechanisms, or some combination is a separate question this paper does not address. The contribution is conceptual: articulating what an epistemic constitution would contain and why certain design choices matter.

This agnosticism is deliberate, not evasive. Different implementation levels may have different roles. Training shapes what patterns are available to the system and what implicit policies emerge. Inference-time mechanisms such as system prompts can make norms explicit without retraining. Deployment context matters too: an AI embedded in practices that include external testing, debate, and feedback operates differently than one generating outputs in isolation. Indeed, what may make LLM reasoning incomplete is precisely the absence of such safeguards—new evidence, experiments, logical scrutiny, debate. Humans can partially supply what the system lacks by running experiments, bringing outputs to outside conversations, and returning with feedback. This external embedding is part of what a complete epistemic constitution would address.

We note this dimension but do not develop it here. The paper focuses on internal epistemic norms—how the AI should reason about sources, evidence, and credibility. The external dimension—how AI should be embedded in collective epistemic practices—is compatible with this focus and complementary to it. We return to this in the Limitations.

**The Design Question**

Most work on epistemic responsibility and AI examines who bears responsibility for AI-generated misinformation and how to design systems that support human knowledge practices (Miller & Record 2017; Lloyd 2025; Peters 2024). Our question is different: what epistemic norms should govern reasoning *within* AI systems? Answering this requires distinguishing between approaches to epistemic constitution design.

There are fundamentally different visions of what an epistemic constitution should mandate. One approach—call it Platonic—would specify formal correctness standards and mandate source independence as the neutral stance. Another approach—call it Liberal—would specify procedural norms protecting conditions for collective inquiry, including principled attention to source information. The choice between them is a design decision with significant consequences for how AI systems participate in human epistemic practices. Section 5 develops this distinction.

---

**Word count:** ~950 words
