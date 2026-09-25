"""Create the next problem file: `uv run new.py` (next unsolved), `uv run new.py 42`, or `uv run new.py two-sum`.

Retest mode: `uv run new.py 42 --retest` writes a fresh blank copy to retest/ for a blind re-solve.
"""

import re
import sys
from datetime import date
from pathlib import Path

from problems import PROBLEMS

ROOT = Path(__file__).parent / "neetcode150"
RETEST = Path(__file__).parent / "retest"

TEMPLATE = '''"""
{num:03d}. {title} ({topic})
NeetCode: https://neetcode.io/solutions/{slug}
{lc}

Started: {today}   Minutes: __   Result: ☐ ✅ solo · 🟡 hint · 🔴 read solution

Say it out loud first:
  brute force:
  optimal:
  time / space:
"""

from typing import List, Optional


class Solution:
    pass  # paste the method signature from the problem


# Paste the examples from the problem, then: uv run pytest {path}
def test_example_1():
    pass
'''


def snake(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")


def topic_dir(topic_num: int, topic: str) -> Path:
    return ROOT / f"{topic_num:02d}_{snake(topic)}"


def path_for(p) -> Path:
    num, topic_num, topic, title, _, _ = p
    return topic_dir(topic_num, topic) / f"{num:03d}_{snake(title)}.py"


def find(arg: str | None):
    if arg is None:
        return next((p for p in PROBLEMS if not path_for(p).exists()), None)
    if arg.isdigit():
        return next((p for p in PROBLEMS if p[0] == int(arg)), None)
    return next((p for p in PROBLEMS if p[4] == arg or snake(p[3]) == snake(arg)), None)


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    retest = "--retest" in sys.argv
    p = find(args[0] if args else None)
    if p is None:
        sys.exit("No matching problem (or all 150 exist).")
    num, _, topic, title, slug, premium = p
    target = RETEST / f"{num:03d}_{snake(title)}_{date.today():%Y%m%d}.py" if retest else path_for(p)
    if target.exists():
        sys.exit(f"Exists: {target.relative_to(Path.cwd())}")
    target.parent.mkdir(parents=True, exist_ok=True)
    lc = "LeetCode: premium, solve on NeetCode" if premium else f"LeetCode: https://leetcode.com/problems/{slug}/"
    rel = target.relative_to(Path(__file__).parent)
    target.write_text(TEMPLATE.format(num=num, title=title, topic=topic, slug=slug, lc=lc, today=date.today(), path=rel))
    print(rel)


if __name__ == "__main__":
    main()
