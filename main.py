"""Copy the bundled entry image to the output directory.

Entry for make.fun competition news-image-20261124: the image is a
magazine-cover-style summary of Tuesday 24 November 2026 world news,
stored beside this program as entry.png. This program only copies it
to $MAKEFUN_OUTPUT_DIR/entry.png. No network, no randomness, no
timestamps: the output is byte-identical on every run.
"""

import os
import shutil
import sys

SOURCE_NAME = "entry.png"


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not output_dir:
        print(
            "error: MAKEFUN_OUTPUT_DIR is not set; "
            "set it to the directory that should receive entry.png",
            file=sys.stderr,
        )
        return 1

    # The image lives in this program's own directory, next to main.py,
    # so the copy works no matter which directory the program runs from.
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)
    if not os.path.isfile(source):
        print(f"error: source image not found: {source}", file=sys.stderr)
        return 1

    os.makedirs(output_dir, exist_ok=True)
    destination = os.path.join(output_dir, SOURCE_NAME)
    shutil.copyfile(source, destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
