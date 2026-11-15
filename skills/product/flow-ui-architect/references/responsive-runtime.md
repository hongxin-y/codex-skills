# Responsive Runtime

响应式工程验证的是运行时可用空间和输入环境，不只是 viewport 宽度。

## 1. 运行时变量

- 桌面/移动浏览器的 layout viewport、Visual Viewport、软键盘和地址栏可能不同。
- 移动布局需要根据任务选择 `svh`、`lvh` 或 `dvh`，不能假设 `100vh` 永远等于可见区域。
- 底部 Sheet、输入栏和固定工具栏处理 `env(safe-area-inset-*)`；键盘打开和关闭后验证恢复。
- 侧栏内组件根据 container width 和内容压力变换，不能只看全局 viewport；适用时使用 container query。
- RTL、200%/400% zoom、最小字体和超宽屏都属于响应式输入。

## 2. 转换与状态

沿用 `resize → compact → rail → drawer/sheet → dedicated page`，但每个转换必须保留当前对象、选择、筛选、排序、草稿、错误、任务阶段和返回焦点。横竖屏、断点附近 resize 和容器重建不得重置业务状态。

触控环境不能把关键操作只放在 hover；粗指针下优先提供持久或点击入口。二维表格、地图、时间线等有本质二维关系的内容可以保留局部双向滚动，但要提供优先列、聚焦、缩放或替代查看策略。

## 3. 运行时验收

至少检查：窄手机、常用手机、平板、小笔记本、桌面和超宽屏；100/125/200/400% zoom；鼠标、键盘、触摸和混合输入；长文本、CJK、RTL、emoji、异步、错误和权限差异。不要做无边界的全笛卡尔积，按 Red Route 和组件风险选核心覆盖与 pairwise 组合。

