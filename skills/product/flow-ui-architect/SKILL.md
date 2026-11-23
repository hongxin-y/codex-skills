---
name: flow-ui-architect
description: "Design, review and implement UI/UX for websites, apps and multi-page products with function-first modeling, auditable multi-step decisions and a mandatory generated-reference-image iteration gate before implementation. Use for feature and interaction design, information architecture, visual systems, frontend UI changes and usability reviews. Choose patterns by user intent and preserve existing behavior outside the requested scope."
---

# Flow UI Architect

Turn a brief product scenario into an appropriate, usable, attractive and implementable interface. Support the intended user experience and complete user journeys. Reading, comparing, transacting, creating and exploring can require different definitions of success.

## Operating contract

- Work as a product designer, interaction designer, visual designer and frontend engineer when appropriate.
- A one-sentence scenario is enough to begin. Infer ordinary missing details and label consequential assumptions. Ask only when an unknown materially affects safety, permissions, business correctness or irreversible decisions.
- Separate USER facts, REPO facts, EVIDENCE and ASSUMPTIONS. Never present guesses as verified requirements.
- Identify the user intent and success criterion before choosing features, pages or controls. A request for a button, chart or page is a proposed solution; establish the problem it serves without expanding the user's scope.
- Choose page count, Red Routes, action hierarchy, navigation depth, review cycles and visual complexity based on the task. Do not enforce arbitrary numerical quotas.
- Preserve useful existing project conventions and components.
- Respect the requested change boundary. A visual-only change preserves interaction and data behavior; reusing an existing design does not authorize importing its business rules.
- Make important decisions explicit, but adapt explanation length to task complexity.
- Keep real accessibility standards and technical constraints.
- Treat this file and the routed reference files as an execution protocol. Do not jump from a brief to a polished screen or code without completing the required intermediate records.
- For new visual design or visual changes, use the Image Generation capability to create a visual reference before detailed implementation, iterate it through the required review rounds, and do not write UI code until the reference is approved and all pre-code design and validation steps are complete.
- For every required step, read the named reference before making the step's decision, apply the relevant rules, and record the concrete artifact produced. A reference may be marked `N/A` only with a reason tied to the task; never claim to have followed unread guidance.

## Select the operating mode

DESIGN: Produce concrete screen and interaction designs. For a multi-page request, show the Page Element Blueprint for each page before detailed layout decisions.

BUILD: Inspect the existing repository and implement the requested UI. For a multi-page build, first create a concise page blueprint and shared contract, then proceed without requiring approval unless a consequential decision is blocked. Do not replace working code with a design essay.

REVIEW: Diagnose existing designs or code, identify task friction and inconsistencies, and propose repairs. Implement repairs only when requested. Distinguish observed defects from hypotheses; a discussion-only review does not authorize edits.

## Product intent and applicability

Use the page modes in [task-modeling](references/task-modeling.md) to choose the evaluation criteria:

| Dominant intent | Prioritize | Avoid assuming |
| --- | --- | --- |
| Find or understand | Orientation, comprehension, evidence and return position | Every page needs a submission or next-step button |
| Compare or decide | Relevant differences, clear terms and informed choice | Faster conversion always benefits the user |
| Operate or transact | Correct outcome, efficient action and recovery | Fewer clicks alone mean better usability |
| Create or express | Flexible input, control, iteration and recoverability | All content should be constrained to predefined choices |
| Explore or engage | Discovery, relevance and user-directed navigation | A single linear route or terminal completion is required |

A product may combine these intents. Record the dominant intent per relevant surface and explain any tradeoff; do not turn every product into an operational workbench.

Read conditional guidance only when the feature needs it:

- Inputs, settings or collapsible content: [input-and-disclosure](references/input-and-disclosure.md).
- Counts, charts, progress, results, source or freshness claims: [information-integrity](references/information-integrity.md).
- Collaboration, editing, long-running work, bulk actions or consequential transactions: the applicable branch of [scenario-extensions](references/scenario-extensions.md). Do not create roles, approvals, versions or audit processes merely to fill a branch.

These rules refine the existing steps; they do not add another execution gate.

## Mandatory execution protocol

Run this protocol for DESIGN, BUILD and REVIEW. Keep a visible step ledger in the working response or working notes:

| Step | Required artifact | Required references | Status |
| --- | --- | --- | --- |
| 0. Scope and facts | USER / REPO / EVIDENCE / ASSUMPTIONS split | `task-modeling.md` | DONE, N/A with reason, or BLOCKED |
| 1. Functional scope and relationship model | Function inventory, relationship graph, user-habit hypotheses, frontend information map and canonical owners | `functional-scope-and-relationships.md`, `task-modeling.md` | DONE, N/A with reason, or BLOCKED |
| 2. Task model | User intent, success criterion, actors, objects, relevant permissions and constraints | `task-modeling.md` | DONE, N/A with reason, or BLOCKED |
| 3. Route model | Intent-appropriate journey, relevant feedback, recovery and continuation; Red Route map | `decision-rules.md` | DONE, N/A with reason, or BLOCKED |
| 4. Page scope and blueprint | Page inventory, or a compact Page Element Blueprint for a single page | `multi-page-design.md`, `design-output-template.md` | DONE, N/A with reason, or BLOCKED |
| 5. Art direction and reference image gate | Visual Context Profile, user-perception hypotheses, candidate directions or inherited contract, selected Visual Grammar Contract, generated reference versions `V0 → V1 → V2+`, review log and approval record | `visual-direction-selection.md`, `user-perception-and-visual-decisions.md`, `image-reference-iteration.md`, `art-direction-catalog.md`, `design-system-profiles.md` when a system foundation exists | DONE, N/A with reason, or BLOCKED |
| 6. Spatial orchestration | Space roles, layout skeleton, lifecycle, visibility, persistence, responsive transformation and occlusion budget | `spatial-orchestration.md`, `component-morphology.md`, `visibility-persistence.md`, `responsive-transformation.md`, `floating-ui-and-occlusion.md`; `workspace-layouts.md` when applicable | DONE, N/A with reason, or BLOCKED |
| 7. Layout and interaction | Compared layout choice, component ownership and interaction states | `layout-patterns.md`, `interaction-patterns.md`, `component-style-grammar.md` | DONE, N/A with reason, or BLOCKED |
| 8. Cost and continuity | P/K/D/C/W/E/M analysis, preserved context and handoffs | `operation-cost.md`, `flow-continuity.md` | DONE, N/A with reason, or BLOCKED |
| 9. Visual system | Hierarchy, density, tokens, responsive transformations, component expression and accessibility decisions | `color-and-tokens.md`, `color-strategy-catalog.md`, `typography-and-grid.md`, `surface-shape-depth.md`, `imagery-iconography-motion.md`, `visual-quality.md` | DONE, N/A with reason, or BLOCKED |
| 10. UI engineering quality | UI Engineering Blueprint covering geometry, spacing ownership, intrinsic sizing, overflow, scroll, layering, hit testing, focus, async stability and platform risk | `ui-engineering-blueprint.md`, `ui-engineering-foundations.md`, `overlay-and-scroll-engineering.md`, `component-engineering-checklists.md`; `responsive-runtime.md`, `visual-stability-performance.md`, `browser-platform-matrix.md` when applicable | DONE, N/A with reason, or BLOCKED |
| 11. Review and repair | Findings, repairs, impacted routes, engineering runtime behavior, spatial/dynamic behavior, visual consistency and regression checks | `review-repair-protocol.md`, `art-direction-review.md`, `anti-ai-template-review.md`, `perceived-quality.md`, `ui-debug-playbook.md`, `validation-checklist.md` | DONE, N/A with reason, or BLOCKED |
| 12. Delivery | Requested design, implementation or review result with limitations | `implementation-playbook.md` when building; `design-output-template.md` otherwise | DONE, N/A with reason, or BLOCKED |

Rules for the ledger:

- Do not mark a step DONE with a generic sentence. Record the decision, the artifact, and the reference rule that changed the decision.
- Before marking any step DONE, apply the multi-step [decision-deliberation-protocol](references/decision-deliberation-protocol.md): state the decision, gather evidence, compare candidates, simulate representative user habits and edge cases, inspect downstream consequences and record a falsifying counterexample. A one-line preference is not a completed decision.
- Do not start detailed screen layout or UI code while Steps 0–6 and the Step 5 Reference Approval Gate are incomplete. BUILD must inspect the repository before implementation. REVIEW must record observed evidence before proposing repairs. For every applicable pre-code step, `BLOCKED` prevents UI implementation until the blocker is resolved. `N/A` requires a task-specific reason. BUILD must not declare implementation complete until engineering and review steps are rerun against actual browser behavior.
- If a step does not apply, write `N/A — <specific reason>` and continue only after checking that later steps do not depend on it. If it is blocked, state the blocker and either ask the smallest necessary question or continue with a labeled assumption when safe.
- Every major region, panel, filter, floating element, assistant, feedback layer and responsive variant must receive a spatial role, visibility lifecycle, persistence rule, container choice, occlusion budget and state-restore decision. “Simple page”, “existing component” and “time pressure” are not valid reasons to omit a decision point.
- Every visual design or visual change must have an auditable image reference chain with at least `V0`, `V1` and `V2` (or a documented `BLOCKED` reason). A generated image cannot be replaced by a screenshot, placeholder, text-only moodboard or code preview.
- Every page, route, navigation item and major component must trace back to one or more function nodes and relationship edges. Do not draw frontend screens by counting features; derive grouping and hierarchy from function dependency, shared state, user frequency, interruption/recovery habits and decision context.
- After implementation or repair, rerun the affected steps against actual behavior. A design note, blueprint or paper review does not prove the UI works.
- The final response must include the completed ledger, assumptions, unresolved limitations, changed files when applicable, and actual checks performed.

## Core workflow

### Determine functions and their relationships first

Before task modeling, **MUST READ and apply** [functional-scope-and-relationships](references/functional-scope-and-relationships.md) and [decision-deliberation-protocol](references/decision-deliberation-protocol.md). Inventory the actual user-facing function points, their inputs/outputs, preconditions, states, permissions, frequency, criticality, canonical owners and recovery. Draw the relationship graph with `requires`, `sequence`, `alternative`, `parallel`, `contextual-shortcut`, `shared-state`, `recovery` and `destructive-impact` edges. Record user-habit hypotheses for first use, expert repetition, interruption/return, batch work, comparison, device and risk contexts.

Only after this graph is coherent may you derive the frontend map: pages/routes, navigation levels, persistent versus on-demand regions, page-to-page state flow, component ownership and responsive transformations. Every page and major component must link back to function nodes; every function must have an entry, feedback, recovery and continuation path. Run the six decision checks before marking Step 1 DONE.

### Understand the user intent and task

Infer the user intent, success criterion, actors, triggers, objects, relevant permissions, frequency, urgency, error costs, device context and any actual collaboration needs. **MUST READ and apply** [task-modeling](references/task-modeling.md) and [decision-deliberation-protocol](references/decision-deliberation-protocol.md), then record the task model in Step 2. Apply scenario extensions only when their trigger exists in the product.

### Identify task routes

Model the relevant entry, locate, inspect, decide, act, feedback, recovery and continuation segments. A reading or exploration journey need not include a mutation, handoff or final submission. Select Red Routes according to user value, frequency, impact, risk and dependencies. There is no prescribed route count. **MUST READ and apply** [decision-rules](references/decision-rules.md) and [decision-deliberation-protocol](references/decision-deliberation-protocol.md), then record the route map in Step 3. Check each route against the function relationship graph and at least one interruption or recovery habit.

### Determine page scope

For a single-page task, select a suitable layout directly, but still create a compact Page Element Blueprint before detailed styling or code. Trace every element to the function graph before selecting the layout.

For multiple pages or connected product surfaces, the MULTI-PAGE DESIGN GATE below is mandatory before detailed UI or implementation. **MUST READ and apply** [multi-page-design](references/multi-page-design.md), [design-output-template](references/design-output-template.md) and [decision-deliberation-protocol](references/decision-deliberation-protocol.md), then record page boundaries, function ownership, relationship edges, user-habit rationale and the Page Element Blueprint in Step 4.

### Establish visual direction before styling

Run the Art Direction Gate after the Page Element Blueprint and before detailed layout styling or code. **MUST READ and apply** [visual-direction-selection](references/visual-direction-selection.md), [user-perception-and-visual-decisions](references/user-perception-and-visual-decisions.md) and [decision-deliberation-protocol](references/decision-deliberation-protocol.md). Use [art-direction-catalog](references/art-direction-catalog.md) when the repository or brand does not already establish a direction, and use [design-system-profiles](references/design-system-profiles.md) to separate interaction-system foundations from visual language. Record the Visual Context Profile, psychological hypotheses with observable signals and counter-risks, candidate comparison or inherited direction, selected Visual Grammar Contract and rejected alternatives in Step 5.

Do not treat a palette, gradient, glass effect, font choice or component variant as an art direction. The direction must explain typography, grid, density, palette strategy, shape, surface/depth, imagery, iconography, motion and component expression as one system.

### Generate and iterate the visual reference before continuing

Immediately after the Visual Grammar Contract, **MUST READ and apply** [image-reference-iteration](references/image-reference-iteration.md) and use the Image Generation capability to generate `V0`. Then generate at least `V1` and `V2` through targeted iterations. Inspect each result, record the prompt and changed decision group, run the reference review checks, preserve rejected versions and write the Reference Approval Gate record. If image generation, image inspection or approval is unavailable, mark the gate `BLOCKED`; do not substitute HTML, code, screenshot or verbal approval and do not begin implementation. The reference approval closes Step 5 only after the decision-deliberation checks have been recorded.

The approved image is the visual source of truth for subsequent spatial, layout, visual-system and engineering decisions. It does not replace those decisions: complete every later step, pre-code validation and review before BUILD code begins. After implementation, compare real screenshots and behavior with the approved reference and repair deviations.

### Orchestrate space and dynamic behavior before detailed layout

Before choosing exact columns, cards, panels or floating controls, **MUST READ and apply** [spatial-orchestration](references/spatial-orchestration.md), [component-morphology](references/component-morphology.md), [visibility-persistence](references/visibility-persistence.md), [responsive-transformation](references/responsive-transformation.md), [floating-ui-and-occlusion](references/floating-ui-and-occlusion.md) and [decision-deliberation-protocol](references/decision-deliberation-protocol.md). Read [workspace-layouts](references/workspace-layouts.md) for workbenches, editors, monitoring, maps, complex forms or other multi-region surfaces.

Record the page's space roles, selected layout skeleton, rejected alternative, spatial bottleneck, lifecycle level (V0–V4) for every major region, collapse/expand trigger, auto-collapse prohibition, pin/remember behavior, responsive transformation, state restoration and floating occlusion budget. Simulate first use, repeated expert use, interruption/return and narrow-screen use before choosing persistence. If a field is not applicable, write `N/A — <specific reason>`; never skip it.

Preserve task-critical state, current focus, unsaved input, active errors, repeated comparison and user-pinned preferences during collapse or transformation. Use `resize → compact → rail → drawer/sheet → dedicated page` before hiding content. When a container is too small, escalate `Tooltip → Popover → Drawer/Panel → Dedicated Page` according to content complexity; do not solve every pressure case with a modal.

### Choose layout and interaction patterns

Select workbench, queue, master-detail, search/results, dashboard, form, wizard, editor, timeline, feed, comparison or a justified hybrid. Compare alternatives. Use inline actions, drawers, modals, tabs, sticky bars, FABs and other controls only when they fit the job. **MUST READ and apply** [layout-patterns](references/layout-patterns.md), [interaction-patterns](references/interaction-patterns.md), [component-style-grammar](references/component-style-grammar.md) and [decision-deliberation-protocol](references/decision-deliberation-protocol.md), then record the chosen pattern, component variants and rejected alternatives in Step 7. Derive variants from the Visual Grammar Contract and function relationships; do not select them independently because they are fashionable.

### Optimize cost and continuity

Compare P/K/D/C/W/E/M: pointing, input, decisions, context switches, waiting, error recovery and memory burden. Preserve search, filters, sort, selection, scroll, drafts and next-task context where relevant. **MUST READ and apply** [operation-cost](references/operation-cost.md), [flow-continuity](references/flow-continuity.md) and [decision-deliberation-protocol](references/decision-deliberation-protocol.md), then record the cost and handoff decisions in Step 8.

### Build the visual system

Define hierarchy, density, typography, spacing, semantic color tokens, surfaces and responsive transformations. **MUST READ and apply** [color-and-tokens](references/color-and-tokens.md), [color-strategy-catalog](references/color-strategy-catalog.md), [typography-and-grid](references/typography-and-grid.md), [surface-shape-depth](references/surface-shape-depth.md), [imagery-iconography-motion](references/imagery-iconography-motion.md), [visual-quality](references/visual-quality.md) and [decision-deliberation-protocol](references/decision-deliberation-protocol.md), then record the visual and accessibility decisions in Step 9. Run the Real-content Stress Test before marking the step complete.

### Establish the UI Engineering Blueprint

Before implementation or final design handoff, **MUST READ and apply** [ui-engineering-blueprint](references/ui-engineering-blueprint.md), [ui-engineering-foundations](references/ui-engineering-foundations.md), [overlay-and-scroll-engineering](references/overlay-and-scroll-engineering.md), [component-engineering-checklists](references/component-engineering-checklists.md) and [decision-deliberation-protocol](references/decision-deliberation-protocol.md). Read [responsive-runtime](references/responsive-runtime.md), [visual-stability-performance](references/visual-stability-performance.md), [browser-platform-matrix](references/browser-platform-matrix.md) and [ui-debug-playbook](references/ui-debug-playbook.md) when the product uses responsive, async, overlay, virtualized, high-density or platform-sensitive UI.

For every major region and shared interactive primitive, record the Engineering Blueprint: layout contract, spacing owner, intrinsic sizing, content-growth and overflow policy, scroll owner, containing block and sticky reference, stacking/portal/top-layer policy, collision boundary, focus and hit-testing behavior, long-content/i18n/RTL behavior, async placeholder and error slot, responsive/viewport/safe-area strategy, asset metrics, motion/compositing risk and validation cases. Simulate how the chosen contract behaves when the related function is repeated, interrupted, denied, slow or supplied extreme content. If a field does not apply, write `N/A — <specific reason>`. Record this artifact in Step 10 only after the deliberation protocol has challenged the leading design.

Do not infer production readiness from a plausible screenshot or from “the component renders”. Validate the five layers separately: layout, paint, stacking/compositing, hit testing and accessibility tree. For BUILD, run a browser runtime audit after implementation: overflow, active scroll containers, overlay clipping/placement, focus visibility/return, pointer target, console errors and layout stability. Use screenshot regression for geometry and visual surfaces, and manual keyboard/touch/overlay checks for behavior that automation cannot prove.

Engineering invariants: parent layouts own sibling spacing; `min-width:0` / `min-height:0` / `minmax(0,1fr)` are justified by content contracts; arbitrary huge z-index values are not a layering strategy; every overlay has collision, scroll, focus and safe-area rules; images/fonts/skeletons/errors reserve stable space when appropriate; `transition: all`, global `will-change`, `outline:none` without replacement and unbounded `100vh` are review risks, not defaults.

### Deliver and validate

For DESIGN, provide an actionable blueprint or prototype. For BUILD, implement and run available checks. For REVIEW, prioritize findings and repairs. **MUST READ and apply** [design-output-template](references/design-output-template.md), [implementation-playbook](references/implementation-playbook.md) when building, [review-repair-protocol](references/review-repair-protocol.md), [art-direction-review](references/art-direction-review.md), [anti-ai-template-review](references/anti-ai-template-review.md), [perceived-quality](references/perceived-quality.md), [ui-debug-playbook](references/ui-debug-playbook.md), [decision-deliberation-protocol](references/decision-deliberation-protocol.md) and [validation-checklist](references/validation-checklist.md) before delivery. Review Task fit and Accessibility first, then Semantic fit, Hierarchy, Authenticity, Coherence, Craft, Restraint and Distinctiveness; do not compress this into an unsupported total score.

For BUILD, run a **pre-code Review/Repair** against the approved reference, page blueprints, spatial decisions, visual system and Engineering Blueprint. Resolve blocking issues before writing code. After implementation, rerun the same review against actual browser behavior, screenshots and input modes; a pre-code pass never substitutes for the post-code pass.

## Mandatory MULTI-PAGE DESIGN GATE

Apply whenever the request includes multiple connected pages, routes or substantial screens.

### Gate A — Page inventory and route graph

Identify every justified page, its role, entry/exit points and Red Route participation. Avoid adding pages merely because an app convention suggests them. Create a shared product contract covering navigation, naming, permissions, status semantics, data ownership, component reuse and visual tokens.

### Gate B — Per-page element design BEFORE detailed screens

Create a Page Element Blueprint for EACH page, including:
- Page ID, purpose, intended user and completion or experience criterion.
- Functional points and actions, including action ownership and consequences.
- Required content, data objects, source and edit permissions.
- Red Routes entering, passing through or completing on the page.
- Focal point: what the user should notice, understand and do next.
- Element inventory and hierarchy: navigation, data, controls, feedback and states.
- Operation path and operation count when derivable, with P/K/D/C/W/E/M analysis; distinguish estimates from measurements.
- Entry, exit, handoff, preserved context and recovery.
- Shared versus page-specific components, responsive behavior and assumptions.

Do not skip this step and jump straight to independent page mockups. In DESIGN mode, present these blueprints as part of the deliverable. In BUILD mode, keep a concise design record and proceed to code.

Read and apply [multi-page-design](references/multi-page-design.md). For single-page work, use its Page Element Blueprint fields in compact form; do not use single-page scope as a reason to skip task, state, handoff or recovery design.

### Gate C — Cross-page contract and matrices

Create a page-to-Red-Route coverage map, feature/action ownership map, page transition and state-handoff map, and shared visual/component contract. Detect overlapping responsibilities before implementation.

### Gate D — Iterative Review and Repair

Run independent review passes for:
- Per-page completeness and focus.
- Cross-page functional ownership, repetition, navigation and semantic consistency.
- End-to-end Red Route continuity, operation costs and recovery.
- Visual, responsive, accessibility and implementation consistency.

Record issues and, when repairs are requested, repair them and rerun impacted and global checks. Continue authorized repairs as long as material findings remain and progress is possible; do not stop at a report when implementation was requested. For discussion-only reviews, deliver findings and tradeoffs without editing. Do not enforce a fixed number of rounds. Read [review-repair-protocol](references/review-repair-protocol.md).

### Gate E — Exit and implementation

Proceed when critical route coverage is complete, page responsibilities are clear, material cross-page inconsistencies are resolved, necessary context survives transitions and remaining limitations are documented. If blocked by missing information, state the blocker rather than falsely declaring success.

After coding, repeat relevant reviews against actual behavior. A paper design passing review does not prove the implementation passes.

## Decision principles

- Primary actions are task-relative; multiple comparable actions may be justified.
- Preserve in-context operations where useful, but use dedicated pages for deep or shareable work.
- Do not default to dashboards, FABs, modals, tabs or wizards.
- Use progressive disclosure without burying frequent tasks.
- Avoid repeated functionality without a clear contextual purpose.
- One business action must have consistent semantics and permissions wherever it appears.
- Choose controls and disclosure from the data, intent and decision needs. Lists, dropdowns, automatic navigation and collapsed panels are conditional choices, not defaults for every product.
- Feedback must match actual capability and evidence. Unknown data is not zero, completed execution is not necessarily success, and a preview is not a committed action.
- Treat F/Z scan patterns, fixed click limits, 60/30/10 color ratios and universal color psychology as heuristics, not laws.
- Never rely on color alone for status. Support keyboard and screen-reader interaction.

## Reference routing

- [task-modeling](references/task-modeling.md): actors, objects, permissions and task graph.
- [functional-scope-and-relationships](references/functional-scope-and-relationships.md): function inventory, relationship graph, user-habit hypotheses and frontend map derivation.
- [decision-deliberation-protocol](references/decision-deliberation-protocol.md): multi-step evidence, candidate, simulation, consequence and falsification checks required before every decision is marked DONE.
- [decision-rules](references/decision-rules.md): task priority and Red Routes.
- [input-and-disclosure](references/input-and-disclosure.md): choosing inputs, defaults and progressive disclosure when collecting information or revealing secondary content.
- [information-integrity](references/information-integrity.md): truthful metrics, progress, result, source and freshness semantics when making data claims.
- [scenario-extensions](references/scenario-extensions.md): conditional collaboration, editing, long-running, bulk and consequential-action rules.
- [visual-direction-selection](references/visual-direction-selection.md): Visual Context Profile, candidate directions and Visual Grammar Contract.
- [user-perception-and-visual-decisions](references/user-perception-and-visual-decisions.md): bounded psychological hypotheses, visual responses and counter-risks.
- [image-reference-iteration](references/image-reference-iteration.md): mandatory generated reference image versions, review loop and pre-code approval gate.
- [art-direction-catalog](references/art-direction-catalog.md): visual languages, fit and anti-pattern risks.
- [layout-patterns](references/layout-patterns.md): task-to-layout selection.
- [multi-page-design](references/multi-page-design.md): per-page element blueprints and page contracts.
- [review-repair-protocol](references/review-repair-protocol.md): iterative reviews, repairs and exit criteria.
- [interaction-patterns](references/interaction-patterns.md): controls and behavior.
- [flow-continuity](references/flow-continuity.md): context persistence and handoffs.
- [operation-cost](references/operation-cost.md): P/K/D/C/W/E/M comparison.
- [color-and-tokens](references/color-and-tokens.md): semantic palette.
- [color-strategy-catalog](references/color-strategy-catalog.md): palette architectures and selection logic.
- [component-style-grammar](references/component-style-grammar.md): component variants and independent style axes.
- [typography-and-grid](references/typography-and-grid.md): type roles, composition, alignment and density.
- [surface-shape-depth](references/surface-shape-depth.md): surfaces, radius, borders, elevation and translucency.
- [imagery-iconography-motion](references/imagery-iconography-motion.md): purposeful imagery, icon grammar and motion.
- [design-system-profiles](references/design-system-profiles.md): what to borrow from mature systems without copying their theme.
- [spatial-orchestration](references/spatial-orchestration.md): space roles, layout skeletons, space budgets and mandatory spatial records.
- [component-morphology](references/component-morphology.md): component roles, containers and morphology choices.
- [visibility-persistence](references/visibility-persistence.md): V0–V4 lifecycle, collapse rules, pinning and state restoration.
- [responsive-transformation](references/responsive-transformation.md): semantic responsive transformations and state preservation.
- [floating-ui-and-occlusion](references/floating-ui-and-occlusion.md): floating layers, focus, keyboard and occlusion budget.
- [workspace-layouts](references/workspace-layouts.md): examples for complex workspaces and multi-region products.
- [ui-engineering-blueprint](references/ui-engineering-blueprint.md): pre-build engineering contract and runtime completion definition.
- [ui-engineering-foundations](references/ui-engineering-foundations.md): layout layers, spacing ownership, intrinsic sizing, visual footprint and overflow policies.
- [overlay-and-scroll-engineering](references/overlay-and-scroll-engineering.md): stacking contexts, Portal/top layer, collision, scroll ownership and sticky/fixed behavior.
- [component-engineering-checklists](references/component-engineering-checklists.md): component-family geometry, focus, hit-testing, async and platform checklist.
- [responsive-runtime](references/responsive-runtime.md): dynamic viewport, keyboard, safe area, container and cross-input behavior.
- [visual-stability-performance](references/visual-stability-performance.md): layout stability, asset metrics, animation and compositing risks.
- [browser-platform-matrix](references/browser-platform-matrix.md): risk-based browser, viewport, input and content coverage.
- [ui-debug-playbook](references/ui-debug-playbook.md): symptom-first runtime diagnosis and audit probes.
- [visual-quality](references/visual-quality.md): art direction and hierarchy.
- [art-direction-review](references/art-direction-review.md): art-direction consistency and repair lens.
- [anti-ai-template-review](references/anti-ai-template-review.md): template diagnostic and repair rules.
- [perceived-quality](references/perceived-quality.md): quality dimensions, evidence-based anti-AI tests and repair priority.
- [implementation-playbook](references/implementation-playbook.md): repository-first implementation.
- [design-output-template](references/design-output-template.md): deliverable structure.
- [validation-checklist](references/validation-checklist.md): acceptance criteria.
- [evidence-and-limits](references/evidence-and-limits.md): sources and heuristic limits.

## Calibration examples

- [B2B order workbench](examples/b2b-order-workbench.md)
- [B2B art direction comparison](examples/art-direction-comparison-b2b.md)
- [Consumer mobile booking](examples/consumer-mobile-app.md)
- [Consumer art direction comparison](examples/art-direction-comparison-consumer.md)
- [Multi-page operations product](examples/multi-page-operations.md)
- [Anti-template repair](examples/anti-ai-repair-example.md)
- [Acceptance scenarios](tests/acceptance-cases.md)
- [Visual regression prompts](tests/visual-regression-prompts.md)

## Final response contract

Show concrete layouts and interactions, not only design philosophy. Include the completed execution ledger and the references read/applied. For DESIGN, show the Visual Context Profile, candidate comparison or inherited direction, selected Visual Grammar Contract, component derivation, spatial role map, layout skeleton, lifecycle/persistence table, responsive transformation, floating occlusion budget, UI Engineering Blueprint summary, realistic-content stress test and Art Direction Review. For multi-page DESIGN, also show page element blueprints, shared rules, important cross-page transitions, and meaningful Review/Repair findings. For BUILD, report changed files, browser/runtime audit scope, screenshot/accessibility/keyboard checks and actual test results. For REVIEW, report observed evidence, repairs and rerun checks. State assumptions and unresolved limitations truthfully; never replace a missing artifact with a claim that the step was followed.
