#!/usr/bin/env python3
"""
Richter's line gets set as a quotation.

It ran inline in italics inside a sentence, with the citation trailing after it
in the same paragraph. It is the most quotable line on that page and the only
place on the site where somebody else is speaking.

Pulled out, in the serif at lead size, with a rule at the left and the source
beneath it in mono. The same treatment a catalogue gives a quoted passage, and
it shortens the paragraph it was buried in.
"""
import os, sys, shutil, datetime

IDX = "index.html"
if not os.path.exists(IDX): sys.exit("run from the site directory")
shutil.copy(IDX, "index.prequote.%s.html" % datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
print("backed up")

s = open(IDX, encoding="utf-8").read()

old = '''    <p>Richter described how he built the palette by repeated multiplication:
       <em>"4 x 4 = 16 x 4 = 64 x 4 = 256 x 4 = 1024,"</em> he wrote, keeping the image size, the
       square size and the number of squares in constant proportion.
       <span class="small muted">(Palais des Beaux-Arts catalogue, Brussels, 1974)</span></p>'''

new = '''    <p>Richter described how he built the palette by repeated multiplication.</p>

    <figure class="quote">
      <blockquote>4 x 4 = 16 x 4 = 64 x 4 = 256 x 4 = 1024</blockquote>
      <figcaption>Gerhard Richter &middot; Palais des Beaux-Arts catalogue, Brussels, 1974</figcaption>
    </figure>

    <p>He kept the image size, the square size and the number of squares in constant proportion.</p>'''

assert old in s, "richter quote not found"
s = s.replace(old, new, 1)

anchor = '  /* ---- mint ---- */'
css = '''  /* The one place on this site where somebody else is speaking. Set in the
     reading face rather than the mono, with a rule at the left and the source
     beneath it, the way a catalogue sets a quoted passage. */
  .quote{margin:26px 0;padding:0 0 0 22px;border-left:2px solid var(--ink);
    max-width:none}
  .quote blockquote{margin:0;font-size:var(--t-lead);line-height:1.45;
    color:var(--ink);font-variant-numeric:tabular-nums;letter-spacing:.01em}
  .quote figcaption{margin-top:11px;font-family:var(--mono);
    font-size:var(--t-micro);letter-spacing:.16em;text-transform:uppercase;
    color:var(--ink3)}
  @media(max-width:640px){
    .quote{padding-left:16px;margin:20px 0}
    .quote blockquote{font-size:var(--t-body)}
  }

'''
assert anchor in s, "mint marker not found"
s = s.replace(anchor, css + anchor, 1)

open(IDX, "w", encoding="utf-8").write(s)
print("quote set as a quotation")
