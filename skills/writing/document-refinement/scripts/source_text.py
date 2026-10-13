#!/usr/bin/env python3
"""Read-only, text-oriented source extraction; no rendering or network access."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import sys
import zipfile
from email import policy
from email.parser import BytesParser
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree as ET


class HTMLBlocks(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.active, self.depth, self.parts, self.blocks = None, 0, [], []
        self.skipped = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skipped += 1
        if self.skipped:
            return
        if self.active is None and tag in ("h1", "h2", "h3", "h4", "h5", "h6", "p", "tr", "li", "pre"):
            self.active, self.depth, self.parts = tag, 1, []
        elif tag == self.active:
            self.depth += 1
        elif self.active and tag in ("br", "td", "th"):
            self.parts.append("\n" if tag == "br" else "\t")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skipped = max(0, self.skipped - 1)
            return
        if self.skipped:
            return
        if tag == self.active:
            self.depth -= 1
            if not self.depth:
                text = "".join(self.parts)
                if self.active != "pre":
                    text = " ".join(text.split())
                self.blocks.append({"element": self.active, "text": text})
                self.active, self.parts = None, []

    def handle_data(self, data):
        if self.active and not self.skipped:
            self.parts.append(data)


def html_blocks(text: str) -> list:
    parser = HTMLBlocks()
    parser.feed(text)
    parser.close()
    if parser.active:
        raise ValueError("Unclosed HTML extraction block; use a more complete HTML/Word extractor")
    if not parser.blocks:
        raise ValueError("No supported HTML text blocks; inspect with a suitable HTML/Word tool")
    return [{"block": i, **block} for i, block in enumerate(parser.blocks, 1)]


def extract_source(path: str | Path) -> dict:
    path = Path(path).resolve()
    raw = path.read_bytes()
    result = {"source": str(path), "sha256": hashlib.sha256(raw).hexdigest()}
    if raw.startswith(b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1"):
        raise ValueError("Binary legacy Word is not supported; use a trusted Word converter and inspect the result")
    if raw.startswith(b"%PDF"):
        raise ValueError("PDF requires a PDF extractor/render inspection; it is not UTF-8 text")
    if zipfile.is_zipfile(io.BytesIO(raw)):
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            names = archive.namelist()
            if "word/document.xml" not in names:
                raise ValueError("ZIP is not a supported DOCX")
            ns = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
            parts = ["word/document.xml"] + sorted(n for n in names if re.fullmatch(
                r"word/(?:header\d*|footer\d*|footnotes|endnotes|comments)\.xml", n))
            blocks = []
            for part in parts:
                info = archive.getinfo(part)
                if info.file_size > 32 * 1024 * 1024:
                    raise ValueError("DOCX XML part exceeds the extractor's 32 MiB limit")
                xml = archive.read(part)
                if b"<!DOCTYPE" in xml.upper() or b"<!ENTITY" in xml.upper():
                    raise ValueError("Unexpected XML entity declarations")
                root = ET.fromstring(xml)
                for index, paragraph in enumerate(root.iter(ns + "p"), 1):
                    text = []
                    for node in paragraph.iter():
                        if node.tag in (ns + "t", ns + "delText"):
                            text.append(node.text or "")
                        elif node.tag == ns + "tab":
                            text.append("\t")
                        elif node.tag in (ns + "br", ns + "cr"):
                            text.append("\n")
                    blocks.append({"part": part, "paragraph": index, "text": "".join(text),
                                   "has_tracked_changes": any(n.tag in (ns + "ins", ns + "del") for n in paragraph.iter())})
        result.update(format="docx-text", blocks=blocks,
                      limits="Paragraph text includes tracked insertions/deletions together when present; inspect them separately. No pagination, table layout, image OCR or rendering.")
        return result
    mime_head = raw[:8192]
    if re.search(br"(?im)^Content-Type:\s*multipart/", mime_head):
        message = BytesParser(policy=policy.default).parsebytes(raw)
        blocks = []
        for index, part in enumerate(message.walk()):
            if part.get_content_type() == "text/html":
                for block in html_blocks(part.get_content()):
                    blocks.append({"mime_part": index, **block})
        if not blocks:
            raise ValueError("Multipart source contains no supported HTML body")
        result.update(format="html-in-mime", blocks=blocks,
                      limits="Non-preformatted whitespace normalized; MIME transfer encoding and HTML entities decoded. No pagination, layout, image OCR or rendering.")
        return result
    text = raw.decode("utf-8")
    if re.search(r"<(?:!doctype\s+html|html|body)(?:\s|>)", text[:2048], re.I):
        result.update(format="html", blocks=html_blocks(text),
                      limits="Non-preformatted whitespace normalized and HTML entities decoded. No pagination or image/layout inspection.")
    elif path.suffix.lower() in (".txt", ".md", ".markdown"):
        result.update(format="utf8-text", text=text, limits="Text only; no rendered-layout verification.")
    else:
        raise ValueError("Unsupported source format; do not infer text fidelity from a filename extension")
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input")
    args = parser.parse_args(argv)
    try:
        print(json.dumps(extract_source(args.input), ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, LookupError, ET.ParseError, zipfile.BadZipFile) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    raise SystemExit(main())
