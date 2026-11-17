"""Write the relaxation contest entry to the output directory."""

import os
import pathlib


ENTRY = """\
The kitchen after midnight keeps its own quiet.
A tap finds the cup left soaking,
one drop, then another.
The fridge hums low, stops, hums again.
On the counter a pear darkens slowly
where the skin was nicked this afternoon.

The cloth on the faucet will dry by morning.
The salt left out will not mind the hours.
A glass of water stands untouched,
holding the light from the hall.

A moth circles the bulb above the stove,
its shadow wider than itself,
turning without urgency—
the way a thought turns
when you have forgotten
you were thinking it.
"""


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    dest = pathlib.Path(output_dir())
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
