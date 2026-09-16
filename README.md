# Codex Skills Collection

一组可复用的 Codex skills，按使用领域分类，适合个人使用与开源分享。

## 当前 Skills

### Travel

- `skills/travel/attraction-itinerary-excel`：从旅行行程截图或文档中逐条提取地点，核验票务与开放时间，并生成包含人民币估算和来源链接的完整 Excel。
- `skills/travel/map-itinerary-visualizer`：在地图上定位行程地点，按日期规划访问顺序，并生成带标记、箭头和图例的路线图。

### System

- `skills/system/disk-space-diagnosis`：只读分析 Windows 磁盘空间占用，解释大文件用途，分类可清理项目，并提出低风险优化路径。

### Writing

- [skills/writing/document-refinement](skills/writing/document-refinement/SKILL.md)：通用文档润色与渐进完善，适用于中英文邮件、报告、方案和说明文档。保留原意与修改边界，去除空话和写作过程旁白，按需填写 `[TBD]`，并提供原文比对、修改范围检查和替换对照表提取工具。

## 使用

将所需 skill 目录复制到本机 Codex skills 目录，或直接使用仓库中的 `SKILL.md` 作为技能定义。

复制时保留完整的 skill 目录，包括其中的 `agents/`、`references/`、`scripts/` 等配套文件。

安装 `document-refinement` 后，可这样调用：

```text
$document-refinement 帮我润色这份文档，尽量保留原文。暂不修改的部分保持不变，缺失信息先留 [TBD]。
```

日常文字润色不需要运行脚本；该 skill 附带的核对与提取脚本使用 Python 3.10+，仅依赖标准库。
