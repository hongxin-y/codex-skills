# Deliverable routing

Adapt the detail to the task. The sections below are content expectations, not fixed quotas.

## DESIGN: single page

Describe actor, job, key assumptions, Red Routes, selected layout, component hierarchy, interactions, visual direction, responsive behavior, important states and validation.

## DESIGN: multiple pages — REQUIRED ORDER

### Product overview

Business scenario, actors, objects, key assumptions and Red Route graph.

### Page inventory

List pages with purpose, ownership and entry/exit.

### Page Element Blueprints

For EACH page, present:

| Field | Content |
| --- | --- |
| Page | ID and purpose |
| Actor / job | Who does what |
| Functions | Actions and consequences |
| Content | Data and information shown |
| Red Routes | Which journeys use the page |
| Focal point | What should attract attention and why |
| Element hierarchy | Navigation, data, controls, feedback |
| Operations | Route segment, derived interaction count and P/K/D/C/W/E/M |
| State | Loading, empty, success, failure and permission |
| Handoff | Entry, exit, context preservation |
| Shared rules | Components, tokens, navigation, permissions |

Show these before detailed screen layouts.

### Shared product contract

Navigation, labels, canonical action ownership, data source, status semantics, components, tokens and responsive rules.

### Cross-page matrices

Route coverage, feature ownership, state handoffs and component/visual consistency.

### Detailed screen designs

Layouts, controls, labels, interaction states, responsive transformation and visual direction.

### Review and Repair log

Important issues found, repairs made, impacted routes, regression results and remaining limitations.

## BUILD

Deliver working code and a concise explanation. In multi-page work, create page blueprints and review records during implementation; include a meaningful summary in the final report.

Report changed files, working flows, actual test results and limitations.

## REVIEW

Prioritize findings by affected task and severity. State observed issue, cause, concrete repair and verification method. If asked to fix, implement rather than only describing the change.

## Operation comparison

Use P/K/D/C/W/E/M qualitatively. Include step counts only when the paths are sufficiently specified, and label estimates versus measurements.
