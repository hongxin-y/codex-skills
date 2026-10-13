#!/usr/bin/env python3
"""Regression tests use synthetic files inside automatically cleaned temporary folders."""

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from email.message import EmailMessage
from pathlib import Path

import document_audit as audit
import source_text as source


class AuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="document-audit-test-")
        self.root = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)

    def file(self, name, text):
        path = self.root / name
        path.write_bytes(text.encode("utf-8") if isinstance(text, str) else text)
        return path

    def plan(self, text, changes):
        return {"baseline_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(), "changes": changes}

    def edit(self, text, needle, replacement, identifier="change", offset=0):
        start = text.index(needle, offset)
        return {"id": identifier, "start": start, "end": start + len(needle),
                "expected": needle, "replacement": replacement, "what_to_fill": "Confirmed scope"}

    def trace(self, text, new, changes, **kwargs):
        return audit.build_trace(self.file("base.md", text), self.file("current.md", new), self.plan(text, changes), **kwargs)

    def test_headings_inside_fences_are_not_sections(self):
        data = "# Title\n````text\n## Fake\n```\n[TBD]\n````\n## Real\n[TBD]\n"
        result = audit.scan(data)
        self.assertEqual([h["selector"] for h in result["headings"]], ["# Title", "## Real"])
        self.assertEqual([p["in_fence"] for p in result["placeholders"]], [True, False])

    def test_unclosed_fence(self):
        result = audit.scan("## A\n```json\n{\n")
        self.assertFalse(result["fences"][0]["closed"])
        self.assertEqual(result["mechanical_errors"][0]["kind"], "unclosed_fence")

    def test_json_is_checked_not_only_counted(self):
        result = audit.scan('```json\n{"ok": true}\n```\n```json\n{"broken":}\n```\n')
        self.assertEqual(len(result["mechanical_errors"]), 1)
        self.assertEqual(result["mechanical_errors"][0]["kind"], "json_syntax")

    def test_non_json_constants_are_rejected(self):
        self.assertEqual(len(audit.scan("```json\nNaN\n```\n")["mechanical_errors"]), 1)

    def test_newlines_and_bom_preserved(self):
        path = self.file("bom.md", "\ufeff# 示例\r\n[TBD]\r\n")
        result = audit.inventory(path)
        self.assertTrue(result["utf8_bom"])
        self.assertEqual(result["newlines"]["crlf"], 2)
        self.assertEqual(result["headings"][0]["selector"], "# 示例")
        self.assertEqual(result["source"]["sha256"], hashlib.sha256(path.read_bytes()).hexdigest())

    def test_allowed_section_preserves_everything_else(self):
        old = "# Report\n## Schedule\nold\n### Detail\nold detail\n## Body\nkeep\n"
        new = old.replace("old detail", "new detail")
        result = audit.compare_documents(self.file("b.md", old), self.file("c.md", new), ["### Detail"])
        self.assertTrue(result["ok"])

    def test_unrelated_edit_detected(self):
        old = "## Schedule\nold\n## Body\nkeep\n"
        new = old.replace("old", "new").replace("keep", "altered")
        result = audit.compare_documents(self.file("b.md", old), self.file("c.md", new), ["## Schedule"])
        self.assertFalse(result["ok"])

    def test_suffix_only_is_narrow_check(self):
        old = "## Context\nbefore\n## Appendix\nkeep\n"
        new = old.replace("before", "changed")
        result = audit.compare_documents(self.file("b.md", old), self.file("c.md", new), protect_from="## Appendix")
        self.assertEqual(result["checks"], {"protected_suffix_unchanged": True})
        new = new.replace("keep", "changed")
        self.assertFalse(audit.compare_documents(self.file("b.md", old), self.file("c.md", new), protect_from="## Appendix")["ok"])

    def test_duplicate_heading_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "exactly once"):
            audit.section_range("## A\nx\n## A\ny\n", "## A")

    def test_missing_heading_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "matches=0"):
            audit.section_range("## B\nx\n", "## A")

    def test_overlapping_sections_rejected(self):
        with self.assertRaisesRegex(ValueError, "overlap"):
            audit.masked_sections("## A\nx\n### B\ny\n", ["## A", "### B"])

    def test_fence_payload_change_detected(self):
        old = '## A\n```json\n{"n":1}\n```\n'
        new = old.replace('"n":1', '"n":2')
        result = audit.compare_documents(self.file("b.md", old), self.file("c.md", new), ["## A"], protect_fences=True)
        self.assertFalse(result["ok"])
        self.assertFalse(result["checks"]["fences_unchanged"])

    def test_outside_scope_line_ending_change_detected(self):
        old = "## A\r\nx\r\n## B\r\ny\r\n"
        new = old.replace("x", "z").replace("## B\r\n", "## B\n")
        self.assertFalse(audit.compare_documents(self.file("b.md", old), self.file("c.md", new), ["## A"])["ok"])

    def test_unicode_offsets_are_codepoints(self):
        old = "# 中文 😀\r\n## Schedule\r\n[TBD]\r\n"
        edit = self.edit(old, "[TBD]", "已选择\r\n第二行")
        new = old.replace("[TBD]", edit["replacement"])
        report = self.trace(old, new, [edit], tbd_only=True)
        row = report["placeholders"][0]
        self.assertEqual(new[row["current_start"]:row["current_end"]], edit["replacement"])
        self.assertEqual(row["original_start"], old.index("[TBD]"))
        self.assertNotEqual(row["original_start"], len(old[:row["original_start"]].encode("utf-16-le")) // 2)

    def test_partial_added_and_unchanged_markers(self):
        old = "## A\n[TBD]\n## B\n[TBD]\n"
        first = self.edit(old, "[TBD]", "Known; owner [TBD].")
        tail = {"id": "new-section", "start": len(old), "end": len(old), "expected": "", "replacement": "## C\n[TBD]\n"}
        new = old.replace("[TBD]", first["replacement"], 1) + tail["replacement"]
        report = self.trace(old, new, [first, tail])
        self.assertEqual([p["id"] for p in report["placeholders"]], ["TBD-001", "TBD-002"])
        self.assertEqual(report["counts"]["partial"], 1)
        self.assertEqual(report["counts"]["unfilled"], 1)
        self.assertEqual(report["counts"]["current_literal_tbd"], 3)
        self.assertEqual(report["counts"]["new_markers_outside_original_placeholder_values"], 1)

    def test_deletion_not_misclassified_as_filled(self):
        old = "## A\n[TBD]\n"
        report = self.trace(old, old.replace("[TBD]", ""), [self.edit(old, "[TBD]", "")])
        self.assertEqual(report["counts"]["deleted"], 1)
        self.assertEqual(report["counts"]["filled"], 0)

    def test_exact_table_roundtrip(self):
        old = "## A\n[TBD]\n"
        value = "中文 😀 | <br> &amp; `id_field` [x] *bold* \\\r\n\r\nNext"
        report = self.trace(old, old.replace("[TBD]", value), [self.edit(old, "[TBD]", value)])
        markdown = audit.markdown_trace(report)
        row = next(line for line in markdown.splitlines() if line.startswith("| TBD-001"))
        self.assertEqual(audit.decode_cell(row.split("|")[7].strip()), value.replace("\r\n", "\n"))
        self.assertEqual(report["placeholders"][0]["replacement_text"], value)

    def test_unexplained_changes_fail(self):
        old = "## A\n[TBD]\nkeep\n"
        edit = self.edit(old, "[TBD]", "filled")
        with self.assertRaisesRegex(ValueError, "unexplained"):
            self.trace(old, old.replace("[TBD]", "filled").replace("keep", "changed"), [edit])

    def test_stale_baseline_hash(self):
        old = "[TBD]"
        plan = self.plan(old, [])
        plan["baseline_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "stale baseline"):
            audit.build_trace(self.file("b.md", old), self.file("c.md", old), plan)

    def test_stale_current_hash(self):
        old = "unchanged"
        plan = self.plan(old, [])
        plan["current_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "Stale current"):
            audit.build_trace(self.file("b.md", old), self.file("c.md", old), plan)

    def test_wrong_expected_text(self):
        old = "[TBD]"
        edit = self.edit(old, "[TBD]", "value")
        edit["expected"] = "wrong"
        with self.assertRaisesRegex(ValueError, "Expected text"):
            self.trace(old, "value", [edit])

    def test_region_attribution_does_not_guess(self):
        old = "## A\n[TBD]\n"
        with self.assertRaisesRegex(ValueError, "Ambiguous"):
            self.trace(old, "changed", [self.edit(old, old, "changed")])

    def test_insertion_inside_marker_rejected(self):
        old = "[TBD]"
        edit = {"id": "bad", "start": 2, "end": 2, "expected": "", "replacement": "x"}
        with self.assertRaisesRegex(ValueError, "Ambiguous"):
            self.trace(old, "[TxBD]", [edit])

    def test_unordered_and_overlapping_changes_rejected(self):
        old = "abcdef"
        first, second = self.edit(old, "ab", "AB", "one"), self.edit(old, "bc", "BC", "two")
        with self.assertRaisesRegex(ValueError, "overlapping"):
            self.trace(old, "ABBCdef", [first, second])
        with self.assertRaisesRegex(ValueError, "unordered"):
            self.trace(old, old, [self.edit(old, "ef", "EF", "late"), first])

    def test_shared_insertion_boundary_rejected(self):
        old = "abc"
        first = {"id": "insert", "start": 1, "end": 1, "expected": "", "replacement": "X"}
        second = self.edit(old, "b", "B")
        with self.assertRaises(ValueError):
            self.trace(old, "aXBc", [first, second])

    def test_tbd_only_rejects_prose_edit(self):
        with self.assertRaisesRegex(ValueError, "Non-TBD"):
            self.trace("old", "new", [self.edit("old", "old", "new")], tbd_only=True)

    def test_new_document_addition_without_original_markers(self):
        old = "## Schedule\nChosen.\n"
        edit = {"id": "new", "start": len(old), "end": len(old), "expected": "", "replacement": "\n## Storage\n[TBD]\n"}
        report = self.trace(old, old + edit["replacement"], [edit])
        self.assertEqual(report["counts"]["original_placeholders"], 0)
        self.assertEqual(report["counts"]["new_markers_outside_original_placeholder_values"], 1)

    def test_plain_email_trace_preserves_conditions(self):
        old = "Hi Alex,\nFollowing careful consideration, we propose a short call.\nIf the draft is ready, we may meet on Friday.\n"
        edit = self.edit(old, "Following careful consideration, we propose a short call.", "We propose a short call.")
        new = old.replace(edit["expected"], edit["replacement"])
        result = self.trace(old, new, [edit])
        self.assertEqual(result["counts"]["original_placeholders"], 0)
        self.assertEqual(result["other_edits"][0]["replacement"], edit["replacement"])
        with self.assertRaisesRegex(ValueError, "unexplained"):
            self.trace(old, new.replace("If the draft is ready, we may meet", "We will meet"), [edit])

    def test_deferred_field_survives_an_earlier_style_edit(self):
        old = "## Summary\n本轮先补充说明。结果仅适用于这组样本。\n## Budget\n[TBD]\n"
        edit = self.edit(old, "本轮先补充说明。", "")
        new = old.replace(edit["expected"], "")
        result = self.trace(old, new, [edit])
        self.assertEqual(result["counts"]["unfilled"], 1)
        row = result["placeholders"][0]
        self.assertEqual(new[row["current_start"]:row["current_end"]], "[TBD]")
        with self.assertRaisesRegex(ValueError, "unexplained"):
            self.trace(old, new.replace("[TBD]", "1000"), [edit])

    def test_narration_candidates_do_not_fail_or_rewrite_text(self):
        text = "## Notes\n本轮先补齐已确认部分。\n提交申请后，负责人核验资料；资料不全时退回补充。\n"
        path = self.file("review.md", text)
        report = audit.inventory(path)
        self.assertEqual(report["mechanical_errors"], [])
        self.assertEqual([h["line"] for h in report["review_hints"]], [2])
        self.assertEqual(path.read_bytes(), text.encode("utf-8"))

    def test_cli_is_read_only_and_exit_codes_are_meaningful(self):
        path = self.file("current.md", "## A\n```json\ninvalid\n```\n")
        before = path.read_bytes()
        listing = set(self.root.iterdir())
        process = subprocess.run([sys.executable, "-B", str(Path(audit.__file__)), "inventory", str(path), "--strict"], capture_output=True)
        self.assertEqual(process.returncode, 1)
        self.assertEqual(path.read_bytes(), before)
        self.assertEqual(set(self.root.iterdir()), listing)

    def test_trace_cli_json_and_markdown(self):
        old = "## Schedule\n[TBD]\n## Author\n[TBD]\n"
        edit = self.edit(old, "[TBD]", "Use a queue.\nScope remains bounded.")
        baseline = self.file("base.md", old)
        current = self.file("current.md", old.replace("[TBD]", edit["replacement"], 1))
        plan = self.file("edits.json", json.dumps(self.plan(old, [edit])))
        before = {p.name: p.read_bytes() for p in self.root.iterdir()}
        command = [sys.executable, "-B", str(Path(audit.__file__)), "trace", str(baseline), str(current), "--plan", str(plan), "--tbd-only"]
        result = subprocess.run(command, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["counts"]["filled"], 1)
        markdown = subprocess.run(command + ["--format", "markdown"], capture_output=True)
        self.assertEqual(markdown.returncode, 0, markdown.stderr)
        row = next(line for line in markdown.stdout.decode("utf-8").splitlines() if line.startswith("| TBD-001"))
        self.assertEqual(audit.decode_cell(row.split("|")[7].strip()), edit["replacement"])
        self.assertEqual({p.name: p.read_bytes() for p in self.root.iterdir()}, before)

    def test_utf8_source_text(self):
        data = "# 原稿\r\n原句 😀\r\n"
        self.assertEqual(source.extract_source(self.file("source.md", data))["text"], data)

    def test_html_entities_and_inline_text(self):
        data = "<html><body><h1>Title</h1><p>Keep <b>this</b> &amp; that.</p><script>not source evidence</script></body></html>"
        result = source.extract_source(self.file("source.html", data))
        self.assertEqual(result["blocks"][1]["text"], "Keep this & that.")
        self.assertNotIn("not source evidence", json.dumps(result))

    def test_mime_word_export(self):
        message = EmailMessage()
        message.make_related()
        body = EmailMessage()
        body.set_content("<html><body><h2>Retention</h2><p>保留原句。</p></body></html>", subtype="html", charset="utf-8")
        message.attach(body)
        result = source.extract_source(self.file("export.doc", message.as_bytes()))
        self.assertEqual(result["format"], "html-in-mime")
        self.assertEqual(result["blocks"][1]["text"], "保留原句。")

    def test_docx_text_and_revision_warning(self):
        path = self.root / "source.docx"
        xml = '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:r><w:t>Keep </w:t></w:r><w:ins><w:r><w:t>new</w:t></w:r></w:ins><w:del><w:r><w:delText>old</w:delText></w:r></w:del></w:p></w:body></w:document>'
        with zipfile.ZipFile(path, "w") as archive:
            archive.writestr("word/document.xml", xml)
        result = source.extract_source(path)
        self.assertTrue(result["blocks"][0]["has_tracked_changes"])
        self.assertEqual(result["blocks"][0]["text"], "Keep newold")

    def test_unsupported_formats_fail(self):
        cases = [("binary.doc", b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1x"), ("file.pdf", b"%PDF-1.7"), ("file.bin", b"not a document")]
        for name, data in cases:
            with self.subTest(name=name), self.assertRaises(ValueError):
                source.extract_source(self.file(name, data))

    def test_non_docx_zip_rejected(self):
        path = self.root / "archive.zip"
        with zipfile.ZipFile(path, "w") as archive:
            archive.writestr("unrelated.txt", "text")
        with self.assertRaisesRegex(ValueError, "not a supported DOCX"):
            source.extract_source(path)


if __name__ == "__main__":
    unittest.main(verbosity=2)
