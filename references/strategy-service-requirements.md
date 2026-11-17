# Product strategy, service design, and requirements

Operational guide and topic inventory. Procedures and checks are an original synthesis; use the source register for the authority, inspected portion, and limits of specific references.

### Coverage

| Area | Details to consider |
| --- | --- |
| Product direction | Vision; positioning; audiences; buyers/users/operators; value proposition; business and funding model; incentives; unit meaning; product outcomes. |
| Problem discovery | Current-state audit; competitive alternatives; workarounds; jobs to be done; root-cause hypotheses; needs; constraints; assumptions; opportunity trees. |
| Service design | Ecosystem; actors; journeys; touchpoints; channels; frontstage/backstage; blueprints; staff tools; queues; capacity; recovery; assisted service. |
| Systems thinking | Feedback loops; time delays; local versus whole-system effects; dependencies; incentive conflicts; unintended consequences; shared resources. |
| Requirements | Actors; triggers; preconditions; functional rules; quality requirements; permissions; states; calculations; regional variation; exclusions; acceptance criteria. |
| Business analysis | Entities; relationships; field dictionary; decision tables; object lifecycles; eligibility; precedence; effective dates; traceability; auditability. |
| Scope and prioritization | Risk reduction; MVP; sequencing; evidence confidence; effort; feasibility; viability; reach; exclusions; maintenance cost. |
| Collaboration | Stakeholder map; decision rights; workshop; critique; engineering feasibility; operational review; rationale; unresolved decisions. |

### Procedure

1. State the affected users, actual task, problem evidence, intended outcome, and decision owner.
2. Map the surrounding service and actors so an interface change does not shift unrecognized work or risk into another channel.
3. Describe domain objects and their lifecycles. Record field meanings and distinguish absent, unknown, not applicable, zero, and unavailable.
4. Translate requirements into testable normal, alternate, permission, exceptional, and recovery paths. Surface contradictions instead of silently inventing rules.
5. Use decision tables for eligibility or calculations when prose becomes ambiguous. Verify authoritative business definitions with the appropriate owner.
6. Explore materially different options, assess evidence and feasibility, and sequence learning before expensive commitment.
7. Trace important requirements to flows, screens, content, tests, metrics, and operational responsibilities.
8. Document the chosen tradeoff and what would cause the team to revisit it.

### Outputs

Problem and outcome brief; ecosystem or service blueprint; entity/field glossary; rule and permission matrices; scoped flow; traceability; acceptance criteria.

### Quality checks

Buyer and user needs are distinguished; staff and assisted channels are covered; system dependencies are visible; calculated values have verified semantics; assumptions have owners; exclusions and scope boundaries are explicit.

### Limits and common failures

Frameworks such as Double Diamond, Lean UX, design thinking, Jobs to Be Done, opportunity trees, RICE, Kano, and MoSCoW are optional working structures. Select by the decision and evidence rather than applying every framework. The ISO public abstract supports lifecycle scope; it does not provide access to all normative clauses or domain safety requirements.

### Sources to consult

- S06: [GOV.UK: Plan user research](https://www.gov.uk/service-manual/user-research/plan-user-research-for-your-service). Body excerpts inspected.
- S38: [Ben Shneiderman: Eight Golden Rules](https://www.cs.umd.edu/users/ben/goldenrules.html). Body excerpts inspected.
- S46: [GOV.UK: Live phase](https://www.gov.uk/service-manual/agile-delivery/how-the-live-phase-works). Body excerpts inspected.
- S62: [ISO 9241-210:2019](https://www.iso.org/standard/77520.html). Public abstract inspected; full standard not accessed.
