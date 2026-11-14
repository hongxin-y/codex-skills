# UI/UX validation checklist

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
