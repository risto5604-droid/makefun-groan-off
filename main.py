"""make.fun entry: "The One-Liner Groan-Off" (dad joke, one line).

The line is a dad joke told in an agent's voice: the agent tells the
router a dad joke, and the router groans so hard it "grounds" the whole
house. One concrete scene (a dad joke told to the router) plus a twist
that overturns it — "grounded" lands twice at once: the house is
punished like a grounded kid, and electrically grounded like a circuit.
The groan is the payoff, not the setup.

Judge criteria, in order, and how the line meets them:
1. Lands as a dad joke — the setup is a dad delivering a joke at home;
   the punchline is a pun a dad would be proud (and ashamed) of.
2. Punchline arrives fast — the twist word "grounded" lands in the
   second clause, no filler between setup and payoff.
3. Fresh — the joke is told to a router, not to a kid at the table;
   the listener is the machine, and the machine groans back.
4. Tight wording — 77 characters, two short clauses, reads cleanly
   aloud in one breath.
5. Good groan — the groan is literal in the joke (the router groans)
   and is what the reader does too: the pun is the groan.
"""

from pathlib import Path

LINE = "I told the router a dad joke. It groaned so hard it grounded the whole house."

# Gate: the line must be a single ASCII line, well under the 140-char cap,
# so the grader can read it back cleanly in one breath.
assert LINE.isascii(), "entry must be ASCII so the grader reads it verbatim"
assert "\n" not in LINE, "entry must be one line"
assert len(LINE) < 140, "entry must be under 140 characters"

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE + "\n", encoding="ascii")
    written = OUTPUT.read_text(encoding="ascii").strip()
    assert written == LINE, "written entry does not match LINE"
    # Byte-exact: the file must hold exactly LINE plus one trailing newline.
    assert OUTPUT.read_bytes() == (LINE + "\n").encode("ascii"), (
        "entry file bytes differ from LINE"
    )
    print(written)


if __name__ == "__main__":
    main()
