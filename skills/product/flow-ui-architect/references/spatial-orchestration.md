# Spatial Orchestration

空间编排是任务建模之后、详细布局之前的强制决策层。空间不是装饰容器，而是用户在当前任务中分配给内容、参考、导航、工具、状态和恢复动作的有限资源。

## 1. 先拆空间角色

为每个页面区域和主要浮层标记以下角色。一个区域可以有多个角色，但必须说明主角色和次角色：

| 角色 | 说明 | 默认判断 |
| --- | --- | --- |
| Task Area | 用户完成当前目标的主工作面 | 必须保持最高可见性和最大连续空间 |
| Reference Area | 用户反复对照的上下文、来源、预览或历史 | 高频对照时持久化，低频时可折叠或按需打开 |
| Navigation Area | 进入对象、页面、工作区和层级 | 高频切换时持久，低频或窄屏时转为抽屉/菜单 |
| Tool Area | 编辑、筛选、批量操作、快捷命令 | 依赖上下文；随对象或选择状态显示 |
| Status Area | 状态、进度、同步、错误和权限 | 会影响决策时必须可见，短暂反馈才用瞬时层 |
| Transient Layer | Tooltip、Popover、Toast、Modal、命令面板等 | 只在触发后出现，不抢夺不需要的空间 |
| Breathing Space | 分组、节奏、阅读和视觉恢复空间 | 用于建立层级，不得压缩关键任务区域 |

每个区域都要回答：它服务哪个任务、用户多久需要它、隐藏后用户损失什么、重新打开的成本是多少。

## 2. 选择布局骨架

用任务关系选择骨架，并至少记录一个被拒绝的替代方案。不要先选“看起来像产品”的模板。

| 任务关系 | 优先骨架 | 适用信号 | 风险检查 |
| --- | --- | --- | --- |
| 单一连续任务 | Single Column | 阅读、表单、设置、线性确认 | 是否需要持续参考或并列比较 |
| 稳定导航 + 主内容 | Left Nav + Content | 页面切换频繁且内容独立 | 导航是否占据过多首屏宽度 |
| 对象列表 + 当前对象 | Master–Detail | 反复浏览、查看、处理对象 | 选中态、返回列表、窄屏转化 |
| 导航 + 对象列表 + 检查器 | Three Pane / Workbench | 高密度生产、分析、管理台 | 三列是否挤压主任务和键盘焦点 |
| 大画布 + 工具 | Canvas + Edge Tools | 设计、地图、编辑器、监控 | 工具是否遮挡画布和关键控件 |
| 多指标并列 | Dashboard Grid | 监控、概览、比较 | 是否存在主任务；避免平均分配空间 |
| 行级扫描和批量动作 | Table Workbench | 筛选、排序、批量处理 | 行密度、固定列、横向滚动和错误定位 |
| 有顺序的多步任务 | Wizard / Stepper | 前置条件强、阶段性提交 | 是否能安全回退、保存和恢复 |
| 沉浸式单对象 | Immersive | 播放、阅读、演示、聚焦编辑 | 返回、状态、退出和辅助操作可达 |

如果没有骨架能同时满足任务和约束，明确记录 `Hybrid` 的组合关系、每个区域的主权和窄屏转换方案。

## 3. 做空间预算而不是只说“紧凑/宽松”

记录以下变量的方向和证据；没有必要伪造精确数值：

- `main_task_visible_area_ratio`：主任务区域在可视空间中的占比。
- `critical_info_above_fold_ratio`：决策所需信息在首屏可见的比例。
- `persistent_reference_visibility`：重复参考内容是否持续可见。
- `navigation_round_trips`：完成一次任务需要离开主任务区域多少次。
- `scroll_distance`：关键内容、错误和操作之间的滚动负担。
- `occluded_interactive_area`：浮层、固定栏和面板遮挡的可交互面积。
- `context_restore_time`：收缩/切换/返回后恢复上下文的时间。
- `responsive_overflow`：缩窄或放大后是否溢出、截断或丢失语义。

不要把这些变量合成为一个“空间利用率分数”。先说明哪一个变量是当前任务的瓶颈，再决定收缩、重排、转层或增加空间。

## 4. 每个区域必须有生命周期

为每个主要区域、面板、浮动元素、筛选器、助手和反馈层写出：

```text
role → priority → frequency → criticality → context dependency
→ default visibility → expandability → auto-collapse policy
→ dismissal policy → pin/remember policy → responsive transformation
→ occlusion budget → state restore → canonical action owner
```

若字段不适用，也要写 `N/A — <具体原因>`。不得以“组件简单”“页面只有一屏”“使用现成组件”为跳过理由。

## 5. 容器不够时的升级路径

当信息或操作无法在当前容器中保持清晰、可达和不遮挡时，按语义升级：

`Tooltip → Popover → Drawer/Side Panel → Dedicated Page`

Tooltip 只解释短语；Popover 承载短小、局部、可快速关闭的内容；Drawer/Panel 承载需要连续查看或编辑的上下文；Dedicated Page 承载复杂、可分享、可恢复或需要独立导航的任务。不要用一个弹窗解决所有空间压力。

## 6. 必须留下的空间决策记录

每个页面交付中至少包含：

1. 空间角色图和布局骨架。
2. 每个主要区域的生命周期表。
3. 空间瓶颈变量与保留/收缩/转层理由。
4. 窄屏和内容超长时的转换顺序。
5. 被拒绝的一个布局或容器方案及原因。

