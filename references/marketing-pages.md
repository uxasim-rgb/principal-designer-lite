# Landing pages and marketing sites

Marketing pages answer a visitor's questions in the order they arrive, and make the next step easy. They are judged in seconds, so clarity beats cleverness.

## The visitor's questions, in order

1. **What is this?** A headline that says what the product does for whom. Concrete nouns and verbs.
2. **Is it for me?** Audience cues in the subhead, imagery and examples.
3. **Does it work?** Show the product itself: a real screenshot, a short loop, a demo. Proof beats adjectives.
4. **Why this over what I do now?** The specific difference, ideally against the real alternative (spreadsheets, an agency, a competitor category).
5. **Can I trust it?** Real customers, real numbers, security or compliance facts, a human behind it.
6. **What does it cost and what happens next?** Pricing or how to get it, and what the first step involves.

Build only the sections these questions need. A small product might need hero, product shot, three specific benefits, proof and CTA. Do not add sections because templates have them.

## Hero

- Headline: 4 to 10 words, the outcome or the thing. Avoid slogans that could belong to anyone.
- Subhead: one or two sentences adding who it is for and how it works.
- One primary CTA with a specific label ("Start free trial", "Book a demo", "Download for Mac"). Optional secondary ("See how it works").
- A visual of the actual product, not an abstract illustration.
- Above the fold on mobile: headline, subhead and CTA should be visible without scrolling.

## Proof and trust

- Only real logos, testimonials, ratings and numbers. If the user has none, leave a clearly marked placeholder or omit the section. Never invent them.
- A testimonial is stronger with a name, role, company and a specific result.
- Numbers need a basis ("used by 3,000 clinics" must be true and current).

## Conversion basics

- One goal per page. Repeat the same CTA after major sections rather than adding different ones.
- Reduce form fields to what is needed now. Each extra field costs completions.
- Pricing: show it if you can. Make plan differences scannable; highlight one plan only if it is genuinely the best fit for most.
- Remove navigation distractions on paid-traffic landing pages if the goal is a single action.
- Page speed is part of conversion: compress images, avoid heavy video autoplay on mobile, check Core Web Vitals (see `implementation-qa.md`).

## Visual approach

- Typography does most of the brand work: a distinctive display face for headlines with a quiet text face can carry a whole site.
- Generous section spacing (80 to 128px on desktop) and a narrow text measure.
- Alternate text and visuals for rhythm, but keep a consistent grid.
- See `anti-slop.md`: marketing pages are where AI defaults (gradients, blobs, three icon boxes, "Supercharge your workflow") show most.

## SEO and sharing basics

- One `h1`, logical heading order, descriptive `title` (about 50 to 60 characters) and meta description (about 150 to 160).
- Open Graph and Twitter card image (1200×630) and text.
- Real alt text on meaningful images.
- Fast first load; text rendered as HTML, not inside images.

## Measuring

Define the conversion event before launch, instrument it, and compare against a baseline. A higher click rate on a button is not proof the page is better; check downstream completion (see `metrics-experimentation.md`).

### Pricing pages

- **2 to 4 plans,** starting from 3. Emphasize exactly one; badging none or several gives no signal.
- **Lead each card with what separates it from the plan below** (1, 3 or unlimited projects) and link to a full comparison table instead of thirty check marks per card.
- **Name plans for who they are for** (Solo, Team, Agency), not Basic and Standard. One button per card that names the plan ("Choose Team"); repeat it at the end of long pages.
- **A billing toggle only if both periods exist,** with the annual saving stated as an amount or "2 months free".
- **Answer the money questions beside the table:** billing cycle, cancelling, refunds, trial terms. Put "No card required" or a guarantee next to the button, not in fine print.
- **Seat sliders or usage estimators** only when price really scales with them. "Talk to sales" only for large or complex deals. Local currency where the audience is global.
- **Order low to high by default.** Showing the highest plan first is anchoring, not deception, and can be tested. A crossed-out "was" price that was never charged is deception (`deceptive-design.md`).
- **Message match on campaign pages:** the headline repeats the promise of the ad or link that brought the visitor. A floating chat widget is a desktop treatment; on mobile it covers buttons.
