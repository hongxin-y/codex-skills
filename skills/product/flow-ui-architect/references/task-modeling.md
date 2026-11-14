# Task modeling from a brief

## Objective

Infer enough of the product to choose a useful interface without turning every short request into a questionnaire.

## Model the task

For each meaningful user job, identify:

- Actor and permission boundary.
- Trigger and expected outcome.
- Business objects and their lifecycle states.
- Actions, prerequisites, consequences and reversibility.
- Information required at decision time.
- Completion feedback and next likely job.
- Exceptions, interruption and recovery.
- Device, collaboration and technical context.

Use USER, REPO, EVIDENCE and ASSUMPTION distinctions. Ask only when an unknown materially changes risk, permissions or business correctness.

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

A product can contain different modes on different pages. Model each page according to its actual job.

## Example

Request: “做一个客服处理退款的后台。”

Likely actor: support agent, with possible supervisor escalation.
Object: refund request linked to order and payment.
Task: review eligibility, decide, execute or escalate, then continue.
Required context: customer, transaction, policy, history and risk signals.
Likely layout: queue and contextual detail.
Critical unknown: actual refund authorization and irreversible settlement rules.

Do not invent the company's refund policy.
