# Image Reference Iteration Gate

这是视觉决策和实现之间的强制门禁。它把 Visual Context Profile、Visual Grammar Contract、空间编排和真实内容压力转成可观察的视觉参考图，再通过多轮生图和评审收敛；参考图确认前不得写 UI 代码。

## 适用范围

- DESIGN：必须生成并迭代参考图，再交付页面蓝图或原型。
- BUILD：必须先完成参考图门禁、设计流程和工程蓝图，再开始写 UI 代码。
- REVIEW：如果任务包含视觉重设计或视觉修复，必须重新生成/迭代参考图；纯逻辑、数据、性能或非视觉 bug 才能写 `N/A — no visual decision is changing`。

如果生图能力不可用、无法查看生成结果或无法记录版本，状态必须是 `BLOCKED`，不得用 HTML 截图、组件预览或文字描述冒充参考图，也不得绕过门禁开始编码。

## 1. 生成前输入

先完成并读取相关参考：

1. `visual-direction-selection.md`：Visual Context Profile 和 Visual Grammar Contract。
2. `user-perception-and-visual-decisions.md`：用户心理假设、可观察信号和反风险。
3. `spatial-orchestration.md`：空间角色、布局骨架、密度和动态层级。
4. `component-style-grammar.md`、`typography-and-grid.md`、`surface-shape-depth.md`、`imagery-iconography-motion.md`：视觉表达约束。

把以下内容写入每次生图的 prompt/记录：产品类型、主要用户和任务、主/次焦点、布局骨架、密度、表面/层级、颜色策略、字体角色、组件表达、内容类型、设备和必须避免的模板化特征。不要只写“高级、现代、有设计感”。

## 2. 使用生图能力

- 使用可用的 Image Generation 能力生成视觉参考图；不要先用代码画一个临时页面再把它当作参考图。
- 新图从零生成时，不携带无关的历史图片；编辑已有版本时，使用对应的本地参考图或当前会话中的目标图，保持版本链可追踪。
- 每个版本记录：版本 ID、生成时间、完整 prompt、输入参考、改变的决策组、评审结果、是否保留。
- 参考图可以是关键页面、工作台、移动状态或组件/表面探索；如果产品有多个页面，先生成共享视觉语言和代表性页面，再覆盖差异页。
- 参考图用于确认视觉方向、空间关系和组件气质，不等于最终可访问、可交互或生产实现；后续仍必须完成工程门禁和浏览器验证。

## 3. 强制迭代序列

至少保留三版可审计结果：初始概念 `V0` + 至少两轮迭代 `V1`、`V2`。即使 V0 看起来已经不错，也必须用后续轮次完成针对性压力测试；不设任意上限，直到关键问题收敛。

| 版本 | 主要目的 | 必查内容 |
| --- | --- | --- |
| V0 — concept | 验证视觉方向和构图是否服务任务 | Visual Context Profile、主焦点、布局骨架、整体气质、非模板化特征 |
| V1 — structure | 修正空间、层级和组件表达 | Task/Reference/Navigation/Tool/Status 关系、密度、阅读路径、收缩/展开、浮层占位 |
| V2 — realism | 用真实压力确认可实现性和质量 | 长短内容、错误/空/加载/权限、长表格、窄屏、动态状态、颜色/对比度、AI 味测试 |
| V3+ — polish | 只在仍有重要问题时继续 | 对齐、节奏、表面、图标、动效、品牌差异、跨页连续性 |

每轮只改变一组可解释的决策（例如空间层级、表面/颜色、组件形态或内容压力），不要一次改完所有方向。保留被拒绝版本和拒绝原因，防止反复回到已淘汰的模板。

## 4. 每轮评审记录

对当前图与上一版逐项记录：

- 任务焦点是否更清楚，用户是否能预测下一步。
- 空间角色、密度、主/次层级和视觉足迹是否符合空间预算。
- 组件样式是否来自 Visual Grammar Contract，是否出现无语义卡片、渐变、玻璃、pill、发光或重复装饰。
- 用户心理假设是否仍有可观察依据，是否引入新的误导、噪声或不安全感。
- 真实内容、异常状态、窄屏和响应式转换是否仍能成立。
- Deletion、Substitution、Real-content 三项反 AI 测试结果。
- 本轮保留、拒绝和下一轮唯一的主要修复方向。

不要用“更好看”“更高级”作为唯一结论；把判断写成任务、语义、层级、真实性、可访问性或工程风险。

## 5. Reference Approval Gate

在进入 Step 6 空间编排、后续布局/工程设计或代码前，必须有一条明确记录：

```text
reference_status: APPROVED | BLOCKED | REVISE
approved_version: V2 or V3+
approval_by: user | agent_after_review
approval_basis: <具体任务、视觉语法、真实内容和反 AI 检查结果>
open_risks: <none or explicit list>
```

`REVISE` 或 `BLOCKED` 时只能继续生图/评审，不能开始代码。用户明确说“先做图再实现”时，`approval_by` 必须标明是否真的得到用户确认；Agent 自己完成的客观检查不得伪称为用户批准。

## 6. 参考图之后、代码之前

参考图批准后仍必须完成现有后续流程：Page Blueprint、空间/动态、布局/交互、成本/连续性、视觉系统、UI Engineering Blueprint、设计 Review/Repair 和预编码验证。参考图不是跳过这些步骤的捷径。

BUILD 的代码门禁同时要求：

- 参考图版本链和批准记录已完成。
- 步骤台账中的所有前置步骤均为 DONE，或有明确 `N/A` / `BLOCKED` 解决计划。
- 预编码评审没有未解决的阻断问题。
- 已记录实现后的截图对照、浏览器运行时、可访问性、键盘/触摸和平台验证计划。

代码完成后，使用实际页面截图和运行时行为对照批准参考图；视觉偏差或工程回归要回到相应步骤修复并再次验证。

