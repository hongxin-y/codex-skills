# Deliverable routing

Adapt the detail to the task. The sections below are content expectations, not fixed quotas.

## Required execution record

Before the deliverable, include a compact ledger with one row for every applicable step:

| Step | Reference read | Decision applied | Artifact produced | Status |
| --- | --- | --- | --- | --- |
| Scope and facts |  |  |  | DONE / N/A with reason / BLOCKED |
| Task model |  |  |  | DONE / N/A with reason / BLOCKED |
| Route model |  |  |  | DONE / N/A with reason / BLOCKED |
| Page scope and blueprint |  |  |  | DONE / N/A with reason / BLOCKED |
| Layout and interaction |  |  |  | DONE / N/A with reason / BLOCKED |
| Cost and continuity |  |  |  | DONE / N/A with reason / BLOCKED |
| Visual system |  |  |  | DONE / N/A with reason / BLOCKED |
| Review and repair |  |  |  | DONE / N/A with reason / BLOCKED |
| Delivery |  |  |  | DONE / N/A with reason / BLOCKED |

Do not fill the reference or artifact columns with generic confirmations. Name the file or rule read and summarize the concrete decision it changed. If a step is not applicable, explain why it cannot affect the requested result.

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
