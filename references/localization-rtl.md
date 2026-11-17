# Localization, RTL, scripts, regional rules, and content operations

Operational guide and topic inventory. Procedures and checks are an original synthesis; use the source register for the authority, inspected portion, and limits of specific references.

### Coverage

| Area | Details to consider |
| --- | --- |
| Language architecture | Locale/language distinction; fallback; detection; selection; remembered choice; translated/untranslated; source text; string context. |
| Grammar | Pluralization; grammatical gender; inflection; placeholders; sentence order; concatenation; variable length; pseudo-localization. |
| RTL and scripts | Base direction; bidirectional isolation; mixed text; identifiers; punctuation; ordering; mirroring exceptions; keyboard and focus; numerals. |
| Formats | Dates; calendars; time zones; daylight saving; numbers; decimal/group separators; currency; units; phone; address; personal names. |
| Typography | Script coverage; fallback; shaping; ligatures; diacritics; baseline; line height; word wrapping; truncation; text expansion. |
| Regional behavior | Fields; eligibility; features; documents; terminology; content; business rules; policies; payment methods; source applicability. |
| Cultural validation | Images; symbols; examples; sensitivity; trust; local expectations; research; expert review; stereotype avoidance. |
| Operations | Authoring; approval; translation; context screenshots; terminology; review; QA; version sync; maintenance; archive. |

### Procedure

1. Identify supported languages, scripts, regions, audiences, and actual regional business variations.
2. Separate translatable content from locale-dependent behavior and domain rules.
3. Design resilient strings and layouts, including expansion, plurals, mixed scripts, and realistic identifiers.
4. Specify document base direction and logical layout; define exceptions based on meaning and platform conventions.
5. Verify time, number, money, unit, address, and name handling against actual locale needs.
6. Provide translation context, terminology, content ownership, and an approval/review workflow.
7. Test real localized tasks with the correct fonts, accessibility tools, and representative users.
8. Track untranslated, stale, regionally incorrect, or inaccessible content as product defects.

### Outputs

Locale and regional matrix; terminology/glossary; direction/format rules; string/content contract; localized QA evidence.

### Quality checks

Locales are explicit; core tasks survive expansion and scaling; mixed-script data remains readable; regional variations are sourced; time ambiguity is handled; translations match actual behavior.

### Limits and common failures

RTL is more than reversing a screenshot. CSS positioning alone does not establish text direction. Arabic and Urdu can need distinct font and line-height decisions; test actual text and diacritics. Never assume all people in a region share one cultural preference.

### Sources to consult

- S25: [W3C: Structural RTL markup](https://www.w3.org/International/questions/qa-html-dir.en.html). Body excerpts inspected.
- S28: [CSS Logical Properties Level 1](https://www.w3.org/TR/css-logical-1/). Status and scope inspected.
- S30: [Apple HIG: Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility). Markdown body excerpts inspected.
- S53: [Apple WWDC22: Writing for interfaces](https://developer.apple.com/videos/play/wwdc2022/10037/). Transcript excerpt inspected; playback not reviewed.

### Urdu and Arabic typography

For Nastaliq and Naskh sizing, line height, numerals and script-specific rules, read `urdu-arabic-typography.md`.
