# Visual direction selection

## When to read

Read before detailed styling or code whenever the repository or brand system does not already establish a visual direction. If a mature design system already exists, document the inherited contract and explain which decisions remain open.

## Visual Context Profile

Record the facts that should change visual decisions:

| Dimension | Questions |
| --- | --- |
| Product mode | Operate, Persuade, Read, Experience or mixed? |
| Audience | Expert or novice, domain knowledge, age, culture and accessibility context? |
| Session | Short repeated work, long session, occasional high-risk task or immersive browsing? |
| Density | Sparse, moderate, dense or extremely dense? Why? |
| Trust and risk | Low-stakes, consequential or regulated? |
| Brand | Neutral, authoritative, warm, premium, playful or experimental? |
| Content | Text, structured data, media, canvas or mixed? |
| Device | Desktop, mobile, native, responsive or spatial? |
| Existing system | Which components, tokens and platform conventions already exist? |
| Differentiation | Should the product feel system-native, strongly branded or tool-like? |

Do not invent these facts. Use USER facts, REPO facts, EVIDENCE and ASSUMPTIONS.

## Candidate art directions

Do not select a generic SaaS aesthetic by default. When the direction is genuinely open, propose meaningfully different candidates that expose a real trade-off. The number of candidates is task-dependent; do not create alternatives that differ only by hue.

For every candidate record:

- Visual thesis: the job the visual language performs.
- Lineage or reference: design movement, product system or platform influence.
- Fit: which context facts it supports.
- Typography: family character, roles, scale and numeric treatment.
- Grid and composition: alignment, columns, density and scan path.
- Palette strategy: neutral/accent, tonal, warm/cool, chroma and status separation.
- Shape and surface: radius family, borders, elevation, translucency and grouping.
- Imagery and iconography: source, purpose, optical weight and consistency.
- Motion: continuity, status, hierarchy and reduced-motion behavior.
- Component treatment: variants for the important controls and data views.
- Risks and anti-example: where the direction would fail or become a cliché.

Select one direction and explain why the others were rejected. A candidate comparison is not required when an existing brand or design system already fixes the direction; in that case record the inherited decision and its constraints.

## Visual Grammar Contract

Commit the selected direction to a cross-page contract before choosing individual component styles:

- Art direction thesis and lineage.
- Type roles: display, page title, section title, body, label, metadata and numeric.
- Grid, alignment, shell, density modes and responsive transformations.
- Palette strategy, semantic roles, status mappings and dark-theme remapping.
- Shape grammar: radius family and where capsules are allowed.
- Surface/depth grammar: flat, border-led, layered, elevated or translucent.
- Icon family, stroke/fill behavior and metaphor rules.
- Imagery rules and when illustration is functional.
- Motion rules, durations only when known, and reduced-motion fallback.
- Component variant mapping and explicit anti-patterns.

Component variants must be derived from this contract. Do not independently choose pill tabs, glass cards, gradient buttons or soft shadows because they are fashionable.

## Real-content stress test

Before finalizing the direction, run the visual system against content that can break it:

- Long and short titles, names, labels and localized text.
- Large and small numbers, missing values and long status labels.
- Empty, loading, error, partial failure, permission and unsaved states.
- Long tables, deep navigation, many tags and dense filters.
- Narrow screens, zoom, keyboard focus and reduced motion.

Record what changed after the stress test. A direction that only works with short placeholder content is not ready.
