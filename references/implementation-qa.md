# Implementation, engineering collaboration, performance, and quality assurance

Operational guide and topic inventory. Procedures and checks are an original synthesis; use the source register for the authority, inspected portion, and limits of specific references.

### Coverage

| Area | Details to consider |
| --- | --- |
| Handoff | Task context; requirements; flows; state model; content; rules; assets; tokens; layouts; input; semantics; acceptance; open questions. |
| Frontend literacy | DOM/semantics; native widgets; components; APIs; constraints; CSS layout; units; responsive composition; event timing; lifecycle. |
| Data behavior | Source of truth; identity; loading; cache; freshness; permissions; concurrent editing; optimistic changes; partial failures; idempotency. |
| Performance UX | Perceived/actual latency; loading; interaction responsiveness; layout shift; media weight; slow network; low-end hardware; field measurement. |
| Implementation review | Functional behavior; visual craft; content; data meaning; tokens; accessibility; localization; inputs; browsers; platforms; operational routes. |
| QA records | Expected/observed; environment; state; reproducibility; severity; evidence; requirement; owner; fix; retest; regression scope. |
| Release support | Known issues; monitoring; flags; rollout; rollback experience; configuration; migration; documentation; support training. |

### Procedure

1. Review design intent with engineering before implementation commitments. Resolve material feasibility and data assumptions.
2. Specify behavior and acceptance with sufficient precision for construction while allowing engineers to choose appropriate implementation details.
3. Align tokens, components, assets, content, semantics, and responsive rules across design and code.
4. Inspect the running product with representative real data, input methods, permissions, and failure conditions.
5. Assess performance with appropriate field and lab evidence, separating backend work, rendering, interaction delay, and visual instability.
6. Write defects with reproducible context and user impact. Separate systemic causes from isolated cosmetic symptoms.
7. Verify fixes and relevant regressions without repeating unrelated testing indefinitely.
8. Update source artifacts and operational documentation to reflect the actual release.

### Outputs

Implementation contract; feasibility decisions; design-code mapping; performance requirements; QA findings; verification record.

### Quality checks

The running behavior matches agreed intent; accessibility is implemented; field and amount semantics are correct; async states are truthful; relevant environments are checked; remaining risks have owners.

### Limits and common failures

Pixel similarity does not establish correct behavior. A good lab performance score does not prove every user has a good experience. Browser support and library behavior change; verify actual versions. Avoid passing explanatory backend details into user-facing copy unless they help a meaningful user decision.

### Sources to consult

- S17: [WAI-ARIA APG patterns](https://www.w3.org/WAI/ARIA/apg/patterns/). Pattern index inspected.
- S19: [APG: Modal dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/). Body excerpts inspected.
- S20: [APG: Combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/). Body excerpts inspected.
- S21: [APG: Grid](https://www.w3.org/WAI/ARIA/apg/patterns/grid/). Body excerpts inspected.
- S26: [CSS Box Model Level 3](https://www.w3.org/TR/css-box-3/). Scope and selected concepts inspected.
- S27: [CSS Values and Units Level 4](https://www.w3.org/TR/css-values-4/). Status and selected concepts inspected.
- S28: [CSS Logical Properties Level 1](https://www.w3.org/TR/css-logical-1/). Status and scope inspected.
- S29: [CSS Grid Layout Level 2](https://www.w3.org/TR/css-grid-2/). Status and scope inspected.
- S43: [Google: Web Vitals](https://web.dev/articles/vitals). Body excerpts inspected.
