# AI, conversational interfaces, agents, and human oversight

Operational guide and topic inventory. Procedures and checks are an original synthesis; use the source register for the authority, inspected portion, and limits of specific references.

### Coverage

| Area | Details to consider |
| --- | --- |
| Product fit | User need; AI/non-AI alternatives; task value; failure consequence; data suitability; evaluation; cost; latency. |
| Expectations | Capability; limits; uncertainty; provenance; data use; generated versus sourced; appropriate reliance; user role. |
| Conversation | Intent; context; turns; clarification; ambiguity; repair; interruption; fallback; memory; multimodal input; human handoff. |
| Generative workspace | Prompt; source context; attachments; streaming; partial output; stop; retry; compare; edit; citation; export; history. |
| Agentic action | Scope; permissions; plan; preview; approval when required; execution; progress; external side effects; audit; cancel; undo; recovery. |
| Failure | Incorrect output; missing evidence; misleading citation; inconsistency; unsafe advice; overreach; tool error; partial completion; unknown outcome. |
| Personalization | Remembered preferences; user visibility; correction; reset; expiration; privacy; contextual boundaries; changing models. |
| Evaluation | Representative tasks; quality; calibration; recovery; overreliance; accessibility; subgroup effects; adversarial context; model/version regressions. |

### Procedure

1. Determine whether AI is useful for the task and what failures could mean for affected people.
2. Define the system's role, boundaries, data sources, output quality expectations, and actual action authority.
3. Communicate capabilities and uncertainty in task-relevant language without fabricated confidence scores.
4. Design input, generated output, revision, feedback, citations, state, and interruption as a complete workflow.
5. For tools or agents, specify permission scope, reviewable action details, progress, side effects, cancellation, and recovery according to actual authorization requirements.
6. Design correction and fallback for inevitable mistakes, including access to human or non-AI routes when needed.
7. Evaluate representative users and tasks, consequential errors, accessibility, inappropriate reliance, and change across versions.
8. Maintain user controls for memory, context, data use, and personalization.

### Rules for agents that change records

- **Draft, review, approve, apply, report.** The agent drafts; the person sees each change (old value, new value, who and what it affects) before approving.
- **An approval covers exactly what was shown.** If the draft changes after approval, it needs a new approval.
- **Side effects outside the product are separate steps.** Emailing or notifying a supplier, or charging a card, gets its own preview and its own confirmation, and says plainly that it cannot be unsent. Design it; do not scope it out.
- **The audit trail records the agent as drafter and the person as approver,** in separate fields, with the time of each. A single "actor" field loses who decided.
- **Cancelling halfway** stops further changes and shows which items were applied, which were not, and how to undo the applied ones.
- **A timeout is unknown, not failed.** Show "Checking..." and look up the result before allowing a retry, so nothing is applied twice.

### Outputs

AI-fit brief; expectation/authority model; conversation or generation flow; failure/recovery matrix; evaluation and monitoring plan.

### Quality checks

Uncertainty is honest; citations support claims; external actions have clear scope; corrections are possible; consequential outcomes are recoverable where feasible; evaluation goes beyond subjective fluency.

### Limits and common failures

A conversational surface is not automatically appropriate for every task. Natural language confidence is not calibrated probability. A generated plan is not evidence that an action happened. A video summary is not the same evidence as a reviewed transcript or experiment.

### Sources to consult

- S47: [Microsoft HAX guidelines](https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/). Overview inspected.
- S48: [Microsoft: HAX webinar](https://www.microsoft.com/en-us/research/video/create-human-centered-ai-with-the-human-ai-experience-hax-toolkit-webinar/). Official summary inspected; playback not reviewed.
- S64: [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework). Overview inspected.
- S65: [NIST Generative AI profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence). Publication abstract inspected.
