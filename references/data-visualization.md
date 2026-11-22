# Data visualization and dashboards

Charts exist to answer a question faster than a table would. Start from the question, not the chart type.

## Choosing a form

| Question | Use | Avoid |
| --- | --- | --- |
| How does a value change over time? | Line chart (bars for few discrete periods) | Pie, area stacks with many series |
| How do categories compare? | Horizontal bar chart, sorted | 3D bars, pie with many slices |
| What is the part-to-whole? | Stacked bar, or a pie/donut with 2 to 4 slices | Pie with 6+ slices |
| How are values distributed? | Histogram, box plot, dot plot | Average alone |
| How do two measures relate? | Scatter plot | Dual-axis line charts (often misleading) |
| Where is it? | Map, only when location matters | Map for data that is not spatial |
| One key number | Stat tile with comparison (vs last period, vs target) | A gauge |
| Exact values to look up | Table | A chart |

## Defaults

- Bar charts start at zero. Line charts may not, but label the axis clearly.
- Sort categorical bars by value unless the categories have a natural order.
- Direct-label lines and bars where possible instead of a legend.
- Remove chart junk: heavy gridlines, borders, backgrounds, 3D, shadows. Light horizontal gridlines are enough.
- Show units and time range. Round to meaningful precision.
- Use color for meaning: one highlight color against gray for the thing that matters; a sequential palette for ordered values; a diverging palette around a meaningful midpoint; categorical colors for at most about 6 to 8 series.
- Palettes must work for color-vision deficiencies; never rely on red versus green alone.

## Dashboards

- Start with the decisions the viewer makes and the questions they ask, in priority order. Top left gets the most important.
- Few key numbers at top with context (comparison, trend, target), then supporting charts, then detail tables.
- Consistent time range and filters across the dashboard, visible at the top.
- Design the states: loading, no data, partial data, stale data (show last updated), error.
- Avoid the "wall of charts" look; every chart should answer a named question.

## Accessibility

- Text alternative for each chart: a summary of the key insight, plus access to the underlying data (table or download). See WAI complex images guidance in `sources.md` (S72).
- Contrast 3:1 for chart elements against the background and adjacent elements where meaning depends on telling them apart.
- Patterns or labels in addition to color.
- Keyboard and screen-reader access for interactive charts (tooltips reachable by focus).

## Honesty

- No truncated axes that exaggerate change on bar charts.
- No cherry-picked time ranges.
- Show uncertainty when it matters (intervals, sample sizes).
- Label projections and estimates as such.

### Operational or analytical: decide first

- **Operational dashboards** are live and glanceable: everything that needs watching is visible at once and refreshes often.
- **Analytical dashboards** go from overview to detail, refresh on a fixed schedule, and avoid constant movement, which reads as noise.
- **Numbers people compare never sit on separate tabs.** Tabs are for content nobody compares side by side.
- **Role-based views** only when roles really need different information.
- **Labeled sample data** is acceptable on a first-run dashboard when showing beats describing.
