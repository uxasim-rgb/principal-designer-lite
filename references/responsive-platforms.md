# Responsive, adaptive, multimodal, and platform-specific design

Operational guide and topic inventory. Procedures and checks are an original synthesis; use the source register for the authority, inspected portion, and limits of specific references.

### Coverage

| Area | Details to consider |
| --- | --- |
| Layout strategy | Responsive reflow; adaptive composition; content-first constraints; intrinsic sizing; min/max; breakpoints; container conditions; panes. |
| Changing environments | Window resize; orientation; split screen; folding; keyboards; safe areas; display scaling; browser chrome; backgrounding. |
| Input capabilities | Touch/pointer co-existence; keyboard; pen; remote; controller; gaze; voice; assistive inputs; hardware. |
| Phone/tablet/desktop | Reach; task depth; navigation; multiwindow; file workflows; expert commands; persistent context; transfer. |
| Wearable/TV | Glanceability; short tasks; distance; focus traversal; shared accounts; low input bandwidth; battery and companion device. |
| Spatial | Depth; scale; field of view; occlusion; tracking; embodied reach; gaze; hands; comfort; motion; physical constraints. |
| Embedded/public | Kiosk; ATM; POS; industrial; medical; vehicle; viewing distance; gloves; posture; privacy; shared session; environment. |
| Resilience | Connectivity; latency; low power; memory; peripheral failure; offline; sensor failure; synchronization; state restoration. |
| Output channels | Visual; semantic; audio; haptic; captions; transcripts; print; email; document; cross-channel service. |

### Procedure

1. Name the actual target surfaces, versions, window conditions, input capabilities, physical contexts, and supported user settings.
2. Prioritize the user's tasks and information before creating a set of screen-size mock-ups.
3. Define what reflows, changes composition, becomes supplementary, or changes interaction. Preserve essential actions and meaning.
4. Specify navigation, multi-pane relationships, input alternatives, and state continuity during environment changes.
5. Load current platform guidance when a platform-specific rule affects the decision. Retain documented project differences.
6. Evaluate constrained and expanded windows, text scaling, long content, posture changes, and actual input combinations.
7. Check physical and service constraints for public, embedded, spatial, or safety-sensitive contexts with the relevant specialists.
8. Publish a support and verification matrix with representative tested cases and known gaps.

### Outputs

Platform/context profile; adaptive rules; pane/navigation models; input matrix; continuity specification; representative verification coverage.

### Quality checks

Behavior responds to actual available space and capability; state survives changes; information priority is explicit; input alternatives work; supported versions are known; physical context is evaluated.

### Limits and common failures

Phone, tablet, and desktop labels alone do not determine a layout. Screen size is not a reliable proxy for pointer or keyboard capability. Platform logical units and physical pixels are distinct. Older video guidance needs a current applicability check.

### Sources to consult

- S01: [Fluent 2: Layout](https://fluent2.microsoft.design/layout). Body excerpts inspected.
- S27: [CSS Values and Units Level 4](https://www.w3.org/TR/css-values-4/). Status and selected concepts inspected.
- S28: [CSS Logical Properties Level 1](https://www.w3.org/TR/css-logical-1/). Status and scope inspected.
- S29: [CSS Grid Layout Level 2](https://www.w3.org/TR/css-grid-2/). Status and scope inspected.
- S30: [Apple HIG: Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility). Markdown body excerpts inspected.
- S31: [Android: Make apps accessible](https://developer.android.com/guide/topics/ui/accessibility/apps). Body excerpts inspected.
- S32: [Android: Adaptive apps](https://developer.android.com/develop/adaptive-apps/guides/get-started-with-adaptive-apps). Page excerpts inspected.
- S33: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines). Markdown overview inspected.
- S49: [Apple WWDC23: Principles of spatial design](https://developer.apple.com/videos/play/wwdc2023/10072/). Official summary inspected; playback not reviewed.
- S50: [Apple WWDC23: Spatial user interfaces](https://developer.apple.com/videos/play/wwdc2023/10076/). Official summary inspected; playback not reviewed.
- S51: [Apple WWDC23: Spatial input](https://developer.apple.com/videos/play/wwdc2023/10073/). Transcript excerpt inspected; playback not reviewed.

### Design for the thumb

- **Primary actions in the lower middle,** or in a bottom sheet. Destructive actions out of the easy reach zone, or guarded. Add bottom padding so content can scroll up into the comfortable middle.
- **Corners are harder to hit,** so targets there should be larger than the minimum. Keep about 8dp between adjacent targets (Material 3) and separate opposite actions such as Save and Delete.
- **Gestures are shortcuts to a visible control,** never the only way. Use conventional single-finger gestures (WCAG 2.5.1).
- **One floating action button at most,** for the screen's main create action only, never destructive, never covering content.
- **Icons:** start from SF Symbols or Material Symbols and match custom icons to their weight and grid. On Apple platforms use monochrome rendering for controls and save hierarchical, palette or multicolor for icons that carry meaning.
- **If the product really is desktop-only,** say so and skip mobile findings rather than inventing them.
