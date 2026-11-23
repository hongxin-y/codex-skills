# Multi-page design orchestration

This is a mandatory pre-layout stage for multi-page products. It begins with a function and relationship model; page count and frontend structure are derived from function relationships and user habits.

## Purpose

Prevent a set of individually attractive but mutually inconsistent pages. Design the product as one task system before designing each screen in detail.

## Stage A: Page inventory

Before the page registry, create a function graph with function IDs, user outcomes, preconditions, states, canonical owners and typed edges (`requires`, `sequence`, `alternative`, `parallel`, `contextual-shortcut`, `shared-state`, `recovery`, `destructive-impact`). Run the [decision-deliberation-protocol](decision-deliberation-protocol.md) before grouping functions into pages. A page that exists only because a feature is listed is not justified.

Infer the minimum justified set of pages from actors, business objects, tasks, permissions, content depth, navigation needs and the function graph.

Create a page registry:

| Field | Meaning |
| --- | --- |
| Page ID | Stable identity and route or entry |
| Role | Why this page exists |
| Actor | Intended user and permissions |
| Main job | User outcome or experience criterion owned by the page |
| Business objects | Entities read or changed |
| Red Routes | Critical journeys using this page |
| Entry / exit | Where the user comes from and goes |
| Data ownership | Read-only summary, canonical edit, derived view |
| Dependencies | Shared state, services and other pages |

Avoid inventing pages to fill a navigation pattern. Combine or separate surfaces based on real task boundaries.

For every page, record the function nodes it owns, the incoming/outgoing relationship edges, the user-habit assumptions that change ordering or persistence, and the evidence for the chosen page boundary.

## Stage B: Page Element Blueprint — REQUIRED FOR EACH PAGE

Produce this design record BEFORE detailed visual layouts:

### Identity and responsibility

- Page ID, title and purpose.
- Intended user and relevant permission context.
- Primary intent and completion or experience criterion; reading and exploration need not end in submission.
- Responsibilities explicitly NOT owned by this page, when duplication risk exists.

### Function and content

- Functional points: actions the user can perform, with trigger, scope, consequence and permission.
- Function nodes owned by this page, relationship edges crossing the page boundary, canonical action owners and the user-habit assumptions behind the grouping.
- Content: business data, explanatory content, status, metadata and decision evidence.
- Element inventory: navigation, headers, filters, search, tables, cards, forms, controls, feedback, overlays and secondary content.
- Element priority: which are always visible, contextual or progressively disclosed.

### Red Routes and focus

- Routes that enter, traverse or finish here.
- Entry state, decision point, success state and exit/handoff.
- Focal point: what the user should notice first, understand next and act on.
- Main action(s) based on current task state; do not enforce a singular CTA.

### Operations and cost

For each relevant route segment, list the interaction sequence:

Entry → inspect → decide → action → feedback → exit.

Record a derived operation count when the proposed path is sufficiently specified. Distinguish pointer actions, typing, decisions, navigation and confirmations. Mark counts as estimated when no usability data exists.

Assess P/K/D/C/W/E/M:
pointing, keyboard/input, decisions, context switching, waiting, error recovery and memory burden.

Do not optimize to a universal click ceiling. A necessary confirmation can be justified by reduced risk.

### Continuity and state

- What query, filters, sort, scroll, selection, drafts and focus persist?
- What data is handed to the next page?
- What happens on return, failure, interruption and permission denial?
- Which components and tokens are shared?
- How does the layout transform on smaller screens?

### Visual role and inheritance

- What is this page's visual role: operational, editorial, immersive, conversion or another justified role?
- What are the primary and secondary focal points and the intended scan path?
- What density mode does the page need, and why does its task justify it?
- Which Visual Grammar Contract rules does the page inherit, and which differences are intentional?
- Which surface model, component variants, imagery, iconography and motion rules apply?
- Which realistic long, short, missing and exceptional content states were used to stress-test the page?
- What visual anti-pattern is most likely here, and how will review detect or repair it?

### Spatial orchestration and dynamic behavior

- Assign every major region the role of Task, Reference, Navigation, Tool, Status, Transient or Breathing Space.
- Record the selected layout skeleton, the rejected alternative and the spatial bottleneck (`main_task_visible_area_ratio`, reference visibility, round trips, scroll burden or occlusion).
- For every major panel, filter, assistant, feedback layer and floating element record `default_visibility` (V0–V4), expand/collapse trigger, auto-collapse prohibition, dismissal rule, pin/remember preference and state restoration.
- Record the responsive transformation sequence (`resize → compact → rail → drawer/sheet → dedicated page`) and the semantics/state preserved at every transition.
- Record the floating occlusion budget, focus return target, keyboard behavior and the fallback container if the current container becomes too small.
- If any field is not applicable, write `N/A — <specific reason>`; a simple page or shared component is not an exemption.

### Generated reference image

- Record the approved reference version used by the page (`V0 → V1 → V2+`), the prompt/change log, review findings and approval basis.
- If pages intentionally diverge, explain which Visual Grammar Contract rules and reference-image decisions are shared versus page-specific.
- Do not enter detailed implementation until the reference image gate and the page's pre-code validation are complete.

### UI Engineering quality

- Record the page's Engineering Blueprint for major regions and shared primitives: layout/sizing, spacing owner, intrinsic growth, overflow/scroll owner, positioning/sticky reference, stacking/Portal/top-layer, overlay collision, focus/hit testing, long content/i18n/RTL, async placeholder/error slots, responsive viewport/safe area, asset metrics, motion risk and validation cases.
- Identify which decisions are design-time contracts and which require browser runtime verification. A page blueprint or screenshot does not prove scroll, hit-testing, focus, layout stability or cross-platform behavior.

## Stage C: Shared product contract

Before detailed screen styling, establish:

- Navigation and route naming conventions.
- Global shell and persistent navigation.
- Canonical owners for business actions and editable data.
- Shared object labels, status vocabulary and error language.
- Component library, semantic color tokens, typography and spacing.
- Authentication, permissions and destructive action conventions.
- Search, filter, sorting and draft preservation rules.
- Responsive behavior and overlay patterns.
- Spatial roles, lifecycle levels, pin/remember policy, state restoration and floating occlusion budget.
- Engineering contracts for shared layout, overlay, table, form, typography, asset, motion and browser/platform behavior.

The shared contract can evolve, but changes must trigger a cross-page review.

## Stage D: Cross-page matrices

### Route coverage matrix

Map each Red Route to its entry, participating pages, completion and recovery. Every important route must have a reachable path to completion.

### Feature ownership matrix

For every significant feature, record its canonical owner and any contextual shortcuts elsewhere. Distinguish true duplication from intentional reuse.

Example:
- Approve order: canonical action in order processing detail.
- Queue row: may expose a shortcut that invokes the same validated operation.
- Analytics page: shows aggregated approval outcomes, not a second independent approval implementation.

### State handoff matrix

For every page transition, record source, destination, state carried, return behavior and failure behavior.

### Visual and component matrix

Check shared headers, buttons, forms, filters, status labels, tables, feedback and navigation for consistent semantics and appearance. Also check typography roles, grid/alignment, density, radius, borders, surfaces, shadows, icons, imagery, motion and component variants against the Visual Grammar Contract.

## Stage E: Detailed layout

Only after the per-page element blueprints and cross-page contract are coherent, choose layouts, component positions, hierarchy and styling for each page.

A page may be visually distinct when its job differs, but should still belong to the same product system.

## Duplicate classification

Not all repetition is harmful.

**Harmful duplication**:
- Two independent editing locations with divergent validation.
- Repeated data collection that the product already knows.
- Multiple pages with the same purpose but unclear ownership.
- Inconsistent status labels or action semantics.
- Repeated navigation that adds no task value.

**Intentional repetition**:
- Global navigation and account controls.
- Contextual summary of an object on several pages.
- A sticky action that mirrors a distant action on a long page.
- An accessible shortcut to a canonical operation.

Intentional repetition must share semantics, permissions, data and feedback.

## Output expectation

In DESIGN mode, present the per-page element records before detailed screen proposals. In BUILD mode, create a concise internal design record, implement, and report the important page boundaries and continuity decisions.

Do not treat a page registry alone as completed design. Run [review-repair-protocol](review-repair-protocol.md) before finalizing.
