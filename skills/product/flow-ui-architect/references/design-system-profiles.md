# Design system profiles

## How to use profiles

A design system is a source of interaction, token and component knowledge, not a visual theme to copy blindly. Select the parts that fit the task and repository. If the project already uses one, preserve its primitives and document any brand-level expression layered above it.

| System/profile | Borrow for | Do not infer |
| --- | --- | --- |
| Material 3 / Expressive | Semantic color roles, shape, elevation, motion, adaptive and broad component coverage | That every product should look like a default Material demo |
| Apple HIG / materials | Platform-native behavior, Dynamic Type, device adaptation, navigation/control materials and touch expectations | That translucent materials belong on every content surface |
| Fluent 2 | Neutral/shared/brand palette, productivity hierarchy and desktop/web semantics | That acrylic or Microsoft-specific appearance is required |
| Carbon | Data-heavy operations, modularity, accessibility, table/form discipline and product extension | That every B2B page needs KPI cards or a Carbon clone |
| Ant Design | Enterprise workflows, certainty, modular components and structured data patterns | That an Ant component choice determines the art direction |
| Atlassian | Tokens, content, navigation, component semantics and product-wide consistency | That every available component is current or appropriate |
| Spectrum | Creative-product foundations, adaptive expression and cross-product consistency | That creative tools require decorative effects |
| Polaris | Merchant/admin workflows and commerce patterns | That commerce implies a particular color or style |
| GOV.UK / USWDS | High-trust information architecture, plain content and accessibility discipline | That public-service density fits every audience |

Write the relationship explicitly:

Design system foundation = behavior, tokens and reusable mechanics.
Art direction = typography, grid, density, surface, shape, imagery, icons and motion.
Existing repository = engineering and product constraints.

These three layers can collaborate but should not be conflated.
