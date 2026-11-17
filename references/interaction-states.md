# Interaction behavior, states, input, and recovery

Operational guide and topic inventory. Procedures and checks are an original synthesis; use the source register for the authority, inspected portion, and limits of specific references.

### Coverage

| Area | Details to consider |
| --- | --- |
| Behavior models | Goals; tasks; events; states; transitions; guards; side effects; persistence; authorization; success criteria. |
| Input | Touch; pointer; keyboard; pen; voice; remote; controller; gaze; hands; switch; assistive input; hardware controls; equivalent paths. |
| Feedback | Affordances; signifiers; mapping; perceived action; status; progress; completion; acknowledgment; uncertainty; error and recovery. |
| Object states | Draft; new; active; selected; edited; invalid; submitting; queued; pending; complete; partial; failed; stale; archived; deleted. |
| Control states | Default; hover; focus-visible; pressed; selected; checked; mixed; expanded; read-only; disabled; loading; error; drag; drop. |
| Overlays | Modal/nonmodal; dialogs; sheets; drawers; popovers; menus; tooltips; focus boundary; initial focus; dismissal; focus return. |
| Manipulation | Select; drag; resize; reorder; snap; scroll; pan; zoom; precision; bounds; cancellation; undo; alternative controls. |
| Efficiency | Shortcuts; commands; batching; defaults; recent work; repetition; expert paths; discoverability; progressive complexity. |
| Interruptions | Back; refresh; timeout; lost network; app suspension; permission changes; conflicting edits; drafts; resume; cross-device transfer. |

### Procedure

1. Identify the user's intent and the domain object being changed. Separate navigation from commands and actual object mutations.
2. Model relevant states and transitions before styling the controls. Include asynchronous, partial, stale, unauthorized, and interrupted states.
3. Define each action's trigger, preconditions, feedback, side effects, persistence, and possible outcomes.
4. Choose a pattern appropriate to the platform and task. Specify dismissal, back behavior, focus, and non-pointer operation.
5. Design normal and alternate inputs together. Provide suitable alternatives to dragging, complex gestures, hover-only information, and precision-dependent interaction.
6. Define cancellation, reversal, and retry with the real transaction semantics. A timeout may mean unknown outcome rather than confirmed failure.
7. Check interruption and concurrent-change paths. Revalidate eligibility or permission when necessary without silently losing useful work.
8. Validate representative tasks in an interactive or running implementation and record what a static mock-up cannot establish.

### Outputs

State-transition table; interaction specification; input/keyboard map; exception matrix; annotations; acceptance criteria.

### Quality checks

Every important action has an observable result; disabled and read-only are distinct; focus and dismissal are specified; recovery is feasible; retries do not duplicate consequential work; expert efficiency preserves novice discoverability.

### Limits and common failures

Visible styling does not implement authorization. A spinner does not define a transaction state. A modal pattern is not appropriate for every interruption. Tooltip text cannot carry essential instructions without a suitable accessible alternative. Normative requirements and APG examples have different status.

### Sources to consult

- S05: [Nielsen: Ten Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/). Body excerpts inspected.
- S19: [APG: Modal dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/). Body excerpts inspected.
- S20: [APG: Combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/). Body excerpts inspected.
- S21: [APG: Grid](https://www.w3.org/WAI/ARIA/apg/patterns/grid/). Body excerpts inspected.
- S38: [Ben Shneiderman: Eight Golden Rules](https://www.cs.umd.edu/users/ben/goldenrules.html). Body excerpts inspected.
- S39: [Don Norman: Affordances and Design](https://jnd.org/affordances-and-design/). Body excerpts inspected.
- S40: [Don Norman: Signifiers](https://jnd.org/signifiers-not-affordances/). Body excerpts inspected.
- S51: [Apple WWDC23: Spatial input](https://developer.apple.com/videos/play/wwdc2023/10073/). Transcript excerpt inspected; playback not reviewed.
