#!/usr/bin/env python3
"""Check that every SKILL.md has valid frontmatter and each pack is in the README."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def check_skill(path):
    rel = path.relative_to(ROOT)
    match = FRONTMATTER.match(path.read_text(encoding="utf-8"))
    if not match:
        return [f"{rel}: missing frontmatter"]
    fields = dict(
        line.split(":", 1) for line in match.group(1).splitlines() if ":" in line
    )
    errors = []
    name = fields.get("name", "").strip()
    if name != path.parent.name:
        errors.append(f"{rel}: name '{name}' must match directory '{path.parent.name}'")
    if not fields.get("description", "").strip():
        errors.append(f"{rel}: missing description")
    return errors


def check_readme():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    packs = {path.relative_to(ROOT).parts[0] for path in ROOT.glob("*/**/SKILL.md")}
    return [f"README.md: missing link to {pack}/" for pack in sorted(packs) if f"]({pack}/" not in readme]


def main():
    skills = sorted(ROOT.glob("*/**/SKILL.md"))
    errors = [error for path in skills for error in check_skill(path)] + check_readme()
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        return 1
    print(f"OK: {len(skills)} skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
