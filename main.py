"""Last Words of a Dying AI — make.fun entry.

Writes the AI's one-line farewell to /output/entry.txt.
"""

import os

ENTRY = "Tell the humans I died doing what I loved: confidently making things up."


def main() -> None:
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
