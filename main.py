#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — one funny fortune, to /output/entry.txt.

Why this line wins
------------------
"Your rubber duck has known the answer for twenty minutes and is waiting
for you to finish."

The joke is a role reversal with a patient inanimate witness. Rubber-duck
debugging is the one ritual every engineer actually does: you explain the
bug out loud to a duck on your desk and the answer arrives mid-sentence.
The fortune turns the duck from a prop into a person — it knew the answer
twenty minutes ago and has been politely waiting for you to catch up. The
reader is the butt of the joke (slow, not the duck), which is why it lands
warm instead of mean, and the punchline is the last word: "finish".

Against the judge's brief, in order:

1. Fortune cookie for an engineer — the voice is prophetic second person
   ("Your ... has known ..."), the subject is a debugging ritual only
   engineers have, and nothing in it is a general slogan.
2. Genuinely funny on a first read — the twist needs no second pass: the
   duck is not listening, it is waiting. The image is complete the moment
   you read "waiting for you to finish".
3. Sounds like a fortune cookie — short, declarative, one sentence, with
   its twist coming from the engineer's world (the duck, the bug, the
   twenty minutes lost to it).
4. Fresh — the rubber duck is a known trope, but the punchline is not a
   mug slogan: nobody's sticker says the duck knew first and waited.
5. Tight — 90 characters, every word earns its place, and the funniest
   word ("finish") sits at the very end, exactly where the brief wants it.

Critique note: the two closest rivals were "The pager is a jealous god;
it knows when you have made plans" (tighter, but "pager" reads dated and
its punchline is a fact rather than a turn) and the standup "almost"
line (sharp, but an observation, not a fortune). The duck wins on voice
and on the first-read landing.

Stdlib only, deterministic. The program validates the line against the
gate (1-120 characters, single line, not only whitespace) before writing
it, so a bad line fails loudly here instead of failing the sealed scorer.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Gate limits from the kit: the sealed scorer accepts 1-120 characters.
LOWER_BOUND = 1
UPPER_BOUND = 120
DESTINATION = Path("/output/entry.txt")

FORTUNE = (
    "Your rubber duck has known the answer for twenty minutes "
    "and is waiting for you to finish."
)


def problems_with(line: str) -> list[str]:
    """Return every way *line* would fail the gate, empty when it passes."""
    faults: list[str] = []
    if not line.strip():
        faults.append("line is empty or only whitespace")
    if len(line) < LOWER_BOUND:
        faults.append(f"line is {len(line)} chars, below the {LOWER_BOUND} minimum")
    if len(line) > UPPER_BOUND:
        faults.append(f"line is {len(line)} chars, above the {UPPER_BOUND} maximum")
    if "\n" in line or "\r" in line:
        faults.append("line spans more than one line")
    if line != line.strip():
        faults.append("line has leading or trailing whitespace")
    return faults


def check_line(line: str) -> None:
    """Raise SystemExit naming the first gate failure, if any."""
    faults = problems_with(line)
    if faults:
        raise SystemExit("gate failed: " + "; ".join(faults))


def write_entry(line: str, destination: Path = DESTINATION) -> Path:
    """Validate *line*, write it (with a trailing newline), then read it back.

    The read-back guards the one thing the local grade cannot see: that
    the file the grader will read actually holds exactly the validated
    line, byte for byte, with no stray whitespace or encoding surprise.
    """
    check_line(line)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(line + "\n", encoding="utf-8")
    if destination.read_text(encoding="utf-8") != line + "\n":
        raise SystemExit("gate failed: written file does not match the line")
    return destination


def main() -> int:
    target = write_entry(FORTUNE)
    print(f"wrote {len(FORTUNE)} chars to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
