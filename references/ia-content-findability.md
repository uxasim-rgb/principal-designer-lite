# Information architecture, content, and findability

Operational guide and topic inventory. Procedures and checks are an original synthesis; use the source register for the authority, inspected portion, and limits of specific references.

### Coverage

| Area | Details to consider |
| --- | --- |
| Information models | Objects; relationships; hierarchy; taxonomy; facets; metadata; controlled vocabulary; aliases; tags; provenance; ownership. |
| Navigation | Global/local/contextual; information scent; breadcrumbs; tabs; navigation rails; sidebars; routes; deep links; progressive disclosure. |
| Findability research | Content audit; open/closed/hybrid card sorting; tree tests; first-click tasks; query analysis; labeling studies; cross-link review. |
| Search | Query entry; autocomplete; suggestions; recent searches; result relevance; snippets; highlights; filters; sorting; grouping; saved views. |
| Recovery | No results; spelling; ambiguous intent; permissions; unavailable content; stale index; removed object; broken deep link; alternative routes. |
| Content craft | Labels; headings; instructions; hints; empty states; success; error; confirmation; terminology; voice; contextual tone; reading order. |
| Content operations | Structured content; authoring; approval; localization; version; audit; review dates; archive; retirement; cross-channel reuse. |
| Comprehension | Plain language; consequences; action specificity; jargon; numeric meaning; risk statements; progressive explanation; accessible reading. |

### Procedure

1. Inventory content and objects, user tasks, current labels, ownership, and the consequences of finding the wrong item.
2. Build a conceptual organization around meaningful relationships. Test whether the structure matches user understanding rather than an internal org chart.
3. Define navigation, search, and browse as a connected finding experience, including return paths and recoverable dead ends.
4. Specify labels and result anatomy with realistic content. Explain distinctions users must make without requiring undocumented domain knowledge.
5. For filters, define combination logic, counts, application timing, reset, persistence, grouping, and selection consequences.
6. Write messages in the actual interaction context. State the outcome or problem and the useful next action.
7. Validate representative findability and comprehension tasks. Choose card sorting or tree testing only when the question fits.
8. Assign source-of-truth and maintenance rules so help and labels remain aligned with the product.

### Outputs

Object/content map; taxonomy; navigation and search specification; UI copy matrix; content model; findability/comprehension evaluation plan.

### Quality checks

Content supports the actual task; labels distinguish similar concepts; search recovery is useful; important information survives translation and truncation; copy does not promise unverified outcomes; ownership and review are defined.

### Limits and common failures

A sitemap alone does not specify IA. A successful card sort does not prove the final navigation is findable. Search ranking behavior needs the actual data and relevance evaluation. Shorter copy can remove essential meaning; clarity takes precedence over arbitrary word counts.

### Sources to consult

- S10: [NN/G: Choosing research methods](https://www.nngroup.com/articles/which-ux-research-methods/). Body excerpts inspected.
- S22: [WAI Forms Tutorial](https://www.w3.org/WAI/tutorials/forms/). Body excerpts inspected.
- S25: [W3C: Structural RTL markup](https://www.w3.org/International/questions/qa-html-dir.en.html). Body excerpts inspected.
- S53: [Apple WWDC22: Writing for interfaces](https://developer.apple.com/videos/play/wwdc2022/10037/). Transcript excerpt inspected; playback not reviewed.

### Choose the scheme and structure before the labels

- **Exact schemes** (A to Z, by date, by place) work only when people already know the item's name. **Browsing needs topic, task or audience schemes.** Mixing schemes is fine on a home page and confusing deeper down.
- **Structure follows the content:** a hierarchy for top-down browsing; a database with facets for large sets of similar items; a sequence for step-by-step processes; flat for small sites. Cross-links supplement a structure, never replace it.
- **Check the label system as a set:** one syntax (do not mix verbs, nouns and questions); one level of granularity ("Electronics" does not sit beside "Smartphones"); complete sets (a "Men" and "Kids" with no "Women" makes people distrust the rest); no empty labels such as "Explore", "Discover" or "More".
- **Sweep every way people seek:** a known item, exploring, browsing, finding something again (recently viewed, history), and not knowing what they need, which calls for plain labels ("Tax forms", not "Resources").
- **Audit from the side door.** Arrive on a deep page from a search result: the page must say where you are, reach the main areas, and offer siblings or the parent.
- **Growth test:** where would the next 50 items go? A structure that already strains fails.
- **Cheap evidence for labels:** search log analysis and free listing, before or alongside card sorts.

### Match tone to the moment, not only the brand

| Moment | Tone | Rule |
| --- | --- | --- |
| Payment, security, data loss | Confident and plain | No hedging ("maybe", "try to") |
| Light errors, empty inboxes | Playful is allowed | Only when nothing is at stake, never at the cost of clarity |
| Effort or achievement | Encouraging | Do not cheer routine actions |
| Permission and data requests | Direct, active | Say what is collected and why |
| Regulated or professional | Formal | Still plain words |
| Dense UI and mobile labels | Terse | Keep the context that is needed |

A joke on a payment error is a finding. Lead an error with the action that fixes it rather than the failure.

**Links:** say when a link opens a new tab, give file links their type and size ("Annual report (PDF, 2.5 MB)"), and never use a raw address as link text. These are good practice, not WCAG failures.

**Copy review procedure:** inventory every string first, including the hidden ones (errors, empty states, tooltips, confirmations, notifications); check consistency across the whole flow, not screen by screen; report each finding as current text and rewrite, with a list of inconsistent terms and the top three rewrites.
