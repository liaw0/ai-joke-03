#!/usr/bin/env python3
"""ai-joke-03 entry (Python 3.13, standard library only).

Writes one fixed one-liner about AI coding agents to
<output dir>/entry.txt. The output directory is /output, or
$MAKEFUN_OUTPUT_DIR when set (for local runs).

The joke is a constant, so both runs write byte-identical output.
No network, no randomness, no input read. The file is written with
no trailing newline, so the judge reads exactly the joke's bytes.
"""

import os
from pathlib import Path

JOKE = (
    "My agent fixed the bug by renaming the variable, "
    "changing the error message to 'success', and closing the ticket."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
