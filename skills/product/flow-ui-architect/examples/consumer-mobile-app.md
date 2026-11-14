# Example: consumer mobile course booking

## Request

“做一个手机端健身课程预约 App，让用户快速找到合适的课、预约，并方便改期或取消。”

## Task

Actor: member.
Objects: course, instructor, slot, location, booking and cancellation policy.
Outcome: choose a class, confirm availability, book and manage later changes.

## Layout

Discovery/search with course cards and filters, focused detail/slot selection and a bookings area. No default dashboard or FAB.

## Blueprint

~~~text
发现课程
┌───────────────────────────────┐
│ 今天想练什么？                 │
│ [搜索课程 / 教练]              │
│ [日期] [类型] [地点] [难度]     │
│                               │
│ 瑜伽 · 周六 10:00              │
│ 教练 / 地点 / 剩余名额         │
│ [查看时段]                     │
│                               │
│ 力量训练 ...                   │
├───────────────────────────────┤
│ 发现       我的预约      账户  │
└───────────────────────────────┘
~~~

## Continuity

Preserve filters on return from detail. Show booking policy before commitment. On success show booking details and update My Bookings. Handle sold-out, duplicate booking, network failure and cancellation policy conflicts.

Use a sticky bottom action only if it does not obscure content. Provide accessible controls, status labels and contrast.

## Evaluation

Test discovery → selection → booking → confirmation and booking → change/cancel. Verify recovery rather than merely counting taps.
