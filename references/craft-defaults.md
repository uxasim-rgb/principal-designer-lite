# Craft defaults

Use these values when the project has no system of its own. They are starting points chosen to be safe and good-looking, not laws. When a project system, platform guideline or real content says otherwise, the project wins. When you deviate, say why in one line.

The point of this file: the rest of the library is careful about what is *not* universal. This file is what you actually do on Monday morning.

## Contents
1. Order of precedence
2. Typography
3. Spacing and layout
4. Color
5. Shape, borders, depth
6. Components and states
7. Interaction timing and motion
8. Copy
9. Accessibility floor
10. When to break a default

## 1. Order of precedence

1. Legal or regulatory requirement for this product and region.
2. The project's own design system, tokens and components.
3. The target platform's guidelines (Apple HIG, Material, Fluent) for native apps.
4. Real content and real user evidence.
5. These defaults.

## 2. Typography

| Decision | Default | Notes |
| --- | --- | --- |
| Body size, web | 16px | 15px is fine for dense desktop tools; 17pt is iOS body. Never below 14px for reading text. |
| Body line height | 1.5 | 1.4 for dense UI, 1.6 to 1.7 for long reading. Urdu Nastaliq needs more, see `urdu-arabic-typography.md`. |
| Heading line height | 1.1 to 1.25 | Tighter as size grows. |
| Line length | 60 to 75 characters | Hard cap around 80. Set with `max-width: 65ch` on text blocks. |
| Type scale | 12, 14, 16, 18, 20, 24, 30, 36, 48, 60 | A ratio around 1.2 to 1.25. Use 4 to 6 sizes in one product, not all of them. |
| Weights | 400 body, 500 or 600 for UI labels and headings | Two or three weights per family. Avoid 300 for body text on screens. |
| Families | One family is enough. Two at most (display + text). | A good neutral sans for product UI: Inter, Geist, IBM Plex Sans, Source Sans 3, system-ui. Pick a distinctive display face only for marketing or brand moments. |
| Numbers | Tabular figures in tables, prices, timers | `font-variant-numeric: tabular-nums`. Right-align numeric columns. |
| Letter spacing | 0 for body; slight negative (-0.01 to -0.02em) for large headings; positive (+0.04 to +0.08em) only for small uppercase labels | |
| Hierarchy | Prefer size and weight; use color (secondary gray) as the third lever | Do not create hierarchy with five font sizes when two plus weight works. |

## 3. Spacing and layout

**Spacing scale (4px base):** 4, 8, 12, 16, 24, 32, 48, 64, 96. Use 8 as the common step; 4 and 12 for tight component internals. This matches common systems and keeps values few enough to be consistent.

| Relationship | Default |
| --- | --- |
| Icon to label | 8 |
| Label to field | 6 to 8 |
| Between fields in a form | 16 to 24 |
| Inside a card or panel | 16 (compact), 24 (comfortable) |
| Between related groups | 24 to 32 |
| Between page sections (product UI) | 32 to 48 |
| Between page sections (marketing) | 80 to 128 |
| Page side margin | 16 mobile, 24 tablet, 32 or more desktop |

Rule of thumb: space inside a group must be clearly smaller than space between groups (proximity does the grouping, so borders and boxes are often unnecessary).

**Layout:**
- Content max width: 1200 to 1280px for apps and marketing; reading pages around 680 to 720px.
- Grid: 12 columns desktop, 8 tablet, 4 mobile; gutter 16 to 24px.
- Breakpoints (web): 640, 768, 1024, 1280. Design mobile and a wide desktop; check the in-between.
- Align to a few strong vertical edges. Left-align text by default; center only short headings and single calls to action.

## 4. Color

- **Start neutral.** Build the UI in a gray ramp (9 to 11 steps) plus one accent. Add status colors (success, warning, danger, info) only where they mean something.
- **Accent use:** primary buttons, links, focus, selected states. Roughly 5 to 10 percent of the screen. If everything is accented, nothing is.
- **Text on light backgrounds:** primary text near-black (not pure #000, e.g. #111 to #1a1a1a), secondary text a mid gray that still meets 4.5:1.
- **Backgrounds:** white or a very light neutral; use one subtle tint step to separate surfaces instead of shadows everywhere.
- **Dark mode:** do not invert. Use dark gray surfaces (around #0f0f10 to #1a1a1c), lighten surfaces as they rise, desaturate the accent slightly, and recheck every contrast pair.
- **Contrast minimums:** 4.5:1 body text, 3:1 large text (24px, or 18.66px bold) and for UI component boundaries, focus indicators and meaningful icons.
- **Never encode meaning by color alone.** Pair with icon, text or pattern.
- **Gradients:** off by default. Use only when the brand calls for it and it carries meaning. See `anti-slop.md`.

## 5. Shape, borders, depth

- **Radius:** pick one family and stick to it. Defaults: 6px for inputs and buttons, 8 to 12px for cards and dialogs, full pill only for tags or one deliberate style. Nested radius = outer radius minus padding.
- **Borders:** 1px, low-contrast neutral. Prefer a border or a background tint, not both plus a shadow.
- **Shadows:** few and soft. Reserve them for things that float (menus, popovers, dialogs, dragged items). Flat cards on a tinted background often look cleaner.
- **Elevation levels:** at most three (flat, raised, overlay).

## 6. Components and states

| Item | Default |
| --- | --- |
| Button height | 36px desktop, 40 to 44px touch; padding 12 to 16px horizontal |
| Input height | Same as button so they align in a row |
| Touch target | At least 44×44pt (iOS) / 48×48dp (Android) for primary touch targets; WCAG 2.2 AA floor is 24×24 CSS px with spacing exceptions |
| Primary actions | One per view or decision scope. Secondary is outline or subtle; tertiary is text. |
| Destructive actions | Not styled as primary next to safe actions; confirm or allow undo based on reversibility |
| Labels | Visible labels above fields. Placeholder is an example, never the label. |
| Disabled buttons | Prefer enabled plus clear validation over a mystery disabled button. If disabled, say why nearby. |
| Icons | One family, one stroke weight, 16 or 20px in UI, with text labels for anything not universally understood |
| Tables | Left-align text, right-align numbers, 40 to 48px rows (32 dense), sticky header for long tables, no zebra stripes unless rows are wide |
| Modals | For short, focused decisions only. Prefer inline or a page for anything with more than a few fields. |

**Every data view needs these states designed**, not just the happy path: loading (skeleton for known layouts, spinner for short unknown waits), empty first-use, empty after filtering, error with recovery, partial data, and no-permission. Every action needs pending, success and failure.

Two state rules that are easy to get wrong:
- A timeout or server error is never shown as "No results" or an empty list. Say the search or load failed and offer retry, keeping what the user typed.
- A timeout on a write means the outcome is unknown, not failed. Check status before offering a retry that could duplicate the action.

## 7. Interaction timing and motion

- Response under 100ms feels instant; show progress if work exceeds about 1 second; give determinate progress or a cancel if it exceeds about 10 seconds.
- Motion durations: 100 to 150ms for small state changes (hover, toggle), 200 to 300ms for panels and dialogs, up to 400ms for large page transitions. Ease-out for entering, ease-in for leaving.
- Motion explains change; it is not decoration. Respect `prefers-reduced-motion` with a fade or no animation.
- Do not delay the user with animation they must wait through to continue.

## 8. Copy

- Buttons say the action as a verb plus object: "Save changes", "Send invoice", not "OK" or "Submit".
- Errors: what happened, why if useful, and how to fix it, in plain words. No blame, no codes alone.
- Empty states: what this place is for and the one action to fill it.
- Sentence case for UI text. Title Case only where the platform or brand requires it.
- Specific beats clever. Cut words until meaning would be lost, then stop.

## 9. Accessibility floor

Applies to every output unless the user explicitly scopes it out:
- Contrast as in section 4.
- Visible focus indicator on every interactive element (2px outline with 2px offset in the accent or a high-contrast color).
- Real semantic elements (`button`, `a`, `label`, headings in order, landmarks) in any code you write.
- All functionality available by keyboard; no keyboard traps.
- Alternatives for drag, hover-only and complex gestures.
- Text can grow to 200 percent without loss; layouts reflow at 320 CSS px width.
- Images that convey meaning have alt text; decorative images have empty alt.

## 10. When to break a default

Break a default when you can name the reason: the project system says so, the platform convention differs, real content does not fit, research shows otherwise, or the brand needs a deliberate signature moment. Record the exception so it is not mistaken for drift.
