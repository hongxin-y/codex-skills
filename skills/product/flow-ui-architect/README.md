# Flow UI Architect V2.3

A Codex Skill for turning a short business scenario into a coherent, task-first, visually intentional and implementable UI.

## Install

Place the `flow-ui-architect` directory directly under a Codex skills directory:

- Personal: `~/.agents/skills/flow-ui-architect/`
- Project: `<repo>/.agents/skills/flow-ui-architect/`

Keep `SKILL.md`, `agents/`, `references/`, `examples/` and `tests/` together.

## Invoke

Use $flow-ui-architect with a business scenario.

Examples:
- 使用 $flow-ui-architect 设计一个运营处理异常订单的后台。
- 使用 $flow-ui-architect 为这个项目实现一套多页面 CRM。
- 使用 $flow-ui-architect 审查现有页面的重复功能和跨页断点，并直接修复。

## V2.1 additions

Multi-page design now follows a mandatory design-and-review gate:

1. Inventory pages, actors, jobs and routes.
2. Produce a Page Element Blueprint for every page before detailed screen design.
3. Establish shared navigation, data ownership, component and visual contracts.
4. Review individual pages, cross-page duplication, complete Red Routes and visual/technical consistency.
5. Repair findings and rerun impacted reviews until material issues converge.
6. Implement or deliver the final blueprint, reporting verified outcomes and unresolved limitations.

The process does not impose arbitrary counts on pages, Red Routes, actions or review cycles. It retains applicable accessibility and technical standards.

Every invocation also uses a step ledger. The agent must read and apply the references routed for each step, produce the required intermediate artifact, and mark a step as N/A or BLOCKED with a reason instead of silently skipping it.

V2.2 adds a mandatory Art Direction Gate after the page blueprint and before detailed styling or code. The agent derives a Visual Context Profile, compares meaningful visual directions when the direction is open, selects a Visual Grammar Contract, derives component variants from it, stress-tests realistic content and runs Art Direction Review/Repair.

V2.3 adds a mandatory Spatial Orchestration Gate before detailed layout. The agent assigns Task, Reference, Navigation, Tool, Status, Transient and Breathing Space roles; chooses and compares a layout skeleton; decides V0–V4 visibility, collapse/expand, pin/remember and state restoration; specifies responsive transformation (`resize → compact → rail → drawer/sheet → dedicated page`); and records floating occlusion and focus budgets. Every major region, panel, filter, assistant and feedback layer must have these decisions, or an explicit N/A reason. The agent must not write UI code until the ledger's decision steps are complete. Visual decisions also record bounded user-perception hypotheses with observable signals, counter-risks and verification methods. Review applies perceived-quality dimensions in priority order and runs deletion, substitution and realistic-content tests to remove generic AI-template signals.

See SKILL.md for the operating instructions.
