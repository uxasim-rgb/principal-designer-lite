# Screen and flow recipes

What specific screens and flows must contain, in what order, and the decisions to make before drawing them. The state and unhappy-path rules in `interaction-states.md` apply to every recipe; this file adds what is particular to each one. Pricing pages live in `marketing-pages.md`, cancellation tactics in `deceptive-design.md`, dashboards in `data-visualization.md`.

Percentages that some sources quote for these patterns (social login preference, signup lift, abandonment) are not repeated here without a source. Do not add them to a deliverable unless you can cite one.

Adapted in part from Uxcel Lab product-skills (MIT); see `THIRD_PARTY_NOTICES.md` in this skill folder.

## Contents

Sign up and log in · Password reset · Settings · Onboarding · Checkout and payment · Booking search · Account deletion and cancellation · Activity feeds · Help and contact support · 404 pages · Slips and mistakes

## Sign up and log in

- **Two separate views,** each titled with what it is. The switch link ("New here? Create an account") sits above the fields, not under the button.
- **Labels that look different:** "Log in" and "Create account". "Sign in" next to "Sign up" is too easy to confuse.
- **Sign up asks for an identifier and a password only.** Collect everything else later, at the moment it is needed.
- **Passwords:** a show and hide toggle, no "confirm password" field. Follow NIST SP 800-63B: no composition rules (uppercase, symbol) and no forced periodic changes; check against a list of common and breached passwords; allow at least 64 characters. Show the length requirement and the blocklist result live, not a checklist of character rules.
- **Let the browser and password managers work:** `autocomplete="username"`, `current-password`, `new-password` and `one-time-code`. Allow paste. Offer passkeys as a first-class option.
- **WCAG 3.3.8 (AA):** no cognitive test (remembering, transcribing, solving a puzzle) as the only way in. A text CAPTCHA needs an alternative.
- **Errors at log in** say the details did not match, not which one was wrong. At sign up, in high-stakes products, send an email ("If this address is new, we sent a link") rather than revealing on screen that an account exists.

| Decision | Apply when | Avoid when |
| --- | --- | --- |
| Social sign-in | Consumer apps | Enterprise single sign-on or privacy-sensitive audiences. Always keep an email option |
| Username as identifier | Public handles matter | Everywhere else; use email or phone |
| "Remember me" | Low-stakes apps | Banking, health, enterprise: remember the identifier only and time out on inactivity |
| Second factor | Sensitive data or money | Make it optional elsewhere |

## Password reset

1. A "Forgot password?" link directly under the password field.
2. A request screen asking for one identifier.
3. A confirmation that does not reveal whether the account exists: "If an account exists for this address, we sent a link."
4. An email or SMS that leads with the link or code.
5. A new-password screen with the rules visible.
6. Success, then back to log in or to where the person was going.

## Settings

- **Preferences only,** never stray links. Group by type under headings with white space; within a group, order by how often people change things. Expert options go behind "Advanced", one level deep at most.
- **Show each setting's current value** next to it. Name a switch after what it controls ("Email notifications"), not its state.
- **Destructive items** (sign out, delete account) go last and are set apart, never hidden. Urgent account alerts (trial ending, storage full) go at the top.
- **When changes apply depends on the control,** not the operating system. A switch applies immediately. Checkboxes, multi-field edits and sensitive changes wait for an explicit Save.
- **Save states:** no changes ("All changes saved"), unsaved changes, saving, saved, with Undo where reversible. Disable Save only for "no changes" and say so.
- **Leaving with unsaved changes** never saves silently. A short dialog: "Discard" and "Keep editing".
- **Changing email, password or payment method** asks for re-authentication. Everyday switches need no confirmation.
- **Search** only past a few dozen options, after first cutting options.
- **Mobile:** manage in the app what you can. For system permissions, explain why and deep-link to the system settings.

## Onboarding

- **Gate first.** A guided tour is justified only when the product is complex, needs data before it works, has unfamiliar workflows, or a tutorial is expected (games). Otherwise use empty-state prompts and one tip at a time.

| Method | Use for |
| --- | --- |
| Interactive tour | Learning by doing |
| Checklist with progress | Multi-step setup |
| Contextual tips | Features people discover over time |
| Static walkthrough | Last resort: 4 or 5 screens, about a minute in total |

- **Always skippable,** with step count and position shown. Never show completed onboarding again; store the state.
- **Show value before asking for anything,** and give an early real win. Let people try the product before registering unless it needs an account to work.
- **Ask profile questions** only if the answer changes the experience, and say why you are asking.
- **Permissions:** ask at the moment the permission is needed, with an explanation in the app before the system prompt. Never ask for everything at launch. iOS shows its system prompt only once, so after a denial the only route is a deep link to Settings. Android 13 and later need a runtime prompt for notifications.
- **End with the first real action** ("Create your first project").

## Checkout and payment

- **Stages:** cart, identity, delivery details, payment, processing, confirmation.
- **Guest checkout is the primary button.** Offer account creation on the confirmation screen, prefilled.
- **The checkout page holds** the logo, a way back to the cart and a support link. No navigation, footer link lists, ads or pop-ups.
- **The cart** shows a thumbnail matching the chosen variant, a quantity stepper, variant editing in place, and delivery, tax and total. The checkout button sits after the summary. Fees appear from the first price shown (`deceptive-design.md` owns drip pricing).
- **Promo codes:** a collapsed "Have a promo code?" link that opens the field. Apply automatically when the offer applies to everyone; codes from an email or ad apply on click. The discount shows next to the total, with applied, error and remove states. An expired code points to current offers.
- **Card entry:** group the number automatically, detect the card type from the first digits (no brand picker), numeric keyboard, autofill. Prefer the payment provider's hosted fields; the card security code is never stored after authorization (PCI DSS).
- **Region:** currency from the country. For international delivery, ask the country first and then show that country's address fields. One "Full name" field unless a law or an integration needs it split. Offer the payment methods that matter in the buyer's region, most used first.
- **Length:** one page when short; numbered steps or a one-page accordion when long.
- **Processing** blocks a second submission. A timeout is "checking", never "failed", and a retry never charges twice.
- **Confirmation screen and email** both carry the order summary, the cost breakdown, what happens next and when, tracking, a support contact and the account offer.
- **Trust:** one plain security cue next to the card fields. Do not stack seals.
- **Mobile is its own design:** steppers, numeric keyboards, 48dp targets with about 8dp between them.

## Booking search

One prominent search bar; an obvious "today"; clear hover and selection across a date range; paired from and to fields next to each other with a swap control; the query kept visible and editable on the results page. Offer save-for-later only where people compare many options.

## Account deletion and cancellation

- **Decide which exit it is.** Cancelling a subscription is usually reversible: light friction, and access runs to the end of the paid period. Deleting an account is often permanent: a deliberate step such as re-entering the password or typing the word.
- **Before the final step, state the facts:** when deletion happens, whether there is a restore window and how long, what happens to public content, how long access lasts.
- **Offer an export** before deletion.
- **Pause, deactivate or downgrade** sit next to an easy delete, never instead of it, and each says what happens to data, billing and visibility.
- **At most one retention offer,** declined in one tap. An optional exit survey with preset reasons and "Other" that never blocks the exit. "Stay" and "Cancel" have equal visual weight.
- **End with** thanks, the end date and at most one reactivation email.
- **Store rules:** the App Store requires in-app account deletion for apps that let people create an account (guideline 5.1.1(v)); Google Play requires in-app deletion and a web link to request it. Laws on cancelling subscriptions change; `deceptive-design.md` owns the current position.

## Activity feeds

- **Decide chronological or ranked before launch.** Chronological when when-it-happened is the point (logs, team history, transactions); ranked when volume makes recency noisy. Switching later upsets people.
- **Each entry shows only what is needed to decide and move on.** Controls match the purpose: a social feed gets reactions and replies; a read-only updates feed gets one link or none.
- **Group similar events** once volume would flood ("12 people followed you today"); keep them separate in quiet feeds.
- **Timestamps by feed type:** relative and short in social feeds ("3h"); absolute with a time zone in logs and transactions. Always expose the exact time on hover and focus through `<time datetime>`.
- **Empty feeds:** seed social and discovery feeds; an audit log or transaction list shows an honest empty state.
- **Loading** is visible on pull to refresh and on load more. Sponsored entries are labeled every time.

## Help and contact support

- **Self-service first,** ordered by the top contact reasons from tickets and search logs. A growing FAQ is a list of product bugs, not a success.
- **Before someone picks a channel,** say what it is, the expected response time, what to have ready, and whether it is recorded.
- **Offer only channels the team can staff.** Outside hours, say the channel is offline and offer email or articles.
- **A bot that answers first says so** in its first message and always offers a route to a person (`ai-agents.md`).
- **Help at the point of error:** link the right article, or a person for complex cases.
- **After resolution,** one short "Did this fix it?". Chat users get a transcript. Rating first, comment optional, never a mid-task pop-up, never required.
- **Placement:** a footer link on simple sites, the header on complex ones. In account menus, help near the bottom, feedback above it, sign out last. Every video guide has a text version.
- **WCAG 3.2.6 (A):** help mechanisms appear in the same relative place on every page that has them.

## 404 pages

A plain explanation without blame; at least two ways onward (home, plus search or popular pages); the closest matching address when there is one. Short copy and a search box are enough.

## Slips and mistakes

Decide which kind of error before choosing the fix. A slip is an autopilot error by someone who knows the product: fix it with constraints, safe defaults and undo, and keep a confirm button away from the control that opened it so a double tap cannot confirm. A mistake comes from a wrong mental model: fix it with clearer labels and guidance, and use research to find the gap.
