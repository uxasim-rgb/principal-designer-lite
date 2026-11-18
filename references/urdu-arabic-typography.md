# Urdu and Arabic script typography

Practical rules for interfaces in Urdu, Arabic and related scripts. Read with `localization-rtl.md`, which covers direction, bidirectional text and regional formats.

## Nastaliq versus Naskh

- **Urdu readers expect Nastaliq** for reading text. It is the cultural default for Urdu; using a Naskh face for Urdu body copy often reads as foreign or as Arabic.
- **Arabic uses Naskh** (and Kufi or modern sans styles for UI and display).
- Naskh can be acceptable for very dense Urdu UI (tables, small labels) when Nastaliq would not fit, but test with real readers first.
- Open, web-licensable Nastaliq fonts include Noto Nastaliq Urdu and Gulzar. Check the license of any other Urdu font before shipping it on the web or in an app.

## Size and spacing

Nastaliq is tall, diagonal and stacks letters vertically, so Latin defaults break it:

| Setting | Latin default | Nastaliq starting point |
| --- | --- | --- |
| Body size | 16px | 18 to 20px (it looks smaller at the same size) |
| Line height | 1.5 | 2 to 2.4 |
| Fixed-height containers | Common | Avoid. Let height grow; clipping of descenders and dots is the most common bug |
| Truncation | Ellipsis at one line | Allow two lines; single-line clamp often clips glyph tops |
| Money and critical numbers | Often in fixed-width boxes | Never clipped or truncated at any text size. Do not put a balance inside `overflow: hidden` or a fixed height; let the row wrap or stack instead |
| Letter spacing | 0 | Always 0. Letter spacing breaks joined letters |

Naskh Arabic needs less than Nastaliq: around 1.6 to 1.8 line height and a size about 10 to 15 percent above the Latin equivalent.

## Things that do not exist in these scripts

- No uppercase. Do not apply `text-transform: uppercase` styles to Urdu or Arabic labels; use weight or size for emphasis.
- No true italics. Do not fake-slant; use weight or color.
- Avoid `text-align: justify` on the web; browser justification does not use proper kashida elongation and produces gaps.

## Numerals

- Arabic-script digits come in two sets: Arabic-Indic (used in many Arabic-speaking countries) and Extended Arabic-Indic (the Persian/Urdu forms, which differ for 4, 5, 6 and 7).
- In Pakistan, Western digits (0 to 9) are widely used in apps, prices and dates, even in Urdu text. Decide per product and audience, and be consistent.
- Numbers stay left to right inside right-to-left text. Phone numbers, card numbers and IDs need isolation so they do not reorder.

## Dates and relative time in Urdu

- "کل" means both yesterday and tomorrow. Use "گزشتہ کل" for yesterday, or show the date, so a transaction list is never ambiguous.
- Prefer group headers by date over repeating a date on every row in narrow layouts.

## Direction and mixed content

- Set `lang="ur"` (or `ar`) and `dir="rtl"` on the root or the right container so fonts, shaping and screen readers behave.
- Wrap user-generated names and mixed-language strings in `<bdi>` or use `dir="auto"` so an English product name inside Urdu text does not scramble punctuation.
- Use CSS logical properties (`margin-inline-start`, `padding-inline-end`) so layouts mirror without separate stylesheets.
- Mirror directional icons (back, forward, reply, progress direction). Do not mirror icons that represent real objects or time (clock, play button, checkmark, media scrubbers in many conventions, logos).

## Testing

- Test with real Urdu or Arabic text, not machine-translated filler. Long words and diacritics change layout.
- Test with diacritics (zer, zabar, pesh) on, since they add vertical height.
- Check rendering in the browsers and OS versions your users have; Nastaliq shaping quality differs.
- Ask a native reader to review hierarchy and tone; weight and size cues do not transfer one to one from Latin.
