# Motion, waiting, sound, and haptic interaction

Operational guide and topic inventory. Procedures and checks are an original synthesis; use the source register for the authority, inspected portion, and limits of specific references.

### Coverage

| Area | Details to consider |
| --- | --- |
| Motion roles | Continuity; causality; hierarchy; orientation; attention; status; direct manipulation; expression. |
| Motion mechanics | Duration; delay; easing; spring; distance; sequencing; choreography; interruption; reversal; cancellation; performance. |
| Waiting | Known/unknown progress; skeleton; spinner; optimistic update; background job; estimated time; queue; retry; timeout. |
| Gesture | Drag; swipe; reorder; resize; pan; zoom; inertia; bounds; snap; precision; accessible alternatives. |
| Audio | Meaning; urgency; volume; context; quiet mode; speech; playback; focus; interruptions; equivalent non-audio information. |
| Haptics | Event meaning; timing; intensity role; device support; user setting; fatigue; redundancy; alternatives. |
| Comfort | Reduced motion; vestibular response; flashing; cognitive distraction; user control; spatial locomotion; physical fatigue. |

### Procedure

1. Define the information or action that feedback must communicate before selecting an effect.
2. Use motion to explain meaningful state or spatial relationships. Keep ornamental motion proportionate to the task.
3. Specify timing, trajectory, sequence, interruption, reversal, and cancellation, including what happens if events occur rapidly.
4. Provide truthful progress and useful recovery for waiting. Distinguish optimistic presentation from confirmed backend completion.
5. Design audio and haptics for actual settings and user preferences, with suitable equivalents.
6. Define reduced-motion and other sensory alternatives as complete experiences.
7. Inspect real runtime performance and comfort on relevant hardware.
8. Record motion roles and tokens with component examples and acceptance checks.

### Outputs

Motion and sensory principles; transition/state specification; progress model; tokens; preference behavior; runtime checks.

### Quality checks

Feedback communicates the actual state; animation can be interrupted appropriately; reduced-motion behavior is usable; important information has alternatives; timing assumptions are contextualized.

### Limits and common failures

A single threshold such as 400ms cannot determine every interaction's quality. Historical response-time guidance is contextual. Fabricated progress percentages and fake success states damage trust. Long or repeated sensory effects can create burden even when individually attractive.

### Sources to consult

- S33: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines). Markdown overview inspected.
- S42: [NN/G: Response-time limits](https://www.nngroup.com/articles/response-times-3-important-limits/). Body excerpts inspected.
- S49: [Apple WWDC23: Principles of spatial design](https://developer.apple.com/videos/play/wwdc2023/10072/). Official summary inspected; playback not reviewed.
- S51: [Apple WWDC23: Spatial input](https://developer.apple.com/videos/play/wwdc2023/10073/). Transcript excerpt inspected; playback not reviewed.
- S54: [W3C: Video captions](https://www.w3.org/WAI/perspective-videos/captions/). Explanation inspected; playback not reviewed.
