# Design critique

How to review a design so the feedback is useful, specific and honest about what the artifact can show.

## Before critiquing

- What is the design trying to achieve, for whom, at what stage? A wireframe gets structural feedback; a final mock gets polish feedback. If unknown, assume from the artifact and say so.
- What can the artifact show? A screenshot shows layout, hierarchy, copy, color and type. It cannot show behaviour, hit areas, keyboard or screen-reader support, or performance. Mark those as "needs runtime check", not as findings.

## Order of review

Go from what matters most to least, so the big problems are not buried under pixel notes:

1. **Purpose and task fit.** Can the user tell what this is and what to do? Is the primary action obvious?
2. **Information and flow.** Is the content in the order the user needs it? Is anything missing (a price, a status, a next step)?
3. **Hierarchy and layout.** Squint test. Grouping by proximity. Alignment. Scanability.
4. **Interaction and states.** Implied behaviour, missing states (empty, error, loading), recovery, destructive actions.
5. **Content and copy.** Labels, errors, buttons, terminology consistency.
6. **Visual craft.** Type, spacing consistency, color use, icon consistency, the anti-slop list.
7. **Accessibility.** Contrast (measurable from pixels, roughly), text size, color-only meaning, visible labels, target size estimates.

## Writing each finding

Use this shape (see `output-contracts.md`, audit finding):
- **Where:** screen, element, state.
- **Issue:** what you observe, specifically.
- **Why it matters:** the effect on the user's task.
- **Severity:** critical (blocks task or causes harm), major (causes errors or significant delay), minor (friction), polish.
- **Fix:** a concrete change. Show it when possible.

Good: "The 'Delete project' button uses the same filled blue as 'Save' and sits beside it. Users scanning for the primary action may hit delete. Make delete a text or outline button in danger color, move it away from Save, and confirm with the project name." (major)

Weak: "The buttons could be clearer."

## Tone

- Be direct. Lead with the most important issues. Do not soften critical findings into suggestions.
- Name what works, briefly and specifically, so it is not lost in a redesign.
- Separate fact (observable), judgement (your expert opinion, labelled as such) and hypothesis (would need testing).
- Do not pad to reach a number of findings. Five real issues beat twenty trivial ones.

## Heuristic frameworks

Nielsen's 10 heuristics and Shneiderman's 8 rules (see `laws-principles.md`) are useful lenses for completeness. Use them to check you have not missed a category, not as a scorecard to fill in.

## Output

Summary (2 or 3 lines: overall state and the top issues), then findings ordered by severity, then "Needs runtime or user check", then optionally a revised mock showing the top fixes.
