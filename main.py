"""Write the relaxation contest entry to the output directory."""

import os
import pathlib


ENTRY = """\
The wheel is still turning but no one’s foot is on the pedal. \
The clay sits centered on the bat, wide and wet, ringed where the \
fingers last drew through it. As the wheel slows the wobble that \
was always there but too fast to see comes through—a faint \
lurch at each rotation, then less, then almost none.

Water has pooled in the tray beneath. It circles with the wheel, \
lagging behind, settling toward the low side. A drip gathers on \
the rim and falls, and the sound of it landing in the bucket is \
the loudest thing in the room. The gap before the next one is longer.

The hum of the wheel has dropped in pitch, low enough to feel \
through the floor. The clay glistens where the sponge last touched \
it. Its wet surface catches the window light at the same point in \
each revolution, a bright crescent that stretches slower and slower \
until it holds.

The wheel turns once more, barely. The drip on the rim rounds but \
does not fall. The water in the tray settles flat.
"""


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    dest = pathlib.Path(output_dir())
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
