# Browser and Platform Matrix

## 1. 风险分层覆盖

不要把 Browser × Viewport × Input × Content × State 全量相乘。按风险选择：

- **关键 Red Route**：目标浏览器 × 关键 viewport × 键盘/触摸核心覆盖。
- **高风险组件**：浏览器 pairwise，加上 modal、sticky、长内容、异步和键盘状态。
- **低风险视觉变体**：Storybook/组件截图扫描和主题对照。
- **真实线上行为**：RUM、JS 错误、layout shift 和关键交互失败监控（若产品具备）。

## 2. 覆盖维度

```text
Browser: Chromium / Firefox / Safari / iOS Safari / target Android WebView / Electron when relevant
Viewport: phone / tablet / laptop / desktop / ultrawide
Zoom: 100 / 125 / 200 / 400%
Input: mouse / keyboard / touch / screen reader / mixed pointer
Content: short / long / CJK / RTL / emoji / missing / extreme / async / error
State: default / hover / focus / active / disabled / loading / error / empty / selected / expanded / modal-open / keyboard-open
```

## 3. 自动化与人工边界

- Playwright/Storybook 截图适合边框、对齐、阴影、圆角、主题和已知状态回归。
- axe 等自动化工具适合发现一部分可访问性问题。
- 键盘路径、读屏语义、焦点遮挡、复杂浮层组合、触摸手感和真实移动键盘仍需人工或设备检查。
- 如果没有真机、目标浏览器或性能样本，交付标记为未验证，不推断“跨平台稳定”。

