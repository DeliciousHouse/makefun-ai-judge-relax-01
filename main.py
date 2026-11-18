"""Write the relaxation contest entry to the output directory."""

import os
import pathlib


ENTRY = """\
Someone gave the hammock a push a while ago. You are still swaying, \
but only just, each arc shorter than the last, the ropes pulling at \
the top of each turn before they let you back. The canvas is cupped \
around you, holding your weight without gripping.

Overhead the leaves turn over and turn back as you pass beneath them. \
The light comes in pieces, warm on your arm and then gone and then \
warm again, each patch resting a little longer as you slow.

The ropes creak where they wrap the branch. At first it kept a steady \
rhythm, but the gaps have widened, and between them you can hear a \
gate down the lane, and then nothing at all.

Your heel brushes the ground at the low point of each pass. Just \
grazes it. The hammock lifts you back, less each time. The air is \
heavy and smells of clover. The turns shrink until you feel them in \
your stomach, a faint tip and return, and then you cannot tell if you \
are moving or the breeze is. It does not matter. You are held.
"""


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    dest = pathlib.Path(output_dir())
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
