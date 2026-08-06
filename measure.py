#!/usr/bin/env python3
"""
Centres the text column on the reading pages.

Every paragraph is capped at 60ch, which is a good measure and should not
change. The problem is that Heart, About, Method and Richter use a container
sized for the canvas: 1160px wide holding a 560px column, so six hundred
pixels sit empty and all of it on the right.

Centring the column splits that space evenly and the page reads as composed
rather than as text that failed to reach the edge. The canvas and auction
pages keep the full width, because what they hold is not prose.
"""
import os, sys, shutil, datetime

IDX = "index.html"
if not os.path.exists(IDX): sys.exit("run from the site directory")
shutil.copy(IDX, "index.premeasure.%s.html" % datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
print("backed up")

s = open(IDX, encoding="utf-8").read()

anchor = "  section{display:none;padding-top:40px}"
add = '''  /* Reading pages centre their column. Everything in them is capped at 60ch,
     so in a container built for a 64 by 64 canvas the text occupied the left
     half and left the right half empty. Centring splits the space and the
     measure stays where it should be.

     The canvas and auction pages are excluded: what they hold is a picture
     and a set of controls, not prose, and both want the room. */
  section[data-tab="heart"] > *,
  section[data-tab="about"] > *,
  section[data-tab="method"] > *,
  section[data-tab="richter"] > *{
    max-width:62rem;
    margin-left:auto;
    margin-right:auto;
  }
  /* Full bleed inside those pages for anything that is an object rather than
     a paragraph: the heart plate, the glow table, the Richter grid. */
  section[data-tab="heart"] > .hplate,
  section[data-tab="heart"] > .hscroll,
  section[data-tab="richter"] > .plate{max-width:none}

'''
assert anchor in s, "section rule not found"
s = s.replace(anchor, add + anchor, 1)
open(IDX, "w", encoding="utf-8").write(s)
print("text columns centred on heart, about, method and richter")
