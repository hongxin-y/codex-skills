# Codex Skills Collection

一组可复用的 Codex 技能，涵盖旅行规划、Windows 磁盘诊断和文档润色。按领域整理，每个技能可单独使用。

## 技能目录

| 领域 | 技能 | 适合处理什么 |
| --- | --- | --- |
| Travel · 旅行 | [attraction-itinerary-excel](skills/travel/attraction-itinerary-excel/SKILL.md) | 从行程截图或文档提取地点，核验票务、开放时间和预约方式，生成含人民币估算与来源链接的 Excel。 |
| Travel · 旅行 | [map-itinerary-visualizer](skills/travel/map-itinerary-visualizer/SKILL.md) | 定位行程地点，按日期规划访问顺序，生成带编号、路线箭头和图例的地图图片。 |
| System · 系统 | [disk-space-diagnosis](skills/system/disk-space-diagnosis/SKILL.md) | 只读分析 Windows 磁盘占用，解释大文件用途、清理风险和可行的优化方式，不执行清理。 |
| Writing · 写作 | [document-refinement](skills/writing/document-refinement/SKILL.md) | 润色中英文邮件、报告和方案，保留原意与修改边界，去除空话和写作过程旁白，逐步补全缺失内容。 |

## 快速开始

### 1. 选择并复制技能

打开上表中的 `SKILL.md`，确认用途和所需工具，然后复制对应的**整个技能文件夹**。例如，文档润色技能位于 `skills/writing/document-refinement/`。

保留文件夹中的 `agents/`、`references/`、`scripts/` 等配套内容，不要只复制 `SKILL.md`。如果目标目录已有同名技能，先比较内容，避免覆盖自己的修改。

### 2. 放入技能加载目录

按使用范围选择位置：

- **个人使用**：放入 `~/.agents/skills/`，供不同项目使用。`~` 表示当前用户的主目录。
- **项目使用**：放入目标项目的 `.agents/skills/`，随项目维护。

技能文件夹直接放在加载目录下，不保留本仓库的领域分类层。例如，个人安装后的入口为 `~/.agents/skills/document-refinement/SKILL.md`。目录规则见 [Codex 官方技能文档](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)。

### 3. 在任务中调用

选择技能，并附上要处理的文件、截图或路径。例如：

```text
$document-refinement 帮我润色这份文档，尽量保留原文。暂不修改的部分保持不变，缺失信息先留 [TBD]。
```

Codex 支持按任务自动匹配技能，也可以显式指定；若新技能未出现，可重启后再查看。具体调用方式见 [官方说明](https://learn.chatgpt.com/docs/build-skills#how-chatgpt-and-codex-use-skills)。

## 更多调用示例

每条示例用于一个独立任务；旅行任务请同时提供行程和出行日期。

```text
$attraction-itinerary-excel 按这份行程逐条整理地点，核实门票、开放时间和预约方式，生成 Excel，不增删原行程项目。

$map-itinerary-visualizer 把这份行程按日期画在地图上，标出地点编号和建议路线，说明调整顺序的原因。

$disk-space-diagnosis 帮我分析 C 盘为什么快满了，解释主要占用项和清理风险，只做诊断，不删除或修改文件。
```

## 所需工具与使用边界

复制技能只会添加工作指引，不会一并安装它依赖的工具。各技能的具体要求以其 `SKILL.md` 为准。

- **行程 Excel**：需要联网查询。当前指引还要求表格技能和 `@oai/artifact-tool`，用于生成与检查工作簿。票价、汇率和开放时间应按出行日期核验，估算值与无法核实的信息需注明。
- **行程地图**：需要地图访问、截图及图片处理能力。无法取得真实地图时，替代示意图必须明确标注，不能当作地图截图交付。
- **磁盘诊断**：面向 Windows，需要 PowerShell 等只读查询能力。诊断不包含删除文件或调整系统设置；后续操作须单独确认目标和风险。
- **文档润色**：日常文字修改无需运行脚本；可选的核对与提取脚本使用 Python 3.10+ 标准库。脚本能核对文本和修改范围，但不能证明事实正确；Word/PDF 排版、OCR 和渲染检查需要相应工具。

## 维护与验证

新增技能按 `skills/<领域>/<技能名>/` 放置，并在上方目录补充链接与用途。入口使用 `SKILL.md`；有配套资源时，保持相对引用可用。分享前检查是否包含个人路径、凭据或敏感样例。

修改文档润色技能的脚本后，可在本仓库根目录运行其回归测试：

```shell
python -B skills/writing/document-refinement/scripts/test_document_audit.py
```

该测试只覆盖文档核对与提取脚本，不代表其他技能已经通过测试，也不替代实际产物检查。
