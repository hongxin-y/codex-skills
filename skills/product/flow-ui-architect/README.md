# Flow UI Architect V2.1

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

See SKILL.md for the operating instructions.
