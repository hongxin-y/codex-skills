# Skill acceptance scenarios

These are prompts and expected design behavior, not automatically executed tests.

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
