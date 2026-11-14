# Example: B2B order operations workbench

## Request

“设计一个运营每天处理大量异常订单的后台，能快速审核、备注、转交和处理下一单。”

## Inference

Actor: operations specialist, possibly supervisor.
Objects: order, exception, customer, payment/fulfillment state, notes, assignee and audit trail.
Outcome: safely resolve or escalate eligible exceptions while retaining queue context.

## Layout

Choose a queue/table workbench with contextual detail panel. Monitoring metrics are secondary to processing records.

## Blueprint

~~~text
┌─────────────────────────────────────────────────────────────────┐
│ 订单工作台                     搜索订单 / 客户         用户通知    │
├─────────────────────────────────────────────────────────────────┤
│ 状态  异常类型  负责人  时间范围        保存视图 / 清除筛选       │
├────────────────────────────────┬────────────────────────────────┤
│ 订单队列                       │ 当前订单详情                   │
│ 编号  异常  优先级  时长  状态   │ 订单摘要 / 风险 / 历史         │
│ ...                            │ 处理依据和备注                 │
│ ...                            │ [批准] [转交] [暂缓]           │
│                                │ 操作反馈 / 处理下一项          │
└────────────────────────────────┴────────────────────────────────┘
~~~

## Behavior

Selecting a row updates detail while preserving filters, sort and list position. Actions depend on current state and permissions. Success updates the row and counts and exposes the next eligible item. Failure retains notes and selection.

Desktop uses simultaneous queue and detail. Mobile uses focused detail with preserved return context.

## Cost hypothesis

Reduced repeated search, context switching and memory burden. Confirmation remains when risk warrants it. No invented measured time savings.

## Implementation

Reuse existing components, label mocks, and verify selection, filters, success, failure, focus and responsive behavior.
