# Task continuity and state preservation

Optimize the complete work session rather than isolated screens.

## Task graph

Entry → locate → inspect → decide → act → feedback → next task / recover / exit.

Use the segments appropriate to the intent. Reading can continue through references, creation can loop through revision, and exploration can branch without a required final submission. Do not invent a mutation or handoff to complete the diagram.

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

Choose continuation by the user's actual goal:

- Offer the next item when sequential processing is expected and eligibility is known.
- Keep the result visible when reading, comparison or reflection should continue.
- Open a configuration or decision when it is the next useful step; opening it does not execute its consequential action.
- Explain waiting or handoff only when another actor or system is actually involved.
- Allow a natural exit when the user's goal is complete, without requiring a new task.

For applicable collaboration, editing, execution or bulk rules, use [scenario-extensions](scenario-extensions.md). For result, progress and freshness semantics, use [information-integrity](information-integrity.md).

## Example

Weak flow: filter orders → open full detail → approve → return to default list → search again.

Better flow: filter orders → inspect in contextual detail → approve → update row and counts → preserve filter/scroll → continue with next eligible order.
