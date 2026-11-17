# Lifecycle workflow catalog

320 candidate workflows across 40 families. These are scope definitions used by the master procedure, not 320 independently implemented or evaluated skills. Find the relevant family or task, then use the operational guides and output contracts.

40 families · 320 candidate workflows. Each family owns a recognizable area of work. Several candidates may ship inside one skill before real usage justifies separate entry points.

| Family | Coverage owner |
| --- | --- |
| 01. Project intake and collaboration | Plan the work and establish decision ownership. |
| 02. Product and business strategy | Connect design decisions to user and business outcomes. |
| 03. Context and ecosystem discovery | Understand the environment around the interface. |
| 04. Research planning and operations | Make research appropriate, ethical, and repeatable. |
| 05. Qualitative research | Understand behavior and context without inventing participants. |
| 06. Quantitative research | Measure patterns and uncertainty appropriately. |
| 07. Research synthesis and evidence | Turn observations into traceable design decisions. |
| 08. Problem and opportunity definition | Choose which problem deserves design effort. |
| 09. Service and systems design | Design the whole service across digital and physical channels. |
| 10. Requirements and business logic | Make behavior explicit enough to design and build. |
| 11. Information architecture | Make information and objects understandable and findable. |
| 12. Content design and UX writing | Give people the information they need to act. |
| 13. Concept generation and selection | Explore options before committing to a direction. |
| 14. Task flows and state models | Specify how people progress through a task. |
| 15. Interaction behavior | Define the behavior behind visual controls. |
| 16. Forms, input, and validation | Help users enter correct information with minimal effort. |
| 17. Search, browse, and discovery | Support purposeful finding and exploration. |
| 18. Data-heavy and enterprise interfaces | Support complex work without hiding business meaning. |
| 19. Identity, accounts, and permissions | Make account access understandable and recoverable. |
| 20. Transactions and product lifecycles | Design complete object and transaction lifecycles. |
| 21. Visual UI foundations | Create clear, consistent visual communication. |
| 22. Components and reusable patterns | Design reusable controls with complete behavior. |
| 23. Responsive and adaptive design | Adapt behavior to available space and input capability. |
| 24. Design systems | Maintain a shared design language connected to implementation. |
| 25. Accessibility and inclusive design | Include diverse abilities throughout research, design, and implementation. |
| 26. Localization and internationalization | Design for languages, scripts, and regional conventions. |
| 27. Motion, sound, and haptics | Use sensory feedback to explain state and support action. |
| 28. AI, conversation, and human-machine interaction | Design for uncertain system behavior and appropriate user control. |
| 29. Prototyping and technical feasibility | Choose artifacts that answer a concrete design question. |
| 30. Evaluation and validation | Check whether a design helps users achieve the intended outcome. |
| 31. Handoff, implementation, and design QA | Carry design intent into the working product. |
| 32. Launch and release readiness | Prepare the experience and team for real use. |
| 33. Measurement and instrumentation | Make outcomes measurable before interpreting success. |
| 34. Post-launch diagnosis and continuous research | Understand what happens in real use and why. |
| 35. Experimentation and optimization | Test improvements without overclaiming evidence. |
| 36. Activation, retention, and responsible growth | Help users achieve recurring value and control their relationship. |
| 37. Live service reliability, support, and maintenance | Keep the experience dependable after release. |
| 38. Evolution, migration, and retirement | Manage long-term change and safe endings. |
| 39. Design operations, governance, and leadership | Make design work sustainable across people and teams. |
| 40. Professional practice and knowledge maintenance | Keep the skill collection credible and useful over time. |

#### 01. Project intake and collaboration

Plan the work and establish decision ownership.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `triage-design-request` | Clarify the request, intended user outcome, product stage, constraints, urgency, and what evidence exists. | Scoped brief and open-question log |
| `audit-existing-product` | Inventory journeys, screens, content, current defects, previous decisions, and evidence before proposing changes. | Current-state audit with evidence |
| `map-stakeholders-decisions` | Identify users, buyers, operators, sponsors, approvers, dependencies, and who can make each decision. | Stakeholder and decision map |
| `plan-design-engagement` | Choose the smallest useful discovery, design, validation, and delivery activities; estimate effort and dependencies. | Design work plan |
| `facilitate-design-kickoff` | Align the team on the problem, vocabulary, outcomes, collaboration rules, risks, and definition of done. | Kickoff agenda and decision record |
| `plan-design-workshop` | Select participants, accessible activities, timing, materials, facilitation methods, and synthesis approach. | Workshop plan and outputs |
| `manage-design-assumptions` | Separate known facts, assumptions, hypotheses, constraints, and unresolved questions; assign owners and next checks. | Assumption and risk register |
| `record-design-decisions` | Capture alternatives, evidence, rationale, tradeoffs, approvers, review dates, and consequences. | Decision record |

#### 02. Product and business strategy

Connect design decisions to user and business outcomes.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `frame-product-vision` | Describe the people served, durable need, intended benefit, strategic direction, and boundaries. | Vision and positioning brief |
| `map-business-model` | Map buyers, users, value exchange, revenue or funding, operating costs, incentives, and partner dependencies. | Business-model map |
| `segment-product-audience` | Distinguish user, buyer, operator, and administrator segments by needs and context; mark unvalidated segmentation. | Evidence-linked segment map |
| `define-value-proposition` | Connect a specific audience problem to meaningful benefits and plausible differentiation. | Value proposition and evidence gaps |
| `analyze-market-competition` | Compare competitors, substitutes, existing workarounds, and adjacent products using observable evidence. | Competitive opportunity matrix |
| `define-product-outcomes` | Connect strategic goals to user outcomes, leading signals, guardrails, and ownership. | Outcome and measurement tree |
| `plan-product-scope` | Set MVP boundaries, risky assumptions, feasibility dependencies, and what can be learned with a smaller release. | Scope and sequencing proposal |
| `prioritize-product-opportunities` | Compare opportunities by impact, evidence, effort, risk, and strategic fit without disguising uncertain estimates as facts. | Prioritized opportunity backlog |

#### 03. Context and ecosystem discovery

Understand the environment around the interface.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `map-service-ecosystem` | Map organizations, actors, channels, information exchanges, incentives, and dependencies. | Ecosystem map |
| `study-domain-language` | Capture domain entities, terminology, aliases, abbreviations, business meaning, and unresolved definitions. | Domain glossary |
| `audit-existing-evidence` | Review prior research, analytics, tickets, sales feedback, operational logs, and study limitations. | Evidence inventory and gaps |
| `map-current-work` | Describe the actual sequence of activities, handoffs, workarounds, tools, and exceptions. | Current-state workflow |
| `assess-technical-constraints` | Review APIs, data availability, latency, architecture, integrations, supported hardware, and implementation limits with engineers. | Feasibility and constraint brief |
| `map-policy-constraints` | Identify applicable organizational policies, jurisdiction questions, accessibility obligations, and specialist review dependencies. | Policy applicability register |
| `study-use-environment` | Assess connectivity, noise, light, posture, gloves, interruptions, shared devices, language, and digital confidence. | Context-of-use profile |
| `map-dependencies-risks` | Identify cross-team, vendor, operational, data, and release dependencies; assign mitigation owners. | Dependency and risk map |

#### 04. Research planning and operations

Make research appropriate, ethical, and repeatable.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `frame-research-questions` | Translate decisions and uncertainties into answerable research questions and hypotheses. | Research question and decision map |
| `select-research-method` | Choose qualitative, quantitative, mixed, evaluative, or exploratory methods based on the decision and available evidence. | Method rationale |
| `plan-research-study` | Define study scope, sampling rationale, logistics, analysis plan, success criteria, and limitations. | Research plan |
| `recruit-research-participants` | Define inclusion and exclusion criteria, screeners, accessibility accommodations, incentives, and recruitment risks. | Recruitment plan and screener |
| `prepare-research-consent` | Plan informed consent, recording permission, data minimization, retention, withdrawal, and appropriate specialist review. | Consent and data-handling materials |
| `write-research-protocol` | Prepare neutral interview prompts or tasks, observer guidance, note templates, and pilot checks. | Study protocol |
| `run-research-logistics` | Coordinate schedules, accessible tools, interpreters, devices, observers, backup plans, and participant communication drafts. | Session operations checklist |
| `govern-research-repository` | Set access, taxonomy, evidence links, anonymization, retention, expiry, and reuse rules for research records. | Research repository structure |

#### 05. Qualitative research

Understand behavior and context without inventing participants.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `conduct-user-interviews` | Run or support neutral interviews about real experiences; distinguish direct observation from interpretation. | Interview notes and evidence links |
| `conduct-contextual-inquiry` | Observe real tasks in context, probe relevant behavior, and document environment and workarounds. | Contextual observation record |
| `plan-field-ethnography` | Define field access, observation focus, researcher effects, ethical constraints, and interpretation boundaries. | Fieldwork plan and findings structure |
| `run-diary-study` | Plan longitudinal prompts, participation cadence, burden, follow-up interviews, and analysis. | Diary protocol and longitudinal findings |
| `facilitate-co-design` | Create inclusive activities with users and staff, preserve minority views, and separate generated ideas from validated needs. | Co-design outputs |
| `research-expert-workflows` | Study high-skill practices, shortcuts, exception handling, tacit knowledge, and risks of oversimplification. | Expert workflow model |
| `analyze-support-conversations` | Code support contacts, call transcripts, reviews, and complaints with privacy controls and sampling caveats. | Support theme analysis |
| `research-nonusers-churn` | Investigate abandonment, non-adoption, switching, barriers, and accessibility exclusion without assuming causes. | Barrier and churn findings |

#### 06. Quantitative research

Measure patterns and uncertainty appropriately.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `design-user-survey` | Define the decision, sampling approach, neutral questions, response options, accessibility, and pilot review. | Survey and analysis plan |
| `assess-research-sampling` | Review coverage, selection bias, missing groups, sample limitations, and when specialist statistical planning is needed. | Sampling assessment |
| `analyze-product-usage` | Inspect valid event definitions, cohorts, task pathways, missing data, and confounding before interpreting behavior. | Usage analysis |
| `run-attitudinal-measurement` | Select an appropriate satisfaction or usability instrument; preserve wording, scoring, context, and limitations. | Instrument plan and interpreted scores |
| `analyze-behavioral-benchmarks` | Compare task success, errors, effort, and time with a defined baseline and comparable conditions. | Benchmark report |
| `analyze-survey-results` | Clean responses, report distributions and uncertainty, inspect segments, and distinguish correlation from causal evidence. | Survey analysis |
| `analyze-search-logs` | Study query intent, reformulation, zero results, relevance issues, and privacy-sensitive terms. | Search behavior findings |
| `review-statistical-claims` | Check denominators, missingness, effect size, uncertainty, comparisons, and whether the evidence supports the claim. | Measurement quality review |

#### 07. Research synthesis and evidence

Turn observations into traceable design decisions.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `code-research-evidence` | Create codes, preserve source links, compare interpretations, and distinguish frequency from importance. | Coded evidence set |
| `synthesize-research-themes` | Group related observations, document counterexamples, and avoid treating affinity clusters as proof. | Theme map |
| `write-research-insights` | Connect an evidenced observation to a meaningful explanation, impact, and design implication; label inference. | Evidence-linked insights |
| `model-user-needs` | State user needs independently of proposed features and identify strength of evidence. | User-needs register |
| `build-evidence-based-personas` | Create behavioral archetypes grounded in research; label provisional models and avoid invented biographies. | Persona or behavioral archetype set |
| `model-jobs-to-be-done` | Describe situations, desired progress, forces, constraints, and hiring or switching criteria. | Job and forces model |
| `map-user-journey` | Map stages, tasks, touchpoints, emotions only when evidenced, pain points, and opportunities. | Current or future journey map |
| `present-research-findings` | Communicate decisions, key evidence, limitations, conflicting findings, and next actions. | Research readout |

#### 08. Problem and opportunity definition

Choose which problem deserves design effort.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `write-problem-statement` | Specify affected people, context, unmet need, impact, current evidence, and boundaries. | Problem statement |
| `find-root-causes` | Explore plausible contributing causes using evidence; separate UI symptoms from policy, data, and operational causes. | Causal hypothesis map |
| `map-opportunity-tree` | Connect a desired outcome to user opportunities, potential solutions, and assumption tests. | Opportunity solution tree |
| `frame-how-might-we` | Create appropriately scoped ideation questions without presupposing a solution. | Opportunity prompts |
| `prioritize-user-problems` | Compare problem severity, prevalence, exclusion, risk, and evidence confidence. | Problem priority matrix |
| `define-design-principles` | Turn product values and context into actionable decision rules with concrete examples. | Design principles |
| `define-success-criteria` | Specify observable user outcomes, acceptance conditions, guardrails, and evidence needed to assess success. | Success criteria |
| `write-design-brief` | Consolidate the problem, audience, scope, constraints, evidence, outcomes, deliverables, and unresolved questions. | Decision-ready design brief |

#### 09. Service and systems design

Design the whole service across digital and physical channels.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `create-service-blueprint` | Connect customer actions with frontstage staff, backstage operations, systems, policies, evidence, and failure points. | Service blueprint |
| `design-channel-handoffs` | Specify continuity between web, mobile, phone, email, physical locations, and human support. | Channel handoff specification |
| `map-system-feedback` | Model reinforcing effects, delays, dependencies, incentives, and unintended consequences. | System relationship map |
| `design-operational-service` | Define staff tools, queues, ownership, service levels, escalations, training, and exception handling. | Operating-model design |
| `design-assisted-service` | Support people who need help through proxies, assisted digital channels, accessible support, and safe delegation. | Assisted-service journey |
| `design-service-recovery` | Plan what happens after missed appointments, failed deliveries, lost documents, or other service failures. | Recovery blueprint |
| `design-physical-digital-journey` | Align physical wayfinding, check-in, hardware, paperwork, and digital identity or status. | Joined-up journey specification |
| `evaluate-service-capacity` | Assess demand, queue expectations, staffing dependencies, bottlenecks, and customer-facing waiting information. | Capacity and waiting experience plan |

#### 10. Requirements and business logic

Make behavior explicit enough to design and build.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `clarify-product-requirements` | Find ambiguous language, missing actors, conflicting requirements, dependencies, and unanswered decisions. | Clarification log and requirement summary |
| `write-user-stories` | Describe actor, goal, benefit, scope, and dependencies without forcing every requirement into one format. | User-story set |
| `write-acceptance-criteria` | Specify testable behavior, permissions, state transitions, error cases, and examples. | Acceptance criteria |
| `model-domain-data` | Define entities, relationships, identifiers, field meanings, data provenance, and lifecycle states. | Conceptual data model |
| `model-business-rules` | Represent calculations, eligibility, dependencies, priorities, exceptions, and precedence in reviewable tables. | Business-rule and decision tables |
| `design-role-permissions` | Specify who can see, create, edit, approve, export, delegate, or administer each object in each state. | Role and permission matrix |
| `map-requirement-coverage` | Trace requirements to journeys, screens, content, tests, metrics, and open gaps. | Traceability matrix |
| `design-exception-paths` | Cover cancellations, partial outcomes, invalid inputs, missing data, retries, reversals, and operational overrides. | Exception and edge-case matrix |

#### 11. Information architecture

Make information and objects understandable and findable.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `inventory-content-objects` | Inventory pages, documents, objects, owners, audiences, duplication, quality, and lifecycle status. | Content and object inventory |
| `model-product-information` | Define the relationships and mental model behind objects, content, navigation, and actions. | Information architecture model |
| `design-taxonomy-metadata` | Create categories, tags, attributes, controlled vocabulary, aliases, and governance rules. | Taxonomy and metadata schema |
| `design-site-structure` | Organize pages, product areas, hierarchies, relationships, and routes around user tasks. | Sitemap or product structure |
| `design-navigation-system` | Specify global, local, contextual, breadcrumb, tab, and in-page navigation with state behavior. | Navigation specification |
| `run-card-sorting` | Plan open, closed, or hybrid sorting, participant selection, accessible tasks, and cautious interpretation. | Card-sort study and findings |
| `run-tree-testing` | Validate findability through task-based navigation tests with clear success definitions. | Tree-test findings |
| `design-findability-model` | Connect navigation, search, browse, cross-links, labels, and recovery from dead ends. | Findability strategy |

#### 12. Content design and UX writing

Give people the information they need to act.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `plan-product-content` | Define content needs, channels, ownership, lifecycle, source of truth, and success measures. | Content strategy |
| `write-interface-copy` | Write labels, actions, hints, descriptions, empty states, and success messages in context. | UI copy specification |
| `write-error-recovery-copy` | Explain the problem, preserve dignity, identify the affected item, and provide a useful recovery action. | Error-message matrix |
| `define-voice-tone` | Set consistent voice and adapt tone to risk, urgency, user emotion, and context. | Voice and tone guide |
| `design-content-hierarchy` | Organize headings, summaries, detail, disclosure, links, and reading order around user tasks. | Content hierarchy |
| `design-help-education` | Create contextual help, onboarding education, documentation, tutorials, and escalation routes. | Help and learning plan |
| `audit-content-quality` | Review clarity, accuracy, reading burden, duplication, accessibility, findability, and maintenance. | Content audit |
| `govern-content-lifecycle` | Set authoring, approval, translation, review, archive, and removal workflows. | Content governance model |

#### 13. Concept generation and selection

Explore options before committing to a direction.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `generate-design-concepts` | Explore several materially different responses to the problem and note their assumptions. | Concept alternatives |
| `facilitate-design-studio` | Run individual sketching, sharing, critique, and iteration with accessible participation. | Design-studio outputs |
| `run-codesign-ideation` | Use user and staff participation to generate concepts while documenting whose perspectives are missing. | Participatory concept set |
| `explore-adjacent-patterns` | Study relevant patterns from other domains and assess whether their context transfers. | Pattern comparison |
| `storyboard-user-scenario` | Show context, trigger, action, system behavior, handoffs, and outcome. | Scenario storyboard |
| `evaluate-concept-options` | Compare user value, feasibility, viability, inclusivity, risk, and evidence across options. | Concept evaluation matrix |
| `test-risky-assumptions` | Select lightweight experiments to test desirability, usability, feasibility, or viability assumptions. | Assumption test plan |
| `sequence-design-experiments` | Order learning activities by uncertainty, decision impact, cost, and dependencies. | Learning roadmap |

#### 14. Task flows and state models

Specify how people progress through a task.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `analyze-user-tasks` | Break tasks into goals, subtasks, dependencies, frequency, expertise, errors, and interruptions. | Task analysis |
| `map-task-flows` | Describe a task from entry to completion, including decisions, alternate paths, and exits. | Task-flow diagram |
| `map-user-flows` | Connect actors, entry points, screens, decisions, and outcomes across a journey. | User-flow diagram |
| `create-wireflows` | Connect low-fidelity screen structure with navigation and interaction decisions. | Wireflow |
| `model-interface-states` | Define states, events, transitions, guards, side effects, and recovery for interactive objects. | State-transition model |
| `design-interrupted-work` | Specify save and resume, abandonment, drafts, timeout recovery, and changed context. | Interruption and resume specification |
| `design-cross-session-continuity` | Define deep links, restored state, device handoffs, shared links, and account-dependent continuity. | Continuity rules |
| `review-flow-complexity` | Check unnecessary decisions, repeated entry, loops, dead ends, workload, and completion clarity. | Flow simplification review |

#### 15. Interaction behavior

Define the behavior behind visual controls.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `choose-interaction-patterns` | Select interaction patterns by user intent, platform convention, accessibility, frequency, and consequence. | Pattern rationale |
| `specify-component-states` | Define enabled, disabled, focused, hovered, pressed, selected, loading, invalid, and unavailable states as applicable. | Component state matrix |
| `design-input-behavior` | Specify touch, pointer, keyboard, pen, voice, gaze, controller, and assistive alternatives as relevant. | Input interaction specification |
| `design-feedback-affordances` | Make available actions, system status, progress, feedback, and completion perceivable. | Affordance and feedback specification |
| `design-direct-manipulation` | Specify drag, reorder, resize, select, snap, precision, constraints, and equivalent non-drag controls. | Manipulation behavior |
| `design-overlays-disclosure` | Choose dialogs, drawers, sheets, popovers, tooltips, inline expansion, and their dismissal and focus rules. | Overlay and disclosure specification |
| `design-command-efficiency` | Support shortcuts, command palettes, repeat actions, selection, undo, and expert workflows. | Efficiency interaction model |
| `design-progressive-complexity` | Expose capabilities at the right moment while keeping essential actions discoverable. | Progressive disclosure plan |

#### 16. Forms, input, and validation

Help users enter correct information with minimal effort.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `design-form-structure` | Group fields, sequence questions, choose single-page or stepped flows, and minimize repeated entry. | Form structure and field inventory |
| `select-input-controls` | Match controls to data, task, precision, device, accessibility, and available values. | Control selection specification |
| `specify-field-behavior` | Define labels, hints, examples, defaults, formats, masks, limits, autocomplete, and input modes. | Field behavior matrix |
| `design-dependent-fields` | Specify conditional visibility, dependencies, recalculation, preserved values, and effects of changing prior answers. | Dependency rules |
| `design-validation-recovery` | Plan validation timing, inline messages, error summaries, server failures, preserved data, and focus recovery. | Validation matrix |
| `design-multistep-forms` | Define step structure, progress, navigation, review, save and resume, branching, and completion. | Multistep form specification |
| `design-file-capture-upload` | Specify file choice, camera or scanner capture, types, limits, progress, preview, retries, cancellation, and failed processing. | Upload and capture flow |
| `design-review-submit` | Support review, corrections, authorization where relevant, duplicate-submit prevention, confirmation, and receipts. | Submission flow |

#### 17. Search, browse, and discovery

Support purposeful finding and exploration.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `design-search-entry` | Specify entry points, query input, suggestions, autocomplete, keyboard behavior, and recent searches. | Search entry specification |
| `design-search-results` | Define result anatomy, relevance signals, highlighting, pagination, previews, and actions. | Search result pattern |
| `design-filters-facets` | Specify filter types, counts, dependencies, application timing, applied chips, reset, and persistence. | Filter and facet behavior |
| `design-sort-group-controls` | Define ordering, grouping, defaults, clear labels, group totals, and behavior after data changes. | Sort and grouping rules |
| `design-browse-discovery` | Organize categories, recommendations, related items, progressive refinement, and exploration entry points. | Browse model |
| `design-search-recovery` | Handle no results, spelling, ambiguous queries, missing permissions, stale indexes, and alternative actions. | Search recovery states |
| `design-saved-searches` | Specify saving, naming, editing, sharing, alerts, ownership, and changed criteria. | Saved-search lifecycle |
| `evaluate-search-relevance` | Connect representative queries and user tasks to relevance criteria, findability tests, and feedback. | Search evaluation plan |

#### 18. Data-heavy and enterprise interfaces

Support complex work without hiding business meaning.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `design-data-tables` | Specify columns, row identity, density, sorting, selection, pinned content, expansion, keyboard behavior, and responsive alternatives. | Table interaction specification |
| `design-analytics-dashboards` | Connect role-specific decisions to metrics, hierarchy, comparison, drill-down, freshness, and actionable context. | Dashboard specification |
| `design-data-visualizations` | Match chart to question and data; specify scales, uncertainty, comparisons, accessible alternatives, and interaction. | Chart specification |
| `design-bulk-operations` | Define scope, all-pages selection, eligibility, partial success, confirmation, progress, cancellation, and audit feedback. | Bulk action flow |
| `design-approval-workflows` | Specify ownership, queues, delegation, thresholds, multi-step approvals, rejection reasons, and exceptional routes. | Approval state model |
| `design-import-export` | Define scope, columns, formats, preview, validation, background processing, failures, privacy, and downloadable outcomes. | Import and export specification |
| `design-data-editing` | Specify inline versus dedicated editing, drafts, optimistic changes, conflicts, recalculation, and commit boundaries. | Editing behavior |
| `design-audit-history` | Represent versions, actors, dates, changes, reasons, attachments, visibility, and recovery or comparison. | History and audit pattern |

#### 19. Identity, accounts, and permissions

Make account access understandable and recoverable.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `design-registration-onboarding` | Specify account creation, invitations, eligibility, verification, initial setup, and account linking. | Account onboarding flow |
| `design-authentication` | Design sign-in, passkeys or other approved methods, SSO, multi-factor steps, device trust, and session behavior with security specialists. | Authentication flow |
| `design-account-recovery` | Define identity recovery, lost-device paths, lockouts, verification status, and safe support handoffs. | Recovery flow |
| `design-access-management` | Translate roles and policies into invitations, provisioning, access requests, and understandable denials. | Access management UI |
| `design-account-settings` | Organize profile, preferences, notifications, devices, security, connected apps, and billing settings. | Settings architecture |
| `design-workspace-switching` | Specify tenant or organization selection, active-context visibility, remembered context, and cross-tenant mistakes. | Workspace switching behavior |
| `design-consent-privacy-controls` | Support understandable consent choices, preference changes, data access, exports, revocation, and deletion requests. | Privacy control flow |
| `design-account-exit` | Specify deactivation, deletion, ownership transfer, subscriptions, data consequences, waiting states, and confirmation. | Account exit flow |

#### 20. Transactions and product lifecycles

Design complete object and transaction lifecycles.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `design-object-lifecycle` | Map creation, draft, review, publication, updates, suspension, archive, restoration, and deletion as relevant. | Object lifecycle specification |
| `design-checkout-payment` | Specify review, totals, payment states, authorization, confirmation, failure recovery, and duplicate-action protection. | Payment journey |
| `design-billing-subscriptions` | Represent plans, metering, trials, invoices, renewals, upgrades, downgrades, cancellations, and outstanding charges. | Billing lifecycle |
| `design-booking-scheduling` | Handle availability, constraints, time zones, temporary holds, conflicts, rescheduling, cancellations, and reminders. | Booking model |
| `design-refunds-reversals` | Show eligibility, amount, authorization, reasons, processing states, partial outcomes, and final confirmation. | Reversal or refund flow |
| `design-notification-system` | Define triggers, audience, urgency, channel, consent, grouping, frequency, delivery failures, and preferences. | Notification policy and patterns |
| `design-collaborative-work` | Specify sharing, ownership, comments, mentions, presence, real-time edits, version conflicts, and asynchronous handoffs. | Collaboration model |
| `design-transaction-reconciliation` | Represent pending versus completed work, mismatched records, partial settlement, disputes, and operational follow-up. | Reconciliation and dispute flow |

#### 21. Visual UI foundations

Create clear, consistent visual communication.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `define-visual-direction` | Translate brand, audience, task context, and product values into several defensible visual directions. | Visual direction and rationale |
| `design-layout-hierarchy` | Specify alignment, grouping, reading order, emphasis, composition, and relationships between content and actions. | Layout specification |
| `design-typography-system` | Choose appropriate typefaces, hierarchy, sizes, line lengths, spacing, numeric styles, script coverage, and scaling behavior. | Typography specification |
| `design-color-system` | Define semantic color roles, contrast, charts, statuses, themes, and non-color cues. | Color specification |
| `design-spacing-grid` | Define grids, spacing, sizing, alignment, density, and responsive relationships without treating a token scale as a universal rule. | Spacing and layout tokens |
| `design-icons-imagery` | Choose or commission icons, images, illustration, and data assets; define meaning, consistency, accessibility, and rights. | Visual asset specification |
| `design-themes-surfaces` | Specify light, dark, high-contrast, depth, borders, materials, elevation, and system preference behavior. | Theme and surface specification |
| `review-visual-craft` | Check optical alignment, consistency, hierarchy, typography, imagery, density, and realistic content at supported sizes. | Visual quality review |

#### 22. Components and reusable patterns

Design reusable controls with complete behavior.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `design-action-components` | Specify buttons, links, icon actions, split actions, menus, labels, hierarchy, loading, and disabled behavior. | Action component specification |
| `design-navigation-components` | Specify tabs, rails, sidebars, breadcrumbs, pagination, steppers, and active or overflow states. | Navigation component specification |
| `design-input-components` | Specify input fields, pickers, selects, comboboxes, toggles, sliders, date controls, and validation hooks. | Input component specification |
| `design-information-components` | Specify cards, lists, badges, status labels, tooltips, accordions, descriptions, and structured metadata. | Information component specification |
| `design-feedback-components` | Specify alerts, banners, snackbars, progress, skeletons, spinners, inline feedback, and persistence. | Feedback component specification |
| `design-container-components` | Specify dialogs, sheets, drawers, panels, split views, resize behavior, and nested interaction limits. | Container component specification |
| `design-page-patterns` | Specify common list-detail, record, settings, overview, form, error, and completion page compositions. | Page pattern library |
| `audit-component-reuse` | Identify variants, duplication, inconsistent behavior, missing states, over-generalization, and reuse opportunities. | Component consolidation plan |

#### 23. Responsive and adaptive design

Adapt behavior to available space and input capability.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `plan-adaptive-behavior` | Define layout changes by content, available window space, input, posture, and user needs. | Adaptive behavior matrix |
| `design-fluid-layouts` | Specify reflow, wrapping, min/max constraints, intrinsic sizing, spacing, and container behavior. | Fluid layout rules |
| `design-content-priority` | Decide what reflows, changes presentation, becomes supplementary, or stays essential at limited sizes. | Content priority map |
| `adapt-navigation-layout` | Translate navigation and information hierarchy across compact, medium, and expanded contexts. | Responsive navigation specification |
| `adapt-data-dense-views` | Specify tables, charts, multi-pane content, toolbars, and bulk actions for constrained viewports. | Adaptive data-view patterns |
| `design-window-posture-changes` | Handle resizing, orientation, folding, multitasking, safe areas, on-screen keyboards, and state preservation. | Window and posture transition rules |
| `design-cross-input-adaptation` | Support touch, pointer, keyboard, pen, controller, and other inputs without relying on screen size alone. | Input capability adaptation plan |
| `verify-adaptive-coverage` | Review representative sizes, zoom, text scaling, content extremes, input changes, and device configurations. | Adaptive verification matrix |

#### 24. Design systems

Maintain a shared design language connected to implementation.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `audit-design-system` | Inventory foundations, tokens, components, patterns, code alignment, accessibility, documentation, and adoption gaps. | Design-system audit |
| `architect-design-tokens` | Define primitive, semantic, and component tokens; specify themes, naming, ownership, and code mapping. | Token architecture |
| `architect-component-library` | Define component boundaries, APIs or properties, variants, composition, accessibility, and design-code relationships. | Component architecture |
| `document-component-usage` | Explain intent, anatomy, behavior, content, accessibility, examples, constraints, and when another pattern is better. | Component documentation |
| `govern-system-contributions` | Define contribution criteria, review, ownership, release processes, exceptions, and change communication. | Contribution and governance model |
| `plan-system-adoption` | Map migration paths, tooling, education, adoption measures, product constraints, and support. | Adoption plan |
| `manage-system-versions` | Specify releases, compatibility, breaking changes, deprecation, and migration guidance. | Versioning and deprecation plan |
| `measure-system-health` | Track usage, consistency, contribution flow, accessibility, support burden, and design-code divergence. | System health scorecard |

#### 25. Accessibility and inclusive design

Include diverse abilities throughout research, design, and implementation.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `plan-inclusive-design` | Identify excluded groups, situational constraints, participation needs, and relevant accessibility targets early. | Inclusion and accessibility plan |
| `review-visual-accessibility` | Assess contrast, non-color cues, zoom, text scaling, reflow, focus visibility, and visual presentation. | Visual accessibility findings |
| `specify-keyboard-focus` | Define keyboard access, order, focus movement and restoration, shortcuts, escape behavior, and modal boundaries. | Keyboard and focus specification |
| `specify-screen-reader-experience` | Define structure, names, roles, values, descriptions, state announcements, errors, and reading order. | Semantic and announcement specification |
| `design-cognitive-accessibility` | Reduce memory burden, jargon, ambiguity, time pressure, distraction, and unnecessary complexity. | Cognitive accessibility review |
| `design-motor-input-access` | Provide adequate targets, alternatives to complex gestures and dragging, forgiving controls, and compatible input paths. | Motor and input accessibility plan |
| `design-accessible-media` | Specify captions, transcripts, audio description where applicable, player controls, sound alternatives, and motion preferences. | Media accessibility specification |
| `validate-accessibility` | Combine design inspection, automated implementation checks, manual assistive-technology evaluation, and research with disabled users as appropriate. | Accessibility evaluation and remediation plan |

#### 26. Localization and internationalization

Design for languages, scripts, and regional conventions.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `plan-product-localization` | Identify languages, regions, scripts, translation workflows, content ownership, and local research needs. | Localization strategy |
| `design-rtl-bidirectional` | Specify directionality, mirroring exceptions, mixed-script values, ordering, icons, and reading or focus behavior. | RTL and bidirectional specification |
| `design-locale-formatting` | Define dates, calendars, time zones, numbers, currencies, units, addresses, names, and phone formats. | Locale formatting matrix |
| `design-translation-resilience` | Handle expansion, variable strings, pluralization, grammar, truncation, wrapping, and pseudolocalization. | Translation resilience rules |
| `adapt-cultural-context` | Review imagery, symbols, examples, sensitive content, local expectations, and assumptions with appropriate local expertise. | Cultural adaptation review |
| `design-language-switching` | Specify language discovery, remembered choice, translated versus untranslated content, and fallback behavior. | Language-switching flow |
| `design-regional-variation` | Represent region-specific fields, features, policies, eligibility, documents, and content without duplicating the whole product. | Regional variation matrix |
| `verify-localized-experience` | Review translations in context, real fonts, RTL, data formats, accessibility, and regional task completion. | Localization QA report |

#### 27. Motion, sound, and haptics

Use sensory feedback to explain state and support action.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `define-motion-language` | Set motion purposes, duration and easing roles, hierarchy, restraint, and relationship to product character. | Motion principles and tokens |
| `design-state-transitions` | Explain entry, exit, hierarchy, object continuity, layout changes, and state changes through animation. | Transition specification |
| `design-microinteractions` | Specify triggers, state rules, feedback, repetition, and edge cases for small interactions. | Microinteraction behavior |
| `design-loading-progress` | Choose determinate or indeterminate progress, placeholders, delays, cancellation, and truthful waiting information. | Progress and waiting specification |
| `design-gesture-motion` | Specify direct manipulation, physics expectations, interruptibility, reversal, and non-gesture alternatives. | Gesture-motion specification |
| `design-product-sound` | Define sound purpose, urgency, context, user control, quiet environments, and visual or haptic equivalents. | Sound behavior specification |
| `design-haptic-feedback` | Specify meaningful haptic events, intensity roles, device limits, user preferences, and alternatives. | Haptic specification |
| `verify-motion-comfort` | Check reduced-motion behavior, flashing, vestibular comfort, user control, performance, and interruption. | Sensory accessibility review |

#### 28. AI, conversation, and human-machine interaction

Design for uncertain system behavior and appropriate user control.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `assess-ai-product-fit` | Identify the user need, whether AI is appropriate, failure consequences, non-AI alternatives, and evaluation requirements. | AI opportunity and risk brief |
| `design-ai-expectations` | Communicate capabilities, limitations, data use, intended role, provenance, and uncertainty without false precision. | AI expectation and trust specification |
| `design-conversational-flows` | Specify intent handling, turns, clarification, interruption, repair, fallback, context, and human handoff. | Conversation model |
| `design-generative-workspace` | Specify prompt entry, source context, streaming, partial results, stop, retry, compare, edit, cite, and export. | Generative interaction specification |
| `design-agent-control` | Define permissions, plans, previews, action scope, approval points where needed, cancellation, progress, and undo or recovery. | Agent control model |
| `design-ai-failure-recovery` | Handle incorrect, irrelevant, missing, unsafe, or inconsistent outputs; enable correction and appropriate escalation. | AI failure and recovery matrix |
| `design-ai-personalization` | Specify memory visibility, preference control, correction, reset, privacy, and behavior as the model changes. | Personalization control specification |
| `evaluate-human-ai-experience` | Evaluate task value, output quality, accessibility, overreliance, recovery, subgroup effects, and change over time. | Human-AI evaluation plan |

#### 29. Prototyping and technical feasibility

Choose artifacts that answer a concrete design question.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `choose-prototype-fidelity` | Select sketches, wireframes, interactive, coded, service, or hardware prototypes based on the uncertainty being tested. | Prototype strategy |
| `create-low-fidelity-prototype` | Represent structure, content priority, task progression, and alternatives without premature visual polish. | Low-fidelity prototype |
| `create-interactive-prototype` | Represent key tasks, realistic content, conditional states, and meaningful interactions. | Interactive prototype |
| `create-coded-prototype` | Use implementation to test real layout, accessibility, input behavior, performance, or data interactions. | Coded prototype and limitations |
| `prototype-service-hardware` | Represent roleplay, physical touchpoints, device interactions, handoffs, and environmental constraints. | Service or hardware prototype |
| `prototype-variable-data` | Include realistic distributions, empty and extreme data, changing permissions, and exception cases; label synthetic data. | Prototype data and state set |
| `run-feasibility-spike` | Collaborate with engineering to check uncertain APIs, browser capabilities, hardware, interaction mechanics, and cost constraints. | Feasibility findings |
| `prepare-prototype-for-study` | Verify tasks, links, starting states, reset behavior, accessibility limitations, and capture needs. | Study-ready prototype |

#### 30. Evaluation and validation

Check whether a design helps users achieve the intended outcome.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `run-heuristic-review` | Inspect the design against appropriate heuristics and platform conventions; distinguish expert judgment from observed user evidence. | Heuristic findings with severity rationale |
| `run-cognitive-walkthrough` | Evaluate whether a defined user can discover and complete each task step with the available cues. | Walkthrough findings |
| `plan-usability-evaluation` | Define decisions, participants, representative tasks, success criteria, methods, and analysis. | Usability evaluation plan |
| `conduct-usability-test` | Observe realistic tasks, avoid leading participants, record outcomes and behaviors, and document study limitations. | Usability observations |
| `analyze-usability-findings` | Connect task failures and difficulties to evidence, severity, confidence, consequences, and possible remedies. | Prioritized usability findings |
| `run-comparative-evaluation` | Compare alternatives under appropriate conditions; avoid treating preference alone as proof of better usability. | Comparison findings |
| `validate-content-comprehension` | Assess interpretation of labels, instructions, choices, error messages, and important consequences. | Comprehension findings |
| `prioritize-validation-fixes` | Resolve critical failures, review tradeoffs, assign owners, and plan focused re-evaluation. | Remediation and retest plan |

#### 31. Handoff, implementation, and design QA

Carry design intent into the working product.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `prepare-design-handoff` | Provide flows, behavior, content, assets, data assumptions, responsive rules, open questions, and acceptance conditions. | Implementation-ready handoff |
| `specify-interaction-contracts` | Define states, triggers, side effects, persistence, backend dependencies, and error recovery beyond screen appearance. | Behavior specification |
| `prepare-accessible-assets` | Export appropriate formats, naming, size variants, licensing, text alternatives, and accessibility annotations. | Asset and annotation package |
| `review-design-with-engineering` | Resolve feasibility, architecture, component reuse, scope, dependencies, and implementation choices together. | Engineering review decisions |
| `perform-implementation-design-qa` | Compare the running product with agreed behavior, visuals, content, data states, and supported devices. | Design QA findings |
| `verify-production-content-data` | Check real data, permissions, rounding, labels, documents, status meaning, and freshness with relevant owners. | Data and content validation record |
| `triage-design-defects` | Separate functional, visual, content, accessibility, and systemic issues; assess impact and assign ownership. | Prioritized defect backlog |
| `verify-design-fixes` | Recheck changed behavior and related states, record remaining issues, and update design specifications. | Verification record |

#### 32. Launch and release readiness

Prepare the experience and team for real use.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `plan-design-release` | Define target cohorts, release scope, dependencies, staged exposure, user impact, and measurable success. | Experience release plan |
| `run-launch-readiness-review` | Check critical journeys, accessibility evidence, content, analytics, support readiness, and unresolved risks. | Release readiness assessment |
| `plan-beta-pilot` | Select pilot users, coverage, feedback channels, success thresholds, support, and graduation decisions. | Pilot plan |
| `design-feature-introduction` | Introduce meaningful changes through contextual guidance, release notes, education, and appropriate dismissal. | Feature introduction specification |
| `prepare-service-support` | Equip support and operations with walkthroughs, known issues, explanations, recovery paths, and escalation ownership. | Support readiness materials |
| `plan-rollout-migration` | Design flags, cohort transitions, old/new coexistence, user guidance, and effects on existing work. | Rollout experience plan |
| `define-rollback-experience` | Specify customer-facing behavior if a release is disabled or reversed, including saved work and support guidance. | Rollback experience requirements |
| `run-launch-observation` | Observe initial task completion, feedback, incidents, accessibility issues, and unexpected behavior; coordinate quick decisions. | Launch learning and issue log |

#### 33. Measurement and instrumentation

Make outcomes measurable before interpreting success.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `map-goals-signals-metrics` | Connect user and product goals to observable signals, measures, segments, and meaningful guardrails. | Goals-to-metrics map |
| `define-task-success-metrics` | Specify task completion, errors, effort, time, recovery, and quality with clear denominators and exclusions. | Task measurement definitions |
| `design-event-taxonomy` | Define events, properties, object identity, timing, naming, and versioning without collecting unnecessary personal data. | Tracking specification |
| `plan-analytics-privacy` | Specify consent dependencies, minimization, masking, retention, access, and limits on behavioral recording. | Privacy-aware measurement plan |
| `validate-event-instrumentation` | Verify events against actual actions, duplicate and missing events, timestamps, identity transitions, and test traffic. | Instrumentation QA report |
| `establish-experience-baseline` | Record comparable pre-change behavior, seasonal context, cohorts, sample limits, and known measurement gaps. | Baseline report |
| `design-experience-scorecard` | Combine user, business, accessibility, reliability, and guardrail signals with owners and review cadence. | Experience scorecard |
| `plan-learning-cadence` | Set how results, qualitative evidence, support signals, and roadmap decisions are reviewed over time. | Continuous learning plan |

#### 34. Post-launch diagnosis and continuous research

Understand what happens in real use and why.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `diagnose-funnel-friction` | Inspect valid funnel steps, segment differences, drop-offs, missing events, and competing explanations. | Funnel diagnosis and research questions |
| `analyze-cohorts-retention` | Compare adoption and repeated use by relevant cohorts, accounting for user need and task frequency. | Cohort and retention findings |
| `review-behavioral-recordings` | Where appropriately consented, inspect masked session evidence or interaction aggregates; avoid inferring intent from clicks alone. | Behavioral evidence review |
| `synthesize-voice-of-customer` | Combine tickets, reviews, interviews, account feedback, and community reports while preserving source and sampling caveats. | Customer feedback synthesis |
| `research-live-workflows` | Observe actual production work, workarounds, cross-channel handoffs, and newly emerging needs. | Live-use research findings |
| `investigate-exclusion-regressions` | Identify groups, devices, regions, assistive technologies, or low-connectivity contexts harmed by a change. | Exclusion and regression assessment |
| `review-launch-outcomes` | Compare intended outcomes with actual evidence, explain uncertainty, and identify what the release taught the team. | Post-launch outcome review |
| `prioritize-live-improvements` | Connect evidence to user impact, risk, effort, ownership, and a prioritized improvement backlog. | Continuous-improvement backlog |

#### 35. Experimentation and optimization

Test improvements without overclaiming evidence.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `frame-product-experiment` | Define the problem, hypothesis, mechanism, audience, primary outcome, and guardrails. | Experiment brief |
| `design-experiment-variants` | Create meaningful alternatives with controlled differences and equivalent accessibility quality. | Variant specifications |
| `plan-controlled-experiment` | Define assignment unit, exposure, sample and power needs, duration, exclusions, stopping rules, and statistical review. | Experiment design |
| `validate-experiment-setup` | Check assignment, exposure, instrumentation, cross-device effects, sample imbalance, and implementation differences. | Experiment QA record |
| `interpret-experiment-results` | Review effect sizes, uncertainty, guardrails, segment caveats, multiple comparisons, and practical significance. | Experiment analysis |
| `evaluate-without-ab-test` | Select suitable usability, before/after, longitudinal, or quasi-experimental approaches and state causal limits. | Alternative evaluation plan |
| `decide-experiment-outcome` | Recommend ship, revise, stop, or investigate based on the decision rules, evidence, risk, and user impact. | Experiment decision record |
| `maintain-experiment-learnings` | Record results, null findings, failed hypotheses, context, reusable evidence, and re-evaluation triggers. | Experiment knowledge base |

#### 36. Activation, retention, and responsible growth

Help users achieve recurring value and control their relationship.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `design-first-value-experience` | Reduce unnecessary setup, clarify purpose, support empty states, and help users reach their first meaningful outcome. | Activation journey |
| `diagnose-onboarding-dropoff` | Identify friction and unmet expectations by segment, evidence, device, and task context. | Onboarding diagnosis |
| `design-feature-discovery` | Help the right users discover relevant capabilities through context, search, education, and progressive exposure. | Feature adoption plan |
| `improve-repeat-task-experience` | Support saved preferences, recent work, efficient return paths, reminders when useful, and expert progression. | Repeat-use improvements |
| `design-reengagement` | Offer relevant return paths, understandable preferences, and controlled reminder frequency. | Re-engagement experience |
| `design-pricing-plan-choice` | Make plans, entitlements, limits, charges, renewals, and consequences understandable without hidden defaults. | Plan comparison and upgrade flow |
| `research-retention-churn` | Distinguish completed user need, product failure, cost, switching, and involuntary loss; identify appropriate remedies. | Retention research and actions |
| `audit-growth-manipulation` | Review coercion, misleading urgency, disguised choices, obstructed cancellation, consent pressure, and harmful metrics. | Responsible growth review |

#### 37. Live service reliability, support, and maintenance

Keep the experience dependable after release.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `design-degraded-service` | Handle slow, unavailable, stale, or partially functioning dependencies with truthful status and useful alternatives. | Degraded-service specification |
| `design-offline-sync-recovery` | Specify queued work, local drafts, reconnection, merge conflicts, retry, device limits, and data freshness. | Offline and sync state model |
| `design-long-running-jobs` | Represent background jobs, progress, cancel limits, resumability, completion notifications, and downloadable outcomes. | Background-job lifecycle |
| `design-incident-communication` | Explain impact, affected tasks, workarounds, updates, resolution, and follow-up in accessible language. | Incident communication drafts and patterns |
| `design-support-escalation` | Connect self-service, diagnostics, support channels, context transfer, ownership, and follow-up. | Support escalation journey |
| `monitor-experience-regressions` | Define experience checks for releases, OS changes, dependencies, permissions, localization, accessibility, and performance. | Regression monitoring plan |
| `manage-experience-debt` | Inventory inconsistencies, workarounds, obsolete patterns, known exclusions, and recurring defects; assign ownership and priorities. | Experience debt backlog |
| `maintain-product-content` | Review help, screenshots, labels, translations, policy references, and obsolete guidance against current behavior. | Content maintenance plan |

#### 38. Evolution, migration, and retirement

Manage long-term change and safe endings.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `assess-redesign-need` | Determine whether problems require targeted fixes, workflow change, system modernization, or broader redesign. | Redesign rationale |
| `plan-legacy-modernization` | Map existing capabilities, expert workflows, dependencies, parity requirements, and phased improvement opportunities. | Modernization experience plan |
| `design-data-migration` | Specify preview, field mapping, validation, reconciliation, failures, ownership, and explanations of changed data. | Migration journey |
| `design-workflow-migration` | Support old/new coexistence, retraining, saved work, bookmarks, integration changes, and critical user groups. | Workflow transition plan |
| `manage-feature-deprecation` | Define usage evidence, replacements, notices, timelines, affected users, support, and exceptions. | Deprecation plan |
| `design-product-merger` | Reconcile accounts, objects, terminology, navigation, permissions, entitlements, and product identities. | Product consolidation plan |
| `design-service-retirement` | Plan notices, alternative services, exports, access changes, support, archive or deletion obligations, and ending states. | Retirement journey |
| `preserve-product-learning` | Archive decisions, research, system patterns, migration findings, and retirement outcomes with clear access and retention. | Reusable product learning record |

#### 39. Design operations, governance, and leadership

Make design work sustainable across people and teams.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `design-team-operating-model` | Clarify roles, team structures, collaboration interfaces, capacity, rituals, and decision rights. | Design operating model |
| `plan-design-capacity` | Balance discovery, delivery, maintenance, research, support, and system work across available capacity. | Capacity and dependency plan |
| `facilitate-design-critique` | Set critique goals, context, evidence, inclusive participation, actionable feedback, and decision ownership. | Critique record |
| `align-design-stakeholders` | Prepare clear options, rationale, tradeoffs, evidence, disagreement records, and decisions. | Stakeholder decision materials |
| `govern-design-quality` | Set proportionate reviews, quality criteria, accountability, evidence expectations, and exception handling. | Design quality governance |
| `measure-design-operations` | Assess workflow health, cycle time, rework, consistency, research access, and outcomes without equating output volume with value. | Design operations scorecard |
| `coach-design-team` | Identify competency gaps, mentoring activities, feedback needs, progression evidence, and learning goals. | Development plan |
| `govern-design-tools-assets` | Manage libraries, file structure, naming, access, procurement, licenses, templates, and tool interoperability. | Tool and asset governance plan |

#### 40. Professional practice and knowledge maintenance

Keep the skill collection credible and useful over time.

| Candidate workflow | Scope and small processes | Primary output |
| --- | --- | --- |
| `audit-design-ethics` | Review user agency, unintended harms, exclusion, persuasive choices, incentives, privacy, and vulnerable-user impacts. | Ethical design assessment |
| `review-privacy-security-ux` | Work with specialists on authentication, data exposure, consent, access, abuse reporting, and recovery without claiming certification. | Privacy and security UX findings |
| `assess-sustainable-experience` | Consider unnecessary data transfer, media weight, hardware constraints, longevity, accessibility, and operating burden. | Sustainability improvement brief |
| `write-design-case-study` | Explain the problem, role, evidence, decisions, outcomes, limitations, and lessons without fabricated impact claims. | Evidence-based case study |
| `plan-design-learning` | Map competency needs across methods, platforms, domains, communication, engineering literacy, and leadership. | Learning roadmap |
| `maintain-design-reference-pack` | Record sources, applicability, versions, jurisdiction, owner, verification dates, rights, and update triggers. | Maintained reference pack |
| `evaluate-design-skill` | Use representative task fixtures and expert review to test usefulness, accuracy, omissions, routing, and output quality. | Skill evaluation record |
| `improve-design-skill-library` | Use failures, overlaps, changed standards, user feedback, and real task results to revise, merge, split, or retire skills. | Skill maintenance backlog |
