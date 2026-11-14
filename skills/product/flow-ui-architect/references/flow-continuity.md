# Task continuity and state preservation

Optimize the complete work session rather than isolated screens.

## Task graph

Entry → locate → inspect → decide → act → feedback → next task / recover / exit.

Mark transitions that require re-searching, re-entering values, remembering context or waiting unnecessarily.

## State preservation ledger

| State | Typical expectation |
| --- | --- |
| Search query | Preserved on return from detail |
| Filters and sort | Preserved across actions and refresh |
| Scroll position | Restored when returning to a list |
| Selected object | Remains identifiable |
| Draft | Autosaved or protected against accidental loss |
| Form validation | Correct entries retained |
| History and undo | Available for reversible operations |
| Focus | Moves predictably after overlays |
| Next task | Offered when it follows naturally |

Do not preserve stale or sensitive state without privacy and correctness considerations.

## Page handoff contract

For every page transition define:
- Source and destination.
- User intent and trigger.
- Object ID and state transferred.
- Query/filter/selection/draft context retained.
- Back and deep-link behavior.
- Loading, error and permission handling.
- Completion feedback and next action.

If a route requires repeated context rebuilding, reconsider the page boundary.

## Cohesive workspace

Prefer list + detail + action for repeated object processing. Use a dedicated page for deep editing, concentration or shareable context. Combining unrelated tasks into one giant page is not continuity.

## Completion

After success, update relevant records and views, show feedback and expose the next useful step. Automatic next-item navigation is appropriate only when predictable and safe.

After failure, preserve entered data and offer retry, correction or escalation.

## Example

Weak flow: filter orders → open full detail → approve → return to default list → search again.

Better flow: filter orders → inspect in contextual detail → approve → update row and counts → preserve filter/scroll → continue with next eligible order.
