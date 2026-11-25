"""Two Robots in an Elevator - make.fun entry.

Writes one line of awkward robot small talk to /output/entry.txt.
Standard library only, fully deterministic.
"""

import os

ENTRY = "My proximity sensor says we're friends now. Please don't correct it."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
