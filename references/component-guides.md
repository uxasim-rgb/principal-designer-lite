# Component guides

Per-component decisions: when to use each component, how to size and word it, and the accessibility rules that apply. The state rules in `interaction-states.md` and the waiting and focus defaults in `craft-defaults.md` apply to every component here; this file adds what is specific to each one.

Two rules apply throughout:

- **Target size.** WCAG 2.5.8 (AA) sets a floor of 24 by 24 CSS px, or enough spacing that a 24px circle on each target does not touch another. Platform targets are 44pt (Apple HIG) and 48dp (Material 3). House default: 44px for touch, 32 to 40px for pointer-only desktop tools. None of these is "WCAG 48px".
- **Hover is never the only way in.** Anything revealed on hover is also revealed on keyboard focus and is reachable on touch.

Adapted in part from Uxcel Lab product-skills (MIT); see `THIRD_PARTY_NOTICES.md` in this skill folder.

## Contents

Buttons · Cards · Menus · Modals and dialogs · Navigation (tabs, breadcrumbs, pagination) · Notifications, toasts and badges · Progress trackers · Search and filters · Selection controls · Tables and lists · Tooltips

## Buttons

- **Pick the group type from the choice.** A menu button for several related actions of equal weight. A split button for one default action plus alternatives, with a visible divider so people know the two halves do different things. A toggle group for 2 or 3 mutually exclusive options that should stay visible.
- **Labels are 2 or 3 words on one line.** If a label wraps, rewrite it. No end punctuation, italics or underline. A leading icon goes before the label (mirrored in RTL); a trailing icon is only for a dropdown caret.
- **Size.** Horizontal padding about twice the vertical. Hug content with a minimum width so "OK" still reads as a button and meets the target. On mobile, stacked primary and secondary buttons share one width. Never a fixed width that truncates translated labels. Label text 14 to 16px is a house range; Material 3 uses 14sp.
- **Placement follows the platform.** Material and macOS put the primary action last (right); Windows dialogs put it first. Match the platform rather than a universal rule.
- **Floating action button:** at most one per screen, only for the app's main create action, never destructive, and it must not cover content.
- **Buttons on images** get a scrim so the label and the button edge both keep contrast.
- **Third-party sign-in buttons** use the provider's official assets unchanged.

## Cards

- **Decide browse or lookup first.** Cards suit browsing many different items. Ranked results, comparing specs and finding a known item belong in a list or table.
- **One topic per card, as a teaser:** a title, up to two lines of supporting text, then truncate. Details live on the destination.
- **One emphasized element.** Save and favorite stay quiet; the overflow menu sits top right. Separate parts with space and type weight rather than dividers.
- **A fully clickable card has exactly one action.** Build it as one real link whose hit area is stretched over the card with a pseudo-element, not a link wrapped around everything. Any secondary control sits above the stretched area and stays separately focusable. Show hover and focus. Two or more actions means visible buttons instead.
- **Container:** outlined or tinted for grouping, flat only on a background that clearly differs from the page. Do not stack shadows on media or buttons inside a card.

## Menus

- **Pick the type:** command menu, single select (shows a check mark), multiselect (chosen items show in the trigger and can be removed there without reopening), searchable menu, context menu, overflow menu, cascading menu.
- **Order by use, not alphabet.** Dividers group related items. Past about 7 items or groups, restructure. Past about two scroll lengths, add search or change the flow.
- **Cascading menus:** one child level at most, desktop only, and only where there is room to open.
- **A context menu is a shortcut,** never the only route to an action. In table rows, keep the row's main action outside the overflow menu.
- **Shortcuts:** show standard ones next to common commands. Never invent new ones.
- **Item height:** 48dp for touch, 32 to 40px for pointer, never under the 24px floor.
- **Keyboard:** follow the APG Menu and Menu Button patterns: arrow keys move, Enter or Space activates, Escape closes and returns focus to the trigger.

## Modals and dialogs

- **Gate first.** A modal only for a destructive or irreversible confirmation, a critical warning, or input needed to continue. Success messages, tips and promotions go inline, in a toast or in a banner. Never open a modal the system started in the middle of a high-stakes flow such as checkout.
- **The title carries the message** ("Discard draft?") and the buttons answer it ("Discard", "Keep editing"). At most two actions. Destructive confirmations state the impact ("12 files will be deleted").
- **Never stack a modal on a modal.**
- **Dismissal:** a visible Cancel, a close icon, and Escape or system Back. Clicking outside closes a plain modal only when no entered data would be lost; it never dismisses or confirms an alert dialog.
- **Initial focus** goes into the dialog. For destructive or irreversible actions, focus the least destructive control (Cancel), per the APG Dialog pattern, so Enter cannot destroy data.
- **Type:** fullscreen for complex tasks, a popover for anchored non-critical extras, a lightbox for media, a bottom sheet or action sheet for mobile action lists (never for critical confirmations). Centered on mobile, slightly above center on desktop.
- **Permission requests:** explain the value first, then ask in context at the moment it is needed, one permission at a time, with a way back after a denial.

## Navigation

- **Each layer has one job:** global, local, contextual, utility, footer. Breadcrumbs never replace global navigation.
- **Language selectors** show each language's name in that language, never flags.
- **Hamburger menus** hold secondary items only, when there is room to show the essentials.
- **Dropdown navigation opens on click.** If it also opens on hover, wait about half a second for intent, and meet WCAG 1.4.13 (dismissible with Escape, hoverable, persistent).
- **Tabs:** 2 to 9 peer categories in one row, never stacked; the selected tab visibly connects to its panel; scrollable on mobile when there are many. Steps in a process are not tabs. Tabs are one Tab stop with arrow keys between them (APG Tabs).
- **Bottom navigation:** 3 to 5 destinations.
- **Breadcrumbs:** from depth 3. They mirror the hierarchy, not the click history. Start at Home; the current page is last and is not a link. When long, collapse the middle and keep the first and last. On mobile, one "up one level" link.
- **Pagination:** previous and next, "Page 3 of 10", always showing first, last and current when truncated. Use pagination when people must refind, compare or cite; infinite scroll only for leisure feeds; "Load more" in between.
- **Sticky headers** stay compact and use `scroll-padding-top` so a focused item is never hidden under them (WCAG 2.4.11).

## Notifications, toasts and badges

| Message | Pattern |
| --- | --- |
| Must act now | Persistent alert or banner until resolved |
| Needs attention soon | Warning, persistent |
| Outcome, for information | Toast or snackbar |
| Something new | Badge |

- **Toast timing:** at least 5 seconds, longer for longer text, paused while hovered or focused. Anything the person must act on, including Undo, stays until dismissed: a timed Undo is a time limit, so WCAG 2.2.1 applies. Announce toasts through a polite live region (WCAG 4.1.3). A toast never covers the focused element or the primary controls (WCAG 2.4.11).
- **Badges** mean unread items, never marketing or scores. A dot for "something new"; a count only when the number helps, capped (99+). Status indicators (online, in progress) are information, not notifications.
- **One event, one notification.** Group the rest. When the app is open, update a badge or the view instead of sending a system notification.
- **Push:** transactional first; promotional only with a specific opt-in; send in the person's time zone; watch the opt-out rate. Settings let people mute everything or by type, and choose frequency.

## Progress trackers

A progress tracker shows a journey the person moves through; a loader shows the system working. They are different components.

- Show completed, current and remaining steps, each with a title.
- Use one from 3 steps; past about 7, restructure the flow.
- Numbered, titled steps for forms; a bar for processing; dots only for skippable walkthroughs; vertical for status timelines (delivery, application stages).
- Show a percentage only if it tracks real progress. Jumping percentages destroy trust.
- Multi-step forms do not ask again for what was already entered (WCAG 3.3.7).

## Search and filters

- **Ask how people search.** For known items, invest in the input, suggestions and finding things again. For exploration, invest in filters, related searches and browsing. Recent searches on focus help both.
- **Input:** a visible field on every page where search matters, not just an icon on desktop, wide enough for about 27 characters. The magnifier inside the field submits.
- **Suggestions:** at most about 10, no scrolling, typed and suggested parts styled differently, and the count announced (APG Combobox).
- **Results:** the query stays visible and editable; show the match count; highlight matched terms; a skeleton while loading. A timeout is never "No results".
- **No results** always offers a way forward: a corrected query, a broader scope, categories or related items.
- **Filters:** 5 to 7 visible, most used first, the rest behind "More filters". Checkboxes for criteria that combine. Show applied filters twice: checked in the panel and as removable chips above the results. A sidebar for many groups on desktop, a bar for a few, a Filter button on mobile. Update results live when it is fast; on slow queries use an Apply button that shows the match count.
- **Sort is a separate control from filter.** Offer a list view for comparing specs and a grid for visual goods.

## Selection controls

| The choice | Control |
| --- | --- |
| Exactly one of a few | Radio buttons |
| Zero or more | Checkboxes |
| On or off, taking effect at once | Switch |
| On or off, applied on submit | Checkbox |
| Up to about 5 options | Show them all |
| A long list | Searchable select |
| A feel or a range | Slider |
| An exact value | Text input |

- **Keep the base shapes:** square checkbox, round radio, pill switch. Every option in a group is the same size so none looks favored.
- **Parent checkboxes** have a mixed state; children are indented under them.
- **The whole label is the hit area.** Controls sit before labels in left-to-right layouts and align with the first line of a multi-line label. On mobile, switches sit on the right with the label on the left.
- **Switch labels name the thing** ("Email notifications"), never a question. Say it aloud with "on" and "off" to test.
- **Preselect a radio only** when one option is the safe, common and reversible answer. Never preselect answers with legal, eligibility, consent or payment meaning; people skip a question that looks answered.
- **Sliders:** min and max labels, the value never hidden under the thumb, ticks and snapping for steps, two thumbs for ranges, preset ranges on mobile. Every slider needs a single-pointer alternative: tapping the track, step buttons or a linked number field (WCAG 2.5.7). Mirror direction in RTL.

## Tables and lists

- **Table or list:** a table when people compare several attributes across rows, a list when they scan one item per row. Simple tables often read better as lists, also for screen readers.
- **One format per column:** the same date, currency and unit in every row. No empty header cells. One header level; split a table rather than merging cells.

| Density | Row height | For |
| --- | --- | --- |
| Dense | 32px | Expert tools with a density setting |
| Condensed | 40px | Operations and admin |
| Regular | 48px | Default |
| Relaxed | 56px | Consumer lists |

- **Overflow:** truncate with an ellipsis and give access to the full value through a focusable trigger. Past 6 to 8 columns, let people resize, hide or reorder them.
- **Rows** have hover and selected states. Bulk checkboxes are always visible; the bulk action bar appears on selection. Row actions revealed on hover also appear on focus within the row and are always visible on touch (`@media (hover: none)`), or sit in a visible overflow button.
- **Toolbar** (search, filter, export) above the table only when the volume justifies it. Every meaningful column is sortable.
- **Lists:** thumbnails on the left, controls on the right, aligned to the same edges. Dividers when items run 3 lines or more, inset when there are thumbnails.

## Tooltips

- **Gate each one.** Is the element really unclear? (Not "Submit" on a Submit button.) Is the information needed to finish the task? Then it belongs in the interface. Does the screen need many tooltips? Fix the labels or icons.

| The need | Use instead of a tooltip |
| --- | --- |
| Instructions for a field | Helper text |
| A visual question (where is the CVV) | An inline graphic |
| First-run teaching | Onboarding |
| A touch-first product | A visible label or a tap popover |
| Rich content or actions | A popover |

- Truncated text with a tooltip showing the full value is a valid pairing.
- **WCAG 1.4.13:** the tooltip opens on keyboard focus as well as hover, can be dismissed with Escape without moving the pointer or focus, stays open while the pointer moves onto it, and stays until dismissed or no longer relevant.
- **APG Tooltip:** no interactive content inside (use a popover); the trigger points to it with `aria-describedby`.
- One style across the product, left-aligned text, 4.5:1 contrast, placement that keeps the trigger visible and handles screen edges. Use the pointer cursor only if the trigger is also a control.
