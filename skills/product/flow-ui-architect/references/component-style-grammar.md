# Component style grammar

## Separate the axes

Visual variant is not interaction pattern. Keep these axes independent:

interaction semantics × emphasis × density × shape × surface × material × brand expression

For example, a B2B approval action can be a high-emphasis button with compact density, restrained radius, solid surface, no glass and a brand accent. A consumer play action can use comfortable density, a capsule shape and expressive color. The task semantics stay the same while expression changes.

## Variant selection rules

| Component | Useful variants | Selection logic | Avoid |
| --- | --- | --- | --- |
| Button | filled, tonal, outlined, ghost, text, icon, split | Emphasis and action risk determine variant | Every button filled or several competing primaries |
| Input | bordered, underline, filled, quiet, search field | Form complexity, density and editorial context | Large rounded inputs with placeholder-only labels |
| Select | native-like, bordered, quiet, combobox, searchable | Option count, search need and density | Every selector becoming a pill |
| Checkbox/radio | standard, card-select, tile-select | Use rich tiles only when options need explanation | Turning simple Yes/No into colorful cards |
| Switch | standard, labeled | Immediate binary setting only | Using a switch for a save/confirm workflow |
| Tabs | line, underline, contained, segmented, pill | Parallel views and short filters determine style | Capsule tabs on every page or tabs used as steps |
| Navigation | sidebar, rail, top, bottom, command | Device, module count, hierarchy and frequency | A default desktop sidebar without IA analysis |
| Card | flat grouping, bordered, elevated, tonal, media | Heterogeneous grouping or entry point | Card-inside-card and cards for homogeneous data |
| Table/data grid | borderless, ruled, zebra, dense, comfortable, grouped, tree | Comparison, operation frequency and data hierarchy | Badges, avatars and menus hiding important columns |
| Modal | alert, confirmation, form, content | Short blocking tasks only | Long forms, tables or complex wizards in a modal |
| Drawer/panel | overlay, push, persistent inspector, detail | Preserve parent context during inspection/editing | All deep work forced into a narrow drawer |
| Popover/tooltip | menu, selection, info, contextual, label | Short local clarification or choice | Hiding required information in hover |
| Toast | success, neutral, lightweight error | Non-blocking feedback only | Important recovery instructions that disappear |
| Status/badge | dot, label, soft fill, outlined, icon plus text | Status, category or bounded metadata | Every metadata value becoming a pill |
| FAB/assistant | standard, extended, contextual, embedded | Only when the global action or helper is real | Decorative floating orb added because the product uses AI |
| Charts | line, bar, area, scatter, histogram, stacked, small multiples | Match chart to a specific analytical question | A decorative donut, line and bar trio |
| Empty state | text-only, action-led, illustrative, educational | Cause, next action and user confidence determine it | A large illustration for every empty state |
| Forms | single-column, compact grid, sectioned, progressive, inline | Task sequence and field relationships determine it | Two columns only to look more professional |
| Toolbar | flat, grouped, contextual, sticky, floating | Frequency and selection state determine it | A wall of circular icon buttons |

## Derivation rule

For each important component, write:

component → interaction meaning → emphasis → density → shape → surface/material → brand expression → states.

If a component variant is chosen only because it is fashionable, replace it with a task or visual grammar rationale.
