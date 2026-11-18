# Making: producing design artifacts

How to turn design thinking into something the user can open, judge and hand off. Pick the medium the user can evaluate fastest, and match any existing stack.

## Choosing the medium

| Need | Medium |
| --- | --- |
| See a screen or a few screens | Self-contained HTML file with inline CSS |
| Click through a flow | One HTML file with simple JS view switching, or linked pages |
| Work inside an existing app | The app's own framework, components and tokens |
| The user wants the result in Figma | Figma tools, using the file's components and variables. A Figma link sent for review or for building is input only |
| Explain a flow or states | Mermaid diagram or a state table |
| Compare directions | 2 or 3 variants side by side in one HTML file, clearly labeled |
| Low-fidelity structure | Grayscale HTML wireframe: real labels, boxes for media, no color |

## HTML mockups

1. Start from realistic content. Write the actual headings, labels, numbers and names first.
2. Set up CSS custom properties for the tokens you use (colors, spacing scale, radius, type sizes). This makes the mock honest about its system and easy to hand off.
3. Use semantic HTML: `header`, `nav`, `main`, `button`, `label`, `table`. It costs nothing and makes accessibility checks possible.
4. Build mobile and desktop with one responsive layout (CSS grid or flex, a few media queries).
5. Include at least the states the task depends on: empty, loading, error, long content. Put them as extra sections or a state switcher.
6. Keep it dependency-free unless the user's stack says otherwise. If you need icons, inline SVG from one consistent set.
7. No fake brand logos, testimonials or metrics. Mark placeholders as placeholders.

## In an existing codebase

- Read the project's tokens, theme and existing components before writing anything.
- Reuse components; extend with props rather than forking.
- With Tailwind, use the configured scale; avoid arbitrary values like `p-[13px]` unless it is a documented exception.
- With a component library (shadcn/ui, MUI, Chakra, Radix), use its primitives for behaviour (dialogs, menus, comboboxes) so keyboard and focus work.
- Match file and naming conventions.

## Figma

- When Figma tools are available and the user wants Figma output, read the file's existing components, styles and variables first, and build with them.
- Use auto layout with spacing from the variables, not hand-positioned frames.
- Name layers and frames meaningfully; include state variants.
- If a component is missing from the library, build it as a local component and say so.

## Self-review procedure

When you can render the output in a browser or preview tool:
1. Look at it at 320px, 375px and desktop (around 1280 to 1440px) widths, and with text zoomed to 200%. Content must reflow at 320 CSS px without sideways scrolling.
2. Squint test: is the first thing you notice the most important thing?
3. Run the anti-slop pass (`anti-slop.md`).
4. Check contrast of text and key UI against the floor in `craft-defaults.md`.
5. Tab through it in the browser: is focus visible and in a sensible order? This needs a live page; a screenshot cannot show it.
6. Try long content and an empty state.
7. Fix what you find before showing it.

In the report, say which surface you had (live browser, screenshot only, or none) and list the widths, zoom and keyboard checks you actually ran.

With only a screenshot, report visual observations and list keyboard, focus, reflow and zoom as unchecked. When you cannot render it at all, say so and list what still needs a visual check. A missing preview is never reported as a passed check.

## Handoff from a mock

When a mock will be built by engineers, include with it:
- Tokens used (or the mapping to the project's tokens).
- Each component used and its states.
- Behaviour that the mock fakes (data loading, validation, permissions).
- Responsive rules in words: what stacks, what hides, what reflows.
- Open questions.

See `implementation-qa.md` and `output-contracts.md` (engineering handoff) for the full contract.
