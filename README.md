# Principal Product Designer Lite

One skill that makes Claude work like a principal product designer: the most senior hands-on designer on a team. It frames the problem, makes the artifact (an HTML mock, a spec, a research plan or a critique), checks its own work, and is honest about what it did not verify.

This is the single-skill version. The full collection, with 48 focused skills and a lead designer agent, is [Principal Product Designer](https://github.com/uxasim-rgb/principal-designer).

## What it does

- Covers the whole product design lifecycle: research, strategy, information architecture, interaction and states, visual design, spacing, typography, color, design systems, accessibility, localization (including Urdu and Arabic), native platforms, motion, AI and agent UX, metrics, launch and retirement.
- Picks sensible defaults and states them instead of asking ten questions.
- Sizes the answer to the request: a copy fix gets a sentence, a new flow gets a spec.
- Never invents users, quotes, numbers or partner names.
- Renders visual work at narrow and wide widths and at large text before calling it done.
- Labels work in medical, finance and other regulated domains as a concept and names the specialist review it needs.

## Install

With the skills CLI:

```bash
npx skills add uxasim-rgb/principal-designer-lite
```

Or by hand: copy this folder to `~/.claude/skills/principal-designer-lite` (leave out `evals/`). Claude uses it automatically when a request is about design, or you can call it with `/principal-designer-lite`.

## What is inside

| Folder | Holds |
| --- | --- |
| `SKILL.md` | The router: how the designer works and which file to read for each task |
| `references/` | 37 reference files, from research methods to craft defaults and anti-slop rules |
| `catalogs/` | 320 workflows, 104 context packs and 120 small checks, searched rather than read whole |
| `examples/` | Four finished deliverables showing the expected shape |
| `evals/` | 12 test cases with 63 graded checks |

## Test results

Run against the same 12 design tasks with and without the skill, the version with the skill passed 94% of the graded checks against 83% without it. The biggest gains were in honesty (not describing a video it had not watched, not inventing banks or user counts) and in catching real rendering bugs by looking at its own output.

## License

Not yet chosen.
