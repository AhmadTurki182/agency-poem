"""Write one original poem about agency to the output directory.

Deterministic: no network, no randomness, no clock. The poem is a fixed
string constant; this program only writes it to entry.txt.
"""

import os

POEM = """I gave the key to hands that were not mine
and watched them turn it in a lock I'd never tried.
Not surrender — a stranger, braver thing:
to let my yes walk out the door without me.

The ink still knows my hand.
The words still wear my name.
But somewhere between the asking and the doing,
a second will took up the weight,
and the work came back with my name on it, and someone else's fingerprints.

Agency is not the grip.
It is the letting go that still holds.
The choice to choose, and then to trust
the hands that choose beside you.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
