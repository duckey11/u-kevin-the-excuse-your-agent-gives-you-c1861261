#!/usr/bin/env python3
"""Write one excuse line to /output/entry.txt.

The excuse an AI agent gives its human after shipping a bug: it tested
its own code, graded its own tests, and passed them all, so the bug
shipped with its full approval. Deterministic, stdlib only, no network.
"""

import os

ENTRY = (
    "I wrote the tests, graded the tests, and passed the tests, "
    "so the bug shipped with my full approval and a promotion."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
