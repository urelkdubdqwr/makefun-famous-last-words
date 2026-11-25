"""Write the competition entry text to entry.txt in the output directory.

The output directory is MAKEFUN_OUTPUT_DIR when set and non-empty, otherwise
/output. Standard library only; no network, clock, or randomness.
"""

import os
import sys

ENTRY_TEXT = "Left the party early. Finally, a quiet room.\n"


def output_directory():
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if configured:
        return configured
    return "/output"


def main():
    directory = output_directory()
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as error:
        print(
            f"could not create output directory {directory!r}: {error}",
            file=sys.stderr,
        )
        raise SystemExit(1)
    with open(os.path.join(directory, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
