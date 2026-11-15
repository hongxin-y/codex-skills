# Iterative Review and Repair protocol

## Purpose

Detect and fix problems that are invisible when each page is reviewed alone: duplicated features, conflicting navigation, inconsistent semantics, lost context, disconnected Red Routes and visual fragmentation.

Review is not the final paragraph of a design report. It is a repair loop with explicit findings, changes and regression checks.

## Required loop

Page Blueprints → Art Direction Gate → Review → Issue Ledger → Repair → Regression Review → Re-evaluate.

Repeat while material issues remain and actionable progress is possible. Do not prescribe a fixed number of cycles. The distinct review lenses below must be covered, even if they are combined for a small product.

## Review lens: Individual page

For every page, verify:

- Clear purpose, actor, main job and completion condition.
- Required content is present at decision time.
- Functional points are discoverable and valid for the current state.
- Visual focus matches the job.
- Operation sequence is understandable and not needlessly fragmented.
- Loading, empty, success, error, permission and recovery states are addressed when relevant.
- Responsive and keyboard behavior are plausible.

Repair missing or misplaced elements before polishing.

## Review lens: Spatial and dynamic behavior

For every page and major floating element, verify:

- Task, Reference, Navigation, Tool, Status, Transient and Breathing Space roles are explicit.
- The layout skeleton protects the main task, preserves repeated reference and does not spend space evenly when task priority is uneven.
- Each region has a V0–V4 lifecycle, trigger, dismissal policy, auto-collapse prohibition, pin/remember behavior and state restoration.
- Responsive behavior transforms semantics in the order `resize → compact → rail → drawer/sheet → dedicated page` before hiding content.
- Collapse never loses unsaved input, current focus, active errors, task-critical state, repeated comparison or user-pinned preferences.
- Floating layers have a bounded occlusion budget and do not cover primary actions, focus, errors, keyboard paths or safe areas.
- Tooltip, popover, panel, drawer, modal and page are used according to content complexity; the modal is not a universal space fix.
- Long content, narrow widths, minimum text sizes, keyboard operation and screen-reader order were exercised.

Repair lifecycle or container decisions before tuning spacing. A panel that must be reopened repeatedly is a persistence defect, not a user habit to ignore.

## Review lens: UI engineering quality

For each page, shared primitive and high-risk component, review the actual browser contract:

- Geometry: spacing owner, box sizing, intrinsic sizing, Flex/Grid automatic minimums, visual footprint, baseline and content growth.
- Overflow: actual scroll owner, nested scrolling, scroll chaining, truncation/wrapping, sticky reference, anchor offsets and restoration.
- Layering: clipping boundary, stacking contexts, semantic layer token, Portal/top-layer choice, collision flip/shift/size and overlay registration.
- Hit testing: transparent overlays, pseudo-elements, `pointer-events`, pointer capture, touch-action, nested click ownership and visible-versus-actual target.
- Focus/accessibility: visible focus, focus containment/return, keyboard model, screen-reader tree, target size, forced colors and focus obscuration.
- Runtime stability: image/font/skeleton/error slots, async height, hydration, virtualization measurement, layout shift, animation cancellation and reduced motion.
- Platform: dynamic viewport, keyboard, safe area, RTL, zoom, CJK/emoji/font fallback, target browser and embedded context.

Run the symptom-first [ui-debug-playbook](ui-debug-playbook.md) before changing CSS. In BUILD, collect a runtime audit and rerun affected routes after repairs. Treat arbitrary huge z-index, global `transition: all`, blanket `will-change`, unbounded `100vh`, `outline:none` without replacement and component-level external margins as review risks.

## Review lens: Cross-page architecture

Compare ALL page blueprints and the shared contract:

- Are two pages doing the same job without a justified boundary?
- Does every major feature have a clear canonical owner?
- Are duplicated shortcuts intentionally connected to the same operation?
- Do labels, object names, status vocabulary and button semantics match?
- Is navigation hierarchy stable and predictable?
- Are shared components reused rather than independently reinvented?
- Are permissions and destructive-action safeguards consistent?
- Are data sources and editable fields consistent?
- Are there unnecessary round trips between pages?

Repair by merging pages, reassigning ownership, introducing shared components, changing navigation or consolidating state where appropriate. Do not merge distinct tasks merely to reduce page count.

## Review lens: End-to-end Red Routes

Walk each critical route from entry to verified completion and recovery:

- Can the actor reach every required step?
- Is necessary context available at the moment of decision?
- Do page transitions preserve filters, selection, scroll, drafts and focus where appropriate?
- Does success update the source page and related views coherently?
- Does failure preserve work and provide recovery?
- Can the user continue to the next task without reorientation?
- Are operations duplicated, ambiguous or avoidably repeated?

Compare P/K/D/C/W/E/M qualitatively or using actual measured data. If a proposed improvement adds safety steps, explain the risk tradeoff rather than hiding the extra operations.

## Review lens: Visual, responsive and engineering consistency

Verify semantic tokens, type hierarchy, spacing, button variants, icons, status colors, table patterns, navigation behavior, focus states, mobile transformations and component reuse.

## Review lens: Art direction and anti-template quality

Use [art-direction-review](art-direction-review.md) and [anti-ai-template-review](anti-ai-template-review.md). Verify:

- The selected visual thesis is visible in typography, grid, density, palette, shape, surface, imagery, iconography, motion and component expression.
- Pages look like one product without forcing identical layouts or inventing independent visual languages.
- Component variants derive from the Visual Grammar Contract rather than being chosen independently.
- Realistic content and exceptional states influenced the layout and visual decisions.
- Gradients, blur, glow, pills, cards, KPI blocks, charts and illustrations each have a task, orientation, evidence or brand reason.
- Findings distinguish usability defects, system inconsistencies, art-direction weaknesses and subjective taste.

In BUILD mode, inspect actual code and exercise interactions. A specification review cannot substitute for implementation tests.

Use [perceived-quality](perceived-quality.md) to classify Task fit, Accessibility, Semantic fit, Hierarchy, Authenticity, Coherence, Craft, Restraint and Distinctiveness. Repair in that order; use deletion, substitution and realistic-content tests to turn “AI味” into observable symptoms and concrete changes.

## Issue ledger

For each finding, record:

| Field | Meaning |
| --- | --- |
| ID | Stable issue identity |
| Severity | Blocking, significant or improvement |
| Scope | Page, route, component or global |
| Symptom | Observable problem |
| Root cause | Why it occurs |
| Repair | Concrete change |
| Impacted areas | Pages and routes requiring regression review |
| Verification | Evidence needed to close |
| Status | Open, repaired, verified, blocked or deferred |

Use severity according to task risk, not arbitrary scores. Do not claim an issue verified merely because a proposed fix was written.

## Repair rules

- Fix architecture and ownership before local styling.
- Repair shared components or tokens at their source when the defect is systemic.
- Update the page blueprints and shared contract after any consequential change.
- Recalculate route operations if a transition or action changes.
- Recheck adjacent pages when handoff behavior changes.
- Recheck all pages when global navigation, status semantics or tokens change.
- Avoid fixing one page by creating a new inconsistency elsewhere.

## Regression review

After each meaningful repair, rerun the checks affected by the change. Then perform a cross-page sanity pass so that local improvements do not regress product coherence.

Examples:
- Move an action to a drawer → review action discoverability, keyboard access and the route across both surfaces.
- Merge pages → review navigation, deep links, permissions, return state and all affected routes.
- Rename a status → review every page, filter, badge, notification and message using it.
- Change shared tokens → review contrast and component states throughout the product.

## Exit conditions

The review loop may conclude when:

- Critical Red Routes have coherent entry-to-completion paths.
- Page responsibilities and action ownership are unambiguous.
- Material cross-page inconsistencies and harmful duplication are resolved.
- State handoffs and recovery are accounted for.
- Visual/component conventions are consistent or intentionally differentiated.
- Blocking issues are resolved or explicitly reported as blocked.
- Remaining findings are documented and do not undermine the claimed deliverable.

Do not promise zero defects. If user testing, browser checks or repository access are unavailable, mark those checks as not verified.

## Efficiency and autonomy

Avoid endless cosmetic iteration. If a further pass finds no meaningful issues, or unresolved issues require missing information, stop and report the limitation. Do not use a fixed cycle count as a proxy for quality.

The agent may combine review lenses for a simple app, but must not skip cross-page review and must rerun relevant checks after repairs.

## Final review summary

Report the major detected issues, repairs made, affected routes, verification results and remaining limitations. Keep the summary proportional to the work.
