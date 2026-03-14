# Progress — Student Essay Research

## What Works

### John Locke Institute (JLI) Guide — `essay-prep-app.html`
- ✅ Full interactive guide with sidebar navigation
- ✅ 3 countdown tiles (horizontal, colored) on Dashboard/Overview
- ✅ Sections: Dashboard, Timeline & Plan, Q1 Cashless Society, Q2 Personalised Pricing, Q3 Jeff Bezos, Argument Frameworks, Past Questions, Reading List, Mentorship Orgs, My Checklist
- ✅ Mobile responsive (hamburger, sidebar slides in/out)
- ✅ **This is the reference design** — all other guides should match this UX

### Cambridge Re:think Guide — `cambridge-essay-visual-guide.html`
- ✅ Sidebar navigation (dark blue, orange accents)
- ✅ 7 sections: Overview, All 9 Prompts, Strategy, Essay Structure, Reading Lists, Timeline, Checklist
- ✅ 3 countdown tiles (red/orange/blue) on Overview only
- ✅ Tiles horizontal on all screen sizes (no flex-wrap, min-width:0)
- ✅ Mobile hamburger visible (z-index:10000, above topnav)
- ✅ Mobile sidebar links work (sidenav z-index:10001)
- ✅ Countdown timer JS working (d1, d2, d3 IDs)
- ✅ All committed and pushed to GitHub

### Premium University Competitions Guide — `premium-university-competitions-2026.html`
- ✅ Exists and has content
- ⚠️ Not yet updated with new sidebar/navigation pattern
- ⚠️ May have old hero/navigation structure

### Landing Page — `index.html`
- ✅ Links to all three guides

---

## What's Left to Build / Improve

### High Priority
- [ ] **Cambridge guide content review** — verify all 9 prompts, dates, prizes are accurate for 2026
- [ ] **Premium competitions guide** — update to match new sidebar pattern (if needed)

### Medium Priority
- [ ] **Cambridge guide: add section title** — add "Cambridge Re:think Overview" heading above countdown tiles (like JLI's "Competition Dashboard")
- [ ] **Cambridge guide: scroll-to-top on nav** — add `window.scrollTo(0,0)` in `go()` function so switching sections always shows content from the top
- [ ] **JLI guide: verify dates** — confirm JLI 2026 deadline is still April 2026

### Low Priority
- [ ] **GitHub Pages setup** — configure repo for GitHub Pages so guides are accessible via URL
- [ ] **index.html polish** — improve landing page design
- [ ] **Research notes** — continue adding research for Cambridge prompts

---

## Bugs Fixed (Historical)

| Date | Bug | Fix |
|------|-----|-----|
| Mar 14, 2026 | Cambridge sidebar had no CSS (no background, no positioning) | Added `#sidenav{...}` rule |
| Mar 14, 2026 | Orphaned `#side` CSS fragment corrupted `@media` block | Rewrote `@media(max-width:768px)` block |
| Mar 14, 2026 | `go()` JS parameter `btn` shadowed by `var btn` inside function | Renamed parameter to `clickedBtn` |
| Mar 14, 2026 | `onclick` attributes had escaped quotes `\"` | Used `str.replace()` instead of regex raw strings |
| Mar 14, 2026 | Countdown tiles stacking vertically on mobile | Removed `flex-wrap:wrap`, set `min-width:0` on cards |
| Mar 14, 2026 | Countdown tiles showing on all sections | Moved `cd-hero` inside `#overview` section div |
| Mar 14, 2026 | Mobile hamburger hidden behind topnav | Raised hamburger z-index to 10000 |
| Mar 14, 2026 | Mobile sidebar links unclickable | Raised sidenav z-index to 10001 |

---

## Repository Stats
- **Total commits:** ~15+ (as of March 14, 2026)
- **Latest commit:** `75114bd` — Cambridge guide: reduce countdown tile font sizes
- **Branch:** `main`
- **Remote:** https://github.com/rkmaheshglobal/student-essay-research.git