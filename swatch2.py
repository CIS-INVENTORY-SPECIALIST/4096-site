#!/usr/bin/env python3
"""
Cards go back to white; the swatch gets a ground of its own.

Putting the whole card on paper solved the invisible swatch but cost the cards
their presence: nine outlined regions in the page's own colour read as areas
rather than objects.

The problem was never the card. It was that a white pixel had nothing to be
white against. So give the swatch a small paper tile to sit on, the way a plate
sits in a mount, and leave everything else alone.
"""
import os, sys, shutil, datetime

IDX = "index.html"
if not os.path.exists(IDX): sys.exit("run from the site directory")
shutil.copy(IDX, "index.preswatch2.%s.html" % datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
print("backed up")

s = open(IDX, encoding="utf-8").read()

old = '''  /* Paper, not mount. The swatch is the only white on the card, so a pixel that
     has never sold reads as white rather than as an empty box, and one that has
     reads as colour against a ground instead of against more white. */
  .card{border:1px solid var(--rule);padding:16px;background:var(--paper);cursor:pointer;
    transition:border-color .14s ease,background .14s ease}
  .card:hover{background:var(--mount)}'''
new = '''  .card{border:1px solid var(--rule);padding:16px;background:var(--mount);cursor:pointer;
    transition:border-color .14s ease}'''
assert old in s, "card rule not found"
s = s.replace(old, new, 1)

old2 = '''  /* Hung like everything else on this site: a mount, an ink hairline, and the
     colour inside it. At this size the border is the frame. */
  .chip{width:38px;height:38px;flex:none;background:var(--mount);
    box-shadow:inset 0 0 0 1px var(--ink);
    background-clip:padding-box}'''
new2 = '''  /* The colour sits on a paper tile rather than directly on the card, so a
     pixel that has never sold has something to be white against. Hung the way
     everything else here is: a ground, a hairline, the work inside it. */
  .chip{width:38px;height:38px;flex:none;position:relative;
    background:var(--paper);padding:5px;box-sizing:border-box;
    box-shadow:inset 0 0 0 1px var(--rule)}
  .chip::after{content:"";position:absolute;inset:5px;
    background:inherit;box-shadow:inset 0 0 0 1px rgba(27,27,25,.28)}'''
assert old2 in s, "chip rule not found"
s = s.replace(old2, new2, 1)

open(IDX, "w", encoding="utf-8").write(s)
print("cards white again, swatch on a paper tile")
