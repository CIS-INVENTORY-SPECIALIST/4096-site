#!/usr/bin/env python3
"""
Puts every type size on one scale.

Twenty four sizes had accumulated across ninety four declarations, most of
them used two or three times. That is drift rather than design: nobody can
name the difference between 9.5px and 10px, but a page built from sizes that
relate to each other reads as considered and one built from sizes that do not
reads as assembled.

Seven steps, a minor third apart, written as variables so the whole scale can
be tuned from one place afterwards.
"""
import os, re, sys, shutil, datetime
from collections import Counter

IDX = "index.html"
if not os.path.exists(IDX): sys.exit("run from the site directory")
shutil.copy(IDX, "index.pretype.%s.html" % datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
print("backed up")

s = open(IDX, encoding="utf-8").read()

SCALE = [
    ("micro",  9.0),    # mono labels, uppercase, letterspaced
    ("meta",  11.0),    # mono readouts and captions
    ("small", 13.0),    # secondary prose
    ("body",  15.5),    # reading text
    ("lead",  19.0),    # sub headings
    ("head",  23.0),    # section headings
    ("title", 29.0),    # the wordmark
]

# the variables
anchor = '    --mono:"IBM Plex Mono",ui-monospace,monospace;'
assert anchor in s, "root block not found"
block = anchor + "\n\n    /* Type sits on seven steps a minor third apart. Every size on the page\n" \
        "       is one of these, so nothing is a pixel off something else for no\n" \
        "       reason. Tune the scale here rather than at the call site. */\n"
for name, px in SCALE:
    block += "    --t-%-6s %5.1fpx;\n" % (name + ":", px)
s = s.replace(anchor, block.rstrip("\n"), 1)

def nearest(v):
    return min(SCALE, key=lambda kv: abs(kv[1] - v))

# rewrite every declaration
changed = Counter()
def sub(m):
    v = float(m.group(1))
    name, target = nearest(v)
    if abs(target - v) >= 0.01:
        changed[(v, target)] += 1
    return "font-size:var(--t-%s)" % name

body_start = s.index("<style>")
head = s[:body_start]
rest = s[body_start:]
rest, n = re.subn(r"font-size:\s*([\d.]+)px", sub, rest)
s = head + rest

open(IDX, "w", encoding="utf-8").write(s)

print("%d declarations rewritten to variables" % n)
print()
for (was, now), count in sorted(changed.items()):
    print("  %5.1f -> %5.1f  %d use(s)" % (was, now, count))
