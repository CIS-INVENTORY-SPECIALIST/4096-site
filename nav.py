#!/usr/bin/env python3
"""
The nav gets a mark of its own.

Desktop: each item's underline draws in from the left on hover and stays for
the current page, and it carries one of the three channel colours rather than
ink. Colour on this site always means something, so the nav borrows the same
three rather than inventing a fourth.

Mobile: the burger morphs into a cross whose strokes are half channel colour
and half paper, so the mark only takes colour once it is open. The panel it
opens is revealed by a rule sweeping down it, with each label appearing as the
rule passes: the same hairline the site is built from, doing the revealing.
"""
import os, sys, shutil, datetime

IDX = "index.html"
if not os.path.exists(IDX): sys.exit("run from the site directory")
shutil.copy(IDX, "index.prenav.%s.html" % datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
print("backed up")

s = open(IDX, encoding="utf-8").read()

# ── desktop: the channel rule ─────────────────────────────────────────────
old = '''  nav button[aria-current="page"]::after{content:"";display:block;height:1px;
    background:var(--ink);margin-top:6px}'''
new = '''  /* The rule draws in from the left rather than appearing, and it takes one of
     the three channel colours rather than ink. Every other colour on this site
     means something; the nav borrows the same three rather than inventing a
     fourth. Position rather than name, so adding a page does not need a new
     rule. */
  nav button::after{content:"";display:block;height:1.5px;margin-top:6px;
    background:var(--ink);
    transform:scaleX(0);transform-origin:left;
    transition:transform .22s cubic-bezier(.2,.8,.2,1)}
  nav button:nth-child(3n+1)::after{background:var(--vel)}
  nav button:nth-child(3n+2)::after{background:var(--rhy)}
  nav button:nth-child(3n)::after{background:var(--pat)}
  nav button:hover::after,
  nav button[aria-current="page"]::after{transform:scaleX(1)}'''
assert old in s, "nav underline rule not found"
s = s.replace(old, new, 1)

# ── mobile: no rule under a stacked item ──────────────────────────────────
old2 = '    nav button[aria-current="page"]::after{display:none}'
new2 = '''    /* The stacked menu marks the current page with a ground, not a rule: a
       hairline under one full width row reads as a divider between two rows
       rather than as state. */
    nav button::after{display:none}'''
assert old2 in s, "mobile after rule not found"
s = s.replace(old2, new2, 1)

# ── the burger ────────────────────────────────────────────────────────────
old3 = None
for cand in ['  .navtoggle{', '.navtoggle{']:
    if cand in s: old3 = cand; break
assert old3, "navtoggle rule not found"

i = s.index(old3)
j = s.index('}', i) + 1
burger = '''  /* Three strokes that become a cross, each half a channel colour and half
     paper, so the mark only takes colour once it is open. The middle stroke
     leaves first and the outer two follow, which reads as the thing folding
     rather than snapping. */
  .navtoggle{display:none;width:44px;height:44px;padding:0;border:1px solid var(--rule);
    background:var(--mount);cursor:pointer;position:relative;
    -webkit-tap-highlight-color:transparent}
  .navtoggle span{position:absolute;left:11px;width:22px;height:2px;background:var(--ink);
    transition:transform .38s cubic-bezier(.2,.8,.2,1),opacity .22s ease,
                background .38s ease}
  .navtoggle span:nth-child(1){top:15px}
  .navtoggle span:nth-child(2){top:21px}
  .navtoggle span:nth-child(3){top:27px}
  .navtoggle[aria-expanded="true"] span:nth-child(1){
    background:linear-gradient(to right,var(--vel) 0 50%,var(--mount) 50% 100%);
    transform:translateY(6px) rotate(45deg)}
  .navtoggle[aria-expanded="true"] span:nth-child(2){opacity:0}
  .navtoggle[aria-expanded="true"] span:nth-child(3){
    background:linear-gradient(to right,var(--mount) 0 50%,var(--pat) 50% 100%);
    transform:translateY(-6px) rotate(-45deg)}
'''
s = s[:i] + burger + s[j:]

# ── the panel: a rule sweeps down and the labels appear behind it ─────────
old4 = '    nav#nav.open{display:block !important}'
new4 = '''    nav#nav.open{display:block !important}

    /* A hairline travels the height of the panel and each label appears as it
       passes. The rule is the same one the site is built from; here it does
       the revealing rather than the dividing. */
    nav#nav::before{content:"";position:absolute;left:0;right:0;top:0;height:1.5px;
      background:var(--ink);opacity:0;z-index:2;pointer-events:none}
    nav#nav.open::before{animation:navsweep .52s cubic-bezier(.4,0,.2,1) forwards}
    @keyframes navsweep{
      from{top:0;opacity:1}
      to{top:100%;opacity:1}
    }
    nav#nav button{opacity:0}
    nav#nav.open button{animation:navink .01s linear forwards}
    @keyframes navink{to{opacity:1}}
    nav#nav.open button:nth-child(1){animation-delay:.05s}
    nav#nav.open button:nth-child(2){animation-delay:.12s}
    nav#nav.open button:nth-child(3){animation-delay:.19s}
    nav#nav.open button:nth-child(4){animation-delay:.26s}
    nav#nav.open button:nth-child(5){animation-delay:.33s}
    nav#nav.open button:nth-child(6){animation-delay:.40s}
    nav#nav.open button:nth-child(7){animation-delay:.47s}

    /* Motion is decoration here; the menu has to work without it. */
    @media(prefers-reduced-motion:reduce){
      nav#nav.open::before{animation:none;opacity:0}
      nav#nav.open button{animation:none;opacity:1}
      nav#nav button{opacity:1}
    }'''
assert old4 in s, "nav open rule not found"
s = s.replace(old4, new4, 1)

open(IDX, "w", encoding="utf-8").write(s)
print("desktop channel rule, burger morph, panel sweep")
