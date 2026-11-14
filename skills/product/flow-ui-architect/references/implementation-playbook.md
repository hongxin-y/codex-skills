# Repository-first UI implementation

## Inspect before editing

Identify framework, routing, styling, component library, design tokens, data layer, state management, tests and project instructions.

Reuse existing conventions. Do not install new UI libraries merely from habit.

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

Report checks actually performed. Never claim a browser, build or usability test passed if it was not run.

## Report

Summarize changed files, key layout decisions, completed routes, Review/Repair findings, verification and remaining limitations.

Avoid unrelated rewrites, fake success states and decorative controls without behavior.
