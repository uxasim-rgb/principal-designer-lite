# Small-process checks

120 explicit prompts. Apply checks when relevant; record “not applicable” with a reason where useful. A checklist prompts examination; a checked box needs appropriate evidence. Some checks require a running implementation, real users, domain owners, or specialists.

#### State and feedback

- C001: First use is distinguished from a genuinely empty data set.
- C002: Filtered-empty, permission-empty, and system-error states give appropriate explanations.
- C003: Loading feedback reflects whether progress is known.
- C004: A successful action makes the resulting state clear.
- C005: Unavailable actions explain eligibility when users need that information.
- C006: Stale or cached data is identified where freshness affects decisions.
- C007: Partial results are distinguished from complete results.
- C008: Error recovery preserves useful work where feasible.
- C009: Cancellation explains what stopped and what already happened.
- C010: State changes remain understandable after refresh or return.

#### Navigation and focus

- C011: Back navigation has a defined destination and preserves expected context.
- C012: Deep links work for signed-out, unauthorized, and missing-object states.
- C013: Closing an overlay restores focus to a useful location.
- C014: Opening a modal places focus appropriately and manages its boundary.
- C015: Keyboard order follows a meaningful task and reading sequence.
- C016: Focus remains visible and is not obscured by sticky UI.
- C017: Nested scrolling and sticky regions do not trap users.
- C018: Changing tabs or views preserves or resets state according to explicit rules.
- C019: Navigation identifies the active workspace and current location.
- C020: Unsaved-change handling matches the actual risk of losing work.

#### Fields and validation

- C021: Labels remain available when fields contain values.
- C022: Required, optional, read-only, and unavailable fields are distinguishable.
- C023: Defaults are appropriate and do not silently make consequential choices.
- C024: Validation timing supports correction without needless interruption.
- C025: Error messages identify the problem and a useful next action.
- C026: An error summary links or moves users to relevant fields when appropriate.
- C027: Field dependencies define what happens to previously entered values.
- C028: Input tolerates reasonable pasting, formatting, and international characters.
- C029: Server validation failures preserve entered data when feasible.
- C030: Review screens allow corrections without unnecessary re-entry.

#### Collections, tables, and selection

- C031: Row identity is stable when results are sorted or refreshed.
- C032: Selection scope distinguishes visible rows from all matching records.
- C033: Select-all state is clear after filters, paging, or new data.
- C034: Sorting direction and its effect are perceivable.
- C035: Filter combinations, result counts, applied criteria, and reset are consistent.
- C036: Grouping rules define counts, subtotals, collapsed states, and refresh behavior.
- C037: Long values, missing values, zero, and unknown have distinct treatment.
- C038: Column visibility or reordering preserves essential context.
- C039: Bulk operations show ineligible items and partial outcomes.
- C040: Export scope matches its label and includes the intended records.

#### Transactions and asynchronous work

- C041: Repeated submission cannot silently create duplicate consequential work.
- C042: A timeout distinguishes unknown outcome from confirmed failure.
- C043: Retries are appropriate to the operation and its known state.
- C044: Pending, authorized, completed, failed, and reversed states use correct meaning.
- C045: Amounts specify currency, rounding, precision, and total semantics.
- C046: Background work has an appropriate place to check progress.
- C047: Cancellation states whether processing or financial consequences remain.
- C048: Partial success identifies completed and unresolved items.
- C049: Confirmation provides a usable reference or receipt when needed.
- C050: Reversals, refunds, or undo state their actual limits.

#### Visual layout and content

- C051: Primary action and important consequences have appropriate emphasis.
- C052: Headings, labels, and actions use consistent domain terminology.
- C053: Text wraps or truncates according to an explicit information priority.
- C054: Truncated essential information can be accessed.
- C055: Images and icons have clear meaning at their rendered size.
- C056: Optical alignment and spacing remain consistent with real content.
- C057: Status is communicated with more than color where needed.
- C058: Light, dark, and high-contrast presentations retain meaning.
- C059: Numeric alignment and formatting support comparison.
- C060: UI copy explains the next step without making unsupported promises.

#### Accessibility and sensory alternatives

- C061: Interactive controls have meaningful accessible names.
- C062: Roles, values, selected states, and errors can be conveyed programmatically.
- C063: Dynamic updates are announced appropriately without excessive interruption.
- C064: All relevant actions have workable keyboard and assistive-input paths.
- C065: Complex gestures and dragging have suitable alternatives.
- C066: Target size and spacing meet the applicable requirement.
- C067: Text scaling and zoom preserve critical content and actions.
- C068: Reduced-motion preferences have a defined, usable experience.
- C069: Important audio information has an appropriate non-audio equivalent.
- C070: Captions, transcripts, and accessible media controls are provided as applicable.

#### Languages and regional context

- C071: RTL layout treats directional and non-directional elements correctly.
- C072: Mixed-script identifiers remain readable and correctly ordered.
- C073: Translation expansion does not hide critical actions.
- C074: Pluralization and sentence construction work for the target language.
- C075: Dates distinguish calendar, locale, and time zone where relevant.
- C076: Daylight-saving changes and ambiguous times have defined handling.
- C077: Currency and unit conversions disclose relevant assumptions.
- C078: Names, addresses, and phone formats accept actual regional variation.
- C079: Language changes define content and user-choice persistence.
- C080: Region-specific fields and policies are traceable to an authoritative rule.

#### Privacy, security, and permissions

- C081: Visible actions match actual authorization rather than visual hiding alone.
- C082: Permission changes during a task have a defined recovery path.
- C083: Shared-device sessions avoid exposing prior users' data.
- C084: Expired sessions explain what happens to unsaved work.
- C085: Sensitive content is masked in analytics and recordings as required.
- C086: Consent choices and revocation behavior are understandable.
- C087: Exports and shared links make audience and data scope clear.
- C088: Delegation and ownership transfer show consequences.
- C089: Destructive actions have proportionate review and recovery behavior.
- C090: Account deletion describes timing, retained records, and dependent services accurately.

#### Devices, inputs, and physical context

- C091: On-screen keyboards do not hide the current field or required action.
- C092: Orientation and window resizing preserve useful task state.
- C093: Folding or multi-pane changes do not lose context.
- C094: Touch, pointer, and keyboard input can coexist where supported.
- C095: Hover-only information has a suitable alternative.
- C096: Connectivity loss, reconnect, and queued actions are understandable.
- C097: Low-memory or background interruption has a defined resume path.
- C098: Viewing distance, reach, posture, light, and noise match the use environment.
- C099: Hardware and on-screen status do not contradict each other.
- C100: Time-critical or safety-sensitive behavior receives appropriate specialist validation.

#### Post-launch evidence and regressions

- C101: Event names, properties, and trigger timing match the implemented behavior.
- C102: Funnels distinguish missing instrumentation from actual abandonment.
- C103: Metrics have explicit denominators, windows, and exclusions.
- C104: Baselines and cohorts are comparable enough for the stated claim.
- C105: Qualitative feedback is linked to evidence and sampling limitations.
- C106: Guardrails include user harm and exclusion where relevant.
- C107: Changed components are rechecked for accessibility and localization regressions.
- C108: Experiment conclusions reflect uncertainty and practical significance.
- C109: Live findings have owners, priorities, and a review cadence.
- C110: Learning is reflected in product decisions and reusable patterns.

#### Maintenance, migration, and ending states

- C111: Notifications respect channel, frequency, and preference rules.
- C112: Help and screenshots describe the current product.
- C113: Operating-system and dependency changes trigger relevant reviews.
- C114: Deprecated features identify replacements and affected users.
- C115: Migration previews explain transformations and unresolved records.
- C116: Old and new workflows define coexistence and saved-work behavior.
- C117: Broken links and retired objects offer a useful next step.
- C118: Retirement supports appropriate exports, alternatives, and user communication.
- C119: Research and product records follow the applicable retention policy.
- C120: Skill references record applicability, owner, last verification, and update triggers.

### Foundation-specific additions

- Distinguish padding, margin, parent gap, gutter and container inset.
- Distinguish a spacing ramp, layout grid, text baseline, icon grid and physical pixel grid.
- Check actual content, script, scaling and input before fixing dimensions.
- Record intentional off-grid values and optical corrections.
- Define token alias and theme behavior; inspect code/design differences.
- Document component anatomy, all relevant state intersections and composition.
- Retain source status: a draft, summary, abstract or pointer must not become a claimed standard or completed review.
