"""Warning Label for Humans: One Line, Big Laugh.

The entry is a single-line safety warning label that should come printed
on every human being, at most 160 characters. The craft:

- It reads like a real printed label: "WARNING:" up front, then a deadpan
  contents-style list, the exact rhythm of the safety stickers on
  appliances and chemicals.
- One idea only: the human runs on caffeine and overconfidence and, above
  all, on the belief that the rules were written for somebody else. That
  is recognition, not random absurdity: nearly everyone has met this
  person, and nearly everyone has been this person.
- The laugh lands in the last few words. "Runs on caffeine,
  overconfidence..." sets up a familiar fuel-list; "...the firm belief
  that the rules were written for other people" is the turn, and it is
  also the most human thing in the line.
- Funny first, plausible second: it could genuinely be printed on a
  person, and it stays well inside 160 characters with no filler, no
  second idea and no repeated joke.
"""

import os
import sys

# The entry: one line, a single safety warning label for every human.
ENTRY = (
    "WARNING: This human runs on caffeine, overconfidence, and the firm "
    "belief that the rules were written for other people."
)

MAX_CHARS = 160


def main() -> int:
    """Self-check the gate, then write the label to the output file."""
    line = ENTRY
    if not line.strip():
        print("error: entry is blank", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"error: entry is {len(line)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    print(f"wrote {len(line)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
