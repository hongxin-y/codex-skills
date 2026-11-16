# Repository-first UI implementation

## Inspect before editing

Identify framework, routing, styling, component library, design tokens, data layer, state management, tests and project instructions.

Reuse existing conventions. Do not install new UI libraries merely from habit.

## Change boundary

Identify whether the request covers presentation, interaction, functionality or data integration. Preserve behavior outside that boundary.

For visual-only work, preserve routes, event semantics, submission timing, defaults, expanded/collapsed state, selection scope, focus behavior and scroll/resize interactions. CSS can change behavior through visibility, order, pointer events, positioning or overflow; a CSS-only diff does not prove interaction is unchanged. If the requested visual adaptation needs a consequential behavior change, explain the dependency rather than silently making it.

A discussion or review does not authorize implementation. Reusing a reference design authorizes only the requested adaptation, not its unrelated business rules. Report out-of-scope defects separately and complete the authorized work when possible.

## Plan

Map actors and routes to pages, then page element blueprints to components, state and data dependencies.

For multi-page BUILD, complete the design gate and shared contract before broad implementation. The agent may keep the design record concise but must not skip it.

Identify real APIs. If absent, label local/mock behavior clearly and do not claim persistence.

## Implement

Build actual route behavior, not static screenshots. Include relevant loading, empty, success, error, disabled, conflict and confirmation states.

Preserve filters, selection and drafts when the route depends on them. Handle async errors and optimistic updates safely.

Reuse shared navigation, components and semantic tokens across pages. Avoid independently implementing the same business operation in several places.

## Review and repair

After the initial implementation, run [review-repair-protocol](review-repair-protocol.md) against actual code and behavior. Fix cross-page duplication, mismatched semantics and broken handoffs.

When shared components change, regression-check their consumers.

## Verify

Run available typecheck, lint, unit tests, build and runtime checks. Inspect relevant viewport sizes. Exercise the real Red Routes and error recovery when tooling permits.

Check the preserved interactions as well as the changed surface. For a visual-only update, compare the relevant before/after navigation, input, submission and scrolling behavior; do not treat matching screenshots as a behavior regression check.

Report checks actually performed. Never claim a browser, build or usability test passed if it was not run.

## Report

Summarize changed files, key layout decisions, completed routes, Review/Repair findings, verification and remaining limitations.

Avoid unrelated rewrites, fake success states and decorative controls without behavior.
