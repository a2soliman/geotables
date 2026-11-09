#!/usr/bin/env python3
"""
Fails if a module's IN:/OUT: docstring header disagrees with DATAFLOW.md.

A module's contract (what structure goes in, what comes out) is stated
twice on purpose: once in the module docstring (where you're reading
code) and once in DATAFLOW.md (where you're reviewing the project at a
glance). This script is what keeps those two from drifting apart --
without it, the docstring is just a comment nobody is forced to update.
"""

import ast
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "src" / "geotables"
DATAFLOW_PATH = REPO_ROOT / "DATAFLOW.md"

HEADER_RE = re.compile(r"^(IN|OUT):\s*(.+)$")
TABLE_ROW_RE = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|$")


def parse_module_header(py_file: Path) -> tuple[str, str] | None:
    tree = ast.parse(py_file.read_text())
    doc = ast.get_docstring(tree)
    if not doc:
        return None
    in_val = out_val = None
    for line in doc.splitlines():
        m = HEADER_RE.match(line.strip())
        if m:
            key, val = m.groups()
            if key == "IN":
                in_val = val.strip()
            else:
                out_val = val.strip()
    if in_val is None or out_val is None:
        return None
    return in_val, out_val


def parse_dataflow_table() -> dict[str, tuple[str, str]]:
    rows = {}
    for line in DATAFLOW_PATH.read_text().splitlines():
        m = TABLE_ROW_RE.match(line.strip())
        if m:
            module, in_val, out_val = m.groups()
            rows[module] = (in_val.strip().strip("`"), out_val.strip().strip("`"))
    return rows


def main() -> int:
    table = parse_dataflow_table()
    errors = []

    for py_file in sorted(SRC_DIR.glob("*.py")):
        if py_file.name == "__init__.py":
            continue
        module_name = py_file.name
        header = parse_module_header(py_file)
        if header is None:
            errors.append(f"{module_name}: missing IN:/OUT: header in module docstring")
            continue
        if module_name not in table:
            errors.append(f"{module_name}: has a header but no row in DATAFLOW.md")
            continue
        if header != table[module_name]:
            errors.append(
                f"{module_name}: docstring and DATAFLOW.md disagree\n"
                f"  docstring:   IN={header[0]!r} OUT={header[1]!r}\n"
                f"  DATAFLOW.md: IN={table[module_name][0]!r} OUT={table[module_name][1]!r}"
            )

    source_modules = {p.name for p in SRC_DIR.glob("*.py") if p.name != "__init__.py"}
    for stale in set(table) - source_modules:
        errors.append(f"DATAFLOW.md: row for {stale!r} has no matching module in src/geotables/")

    if errors:
        print("DATAFLOW.md is out of sync with module headers:\n")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"DATAFLOW.md matches {len(source_modules)} module headers.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
