"""Write the relaxation contest entry to the output directory."""

import os
import pathlib


ENTRY = """\
The porch boards still hold the afternoon's warmth. You feel it through \
your socks, steady and even, the way a hand rests on your back without \
pressing. A blanket lies across your knees. Not because you need it. \
Because it was there.

The dog beside the chair is on her side, one ear folded under. Her \
breathing has its own slow pace. Every few minutes she sighs, and each \
time the pause before the next sigh stretches a little longer.

Past the garden a woodpigeon calls, two low notes and a pause, then \
two again. The sound comes the way the smell of cut grass comes when \
the air shifts, faint and gone and faint again.

The light is the colour of warm stone now. It crosses the floorboards \
so slowly you notice only when it reaches the next knot in the grain. \
A little farther each time. A little softer.

The blanket is warmer. The boards are still warm. The dog breathes \
out, slow and long, and the quiet that follows has no edge to it.
"""


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    dest = pathlib.Path(output_dir())
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
