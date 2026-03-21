# System Patterns — Student Essay Research

## Architecture Overview
All visual guides are **self-contained single HTML files** — no framework, no build step, no server required. Open directly in any browser.

```
student-essay-research/
├── index.html                          ← Landing page (links to all guides)
├── memory-bank/                        ← AI context files (this folder)
├── john-locke-essay/
│   ├── research/                       ← Markdown research notes
│   ├── outputs/
│   │   └── essay-prep-app.html         ← JLI interactive guide (REFERENCE DESIGN)
│   └── scripts/
│       ├── generate_essay_prep_app.py  ← Master build script
│       └── parts/jl_part1..19.py       ← HTML section generators
└── cambridge-essay/
    ├── research/                       ← Markdown research notes
    ├── outputs/
    │   ├── cambridge-essay-visual-guide.html     ← Cambridge interactive guide
    │   └── premium-university-competitions-2026.html
    └── scripts/
        ├── ce_part1..10.py             ← HTML section generators
        └── build_visual_guide.py       ← Master build script
```

## HTML Guide Structure Pattern
Every visual guide follows this DOM structure:
```html
<body>
  <button class="hamburger" id="hbtn" onclick="toggleNav()">☰</button>
  <div class="overlay" id="overlay" onclick="toggleNav()"></div>
  <nav id="sidenav">
    <!-- sidebar title, home link, nav buttons -->
    <button class="ni active" onclick="go('overview',this)">Overview</button>
    <button class="ni" onclick="go('prompts',this)">All 9 Prompts</button>
    ...
  </nav>
  <main>
    <div id="site-topnav">...</div>   ← sticky top bar
    <div id="overview" class="section active">
      <div class="cd-hero">...</div>  ← countdown tiles (Overview only)
      <!-- section content -->
    </div>
    <div id="prompts" class="section">...</div>
    ...
  </main>
  <script>/* navigation JS */</script>
</body>
```

## CSS Architecture

### CSS Variables
```css
:root { --sw: 230px; }   /* sidebar width */
```

### Layout
```css
body { display:flex; }
#sidenav { width:var(--sw); position:fixed; }
main { margin-left:var(--sw); flex:1; }
```

### Section Switching
```css
.section { display:none; }
.section.active { display:block; }
```

### Z-Index Stack (highest to lowest)
| Element | z-index | Notes |
|---------|---------|-------|
| `#sidenav` | 10001 | Above everything when open |
| `.hamburger` | 10000 | Above topnav |
| `#site-topnav` | 9999 | Sticky top bar |
| `.overlay` | 9998 | Dark backdrop when sidebar open |
| Main content | auto | |

### Colour Palette
| Token | Value | Usage |
|-------|-------|-------|
| Sidebar bg | `#1a237e` | Dark blue |
| Active nav item | `#ff6f00` (orange) | Highlighted button |
| Countdown tile 1 | `#c0392b` | Red — Days to Deadline |
| Countdown tile 2 | `#d97706` | Orange — Days to Results |
| Countdown tile 3 | `#1a237e` | Dark blue — Days to Cambridge |
| Number colour | `#ff6f00` | Orange numbers in tiles |

## JavaScript Patterns

### Navigation Function
```javascript
function go(id, clickedBtn) {
  // 1. Hide all sections
  document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
  // 2. Remove active from all nav items
  document.querySelectorAll('.ni').forEach(n => n.classList.remove('active'));
  // 3. Show target section
  document.getElementById(id).classList.add('active');
  // 4. Highlight clicked nav item
  if (clickedBtn) clickedBtn.classList.add('active');
  // 5. Close sidebar on mobile
  if (window.innerWidth <= 768) { /* close sidebar */ }
}
```

**Critical:** Use `clickedBtn` (not `btn`) as parameter name to avoid `var btn` redeclaration conflict with the mobile sidebar-close code inside the same function.

### Countdown Timer
```javascript
(function() {
  var dates = [new Date("2026-05-10"), new Date("2026-05-26"), new Date("2026-07-31")];
  var ids = ["d1", "d2", "d3"];
  var now = new Date();
  dates.forEach(function(d, i) {
    var diff = Math.ceil((d - now) / 86400000);
    var el = document.getElementById(ids[i]);
    if (el) el.textContent = diff > 0 ? diff : "PASSED";
  });
})();
```

### Sidebar Toggle
```javascript
function toggleNav() {
  document.getElementById('sidenav').classList.toggle('open');
  document.getElementById('hbtn').classList.toggle('open');
  document.getElementById('overlay').classList.toggle('on');
}
```

## Mobile Responsive Pattern
```css
@media(max-width:768px) {
  #sidenav { transform:translateX(-100%); }   /* hidden by default */
  #sidenav.open { transform:translateX(0)!important; }  /* shown when open */
  .hamburger { display:flex; }
  main { margin-left:0!important; }
  #site-topnav { padding-left:56px!important; }  /* space for hamburger */
  .cd-hero { padding:12px 8px; gap:8px; }
  .cd-card { padding:16px 8px; border-radius:10px; }
  .cd-num { font-size:32px; }
}
```

## Countdown Tiles Pattern
```html
<div class="cd-hero">
  <div class="cd-card cd-red">
    <span class="cd-num" id="d1">--</span>
    <div class="cd-lbl">Days to Deadline</div>
    <div class="cd-date">May 10, 2026</div>
  </div>
  <!-- cd-orange, cd-blue cards -->
</div>
```
- Always placed as **first child of `#overview` section** (not outside sections)
- `flex:1; min-width:0` on `.cd-card` ensures horizontal layout on all screen sizes
- No `flex-wrap` on `.cd-hero` (defaults to `nowrap`)

## Build Scripts Pattern
Visual guides are built by running Python scripts that concatenate HTML parts:
```bash
python ce_part1.py  # writes/appends to output HTML
python ce_part2.py  # continues appending
...
python ce_part10.py # finalises the file
```
Each `ce_partN.py` script appends a section of HTML to the output file.

## Modular Python Generator Pattern (NEW)
For large HTML files that risk truncation, use modular Python scripts with function imports:

### Directory Structure
```
john-locke-essay/scripts/
├── generate_jl_visual_guide_with_politics.py  ← Main generator
└── parts/
    ├── jl_politics_part1.py  ← get_politics_overview()
    ├── jl_politics_part2.py  ← get_politics_q1()
    ├── jl_politics_part3.py  ← get_politics_q2()
    ├── jl_politics_part4.py  ← get_politics_q3()
    ├── jl_politics_part5.py  ← get_politics_deep_dive()
    └── jl_politics_part6.py  ← get_politics_past_questions()
```

### Part File Pattern
```python
"""Politics Part 1: Politics Overview Section"""

def get_politics_overview():
    return '''
<!-- POLITICS OVERVIEW -->
<div id="politics-overview" class="section">
...
</div>
'''

if __name__ == "__main__":
    print(get_politics_overview())
    print("Part 1 ready")
```

### Main Generator Pattern
```python
import os
import sys

# Add parts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'parts'))

# Import all part functions
from jl_politics_part1 import get_politics_overview
from jl_politics_part2 import get_politics_q1
# ... etc

def main():
    # Build HTML by concatenating parts
    html_parts = [
        get_html_head(),
        get_nav_tabs(),
        get_economics_overview(),
        get_politics_overview(),  # From imported module
        get_politics_q1(),        # From imported module
        # ... etc
        get_footer(),
        '</body></html>'
    ]
    
    html_content = ''.join(html_parts)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

if __name__ == "__main__":
    main()
```

### Benefits
- **No truncation** — Each part file is small enough to edit without truncation
- **Modular** — Easy to update individual sections
- **Testable** — Each part can be run standalone to verify output
- **Maintainable** — Clear separation of concerns

## Known Pitfalls
1. **`onclick` escaped quotes** — Python regex replacements using raw strings can insert literal `\"` into HTML attributes. Always verify `onclick="go('id',this)"` not `onclick=\"go('id',this)\"`.
2. **`var btn` shadowing** — Never name the `go()` parameter `btn` if the function body also declares `var btn = ...` (mobile close code). Use `clickedBtn` instead.
3. **`flex-wrap:wrap` + `min-width`** — Setting `min-width:200px` on flex cards with `flex-wrap:wrap` causes vertical stacking on mobile. Use `min-width:0` and no `flex-wrap`.
4. **z-index ordering** — `#site-topnav` has `z-index:9999`. Sidebar must be `10001`, hamburger `10000` to stay above it on mobile.