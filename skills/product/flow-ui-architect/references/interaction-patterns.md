# Interaction patterns

Choose controls based on information requirements, task frequency, context preservation, risk and recovery.

| Pattern | Prefer when | Avoid when |
| --- | --- | --- |
| Inline action/edit | Small, reversible change in context | Complex validation or risky consequences |
| Popover | Lightweight contextual choice | Long or critical workflow |
| Dropdown/menu | Related secondary commands | Hiding frequent primary actions |
| Split button | Common action with meaningful variants | Ambiguous default behavior |
| Drawer | Inspect/edit while keeping list context | Task needs extensive workspace |
| Modal | Short interruptive decision | Multi-step deep work |
| Dedicated page | Rich, focused, shareable work | Every small routine action |
| Tabs | Stable peer content categories | Sequential steps disguised as tabs |
| Wizard | Dependencies and staged validation | A simple form |
| Bottom sheet | Mobile contextual action | Complex full-screen work |
| Sticky action bar | Actions needed while scrolling | Obscuring content |
| Context toolbar | Selection-specific operations | Unclear scope |
| Command palette | Expert cross-area commands | Replacing discoverable basic navigation |
| FAB | Frequent global create/compose action | Dense enterprise workspace |
| Floating assistant | Optional help or AI collaboration | Replacing core product actions |

## FAB versus assistant

A FAB executes a recognizable product action. A floating assistant opens a support or collaboration experience. A sticky action bar exposes controls for the current task. Do not conflate them.

## Semantics

Use buttons for actions and links for navigation. Labels should state consequences. Do not rely on icon-only controls without accessible names. Make destructive operations clear.

## States

Design relevant loading, empty, filtered-empty, success, failure, partial success, permission, disabled, conflict, unsaved and offline states. Provide visible focus and keyboard behavior.

## Feedback

Explain what happened, what remains and what can happen next. Use undo when safe; use confirmation when risk justifies it.

## Cross-page rule

The same action must have consistent meaning, eligibility, permissions and feedback on every page. Contextual shortcuts may differ visually, but must invoke the same underlying behavior.
