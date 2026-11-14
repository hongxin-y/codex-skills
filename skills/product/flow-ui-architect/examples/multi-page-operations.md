# Example: multi-page operations product with Review and Repair

## Request

“设计一个多页面订单运营系统，包含待处理队列、订单详情、分析报表和团队设置，要求处理高效且风格统一。”

## Stage A: Page inventory

- P-QUEUE: operational queue. Owns locating, prioritizing and selecting work.
- P-DETAIL: deep order inspection and complex resolution. Owns canonical decision and action.
- P-ANALYTICS: aggregated performance and drill-down. Owns analysis, not order approval.
- P-SETTINGS: team preferences and authorized configuration. Owns settings, not order processing.

These boundaries are illustrative. If quick actions can safely live in a queue detail panel, P-DETAIL may be a contextual surface instead of a separate route.

## Stage B: Page Element Blueprints

### P-QUEUE

Actor/job: operator finds next eligible order.
Functions: search, filter, sort, select, save view, open detail.
Content: order ID, exception, urgency, owner, state and age.
Red Routes: process exception; escalate exception; resume unfinished work.
Focus: next actionable record and why it needs attention.
Operations: locate → inspect summary → select; count only when specific interactions are defined.
State: loading, empty, filtered-empty, stale, permission.
Handoff: pass order ID and preserve query, filter, sort, scroll and selection.
Ownership: queue and prioritization; not canonical final approval.

### P-DETAIL

Actor/job: authorized operator reviews and resolves a selected order.
Functions: inspect evidence, add note, approve/reject/hold/escalate as permitted.
Content: order, payment, customer, policy, history, decision evidence.
Red Routes: process exception; escalate exception.
Focus: decision evidence and the next valid action.
Operations: inspect → decide → act → feedback; confirmation is conditional on risk.
State: eligible/ineligible, unsaved note, submitting, success, failure, conflict.
Handoff: return to queue with preserved context; update row and counts.
Ownership: canonical decision and mutation.

### P-ANALYTICS

Actor/job: manager understands performance and exceptions.
Functions: filter time period, compare trends, drill into matching records.
Content: volume, backlog, processing time, error categories.
Red Routes: investigate backlog and open affected orders.
Focus: trends and actionable exceptions.
Operations: choose metric/filter → inspect detail → drill into queue.
State: loading, no data, partial data, error.
Handoff: pass analysis filter into queue; provide return context.
Ownership: aggregate analysis; not a second approval workflow.

### P-SETTINGS

Actor/job: authorized administrator configures team preferences.
Functions: assign roles, edit permitted preferences, view audit of changes.
Content: team members, roles, policies and change history.
Red Routes: update team configuration.
Focus: permission-sensitive setting and its consequences.
Operations: select setting → edit → validate → save → feedback.
State: insufficient permission, unsaved changes, conflict, success.
Handoff: return to prior page; propagate relevant setting changes.
Ownership: configuration; not order processing.

## Stage C: Shared contract

Global navigation uses stable labels: 工作台, 分析, 团队设置.
Order statuses have one canonical vocabulary.
The order decision operation is implemented once and reused through shortcuts.
Shared components include search, filters, status badges, feedback, confirmation and form fields.
Semantic tokens define primary, warning, danger, success and focus consistently.

## Stage D: Initial Review findings

Issue R-01 — Significant: queue and detail both implement independent approve logic.
Repair: assign canonical mutation to detail service; queue shortcut calls the same validated action or opens the relevant detail context.
Regression: test permissions, status updates and error feedback from both entry points.

Issue R-02 — Significant: analytics drill-down opens an unfiltered queue.
Repair: encode filter context in navigation state or URL and restore it on arrival.
Regression: test drill-down, back navigation, refresh and deep link.

Issue R-03 — Significant: status “待审” in queue and “处理中” in detail refer to the same backend state.
Repair: unify semantic status mapping and labels.
Regression: inspect all pages, filters, badges and notifications.

Issue R-04 — Improvement: settings page uses a visually different primary button.
Repair: reuse shared button variant and semantic tokens.
Regression: check settings, detail, focus and disabled states.

## Stage E: Repair and re-review

After repairs, rerun:
- Page completeness for P-QUEUE and P-DETAIL.
- Cross-page action ownership and status consistency.
- Red Route: queue → detail → resolve → updated queue.
- Red Route: analytics → filtered queue → detail → back.
- Shared component and accessibility checks.

If a route still loses context, reopen the issue and repair again. Do not claim success without actually validating the design or implementation.

## Exit

The design can proceed when critical routes close, ownership is clear and material duplication or inconsistency is resolved. User testing and runtime verification remain separate evidence requirements.
