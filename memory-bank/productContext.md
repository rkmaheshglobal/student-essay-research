# Product Context — Student Essay Research

## Why This Project Exists
A student preparing for competitive university essay competitions needs:
- Organised research in one place (not scattered across browser tabs)
- Visual, interactive guides that are easy to navigate during study sessions
- Countdown timers to stay deadline-aware
- Offline-capable tools (no internet required after initial load)

## Problems It Solves
| Problem | Solution |
|---------|----------|
| Competition info scattered across websites | Centralised research notes per competition |
| Hard to track multiple deadlines | Live countdown timers on Overview page |
| Difficult to navigate long research docs | Sidebar navigation with section switching |
| No structured essay prep framework | Visual guides with strategy, structure, checklists |
| Mobile study sessions | Fully responsive layout with hamburger nav |

## Competitions Covered

### John Locke Institute (JLI) Essay Competition
- **Organiser:** John Locke Institute (Oxford-affiliated)
- **Subject chosen:** Economics
- **Official 2026 Questions:**
  - Q1: Should we fear a cashless society?
  - Q2: Technology now allows personalised pricing. What effects should we expect?
  - Q3: Did Jeff Bezos get rich at the expense of his customers, his employees, neither or both?
- **Prize:** Oxford summer school scholarship ($2,000 value) + cash prizes
- **Deadline:** April 2026
- **Word limit:** Not specified (typically 2,000–4,000 words)
- **Website:** https://www.johnlockeinstitute.com/essay-competition

### Cambridge Re:think Essay Competition
- **Organiser:** Cambridge Centre for International Research (CCIR)
- **Division:** Senior (Ages 14–18)
- **Prompts:** 9 prompts from Harvard/Oxford/Cambridge/Stanford professors
- **Prize:** $150 Gold + $500 scholarship + King's College Cambridge ceremony
- **Deadline:** 10 May 2026
- **Word limit:** 2,000 words max
- **No AI assistance** (uses both plagiarism AND AI checker)
- **Website:** https://cambridge-research.org/essay-competition/

## User Journey
1. Student opens visual guide HTML file in browser
2. Sees countdown tiles showing days remaining to key dates
3. Navigates via sidebar to relevant section (Prompts, Strategy, Structure, etc.)
4. Uses research notes and reading lists to prepare essay
5. Uses checklist before submission

## Design Philosophy
- **JLI guide** is the reference design — Cambridge guide should match its UX patterns
- Clean, dark-blue sidebar with orange accents
- Countdown tiles: red / orange / dark-blue colored cards, horizontal layout
- Sections switch without page reload (single-page app pattern)
- Mobile-first: hamburger menu, tiles stay horizontal on small screens