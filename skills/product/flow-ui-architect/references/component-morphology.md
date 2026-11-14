# Component Morphology

组件的外观、容器和交互生命周期是三类不同决策。先按任务关系选组件角色，再选容器，最后从 Visual Grammar Contract 推导视觉变体。

## 1. 按任务角色选组件

| 角色 | 典型组件 | 适用场景 | 不能替代 |
| --- | --- | --- | --- |
| Global navigation | Sidebar、Rail、Top Nav、Menu | 跨页面和工作区移动 | 局部筛选 |
| Local navigation | Tabs、Section Nav、Stepper | 当前对象或流程内切换 | 跨对象主导航 |
| Object browser | List、Table、Tree、Search Results | 定位、扫描和选择对象 | 复杂编辑 |
| Inspector | Form、Property Panel、Detail View | 编辑当前对象属性 | 承载大量对象浏览 |
| Reference | Preview、History、Source、Comparison | 持续对照上下文 | 主任务操作区 |
| Tool | Toolbar、Command Bar、Filter Bar、Context Menu | 对当前对象执行动作 | 持久状态说明 |
| Status | Badge、Progress、Banner、Inline Error | 表达状态、进度、风险 | 唯一操作入口 |
| Feedback | Toast、Snackbar、Inline Message、Dialog | 反馈结果、阻断或恢复 | 长期导航 |
| Transient | Tooltip、Popover、Command Palette、Modal | 触发式、短期辅助 | 复杂且需持续比较的工作 |

## 2. 容器选择规则

- **Sidebar/rail**：用于稳定导航或高频上下文；窄屏优先转为 drawer/sheet。
- **Panel**：用于与主任务并行的检查、预览或属性；必须有明确的占用宽度和关闭后恢复状态。
- **Drawer/sheet**：用于需要连续查看、编辑或筛选但不应永久占用空间的上下文。
- **Popover**：用于局部、短小、和触发源有空间关系的内容；不得放入长表单或关键流程。
- **Modal/dialog**：只用于阻断、确认、权限、不可逆动作或需要隔离的决定；复杂编辑应升级为页面或面板。
- **Toolbar/command bar**：用于当前上下文的动作；动作所有权只能有一个 canonical owner。
- **FAB/speed dial**：只有在一个主要、频繁且跨页面的动作无法自然放入主层级时才使用。
- **Assistant/chat bubble**：只有当用户确实需要持续问答或建议，且有明确入口、状态和退出策略时才使用。

## 3. 外观变体不是组件角色

同一个 Panel 可以使用 solid、bordered、elevated 或 translucent 表面；同一个 Button 可以是 primary、secondary、tertiary 或 destructive。变体必须来自视觉语法中的层级、语义和密度，不得因为“常见”或“好看”单独决定。

组件交付必须同时写清：角色、容器、视觉变体、状态、键盘行为、响应式变换和生命周期。缺一项就不能算完成。

