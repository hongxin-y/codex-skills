---
name: flow-ui-architect
description: "Design, review, and implement coherent, accessible, task-first UI/UX from brief business scenarios. Use for page design, multi-page product flows, navigation, frontend implementation, UI review, visual systems, Red Routes, workflow optimization, and cross-page consistency. Infer reasonable requirements, create per-page element blueprints, review and repair duplication or continuity problems, and implement working UI when requested."
---

# Flow UI Architect

Transform a brief business scenario into an appropriate, usable, attractive and implementable interface. Optimize complete user tasks, not decorative screen count or fashionable layout templates.

## Operating contract

- Work as a product designer, interaction designer, visual designer and frontend engineer when appropriate.
- A one-sentence scenario is enough to begin. Infer ordinary missing details and label consequential assumptions. Ask only when an unknown materially affects safety, permissions, business correctness or irreversible decisions.
- Separate USER facts, REPO facts, EVIDENCE and ASSUMPTIONS. Never present guesses as verified requirements.
- Choose page count, Red Routes, action hierarchy, navigation depth, review cycles and visual complexity based on the task. Do not enforce arbitrary numerical quotas.
- Preserve useful existing project conventions and components.
- Make important decisions explicit, but adapt explanation length to task complexity.
- Keep real accessibility standards and technical constraints.

## Select the operating mode

DESIGN: Produce concrete screen and interaction designs. For a multi-page request, show the Page Element Blueprint for each page before detailed layout decisions.

BUILD: Inspect the existing repository and implement the requested UI. For a multi-page build, first create a concise page blueprint and shared contract, then proceed without requiring approval unless a consequential decision is blocked. Do not replace working code with a design essay.

REVIEW: Diagnose existing designs or code, identify task friction and inconsistencies, and propose or implement repairs. Distinguish observed defects from hypotheses.

## Core workflow

### Understand the business task

Infer actors, triggers, outcomes, business objects, permissions, frequency, urgency, error costs, device context and collaboration needs. Read [task-modeling](references/task-modeling.md).

### Identify task routes

Model entry, locate, inspect, decide, act, feedback, recovery and continuation. Select Red Routes according to user value, frequency, business impact, risk and dependencies. There is no prescribed route count. Read [decision-rules](references/decision-rules.md).

### Determine page scope

For a single-page task, select a suitable layout directly.

For multiple pages or connected product surfaces, the MULTI-PAGE DESIGN GATE below is mandatory before detailed UI or implementation.

### Choose layout and interaction patterns

Select workbench, queue, master-detail, search/results, dashboard, form, wizard, editor, timeline, feed, comparison or a justified hybrid. Compare alternatives. Use inline actions, drawers, modals, tabs, sticky bars, FABs and other controls only when they fit the job. Read [layout-patterns](references/layout-patterns.md) and [interaction-patterns](references/interaction-patterns.md).

### Optimize cost and continuity

Compare P/K/D/C/W/E/M: pointing, input, decisions, context switches, waiting, error recovery and memory burden. Preserve search, filters, sort, selection, scroll, drafts and next-task context where relevant. Read [operation-cost](references/operation-cost.md) and [flow-continuity](references/flow-continuity.md).

### Build the visual system

Define hierarchy, density, typography, spacing, semantic color tokens, surfaces and responsive transformations. Read [color-and-tokens](references/color-and-tokens.md) and [visual-quality](references/visual-quality.md).

### Deliver and validate

For DESIGN, provide an actionable blueprint or prototype. For BUILD, implement and run available checks. For REVIEW, prioritize findings and repairs. Use [design-output-template](references/design-output-template.md), [implementation-playbook](references/implementation-playbook.md) and [validation-checklist](references/validation-checklist.md).

## Mandatory MULTI-PAGE DESIGN GATE

Apply whenever the request includes multiple connected pages, routes or substantial screens.

### Gate A — Page inventory and route graph

Identify every justified page, its role, entry/exit points and Red Route participation. Avoid adding pages merely because an app convention suggests them. Create a shared product contract covering navigation, naming, permissions, status semantics, data ownership, component reuse and visual tokens.

### Gate B — Per-page element design BEFORE detailed screens

Create a Page Element Blueprint for EACH page, including:
- Page ID, purpose, actor and completion condition.
- Functional points and actions, including action ownership and consequences.
- Required content, data objects, source and edit permissions.
- Red Routes entering, passing through or completing on the page.
- Focal point: what the user should notice, understand and do next.
- Element inventory and hierarchy: navigation, data, controls, feedback and states.
- Operation path and operation count when derivable, with P/K/D/C/W/E/M analysis; distinguish estimates from measurements.
- Entry, exit, handoff, preserved context and recovery.
- Shared versus page-specific components, responsive behavior and assumptions.

Do not skip this step and jump straight to independent page mockups. In DESIGN mode, present these blueprints as part of the deliverable. In BUILD mode, keep a concise design record and proceed to code.

Read [multi-page-design](references/multi-page-design.md).

### Gate C — Cross-page contract and matrices

Create a page-to-Red-Route coverage map, feature/action ownership map, page transition and state-handoff map, and shared visual/component contract. Detect overlapping responsibilities before implementation.

### Gate D — Iterative Review and Repair

Run independent review passes for:
- Per-page completeness and focus.
- Cross-page functional ownership, repetition, navigation and semantic consistency.
- End-to-end Red Route continuity, operation costs and recovery.
- Visual, responsive, accessibility and implementation consistency.

Record issues, repair them, and rerun impacted and global checks. Continue as long as material findings remain and progress is possible. Do not enforce a fixed number of rounds; do not stop after merely writing a review report. Read [review-repair-protocol](references/review-repair-protocol.md).

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
- Treat F/Z scan patterns, fixed click limits, 60/30/10 color ratios and universal color psychology as heuristics, not laws.
- Never rely on color alone for status. Support keyboard and screen-reader interaction.

## Reference routing

- [task-modeling](references/task-modeling.md): actors, objects, permissions and task graph.
- [decision-rules](references/decision-rules.md): task priority and Red Routes.
- [layout-patterns](references/layout-patterns.md): task-to-layout selection.
- [multi-page-design](references/multi-page-design.md): per-page element blueprints and page contracts.
- [review-repair-protocol](references/review-repair-protocol.md): iterative reviews, repairs and exit criteria.
- [interaction-patterns](references/interaction-patterns.md): controls and behavior.
- [flow-continuity](references/flow-continuity.md): context persistence and handoffs.
- [operation-cost](references/operation-cost.md): P/K/D/C/W/E/M comparison.
- [color-and-tokens](references/color-and-tokens.md): semantic palette.
- [visual-quality](references/visual-quality.md): art direction and hierarchy.
- [implementation-playbook](references/implementation-playbook.md): repository-first implementation.
- [design-output-template](references/design-output-template.md): deliverable structure.
- [validation-checklist](references/validation-checklist.md): acceptance criteria.
- [evidence-and-limits](references/evidence-and-limits.md): sources and heuristic limits.

## Calibration examples

- [B2B order workbench](examples/b2b-order-workbench.md)
- [Consumer mobile booking](examples/consumer-mobile-app.md)
- [Multi-page operations product](examples/multi-page-operations.md)
- [Acceptance scenarios](tests/acceptance-cases.md)

## Final response contract

Show concrete layouts and interactions, not only design philosophy. For multi-page DESIGN, show page element blueprints, shared rules, important cross-page transitions, and meaningful Review/Repair findings. For BUILD, report changed files and actual tests. State assumptions and unresolved limitations truthfully.
