# Forms, transactions, tables, and enterprise workflows

Operational guide and topic inventory. Procedures and checks are an original synthesis; use the source register for the authority, inspected portion, and limits of specific references.

### Coverage

| Area | Details to consider |
| --- | --- |
| Field definition | Entity; data type; label; meaning; requiredness; default; hint; format; bounds; input mode; autocomplete; examples; permissions. |
| Conditional input | Dependencies; visibility; eligibility; dynamic options; invalidated answers; recalculation; preservation; server truth. |
| Validation | Timing; synchronous/asynchronous; client/server; field error; summary; focus; correction; preserved values; external dependency. |
| Complex forms | Branches; steps; progress; review; save/resume; document capture; upload; preview; identity; authorization; completion. |
| Tables and collections | Row identity; columns; density; sorting; filtering; grouping; totals; expansion; sticky regions; pagination; virtualization; responsive alternative. |
| Selection and batching | Visible/all matching; changed filters; mixed eligibility; cross-page selection; progress; cancellation; partial outcomes; exports. |
| Transactions | Draft; pending; authorization; processing; complete; failed; unknown outcome; duplicate prevention; retries; reversals; reconciliation. |
| Enterprise work | Queues; approvals; delegation; thresholds; audit; effective dates; versioning; configuration; multi-tenant context; concurrent edits. |

### Procedure

1. Identify the task, object, role, data meaning, and consequence of an incorrect change.
2. Create field, column, action, eligibility, and permission dictionaries using verified domain rules.
3. Minimize repeated entry and inappropriate defaults. Choose controls that match the value space and context.
4. Specify dependencies, validation, save/review/submit boundaries, async checks, and data preservation.
5. Define record identity, filter and grouping rules, totals, selection scope, pagination, and bulk outcomes.
6. Model the entire transaction lifecycle with the backend and operations owners. Distinguish unknown outcome from confirmed failure.
7. Cover locale formats, accessibility, small windows, long values, permissions changing during work, and concurrent changes.
8. Validate representative end-to-end tasks, including correction, interruption, partial completion, and recovery.

### Outputs

Field/column/action specifications; business-rule table; state and selection models; responsive/accessibility behavior; acceptance criteria; test scenarios.

### Quality checks

Zero is distinct from missing; totals have defined meaning; amount precision and currency are explicit; selection scope is clear; retries are safe for the operation; partial results are visible; errors preserve work; approval and audit requirements are traceable.

### Limits and common failures

A visually tabular display does not automatically need an ARIA grid. Avoid duplicating technical widgets where native semantics and simpler interaction meet the task. Never invent eligibility, settlement, tax, clinical, or financial rules from a mock-up.

### Sources to consult

- S19: [APG: Modal dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/). Body excerpts inspected.
- S20: [APG: Combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/). Body excerpts inspected.
- S21: [APG: Grid](https://www.w3.org/WAI/ARIA/apg/patterns/grid/). Body excerpts inspected.
- S22: [WAI Forms Tutorial](https://www.w3.org/WAI/tutorials/forms/). Body excerpts inspected.
- S25: [W3C: Structural RTL markup](https://www.w3.org/International/questions/qa-html-dir.en.html). Body excerpts inspected.
- S31: [Android: Make apps accessible](https://developer.android.com/guide/topics/ui/accessibility/apps). Body excerpts inspected.

### Say the required convention once, and keep errors in the flow

- **State the convention at the top** ("All fields are required unless marked optional"); WCAG 3.3.2 needs required status communicated, and an unexplained asterisk is ambiguous.
- **Errors sit above or below the field,** never to its side: side errors break at 400% zoom and on narrow screens (WCAG 1.4.10).
- **Inputs 16px or larger on mobile** so iOS does not zoom on focus. Show and hide on password fields; accept pasted and autofilled one-time codes as a whole.
- **Default facts** (a detected country), **never decisions** (consent, marketing opt-ins).
- **After submit,** show loading, success and failure states.
