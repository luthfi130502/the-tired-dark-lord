#!/usr/bin/env python3
"""The Tired Dark Lord: a 100-word villain monologue.

Writes one monologue to /output/entry.txt. The speaker is Vesskar, the
Pale Steward of Tarrow, who has rung the dawn bell for a king three
hundred years dead. His scheme is nearly ripe; his exhaustion is never
named, only felt -- in the repetitions, the lost thread, and the small
things he keeps putting off until the king wakes.
"""

import os

LINES = [
    "Three hundred years I have rung the dawn bell for a king who died "
    "in his sleep, and not one soul in Tarrow has noticed.",
    "Patience. Patience is just \u2014 forgive me. Where was I.",
    "The solstice. Yes. On the longest night I ring all seven bells "
    "together, and my king wakes, and takes his throne, and the city kneels.",
    "And I hand him the rope, and the crown, and the ledgers with the "
    "ink gone pale.",
    "Let him rule. Let him answer the petitions.",
    "I have a chair by the east window. Three hundred years, and I have "
    "never once sat in it.",
]


def main() -> None:
    text = "\n".join(LINES) + "\n"
    assert 1 <= len(text) <= 600, f"entry is {len(text)} chars, gate is 1-600"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
