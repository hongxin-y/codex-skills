# Overlay and Scroll Engineering

## 1. Stacking / clipping 调试顺序

1. 元素是否真的重叠，还是视觉足迹扩大造成的粘连？
2. 是否被祖先 `overflow`、`clip-path` 或 `contain: paint` 裁切？
3. 元素和遮挡者分别在哪个 stacking context？
4. 谁创建了这些 context，最近共同的 stacking-context ancestor 是谁？
5. 父层的 stack level 和 DOM paint order 如何？
6. 应改 stacking architecture、Portal 或 top layer，还是只需调整 token？

禁止把业务组件的 `z-index: 99999` 当作第一修复方案。使用语义 layer token，例如 `base`、`sticky`、`dropdown`、`popover`、`tooltip`、`backdrop`、`modal`、`toast`、`drag-preview`；具体数字由项目统一映射。

## 2. Overlay contract

每个 Dialog、Drawer、Tooltip、Popover、Menu、Combobox、Toast、FAB 和助手记录：anchor、placement、collision boundary、flip/shift/size 策略、portal/top-layer 策略、Escape owner、outside-press、scroll strategy、focus strategy、return focus 和 safe-area 占用。

定位不是只测一次 `top/left`：anchor 滚动、resize、layout shift 和字体/内容变化后，要重新定位、关闭或升级容器。

### Overlay registration 示例

```ts
type OverlayRegistration = {
  id: string;
  type: "modal" | "drawer" | "popover" | "tooltip" | "menu" | "toast" | "fab" | "assistant" | "banner";
  modal: boolean;
  collisionBoundary: Element | "viewport";
  placement?: string;
  dismissOnEscape: boolean;
  dismissOnOutsidePress: boolean;
  scrollStrategy: "follow" | "close" | "lock" | "independent";
  focusStrategy: "trap" | "move" | "retain";
  returnFocus?: Element;
  safeAreaAware: boolean;
};
```

这是治理模型，不是 HTML 标准；项目可以用框架/库的等价结构。

## 3. Scroll owner、sticky 和 fixed

- 页面、主内容、表格、代码块和 Drawer 分别声明 scroll owner，减少无意义的嵌套滚动。
- sticky 依赖最近的滚动机制祖先和 containing block；先查 ancestor overflow、父高度和裁切，再改 offset。
- fixed/absolute 可能受祖先 transform、filter、contain 或 will-change 改变 containing block 的影响。
- fixed header/footer、cookie banner、底部 tabbar 和 safe area 必须把占用的 inset 提供给内容、焦点和锚点滚动。
- 对 hash、键盘焦点和错误定位使用合适的 `scroll-padding` / `scroll-margin`，避免目标被 sticky 遮挡。

## 4. 复杂表格

Sticky header + sticky first column 是复合组件：定义 body < header < sticky column < corner 的层级；角落单元格背景必须不透明；横向滚动、列宽调整、虚拟化、边框模型和焦点遮挡都要截图/键盘验证。

