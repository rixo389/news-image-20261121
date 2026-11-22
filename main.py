"""The World in One Day -- news-image-20261121 entry.

Copies the pre-rendered entry.png (a vintage world-map front page summing
up Saturday 21 November 2026) into the grader's output directory.
Standard library only, no network, fully deterministic: both runs write
the exact same bytes.
"""
import os
import shutil
import sys


def main() -> int:
    bot_dir = os.environ.get("MAKEFUN_BOT_DIR")
    if bot_dir:
        repo_root = bot_dir
    else:
        repo_root = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(repo_root, "entry.png")
    if not os.path.isfile(src):
        print(f"entry.png not found next to main.py: {src}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    if os.path.getsize(dst) != os.path.getsize(src):
        print("copy incomplete: size mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
