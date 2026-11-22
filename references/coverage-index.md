# Coverage index and depth status

This index supports retrieval and omission checks. Counts describe authored scope, not proof of exhaustive knowledge or specialist validation.

| Asset | Coverage | Depth/status |
| --- | --- | --- |
| Operational guides | 21 guides; 171 grouped areas | Authored procedures, outputs, checks and limits; task-specific verification still required |
| Topic mentions | 1639 indexed mentions; 1265 distinct normalized labels | Labels overlap semantically; do not interpret as independent mastered competencies |
| Named principles | 80 | Classified register; some original-source review remains outstanding |
| Methods/instruments | 56 | Selector and core playbooks; advanced protocols require original-method verification |
| Components/patterns | 106 | Detailed contract plus catalog; not all independently evaluated |
| Lifecycle workflows | 320 across 40 families | Scope catalog routed through the operational guides |
| Context profiles | 30 devices; 16 systems; 58 domains | Starter inventories, not complete verified niche handbooks |
| Small checks | 120 original checks plus foundation additions | Apply when relevant and attach appropriate evidence |
| Sources | 76 records, including 11 video/film resource pages | Inspection and access status recorded per item |

### Guides

| Reference | Grouped coverage |
| --- | --- |
| [Research strategy, evidence, and planning](research-strategy.md) | Decision framing; Study dimensions; Evidence review; Participant coverage; Research operations; Study integrity; Analysis; Measurement literacy; Research assets |
| [Product strategy, service design, and requirements](strategy-service-requirements.md) | Product direction; Problem discovery; Service design; Systems thinking; Requirements; Business analysis; Scope and prioritization; Collaboration |
| [Information architecture, content, and findability](ia-content-findability.md) | Information models; Navigation; Findability research; Search; Recovery; Content craft; Content operations; Comprehension |
| [Interaction behavior, states, input, and recovery](interaction-states.md) | Behavior models; Input; Feedback; Object states; Control states; Overlays; Manipulation; Efficiency; Interruptions |
| [Visual foundations: typography, color, imagery, shape, and depth](visual-foundations.md) | Composition; Typography; Text behavior; Color; Shape; Depth; Icons and media; Expression |
| [Spacing, padding, layout grids, baseline rhythm, and density](spacing-layout.md) | Spacing vocabulary; Scale design; Grid types; Layout behavior; Density; Alignment; Platform units; Exceptions |
| [Design tokens, themes, modes, and design-code alignment](design-tokens.md) | Token levels; Token families; Modes and axes; Naming; Data integrity; Delivery; Testing |
| [Design-system architecture, documentation, style guides, and governance](design-systems.md) | Purpose and scope; Brand and style guide; Foundations; Tokens; Components; Patterns and templates; Design assets; Implementation; Documentation; Governance; Adoption and health |
| [Forms, transactions, tables, and enterprise workflows](forms-tables-enterprise.md) | Field definition; Conditional input; Validation; Complex forms; Tables and collections; Selection and batching; Transactions; Enterprise work |
| [Accessibility, inclusive design, and evidence of conformance](accessibility.md) | Planning; Perception; Operation; Understanding; Semantics; Human variation; Assistive tools; Evaluation; Non-web |
| [Responsive, adaptive, multimodal, and platform-specific design](responsive-platforms.md) | Layout strategy; Changing environments; Input capabilities; Phone/tablet/desktop; Wearable/TV; Spatial; Embedded/public; Resilience; Output channels |
| [Motion, waiting, sound, and haptic interaction](motion-sound-haptics.md) | Motion roles; Motion mechanics; Waiting; Gesture; Audio; Haptics; Comfort |
| [Prototyping, usability evaluation, and design validation](prototyping-evaluation.md) | Fidelity; Test readiness; Expert review; User evaluation; Evidence; Analysis; Technical validation |
| [Implementation, engineering collaboration, performance, and quality assurance](implementation-qa.md) | Handoff; Frontend literacy; Data behavior; Performance UX; Implementation review; QA records; Release support |
| [Metrics, instrumentation, experimentation, and causal limits](metrics-experimentation.md) | Outcome models; Metric definitions; Behavioral analysis; Instrumentation; Experiment design; Interpretation; Alternative methods; Learning |
| [Launch, live operation, support, migration, and retirement](launch-live-retirement.md) | Release readiness; Rollout; Live diagnosis; Resilience; Service support; Continuous improvement; Migration; Retirement |
| [AI, conversational interfaces, agents, and human oversight](ai-agents.md) | Product fit; Expectations; Conversation; Generative workspace; Agentic action; Failure; Personalization; Evaluation |
| [Localization, RTL, scripts, regional rules, and content operations](localization-rtl.md) | Language architecture; Grammar; RTL and scripts; Formats; Typography; Regional behavior; Cultural validation; Operations |
| [Domain knowledge, privacy, security, ethics, and sustainability](domain-privacy-ethics.md) | Domain model; Critical workflows; Privacy; Security UX; Ethics; Trust and safety; Sustainability; Applicability |
| [Design operations, facilitation, professional practice, and skill maintenance](designops-practice.md) | Team operations; Facilitation; Communication; Quality governance; Research and assets; Capability; Portfolio and reporting; Library maintenance |
| [Source research, article and video ingestion, and evidence integrity](evidence-source-ingestion.md) | Source classes; Research origins; Article inspection; Video inspection; Current facts; Claim records; Knowledge operations; Coverage status |

### Depth contract

Operational guidance provides a usable general procedure. Indexed topics provide recall and routing. An applicable requirement needs its actual authoritative source and version. A specialist domain needs real rules, context and qualified review. A performed evaluation needs actual evidence. Keep these levels distinct in all outputs.

### Extending coverage

When a task reveals a missing topic, record the decision it affects, applicable context, needed authority, evidence gap and owner. Add procedural guidance only after researching the method or context; add a realistic evaluation case. Revisit overlapping or obsolete content rather than adding names indefinitely.

### Added in the skill build (16 November 2026)

| File | Purpose |
| --- | --- |
| `craft-defaults.md` | Opinionated starting values for type, spacing, color, components, motion, copy and the accessibility floor |
| `anti-slop.md` | Visual, copy and structural tells of generic AI design, with fixes |
| `making.md` | Producing HTML mocks, codebase UI, Figma work and self-review |
| `critique.md` | Review order, finding format and tone |
| `marketing-pages.md` | Landing pages, conversion, SEO basics |
| `case-studies.md` | Portfolio case studies and presenting work |
| `deceptive-design.md` | Dark patterns, fair alternatives, legal orientation |
| `data-visualization.md` | Chart choice, dashboards, chart accessibility |
| `platform-updates.md` | Liquid Glass, Material 3 Expressive, WCAG 3, EAA, ADA Title II, DTCG status |
| `urdu-arabic-typography.md` | Nastaliq and Naskh sizing, numerals, bidi, mirroring |
| `product-management.md` | PRDs and specs, user stories, vision and strategy, roadmaps, OKRs, competitive analysis, go-to-market, decision quality |
| `component-guides.md` | Per-component rules for buttons, cards, menus, modals, navigation, toasts, progress trackers, search, selection controls, tables, tooltips |
| `screen-recipes.md` | Sign up and log in, password reset, settings, onboarding, checkout, booking, account deletion, activity feeds, support, 404 |

Worked examples live in `examples/`; test cases with pass/fail criteria live in `evals/`. No scripts ship with this skill. For contrast, compute the WCAG 2 ratio as (L1 + 0.05) / (L2 + 0.05), where L1 and L2 are the relative luminance of the lighter and darker sRGB colors; for example #767676 on #FFFFFF is 4.54:1. Compare the unrounded ratio with the threshold and round only for display.
