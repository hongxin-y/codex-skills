# Art direction review and repair

Use this lens after the Visual Grammar Contract and after meaningful implementation changes.

## Consistency

- Pages look like one product without forcing identical layouts.
- Typography roles, density modes and alignment rules are coherent.
- Radius, border, shadow, surface and material rules are coherent.
- The same component uses the same visual semantics wherever the task meaning is the same.
- Status colors, labels, icons and feedback are semantically consistent.
- Icons come from one family or documented exceptions.
- Motion has a consistent purpose and reduced-motion behavior.

## Anti-template

- The direction is identifiable beyond a logo and accent color.
- Cards, pills, gradients, blur, glow and illustrations have explicit reasons.
- KPI blocks answer a real monitoring job.
- Real content length and exceptional states influenced the layout.
- The selected trend includes its underlying design logic, not only its surface effect.

## Issue ledger

For each issue record:

| Field | Meaning |
| --- | --- |
| ID | Stable issue identity |
| Category | Usability defect, system inconsistency, art-direction weakness or subjective taste |
| Severity | Blocking, significant, improvement or deferred |
| Scope | Page, route, component or global |
| Evidence | Observable behavior or stated rationale |
| Repair | Concrete change |
| Regression | Pages, routes and states to recheck |
| Status | Open, repaired, verified, blocked or deferred |

Repair architecture, visual grammar and shared tokens before local decoration. Rerun impacted reviews after every consequential change. Do not use a fixed review count as proof of quality.
