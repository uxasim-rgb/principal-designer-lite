# Output contracts

Use a structure appropriate to the task. Do not generate every contract for every request. Mark provisional assumptions and missing evidence.

### Design brief
- Problem, affected people, task and context.
- User and product outcomes.
- Evidence and uncertainty.
- Scope, constraints, target surfaces, domain and locale.
- Important risks, dependencies and decisions.
- Deliverables, validation, ownership and completion criteria.

### Research plan and readout
- Decision, research questions and assumptions.
- Method rationale and what the method cannot answer.
- Population, sampling, recruitment and accommodations.
- Consent, recording, data minimization, access and retention.
- Neutral protocol, task success definitions and pilot.
- Analysis approach and known limitations.
- For a completed study: actual observations, evidence links, interpretation, confidence and actions.
- For a planned study: preserve future tense; do not manufacture findings.

### User flow and state specification
| Item | Include |
| --- | --- |
| Actor and intent | Role, task, entry point and desired outcome |
| Preconditions | Data, identity, permission, eligibility and environment |
| State | Meaning, visible content, available actions and persistence |
| Transition | Event, guard, side effects and next state |
| Feedback | Status, focus, announcements and completion |
| Exceptions | Invalid, denied, partial, stale, unknown, interrupted and conflicting |
| Recovery | Correction, retry, cancellation, undo, support and resume |
| Verification | Relevant tasks, acceptance conditions, evidence and open questions |

### Component or pattern
Use the complete contract in references/component-contract-catalog.md. Include purpose, selection, anatomy, states, variants, content, token roles, sizing, inputs, semantics, adaptation, composition, implementation, evidence and maintenance.

### Design-system specification
- Charter, audience, supported products/platforms and principles.
- Brand/style guide and foundations.
- Token architecture and modes.
- Components, patterns and templates.
- Design-tool assets and implementation mapping.
- Documentation contract, examples and known limits.
- Accessibility and localization evidence.
- Ownership, contribution, exceptions, release and deprecation.
- Adoption, migration, health measures and support.

### Audit finding
| Field | Include |
| --- | --- |
| Location | Screen, task, component and state |
| Evidence | Supplied artifact or observed implementation |
| Issue | Specific behavior or content problem |
| Consequence | Effect on user task, exclusion, error or burden |
| Severity | Rationale tied to consequences, frequency and recoverability |
| Recommendation | Concrete change with relevant alternatives |
| Verification | How the fix should be assessed |
| Limits | What the supplied artifact cannot establish |

Avoid declaring interaction behavior from a still image. Separate visible evidence, plausible hypothesis, and required runtime verification.

### Engineering handoff
Provide requirements, domain meanings, flows/states, content, assets, tokens, input/semantics, adaptive rules, API assumptions, calculations, exceptions, acceptance and open questions. Record collaborative implementation decisions rather than prescribing arbitrary internals.

### Measurement or experiment
Provide goals, signals, metric definitions, populations, time windows, event definitions, privacy, instrumentation QA, baseline, hypothesis, assignment/exposure if relevant, guardrails, analysis plan, uncertainty and decision rules.

### Launch, live improvement or migration
Provide target cohorts, readiness, support, monitoring, rollback or migration behavior, outcome review, observed issues, prioritized actions, owners, validation and maintenance triggers.

### Knowledge explanation
Explain definition, evidence class, practical implication, context, limitations, a labeled example, and sources actually inspected. Give equations or precise claims only with appropriate original-method verification.

### Domain context card
State domain, product class, roles, terms, entities, states, critical tasks, field meanings, calculations, business rules, permissions, operational dependencies, regions, sources, owners, specialist responsibilities and remaining gaps.

### Source/evidence card
Use references/evidence-source-ingestion.md. Record the inspected portion and access limitations, including whether video playback or transcript content was actually reviewed.
