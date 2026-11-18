# Design tokens, themes, modes, and design-code alignment

Operational guide and topic inventory. Procedures and checks are an original synthesis; use the source register for the authority, inspected portion, and limits of specific references.

### Coverage

| Area | Details to consider |
| --- | --- |
| Token levels | Primitive/reference; semantic/system; component; aliases; ownership; shared versus platform-specific values. |
| Token families | Color; dimension; typography; font; border; radius; opacity; shadow; elevation; duration; easing; spacing; size; z-order. |
| Modes and axes | Light/dark; contrast; brand; locale; density; platform; motion preference; product variant; capability. |
| Naming | Meaning; hierarchy; role; state; target; direction; scale; deprecated names; reserved syntax. |
| Data integrity | Type; value; unit; alias; reference; cycle; fallback; missing token; duplicate; inheritance; composite token. |
| Delivery | Source of truth; transforms; generated outputs; UI-kit variables; code packages; version; mapping; change review; compatibility. |
| Testing | Reference resolution; valid units; completeness by mode; contrast pairs; component mapping; snapshots; migration; exceptions. |

### Procedure

1. Inventory current design and implementation values, variants, source systems, and known drift.
2. Define the token roles and supported axes. Avoid a combinatorial collection of modes without an actual consumer need.
3. Choose names that preserve meaning at each level. Use primitive names for raw values and semantic names for intended roles.
4. Define alias resolution, type expectations, units, inheritance, fallback behavior, and platform transforms.
5. Map design-tool variables and component properties to implementation equivalents. Identify which representations cannot round-trip faithfully.
6. Generate outputs from a declared source of truth where feasible. Validate aliases, cycles, modes, and meaningful contrast relationships.
7. Document the change policy, deprecation and migration path, ownership, and how local exceptions are approved.
8. Test representative components across supported modes and platforms before releasing.

### Outputs

Token taxonomy; typed definitions; mode/alias matrix; design-code mapping; transform requirements; validation report; migration guide.

### Quality checks

Types and units are explicit; aliases resolve without cycles; semantic roles are coherent; mode combinations are supported; transformations are traceable; exceptions and breaking changes are documented.

### Limits and common failures

A naming hierarchy is an architectural choice, not a mandatory universal three-tier law. DTCG 2025.10 is a Community Group specification and is explicitly not a W3C Standard (S04). A valid token file does not prove an accessible theme.

#### Minimal dimensional example

~~~json
{
  "space": {
    "$type": "dimension",
    "100": {"$value": {"value": 4, "unit": "px"}},
    "200": {"$value": {"value": 8, "unit": "px"}},
    "400": {"$value": {"value": 16, "unit": "px"}}
  },
  "component": {
    "card": {
      "inset": {"$type": "dimension", "$value": "{space.400}"}
    }
  }
}
~~~

This illustrates typed dimensions and an alias. Verify the selected exchange format, version, and tooling before claiming full conformance. No validation script ships with this skill; use the tooling the project already has.

#### Theme review

Define relationships such as foreground/background, border/surface, selected/unselected, focus/adjacent background, and chart series/context. Test actual states and content. Preserve meaning across themes, not numerical equality. Address system high-contrast and forced-color behavior through the applicable implementation guidance.

A token change can affect hundreds of interfaces. Record the intended semantic effect, affected components, theme and platform impacts, required review, release type, and rollback or migration route.

### Sources to consult

- S04: [DTCG Format Module 2025.10](https://www.designtokens.org/tr/2025.10/format/). Status and selected sections inspected.
- S01: [Fluent 2: Layout](https://fluent2.microsoft.design/layout). Body excerpts inspected.
- S02: [Carbon: Spacing](https://www.carbondesignsystem.com/building-blocks/foundations/spacing/overview). Body excerpts inspected.
- S30: [Apple HIG: Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility). Markdown body excerpts inspected.
