# Deceptive design (dark patterns)

Patterns that push people into choices they would not make with clear information. They damage trust, raise support costs and are increasingly illegal. Never design them, and flag them when reviewing.

## Common patterns

| Pattern | What it looks like | Fair alternative |
| --- | --- | --- |
| Confirmshaming | "No thanks, I don't like saving money" | Neutral decline: "No thanks" |
| Roach motel / hard cancellation | Easy sign-up, cancellation by phone or buried in menus | Cancel in the same channel and about the same number of steps as sign-up |
| Hidden costs / drip pricing | Fees appear at the last checkout step | Show total cost, including mandatory fees, early |
| Sneak into basket | Add-ons pre-added to the cart | Offer, unselected |
| Pre-checked consent | Marketing or data sharing boxes ticked by default | Unticked; consent as an active choice |
| Forced continuity | Free trial converts to paid with no reminder | Clear terms up front, reminder before charge, easy cancel |
| Fake urgency / scarcity | Countdown timers that reset, "3 people viewing" that is invented | Only real deadlines and real stock levels |
| Disguised ads | Ads styled as content or results | Clear labeling |
| Nagging | Repeated prompts after a "no" | Respect the answer; offer it again only in context |
| Trick questions | Double negatives in opt-out wording | Plain positive wording |
| Visual interference | "Accept all" bright, "Reject" gray and small | Equal visual weight for equal choices |
| Obstruction | Privacy settings spread across screens | Settings grouped and easy to find |
| Privacy zuckering | Defaults that share more than users expect | Most private reasonable default |

## Legal context (verify for the product's jurisdiction)

- **EU:** the Digital Services Act bans deceptive interface design on online platforms; GDPR requires consent to be freely given, specific and as easy to withdraw as to give; consumer protection law covers misleading practices; the AI Act covers some manipulative AI practices.
- **US:** the FTC has acted against dark patterns, especially around subscriptions and cancellation; several states (for example California's privacy law) treat consent obtained through dark patterns as invalid. Rules on subscription cancellation have changed through litigation, so check the current status.
- **Cookie banners:** in the EU and UK, rejecting should be as easy as accepting.

This is orientation, not legal advice. Name the need for legal review in regulated or high-risk flows.

## Review questions

- Would the user make the same choice if every option were shown with equal clarity?
- Is the default the one that benefits the user, or the one that benefits the business at the user's expense?
- Is leaving as easy as joining?
- Is every number, timer and claim true?

## Persuasion that is fine

Clear value, social proof that is real, honest scarcity, sensible defaults that serve the user, reminders the user asked for, and good design of the paid option. The line is deception or coercion, not persuasion.

### Classify each finding before naming it

| Class | What it is | What to do |
| --- | --- | --- |
| Dark | Works only because people misunderstand what they are doing | Report it as deceptive |
| Grey | Open and common, but the default serves the business over the person | Report it with the fairer default |
| Mistake | Confusing, with no sign of intent | Route it to `critique.md`; never call it dark |

Calling a mistake dark costs the review its credibility. For unclear cases, run four tests:

- **Intent gap:** does the product record something different from what the person thinks they did?
- **Front-page test:** would the team be comfortable reading a news headline about this?
- **Second-order effects:** does it win now and cause regret, complaints or churn later?
- **Defaults:** who benefits from each default?

Close the review with a verdict: trustworthy, some concerns, or manipulative.

### Attention and pricing patterns

| Pattern | Fair alternative |
| --- | --- |
| Infinite feed with no stopping point | A natural end ("You are all caught up") or a visible break |
| Next item autoplays with no choice | Autoplay off by default, or a clear cancel before it starts |
| Variable rewards and streaks that punish a missed day | Progress that survives a break; streak freezes |
| Read receipts on by default | Off by default, or symmetric (you see theirs only if they see yours) |
| Onboarding pushes "enable all notifications" | Ask per type, at the moment it is useful |
| Scarcity claims on unlimited digital goods | Only real, verifiable limits |
| Crossed-out "was" price never actually charged | Show a previous price only if it was really charged; EU rules tie it to the lowest price in the prior 30 days, which must be checked for the market |
