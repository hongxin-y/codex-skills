# Deliverable routing

Adapt the detail to the task. The sections below are content expectations, not fixed quotas.

Use the page's dominant intent to explain success: comprehension and orientation, informed choice, correct operation, creative control or discovery. Include scenario-specific detail only when relevant; a template field does not require adding a role, approval, transaction or publication lifecycle to the product.

## Required execution record

Before the deliverable, include a compact ledger with one row for every applicable step:

| Step | Reference read | Decision applied | Artifact produced | Status |
| --- | --- | --- | --- | --- |
| Scope and facts |  |  |  | DONE / N/A with reason / BLOCKED |
| Functional scope and relationship model |  |  |  | DONE / N/A with reason / BLOCKED |
| Task model |  |  |  | DONE / N/A with reason / BLOCKED |
| Route model |  |  |  | DONE / N/A with reason / BLOCKED |
| Page scope and blueprint |  |  |  | DONE / N/A with reason / BLOCKED |
| Art direction and reference image gate |  |  |  | DONE / N/A with reason / BLOCKED |
| Spatial orchestration |  |  |  | DONE / N/A with reason / BLOCKED |
| Layout and interaction |  |  |  | DONE / N/A with reason / BLOCKED |
| Cost and continuity |  |  |  | DONE / N/A with reason / BLOCKED |
| Visual system |  |  |  | DONE / N/A with reason / BLOCKED |
| UI engineering quality |  |  |  | DONE / N/A with reason / BLOCKED |
| Review and repair |  |  |  | DONE / N/A with reason / BLOCKED |
| Delivery |  |  |  | DONE / N/A with reason / BLOCKED |

Do not fill the reference or artifact columns with generic confirmations. Name the file or rule read and summarize the concrete decision it changed. If a step is not applicable, explain why it cannot affect the requested result.

## DESIGN: single page

Describe intended user, intent, success or experience criterion, function inventory and relationship graph, key assumptions, Red Routes, the Visual Context Profile, bounded user-perception hypotheses, selected or inherited Visual Grammar Contract, generated reference image versions and approval, space roles, layout skeleton, lifecycle/persistence decisions, selected layout, component hierarchy, interactions, responsive transformation, UI Engineering Blueprint summary, realistic-content stress cases, important states and validation.

## DESIGN: multiple pages — REQUIRED ORDER

### Product overview

Product scenario, intended users, intents, success or experience criteria, function inventory, typed relationship graph, user-habit hypotheses, relevant objects, key assumptions and Red Route graph.

### Function-to-frontend map

Show how the function graph becomes the frontend structure before detailed screens:

| Surface | Function nodes owned | Relationship edges crossing the boundary | Persistent / on-demand regions | State and context carried | Canonical action owner |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

Include page or route nodes, navigation levels, major component groups and the state/data handoffs. A Mermaid graph is appropriate when it improves traceability. Every surface and major component must point back to a function node. Every important function must have an entry, result, recovery and continuation path.

### Page inventory

List pages with purpose, ownership and entry/exit.

### Page Element Blueprints

For EACH page, present:

| Field | Content |
| --- | --- |
| Page | ID and purpose |
| User / intent | Who wants to do what, with which success or experience criterion |
| Functions | Actions and consequences |
| Function relationships | Function nodes owned by this page, incoming/outgoing edges, shared state, canonical owner and user-habit rationale |
| Content | Data and information shown |
| Red Routes | Which journeys use the page |
| Focal point | What should attract attention and why |
| Element hierarchy | Navigation, data, controls, feedback |
| Spatial roles | Task, reference, navigation, tool, status, transient and breathing-space assignments |
| Layout skeleton | Selected skeleton, rejected alternative and spatial bottleneck |
| Lifecycle | V0–V4 for each major region, expand/collapse trigger and dismissal rule |
| Persistence | Pin/remember preference, state restored and auto-collapse prohibitions |
| Responsive transformation | Resize → compact → rail → drawer/sheet → page decisions and preserved semantics |
| Occlusion budget | Floating elements, covered area, focus/keyboard behavior and escalation path |
| Engineering blueprint | Layout/sizing, spacing owner, overflow/scroll, positioning/layering, overlay collision, focus/hit testing, content/async, responsive/assets, motion and validation cases |
| Component decision fields | `component_role`, `information_priority`, `task_frequency`, `task_criticality`, `context_dependency`, `reference_persistence`, `default_visibility`, `expandability`, `auto_collapse_policy`, `dismissal_policy`, `user_pin_capability`, `remember_user_preference`, `responsive_transformation`, `occlusion_budget`, `interaction_mode`, `keyboard_behavior`, `focus_return_target`, `screen_reader_state`, `state_restore_policy`, `shared_across_pages`, `canonical_action_owner` |
| Operations | Route segment, derived interaction count and P/K/D/C/W/E/M |
| State | Relevant loading, empty, result, recovery and permission states |
| Handoff | Entry, exit, context preservation |
| Visual role | Operational, editorial, immersive, conversion or another justified role |
| Perception hypothesis | User goal, observable signal, visual response, counter-risk and verification method |
| Focal composition | Primary/secondary focus and scan path |
| Density mode | Sparse, moderate, dense or another justified mode |
| Art-direction inheritance | Global rules inherited and page-level differences |
| Surface model | Flat, border-led, layered, elevated or translucent |
| Component expression | Important component variants and their grammar rationale |
| Content realism | Long, short, missing and exceptional content used for review |
| Visual anti-pattern risk | Template risks and planned repair |
| Shared rules | Components, tokens, navigation, permissions |

Show these before detailed screen layouts.

### Shared product contract

Navigation, labels, canonical action ownership, data source, status semantics, components, tokens and responsive rules.

### Cross-page matrices

Route coverage, feature ownership, state handoffs and component/visual consistency.

### Detailed screen designs

Layouts, controls, labels, interaction states, responsive transformation and visual direction.

The Visual Context Profile and Visual Grammar Contract must already be recorded before this section. Derive component variants from the contract rather than selecting them independently.

### UI Engineering Quality

For each major region or shared primitive, summarize the Engineering Blueprint: spacing owner, intrinsic sizing and content-growth rule, overflow and scroll owner, containing block and sticky reference, stacking/portal/top-layer policy, collision boundary, focus/hit-testing behavior, long-content/i18n/RTL policy, async size stability, responsive/safe-area strategy, asset metrics and validation cases. For BUILD, include browser runtime audit, screenshot regression, accessibility automation and manual keyboard/touch/overlay checks with verified or unverified status.

### Generated reference image record

Before detailed screen implementation, include:

| Field | Content |
| --- | --- |
| Capability | Image Generation capability used, or `BLOCKED` with reason |
| Version chain | `V0` concept → `V1` structure → `V2` realism → optional `V3+` polish |
| Prompt/change log | Prompt, input reference, changed decision group and result for each version |
| Review | Visual grammar, space, content realism, responsive and anti-AI findings per version |
| Approval | Approved version, approval_by (`user` or `agent_after_review`), approval basis and open risks |
| Implementation comparison | Actual screenshot/behavior comparison after BUILD and repairs |

`V0`–`V2` and the approval record are required for visual DESIGN/BUILD work. If the task is genuinely non-visual, record the specific N/A reason.

### Review and Repair log

Important issues found, repairs made, impacted routes, regression results and remaining limitations.

## BUILD

Deliver working code and a concise explanation. In multi-page work, create page blueprints and review records during implementation; include a meaningful summary in the final report.

Report changed files, working flows, actual test results and limitations.

## REVIEW

Prioritize findings by affected task and severity. State observed issue, cause, concrete repair and verification method. If asked to fix, implement rather than only describing the change.

## Operation comparison

Use P/K/D/C/W/E/M qualitatively. Include step counts only when the paths are sufficiently specified, and label estimates versus measurements.
