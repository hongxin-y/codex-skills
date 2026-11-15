# UI Engineering Blueprint

Page Element Blueprint 说明“页面里有什么”；UI Engineering Blueprint 说明这些内容如何在真实浏览器中稳定存在。它是详细实现前的工程决策记录，不要求把所有字段都展示给用户，但必须为每个主要区域、共享 primitive 和高风险交互留下结果。

## 1. 必填结构

```yaml
ui_engineering_blueprint:
  layout_contract:
    display_mode:
    sizing_axis:
    min_inline_size:
    min_block_size:
    intrinsic_size_behavior:
    content_growth_policy:
  spacing:
    spacing_owner:
    internal_spacing_tokens:
    sibling_spacing_source:
    edge_merging_policy:
  overflow:
    overflow_policy: visible-content | wrap | truncate-one-line | clamp-summary | scroll-inline | scroll-block | scroll-both | clip-decorative
    scroll_container_role:
    scroll_chain_policy:
    scrollbar_policy:
    truncation_policy:
  positioning:
    positioning_mode:
    containing_block:
    sticky_reference:
    anchor_strategy:
  layering:
    creates_stacking_context:
    stacking_context_policy:
    layer_token:
    portal_policy:
    top_layer_eligible:
  overlay:
    collision_boundary:
    collision_strategy:
    reserved_viewport_regions:
    escape_owner:
    outside_press_policy:
    scroll_strategy:
  focus_and_hit_testing:
    focus_visibility_policy:
    focus_containment:
    focus_return:
    focus_obscuration_risk:
    hit_area:
    pointer_policy:
    touch_policy:
    drag_alternative:
    keyboard_model:
  content_and_async:
    long_text_policy:
    internationalization_policy:
    rtl_policy:
    emoji_policy:
    async_placeholder_policy:
    intrinsic_placeholder_size:
    loading_size_stability:
    error_slot_policy:
  responsive_and_assets:
    responsive_fallback:
    container_query_policy:
    viewport_unit_policy:
    safe_area_policy:
    keyboard_viewport_policy:
    image_intrinsic_size_policy:
    object_fit_policy:
    font_fallback_metric_policy:
    icon_viewbox_policy:
  motion_and_validation:
    motion_policy:
    reduced_motion_fallback:
    compositing_risk:
    visual_regression_cases:
    keyboard_cases:
    touch_cases:
    extreme_content_cases:
    browser_cases:
```

字段不适用时必须写 `N/A — <具体原因>`。不得因为使用了现成组件、页面很短或没有设计稿而省略工程判断。

## 2. 生成前、生成中、生成后

### 生成前

完成 Page Blueprint、Engineering Blueprint 和风险列表；先决定 spacing owner、scroll owner、overlay root、layer policy、内容增长和响应式降级。

### 生成中

每完成共享 Layout、Overlay、DataGrid、Form、Drawer、Popover 或虚拟列表 primitive，就用长文本、错误、窄屏和键盘检查 overflow、stacking、hit-testing、focus 和状态尺寸。共享 primitive 的修复要回归所有使用它的页面。

### 生成后

按风险运行 Browser Runtime Audit、截图回归、自动化可访问性检查、键盘/触摸/浮层人工检查和 Repair → Regression Review。截图“看起来正确”不能证明滚动、焦点、命中和运行时层级正确。

## 3. 完成定义

实现完成必须同时满足：

`Task correct + layout stable + content resilient + layer correct + scroll correct + hit-test correct + focus correct + responsive correct + async stable + platform-verified`

如果只能完成静态视觉或代码结构，必须在交付中明确哪些运行时条件未验证。

