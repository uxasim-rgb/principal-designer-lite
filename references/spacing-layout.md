# Spacing, padding, layout grids, baseline rhythm, and density

Operational guide and topic inventory. Procedures and checks are an original synthesis; use the source register for the authority, inspected portion, and limits of specific references.

### Coverage

| Area | Details to consider |
| --- | --- |
| Spacing vocabulary | Content box; padding; border; margin; gap; inset; container; gutter; column; row; keyline; baseline; safe area. |
| Scale design | 4-unit; 8-unit; mixed scales; half steps; zero; semantic aliases; optical exceptions; component versus layout roles. |
| Grid types | Manuscript; column; modular; hierarchical; baseline; icon/pixel; fixed; fluid; hybrid; nested; subgrid; spatial arrangement. |
| Layout behavior | Intrinsic sizing; min/max; content constraints; wrapping; reflow; fractional columns; breakpoints; container queries; viewport insets. |
| Density | Compact/comfortable/spacious; input capability; expertise; scanability; row heights; hit targets; text expansion; content priority. |
| Alignment | Geometric/optical; glyph bounds; line box; icon viewport; stroke position; text baseline; numeric alignment; truncation. |
| Platform units | CSS px; root-relative rem; font-relative em; Android dp/sp; Apple points; physical pixels; density and scaling. |
| Exceptions | Thin borders; optical corrections; safe areas; dynamic text; fluid widths; full-bleed media; separators; platform controls. |

### Procedure

1. Inventory the product's current spacing values, recurring relationships, input methods, information density, and accessibility constraints.
2. Identify the applicable system. Retain its established scale when it works; assess a new scale with actual components and layouts.
3. Separate component-internal spacing from relationships among components and page-level layout.
4. Choose a base and a small useful ramp, then map semantic roles to values. Document intentionally allowed exceptions.
5. Define fixed, fluid, and conditional behavior separately. Fluid columns and available widths can legitimately produce fractional dimensions.
6. Specify padding and gaps logically for the writing mode. Include container edges, gutters, wrapping, and safe-area behavior.
7. Test compact and comfortable variants with real text, localized content, pointer/touch input, zoom, and text scaling.
8. Audit implementation for inconsistent values and undocumented exceptions; review each flagged value rather than declaring every off-grid value defective.

### Outputs

Spacing inventory; primitive/semantic ramp; grid specification; responsive/density rules; exception register; example compositions; implementation audit.

### Quality checks

Grouping is clear; task hierarchy is supported; spacing does not clip text; hit areas remain usable; fluid layout rules are explicit; CSS and native units are not confused; exceptions have reasons.

### Limits and common failures

4px and 8px are design-system conventions, not universal UX laws. A grid cannot override readable text, meaningful grouping, platform behavior, or applicable accessibility requirements. A border or optical adjustment need not be forced to the layout base.

#### Working definitions

| Term | Operational distinction |
| --- | --- |
| Padding | Space inside an element's border between its content and border |
| Margin | Space outside a box; understand layout context and possible margin collapsing |
| Gap | Space managed by an applicable parent layout between its items |
| Gutter | A named separation between grid columns or other layout regions |
| Container inset | Space between a container boundary and its contents |
| Baseline rhythm | Alignment or repeated rhythm related to text baselines; it is distinct from a component spacing scale |
| Optical adjustment | A deliberate correction for perceived alignment or balance; document it separately from the main ramp |
| Hit area | The actionable region; it may exceed the visible glyph or shape without overlapping another target |
| Density | The amount and organization of information relative to available space and user task |

#### Comparing common approaches

Fluent documents a four-pixel base ramp with values such as 2, 6, and 10 for particular alignment needs (S01). Carbon describes an eight-pixel mini-unit for its 2x Grid (S03), while its spacing guidance includes multiples of two, four, and eight (S02). Each statement describes that system's approach.

| Approach | Useful context | Evaluate before adopting |
| --- | --- | --- |
| 4-unit ramp | Smaller component relationships and products needing fine spacing steps | Excessive near-duplicate tokens, inconsistent grouping, constrained touch targets |
| 8-unit ramp | Stronger macro rhythm and a smaller set of common layout intervals | Dense controls, small icons, text metrics, useful smaller intervals |
| Mixed ramp | Different levels of hierarchy and documented optical or component needs | Clear semantic roles and controlled exceptions |
| Fluid layout with tokenized insets | Resizable, multilingual, content-driven interfaces | Min/max constraints, wrapping, content order, intrinsic size |
| Density variants | Different information and input contexts | Equivalent functionality, accessibility, user choice, predictable switching |

#### Illustrative project ramp

This is an example to adapt, not an official system's token set.

| Primitive | Example CSS value | Possible semantic use |
| --- | --- | --- |
| space.0 | 0 | Explicit no-gap relationship |
| space.1 | 4px | Closely related micro content |
| space.2 | 8px | Icon/text or related content gap |
| space.3 | 12px | Compact internal padding when appropriate |
| space.4 | 16px | Common container inset |
| space.6 | 24px | Separation among related groups |
| space.8 | 32px | Larger section relationship |
| space.12 | 48px | Major layout interval |

Select values by composition and test them. A 12px gap or 20px inset can be valid even if another product prefers 8px increments. Assign semantic aliases such as field.labelGap, form.sectionGap, card.inset, and page.gutter to preserve meaning when density or layout changes.

#### Implementation considerations

Use margin, padding, and gap according to their responsibilities. Parent-managed gaps can avoid repeated child margins. Use border-box sizing where appropriate and understand what the chosen dimensions include. Select logical inline/block properties for direction-aware layout; verify browser support for the actual features used.

A CSS pixel is not necessarily one physical display pixel. Apple points and Android density-independent units belong to their platform coordinate systems. Root-relative values depend on the root font size; do not claim a universal px-to-rem conversion without stating that assumption. Android scalable text units and browser text sizing require their own behavior.

Avoid fixing every component's height merely to preserve a grid. Multiline labels, translation, user font sizes, Arabic or Urdu diacritics, and assistive settings may require growth. An icon's visual center can differ from its view-box center. Inspect both the asset and rendered composition before adding a local correction.

For every important layout specify: container width behavior, column count or composition, gutters, outer insets, alignment, spacing roles, wrapping, minimum content size, overflow strategy, density, text scaling, and reading order.

### Sources to consult

- S01: [Fluent 2: Layout](https://fluent2.microsoft.design/layout). Body excerpts inspected.
- S02: [Carbon: Spacing](https://www.carbondesignsystem.com/building-blocks/foundations/spacing/overview). Body excerpts inspected.
- S03: [Carbon: 2x Grid](https://www.carbondesignsystem.com/building-blocks/foundations/2x-grid/overview). Body excerpts inspected.
- S26: [CSS Box Model Level 3](https://www.w3.org/TR/css-box-3/). Scope and selected concepts inspected.
- S27: [CSS Values and Units Level 4](https://www.w3.org/TR/css-values-4/). Status and selected concepts inspected.
- S28: [CSS Logical Properties Level 1](https://www.w3.org/TR/css-logical-1/). Status and scope inspected.
- S29: [CSS Grid Layout Level 2](https://www.w3.org/TR/css-grid-2/). Status and scope inspected.
