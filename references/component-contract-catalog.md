# Component and pattern contract

This is a practical catalog of 106 common entries, not a universal inventory of every platform widget. Reuse the contract to extend it for native, embedded, specialist or product-specific components.

### Required specification dimensions

| Dimension | What to specify |
| --- | --- |
| Identity | Name, aliases, owner, status and version |
| User purpose | Task, decision and user need |
| Selection | When to use, when another pattern fits, and relevant alternatives |
| Context | Surface, platform version, domain, locale and physical environment |
| Anatomy | Parts, slots, labels, optional regions, hit area and boundaries |
| Variants | Role, size, density, theme, platform, orientation and configuration |
| Content | Labels, hints, errors, examples, empty content and terminology |
| Data | Type, identity, source, freshness, precision, missing values and permissions |
| State | Default, focus, selection, expanded, busy, invalid and other meaningful states |
| Events | User actions, system events and external updates |
| Preconditions | Eligibility, permission, data and service availability |
| Transitions | Guards, next state, side effects and feedback |
| Persistence | Session, view, object, account or device scope |
| Pointer and touch | Target, gestures, hover alternatives and touch/pointer coexistence |
| Keyboard | Sequence, keys, shortcuts, focus movement, entry and exit |
| Assistive interaction | Meaningful names, roles, values, relationships, reading order and announcements |
| Focus | Initial placement, visible focus, boundaries and restoration |
| Sizing | Content-driven size, minimum/maximum, fixed/fluid, text scaling |
| Space | Padding, gaps, margins, insets, alignment, grid and exceptions |
| Typography | Role, wrapping, truncation, fallback, script and numerals |
| Color and shape | Semantic roles, contrast pairs, borders, corners, surfaces and status cues |
| Motion/sound/haptics | Purpose, timing, interruption, preferences and equivalent information |
| Adaptation | Reflow, available window, orientation, posture, content and input changes |
| Composition | Behavior within forms, tables, panels, overlays and nested structures |
| Async behavior | Pending, progress, stale, timeout, cancellation and unknown outcome |
| Recovery | Error, partial success, retry, correction, undo, support and resume |
| Localization | Direction, mixed scripts, expansion, formats and regional variation |
| API/design mapping | Properties, slots, events, tokens, code, design-tool controls and dependencies |
| Evidence | Tested tasks, data, users, environments, assistive tools and limitations |
| Maintenance | Support matrix, known gaps, release, migration and deprecation |

Apply the dimensions that affect the task. Mark material exclusions and unknowns. A small static element may need only a subset; a transactional or interactive widget usually needs much more.

### State intersections

Do not assume every state combines with every other state. Specify valid intersections, such as selected plus focused, loading plus cancellable, read-only plus focused, invalid plus disabled, expanded plus empty, and pending plus lost connection. Define the precedence and what is actually perceivable.

Separate visual state, interaction state, domain object state, network state, and authorization state. A disabled-looking button does not enforce backend authorization.

### Example: Primary action button

Illustrative project values only.

| Area | Example decision |
| --- | --- |
| Purpose | Submit a reviewed request |
| Label | Describe the actual action; use a dynamic count only when useful and reliable |
| Role | One primary action within the relevant decision scope |
| Space | Inline padding from a semantic token; icon/text gap from a separate token |
| Height | Content-driven with a context-appropriate minimum; allow translated and enlarged text |
| Typography | Use a documented role and test actual script metrics |
| Border | Include border thickness in geometry; record any compensation rather than forcing every measurement onto the layout grid |
| Focus | Visible, unobscured and compatible with system settings |
| Pending | Convey progress and define whether repeated activation is blocked, merged or safe |
| Error | Explain the failed operation at an appropriate scope and preserve useful work |
| Unknown outcome | Offer a way to check status before repeating a consequential action |
| Disabled | Explain unavailable eligibility where useful and discoverable |
| Icon-only form | Provide a meaningful accessible name and adequate action area |
| Keyboard | Use appropriate native activation behavior |
| Input | Support relevant pointer, touch and assistive routes |
| Completion | Show the actual resulting state or receipt |
| Validation | Check operation semantics, input, scaling, content, states and actual implementation |

A button specification does not need an invented universal padding or radius. The project system, task, platform, content and accessibility requirements determine values.

### Catalog

#### Actions and commands

| Entry | Purpose | Specific behavior to define |
| --- | --- | --- |
| Button | Trigger an action | Role hierarchy, label, pending, duplicate activation, disabled eligibility, focus. |
| Icon button | Compact labeled action | Accessible name, tooltip limits, target area, state, icon meaning. |
| Link | Navigate to a destination | Destination clarity, visited behavior, external/download cues, focus. |
| Toggle button | Switch an action state | Pressed state, label consistency, persistence, grouped behavior. |
| Split button | Default plus related actions | Primary action, menu boundary, input, focus and dismissal. |
| Menu and menu item | Expose context-relevant commands | Grouping, checked states, keyboard model, destructive action, disabled reason. |
| Context menu | Commands for a specific object | Invocation alternatives, object context, placement, focus return. |
| Command palette | Discover and execute commands | Search, keyboard, scope, results, eligibility and recent actions. |
| Action toolbar | Group related commands | Priority, overflow, selection context, resizing and keyboard access. |
| Floating action button | Prominent contextual action | Platform appropriateness, overlap, labels, placement and scroll behavior. |
| Segmented control | Choose among related views or values | Single/multiple selection meaning, semantics, overflow, keyboard behavior. |
| Shortcut/key hint | Expose an efficient command | Platform modifiers, conflicts, remapping, discoverability and accessible alternative. |

#### Navigation and orientation

| Entry | Purpose | Specific behavior to define |
| --- | --- | --- |
| App header/top bar | Global context and actions | Title, navigation, safe areas, sticky behavior, overflow. |
| Sidebar/navigation rail | Persistent section navigation | Current item, collapse, hierarchy, resize, keyboard and touch. |
| Bottom navigation/tab bar | Switch primary destinations | Persistence, selection, labels, back stack and platform convention. |
| Tabs | Switch related panels | Activation model, focus, panel association, loading and overflow. |
| Breadcrumb | Show hierarchical context | Current page, parent links, wrapping and meaningful labels. |
| Mega menu | Expose large navigation groups | Hierarchy, hover alternatives, dismissal, focus and constrained screens. |
| Tree navigation | Navigate hierarchical objects | Expansion, selection, loading, keyboard and permissions. |
| Skip link | Bypass repeated content | Visibility on focus, destination, placement and useful target. |
| In-page contents | Navigate within long content | Heading mapping, sticky overlap, current section and deep links. |
| Pagination | Navigate record or content pages | Total/unknown count, current page, limits, loading and retained state. |
| Stepper/progress indicator | Explain staged work | Step meaning, current/completed/error states, non-linear navigation. |
| Wizard navigation | Move through branched steps | Back, validation, skip eligibility, resume and review. |
| Back control | Return through context | Destination, browser/system behavior, state and unsaved work. |
| Workspace/tenant switcher | Change active organization context | Identity, permissions, remembered context and accidental cross-tenant action. |
| Footer | Supplementary page/service navigation | Priority, legal/help context, responsive order and repeated content. |

#### Input and selection

| Entry | Purpose | Specific behavior to define |
| --- | --- | --- |
| Text field | Enter a short string | Persistent label, format, hint, input mode, validation and autocomplete. |
| Textarea | Enter longer text | Resize/grow, limits, paragraphs, paste and saved draft. |
| Password/passkey entry | Authenticate using supported methods | Visibility, paste, platform support, errors and recovery. |
| Search field | Enter a query | Submit timing, clear, suggestions, history and keyboard. |
| Number input | Enter a numeric quantity | Precision, range, step, wheel behavior, locale and invalid text. |
| Money input | Enter a financial amount | Currency, precision, rounding, sign, bounds and calculation meaning. |
| Phone/email input | Enter contact information | Regional variation, permissive formatting, verification and hints. |
| OTP/code entry | Enter verification codes | Paste/autofill, expiry, resend, error, keyboard and accessible grouping. |
| Masked/formatted input | Enter structured values | Editable raw value, paste, partial entry, caret and actual accepted formats. |
| Checkbox | Select independent choices | Checked/mixed, label target, group meaning and validation. |
| Radio group | Select one option | Group label, default, keyboard, disabled options and requiredness. |
| Switch | Toggle an immediate setting | On/off meaning, save timing, pending, failure and visible state. |
| Select | Choose an allowed value | Placeholder versus value, options, grouping, long labels and native behavior. |
| Listbox | Select from a list | Selection/focus model, multi-select, typeahead and virtualization. |
| Combobox/autocomplete | Find or choose a value | Editable/select-only, popup type, acceptance, free text and announcements. |
| Multiselect/token input | Choose several values | Removal, duplicates, overflow, keyboard, search and summary. |
| Date picker | Choose a date | Manual entry, calendar, locale, bounds, disabled dates and timezone meaning. |
| Time picker | Choose a time | Locale, timezone, daylight saving, granularity and manual input. |
| Date/time range | Choose an interval | Inclusive bounds, order, timezones, overlap, validity and presets. |
| Slider/range control | Adjust a value continuously | Precision, alternatives, keyboard, labels, bounds and live effects. |
| Rating control | Express an ordered rating | Scale meaning, empty/selected state, accessible labels and clearing. |
| File/camera/scanner input | Capture evidence or content | Permission, type/size, preview, progress, cancel, processing and retry. |
| Address/name input | Enter human identity/location data | Regional formats, multiple scripts, optional parts and correction. |
| Rich-text editor | Create formatted content | Structure, commands, paste, keyboard, collaboration, accessibility and export. |

#### Structure and information

| Entry | Purpose | Specific behavior to define |
| --- | --- | --- |
| Card/tile | Group a meaningful item | Hierarchy, actions, selection, nested controls, density and overflow. |
| List/list item | Present a sequence of objects | Identity, separators, scanning, selection, actions and responsive order. |
| Accordion/disclosure | Reveal related detail | Heading, expanded state, focus, persistence and hidden required content. |
| Description/metadata list | Present label-value relationships | Semantics, missing values, long text, order and responsiveness. |
| Fieldset/form group | Explain related inputs | Group label, instructions, validation and nested grouping. |
| Divider | Separate meaningful regions | Semantic necessity, contrast, spacing and excessive visual boundaries. |
| Container/stack/grid | Compose layout relationships | Inset/gap ownership, constraints, reflow, alignment and reading order. |
| Split pane/resizer | Coordinate related regions | Minimum sizes, keyboard resizing, persistence, collapse and focus. |
| App/page shell | Provide shared structure | Navigation, content region, landmarks, overlays, scroll and platform context. |
| Badge/status/tag | Convey status or categorization | Meaning, non-color cues, count limits, readability and interactivity. |
| Chip/filter token | Represent a selected criterion or item | Label, remove/select distinction, focus, counts and truncation. |
| Avatar/identity summary | Represent a person or organization | Fallback, privacy, meaning, name, image failure and group context. |
| KPI/summary total | Summarize a decision-relevant value | Definition, unit, period, freshness, comparison, uncertainty and drill-down. |
| Timeline/activity/audit log | Explain a sequence of changes | Actor, timestamp, timezone, event meaning, permissions and revisions. |

#### Feedback and system state

| Entry | Purpose | Specific behavior to define |
| --- | --- | --- |
| Inline field error | Explain a correctable input problem | Field association, cause, next step, timing and focus. |
| Error summary | Orient users to form problems | Useful order, linked fields, focus and retained data. |
| Alert/banner | Communicate important contextual status | Severity, placement, persistence, actions, dismissal and announcement. |
| Toast/snackbar | Acknowledge brief outcomes | Duration, accessible announcement, action availability and missed-message recovery. |
| Linear/circular progress | Represent known progress | Actual denominator, updates, cancellation and stalled state. |
| Spinner/busy indicator | Represent indeterminate work | Delay, scope, interaction availability and timeout. |
| Skeleton/placeholder | Reserve content while loading | Layout stability, truthful structure, motion preference and semantics. |
| Empty state | Explain absence and useful next action | First-use, filtered-empty, denied, unavailable and genuine no-data distinctions. |
| Error/not-found page | Recover from a failed destination | Cause where known, return path, retry, support and preserved context. |
| Offline/connection status | Explain unavailable or delayed synchronization | Local state, queued work, freshness, reconnect and conflicts. |
| Completion/receipt | Confirm a meaningful outcome | What happened, reference, next step, remaining work and downloadable evidence. |

#### Overlays and guidance

| Entry | Purpose | Specific behavior to define |
| --- | --- | --- |
| Modal dialog | Require a focused subtask or decision | Initial focus, inert background, escape policy, return focus and consequence. |
| Alert dialog | Acquire response to an urgent message | Brevity, appropriate initial focus, actions and interruption cost. |
| Drawer/side panel | Show contextual content or work | Modal status, width, scrolling, close, changes and main-context relationship. |
| Bottom sheet | Present contextual mobile content/actions | Detents, drag alternatives, dismissal, keyboard and scrolling. |
| Popover | Show anchored supplementary content | Anchor, placement, dismissal, focus and constrained viewport. |
| Tooltip | Offer brief supplementary explanation | Hover/focus access, timing, essential-content limits and touch alternative. |
| Coachmark/tour | Introduce meaningful capabilities | Relevance, sequence, dismissal, recurrence, accessibility and learning retention. |
| Lightbox/media overlay | Inspect media in context | Navigation, zoom, escape, focus, captions and original context. |

#### Data and work management

| Entry | Purpose | Specific behavior to define |
| --- | --- | --- |
| Data table | Compare structured records | Column rules, sorting, row identity, selection, pagination and semantics. |
| Interactive data grid | Operate tabular data | Cell navigation/editing, focus, validation, virtualization and read-only distinctions. |
| Tree grid | Operate hierarchical tabular data | Expansion, level, row/cell navigation, loading and selection. |
| Filter bar/panel | Refine result scope | Apply timing, combinations, counts, reset, persistence and selection consequences. |
| Sort/group controls | Organize a collection | Defaults, direction, group counts, totals, refresh and reset. |
| Saved view/search | Reuse a configured perspective | Naming, ownership, sharing, changed criteria and permissions. |
| Record detail | Understand and act on an object | Hierarchy, state, actions, related objects, audit and permissions. |
| Approval queue | Review pending decisions | Eligibility, assignment, urgency, delegation, reasons and partial batch outcomes. |
| Kanban/work board | Manage work by state | Allowed transitions, drag alternative, limits, order and concurrent changes. |
| Calendar/schedule | Coordinate events or resources | Timezones, ranges, conflicts, density, reschedule and alternative view. |
| Job/import/export status | Track background processing | Scope, progress, cancel limits, results, partial failure and download lifetime. |
| Dashboard/chart/map | Support interpretation and decisions | Data definition, scale, provenance, freshness, uncertainty, accessible alternative and drill-down. |

#### Media and collaboration

| Entry | Purpose | Specific behavior to define |
| --- | --- | --- |
| Image/gallery/carousel | Inspect visual content | Alternative text, order, crop, controls, motion and constrained layout. |
| Audio player | Control listening | Play/pause, seek, queue, speed, background, interruption and transcript. |
| Video player | Control audiovisual content | Captions, description, controls, keyboard, fullscreen and playback state. |
| Document/PDF viewer | Read and navigate documents | Structure, pages, search, zoom, accessibility, download and permissions. |
| Transcript/caption panel | Access synchronized or textual media | Speaker, timestamps, search, focus, synchronization and correction. |
| Comments/discussion | Discuss an object or task | Threading, permissions, edit/delete, mentions, moderation and notifications. |
| Message/composer | Create and exchange messages | Draft, recipient context, attachments, send state, retry, edit and accessibility. |
| Notification center | Review relevant updates | Grouping, read state, priority, preferences, deep links and stale targets. |
| Share/permission dialog | Grant access or create a link | Audience, role, scope, expiry, revocation and preview of consequences. |
| Version/history comparison | Inspect and restore change | Source versions, differences, actors, timestamps, conflict and restoration meaning. |

### Authoritative pattern lookup

Use the actual platform/component guidance. Relevant starting points include the APG pattern index (S17), modal dialogs (S19), comboboxes (S20), interactive grids (S21), native platform guidance (S30 to S33), and the project system. The catalog is original coverage guidance, not a claim that each component has been independently tested.
