# Color strategy catalog

## Choose a palette architecture

Start from semantic roles and usage conditions, then choose a palette strategy. Do not start with a favorite hue.

| Strategy | Structure | Useful when | Risk |
| --- | --- | --- | --- |
| Monochromatic | One hue with controlled lightness/chroma | Professional tools and strong brand consistency | Weak hierarchy if all roles are too similar |
| Neutral plus accent | Large neutral foundation and restrained brand accent | SaaS, admin, finance and productivity | Safe but easily generic |
| Tonal | Related tonal roles across surfaces | Mobile and Material-like products | Every container becomes a colored card |
| Analogous | Neighboring hues | Wellness, content and warm lifestyle products | Brand hues can collide with status semantics |
| Complementary | Opposing hues with controlled area | Campaigns, sports and expressive brands | High chroma across large areas causes fatigue |
| Split complementary | One hue with two near-opposite accents | Expressive products needing contrast with control | Still needs strict area and status separation |
| Triadic | Three separated hues | Education, children, creative and categorical data | Easy to become a rainbow dashboard |
| Tetradic | Two complementary pairs | Strong brand systems and complex categories | Usually too complex for UI chrome |
| Warm dominant | Warm neutral or accent | Food, hospitality, lifestyle and community | Status colors need extra separation |
| Cool dominant | Cool neutral or blue-green family | Technical, productivity and health data | Easily becomes generic tech |
| Low chroma | Mostly muted colors with limited accent | Premium, professional and long sessions | Can become gray and weak without contrast |
| Selective high chroma | Neutral base with a few saturated focal roles | Creator, entertainment and expressive consumer products | Too many accents destroy focus |

## Decision sequence

Business risk → session duration → content density → brand personality → image/content palette → light/dark context → palette strategy → semantic roles → component roles → contrast verification → color-blind redundancy.

Use neutral roles to establish structure. Reserve brand accent for intentional focus, selection and action. Keep success, warning, danger and info mappings independent from decorative brand color.

## Semantic and dark-theme rules

- Keep primitive, semantic and component token layers separate.
- Pair surfaces with foreground or on-surface roles.
- Dark mode is a semantic remapping, not a light-theme inversion.
- Recheck hover, pressed, selected, disabled and focus states in both themes.
- Do not let a palette strategy override WCAG contrast or non-color status cues.
- Color/emotion research supports associations, not guaranteed behavior or conversion.

## Output

Record the chosen palette strategy, rejected strategies, semantic roles, dark-theme mapping, status separation and contrast checks. If the existing project already owns tokens, map the visual direction to them instead of creating a parallel palette.
