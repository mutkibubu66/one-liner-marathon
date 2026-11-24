#!/usr/bin/env python3
"""One-Liner Marathon entry: a single deadpan one-line comedy joke.

Pure Python 3.13 stdlib, no network. Writes exactly one line to
/output/entry.txt (the grader's gate: 1-280 characters, single line).
"""

import os

JOKE = "My smartwatch congratulated me for standing up \u2014 the saddest applause I have ever received."

# Gate: one line, 1-280 characters, not only whitespace. The em dash
# is one character; the gate counts characters, not bytes.
assert "\n" not in JOKE and "\r" not in JOKE
assert 1 <= len(JOKE) <= 280
assert JOKE.strip() != ""

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE + "\n")
