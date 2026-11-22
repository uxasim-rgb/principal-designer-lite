# Product management: specs, roadmaps and go to market

How to write PRDs and specs, shape vision, strategy, roadmaps and OKRs, and plan competitive analysis and go-to-market. Problem framing and prioritization stay in `strategy-service-requirements.md`; metrics in `metrics-experimentation.md`.

Adapted in part from Uxcel Lab product-skills (MIT); see `THIRD_PARTY_NOTICES.md` in this skill folder.

## Product specs and user stories

Turn an agreed problem into a document a team can build and test from, after the problem is framed and prioritized (`strategy-service-requirements.md`).

The governing idea: a spec is finished when QA could write a pass or fail check for every requirement without asking the author.

### Pick the document first

| | PRD | Functional spec |
| --- | --- | --- |
| Answers | What and why | How the product behaves |
| Written | Early, while scope can move | After requirements are agreed |
| Reader | Everyone: leadership, design, engineering, support | Engineering, design and QA |
| Holds | Problem, goals, people, stories, success metrics | Behavior, states, rules, performance targets, dependencies |

Still deciding what to build means a PRD. The technical spec (how the code achieves it) belongs to engineering; a product spec that prescribes architecture is a finding.

### Gate on the problem

Before any requirement, write three lines: the **problem** (the gap, as a fact), the **consequence** (who is hurt and how), and the **goal** (the improvement, not the solution). If there is no evidence for the problem, carry on with it marked unvalidated on the first page; never present it as established.

### Write the sections a team needs

1. Summary: what, for whom, and why now, in three sentences.
2. Problem, consequence and goal.
3. Scope: what is in, and **what is out**, per release.
4. People and stories.
5. Requirements, each traceable to the problem.
6. Acceptance criteria.
7. Dependencies, constraints and assumptions.
8. Success metrics, with the baseline and where it comes from.
9. Open questions, each with an owner.

Write what is missing rather than inventing it: "Requirement 3 has no target yet" is a correct line in a spec. A made-up number is not.

### Write requirements QA can test

- **No undefined adjectives.** "Fast" becomes "results appear within 2 seconds for 95% of searches"; "easy" becomes a task and a measure.
- **Cover the whole flow,** not the happy path: errors, interruptions, returning users, partial drafts (and how long a draft is kept), permissions, empty and very large data. `interaction-states.md` has the checklist.
- **Testable covers more than function:** usability, performance and accessibility requirements get a check too ("meets WCAG 2.2 AA; keyboard path verified").

### Stories name the need; criteria carry the detail

- **Format:** As a [person from research], I want [action], so that [benefit]. Free form is fine when several roles or benefits will not fit one line, as long as who, what and why stay explicit.
- **Check each story against INVEST:** independent, negotiable, valuable, estimable, small, testable.
- **A story with no who or no why, or in technical words** ("Add login", "Improve dashboard performance"), is a task. Rewrite it from the need.
- **Filter types, edge cases and rules go in acceptance criteria,** written as given, when, then.
- **Split by user value** when a story spans several people or will not fit a cycle, never into technical layers.
- **A story map** runs problem, then capability, then stories, then tasks; every task traces up to a need.
- **Skip stories** when the spec already tells the team who, what and why.

### Dependencies, constraints and assumptions

- **Each dependency** is internal or external, with an owner and a date. External ones carry more risk; map the chain so one delay's knock-on effect is visible.
- **Constraints** cover budget, deadline, legacy technology and law, and say which of time, scope or quality is allowed to flex.
- **Each assumption** becomes a check with an owner, a deadline and a fallback if it proves false.
- **Early warnings:** a critical dependency with vague ownership, dates that disagree across teams, assumptions still unchecked after several cycles.

### Review and validation are different steps

Review checks the document's quality with engineering, design and the business. Validation is evidence from real users before the spec is final. A spec that says "validated" names the method, the participants and which requirements changed. Revisit the spec after reviews and after each release; it is a living document until the work ships.

Show the whole picture first, then the detail each team needs: annotated designs for frontend, data flows for backend, outcomes for leadership. Keep internal and external versions separate.

### Review by build damage

| Severity | What it causes |
| --- | --- |
| `Critical` | Teams build the wrong thing, or different things |
| `Serious` | Delivery breaks or drifts: missing dependency, untestable requirement, no exclusions |
| `Moderate` | Rework later: an unhandled failure path, a vague adjective |
| `Minor` | Hygiene: formatting, naming |

Flag missing decisions, not missing padding. Do not mark a PRD down for lacking the precision of a functional spec. Close with the top three fixes, each with a rewrite. These levels map onto the shared ladder in `critique.md`.

### Evidence

A spec states facts, decisions and assumptions, and labels which is which. Numbers in it (targets, limits, performance budgets) come from a measured baseline, a decision someone owns, or are marked as assumptions to confirm. A user problem claimed without evidence is marked unvalidated. Competitor or market claims carry a source.

### Quality checks

| Symptom | What it means | Fix |
| --- | --- | --- |
| "Fast", "simple", "intuitive" in a requirement | Untestable | Replace with a measure |
| No out-of-scope list | Scope will grow silently | List the exclusions per release |
| Stories with no "so that" | Tasks wearing story clothes | Rewrite from the need |
| Only the happy path is specified | Engineering will invent the rest | Run the `interaction-states.md` checklist |
| A target with no baseline | The number was invented | Mark it as an assumption or measure first |
| Architecture choices in the product spec | Wrong layer | Move them to engineering's technical spec |
| Assumptions listed but no owners | Nobody will check them | Owner, deadline and fallback for each |

### Outputs

**Format:** for a new spec, the document in the section order above, with open questions and unvalidated items marked. For a review, the top three fixes with rewrites, then findings by severity, then what works.

**Done when:** every requirement traces to the problem and has a check QA could run, scope names its exclusions, every assumption has an owner, and nothing in the document is invented.

## Vision, strategy, roadmaps and OKRs

The documents that decide direction: vision, strategy, roadmap and objectives. Ranking the work they point at is in `strategy-service-requirements.md`.

The governing idea: each artifact must be able to say no. A vision that justifies any feature, a strategy with no trade-offs, a roadmap that lists everything, and a key result nobody can miss are all the same failure.

### Keep the layers apart

From slowest to fastest changing: company vision, company strategy, product vision, product strategy, roadmap. A mission says why we exist now; a vision describes the future we are creating. The product vision names which slice of the company vision this product makes real.

### A vision that can reject a feature

- **Test:** name a feature the vision rules out. If every feature can be justified by it, it is too vague.
- About the person, simple, three to five years out. No empty superlatives ("best in class", "seamless", "world-leading").
- **Draft with a template, then cut:** For [people] who [need], [product] is a [category] that [benefit]. Unlike [alternative], we [difference]. Then reduce it to the most memorable line.
- **Deliver two versions:** two or three sentences people will repeat, and a full document with the reasoning and assumptions.

### Strategy is a set of choices

- **The linked choices:** what we aim for, where we play (one primary segment, defined by its job and constraints), how we win (one way of being different), the capabilities that needs, the growth motion (product-led or sales-led) and how we will know.
- **Check that the choices reinforce each other.**
- **Being different needs a barrier:** technology, network effects, data, brand or partnerships. Rivals either cannot copy it or will not, because it conflicts with their model.
- **A "won't do" list is required.** No trade-offs means no strategy. Three to five focus areas at most.
- **Hold the vision; review the strategy at least quarterly.** A change of route to the same destination is normal; a change of destination is rare. Write down in advance what evidence would trigger either.
- **Frameworks:** pick one or two that answer the question (Playing to Win, Five Forces, Kano, Three Horizons) with a one-page canvas as the container. Using all of them is a finding.
- **B2B:** name the user, the champion and the buyer separately; each needs a reason. In a multi-product company each product's strategy must ladder up without colliding with its siblings.

### Gate on strategy

No strategy, no roadmap. If goals are missing, help state them first. Where key results exist, work back from each one to the initiatives believed to move it.

### Themes, outcomes and confidence

- **Theme, then initiative, then features as replaceable bets.** A theme is a problem space tied to the strategy.
- **Every item names an outcome, not a deliverable.** Translate a business outcome ("reduce churn") into one a team can own ("week-one use of the core feature in new accounts").
- **Now, Next, Later is the default.** Use dates only for hard external commitments (a contract, a compliance deadline), and keep that view internal.
- **Mark confidence on every item.** Now is committed; Later is a bet. Customer-facing views carry no delivery dates.
- **One source, three views:** internal (dependencies, risks), leadership (themes, milestones, links to strategy), customers (value and direction only).
- **A roadmap is not a backlog.** Story points or bug tickets on it mean the item is in the wrong place.
- **Give technical debt a standing share of capacity,** themed like any other work.
- **Keep a visible Later and Won't list** with the reason for each item, so requests are answered rather than lost.
- **Review quarterly,** and also when a discovery finding, a competitor move or a strategy change lands.
- **Present it as a story:** the challenge now, the outcomes sought, the direction after. Short and visual, with detail on request.

### Key results that are plainly hit or missed

- **OKRs come from the strategy.** Without one, say so and define the priority first.
- **Objectives are qualitative and ambitious,** never a solution. "So what" test: reaching it is strategic progress, not finished activity.
- **Key result format:** metric, baseline, target, unit, date. "Raise 7-day activation from 22% to 30% by 30 June."
- **Key results measure outcomes.** Rewrite "ship X" as the change in behavior X should cause. If the metric does not exist yet, a valid key result is "define and instrument activation by [date]".
- **2 to 4 key results per objective,** and one focus objective per team per cycle by default.
- **Mix leading and lagging measures.** An all-lagging set only reports failure after the fact.
- **Keep stretch and committed goals in separate lists,** so a missed stretch reads as information rather than failure.
- **One named owner per key result.** Teams propose their own key results under objectives from above; check that sibling teams' key results do not conflict.
- **Check in weekly** with a confidence color, review mid-cycle, and run a retro. Scale this down for small teams. Change OKRs mid-cycle only for a real strategy shift, and write down why.
- **KPIs are standing health signals; OKRs push for change.** A KPI dashboard is not an OKR set.

### Evidence

Baselines in key results are measured, not estimated; if no baseline exists, the first key result is to measure it. Market and competitor claims in a strategy carry a source. Confidence on roadmap items reflects evidence, and an item called committed has an owner and capacity behind it.

### Quality checks

| Symptom | What it means | Fix |
| --- | --- | --- |
| The vision justifies any feature | Too vague to guide | Name what it rules out |
| No "won't do" list | No trade-offs, so no strategy | Write one |
| Roadmap items are features with dates | A delivery plan dressed as a roadmap | Themes and outcomes, Now Next Later |
| Customer roadmap shows dates | Promises the team cannot keep | Remove dates; show direction |
| "Launch X" as a key result | An output, not an outcome | The behavior X should change |
| A key result with no baseline | The target was invented | Measure first, or make measuring the key result |
| Five objectives per team | No focus | One focus objective |

### Outputs

**Format:** the requested artifact (vision, strategy, roadmap or OKR set) with its assumptions and open questions listed; for a review, the top three fixes with rewrites, then findings.

**Done when:** each artifact can reject something, every roadmap item names an outcome and a confidence level, and every key result has a baseline, a target, a date and an owner.

## Competitive analysis and go to market

How a product meets its market: who it is for compared with the alternatives, the position it claims, and how it reaches buyers. It carries out the strategy in the section above.

The governing idea: pick one position you can defend with evidence, and reach buyers the way they already buy.

### Start from the decision

"Understand the competition" is not an objective. Name the decision the analysis informs (enter this segment, match this feature, price here) and stop when it is answered.

1. **Frame the market:** its size (total, serviceable and obtainable, each with a source and method), trends, regulation, new entrants and substitutes.
2. **Cover three kinds of competitor:** direct, indirect (the same need met another way, including spreadsheets and doing nothing) and potential.
3. **Tier them:** a deep look at the primary few, a lighter one at the secondary, monitoring for the rest.
4. **Profile each:** features, pricing, experience, the claim it positions on, and patterns in its reviews. A complaint repeated across many reviews is a structural weakness.
5. **Choose one or two frameworks,** not all: a 2 by 2 positioning map for white space, a feature matrix, SWOT, Five Forces or market sizing.
6. **Separate table stakes from differentiators** in every feature matrix. Matching table stakes earns the right to be considered; differentiators earn the choice.
7. **Read a SWOT at its intersections** (a strength meeting an opportunity, a threat hitting a weakness), not as four lists.
8. **End with implications** at three levels: features (match or differ), positioning (which claims are crowded, which can be owned) and strategy (respond now or prepare).

### Claim one position

Claim one of cheapest, best or most specialized. Specialized is the usual choice for an early product. Expand one dimension at a time: geography, customer size or product line. The value proposition uses the same template as the vision statement above, sharpened to the buyer's words.

### Gate on readiness

Before a go-to-market plan: real customers have paid or seriously committed, used the product more than once, and you can say why they bought and what would make them leave. If not, the work is validation, not go-to-market.

### Fit the plan to the stage

- **The five parts must agree:** customers, channels, pricing, timing and partnerships. Change one, recheck the others.
- **Stages run in order:** founder-led selling, then one channel experiment, then optimizing two or three proven channels, then partners and scale. Do the current stage's work only. How many customers marks each stage depends on price and buyer, so do not borrow someone else's thresholds.
- **Master one channel before adding a second,** and add the second as a test before the first saturates.
- **A channel is a cost structure and a relationship.** Work out acquisition cost per channel. Direct sales for high-price or complex products; digital and marketplaces for low-price volume.
- **Match the motion to the buyer:** self-serve or freemium for consumers, product plus light sales for small businesses, consultative selling for enterprise.
- **Check timing before major spend:** seasonality, budget cycles in B2B, first mover against fast follower, and technical and regulatory readiness. Start ahead of the buying season.
- **Buyers do not move in a line.** Follow their signals rather than a calendar of follow-ups, and measure conversion at each stage change.
- **Partnerships amplify a working direct motion;** they do not fix a broken one.
- **Align the teams:** product, marketing, sales and support share one timeline and one owner per task.
- **Set launch metrics and their baselines before launch:** campaign, adoption, market response and qualitative feedback. `metrics-experimentation.md` owns the choice.

### Evidence

Every fact about a competitor, a market size or a price traces to a public source with a date, or is marked unverified. Gather from public sources only: no fake accounts, no scraping against a site's terms. Never state a partnership, customer or certification the person did not give you. Market sizes show their method, because a large number with no method is decoration.

### Quality checks

| Symptom | What it means | Fix |
| --- | --- | --- |
| "Analyze competitors" with no decision named | The analysis will never end | Name the decision first |
| Only direct competitors listed | The real alternative (spreadsheets, doing nothing) is missing | Add indirect and potential |
| A feature matrix with no table-stakes line | Every row looks equally important | Separate table stakes from differentiators |
| Competitor facts with no source | Claims that may be wrong or stale | Source and date each, or mark unverified |
| Several positions claimed at once | No position | Pick one |
| Five channels at launch | None will be mastered | One channel, tested, then a second |
| Launch metrics chosen after launch | No baseline to compare | Set them before |

### Outputs

**Format:** for an analysis, the decision, the market frame, the competitor tiers and profiles, one or two frameworks, implications at three levels and a recommended position, with sources. For a plan, the readiness check, the stage, the five parts, the timeline and the launch metrics.

**Done when:** a named decision is answered, every competitor claim is sourced or marked, one position is chosen, and the plan fits the product's current stage.

## Decision quality

- **Judge the reasoning, not the result.** A good decision can turn out badly and a careless one can get lucky; the second is the dangerous case, because it teaches the wrong habit. Review decisions against what was known at the time.
- **Match the effort to how costly a reversal would be.** A committee on an easily reversed call is waste; a casual one-way decision is a finding.
- **Write confidence as a probability** ("65% that this lifts completion by more than 5%"), not a verdict. For reversible calls, about 70% confidence is enough to act; name the cost of waiting.
- **Add to the decision record:** the confidence, the criteria, the alternatives considered, all written before the outcome, and a booked review date next to "Revisit if".
- **For high-stakes bets, run a pre-mortem:** a year from now this failed badly; what happened? For sunk costs, ask: starting from zero today, would we still choose this?
- **Name the bias and its countermeasure:** confirmation (look for disconfirming data), anchoring, framing (restate the choice as a gain and as a loss), false consensus (use real user data), hindsight (compare with the record written before).
- **Do not prescribe pre-mortems or journals** for everyday reversible calls.
