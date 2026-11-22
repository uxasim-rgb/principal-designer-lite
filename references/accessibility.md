# Accessibility, inclusive design, and evidence of conformance

Operational guide and topic inventory. Procedures and checks are an original synthesis; use the source register for the authority, inspected portion, and limits of specific references.

### Coverage

| Area | Details to consider |
| --- | --- |
| Planning | Applicability; target standard; conformance level; product version; user participation; exclusion; task risk; accountable owners. |
| Perception | Alternatives for images/media; captions; descriptions; contrast; color; resize; zoom; reflow; spacing; low vision; forced colors. |
| Operation | Keyboard; no traps; focus; shortcuts; timing; pause; motion; flashing; targets; drag alternatives; orientation; accessible authentication. |
| Understanding | Language; labels; predictability; help; instructions; errors; redundant entry; consequences; cognitive burden; plain language. |
| Semantics | Structure; landmarks; headings; tables; controls; accessible names; roles; values; state; relationships; status announcements. |
| Human variation | Blind/low vision; deaf/hard of hearing; motor; speech; cognitive/learning; vestibular; temporary/situational barriers; multiple disabilities. |
| Assistive tools | Screen reader; keyboard; switch; voice control; magnification; high contrast; captions; reduced motion; device-native settings. |
| Evaluation | Design annotations; automated rules; manual interaction; assistive technology; disabled-user research; issue severity; remediation; regressions. |
| Non-web | Native software; documents; hardware; closed functionality; physical access; platform APIs; WCAG2ICT scope and limits. |

### Procedure

1. Determine the product and jurisdiction context, supported platforms, applicable requirements, evaluation scope, and target level with the accountable owners.
2. Involve people who experience relevant barriers and plan accessible research and service alternatives.
3. Specify visual, content, semantic, focus, input, and dynamic-update behavior alongside the design.
4. Use appropriate native or standard patterns; treat ARIA pattern examples as informative guidance rather than automatic proof of conformance.
5. Evaluate the running implementation with a proportionate mix of automated checks, keyboard/manual inspection, assistive technology, and user research.
6. Record the exact criterion or requirement, affected task, environment, evidence, consequence, remediation, and limitations.
7. Verify fixes and check relevant regressions across supported combinations.
8. Keep accessibility documentation current as content, dependencies, platforms, and user workflows change.

### Outputs

Applicability and scope; accessible interaction annotations; evaluation matrix; evidence-linked findings; remediation and regression plan.

### Quality checks

Claims name their scope and evidence; automated checks are supplemented appropriately; controls have meaningful semantics; focus behavior is complete; task recovery works; dynamic information is perceivable; non-web context is handled correctly.

### Limits and common failures

A screenshot cannot establish screen-reader behavior or full conformance. A component passing tests does not certify every composition. WCAG2ICT is informative guidance. WCAG 3 remained an incomplete draft at the source check, so it must not silently replace an applicable WCAG 2 conformance target.

#### Target-area decision example

WCAG 2.2 criterion 2.5.8 specifies a 24-by-24 CSS-pixel pointer target or defined exceptions, including a spacing condition (S18). This is not an instruction to make every visual icon 24px. Apply the actual criterion and its exceptions, then check relevant native-platform guidance and the physical input context.

Separate visible control size, hit area, adjacent target spacing, target overlap, task criticality, and motor precision. Test actual implementation rather than inferring the hit area from a screenshot.

#### Evidence record

Record product/version, task, component/state, platform/browser, assistive technology and settings, requirement reference, expected behavior, observed behavior, reproducibility, severity rationale, owner, fix, retest, and remaining limitation. Mark unknowns explicitly.

### Sources to consult

- S15: [Microsoft Inclusive Design 101](https://inclusive.microsoft.design/articles/inclusive-101-guidebook). Body excerpts inspected.
- S16: [WCAG 2.2](https://www.w3.org/TR/WCAG22/). Status and selected criteria inspected.
- S17: [WAI-ARIA APG patterns](https://www.w3.org/WAI/ARIA/apg/patterns/). Pattern index inspected.
- S18: [WCAG 2.2 Understanding: Target size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum). Criterion and exceptions inspected.
- S19: [APG: Modal dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/). Body excerpts inspected.
- S20: [APG: Combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/). Body excerpts inspected.
- S21: [APG: Grid](https://www.w3.org/WAI/ARIA/apg/patterns/grid/). Body excerpts inspected.
- S22: [WAI Forms Tutorial](https://www.w3.org/WAI/tutorials/forms/). Body excerpts inspected.
- S23: [WCAG2ICT](https://www.w3.org/TR/wcag2ict/). Status and scope inspected.
- S24: [W3C: WCAG 3 introduction](https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/). Status inspected.
- S30: [Apple HIG: Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility). Markdown body excerpts inspected.
- S31: [Android: Make apps accessible](https://developer.android.com/guide/topics/ui/accessibility/apps). Body excerpts inspected.
- S54: [W3C: Video captions](https://www.w3.org/WAI/perspective-videos/captions/). Explanation inspected; playback not reviewed.
- S55: [W3C: Accessibility standards and benefits](https://www.w3.org/WAI/videos/standards-and-benefits/). Transcript and explanatory excerpts inspected; playback not reviewed.

### Pointer, orientation and hover

| Criterion | Requirement |
| --- | --- |
| 1.3.4 Orientation (AA) | Do not lock the screen to portrait or landscape unless the orientation is essential |
| 1.4.13 Content on hover or focus (AA) | Tooltips and hover panels can be dismissed (Escape) without moving the pointer or focus, stay open while the pointer moves onto them, and stay until dismissed or no longer relevant |
| 2.5.1 Pointer gestures (A) | Every path-based or multi-finger gesture has a single-pointer alternative |
| 2.5.2 Pointer cancellation (A) | Actions fire on release, not on press, and can be aborted by moving off the target |
| 2.5.7 Dragging movements (AA, new in 2.2) | Every drag (sliders, sortable lists, boards) has a single-pointer alternative that needs no dragging |
| 2.5.8 Target size minimum (AA, new in 2.2) | 24 by 24 CSS px, or spacing so a 24px circle on each target touches no other. Platform targets (44pt Apple, 48dp Material) are larger guidance, not WCAG |
| 3.2.6 Consistent help (A, new in 2.2) | Help mechanisms appear in the same relative order on every page that has them |
| 3.3.7 Redundant entry (A, new in 2.2) | Do not ask again for information already given in the same process |
| 3.3.8 Accessible authentication (AA, new in 2.2) | No cognitive test as the only way to log in; allow paste and password managers |

Not WCAG requirements, and not to be reported as failures: a 16px minimum body size (a house default; WCAG sets no size), pure black text on white (a craft choice), and a three-typeface limit.
