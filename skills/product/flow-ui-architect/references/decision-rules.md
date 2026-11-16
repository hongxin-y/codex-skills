# Decision rules

## Qualitative priority lenses

Use F/I/T/R/X without fabricated numeric weights:

- F: Frequency of the task.
- I: Impact of successful or failed completion.
- T: Time sensitivity.
- R: Risk and reversibility.
- X: Context exposure required to decide.

Explain important tradeoffs rather than computing a made-up score.

## Red Route selection

Identify jobs from the task graph. Keep routes that explain actual product value, important exceptions and distinct permissions. Merge routes when they are one coherent task with shared context. Split routes when actors, consequences or decision requirements differ materially.

Never enforce a fixed number of Red Routes.

## Feature and navigation boundaries

Before adding a page or navigation item, classify the need: distinct user goal, business object, lifecycle state, filter, alternative view or supporting tool. Use a page when independent context, depth, access or a shareable destination justifies it; use in-context controls when they better preserve the user's intent.

Keep peers at a comparable conceptual level. A status filter, a reporting view and an object catalog should not become equal navigation destinations merely because each has a separate implementation. Multiple shortcuts are useful when they reach the same coherent operation and share its semantics.

Judge both fragmentation and over-consolidation: fewer pages can still create an unreadable surface with competing purposes.

## Action hierarchy

Prioritize the next valid action for the current object and state. Multiple comparable actions may deserve similar visibility when the user must choose between them. Demote infrequent maintenance actions without hiding safety-critical information.

A landing page may benefit from one dominant conversion path; a complex workbench may need multiple state-specific actions. Neither is a universal rule.

## Information hierarchy

Put decision-relevant information before decorative summaries. Group by task, object, state and relationship. Favor recognition over recall.

F-shaped and Z-shaped scanning are hypotheses to test, not mandatory layout rules.

Use [input-and-disclosure](input-and-disclosure.md) for defaults and progressive disclosure. Secondary information may collapse, but critical terms, decision evidence and active errors must remain discoverable before the user acts. Reading, creation and exploration may need different emphasis from processing queues.

## Review questions

Which job does the element serve? Why is it visible now? What information is needed? What happens afterward? What context is lost? Is there a safer or simpler alternative?
