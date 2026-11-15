# Visual Stability and Performance

工程质感包含“内容出现前后是否稳定”。把允许的业务重排和意外位移分开。

## 1. 稳定尺寸

- 图片和视频提供固有尺寸或比例，避免加载后卡片变高。
- 字体 fallback 要检查宽度、行高和数字；必要时使用 metric-compatible fallback、`size-adjust` 或 font metric overrides。
- Skeleton 与真实内容使用接近的结构和高度；不要用一个短灰块代替最终复杂布局。
- Field 预留稳定 help/error slot；错误出现后不应把用户焦点和下一控件无理由推走。
- 异步卡片、懒加载、广告和虚拟列表提前提供合理占位或测量策略。

## 2. 动画与合成

- 优先对明确的 transform/opacity/clip 属性做动效，不使用无边界的 `transition: all`。
- 不要用 `will-change` 给所有元素制造合成层；只在真实变化且经过验证的元素上使用。
- 动画中定义 hit-testing、焦点、取消/反向和退出后的 unmount 时机；透明元素不能继续挡点击。
- 大面积 blur/backdrop-filter、频繁 layout read/write、滚动中同步测量和高频 resize 需要性能验证。
- Respect `prefers-reduced-motion`；降级后仍保留状态和方向。

## 3. 指标边界

可使用 CLS、INP、LCP 或项目 RUM 观察视觉稳定和响应，但阈值会随官方指标版本和产品环境变化；报告具体测量条件、分位数和样本，不把某个数字当作所有 UI 的硬门槛。静态截图不能证明没有 layout shift 或性能问题。

