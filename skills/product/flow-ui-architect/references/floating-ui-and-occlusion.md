# Floating UI and Occlusion

浮动层是可用性预算，不是免费的空间。每个页面要列出浮动元素、触发器、层级、占用区域、关闭方式和遮挡预算。

## 1. 浮动元素分类

FAB/speed dial 用于跨页面主要动作；floating/context toolbar 用于当前选择；popover 用于局部内容；tooltip 用于解释；drawer/panel 用于连续工作；modal 用于阻断决定；PiP/mini player 用于持续媒体；assistant/chat bubble 用于持续帮助。组件名称不能替代角色和生命周期判断。

## 2. 浮动预算规则

- 同一视口不要同时堆叠 FAB、聊天气泡、sticky bar、tooltip、popover 和未处理的 toast。
- 不遮挡主操作、当前焦点、输入光标、错误信息、选中对象或安全区域。
- 需要比较或输入的内容优先使用面板/页面，而不是覆盖主任务的弹层。
- 叠层必须有稳定的 z-index 规则、Esc 关闭顺序和点击外部行为。
- 触摸目标、键盘路径和屏幕阅读器顺序不能因为浮层出现而失去语义。

## 3. 悬停、焦点和模态约束

Hover/focus 内容必须可被键盘触发；用户可以移动到内容上而不消失；有关闭方式；焦点不会被遮挡。Modal 要把焦点移入、限制在模态内、支持 Escape（除非不可逆流程明确禁止）、关闭后返回触发源。工具栏和菜单要定义箭头键、Tab、Home/End 和读屏状态。

## 4. 遮挡验收

记录 `occluded_interactive_area`、被遮挡的关键控件、最大连续显示时间和替代容器。若遮挡不可接受，按 `Popover → Panel/Drawer → Page` 升级，不要通过更高 z-index 掩盖问题。

