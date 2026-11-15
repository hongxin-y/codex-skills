# UI Debug Playbook

先记录症状和复现条件，再按第一检查项排查；不要直接改 CSS 猜答案。

| 症状 | 第一检查 | 常见修复方向 | 回归 |
| --- | --- | --- | --- |
| 元素被遮 | overflow/clip 与 stacking context | 改父层级、Portal/top layer、layer token | 所有 overlay 同开、滚动 |
| z-index 无效 | 最近共同 stacking context | 改 stacking architecture，而非继续加数字 | modal + dropdown + tooltip |
| sticky 无效 | 最近滚动祖先、父高度、overflow | 明确 scroll owner 和 containing block | 嵌套滚动、长列表 |
| fixed 跑偏 | ancestor transform/filter/contain | 移到正确 root 或重构 containing block | zoom、键盘、iframe |
| Flex/Grid 溢出 | 自动最小尺寸和内容贡献 | 有依据地用 `min-width:0`、`min-height:0`、`minmax(0,1fr)` | 长 URL、表格、代码 |
| 两组件粘连/双边框 | spacing owner、视觉足迹 | 父 gap、group border/radius、减 shadow | 1x/2x DPR、zoom |
| 横向滚动 | `scrollWidth/clientWidth` 和 overflow offender | wrap、min-size、独立表格滚动、逻辑属性 | 320px、RTL、长本地化 |
| Tooltip/Popover 被裁或错位 | anchor、clipping boundary、滚动更新 | Portal、flip/shift/size、auto-update | 四角 anchor、scroll、resize |
| Modal 背景滚/焦点跑出 | scroll lock、focus trap/return | 统一 overlay manager 或原生 dialog | Tab、Escape、关闭后焦点 |
| Header/footer 遮焦点 | fixed inset、scroll padding | reserved inset、`scroll-padding`/`scroll-margin` | 键盘遍历、锚点、错误定位 |
| 字体/图片/错误出现后跳 | 占位、metric、稳定 slot | intrinsic size、ratio、fallback metric、error slot | 冷缓存、慢网、长文案 |
| 看得到点不到 | `elementFromPoint`、透明层、pointer-events | 修 hit target、pointer policy、伪元素 | 鼠标、触摸、键盘 |
| 动画后仍挡点击或卡半态 | visibility/unmount、取消状态机 | 同步 pointer/focus 与动画 | rapid toggle、reduced motion |
| 手机输入被键盘盖 | VisualViewport、dvh、safe area | keyboard-aware footer/sheet、真机 fallback | iOS/Android、旋转 |

## 运行时审计样本

```js
const runtimeSnapshot = {
  viewport: {
    innerWidth,
    innerHeight,
    visualViewport: window.visualViewport && {
      width: visualViewport.width,
      height: visualViewport.height,
      offsetTop: visualViewport.offsetTop,
      offsetLeft: visualViewport.offsetLeft,
    },
  },
  documentOverflow: {
    scrollWidth: document.documentElement.scrollWidth,
    clientWidth: document.documentElement.clientWidth,
  },
  focus: document.activeElement?.outerHTML,
  consoleErrors: "collect from the test runner",
};
```

这只是审计起点；overlay、scroll container、layout shift 和命中目标要按项目 DOM 结构补充采集。`scrollWidth > clientWidth` 的 1px 容差、性能阈值和截图差异阈值都必须记录为项目配置，不得伪装成 Web 标准。

