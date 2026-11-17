# Metrics, instrumentation, experimentation, and causal limits

Operational guide and topic inventory. Procedures and checks are an original synthesis; use the source register for the authority, inspected portion, and limits of specific references.

### Coverage

| Area | Details to consider |
| --- | --- |
| Outcome models | User goal; product goal; task outcome; signal; metric; leading/lagging; guardrail; countermetric; ownership. |
| Metric definitions | Numerator; denominator; eligible population; window; unit; identity; exposure; exclusions; missingness; freshness. |
| Behavioral analysis | Funnels; paths; cohorts; segments; adoption; retention; frequency; completion; errors; effort; support burden. |
| Instrumentation | Events; properties; names; timing; object identity; version; duplicates; missing events; test traffic; consent; masking. |
| Experiment design | Hypothesis; mechanism; variants; assignment unit; exposure; power; duration; stopping; guardrails; contamination; interference. |
| Interpretation | Effect size; uncertainty; sample-ratio mismatch; multiple comparisons; segment exploration; seasonality; novelty; confounding; practical value. |
| Alternative methods | Before/after; interrupted time series; matched cohorts; quasi-experiments; usability evidence; longitudinal research; triangulation. |
| Learning | Baseline; scorecard; outcome review; null result; failed hypothesis; decision; follow-up; knowledge reuse. |

### Procedure

1. Connect the user and product goal to observable signals. Select a small useful measurement set and guardrails.
2. Define each metric precisely and identify what behavior it can and cannot indicate.
3. Specify privacy-aware instrumentation and verify it against actual product actions before diagnosing outcomes.
4. Establish a comparable baseline and inspect population, time, task frequency, and missing data.
5. For experiments, define the hypothesis, assignment/exposure, primary outcome, decision rules, uncertainty needs, and ethical constraints before results.
6. Check implementation, instrumentation, assignment, and contamination; involve statistical expertise where the inference requires it.
7. Interpret practical effect and uncertainty alongside qualitative evidence and guardrails. Avoid causal claims unsupported by the study design.
8. Record ship/revise/stop/investigate decisions and retain context for future reuse.

### Outputs

Goals/signals/metrics tree; tracking specification; baseline; experiment plan; QA record; interpreted results; decision log.

### Quality checks

Metrics have definitions; event quality is checked; samples and cohorts are comparable; guardrails are meaningful; claims match design; uncertainty is visible; user value is not reduced to engagement volume.

### Limits and common failures

HEART is a useful framework rather than a mandatory KPI list. Retention is not inherently desirable for every task. More time spent may mean friction. A statistically distinguishable change may be practically unimportant. An uncontrolled before/after change does not automatically establish causation.

### Sources to consult

- S11: [NN/G: Quantitative methods](https://www.nngroup.com/articles/quantitative-user-research-methods/). Body excerpts inspected.
- S43: [Google: Web Vitals](https://web.dev/articles/vitals). Body excerpts inspected.
- S44: [Microsoft: Online experimentation](https://www.microsoft.com/en-us/research/publication/online-experimentation-at-microsoft/). Publication abstract inspected.
- S45: [Google Research: HEART](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/). Publication abstract inspected.
