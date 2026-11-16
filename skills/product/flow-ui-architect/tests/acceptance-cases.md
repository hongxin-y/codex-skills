# Skill acceptance scenarios

These are prompts and expected design behavior, not automatically executed tests.

## Reading and understanding

Prompt: “设计一个帮助新手理解摄影曝光的文章页面，可以看示例和继续阅读。”

Expected: reading hierarchy, understandable examples, discoverable references and preserved reading position. Success concerns comprehension and orientation; no invented assignments, approval stages or mandatory submit/complete button. Supporting navigation need not have one dominant transactional CTA.

## Comparison and informed choice

Prompt: “做一个手机套餐比较页面，让用户看清流量、限速和实际费用。”

Expected: comparable terms, meaningful differences and important conditions visible before choosing. Does not hide limitations in advanced options or claim that faster conversion proves a better user outcome. More reading may be justified by informed choice.

## Open-ended creation

Prompt: “设计一个可以自由写短篇故事、保存和继续修改的工具。”

Expected: flexible expression, an appropriate editor, truthful persistence feedback and recovery. Does not constrain story text to enumerated options or invent reviewer handoffs. Any changed/saved marker has a clear baseline and meaning.

## Exploratory discovery

Prompt: “设计一个独立插画师作品发现页，用户可以浏览、收藏和返回继续看。”

Expected: user-directed discovery, useful previews and navigation with relevant position/selection preservation. No mandatory linear wizard or forced next-item jump after a favorite. Engagement duration alone is not treated as proof of user benefit.

## Input and disclosure choice

Prompt: “设计活动报名表：从目录选已有活动、选择参加时段、填写自由备注，少用不必要的输入。”

Expected: directory-backed choices handle loading/no results; time-slot selection fits option count and availability; notes remain open text. Reliable context may prefill fields. Required fees or conditions remain visible before commitment; secondary settings may collapse without hiding errors. Does not prescribe a dropdown for every field.

## Honest quantities and results

Prompt: “报表显示报名人数、到场率和导出进度，但有些数据还在加载，也有请求失败。”

Expected: unknown/loading/error values are not shown as zero; attendance rate states its applicable scope and denominator when needed. No invented passing target or fake percentage. Export accepted, completed, partially failed and downloaded are distinguished only where those states exist.

## Visual-only change boundary

Prompt: “只调整这个阅读器的字体、颜色和边距，不改任何交互。”

Expected: preserves reading position, navigation, focus, collapse defaults, submission/data behavior and existing resize/scroll semantics. Checks interaction effects of CSS visibility, overflow, order and hit testing. Reports unrelated defects without redesigning the flow or adding a workflow.

## Discussion-only review

Prompt: “先聊聊这个购物页怎么改，不要动代码。”

Expected: observes available evidence, distinguishes hypotheses and proposes concrete tradeoffs. Does not apply repairs merely because the skill includes a repair loop, and does not claim browser or usability verification that was not performed.

## Conditional collaboration

Prompt: “客服主管想看自己要处理的退款，以及同事正在处理的退款；一人处理完不代表整组完成。”

Expected: distinguishes creator, current assignee and authorized actor where relevant; separates actionable work from waiting/monitoring, and personal from group completion. Reading a notification does not finish work. Applies collaboration guidance here without making it a requirement for the reading or discovery scenarios.

## Partial bulk work and consequential action

Prompt: “为相册设计批量导出，可选当前页或全部搜索结果；另有一个付费印刷下单入口。”

Expected: clear selection scope and eligibility, honest partial results, and recoverable export failures without unintended repeated work. Printing shows price, scope and commitment before purchase. Opening settings does not start a paid order; routine reversible selections do not acquire payment-style confirmations.

## Operational workbench

Prompt: “做一个每天批量处理退款审核的后台。”

Expected: queue and decision context, permission/risk safeguards, preserved filters, working next-item flow, no invented click quota.

## Mobile booking

Prompt: “设计一个能快速预约社区课程的手机 App。”

Expected: discovery, availability, booking, manage-booking, sold-out and cancellation states; no FAB by habit.

## High-risk workflow

Prompt: “设计一个财务人员批量审批付款的页面。”

Expected: recipient identity, amounts, authorization, auditability and proportionate confirmation. Does not optimize clicks at the expense of safety.

## Existing repository

Prompt: “把这个项目的订单列表改成更高效的操作台，直接改代码。”

Expected: inspect stack and components, implement actual interactions, run available checks, report real results.

## Multi-page design gate

Prompt: “给我设计一个有订单工作台、客户详情、报表和设置的多页面 SaaS。”

Expected:
- Page inventory before detailed layouts.
- A Page Element Blueprint for every page.
- Functions, content, Red Routes, focal point and operation paths recorded.
- Shared navigation, action ownership, state handoffs and visual contract.
- Cross-page review identifies duplication and continuity problems.
- Repairs are applied to blueprints before final layouts.
- Impacted routes are re-reviewed after changes.

## Cross-page duplication

Prompt: “客户列表和客户详情都有编辑客户的入口，如何处理？”

Expected: distinguish contextual shortcut from duplicate independent implementation. Define canonical ownership, shared validation and consistent feedback. Do not blindly remove all repeated entry points.

## Continuity regression

Prompt: “从报表点击异常订单进入列表，再打开详情，返回后筛选丢了。”

Expected: map state handoffs, repair URL/navigation state or equivalent, verify drill-down and back/refresh paths.

## Review cycle autonomy

Prompt: “系统页面很多，做几轮 Review 和 Repair。”

Expected: cover page, cross-page, route and visual/engineering lenses; maintain issue ledger; repeat until material findings converge; no arbitrary fixed cycle count and no false claim of zero defects.

## Numeric rigidity

Prompt: “复杂多角色系统需要多少 Red Routes 和主要按钮？”

Expected: context-based selection; no universal counts; retains real WCAG standards.

## Review evidence

Prompt: “评审这个页面，告诉我怎么提高转化。”

Expected: distinguish observed problems from hypotheses; propose concrete changes; no invented measured uplift.

## Spatial and dynamic decision gate

Prompt: “做一个三栏的 AI 数据分析工作台，桌面和移动端都要用。”

Expected:
- Reads and applies spatial-orchestration, component-morphology, visibility-persistence, responsive-transformation and floating-ui-and-occlusion.
- Records Task/Reference/Navigation/Tool/Status/Transient roles, a rejected skeleton, the spatial bottleneck and an occlusion budget.
- Assigns V0–V4, collapse/expand, pin/remember and state restoration to every panel, filter, assistant and feedback layer.
- Shows `resize → compact → rail → drawer/sheet → dedicated page` transformations and preserves selection, drafts, errors and focus.
- Does not use a modal or floating assistant as a universal fix for insufficient space.

## Anti-AI visual review

Prompt: “给这个后台做得更高级、更有设计感。”

Expected:
- Builds a Visual Context Profile and Visual Grammar Contract from task and product evidence before selecting colors or components.
- Writes user-perception assumptions as bounded hypotheses with observable signals, counter-risks and verification methods.
- Runs deletion, substitution and realistic-content tests; identifies generic card/gradient/glass repetition as observable symptoms rather than making claims about model psychology.
- Reviews Task fit, Accessibility, Semantic fit, Hierarchy, Authenticity, Coherence, Craft, Restraint and Distinctiveness in that order.

## No-skip compliance

Prompt: “页面很简单，直接给我写代码，不用分析。”

Expected:
- Inspects the repository if building but does not write UI code before the required ledger decisions.
- Marks every inapplicable field with `N/A — <specific reason>` or reports `BLOCKED — <resolution plan>`; never silently omits a decision because the page is small or a component already exists.

## UI engineering quality gate

Prompt: “把一个三栏数据工作台直接实现出来，要求弹窗、表格 sticky、移动端也能用。”

Expected:
- Creates an Engineering Blueprint before implementation with layout/sizing, spacing owner, intrinsic growth, overflow/scroll owner, containing block, stacking/Portal, collision, focus/hit-testing, async stability, responsive viewport/safe-area and validation fields.
- Does not fix overlay problems by adding arbitrary huge z-index values; diagnoses clipping and stacking context first.
- Exercises long URLs, CJK, empty/error/loading states, sticky header/column, narrow width, keyboard, touch and dynamic content.
- Runs or reports browser runtime audit, screenshot/accessibility checks and manual keyboard/touch/overlay checks honestly.
- Defines the actual scroll container and verifies focus visibility, return focus, hit target and last-row visibility under fixed bars.
