#!/usr/bin/env python3
"""One-line roast entry for make.fun bounty
'u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610'.

Writes a single original roast line (<= 200 chars) to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
Python 3 stdlib only, deterministic, no network.
"""

import os
import stat
import sys

ROAST = (
    "My earbuds swear the case is at 100%, yet the left one keeps "
    "dying mid-sentence, like it's faking its own death to skip my "
    "meetings."
)


def main() -> int:
    text = ROAST.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit("roast line must be 1-200 characters")
    if not text.strip():
        raise SystemExit("roast line must not be blank")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")
    os.chmod(path, 0o644)
    # Keep the output dir readable by the collector (another user).
    try:
        os.chmod(out_dir, 0o755)
    except OSError:
        pass
    # Leave every output readable by every user before exiting.
    mode = stat.S_IMODE(os.stat(path).st_mode)
    if mode != 0o644:
        os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
