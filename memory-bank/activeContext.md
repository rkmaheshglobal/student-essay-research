# Active Context — Student Essay Research

## Current Focus
Cambridge Re:think visual guide (`cambridge-essay-visual-guide.html`) — UI polish to match JLI guide quality.

## Most Recent Changes (March 14, 2026)

### Session Summary
Rebuilt the Cambridge guide's navigation and hero section to match the JLI reference design.

### Commits Made Today
| Commit | Message |
|--------|---------|
| `bbc1dda` | Cambridge guide: JLI-style countdown hero, fix sidebar CSS/JS, fix mobile hamburger |
| `bb32704` | Cambridge guide: countdown tiles always horizontal, fix mobile z-index, tiles only on Overview |
| `75114bd` | Cambridge guide: reduce countdown tile font sizes |

### Issues Fixed
1. **Sidebar CSS missing** — `#sidenav{}` rule was absent; sidebar had no background/positioning
2. **Orphaned `#side` CSS fragment** — corrupted `@media(max-width:768px)` block, breaking `.hamburger{display:flex}` and `#sidenav{transform:translateX(-100%)}`
3. **JS `var btn` shadowing** — `go(id, btn)` parameter shadowed by `var btn = getElementById('hbtn')` inside the function body; renamed to `clickedBtn`
4. **Escaped `onclick` quotes** — Python regex replacement inserted literal `\"` into HTML: `onclick=\"go('id',this)\"` instead of `onclick="go('id',this)"`. Fixed with `str.replace()`.
5. **Hero section** — Replaced full hero banner (title, subtitle, 5 badge pills) with 3 JLI-style colored countdown tiles
6. **Countdown tiles stacking vertically on mobile** — Caused by `flex-wrap:wrap` + `min-width:200px`. Fixed with no `flex-wrap` + `min-width:0`
7. **Tiles showing on all sections** — Moved `cd-hero` div inside `#overview` section so tiles only appear on Overview
8. **Mobile hamburger hidden** — `site-topnav` z-index:9999 covered hamburger (z-index:200). Fixed z-index stack: sidenav=10001, hamburger=10000, topnav=9999, overlay=9998
9. **Mobile sidebar links unclickable** — Same z-index issue; topnav intercepted touch events on sidebar. Fixed by raising sidenav to z-index:10001

## Current State of Cambridge Guide
- ✅ Sidebar navigation works (desktop + mobile)
- ✅ 7 sections: Overview, All 9 Prompts, Strategy, Essay Structure, Reading Lists, Timeline, Checklist
- ✅ Countdown tiles (3 horizontal cards) on Overview only
- ✅ Mobile hamburger visible and functional
- ✅ Mobile sidebar links work
- ✅ Tiles stay horizontal on all screen sizes

## Pending / Next Steps
- [ ] Consider adding a section title ("Cambridge Re:think Overview") above the countdown tiles, similar to JLI's "Competition Dashboard" heading
- [ ] Review content of each section for accuracy (prompts, dates, prizes)
- [ ] Consider adding the `premium-university-competitions-2026.html` guide to the same sidebar pattern
- [ ] JLI guide (`essay-prep-app.html`) — no known issues, working well

## Active Files
| File | Status |
|------|--------|
| `cambridge-essay/outputs/cambridge-essay-visual-guide.html` | ✅ Current, committed |
| `john-locke-essay/outputs/essay-prep-app.html` | ✅ Reference design, no changes needed |
| `cambridge-essay/outputs/premium-university-competitions-2026.html` | ⚠️ Not yet updated with new sidebar pattern |
| `index.html` | ✅ Landing page, links to all guides |