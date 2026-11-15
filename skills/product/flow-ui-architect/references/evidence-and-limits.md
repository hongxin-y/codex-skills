# Evidence and limits

## Evidence hierarchy

1. Explicit user requirements and business constraints.
2. Repository facts, existing UI behavior and product data.
3. Relevant standards and credible research.
4. Domain-informed design heuristics.
5. Clearly labeled assumptions.

Do not claim external research or usability testing that was not performed.

## Authoritative references

- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- WAI-ARIA Authoring Practices: https://www.w3.org/WAI/ARIA/apg/
- Material Design: https://m3.material.io/
- Apple Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines/
- Nielsen Norman Group usability heuristics: https://www.nngroup.com/articles/ten-usability-heuristics/
- Nielsen Norman Group visual design and component guidance: https://www.nngroup.com/articles/principles-visual-design/
- GOV.UK Design System: https://design-system.service.gov.uk/
- Microsoft Fluent 2: https://fluent2.microsoft.design/
- IBM Carbon: https://www.carbondesignsystem.com/
- Adobe Spectrum: https://spectrum.adobe.com/
- Baymard research: https://baymard.com/research
- OpenAI Skills: https://github.com/openai/skills

Use the relevant source for each claim. Platform conventions are not universal mandates.

## Heuristics, not laws

- A fixed number of Red Routes or pages.
- Exactly one primary CTA per page.
- A universal click ceiling.
- A fixed number of tabs or disclosure levels.
- A mandatory 60/30/10 palette ratio.
- Universal F/Z scanning.
- A fixed typography-size count.
- Universal color psychology.
- A visual trend is not a complete art direction.
- A design system is not a visual theme to copy wholesale.
- A candidate direction is not better merely because it is more expressive.
- “AI look” is a diagnostic category, not a formal usability score.
- Mandatory FAB, modal, wizard or dashboard.
- A fixed number of Review/Repair cycles.
- A single “space utilization” or density score that claims to summarize all layout quality.
- Treating V0–V4, lifecycle formulas or occlusion budgets as universal measurements; they are decision scaffolds and must be adapted to the task.
- Inferring a user's psychology as certainty. Use observed task frequency, criticality, context dependency, recovery cost and content evidence; label psychological predictions as hypotheses.
- Treating `z-index` tokens, Overlay Collision Budget, spacing ownership, Engineering Blueprint fields or browser matrices as Web standards; these are project governance models built on browser mechanisms.
- Treating a screenshot, component render or automated axe result as proof of runtime correctness; scroll, hit testing, focus, real mobile keyboard and cross-browser behavior still need appropriate checks.

Keep numbers when they are actual measured data, necessary business constraints or applicable standards. Remove arbitrary quotas rather than replacing them with different arbitrary quotas.

## Limits

A plausible design is not the same as a user-tested design. A reviewed blueprint is not the same as a verified implementation. State what was actually checked.

Art-direction judgments should distinguish observable usability or system-consistency defects from art-direction weaknesses and subjective taste. Color/emotion evidence supports associations, not guaranteed behavior or conversion. The attached research report is a source for these boundaries, not an instruction to cite or browse every source during a task.

Spatial heuristics likewise do not prove efficiency. A layout with more visible content may increase comparison speed, or may overload attention; verify with task completion, error, backtracking, focus, scroll, restore and accessibility evidence when available. “Anti-AI” is a repair lens based on observable repetition, generic content and missing product semantics, not a claim about the model's internal preferences.

Engineering guidance distinguishes [规范] browser/accessibility requirements, [浏览器] implementation behavior, [框架] lifecycle behavior, [设计系统] mature conventions and [综合] project heuristics. `min-width:0`, `minmax(0,1fr)`, Portal/top-layer selection, dynamic viewport units, collision middleware, screenshot thresholds and runtime probes are decisions that depend on the content contract and target platform. Record the platform, viewport, input mode and evidence for any claim of stability.
