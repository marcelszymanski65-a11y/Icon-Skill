#!/usr/bin/env python3
"""Basic structural check for the icon-first-design skill package."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    ROOT / "SKILL.md",
    ROOT / "assets",
    ROOT / "references",
    ROOT / "scripts",
    ROOT / "references" / "icon-library-guide.md",
    ROOT / "references" / "usage-patterns.md",
]

missing = [path for path in REQUIRED if not path.exists()]
if missing:
    for path in missing:
        print(f"Missing: {path.relative_to(ROOT)}")
    sys.exit(1)

skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
if not skill_text.startswith("---\\n") or "\\nname: icon-first-design\\n" not in skill_text:
    print("SKILL.md is missing the expected YAML frontmatter or skill name.")
    sys.exit(1)

print("Skill package structure looks good.")
