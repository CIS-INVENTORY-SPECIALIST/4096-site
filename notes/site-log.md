# 4096 SITE — WORKING LOG

Read this first in any new session. It carries the state, the method, and the
things already learned the hard way.

Last updated: 5 August 2026

---

## WHERE THINGS STAND

Working through `site-audit.md`, 33 items, top to bottom.

**Done**
- 1 · B1 duplicate sentence on Method, "From rank to colour" — removed
- 2 · B2 no active nav on Method — parent marks when a child is current, via
  `.navgroup:has([aria-current="page"])`, underline scoped to `min-width:761px`
  so the mobile burger keeps its background-only marker
- 3 · B3 MINTED shown twice on Canvas — dropped from the ledger, Sales added in
  its place; the progress bar already carries the mint count
- 4 · B4 stray rules under the ledger labels — `.sidebar .counter div` was
  matching `.k` and `.v` as well as the cell. Child combinator added to all
  four counter rules
- extra · the standfirst pushed the canvas below the fold; `sizeCanvas` now
  measures the frame's real offset and fits the viewport height, desktop only

- 5 · S1 Method panels capped at 60rem. The content is preformatted with hard
  line breaks in the source and the equations align on spaces, so it cannot
  reflow to fill a wider box. Fit the box to the text, not the other way round
- 6 · S2 and 7 · S3 solved together: reading pages cap and centre at 62rem.
  Cap the section, not each child, or it beats `p{max-width:60ch}` on
  specificity and stretches every paragraph
- 8 · S4 the canvas column centres on the work. Captions centre with what they
  caption; the standfirst above stays flush left because it introduces the page
- 9 · S5 Method promoted to the nav, dropdown and its CSS removed
- 12 · Y1 Your Pixels says a shared state once instead of nine times

**Next: 13 · Y2** — the empty bars on the pixel cards.

---

## HOW WE ARE WORKING

These are not preferences. Every one of them came from getting something wrong.

**Read the code before proposing a fix.** Grep for the actual rule, print the
actual markup. Three separate times a confident guess about a cause was wrong
and cost several rounds.

**Do not diagnose from a scaled screenshot.** The canvas was called broken on
the strength of a zoomed-out image. It renders correctly: the white band at the
top is the 176 minted pixels, grey below is unminted, and the boundary lands
exactly where 176 of 4,096 puts it. Measure with the console instead.

**Check desktop and mobile before writing, not after.** The first nav fix drew
an underline in the burger menu, where nothing is underlined. Every change gets
checked at both.

**Anchor strings must match the file exactly.** Two patches failed on
whitespace and on a selector that was `.navgroup .sub` rather than `.sub`.
Print with `repr()` first when a match fails.

**Prefer removing a cause to adding an override.** The glow table was fixed
with `:not(.glowtable)`, the ledger with a child combinator, the border order
by moving a rule rather than adding `!important`. A stylesheet full of
overrides cannot be reasoned about.

**Comment the reason, not the mechanic.** Every rule that exists because of a
specific failure says what the failure was.

**One item at a time. Verify. Then the next.**

---

## THINGS ALREADY LEARNED

**The canvas is fine.** Do not try to fix it. White at the top is minted, grey
is unminted.

**`sizeCanvas` uses an integer `CELL` between 5 and 12.** Never constrain the
canvas with CSS `max-height` — that scales it by a fraction and blurs a grid
whose whole point is that it is exact. Constrain the input to the cell
calculation instead.

**`innerHeight` is not stable on mobile.** The URL bar collapses on scroll and
changes it by roughly eighty pixels mid-gesture. Anything that feeds
`innerHeight` into layout has to be desktop only or the layout jumps.

**Breakpoints are 1000, 860, 760, 640.** Consolidated from six. Do not add a
new one without a reason that cannot be served by these.
- 1000 · canvas two columns collapse to one
- 860 · heart overlay hides, text stacks below
- 760 · nav becomes a burger
- 640 · phone: type drops, padding tightens, grids stack, 44px targets

**Type is on seven steps**, a minor third apart, as variables in `:root`:
`--t-micro 9`, `--t-meta 11`, `--t-small 13`, `--t-body 15.5`, `--t-lead 19`,
`--t-head 23`, `--t-title 29`. Nothing should be a raw pixel value.

**`.counter` is shared** by the Canvas ledger and the Heart glow table. They
want opposite layouts. Anything touching it needs both checked.

**The mobile nav marks the current page with a background, not an underline.**

**The nav has a mark of its own now.** Desktop: the underline draws in from the
left and takes one of the three channel colours by position, `nth-child(3n+1)`
and so on. Mobile: the burger morphs to a cross with each stroke half channel
colour and half ink, driven by `aria-expanded` rather than a class so the state
a screen reader announces and the state you can see are one thing. The panel is
revealed by a rule sweeping down it, with `clip-path` on the panel matching the
sweep so the white ground and the labels arrive together rather than the ground
appearing first.

**The panel is `width:max-content`** and ranged right under the button, because
the burger sits on the outer edge and left aligned labels under it read as two
objects that happen to overlap.

**Header order on mobile is wordmark, wallet, burger.** Neither control has a
box: two side by side, one bordered and one bare, read as different kinds of
thing.

**Every tab switch goes through `goTab()`,** bound to the document rather than
to the nav, so any element with `data-tab` works anywhere. Bound to the nav
alone, the buttons on About and Your Pixels silently did nothing.

**Alchemy returns 403 on localhost.** Chain data never loads locally, so the
canvas is empty and the heart does not beat. Layout and type are still
accurate. Anything reading the chain has to be checked on the live site.

---

## THE VISUAL LANGUAGE

Print governs anything that is or represents the artwork: the plate, the mount,
the canvas, the caption under a work. Serif, hairlines, ink borders, paper.
Never animated, never shadowed, never rounded.

Screen governs everything you touch or read for information: nav, buttons, the
mint control, stats, forms. Motion, states that respond, real spacing.

The seam is the frame. Inside it is a printed object. Outside it is software.

---

## ENVIRONMENT

    site repo    ~/Desktop/4096-site        (public, GitHub Pages)
    contracts    ~/Desktop/4096             (private)
    sweeper      ~/Desktop/4096-sweeper     (private, on Railway)

    serve        python3 -m http.server 8000 --bind 0.0.0.0
    phone        http://10.101.4.194:8000
    live         fourzeroninesix.xyz  (about ninety seconds after a push)

    layout tool  audit.js — paste into the console.
                 audit() audit.fold() audit.overflow() audit.text()
                 audit.borders()

Verify a patch applied before moving on:

    node -e 'const h=require("fs").readFileSync("index.html","utf8");
      const lo=h.lastIndexOf("<script>"), lc=h.lastIndexOf("</script>");
      try{ new Function(h.slice(lo+8,lc)); console.log("js clean"); }
      catch(e){ console.log("ERR",e.message); }'

---

## OPEN QUESTIONS

**Dark mode.** Not decided. It is the most expected feature on a technical site
now and it changes the whole design language, so it is worth deciding before
much more styling happens.

**Fluid type.** The seven steps are fixed pixel values that jump at 640px.
`clamp()` would scale them smoothly between phone and desktop, one line per
variable. Worth doing.

**Container queries.** The pixel cards size by viewport but sit in a grid whose
column width varies, so a card in a narrow column and one in a wide column
should lay out differently. Only container queries can express that.

**Between-breakpoint testing.** Checking at the breakpoints is not enough. The
760 to 1000 gap where the sidebar and the mint panel disagreed was found by
dragging slowly through the range, and there are likely more.
