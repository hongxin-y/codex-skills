# Color strategy and semantic tokens

Color supports hierarchy, brand character, feedback and accessibility; it cannot replace task design.

## Derive from context

Consider audience, product positioning, environment, content density, existing brand and platform conventions. Do not claim that an industry universally requires a particular color.

## Token layers

Primitive tokens: neutral and hue scales.
Semantic tokens: background, surface, text, border, primary, success, warning, danger, info and focus.
Component tokens: button, input, table, card and navigation states.

Reuse existing project tokens where possible. Avoid raw hex values scattered across components.

## Workflow

Choose a neutral foundation and suitable accent. Separate semantic status from decoration. Define hover, pressed, selected, disabled and focus states. Test foreground/background combinations. Support dark mode where relevant.

OKLCH may help control perceptual color variation, but is not mandatory.

## Accessibility

WCAG 2.2 AA generally requires at least 4.5:1 contrast for ordinary text and 3:1 for qualifying large text. Applicable non-text UI indicators generally require 3:1 contrast against adjacent colors. Evaluate the standard's actual exceptions.

These are evidence-based standards, not arbitrary design quotas.

## Heuristic limits

The 60/30/10 palette ratio is a possible starting point, not a law. Color psychology varies by context and culture. Do not rely on color alone for status.

## Cross-page consistency

Use the same semantic token for the same meaning across pages. A warning, selected state or destructive action must not change meaning because a page has different styling.
