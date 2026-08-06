#!/usr/bin/env python3
"""
The card takes the paper ground so the swatch can be the white thing on it.

A white pixel in a white square on a white card is correct and invisible. Put
the card on paper and the relationship inverts: the swatch is the only mount on
it, so an untraded pixel reads as white rather than as an empty box, and a
traded one reads as colour against a ground rather than against more white.

It also lightens the page. Nine white slabs on paper read as panels floating on
the page; nine paper cards separated by hairlines read as part of it.
"""
import os, sys, shutil, datetime

IDX = "index.html"
if not os.path.exists(IDX): sys.exit("run from the site directory")
shutil.copy(IDX, "index.preswatch.%s.html" % datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
print("backed up")

s = open(IDX, encoding="utf-8").read()

old = '  .card{border:1px solid var(--rule);padding:16px;background:var(--mount);cursor:pointer}'
new = '''  /* Paper, not mount. The swatch is the only white on the card, so a pixel that
     has never sold reads as white rather than as an empty box, and one that has
     reads as colour against a ground instead of against more white. */
  .card{border:1px solid var(--rule);padding:16px;background:var(--paper);cursor:pointer;
    transition:border-color .14s ease,background .14s ease}
  .card:hover{background:var(--mount)}'''
assert old in s, "card rule not found"
s = s.replace(old, new, 1)

old2 = '  .chip{width:38px;height:38px;border:1px solid var(--rule);flex:none}'
new2 = '''  /* Hung like everything else on this site: a mount, an ink hairline, and the
     colour inside it. At this size the border is the frame. */
  .chip{width:38px;height:38px;flex:none;background:var(--mount);
    box-shadow:inset 0 0 0 1px var(--ink);
    background-clip:padding-box}'''
assert old2 in s, "chip rule not found"
s = s.replace(old2, new2, 1)

open(IDX, "w", encoding="utf-8").write(s)
print("cards on paper, swatch is the mount")
