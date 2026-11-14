# Iterative Review and Repair protocol

## Purpose

Detect and fix problems that are invisible when each page is reviewed alone: duplicated features, conflicting navigation, inconsistent semantics, lost context, disconnected Red Routes and visual fragmentation.

Review is not the final paragraph of a design report. It is a repair loop with explicit findings, changes and regression checks.

## Required loop

Page Blueprints → Review → Issue Ledger → Repair → Regression Review → Re-evaluate.

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

In BUILD mode, inspect actual code and exercise interactions. A specification review cannot substitute for implementation tests.

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
