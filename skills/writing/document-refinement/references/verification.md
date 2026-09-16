# 确定性核对

## 根据结论选择检查

一处短句可直接逐字对照；长文、限定区域修改、重复占位符或持续维护的替换表更适合代码。代码核对机械属性，人工判断语义、依据和文体。不要用相似度百分比证明忠于原文，也不要把关键词匹配称为 AI 味检测。

核对与提取脚本使用 Python 3.10+ 标准库，只读输入并向 stdout 输出结果，不调用网络或模型、不修改源文档。解析错误写入 stderr；回归测试会在独立临时目录创建并清理样例。用当前环境已有的 Python；路径在调用时解析成绝对路径，不硬编码某台机器的解释器。

```text
python scripts/source_text.py INPUT
python scripts/document_audit.py inventory CURRENT.md --strict
python scripts/document_audit.py compare BEFORE.md CURRENT.md --allow-section "## Schedule"
python scripts/document_audit.py compare BEFORE.md CURRENT.md --protect-from "## Appendix" --protect-fences
python scripts/document_audit.py trace BASE.md CURRENT.md --plan EDITS.json --format json
python scripts/document_audit.py trace BASE.md CURRENT.md --plan EDITS.json --format markdown --tbd-only
python -B scripts/test_document_audit.py
```

这些是相对技能目录的示例。`compare` 成功返回 0，不符合选择的保护条件返回 1；解析、路径或选择器错误返回 2。`inventory --strict` 在代码块未闭合或 fenced JSON 语法错误时返回 1，措辞候选不会导致失败。

## 输入与范围限制

`document_audit.py` 面向 UTF-8 文本和常规 Markdown；不直接处理 Word、PDF 或完整 Markdown 语法。ATX 标题和普通围栏可识别，复杂嵌套列表、引用中的围栏或特殊 Markdown 需要人工或渲染器检查。

文件哈希为原始字节的 SHA-256；文本保留原始换行和 UTF-8 BOM。位置使用 **从 0 开始的 Unicode 码点索引，结束位置不包含在内**；行号从 1 开始。不要与 UTF-8 字节偏移、JavaScript UTF-16 索引混用。

`source_text.py` 识别文本、DOCX、HTML、HTML-in-MIME Word 导出。DOCX 定位到 XML 部件和段落，HTML 定位到块；不是页码，也不完整保留表格布局、图片或修订呈现。含修订的段落可能同时提取插入和删除文本，不能当作已接受修订的正文。二进制 `.doc` 与 PDF 会拒绝并要求合适的提取工具；不要只因扩展名就强行按文本解码。

格式转换后的纯文本一致，不证明原 Word/PDF 的布局、脚注、批注和图片均保留。按任务使用格式专用工具并检查成品，不能据文本提取宣称完整还原。截图文字须核对不确定的识别结果。

## 三种检查

**盘点**：`inventory` 列出标题、字面 `[TBD]`、围栏、JSON 语法问题与少量待检查措辞。代码例子中的 `[TBD]` 不一定是真实待填事项；工具会标记它是否位于围栏中，但业务分类仍需人工完成。其他占位写法不在本脚本的自动统计范围内。

**边界比较**：`compare --allow-section` 在两个文件中遮蔽指定完整章节，精确比较其余文本。标题必须各匹配一次；缺失、重复或重叠时失败，不猜选。可多次指定互不重叠的章节。`--protect-from` 只保护选中标题起的后续内容；`--protect-fences` 对比所有围栏及顺序。它们不自行证明其他改动已获授权。新增、删除、改名的章节可以用明确修改计划检查。

**修改追踪**：`trace` 用基线和明确的修改计划重建整份当前文档，匹配后才导出原样替换文本。计划是核对资料，不是用户授权的替代物；不能把意外改动补入计划后称为合法修改。

```json
{
  "baseline_sha256": "COPY_ACTUAL_BASELINE_SHA256",
  "changes": [
    {
      "id": "schedule",
      "start": 13,
      "end": 18,
      "expected": "[TBD]",
      "replacement": "The workshop starts on 12 May.",
      "what_to_fill": "The confirmed workshop start date.",
      "basis": "user-confirmed",
      "source_ref": "The user's recorded date selection"
    }
  ]
}
```

示例位置对应 `## Schedule\n\n[TBD]\n`，日期只是虚构样例。实际哈希、位置、原文及替换必须从本次材料取得。修改 ID 唯一，按基线位置排序且不重叠；`expected` 必须与原切片一致。插入用相同 start/end 和空 expected，删除用空 replacement。共用边界的插入需合并成明确的单一修改。

有原始 `[TBD]` 时，每个被替换的原始标记单独记录；包含标记及周围文字的整段修改会被判为归属不明，而不是猜映射。只做段落润色、无需精确占位归属时可以用区域比较，不必为脚本强改写作方式。`--tbd-only` 拒绝原切片不是单个 `[TBD]` 的修改。

JSON 输出保留确切源字符串、前后位置、基线哈希、原始占位符稳定 ID、填充状态与新增标记数。Markdown 表来自这些同一字符串，显示时对特殊字符做可逆编码、换行转成 `<br>`；JSON 保留原始换行。填充说明和依据不是引文。使用 `decode_cell` 还原表格显示单元后再对照，不要把转义后的展示值误认为正文变化。

保持基线不变，连续编辑更新明确计划；新增部分不追记成原始占位符。换用新基线时说明核对范围已经变化。若有维护中的旧格式 JSON，先确认其偏移单位和字段定义，不能直接套用本脚本的结构。

## 人工复核与测试

检查措辞前后的主体、情态、否定、数字、时间、条件、例外与证据强度；对照上下文中的同名概念、例子、公式和表格。技术图要核对节点、连线、分支、循环和入口出口；图能渲染不等于业务语义正确，代码块一致也不等于渲染成功。

脚本改动后运行随附回归测试。测试涵盖 Unicode、换行、越界修改、过期哈希、重复标题、围栏、部分／新增／删除占位符、对照表还原与提取格式。它验证实现的这些行为，不评价一篇文档是否自然或事实是否成立。

交付时使用窄而准确的结论，例如“指定章节之外保持一致”“46 项替换文本与源切片相等”“JSON 语法通过”。说明实质含义仍经人工复核，而不要说脚本已证明没有幻觉、符合全部要求或完全无风险。
