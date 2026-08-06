# 4096 SITE AUDIT

All seven pages reviewed at desktop width: Canvas, Your Pixels, Heart, About,
Method, Richter, Auction.

Ordered by severity. Nothing here is a matter of taste unless marked.

---

## CORRECTION TO AN EARLIER NOTE

I previously called the canvas render broken. It is not.

The white region at the top of the grid is two full rows plus three quarters of
a third. That is 176 pixels of 4,096, which is exactly the mint count. Minted
pixels render white, unminted render grey, and the boundary lands where it
should. Same on the Auction page.

The canvas is correct. What follows about it is design, not repair.

---

## ACTUAL BUGS

### B1 · A sentence is printed twice
Method, "From rank to colour", first paragraph:

> Sixteen cubed is 4,096 possible colours, from 4,096 pixels. Sixteen cubed is
> 4,096 possible colours, from 4,096 pixels.

### B2 · No nav item is active on Method
Richter underlines RICHTER. Auction underlines AUCTION. Method underlines
nothing, so the most technical page on the site gives no indication of where
you are.

### B3 · MINTED appears twice in the same column
Canvas page. Once in the mint panel beside the progress bar, again in the stats
block roughly 240px below. Same number, same label, same column.

The count then appears a third time in the caption under the canvas: "176 of
4,096 minted."

### B4 · Stray rules under the stat labels
Canvas page. MINTED, REMAINING and TEAM each have a short hairline underneath
that stops after about sixty pixels. It does not reach the number, does not
span the cell, and does not appear anywhere else on the site.

---

## STRUCTURAL

### S1 · Method's panels use less than half their width
The accordion rows run the full 648px container. The content inside sits in a
column of about 315px. Every open section has more empty ground than content.

This is the most visible layout problem on the site and it is on the page
holding the best material.

### S2 · Heart's prose column is half its container
Same shape of problem. The body text runs to about 325px inside a 648px
container. The glow table below it runs to 425px. Neither relates to the other
or to the container.

### S3 · About mixes two widths on one screen
The prose column is about 390px. The three-channel table directly beneath it is
648px, the full container. The eye jumps from a narrow column to a wide table
and back to a narrow column.

Inside that table, MEASURES ends around 700px and TO RAISE IT begins at 890px,
leaving a large gap mid-row.

### S4 · Canvas mixes three alignments
The standfirst is left-aligned. The caption and helper text under the canvas
are centred. The buttons under those are centred. The mint panel beside it is
left-aligned.

### S5 · Method is not in the nav
It sits under an About dropdown. The strongest work on the site is the hardest
thing to find.

### S6 · Richter is one column of prose
One image at the top, then roughly fifteen paragraphs across four headings with
no other break. The writing is good and almost nobody will reach the end.

### S7 · The heart plate is unbalanced
Blocks 01 and 03 sit in the left column, 02 and 04 in the right, the heart and
05 in the middle. The right column has a large gap between 02 and 04 that the
left column does not have.

---

## YOUR PIXELS

### Y1 · The same sentence nine times
Every card reads "Never sold. Pure white, and it stays that way until it is."
Nine cards, nine identical lines, stacked in a grid.

It is true and it is correct, and printed nine times it reads as a template
rather than a description.

Say it once above the grid and let the cards carry only what differs.

### Y2 · Nine sets of empty bars
VELOCITY, RHYTHM and PATIENCE all read 0 with empty tracks, on every card. The
bars occupy about a third of each card and carry no information.

### Y3 · The swatch is invisible
A white square on a white card with a hairline border. For a page about colour,
the colour is the least visible thing on it.

### Y4 · No way to connect from the empty state
Disconnected, the page is one line of text in a card telling you to connect a
wallet, with no button. The only connect control is in the header.

---

## TYPOGRAPHIC

### T1 · Hard line breaks in the Method intro
Lines two and three break mid-thought because the breaks are hard-coded rather
than allowed to wrap. At any other window width they land somewhere worse.

### T2 · Code is not distinguished from prose
The equations sit in the same mono at the same size on the same ground as the
paragraphs around them, separated only by an indent.

### T3 · Weak hierarchy inside the Method panels
"What is measured", "How it becomes a number", "What this means for you" are
bold mono at the same size as the body mono beneath them.

### T4 · The Richter quote is not set as a quote
"4 x 4 = 16 x 4 = 64 x 4 = 256 x 4 = 1024" runs inline in italics. It is the
most quotable line on that page.

### T5 · The Richter image is unframed
Every other artwork on the site sits in a mount inside an ink border. This one
sits directly on the paper.

---

## INTERACTION

### I1 · READ and CLOSE sit far from their headings
Tiny grey mono at the far right of the row, roughly 600px from the heading it
belongs to, at the lowest contrast on the page.

### I2 · TIME REMAINING reads as a live countdown
24:00:00 in large serif under that label, on an auction page. It is not
counting. The sub-label explains, but the number has already said something
untrue.

### I3 · No deep links to Method sections
No way to send someone straight to the orthogonalisation.

---

## MOBILE — NEEDS TESTING

### M1 · Code blocks will overflow
`key = e x 32 + ((v - 2^e) x 32) / 2^e, capped at 1023` in mono at 375px will
run past the edge. This is the glow table problem again, in five places.

### M2 · The paired auction stat boxes
RESERVE and TIME REMAINING side by side with a vertical rule, large serif
numbers inside, about 160px each at 375px.

### M3 · The three-channel table on About
Three columns, the third far right. Already fixed for tables generally at
640px, worth confirming this one converts.

### M4 · READ and CLOSE at the far right of a narrow row
Whatever the desktop distance is, on a phone it is the full screen width from
the thing it belongs to.

### M5 · The heart plate's three columns
Already stacks at 860px. Worth confirming block 05 lands sensibly.

---

## WORTH CONSIDERING

Directions, not faults.

- **A theme.** Dark mode is the most expected feature on a technical site now
  and its absence is noticeable.
- **Live values.** The block number ticks in the footer. Minted, sales and glow
  could update in place rather than on refresh.
- **Density.** The pages are generous with space and thin with information. A
  technical audience reads density as respect.
- **Keyboard.** Numbers to switch tabs, escape to close a panel. The people who
  notice are exactly the audience.
- **The unminted grey.** Correct, and it reads to a first-time visitor as a
  canvas that has not loaded. Worth deciding whether that is acceptable.

---

## SUGGESTED ORDER

1. B1 to B4. Four small fixes, one afternoon.
2. S1, S2, S3. One decision about column width applied to three pages.
3. Y1 to Y4. Your Pixels is the page a holder returns to.
4. S5. Method into the nav.
5. Everything else.
