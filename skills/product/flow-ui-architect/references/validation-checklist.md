# UI/UX validation checklist

## Execution compliance

- [ ] The step ledger is present and covers every applicable step.
- [ ] Each required reference was read before the related decision was made.
- [ ] Each DONE step has a concrete artifact, not a generic claim.
- [ ] Each skipped step is marked N/A with a task-specific reason; blocked steps are reported honestly.
- [ ] BUILD did not begin before the task model, route model, blueprint, Art Direction Contract and interaction contract were recorded.
- [ ] REVIEW includes observed evidence, repairs and rerun checks when repairs were requested.

## Product and task

- Is each Red Route grounded in a real user job?
- Is the selected layout appropriate to the task?
- Are current object, state and next action clear?
- Are important exceptions and permissions represented?

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

## Visual and accessibility

- Is there a coherent hierarchy and visual thesis?
- Is there a documented Visual Context Profile and selected art direction or inherited visual contract?
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

## Engineering

- Do visible controls work?
- Are async and error states implemented?
- Is real versus mocked behavior clear?
- Does code follow project conventions?
- Were actual tests run and reported truthfully?

## Review/Repair verification

For each issue, identify its scope, repair and regression checks. Mark verified, unverified, blocked or deferred honestly.

Do not declare zero defects without evidence. Do not use a fixed review count as proof of quality.
