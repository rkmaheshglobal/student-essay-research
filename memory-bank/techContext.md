# Tech Context — Student Essay Research

## Technology Stack
| Layer | Technology | Notes |
|-------|-----------|-------|
| Frontend | Vanilla HTML + CSS + JavaScript | No frameworks, no dependencies |
| Build scripts | Python 3 | Generates HTML files from parts |
| Version control | Git + GitHub | https://github.com/rkmaheshglobal/student-essay-research |
| Hosting | GitHub Pages (optional) | Files work locally too |
| IDE | Visual Studio Code | Windows 11 |

## No External Dependencies
All HTML guides are fully self-contained:
- No CDN links (fonts loaded via Google Fonts `@import` in CSS only)
- No JavaScript libraries
- No CSS frameworks
- Works offline after first load

## Python Build Environment
- Python 3 (available as `python` on PATH)
- No pip packages required — scripts use only `os`, `re`, `sys` (stdlib)
- Scripts run from their own directory or from repo root

## File Naming Conventions
| Pattern | Example | Purpose |
|---------|---------|---------|
| `ce_partN.py` | `ce_part1.py` | Cambridge HTML section generator |
| `jl_partN.py` | `jl_part1.py` | JLI HTML section generator |
| `fix_*.py` | `fix_cam_hero.py` | One-off fix scripts (delete after use) |
| `check_*.py` | `check_sections.py` | Diagnostic scripts (delete after use) |
| `*-visual-guide.html` | `cambridge-essay-visual-guide.html` | Main output guides |

## Git Workflow
- Single branch: `main`
- Remote: `origin` → `https://github.com/rkmaheshglobal/student-essay-research.git`
- Commit directly to main (no PRs, solo project)
- Typical commit: `git add <file> && git commit -m "message" && git push`

## HTML File Sizes (approximate)
| File | Size |
|------|------|
| `cambridge-essay-visual-guide.html` | ~61 KB |
| `essay-prep-app.html` (JLI) | ~120 KB |
| `premium-university-competitions-2026.html` | ~80 KB |

## Browser Compatibility
- Targets modern browsers (Chrome, Firefox, Safari, Edge)
- Uses `classList`, `querySelectorAll`, `forEach` — ES5/ES6 compatible
- CSS uses `var()`, `flex`, `transform` — widely supported
- No IE11 support needed

## Development Workflow for HTML Fixes
When fixing the HTML guides directly (not rebuilding from scripts):
1. Write a Python fix script (`fix_*.py`) in the repo root
2. Run it: `python fix_*.py`
3. Verify output with checks in the script
4. Delete the fix script: `del fix_*.py`
5. Commit: `git add <html-file> && git commit -m "..." && git push`

## Key File Paths
```
c:\SAL-USP\student-essay-research\                          ← repo root (CWD)
c:\SAL-USP\student-essay-research\cambridge-essay\outputs\cambridge-essay-visual-guide.html
c:\SAL-USP\student-essay-research\john-locke-essay\outputs\essay-prep-app.html
c:\SAL-USP\student-essay-research\index.html