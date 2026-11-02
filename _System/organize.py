"""Apply the vault's mechanical rules to Concepts/ and regenerate _System/index.md.

Usage: python _System/organize.py [--report]

--report only prints signs of drift and changes nothing.

Inbox/ is never touched. Note text is never reworded: only metadata, link syntax
and tags change. Running it twice changes nothing the second time.
"""
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONCEPTS = ROOT / "Concepts"
INDEX = ROOT / "_System" / "index.md"

FRONTMATTER = re.compile(r"^---\r?\n(.*?\r?\n)?---[ \t]*(?:\r?\n|$)", re.S)
LINK = re.compile(r"(?<!!)\[\[([^\[\]]*)\]\]")
TAG = re.compile(r"[ \t]*(?<![\w#/&`])#([A-Za-z][\w/-]*)")
INLINE_CODE = re.compile(r"(`[^`\n]*`)")
RELATED = re.compile(r"^## Related(?: Notes)?[ \t]*$")
HEADING = re.compile(r"^#{1,6} ")


def parse_fields(frontmatter):
    """Read scalar and list fields from simple YAML, without a YAML dependency."""
    fields, key = {}, None
    for line in frontmatter.splitlines():
        item = re.match(r"^\s+-\s+(.*)$", line)
        if item and key:
            fields[key].append(item.group(1).strip())
            continue
        pair = re.match(r"^([\w-]+):\s*(.*)$", line)
        if pair:
            key, value = pair.groups()
            value = value.strip()
            fields[key] = [] if value in ("", "[]") else value
    return fields


def fence_state(line, state):
    """Track fences. Admonitions (```ad-*) hold note text, so only real code is skipped."""
    if not line.lstrip().startswith("```"):
        return state
    if state is None:
        return "ad" if line.lstrip().startswith("```ad-") else "code"
    return None


def outside_code(line, fn):
    """Apply fn to a line, skipping inline code spans."""
    return "".join(part if part.startswith("`") else fn(part) for part in INLINE_CODE.split(line))


def strip_links(text, stem, targets):
    def rep(match):
        inner = match.group(1)
        if not inner.strip():
            return ""
        target, _, alias = inner.partition("|")
        alias = alias.lstrip("|")
        lead = target[: len(target) - len(target.lstrip())]
        target = re.sub(r"\.md(?=$|#)", "", target.strip())
        if target.split("#")[0].lower() != stem.lower():
            targets.append(target)
        return alias or lead + target
    return LINK.sub(rep, text)


def link_key(item):
    return re.sub(r"^-\s*\[\[|\]\]$", "", item.strip()).split("|")[0].strip().lower()


def clean_body(body, stem, is_moc, tags, eol):
    """Move inline tags to `tags` and, except in MOCs, inline links to ## Related."""
    text = body.replace("\r\n", "\n")
    main, related = [], []
    heading_found = renamed = in_related = False
    state = None
    for line in text.split("\n"):
        state = fence_state(line, state)
        if state is None and RELATED.match(line):
            renamed = renamed or line.rstrip() != "## Related"
            in_related = heading_found = True
            continue
        if in_related and HEADING.match(line):
            in_related = False
        (related if in_related else main).append(line)

    def collect(part):
        tags.extend(TAG.findall(part))
        return TAG.sub("", part)

    targets, out = [], []
    state = None
    for line in main:
        was_code = state == "code"
        state = fence_state(line, state)
        if was_code or state == "code" or line.lstrip().startswith("```"):
            out.append(line)
            continue
        new = outside_code(line, collect)
        if not is_moc:
            new = outside_code(new, lambda part: strip_links(part, stem, targets))
        if new != line and TAG.search(line) and not new.strip():
            continue  # the line held nothing but tags
        out.append(new)

    items = [l.strip() for l in related if l.strip()]
    seen = {link_key(i) for i in items}
    added = False
    for target in targets:
        if target.lower() not in seen:
            seen.add(target.lower())
            items.append(f"- [[{target}]]")
            added = True

    if out == main and not added and not renamed:
        return body
    new_main = "\n".join(out)
    if items or heading_found:
        new_main = new_main.rstrip() + "\n\n## Related\n" + "".join(i + "\n" for i in items)
    return new_main.replace("\n", eol)


def new_frontmatter(path, inner, fields, tags, eol):
    lines = inner.splitlines()
    current = fields.get("tags", [])
    current = [current] if isinstance(current, str) else current
    new_tags = [t for t in dict.fromkeys(tags) if t not in current]
    if new_tags:
        items = [f"  - {t}" for t in new_tags]
        if isinstance(fields.get("tags"), list):
            i = next(n for n, l in enumerate(lines) if l.startswith("tags:"))
            lines[i] = "tags:"
            while i + 1 < len(lines) and re.match(r"^\s+-\s", lines[i + 1]):
                i += 1
            lines[i + 1:i + 1] = items
        else:
            kept = [f"  - {t}" for t in current]
            lines = ["tags:"] + kept + items + [l for l in lines if not l.startswith("tags:")]

    created = datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%dT%H:%M")
    defaults = [("created", created), ("type", "concept"), ("status", "wip"), ("area", "[]")]
    if fields.get("type") != "moc":
        defaults.append(("source", ""))
    for key, value in defaults:
        if key not in fields:
            lines.append(f"{key}: {value}".rstrip())
    return "---" + eol + "".join(l + eol for l in lines) + "---" + eol


def organize_note(path):
    raw = path.read_bytes().decode("utf-8")
    eol = "\r\n" if "\r\n" in raw else "\n"
    match = FRONTMATTER.match(raw)
    inner = (match.group(1) or "") if match else ""
    fields = parse_fields(inner)
    body = raw[match.end():] if match else raw
    tags = []
    new_body = clean_body(body, path.stem, fields.get("type") == "moc", tags, eol)
    frontmatter = new_frontmatter(path, inner, fields, tags, eol)
    if match and parse_fields(frontmatter) == fields:
        frontmatter = raw[: match.end()]
    new = frontmatter + new_body
    if new != raw:
        path.write_bytes(new.encode("utf-8"))
        return True
    return False


def build_index():
    notes, mocs = [], []
    for path in sorted(CONCEPTS.glob("*.md"), key=lambda p: p.stem.lower()):
        raw = path.read_bytes().decode("utf-8").replace("\r\n", "\n")
        match = FRONTMATTER.match(raw)
        fields = parse_fields(match.group(1) or "") if match else {}
        body = raw[match.end():] if match else raw
        title = re.search(r"^# (.+)$", body, re.M)
        title = title.group(1).strip() if title else path.stem
        area = fields.get("area") or []
        area = [area] if isinstance(area, str) else area
        headings, related, structure, section, fence = [], [], [], None, None
        for line in body.split("\n"):
            fence = fence_state(line, fence)
            if fence == "code":
                continue
            if line.startswith("## "):
                section = line[3:].strip()
                if not RELATED.match(line):
                    headings.append(section)
                    structure.append(f"  - {section}:")
                continue
            links = [l.split("|")[0].strip() for l in LINK.findall(line) if l.strip()]
            if section in ("Related", "Related Notes"):
                related += links
            elif links and structure:
                structure[-1] += " " + ", ".join(links)
            elif links:
                structure.append("  - " + ", ".join(links))
        related = list(dict.fromkeys(related))
        notes.append(f"- {path.stem} | {title} | {fields.get('type', '')} | {fields.get('status', '')} | "
                     f"{', '.join(area)} | {'; '.join(headings)} | {', '.join(related)}")
        if fields.get("type") == "moc":
            parents = f"\n  - parents: {', '.join(related)}" if related else ""
            mocs.append(f"### {path.stem}\n" + "\n".join(structure) + parents)
    text = ("---\ntype: system\n---\n# Vault Index\n\nGenerated by `_System/organize.py`. Do not edit by hand.\n\n"
            "## MOCs\n\n" + "\n\n".join(mocs) + "\n\n## Notes\n\n"
            "file | title | type | status | area | headings | related\n\n" + "\n".join(notes) + "\n")
    if not INDEX.exists() or INDEX.read_text("utf-8") != text:
        INDEX.write_text(text, "utf-8", newline="\n")
        return True
    return False


def report():
    """Print signs of drift. Read-only."""
    notes = {}
    for path in CONCEPTS.glob("*.md"):
        raw = path.read_bytes().decode("utf-8").replace("\r\n", "\n")
        match = FRONTMATTER.match(raw)
        fields = parse_fields(match.group(1) or "") if match else {}
        area = fields.get("area") or []
        targets = [l.split("|")[0].split("#")[0].strip() for l in LINK.findall(raw) if l.strip()]
        notes[path.stem] = {"fields": fields, "area": [area] if isinstance(area, str) else area, "targets": targets}
    names = {n.lower(): n for n in notes}

    mocs = [n for n, d in notes.items() if d["fields"].get("type") == "moc"]
    reached, stack = set(mocs), list(mocs)
    while stack:
        for target in notes[stack.pop()]["targets"]:
            name = names.get(target.lower())
            if name and name not in reached:
                reached.add(name)
                stack.append(name)
    moc_areas = {a for n in mocs for a in notes[n]["area"]}
    outside = [n for n, d in notes.items() if n not in reached and moc_areas.intersection(d["area"])]

    sizes = {}
    for d in notes.values():
        for a in d["area"]:
            sizes[a] = sizes.get(a, 0) + 1

    variants = {}
    for d in notes.values():
        for target in d["targets"]:
            key = re.sub(r"[\s_-]", "", target.lower()).rstrip("s")
            variants.setdefault(key, set()).add(names.get(target.lower(), target))

    sections = [
        ("Notes without an area", [n for n, d in notes.items() if not d["area"]]),
        ("Notes not reachable from their area's MOC", outside),
        ("Areas over 10 notes without a MOC", [f"{a} ({c})" for a, c in sizes.items() if c > 10 and a not in moc_areas]),
        ("Links that may mean the same note", [", ".join(sorted(v)) for v in variants.values() if len(v) > 1]),
    ]
    for title, items in sections:
        print(f"{title}: {len(items)}")
        for item in sorted(items):
            print(f"  {item}")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if "--report" in sys.argv:
        report()
        return
    changed = [p.name for p in sorted(CONCEPTS.glob("*.md")) if organize_note(p)]
    index_changed = build_index()
    print(f"Notes changed: {len(changed)}")
    for name in changed:
        print(f"  {name}")
    print(f"Index {'updated' if index_changed else 'unchanged'}")


if __name__ == "__main__":
    main()
