# UI/UX validation checklist

## Execution compliance

- [ ] The step ledger is present and covers every applicable step.
- [ ] Each required reference was read before the related decision was made.
- [ ] Each DONE step has a concrete artifact, not a generic claim.
- [ ] Each skipped step is marked N/A with a task-specific reason; blocked steps are reported honestly.
- [ ] A function inventory and typed relationship graph exist before page, navigation or component decisions.
- [ ] Every page, route and major component traces to function nodes; every function has an entry, result, recovery and continuation path.
- [ ] User-habit assumptions cover first use, repeated use, interruption/return, comparison or batch behavior and device context when relevant.
- [ ] Every decision records evidence, candidates, representative-user simulation, downstream consequences, a falsifying counterexample and verification.
- [ ] Visual DESIGN/BUILD includes an Image Generation reference chain (`V0`, `V1`, `V2+`), per-version review log and explicit approval record before detailed implementation.
- [ ] BUILD did not start UI code before the reference image gate, pre-code design validation and UI Engineering Blueprint were complete.
- [ ] BUILD did not begin before the task model, route model, blueprint, Art Direction Contract, spatial orchestration record, UI Engineering Blueprint and interaction contract were recorded.
- [ ] BUILD did not begin before the function and relationship model, frontend map and pre-code deliberation records were complete.
- [ ] BUILD did not write UI code until every pre-build decision step was DONE or explicitly N/A/BLOCKED with a resolution plan.
- [ ] REVIEW includes observed evidence, repairs and rerun checks when repairs were requested.

## Product and task

- Is the dominant user intent identified, with an appropriate success or experience criterion?
- Can an unfamiliar target user understand the surface's purpose, current scope, available actions and relevant consequences?
- Is each Red Route grounded in a real user job?
- Is the selected layout appropriate to the task?
- Are current object, state and next action clear?
- Are important exceptions and permissions represented?
- Are new features and entry points justified by user needs rather than the availability of a component?
- Are collaboration, editing, long-running, bulk and consequential-action checks applied only when those scenarios exist?

## Inputs and information integrity

- Do input controls match finite choices, dynamic directories or open expression, including any allowed creation path?
- Are effective defaults and consequential settings discoverable before commitment, with active errors reachable even in collapsed regions?
- Do quantities, comparisons and drill-downs use clear scope and consistent interpretation? Are unknown, unavailable, failed and zero states distinguished?
- Do labels, progress, sources, freshness and result feedback match actual capabilities and evidence?
- Are actual persistence, content changes, execution results and judgment distinguished where applicable, without inventing unnecessary lifecycle states?

## Multi-page structure

- Does every page have a completed Page Element Blueprint?
- Does each page have a distinct justified responsibility?
- Is every critical Red Route covered from entry to completion?
- Does every major action have a canonical owner?
- Is repetition intentional and semantically consistent?
- Do page transitions preserve required context?
- Are navigation, naming, status and component patterns consistent?
- Were material issues repaired and impacted routes rechecked?

## Interaction and continuity

- Do query, filters, sort, selection and scroll persist where expected?
- Are drafts protected?
- Are success, failure, retry and next-task behaviors clear?
- Are floating controls justified?
- Are destructive actions safeguarded proportionately?

## Spatial and dynamic behavior

- [ ] Every major region has a Task, Reference, Navigation, Tool, Status, Transient or Breathing Space role.
- [ ] The layout skeleton, rejected alternative and spatial bottleneck are recorded.
- [ ] Every panel, filter, assistant, feedback layer and floating element has a V0–V4 lifecycle, trigger, dismissal rule and auto-collapse prohibition.
- [ ] Pin/remember preferences and state restoration cover selection, filters, scroll, drafts, focus, errors and panel state where relevant.
- [ ] Responsive transformation uses resize → compact → rail → drawer/sheet → dedicated page before hiding task-critical information.
- [ ] Floating UI has an occlusion budget and does not cover task controls, focus, errors, keyboard paths or safe areas.
- [ ] Hover/focus content is keyboard-triggerable, dismissible and hoverable; modal focus enters, traps, escapes and returns correctly.
- [ ] Long content, narrow widths, keyboard input and screen-reader order were checked for every dynamic container.

## UI engineering quality

- [ ] Every major region and shared primitive has a layout/sizing contract, spacing owner and content-growth rule.
- [ ] Flex/Grid automatic minimum sizing was checked; `min-width:0`, `min-height:0` and `minmax(0,1fr)` are used only when justified by the content contract.
- [ ] Every container has an explicit overflow policy and scroll owner; nested scrolling, scroll chaining, sticky reference, anchor offsets and restoration were checked.
- [ ] Every overlay has a clipping/stacking/Portal or top-layer decision, collision boundary, flip/shift/size strategy, Escape/outside-press owner, scroll strategy and focus return.
- [ ] Visible controls are hit-testable and keyboard reachable; transparent layers, pseudo-elements and pointer-events were inspected.
- [ ] Images, fonts, skeletons, async cards, virtualized rows and error slots have stable-size policies; layout shifts and animation cancellation were considered.
- [ ] Responsive runtime includes dynamic viewport, keyboard, safe-area, container width, RTL and zoom behavior when relevant.
- [ ] High-risk components were checked against the component engineering checklist and browser/platform matrix.
- [ ] BUILD includes browser runtime audit, screenshot regression, accessibility automation and manual keyboard/touch/overlay checks with honest status.
- [ ] Static risks such as arbitrary z-index, `transition: all`, blanket `will-change`, `outline:none`, unbounded `100vh` and component-level external margins were searched or consciously accepted.

## Visual and accessibility

- Is there a coherent hierarchy and visual thesis?
- Is there a documented Visual Context Profile and selected art direction or inherited visual contract?
- Are psychological assumptions written as bounded hypotheses with observable signals, counter-risks and verification methods?
- Were materially different candidate directions compared when the visual direction was open?
- Does the Visual Grammar Contract cover typography, grid, density, palette, shape, surface/depth, imagery, iconography, motion and component variants?
- Were component styles derived from that contract rather than chosen independently?
- Were long content, missing values, dense tables, permissions, errors, empty states and narrow layouts used in a visual stress test?
- Does the anti-template review distinguish usability, system consistency, art direction and subjective taste?
- Are semantic tokens reused?
- Are statuses distinguishable without color alone?
- Are semantic controls, accessible names and visible focus present?
- Is keyboard navigation functional?
- Are applicable WCAG contrast requirements met?
- Does mobile transform the workflow appropriately?
- [ ] Does the visual decision survive realistic content without generic card/gradient/glass repetition?
- [ ] Were deletion, substitution and realistic-content anti-AI tests recorded with repairs?
- [ ] Was the approved reference compared with the implemented result after BUILD, with deviations repaired or reported?

## Engineering

- Were the requested change boundary and unaffected behavior preserved, including visual-only work that can alter interaction through CSS?
- Do visible controls work?
- Are async and error states implemented?
- Is real versus mocked behavior clear?
- Does code follow project conventions?
- Were actual tests run and reported truthfully?

## Review/Repair verification

For each issue, identify its scope, repair and regression checks. Mark verified, unverified, blocked or deferred honestly.

Do not declare zero defects without evidence. Do not use a fixed review count as proof of quality.
