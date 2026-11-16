# Truthful information and feedback

Read when the UI makes claims through counts, charts, progress, source labels, freshness, availability or action results. Apply only the relevant checks.

## Quantities and comparisons

For a meaningful quantity, identify its object, unit, scope, time and comparison basis as needed. Explain version, deduplication or denominator differences when they would change interpretation. A summary and its drill-down should describe the same scope or make the change explicit.

Do not render unknown, not yet loaded, not recorded, unavailable or unauthorized information as zero. Distinguish an empty collection from no matching results and a failed request.

If a target or comparison basis is absent, show the available count or distribution without inventing a passing result. Do not use a decorative progress bar to imply measured completion.

Charts should support a real question. Provide a route to evidence or relevant action when useful; do not duplicate dashboard cards where the user needs reading, editing or discovery.

## Action and execution feedback

- Labels and affordances match capability: preview, download, navigate, edit, save and commit have different meanings.
- Opening a file is not the same as locating a particular passage; a link should not promise unsupported precision.
- A successful request is not necessarily completed downstream execution. Distinguish accepted, pending, finished and failed only where those states actually exist.
- Show real progress when available; otherwise show the known stage or indeterminate activity. Label estimates as estimates.
- Keep partial success, skipped items and recoverable failures visible beyond a transient toast when the user needs to act on them.
- Do not show simulated, optimistic or locally saved behavior as a confirmed server result. Reconcile optimistic updates and preserve user input on failure.

## State, source and freshness

Separate process progress, persistence, content changes, judgment and effective publication when the product has those dimensions. An edited document may be unsaved; a saved draft may be unpublished. A completed export may contain failed records. Do not introduce all these states into a simple read-only page.

When history or versions affect meaning, identify which content a result refers to. Updating current content should not silently reinterpret a historical decision or fixed output.

Sources and freshness labels should reflect available evidence. Cached, stale or inferred values need appropriate qualification when it affects use. Do not invent provenance or certainty to make a design look complete.
