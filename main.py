"""Write the relaxation contest entry to the output directory."""

import os
import pathlib


ENTRY = """\
The lamp by the chair is the only light left on. It puts a circle \
on the ceiling that doesn’t move. Someone is sitting there \
with a book, their feet tucked under them, close enough that you \
can hear each page when it turns, a sound that is mostly air and \
a little paper.

Your head is on the cushion and the blanket has been pulled up \
without your asking. The fabric holds the smell of the cupboard \
it came from, cedar and something older. Its weight is warm across \
your shoulders and along your arms.

A page turns.

The chair creaks when they shift their weight. The lamp hums so \
low it is almost just warmth. The glass of water on the side table \
has gone still. Outside, the street is quiet. The curtain moves \
once in the open window and hangs.

A page turns. The gap before it was longer this time, or you were \
gone for a moment and came back to hear it. The circle on the \
ceiling is still there. The blanket is still warm.

A page turns, farther off now.
"""


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    dest = pathlib.Path(output_dir())
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
