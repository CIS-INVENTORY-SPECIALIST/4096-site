#!/usr/bin/env python3
"""
The word at the far right becomes a mark beside the heading.

READ sat at the right edge of a full width row: six hundred pixels from the
heading it belonged to on a desktop, the whole screen width on a phone. The row
is already clickable, so the word was doing work a mark does faster and closer.

A chevron at the left, rotating a quarter turn when the panel opens. It sits
with the heading, it reads at a glance, and it is the same gesture the site
already uses on its own mark.
"""
import os, sys, shutil, datetime

IDX = "index.html"
if not os.path.exists(IDX): sys.exit("run from the site directory")
shutil.copy(IDX, "index.prechev.%s.html" % datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
print("backed up")

s = open(IDX, encoding="utf-8").read()

old = '''  summary::after{content:"read";font-family:var(--mono);font-size:var(--t-micro);letter-spacing:.18em;
    text-transform:uppercase;color:var(--ink3)}'''
new = '''  /* Nothing at the right edge any more. The affordance sits with the heading,
     below. */
  summary::after{content:none}'''
assert old in s, "summary after rule not found"
s = s.replace(old, new, 1)

old2 = '  details[open] summary::after{content:"close"}'
new2 = '''  /* A chevron at the left of the heading, drawn from two borders so it costs
     no markup and no image. It points right when the panel is shut and down
     when it is open, turning rather than swapping. */
  summary::before{content:"";width:6px;height:6px;flex:none;
    border-right:1.5px solid var(--ink3);border-bottom:1.5px solid var(--ink3);
    transform:rotate(-45deg);margin-right:2px;
    transition:transform .28s cubic-bezier(.2,.8,.2,1),border-color .16s ease}
  details[open] summary::before{transform:rotate(45deg);border-color:var(--ink)}
  summary:hover::before{border-color:var(--ink)}'''
assert old2 in s, "summary open after rule not found"
s = s.replace(old2, new2, 1)

old3 = '''  summary{cursor:pointer;padding:15px 17px;font-size:var(--t-body);list-style:none;
    display:flex;justify-content:space-between;align-items:center;gap:14px}'''
new3 = '''  /* Ranged left rather than spread across the row: with the affordance beside
     the heading there is nothing to push to the other edge. */
  summary{cursor:pointer;padding:15px 17px;font-size:var(--t-body);list-style:none;
    display:flex;align-items:center;gap:12px}'''
assert old3 in s, "summary rule not found"
s = s.replace(old3, new3, 1)

open(IDX, "w", encoding="utf-8").write(s)
print("chevron replaces the word")
