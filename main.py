import os

ENTRY_TEXT = "Left the party early. Finally, a quiet room.\n"


def output_directory():
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if configured:
        return configured
    return "/output"


def main():
    directory = output_directory()
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
