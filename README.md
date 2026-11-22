# Principal Product Designer Lite

One skill that makes Claude work like a principal product designer: the most senior hands-on designer on a team. It frames the problem, makes the artifact (an HTML mock, a spec, a research plan or a critique), checks its own work, and is honest about what it did not verify.

This is the single-skill version. The full collection, with 48 focused skills and a lead designer agent, is [Principal Product Designer](https://github.com/uxasim-rgb/principal-designer).

## What it does

- Covers the whole product design lifecycle: research, strategy, product specs and roadmaps, information architecture, interaction and states, visual design, spacing, typography, color, design systems, accessibility, localization (including Urdu and Arabic), native platforms, motion, AI and agent UX, metrics, launch and retirement.
- Picks sensible defaults and states them instead of asking ten questions.
- Sizes the answer to the request: a copy fix gets a sentence, a new flow gets a spec.
- Never invents users, quotes, numbers or partner names.
- Renders visual work at narrow and wide widths and at large text when it has a browser, and says plainly which checks it could not run when it does not.
- Labels work in medical, finance and other regulated domains as a concept and names the specialist review it needs.

## Install

With the skills CLI:

```bash
npx skills add uxasim-rgb/principal-designer-lite
```

The skills CLI copies the whole folder, including `evals/` and `benchmark/`. They are plain Markdown that the skill never reads, so they are harmless. Or by hand: copy this folder to `~/.claude/skills/principal-designer-lite` and leave out `evals/` and `benchmark/`. Claude uses it automatically when a request is about design, or you can call it with `/principal-designer-lite`.

## What is inside

| Folder | Holds |
| --- | --- |
| `SKILL.md` | The router: how the designer works and which file to read for each task |
| `references/` | 40 reference files, from research methods and product management to per-component guides, screen recipes and anti-slop rules |
| `catalogs/` | 320 workflows, 104 context packs and 120 small checks, searched rather than read whole |
| `examples/` | Four finished deliverables showing the expected shape |
| `evals/` | 14 test cases with 72 graded checks (for maintainers, not needed at runtime) |
| `benchmark/` | Results of past test runs |

## Test results

In one maintainer run of the 12 test cases, the version with the skill passed 59 of 63 graded checks (94%) and the version without it passed 53 (84%). The grader was an LLM, each case ran once, and no check opened a browser, so read this as a smoke test rather than a measured result. The biggest differences were in honesty: not describing a video it had not watched, and not inventing banks or user counts. Setup, per-case results and known limits are in [benchmark/2026-11-17.md](benchmark/2026-11-17.md).

## Changelog

- **1.1.0** (22 November 2026): merged the useful parts of [Uxcel Lab product-skills](https://github.com/Uxcel-Lab/product-skills) (MIT) after reading all 59 of its skills, rewritten and corrected where they disagreed with current standards. New references: `product-management.md`, `component-guides.md` and `screen-recipes.md`, plus new sections in 14 existing references. One waiting-time ladder replaces three that disagreed. See `THIRD_PARTY_NOTICES.md`.
- **1.0.1** (18 November 2026): fixed the skill header so the skills CLI can install it; corrected the age-error and export examples; Figma links are treated as input unless the person wants Figma output; render checks now name what was and was not checked; published the benchmark details.
- **1.0.0** (17 November 2026): first release.

## Credits

Per-component rules, screen recipes and the product management reference adapt material from [Uxcel Lab product-skills](https://github.com/Uxcel-Lab/product-skills) under the MIT License. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## License

MIT. See [LICENSE](LICENSE).
