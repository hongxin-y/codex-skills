# Component Engineering Checklists

组件外观通过视觉语法决定，工程行为通过以下清单决定。只检查与当前产品相关的组件，但每个出现的组件都要标记 DONE、N/A 或 BLOCKED。

| 组件族 | 必查工程问题 |
| --- | --- |
| Button / IconButton / Group | 命中区、文案增长、loading 不改尺寸、icon optical alignment、disabled/aria-disabled、focus、pressed、组内边框 |
| Input / Textarea / Field | label/help/error 所有权、长值、IME、autofill、密码管理器图标、resize、focus 裁切、错误 slot |
| Select / Combobox / Autocomplete | anchor、键盘模型、IME、异步结果、空/加载、滚动跟随、expanded/controls、移动键盘 |
| Checkbox / Radio / Switch | label 命中区、checked/indeterminate、forced colors、键盘和 disabled 语义 |
| Slider / Drag | 键盘与非拖拽替代、touch-action、值反馈、RTL、min/max |
| Tooltip | hover+focus、只承载补充信息、collision flip、延迟、pointer transit、不承载关键操作 |
| Popover / Dropdown / Menu | outside press、Escape、Portal、collision、焦点所有权、滚动更新、嵌套菜单 |
| Modal / Dialog | top layer/portal、scroll lock、focus trap、return focus、Escape、backdrop、移动键盘、嵌套策略 |
| Drawer / Sheet | inline/overlay、body scroll、sticky footer、safe area、背景交互、return focus |
| Toast / Snackbar / Banner | 不遮焦点、队列、live region、持久错误不使用短 toast、底部占用协调 |
| Sidebar / Navigation | 收缩条件、active state、折叠项 tooltip、scroll region、footer pinning、RTL |
| Tabs / Accordion | roving focus、selected state、panel persistence、动态高度、deep link、错误可见性 |
| Card / List | spacing ownership、长内容、空状态、嵌套点击、可伸展交互区 |
| Table / DataGrid | intrinsic width、sticky 层、resize、虚拟化、键盘 grid、截断、RTL、焦点 |
| Virtual list | 测量缓存、overscan、focus retention、scroll restoration、动态行高和失效 |
| Kanban | 拖拽替代、autoscroll、drop indicator、虚拟化、键盘操作 |
| Form / Wizard | error slot、未保存保护、focus first error、状态持久化、异步校验 |
| Chart / Canvas / Map | resize/DPR、可访问摘要、overlay 控件、缩放/手势竞争 |
| Editor / Code block | nested scroll、sticky toolbar、selection overlay、IME、异步语法加载 |
| Chat composer | visual viewport、safe area、autosize、流式输出、follow-bottom 规则 |
| Floating button / Assistant | collision budget、拖动可选替代、safe area、键盘可达、非遮挡、面板锚定 |

## 交付规则

不要只写“组件可用”。对每个组件指出最可能的几何、层叠、命中、焦点、内容或平台风险，以及对应的回归方法。

