# UI Engineering Foundations

## 1. 用五层定位问题

遇到“看起来不对”时按顺序区分：

1. **Layout**：正常流、包含块、格式化上下文、Flex/Grid intrinsic sizing。
2. **Paint**：背景、边框、阴影、伪元素、变换后的视觉足迹。
3. **Stacking / compositing**：stacking context、layer、合成和裁切。
4. **Hit testing**：pointer-events、透明层、伪元素、pointer capture 实际接收事件的位置。
5. **Accessibility tree**：名称、角色、状态、焦点顺序可能与视觉树不同。

提高 `z-index` 只可能解决很小一部分 stacking 问题，不能修复布局、裁切、事件目标或焦点。

## 2. Spacing ownership

- sibling 之间的距离由父级 Stack/Grid/Toolbar/Section 统一拥有。
- 组件只拥有内部 padding 和内部节奏。
- Field 拥有 label → control → help/error 的垂直节奏。
- Group/Segmented/InputGroup 拥有成员拼接、共享边框和圆角。
- 不让相邻组件分别写外部 `margin-left/right` 猜测关系；变体会因此产生双间距和组合爆炸。

每个布局区域记录 `spacing_owner` 和 `sibling_spacing_source`。

## 3. Intrinsic sizing 与收缩

- Flex 子项默认自动最小尺寸可能来自内容；长 URL、nowrap、表格、代码和大图片会撑宽。
- 需要可收缩的主内容通常要验证 `min-inline-size: 0`；纵向 flex 滚动子区通常要验证 `min-block-size: 0`。
- Grid 的 `1fr` 也可能保留自动最小尺寸；需要可收缩时验证 `minmax(0, 1fr)`。
- 不要机械地给所有元素清零最小尺寸；金额、日期、图标按钮、关键标签和可读控件应保留内容契约中的最小尺寸。
- `transform` 不参与正常布局让位；动画或缩放后的视觉位移需要额外检查邻居重叠。

## 4. 视觉足迹与基线

```text
visual footprint ≈ border box + shadow/glow + outline + pseudo-elements + transform displacement
```

布局中的 16px gap 不保证视觉上有 16px 呼吸空间。检查阴影扩散、粗边框、背景相似度、圆角拼接和变换后的邻居。

文字、CJK、emoji、SVG viewBox 和 icon stroke 的 ascent/descent 不同；Button 的 icon+label 应作为一个对齐组处理。数字表格在需要比较时考虑 tabular numerals。使用截图和真实字体验证，不用 `align-items:center` 作为所有基线问题的通用答案。

## 5. Overflow policy

每个容器回答“内容增长后发生什么”，并选择一种策略：`visible-content`、`wrap`、`truncate-one-line`、`clamp-summary`、`scroll-inline`、`scroll-block`、`scroll-both` 或 `clip-decorative`。关键内容不应无说明地截断；装饰可以裁切，交互和焦点不能被裁掉。

