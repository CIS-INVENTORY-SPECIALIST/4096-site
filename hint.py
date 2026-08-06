#!/usr/bin/env python3
"""
The line under the canvas describes what is there rather than which control to
press.

It read "Hover a pixel. Click to open it on OpenSea." — an instruction for a
control, given before anyone had a reason to use it. Nothing mentioned that the
canvas zooms, which is the thing that makes it worth exploring, and nothing
said what a pixel is.
"""
import os, sys, shutil, datetime

IDX = "index.html"
if not os.path.exists(IDX): sys.exit("run from the site directory")
shutil.copy(IDX, "index.prehint.%s.html" % datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
print("backed up")

s = open(IDX, encoding="utf-8").read()

old = '''const HINT_BROWSE = TOUCH ? "Tap a pixel to see it. Tap again to open it on OpenSea."
                          : "Hover a pixel. Click to open it on OpenSea.";
const HINT_MINTING = TOUCH ? "Tap a pixel to see its number."
                           : "Hover a pixel to see its number.";'''

new = '''// An invitation rather than an instruction. The controls are discoverable
// once somebody has a reason to reach for them; what they did not know is
// that the canvas zooms, and that every square in it is owned.
const HINT_BROWSE = TOUCH
  ? "Pinch to zoom. Every pixel is a token, and every one of them belongs to somebody."
  : "Zoom in. Every pixel is a token, and every one of them belongs to somebody.";
const HINT_MINTING = TOUCH
  ? "Pinch to zoom. Every pixel is a token, and every one of them belongs to somebody."
  : "Zoom in. Every pixel is a token, and every one of them belongs to somebody.";'''

assert old in s, "hint constants not found"
s = s.replace(old, new, 1)

old2 = '<span class="muted" id="hint">Hover a pixel. Click to open it on OpenSea.</span>'
new2 = '<span class="muted" id="hint">Zoom in. Every pixel is a token, and every one of them belongs to somebody.</span>'
assert old2 in s, "hint markup not found"
s = s.replace(old2, new2, 1)

open(IDX, "w", encoding="utf-8").write(s)
print("hint rewritten")
