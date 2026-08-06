# 4096 — SESSION HANDOFF

Everything a new session needs to continue without losing anything. Read this
first, then `checklist.md` for what is left.

Written 5 August 2026, end of a long site session.

---

## WHO

Andrew, tenfin9ers / @Tenfin9erz, 27, Springfield IL. Anonymous as the artist
behind 4096 and -prophet-. Writes lowercase, direct, no em dashes. Wallet
`0x388B31b759b771E479C051fF29084DFCd81C4D88`.

## WHAT IS LIVE

**4096** — 4,096 pixels on one 64×64 canvas, each a token. Colour comes only
from trading: velocity is how often it sells, rhythm how uneven the gaps are,
patience the longest unbroken hold. Nobody picks the colours, including him.

    collection   0xEB46ebc19dB1814B6F72eD68ec752631B8F4FF2C
    renderer     0x18aCbF40FF1C2Ae97D11fc7d895AF01254116239
    heartbeat    0x4C9db8E4997F3044b9D4CF0a6B255B85ba3ffb61
    deploy block 25,621,173
    site         fourzeroninesix.xyz

**State as of writing.** 176 minted of 4,096. Two sales. Twelve holders. The
heart has flatlined: seven days with no trade takes glow to zero, and one sale
anywhere brings it straight back to full.

**Proofs4096** — built, 91 tests passing, audited with Slither and Aderyn, full
drop cycle run on a mainnet fork. Not deployed. Waiting on three confirmed
collaborators. Frontend built and deliberately removed from the site until
there is something real to show.

**Also running.** A sweeper on Railway keeping marketplace metadata current,
and a trade light on the Mac that flashes a LIFX bulb the colour of any pixel
that changes hands.

---

## THE RULES THAT DO NOT MOVE

1. The contract is immutable. No logic changes to 4096 or Renderer4096.
2. The sealed threshold and its salt are secret. Never in chat, never in a
   terminal, never in a file.
3. Never reward trading mechanically. Proofs reward having qualified, not the
   act of trading.
4. No VC, no investors.
5. Trust is redirected to code, not asked for.
6. No announced dates, no countdowns, no hype.
7. Proofs: announce the collaborator, never the drop.

---

## THE VOICE

Full document in `4096-voice.md`. The one rule: **state the fact, accept the
outcome, do not argue for it.**

Never: superlatives, roadmaps, gamification, mascots, "click here", asking for
engagement, explaining a decision nobody questioned, spinning a number.

Always: the uncomfortable number first, imperfect results published, credit
given specifically, mistakes admitted before anyone finds them.

His own lines are the reference: *this fills in or it doesn't* — *i wrote the
rules and then stopped* — *nobody has seen it finished. it isn't finished.*

---

## HOW WE WORK

Every one of these came from getting something wrong in this session.

**Read the code before proposing a fix.** Grep the actual rule, print the
actual markup. Three confident guesses about a cause were wrong and cost
several rounds each.

**Do not diagnose from a scaled screenshot.** The canvas was called broken from
a zoomed-out image. It renders correctly: the white band is the 176 minted
pixels and the boundary lands exactly where 176 of 4,096 puts it.

**Measure with the console rather than the eye.** The stray rule under the
ledger labels took six rounds of guessing and thirty seconds of
`getComputedStyle`.

**Check desktop and mobile before writing, not after.** The first nav fix drew
an underline in the burger menu, where nothing is underlined.

**Anchor strings must match exactly.** Several patches failed on whitespace or
on a selector that was `.navgroup .sub` rather than `.sub`. Print with `repr()`
when a match fails.

**Prefer removing a cause to adding an override.** `:not(.glowtable)`, a child
combinator, moving a rule's position. A stylesheet full of `!important` cannot
be reasoned about.

**Comment the reason, not the mechanic.** Every rule that exists because of a
specific failure says what the failure was.

**One item at a time. Verify. Then the next.**

**Know when to stop.** Two things were parked rather than perfected: the
loading placeholder shift and a decorative hairline. Both were right calls.

---

## THINGS ALREADY LEARNED — do not rediscover

**The canvas is fine.** White at the top is minted, grey below is unminted.
Never try to "fix" it.

**`sizeCanvas` uses an integer `CELL` from 5 to 12.** Never constrain the canvas
with CSS `max-height` — that scales it by a fraction and blurs a grid whose
whole point is that it is exact. Constrain the input to the cell calculation.

**It computes the offset above it rather than measuring.** A hidden section
measures as zero, so a function that answers differently depending on which tab
is open makes the canvas jump when you switch back.

**`innerHeight` is not stable on mobile.** The URL bar collapses on scroll and
changes it by about eighty pixels mid-gesture.

**Alchemy returns 403 on localhost.** Chain data never loads locally. Layout and
type are still accurate; anything reading the chain must be checked live.

**Breakpoints are 1000, 860, 760, 640.** Consolidated from six. Do not add one.
1000 canvas two columns collapse · 860 heart overlay hides · 760 nav becomes a
burger · 640 phone.

**Type is seven steps** as variables in `:root`: `--t-micro 9`, `--t-meta 11`,
`--t-small 13`, `--t-body 15.5`, `--t-lead 19`, `--t-head 23`, `--t-title 29`.
Nothing should be a raw pixel value.

**`.counter` is shared** by the canvas ledger and the heart glow table, which
want opposite layouts. Always check both.

**`.code b` does three jobs** in the Method panels: `.lbl` for section labels,
`.eq` for standalone equations, and bare `<b>` for emphasis mid sentence. Style
by class, never by tag.

**Every tab switch goes through `goTab()`,** bound to the document, so any
element with `data-tab` works anywhere.

**The mobile nav marks the current page with a ground, not a rule.**

---

## THE VISUAL LANGUAGE

Print governs anything that is or represents the artwork: the plate, the mount,
the canvas, a caption under a work. Serif, hairlines, ink, paper.

Screen governs everything you touch or read for information: nav, buttons, the
mint control, stats, forms. Motion, states that respond.

The seam is the frame. Inside it is a printed object; outside it is software.

**The frames.** All three reproductions — canvas, Richter plate, auction
preview — hang in the black box moulding from the export tool: `#141412`,
padding on a `clamp()` so it scales, a groove stroked inside it, a white mat,
and a hairline on the work. The Richter grid has no hairline because it is
fully coloured and a line there reads as a gap.

**Colour means something.** `--vel` red is velocity, `--rhy` green is rhythm,
`--pat` blue is patience. The nav borrows the same three by position. The
Method channel panels carry a 4% wash of their own colour. Never introduce a
decorative colour.

---

## ENVIRONMENT

    site       ~/Desktop/4096-site      public, GitHub Pages
    contracts  ~/Desktop/4096           private
    sweeper    ~/Desktop/4096-sweeper   private, on Railway

    serve      python3 -m http.server 8000 --bind 0.0.0.0
               (he keeps this running in a separate terminal)
    phone      http://10.0.0.113:8000   — recheck with `ipconfig getifaddr en0`
    live       fourzeroninesix.xyz, about ninety seconds after a push

    RPC        export RPC="https://eth-mainnet.g.alchemy.com/v2/$(cat ~/Desktop/hoodies-graph/key.txt)"
    opensea    key expires 4 September 2026, get the full one before then

Verify every JS patch:

    node -e 'const h=require("fs").readFileSync("index.html","utf8");
      const lo=h.lastIndexOf("<script>"), lc=h.lastIndexOf("</script>");
      try{ new Function(h.slice(lo+8,lc)); console.log("js clean"); }
      catch(e){ console.log("ERR",e.message); }'

Patches are written as Python scripts, presented as files, copied from
`~/Downloads`, and run from the site directory. Small edits go inline as
heredocs. Always assert the anchor.

---

## OPEN, BEYOND THE SITE

**Stephen** gave five names: Takens, Diid, Andrew, YGG, Dav. Warned they are
busy. Nothing done with them yet. This is the thread that actually moves things.

**Harvey Rayner** — messaged, congratulating him on Jankpop and referencing
marfaMESH. No reply yet. Art Blocks drop 12 August.

**Marfa** — Art Blocks weekend 22 to 25 October. Lodging not booked and it
fills.

**The real constraint.** Not the site. Roughly a hundred people have seen 4096.
Everything else is downstream of that.

---

## WHERE THE SITE WORK STANDS

23 of 38 done. See `checklist.md`.

The two that matter most are 37 and 38, both parked until the list is finished:

**37 · Motion that means something.** The site is almost entirely still. Apple
and X move constantly and every movement reports a state.

**38 · Density.** These pages are generous with space and thin with
information. A technical audience reads density as respect.

He has said explicitly: finish the list first, then come back to those two.
