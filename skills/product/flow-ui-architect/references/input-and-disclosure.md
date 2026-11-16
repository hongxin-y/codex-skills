# Inputs, defaults and progressive disclosure

Read when choosing form controls, settings, optional tools or collapsible content. Choose by user intent and data characteristics; this is not a requirement to add a form or an advanced-options panel.

## Choose the input model

| Information need | Candidate approach | Check before choosing |
| --- | --- | --- |
| A few known alternatives | Visible options, radio buttons or another direct choice | Comparison, labels, available space and selection semantics |
| Many known alternatives | Searchable select or combobox | Search terms, keyboard use, no results and discovery |
| Objects from a changing directory | Search backed by that directory | Loading, stale choices, eligibility and failure handling |
| Open expression or creation | Free text or an appropriate creative editor | Formatting, examples and recoverability |
| Existing values plus permitted new values | Selection with an explicit create path | Whether creation is allowed and how duplicates are handled |
| Several independent values | Multi-select or direct independent choices | Scope, readable summaries and removing a choice |

The table offers alternatives, not fixed mappings. A dropdown menu of commands is different from a select field. Do not constrain a poem, message or search intent to an incomplete enumeration, or force known identifiers into free text when selection would avoid errors.

Use user-facing labels and readable values. Do not expose serialized arrays, internal IDs or schema structure as the normal editing experience.

## Defaults reduce work without concealing decisions

- Reuse reliable context and infer routine values when appropriate; let users inspect and correct consequential choices.
- Expose the effective configuration before commitment when cost, visibility or outcome depends on it. Advanced values can remain collapsed with a useful summary.
- Do not preselect consent or treat inactivity as a judgment where an explicit choice is required.
- Do not require every optional field merely to make a form appear complete.
- Distinguish selecting an existing item from creating or changing shared data.

Examples: a booking form can inherit the selected class date; a writing tool should preserve open expression; a paid export should reveal its effective scope and price before purchase.

## Decide what can be disclosed later

Keep information visible when it is needed for understanding, comparison, the current decision or error recovery. Put lower-frequency explanation, optional configuration and lengthy history behind discoverable controls when that reduces competition.

For each hidden region, check the trigger, summary or count, active-error signal, focus behavior and restoration. An error inside a collapsed section needs a visible indication and a way to reach it. Do not auto-close unsaved input or a reference the user is comparing.

Use [visibility-persistence](visibility-persistence.md) for lifecycle decisions and [interaction-patterns](interaction-patterns.md) for container behavior. Do not turn a prior preference for collapsed comments or continuous lists into a rule for unrelated products.
