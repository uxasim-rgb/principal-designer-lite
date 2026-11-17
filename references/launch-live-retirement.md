# Launch, live operation, support, migration, and retirement

Operational guide and topic inventory. Procedures and checks are an original synthesis; use the source register for the authority, inspected portion, and limits of specific references.

### Coverage

| Area | Details to consider |
| --- | --- |
| Release readiness | Critical journeys; real data; accessibility; localization; analytics; support; known issues; ownership; monitoring; decision criteria. |
| Rollout | Pilot; beta; cohorts; feature flags; exposure; training; communication; old/new coexistence; rollback experience. |
| Live diagnosis | Task failure; drop-off; support; reviews; interviews; field observation; workarounds; exclusion; unexpected use; changed needs. |
| Resilience | Outage; latency; stale data; failed dependency; offline; reconnect; queued work; sync conflicts; background jobs; cancellation. |
| Service support | Self-service; contextual help; diagnostic data; escalation; assisted channels; context handoff; incident communication; recovery. |
| Continuous improvement | Prioritized evidence backlog; experiments; regression checks; experience debt; content updates; system improvements; learning cadence. |
| Migration | Parity and improvement; data mapping; validation; reconciliation; preferences; saved work; links; entitlements; retraining; exceptions. |
| Retirement | Usage evidence; alternatives; notices; timelines; exports; ownership; support; archive/deletion; access changes; final states. |

### Procedure

1. Define who receives the release, what can fail, how outcomes are observed, and who responds.
2. Verify critical task, accessibility, content, data, analytics, support, and operational readiness.
3. Roll out proportionately, communicate meaningful changes, and design the experience of disablement or reversal.
4. Review actual outcomes and feedback across relevant segments, devices, contexts, and support channels.
5. Diagnose causes using multiple evidence sources before selecting changes. Distinguish instrumentation gaps from actual behavior.
6. Maintain resilient operation, current help, regression checks, and a prioritized experience-debt register.
7. Plan migrations around real user work and source-of-truth consistency, including partial outcomes and exceptions.
8. Retire unused capabilities deliberately with appropriate alternatives, exports, communication, and ending states.

### Outputs

Launch/readiness plan; support and observation plan; live issue/outcome review; resilience states; improvement backlog; migration/retirement journey.

### Quality checks

Post-launch owners and actions exist; support can explain the service; failure is recoverable; exclusions are investigated; migrations preserve meaningful work; ending states are designed.

### Limits and common failures

Launch is not evidence of success. Feature adoption does not explain user benefit. Session recordings require appropriate privacy controls and do not directly reveal intent. A redesign can remove valued expert workflows unless they are explicitly studied.

### Sources to consult

- S46: [GOV.UK: Live phase](https://www.gov.uk/service-manual/agile-delivery/how-the-live-phase-works). Body excerpts inspected.
- S43: [Google: Web Vitals](https://web.dev/articles/vitals). Body excerpts inspected.
- S45: [Google Research: HEART](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/). Publication abstract inspected.
