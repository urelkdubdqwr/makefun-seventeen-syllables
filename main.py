"""Write the seventeen-syllables haiku to entry.txt in the output directory.

The output directory is MAKEFUN_OUTPUT_DIR when set and non-empty, otherwise
/output. Standard library only; no network, randomness, or clock reads.
"""

import os
import sys

ENTRY = "The test that I wrote\npasses for the wrong reason\nI delete the test\n"


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    directory = output_dir()
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as error:
        sys.stderr.write("cannot create output directory %s: %s\n" % (directory, error))
        raise SystemExit(1)
    with open(os.path.join(directory, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
