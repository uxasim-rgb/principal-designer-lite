# Visual foundations: typography, color, imagery, shape, and depth

Operational guide and topic inventory. Procedures and checks are an original synthesis; use the source register for the authority, inspected portion, and limits of specific references.

### Coverage

| Area | Details to consider |
| --- | --- |
| Composition | Hierarchy; grouping; alignment; proportion; scale; density; visual rhythm; negative space; reading order; focal points; balance. |
| Typography | Family; fallback; scripts; variable axes; font size; weight; line height; measure; tracking; kerning; paragraph spacing; baseline; tabular numerals. |
| Text behavior | Wrapping; hyphenation; truncation; ellipsis; line clamp; overflow; text scaling; dynamic type; zoom; diacritics; mixed scripts; missing glyphs. |
| Color | Brand primitives; semantic roles; text/background pairs; status; interaction; charts; gradients; gamut; color spaces; contrast; color vision; forced colors. |
| Shape | Corners; borders; strokes; separators; clipping; component geometry; shape roles; touch area; outline and focus; optical alignment. |
| Depth | Surface roles; layers; elevation; shadow; translucency; scrims; z-order; background contrast; occlusion; system material constraints. |
| Icons and media | Symbol meaning; icon family; viewport; stroke; fill; optical size; bounding boxes; image crop; focal point; alt text; licensing. |
| Expression | Brand character; visual direction; illustration; photography; motion personality; restraint; consistency; meaningful signature moments. |

### Procedure

1. Start with the task, information hierarchy, audience, supported scripts, environment, and brand constraints.
2. Choose a coherent visual direction and explain how it supports the product. Keep examples sufficiently different to make a real direction decision.
3. Define type roles and color roles semantically, then assign values and appropriate platform equivalents.
4. Test actual headings, long identifiers, numeric comparisons, content extremes, and localized scripts. Verify fallback fonts and text scaling.
5. Define shape, border, depth, icon, and imagery rules with meaningful states and sufficient contrast.
6. Check optical alignment as well as mathematical bounds. Account for icon view-box whitespace and font metrics rather than applying arbitrary offsets everywhere.
7. Review light, dark, high-contrast, low-quality displays, and real content in context.
8. Document intentional exceptions and validate implementation; visual attractiveness does not establish task success.

### Outputs

Visual direction; semantic type/color roles; foundations specification; asset guidance; theme mapping; visual QA findings.

### Quality checks

The hierarchy survives real content and scaling; semantic meaning survives theme changes; information does not rely only on color; scripts and numerals remain legible; assets have appropriate rights and text alternatives.

### Limits and common failures

Avoid universal body-size, line-height, line-length, corner-radius, and contrast recipes independent of context. Token names should describe roles where reuse requires meaning. Dark mode requires role-specific decisions; automatic color inversion is insufficient. Aesthetic approval may conceal minor usability difficulties during evaluation.

### Sources to consult

- S01: [Fluent 2: Layout](https://fluent2.microsoft.design/layout). Body excerpts inspected.
- S03: [Carbon: 2x Grid](https://www.carbondesignsystem.com/building-blocks/foundations/2x-grid/overview). Body excerpts inspected.
- S30: [Apple HIG: Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility). Markdown body excerpts inspected.
- S33: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines). Markdown overview inspected.
- S37: [NN/G: Aesthetic-usability effect](https://www.nngroup.com/articles/aesthetic-usability-effect/). Body excerpts inspected.
- S52: [Apple WWDC19: Accessible reading](https://developer.apple.com/videos/play/wwdc2019/248/). Transcript excerpt inspected; playback not reviewed.
