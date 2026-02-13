#!/usr/bin/env python3
import re
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "SKILL.md"
text = p.read_text(encoding="utf-8")

checks = {
    "frontmatter_name": r"^---[\s\S]*name:\s*[^\n]+",
    "frontmatter_description": r"^---[\s\S]*description:\s*[^\n]+",
    "use_when": r"\nUse when\n",
    "do_not_use_when": r"\nDo not use when\n",
    "workflow": r"\nWorkflow\n",
    "fallback": r"\nFallback\n",
    "output_format": r"\nOutput format\n",
}

failed = [k for k,v in checks.items() if not re.search(v, text, re.MULTILINE)]
if failed:
    print("FAIL")
    for f in failed:
        print(f"- {f}")
    raise SystemExit(1)

print("PASS")
