#!/usr/bin/env python3
"""Read-only document checks. Python 3.10+, standard library only."""

from __future__ import annotations

import argparse
import difflib
import hashlib
import html
import json
import re
import sys
from pathlib import Path


MARKER = "[TBD]"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_document(path: str | Path) -> dict:
    path = Path(path).resolve()
    raw = path.read_bytes()
    return {"path": str(path), "sha256": digest(raw), "text": raw.decode("utf-8")}


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def strict_json(text: str):
    def reject_constant(value):
        raise ValueError(f"Non-JSON constant: {value}")
    return json.loads(text, parse_constant=reject_constant)


def scan(text: str) -> dict:
    headings, fences, errors, hints = [], [], [], []
    active = None
    style_patterns = (
        r"\bthis (?:document|report|proposal) remains (?:a )?draft\b", r"\bthis section will\b",
        r"\bwe will fill (?:in|out)\b", r"\bas an AI\b",
        r"本轮(?:先|将|已)(?:补充|补齐|完善|调整)", r"后续再(?:补充|完善)本节",
    )
    for index, match in enumerate(re.finditer(r"[^\n]*(?:\n|$)", text), 1):
        raw, offset = match.group(), match.start()
        if not raw:
            continue
        line = raw.rstrip("\r\n")
        visible = line.lstrip("\ufeff") if offset == 0 else line
        fence = re.fullmatch(r" {0,3}(`{3,}|~{3,})(.*)", visible)
        if active is not None:
            if (fence and fence[1][0] == active["marker"]
                    and len(fence[1]) >= active["length"] and not fence[2].strip()):
                active.update(end=offset + len(raw), payload_end=offset, closed=True)
                fences.append(active)
                active = None
            continue
        if fence:
            info = fence[2].strip()
            active = {"start": offset, "line": index, "payload_start": offset + len(raw),
                      "marker": fence[1][0], "length": len(fence[1]), "info": info,
                      "language": info.split()[0].lower() if info else ""}
            continue
        heading = re.fullmatch(r" {0,3}(#{1,6})[ \t]+(.+?)\s*", visible)
        if heading:
            headings.append({"selector": visible.strip(), "level": len(heading[1]),
                             "line": index, "start": offset})
        if re.search(r"\w\\_\w", line):
            hints.append({"line": index, "kind": "escaped_identifier",
                          "note": "Check identifier rendering; this is not an automatic fix."})
        if any(re.search(pattern, line, re.I) for pattern in style_patterns):
            hints.append({"line": index, "kind": "possible_writing_narration",
                          "note": "Inspect context; quotations and actual constraints may be valid."})
    if active is not None:
        active.update(end=len(text), payload_end=len(text), closed=False)
        fences.append(active)
        errors.append({"line": active["line"], "kind": "unclosed_fence"})
    for h_index, heading in enumerate(headings):
        heading["end"] = next((h["start"] for h in headings[h_index + 1:]
                               if h["level"] <= heading["level"]), len(text))
        heading["sha256"] = digest(text[heading["start"]:heading["end"]].encode("utf-8"))
    for fence in fences:
        fence["sha256"] = digest(text[fence["start"]:fence["end"]].encode("utf-8"))
        if fence["language"] == "json" and fence["closed"]:
            try:
                strict_json(text[fence["payload_start"]:fence["payload_end"]])
            except ValueError as exc:
                errors.append({"line": fence["line"], "kind": "json_syntax", "message": str(exc)})
    placeholders = []
    for index, match in enumerate(re.finditer(re.escape(MARKER), text), 1):
        placeholders.append({"id": f"TBD-{index:03d}", "start": match.start(), "end": match.end(),
                             "line": line_number(text, match.start()),
                             "in_fence": any(f["start"] <= match.start() < f["end"] for f in fences)})
    return {"headings": headings, "fences": fences, "placeholders": placeholders,
            "mechanical_errors": errors, "review_hints": hints}


def inventory(path: str | Path) -> dict:
    doc = read_document(path)
    text = doc["text"]
    result = scan(text)
    result.update(source={"path": doc["path"], "sha256": doc["sha256"]},
                  offset_unit="Unicode code points; zero-based, end-exclusive; lines one-based",
                  characters=len(text), literal_tbd_count=len(result["placeholders"]),
                  outside_fence_tbd_count=sum(not p["in_fence"] for p in result["placeholders"]),
                  newlines={"crlf": text.count("\r\n"),
                            "lf_only": text.count("\n") - text.count("\r\n"),
                            "cr_only": text.count("\r") - text.count("\r\n")},
                  utf8_bom=text.startswith("\ufeff"),
                  limits="No factual, semantic, schema, full Markdown or Mermaid-render verification.")
    return result


def section_range(text: str, selector: str) -> tuple[int, int]:
    matches = [h for h in scan(text)["headings"] if h["selector"] == selector]
    if len(matches) != 1:
        raise ValueError(f"Section selector must match exactly once: {selector!r}; matches={len(matches)}")
    return matches[0]["start"], matches[0]["end"]


def masked_sections(text: str, selectors: list[str]) -> str:
    if len(set(selectors)) != len(selectors):
        raise ValueError("Duplicate allowed-section selectors")
    ranges = sorted((*section_range(text, selector), selector) for selector in selectors)
    for prev, current in zip(ranges, ranges[1:]):
        if current[0] < prev[1]:
            raise ValueError("Allowed sections overlap; choose the narrowest sufficient sections")
    pieces, cursor = [], 0
    for start, end, selector in ranges:
        pieces.extend((text[cursor:start], f"\x00ALLOWED:{selector}\x00"))
        cursor = end
    pieces.append(text[cursor:])
    return "".join(pieces)


def compare_documents(baseline, current, allowed=None, protect_from=None, protect_fences=False):
    before, after = read_document(baseline), read_document(current)
    old, new = before["text"], after["text"]
    checks = {}
    if allowed:
        checks["outside_allowed_sections_unchanged"] = masked_sections(old, allowed) == masked_sections(new, allowed)
    if protect_from:
        old_start, _ = section_range(old, protect_from)
        new_start, _ = section_range(new, protect_from)
        checks["protected_suffix_unchanged"] = old[old_start:] == new[new_start:]
    if protect_fences:
        blocks = lambda text: [text[f["start"]:f["end"]] for f in scan(text)["fences"]]
        checks["fences_unchanged"] = blocks(old) == blocks(new)
    if not checks:
        checks["entire_document_unchanged"] = old == new
    hunks = []
    for tag, a1, a2, b1, b2 in difflib.SequenceMatcher(
            None, old.splitlines(keepends=True), new.splitlines(keepends=True), autojunk=False).get_opcodes():
        if tag != "equal":
            hunks.append({"kind": tag, "baseline_lines": [a1 + 1, a2], "current_lines": [b1 + 1, b2]})
    return {"ok": all(checks.values()), "checks": checks, "changed_line_hunks": hunks,
            "sources": {"baseline": {k: before[k] for k in ("path", "sha256")},
                        "current": {k: after[k] for k in ("path", "sha256")}},
            "limits": "Equality checks cover only the selected constraints; no semantic or authority verification."}


def build_trace(baseline, current, plan: dict, tbd_only=False) -> dict:
    before, after = read_document(baseline), read_document(current)
    old, new = before["text"], after["text"]
    if not isinstance(plan, dict) or str(plan.get("baseline_sha256", "")).lower() != before["sha256"]:
        raise ValueError("Missing or stale baseline SHA-256")
    if "current_sha256" in plan and str(plan["current_sha256"]).lower() != after["sha256"]:
        raise ValueError("Stale current SHA-256")
    changes = plan.get("changes")
    if not isinstance(changes, list):
        raise ValueError("Plan changes must be a list")
    placeholders = scan(old)["placeholders"]
    token_map = {(p["start"], p["end"]): p for p in placeholders}
    edits, seen, prior = [], set(), None
    for change in changes:
        if not isinstance(change, dict):
            raise ValueError("Each change must be an object")
        identifier = change.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in seen:
            raise ValueError("Changes require unique, nonempty string IDs")
        seen.add(identifier)
        start, end = change.get("start"), change.get("end")
        if type(start) is not int or type(end) is not int or not 0 <= start <= end <= len(old):
            raise ValueError(f"Invalid range: {identifier}")
        expected, replacement = change.get("expected"), change.get("replacement")
        if not isinstance(expected, str) or not isinstance(replacement, str):
            raise ValueError(f"Expected/replacement must be strings: {identifier}")
        if old[start:end] != expected:
            raise ValueError(f"Expected text differs from baseline: {identifier}")
        if prior is not None:
            if start < prior["end"] or start == prior["start"]:
                raise ValueError("Changes are unordered or overlapping")
            if start == prior["end"] and (start == end or prior["start"] == prior["end"]):
                raise ValueError("Insertion shares an edit boundary; combine the edits explicitly")
        if tbd_only and expected != MARKER:
            raise ValueError(f"Non-TBD edit in TBD-only mode: {identifier}")
        for p in placeholders:
            overlaps = (start < p["end"] and end > p["start"]) or (start == end and p["start"] < start < p["end"])
            if overlaps and (start, end) != (p["start"], p["end"]):
                raise ValueError(f"Ambiguous placeholder attribution: {identifier} covers part or context of {p['id']}")
        edit = dict(change)
        edit.update(start=start, end=end)
        edits.append(edit)
        prior = edit
    pieces, cursor, position = [], 0, 0
    for edit in edits:
        unchanged = old[cursor:edit["start"]]
        pieces.append(unchanged)
        position += len(unchanged)
        edit["current_start"] = position
        pieces.append(edit["replacement"])
        position += len(edit["replacement"])
        edit["current_end"] = position
        edit["original_line"] = line_number(old, edit["start"])
        cursor = edit["end"]
    pieces.append(old[cursor:])
    if "".join(pieces) != new:
        raise ValueError("Current document contains unexplained changes or differs from planned replacements")
    for edit in edits:
        edit["current_line"] = line_number(new, edit["current_start"])
    exact_edits = {(e["start"], e["end"]): e for e in edits}
    mapped = []
    for p in placeholders:
        edit = exact_edits.get((p["start"], p["end"]))
        if edit:
            value, start, end = edit["replacement"], edit["current_start"], edit["current_end"]
        else:
            shift = sum(len(e["replacement"]) - (e["end"] - e["start"])
                        for e in edits if e["end"] <= p["start"])
            start, end, value = p["start"] + shift, p["end"] + shift, MARKER
        if new[start:end] != value:
            raise ValueError(f"Mapped source slice mismatch: {p['id']}")
        status = "unfilled" if value == MARKER else "deleted" if not value else "partial" if MARKER in value else "filled"
        mapped.append({"id": p["id"], "original_start": p["start"], "original_end": p["end"],
                       "original_line": p["line"], "current_start": start, "current_end": end,
                       "current_line": line_number(new, start), "original_text": MARKER,
                       "replacement_text": value, "status": status, "in_original_fence": p["in_fence"],
                       "what_to_fill": edit.get("what_to_fill", "") if edit else "",
                       "basis": edit.get("basis", "") if edit else "",
                       "source_ref": edit.get("source_ref", "") if edit else ""})
    counts = {"original_placeholders": len(mapped), "mapped": len(mapped),
              **{status: sum(p["status"] == status for p in mapped)
                 for status in ("filled", "partial", "unfilled", "deleted")},
              "current_literal_tbd": new.count(MARKER)}
    counts["markers_in_original_placeholder_values"] = sum(p["replacement_text"].count(MARKER) for p in mapped)
    counts["new_markers_outside_original_placeholder_values"] = counts["current_literal_tbd"] - counts["markers_in_original_placeholder_values"]
    return {"ok": True, "sources": {"baseline": {k: before[k] for k in ("path", "sha256")},
                                     "current": {k: after[k] for k in ("path", "sha256")}},
            "offset_unit": "Unicode code points; zero-based, end-exclusive; lines one-based",
            "counts": counts, "placeholders": mapped,
            "other_edits": [e for e in edits if (e["start"], e["end"]) not in token_map],
            "limits": "Verifies exact text and edit coverage, not the truth or authority of plan annotations."}


def encode_cell(value) -> str:
    value = str(value).replace("\r\n", "\n").replace("\r", "\n")
    encoded = html.escape(value, quote=False)
    for character in "|`*_[]\\":
        encoded = encoded.replace(character, f"&#{ord(character)};")
    return encoded.replace("\n", "<br>")


def decode_cell(value: str) -> str:
    return html.unescape(value.replace("<br>", "\n"))


def markdown_trace(report: dict) -> str:
    rows = ["# Document replacement audit", "",
            "Extracted text is verbatim; table cells use reversible display encoding and normalize line breaks for display only.",
            "Filling guidance and basis annotations are separate from document source text.", "",
            f"Counts: `{json.dumps(report['counts'], ensure_ascii=False)}`", "",
            "## Original placeholders", "",
            "| ID | Original line | Current line | Status | Original text | Filling guidance | Current replacement text | Basis / source |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for p in report["placeholders"]:
        values = (p["id"], p["original_line"], p["current_line"], p["status"], p["original_text"],
                  p["what_to_fill"], p["replacement_text"], f"{p['basis']} {p['source_ref']}".strip())
        rows.append("| " + " | ".join(encode_cell(v) for v in values) + " |")
    rows.extend(("", "## Other explicit edits", "",
                 "| ID | Original line | Current line | Previous text | Current text | Basis / source |",
                 "| --- | --- | --- | --- | --- | --- |"))
    for edit in report["other_edits"]:
        values = (edit["id"], edit["original_line"], edit["current_line"], edit["expected"], edit["replacement"],
                  f"{edit.get('basis', '')} {edit.get('source_ref', '')}".strip())
        rows.append("| " + " | ".join(encode_cell(v) for v in values) + " |")
    rows.extend(("", f"Baseline SHA-256: `{report['sources']['baseline']['sha256']}`",
                 f"Current SHA-256: `{report['sources']['current']['sha256']}`", "", report["limits"], ""))
    return "\n".join(rows)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    inv = commands.add_parser("inventory")
    inv.add_argument("file")
    inv.add_argument("--strict", action="store_true", help="Exit 1 on fenced-JSON syntax or unclosed-fence errors")
    comp = commands.add_parser("compare")
    comp.add_argument("baseline")
    comp.add_argument("current")
    comp.add_argument("--allow-section", action="append", default=[])
    comp.add_argument("--protect-from")
    comp.add_argument("--protect-fences", action="store_true")
    trace = commands.add_parser("trace")
    trace.add_argument("baseline")
    trace.add_argument("current")
    trace.add_argument("--plan", required=True)
    trace.add_argument("--format", choices=("json", "markdown"), default="json")
    trace.add_argument("--tbd-only", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.command == "inventory":
            result = inventory(args.file)
            code = int(args.strict and bool(result["mechanical_errors"]))
        elif args.command == "compare":
            result = compare_documents(args.baseline, args.current, args.allow_section, args.protect_from, args.protect_fences)
            code = int(not result["ok"])
        else:
            result = build_trace(args.baseline, args.current, strict_json(read_document(args.plan)["text"]), args.tbd_only)
            if args.format == "markdown":
                print(markdown_trace(result), end="")
                return 0
            code = 0
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return code
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    raise SystemExit(main())
