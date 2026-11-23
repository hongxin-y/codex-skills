# Flow UI Architect V2.7

A Codex Skill for turning a short product scenario into a coherent, intent-appropriate, visually intentional and implementable UI across websites, consumer apps, creative tools and operational products.

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
- 使用 $flow-ui-architect 设计一个适合阅读和查找资料的科普页面。
- 使用 $flow-ui-architect 改善套餐比较或自由创作工具的体验。

## V2.5: intent-led rules and conditional scenarios

Choose evaluation criteria from the user's intent: finding/understanding, comparison/decision, operation/transaction, creation/expression or exploration. Do not force every product into a queue, linear workflow, approval or final submission.

The execution protocol now begins with function scope and relationships. Core decisions include feature value, coherent navigation concepts, actual capability/result semantics and the requested change boundary. Conditional references cover input/default/disclosure choices, information integrity and scenario-specific collaboration, editing, long-running, bulk or consequential actions. Read them only when their trigger exists.

Discussion-only reviews do not authorize edits. Visual-only work preserves interaction and data behavior, including behavioral effects of CSS. Acceptance scenarios include reading, consumer comparison, creation and discovery as well as operational work.

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

V2.4 adds a mandatory UI Engineering Quality Gate. The agent creates an Engineering Blueprint for major regions and shared primitives: layout and intrinsic sizing, spacing ownership, overflow and scroll ownership, containing blocks, stacking contexts, Portal/top-layer, overlay collision, focus and hit testing, long-content/i18n/RTL behavior, async size stability, dynamic viewport and safe area, asset metrics, motion/compositing and browser validation. BUILD may start implementation only after the pre-build blueprint; it cannot declare completion until runtime overflow, overlay, focus, hit-testing, responsive, async and platform checks are rerun against the actual browser. Screenshots and rendered components are evidence, not proof of production readiness.

V2.6 adds a mandatory generated reference image gate for visual DESIGN, BUILD and visual changes in REVIEW. The agent uses the Image Generation capability to produce `V0`, then at least two targeted revisions `V1` and `V2`, recording prompts, changed decisions, review findings, rejected versions and approval. Only after the reference is approved can it complete the remaining spatial, layout, visual, engineering and pre-code validation steps; only then may BUILD write UI code. If image generation, inspection or approval is unavailable, the gate is BLOCKED and screenshots, HTML previews or text-only moodboards cannot substitute for it. After implementation, real screenshots and runtime behavior are compared with the approved reference.

V2.7 adds a function-first and decision-deliberation gate. Before page, navigation, component or visual decisions, the agent builds a function inventory, typed relationship graph, canonical action ownership map, user-habit hypotheses and frontend information map. Before every step is marked DONE, it records evidence, meaningful candidates, representative-user simulations, downstream consequences, a falsifying counterexample, confidence and verification. A page cannot be justified by a feature count, and a one-line preference cannot close a decision.

See SKILL.md for the operating instructions.
