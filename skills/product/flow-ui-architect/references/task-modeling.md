# Task modeling from a brief

## Objective

Infer enough of the product to choose a useful interface without turning every short request into a questionnaire. Identify whether users want to find, understand, compare, decide, act, create or explore before prescribing a workflow.

## Model the task

For each meaningful user job, identify:

- Intended user and any relevant permission boundary; not every product needs multiple roles.
- Trigger, user intent and expected outcome or experience criterion.
- Relevant objects or content and any states the product actually needs.
- Actions, prerequisites, consequences and reversibility.
- Information required at decision time.
- Feedback and a useful continuation or exit when appropriate.
- Exceptions, interruption and recovery.
- Device, collaboration and technical context.

Use USER, REPO, EVIDENCE and ASSUMPTION distinctions. Ask only when an unknown materially changes risk, permissions or business correctness.

## Establish feature value

For a proposed page, control or chart, identify the user problem, who experiences it, frequency, information needed, consequence and recovery cost. Check whether existing capabilities already support the goal. Do not add a new feature solely because its component is available.

Distinguish the business object from its execution attempts, versions, states and views. Keep operation scope clear: current item, selection, all matching items or a whole container. Introduce only the distinctions the actual product needs.

Choose an observable success criterion appropriate to the intent. A reader may need to understand and find a source; a shopper to compare terms and choose confidently; a creator to iterate without losing work. Do not claim these outcomes were measured unless testing occurred, or force a submit/complete event into every experience.

## Derive routes from objects

Model:

Trigger → locate object → inspect state → decide → act → feedback → continue or recover.

For multi-page products, extend this into a route graph with page transitions and state handoffs. The same route may cross pages; a page may participate in several routes.

## Select Red Routes adaptively

A Red Route is a critical end-to-end job, not a fixed screen sequence. Select routes by frequency, user value, impact, time sensitivity, risk and dependency relationships. Do not prescribe a count.

Include low-frequency, high-risk routes when necessary. Exclude decorative routes that do not follow from the business context.

## Page mode

- Operate: repeated manipulation, triage, processing and recovery.
- Persuade: comparison, trust, evaluation and conversion.
- Read: search, understand and reference information.
- Experience: create, explore, learn or engage.

A product can contain different modes on different pages, and a page can mix intents. Select the dominant mode and preserve the supporting ones. A comparison page may need more reading time, and a creative tool may need open input and experimentation; lower time or fewer actions is not automatically a better result.

Use [scenario-extensions](scenario-extensions.md) only when collaboration, editing, long-running execution, bulk work or consequential actions are present. Reading, discovery and simple consumer pages do not inherit those workflows by default.

## Example

Request: “做一个客服处理退款的后台。”

Likely actor: support agent, with possible supervisor escalation.
Object: refund request linked to order and payment.
Task: review eligibility, decide, execute or escalate, then continue.
Required context: customer, transaction, policy, history and risk signals.
Likely layout: queue and contextual detail.
Critical unknown: actual refund authorization and irreversible settlement rules.

Do not invent the company's refund policy.
