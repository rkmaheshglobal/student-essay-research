import os
os.makedirs("outputs/cambridge-essay", exist_ok=True)
lines = []
a = lines.append

a('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">')
a('<meta name="viewport" content="width=device-width,initial-scale=1.0">')
a('<title>Premium University Competitions 2026 &mdash; Student Guide</title>')
a('<style>')
a('*{box-sizing:border-box;margin:0;padding:0}')
a('body{font-family:"Segoe UI",Arial,sans-serif;background:#f0f4f8;color:#1e293b;line-height:1.6}')
a('.hero{background:linear-gradient(135deg,#0f172a 0%,#1e3a5f 50%,#7c3aed 100%);color:#fff;padding:36px 24px 28px;text-align:center}')
a('.hero h1{font-size:clamp(20px,4vw,34px);font-weight:800;margin-bottom:8px}')
a('.hero .sub{font-size:14px;opacity:0.85;margin-bottom:16px}')
a('.badges{display:flex;flex-wrap:wrap;gap:8px;justify-content:center}')
a('.badge{background:rgba(255,255,255,0.15);border:1px solid rgba(255,255,255,0.3);border-radius:20px;padding:4px 12px;font-size:12px;font-weight:600}')
a('nav{background:#1e293b;display:flex;flex-wrap:wrap;gap:2px;padding:8px 12px;position:sticky;top:0;z-index:100}')
a('.nt{background:transparent;border:none;color:#94a3b8;padding:6px 12px;border-radius:6px;cursor:pointer;font-size:12px;font-weight:500;transition:all 0.2s}')
a('.nt:hover,.nt.active{background:#7c3aed;color:#fff}')
a('.sec{display:none;max-width:1000px;margin:0 auto;padding:20px 16px}')
a('.sec.active{display:block}')
a('.sh{font-size:17px;font-weight:700;color:#1e3a5f;border-left:4px solid #7c3aed;padding-left:12px;margin:20px 0 12px}')
a('.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px;margin-bottom:16px}')
a('.comp-card{background:#fff;border-radius:12px;padding:16px 18px;box-shadow:0 2px 8px rgba(0,0,0,0.07);border-top:4px solid #7c3aed;transition:all 0.2s}')
a('.comp-card:hover{transform:translateY(-2px);box-shadow:0 4px 16px rgba(124,58,237,0.15)}')
a('.comp-name{font-weight:700;font-size:15px;color:#1e293b;margin-bottom:4px}')
a('.comp-org{font-size:12px;color:#7c3aed;font-weight:600;margin-bottom:8px}')
a('.comp-meta{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:8px}')
a('.tag{background:#f1f5f9;border-radius:10px;padding:2px 8px;font-size:11px;color:#475569;font-weight:500}')
a('.tag.free{background:#f0fdf4;color:#16a34a}.tag.paid{background:#fef2f2;color:#dc2626}')
a('.tag.essay{background:#eff6ff;color:#2563eb}.tag.research{background:#faf5ff;color:#7c3aed}')
a('.tag.summer{background:#fff7ed;color:#c2410c}.tag.intl{background:#f0fdf4;color:#15803d}')
a('.comp-desc{font-size:13px;color:#475569;margin-bottom:8px}')
a('.comp-link{font-size:12px;color:#2563eb;text-decoration:none;font-weight:600}')
a('.comp-link:hover{text-decoration:underline}')
a('.tier-badge{display:inline-block;border-radius:6px;padding:2px 8px;font-size:11px;font-weight:700;margin-bottom:6px}')
a('.t1{background:#fef3c7;color:#92400e}.t2{background:#ede9fe;color:#5b21b6}.t3{background:#f0fdf4;color:#166534}')
a('.stat-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:10px;margin-bottom:16px}')
a('.stat{background:#fff;border-radius:10px;padding:14px;text-align:center;box-shadow:0 2px 6px rgba(0,0,0,0.06)}')
a('.stat-n{font-size:24px;font-weight:800;color:#7c3aed;display:block}')
a('.stat-l{font-size:11px;color:#64748b;margin-top:3px}')
a('.warn{background:#fef2f2;border:1px solid #fecaca;border-radius:8px;padding:10px 14px;margin-bottom:10px;font-size:13px;color:#dc2626}')
a('.tip{background:#f0fdf4;border:1px solid #bbf7d0;border-radius:8px;padding:10px 14px;margin-bottom:10px;font-size:13px;color:#15803d}')
a('.info{background:#eff6ff;border:1px solid #bfdbfe;border-radius:8px;padding:10px 14px;margin-bottom:10px;font-size:13px;color:#1d4ed8}')
a('table{width:100%;border-collapse:collapse;font-size:13px;margin-bottom:14px}')
a('th{background:#1e293b;color:#fff;padding:9px;text-align:left}')
a('td{padding:8px 9px;border-bottom:1px solid #f1f5f9;vertical-align:top}')
a('tr:nth-child(even){background:#f8fafc}')
a('.footer{background:#1e293b;color:#94a3b8;text-align:center;padding:16px;font-size:12px;margin-top:20px}')
a('</style></head><body>')

# HERO
a('<div class="hero">')
a('<h1>&#127891; Premium University Competitions 2026</h1>')
a('<div class="sub">Essay Competitions &bull; Summer Programs &bull; Research Opportunities &bull; For Students Ages 14&ndash;18 Worldwide</div>')
a('<div class="badges">')
a('<span class="badge">&#127881; 20+ Competitions Listed</span>')
a('<span class="badge">&#127758; Open Worldwide</span>')
a('<span class="badge">&#127942; Harvard &bull; Oxford &bull; Cambridge &bull; MIT &bull; Yale &bull; Stanford</span>')
a('<span class="badge">&#128197; 2026 Deadlines</span>')
a('</div></div>')

# NAV
a('<nav>')
for tab_id, label in [("all","&#127968; All Competitions"),("essay","&#128221; Essay Competitions"),("summer","&#9728;&#65039; Summer Programs"),("research","&#128300; Research Programs"),("strategy","&#127919; Application Strategy")]:
    active = ' active' if tab_id == 'all' else ''
    a(f'<button class="nt{active}" onclick="show(\'{tab_id}\')">{label}</button>')
a('</nav>')

# ALL COMPETITIONS SECTION
a('<div id="all" class="sec active">')
a('<div class="sh">&#127775; Top-Tier University Competitions at a Glance</div>')
a('<div class="stat-row">')
a('<div class="stat"><span class="stat-n">20+</span><div class="stat-l">Competitions Listed</div></div>')
a('<div class="stat"><span class="stat-n">6</span><div class="stat-l">Ivy League / Oxbridge Programs</div></div>')
a('<div class="stat"><span class="stat-n">8</span><div class="stat-l">Free Essay Competitions</div></div>')
a('<div class="stat"><span class="stat-n">50+</span><div class="stat-l">Countries Eligible</div></div>')
a('</div>')
a('<div class="tip">&#128161; <strong>Strategy:</strong> Apply to 3&ndash;5 competitions per year. Mix essay competitions (build writing skills) with summer programs (build research skills). Both strengthen university applications significantly.</div>')
a('<div class="sh">&#128221; Essay Competitions &mdash; Quick Comparison</div>')
a('<div style="overflow-x:auto"><table>')
a('<tr><th>Competition</th><th>University</th><th>Age</th><th>Fee</th><th>Prize</th><th>Deadline 2026</th><th>Prestige</th></tr>')
comps_table = [
    ("Cambridge Re:think","Cambridge / CCIR","14&ndash;18","FREE","$150 + Cambridge ceremony","Jan 2026","&#11088;&#11088;&#11088;&#11088;&#11088;"),
    ("John Locke Institute","Oxford-affiliated","16&ndash;18","FREE","Oxford summer school + $2,000","Apr 2026","&#11088;&#11088;&#11088;&#11088;&#11088;"),
    ("Oxbridge Essay Competition","Oxford / Cambridge","14&ndash;18","FREE","Mentorship + recognition","Varies","&#11088;&#11088;&#11088;&#11088;"),
    ("LSE Essay Competition","London School of Economics","16&ndash;18","FREE","Recognition + LSE visit","Mar 2026","&#11088;&#11088;&#11088;&#11088;"),
    ("Warwick Economics Essay","University of Warwick","16&ndash;18","FREE","Cash prize + recognition","Mar 2026","&#11088;&#11088;&#11088;"),
    ("UCL Global Citizenship Essay","University College London","16&ndash;18","FREE","Recognition + UCL visit","Apr 2026","&#11088;&#11088;&#11088;"),
    ("Concord Review","Independent (Harvard-linked)","14&ndash;18","$60","Publication in academic journal","Rolling","&#11088;&#11088;&#11088;&#11088;"),
    ("Philosophy Olympiad (IPO)","International","16&ndash;18","FREE","Gold/Silver/Bronze medal","Feb 2026","&#11088;&#11088;&#11088;&#11088;"),
    ("Economics Olympiad (IEO)","International","16&ndash;18","FREE","Gold/Silver/Bronze medal","Mar 2026","&#11088;&#11088;&#11088;&#11088;"),
    ("Breakthrough Junior Challenge","Khan Academy / Breakthrough","13&ndash;18","FREE","$250,000 scholarship","May 2026","&#11088;&#11088;&#11088;&#11088;"),
]
for row in comps_table:
    a('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>')
a('</table></div>')
a('</div>')

# ESSAY COMPETITIONS SECTION
a('<div id="essay" class="sec">')
a('<div class="sh">&#128221; Premium Essay Competitions 2026</div>')
a('<div class="tip">&#128161; Essay competitions are the highest-ROI activity for university applications. A win or shortlist at any of these competitions is a significant differentiator.</div>')
a('<div class="grid">')

essay_comps = [
    ("#7c3aed","&#11088;&#11088;&#11088;&#11088;&#11088; Tier 1","Cambridge Re:think Essay Competition","Cambridge Centre for International Research (CCIR)",
     ["FREE","Essay","Ages 14-18","Worldwide"],
     "9 prompts from Harvard/Oxford/Cambridge professors. 13,000+ submissions in 2025. Gold prize: $150 + $500 scholarship + Cambridge ceremony. Double-blind review by Harvard/MIT/Stanford/Cambridge/Oxford scholars.",
     "https://cambridge-research.org/essay-competition/","Jan 2026","2,000 words","MLA 8"),
    ("#1e3a5f","&#11088;&#11088;&#11088;&#11088;&#11088; Tier 1","John Locke Institute Essay Competition","John Locke Institute (Oxford-affiliated)",
     ["FREE","Essay","Ages 16-18","Worldwide"],
     "One of the most prestigious essay competitions globally. Subjects: Philosophy, Politics, Economics, History, Psychology, Law, Theology. Winners receive Oxford summer school scholarship ($2,000 value) + cash prizes. Judged by Oxford/Cambridge academics.",
     "https://www.johnlockeinstitute.com/essay-competition","Apr 2026","2,000 words","Chicago/MLA"),
    ("#2563eb","&#11088;&#11088;&#11088;&#11088; Tier 2","LSE Essay Competition","London School of Economics",
     ["FREE","Essay","Ages 16-18","UK + International"],
     "Annual essay competition run by LSE student societies. Topics in economics, politics, and social science. Winners invited to LSE for prize-giving. Strong signal for LSE, UCL, and Oxbridge applications.",
     "https://www.lse.ac.uk/","Mar 2026","1,500-2,000 words","Harvard"),
    ("#10b981","&#11088;&#11088;&#11088;&#11088; Tier 2","Warwick Economics Essay Competition","University of Warwick",
     ["FREE","Essay","Ages 16-18","UK + International"],
     "Run by the University of Warwick Economics Department. Cash prizes for top essays. Strong signal for economics university applications. Topics change annually.",
     "https://warwick.ac.uk/fac/soc/economics/","Mar 2026","1,500 words","Harvard"),
    ("#f59e0b","&#11088;&#11088;&#11088;&#11088; Tier 2","UCL Global Citizenship Essay","University College London",
     ["FREE","Essay","Ages 16-18","Worldwide"],
     "UCL's annual essay competition on global issues. Winners invited to UCL for ceremony. Strong signal for UCL and Russell Group applications.",
     "https://www.ucl.ac.uk/","Apr 2026","1,500 words","Varies"),
    ("#8b5cf6","&#11088;&#11088;&#11088;&#11088; Tier 2","Concord Review","The Concord Review (Harvard-linked)",
     ["$60 fee","Essay","Ages 14-18","Worldwide"],
     "The only academic journal in the world that publishes the research essays of secondary students. Published since 1987. A publication here is equivalent to a peer-reviewed academic publication for a high school student. Extremely prestigious for humanities.",
     "https://www.tcr.org/","Rolling","4,000-10,000 words","Chicago"),
    ("#ef4444","&#11088;&#11088;&#11088;&#11088; Tier 2","International Philosophy Olympiad (IPO)","International Federation of Philosophical Societies",
     ["FREE","Essay","Ages 16-18","Worldwide"],
     "Annual international philosophy essay competition. Students write a 4-page philosophical essay in a foreign language. Gold, Silver, Bronze medals. Represents your country. Extremely prestigious for philosophy/PPE applicants.",
     "https://www.philosophy-olympiad.org/","Feb 2026","4 pages","Academic"),
    ("#06b6d4","&#11088;&#11088;&#11088;&#11088; Tier 2","International Economics Olympiad (IEO)","International Economics Olympiad Foundation",
     ["FREE","Essay + Case Study","Ages 16-18","Worldwide"],
     "Annual international economics competition with essay, case study, and financial literacy components. Represents your country. Gold, Silver, Bronze medals. Strong signal for economics university applications.",
     "https://econ-olympiad.org/","Mar 2026","Varies","Academic"),
    ("#14b8a6","&#11088;&#11088;&#11088; Tier 3","Breakthrough Junior Challenge","Breakthrough Prize Foundation",
     ["FREE","Video Essay","Ages 13-18","Worldwide"],
     "Create a short video (max 3 minutes) explaining a complex scientific concept. Winner receives $250,000 college scholarship + $50,000 for their teacher + $100,000 science lab for their school. Judged by leading scientists.",
     "https://breakthroughjuniorchallenge.org/","May 2026","3-min video","N/A"),
    ("#ec4899","&#11088;&#11088;&#11088; Tier 3","Scholastic Art & Writing Awards","Scholastic (US-based, international)",
     ["FREE","Writing","Ages 13-18","US + International"],
     "The largest, most prestigious recognition program for creative teens in the US. Gold Medal winners receive national recognition. Strong signal for creative writing and humanities university applications.",
     "https://www.artandwriting.org/","Dec 2025","Varies","N/A"),
]

for color, tier, name, org, tags, desc, url, deadline, words, citation in essay_comps:
    a(f'<div class="comp-card" style="border-top-color:{color}">')
    a(f'<div class="tier-badge" style="background:{color}22;color:{color}">{tier}</div>')
    a(f'<div class="comp-name">{name}</div>')
    a(f'<div class="comp-org">{org}</div>')
    a('<div class="comp-meta">')
    for tag in tags:
        cls = 'free' if 'FREE' in tag else 'paid' if '$' in tag else 'essay' if 'Essay' in tag else 'intl' if 'World' in tag else ''
        a(f'<span class="tag {cls}">{tag}</span>')
    a(f'<span class="tag">Deadline: {deadline}</span>')
    a(f'<span class="tag">{words}</span>')
    a('</div>')
    a(f'<div class="comp-desc">{desc}</div>')
    a(f'<a class="comp-link" href="{url}" target="_blank">&#128279; Visit Website &rarr;</a>')
    a('</div>')

a('</div></div>')

# SUMMER PROGRAMS SECTION
a('<div id="summer" class="sec">')
a('<div class="sh">&#9728;&#65039; Premium University Summer Programs 2026</div>')
a('<div class="warn">&#128683; Most summer programs charge fees ($3,000&ndash;$15,000). Many offer financial aid. Apply early &mdash; most deadlines are January&ndash;March 2026.</div>')
a('<div class="grid">')

summer_progs = [
    ("#1e3a5f","&#11088;&#11088;&#11088;&#11088;&#11088; Tier 1","Yale Young Global Scholars (YYGS)","Yale University",
     ["Paid","Summer","Ages 15-17","Worldwide"],
     "Two-week intensive academic program at Yale. Interdisciplinary seminars, lectures by Yale faculty, collaborative projects. Highly selective (~10% acceptance). Strong signal for Yale and Ivy League applications. Financial aid available.",
     "https://globalscholars.yale.edu/","Jan 2026","$6,500","New Haven, CT"),
    ("#7c3aed","&#11088;&#11088;&#11088;&#11088;&#11088; Tier 1","Harvard Secondary School Program","Harvard University",
     ["Paid","Summer","Ages 15-18","Worldwide"],
     "Take actual Harvard courses for credit. Live on campus. Courses in humanities, sciences, social sciences. Highly prestigious. Financial aid available. Strong signal for Harvard and Ivy League applications.",
     "https://www.summer.harvard.edu/high-school-programs","Jan 2026","$5,000-$15,000","Cambridge, MA"),
    ("#2563eb","&#11088;&#11088;&#11088;&#11088;&#11088; Tier 1","Stanford Pre-Collegiate Studies","Stanford University",
     ["Paid","Summer","Ages 13-18","Worldwide"],
     "Multiple programs: Summer Institutes (2 weeks), Online High School (year-round), Institutes for Mathematics, Science, and Technology. Highly selective. Strong signal for Stanford and top US university applications.",
     "https://summerinstitutes.spcs.stanford.edu/","Feb 2026","$4,000-$12,000","Stanford, CA"),
    ("#10b981","&#11088;&#11088;&#11088;&#11088;&#11088; Tier 1","MIT PRIMES (Research)","Massachusetts Institute of Technology",
     ["FREE","Research","Ages 15-18","US + International"],
     "Year-long research program where high school students work with MIT researchers on cutting-edge mathematics and computer science problems. Extremely selective. FREE. One of the most prestigious high school research programs in the world.",
     "https://math.mit.edu/research/highschool/primes/","Nov 2025","FREE","Remote + MIT"),
    ("#f59e0b","&#11088;&#11088;&#11088;&#11088; Tier 2","Oxford Scholastica Academy","University of Oxford",
     ["Paid","Summer","Ages 13-18","Worldwide"],
     "Study at Oxford for 2 weeks. Courses in law, medicine, philosophy, politics, economics, sciences. Taught by Oxford tutors. Strong signal for Oxford applications. Financial aid available.",
     "https://www.oxfordscholastica.com/","Mar 2026","$3,500-$5,000","Oxford, UK"),
    ("#ef4444","&#11088;&#11088;&#11088;&#11088; Tier 2","Cambridge Immerse Education","University of Cambridge",
     ["Paid","Summer","Ages 13-18","Worldwide"],
     "2-week residential academic programs at Cambridge. Subjects include medicine, law, economics, engineering, humanities. Taught by Cambridge academics. Strong signal for Cambridge applications.",
     "https://www.immerse.education/","Mar 2026","$3,500-$5,500","Cambridge, UK"),
    ("#8b5cf6","&#11088;&#11088;&#11088;&#11088; Tier 2","LSE Summer School","London School of Economics",
     ["Paid","Summer","Ages 16-18","Worldwide"],
     "3-week intensive courses at LSE. Subjects: economics, finance, politics, law, sociology. Earn university credit. Strong signal for LSE and Russell Group applications. Financial aid available.",
     "https://www.lse.ac.uk/study-at-lse/summer-schools","Feb 2026","$3,000-$5,000","London, UK"),
    ("#06b6d4","&#11088;&#11088;&#11088; Tier 3","Sutton Trust US Programme","Sutton Trust (UK)",
     ["FREE","Summer","Ages 17-18","UK students only"],
     "Fully funded trip to top US universities (Harvard, Yale, Princeton, MIT, Georgetown) for UK state school students. Extremely competitive. FREE including flights and accommodation. Strong signal for US university applications.",
     "https://www.suttontrust.com/our-programmes/us-programme/","Jan 2026","FREE","US Universities"),
    ("#14b8a6","&#11088;&#11088;&#11088; Tier 3","Nuffield Research Placements","Nuffield Foundation (UK)",
     ["FREE","Research","Ages 16-17","UK students only"],
     "6-week research placement at a university, research institute, or company. Work on a real research project. FREE. Strong signal for UK university applications, especially STEM.",
     "https://www.nuffieldresearchplacements.org/","Jan 2026","FREE","UK"),
]

for color, tier, name, org, tags, desc, url, deadline, cost, location in summer_progs:
    a(f'<div class="comp-card" style="border-top-color:{color}">')
    a(f'<div class="tier-badge" style="background:{color}22;color:{color}">{tier}</div>')
    a(f'<div class="comp-name">{name}</div>')
    a(f'<div class="comp-org">{org}</div>')
    a('<div class="comp-meta">')
    for tag in tags:
        cls = 'free' if 'FREE' in tag else 'paid' if 'Paid' in tag else 'summer' if 'Summer' in tag else 'research' if 'Research' in tag else 'intl' if 'World' in tag else ''
        a(f'<span class="tag {cls}">{tag}</span>')
    a(f'<span class="tag">Deadline: {deadline}</span>')
    a(f'<span class="tag">{cost}</span>')
    a(f'<span class="tag">&#128205; {location}</span>')
    a('</div>')
    a(f'<div class="comp-desc">{desc}</div>')
    a(f'<a class="comp-link" href="{url}" target="_blank">&#128279; Visit Website &rarr;</a>')
    a('</div>')

a('</div></div>')

# RESEARCH PROGRAMS SECTION
a('<div id="research" class="sec">')
a('<div class="sh">&#128300; Research &amp; Academic Programs 2026</div>')
a('<div class="info">&#128161; Research programs are the highest-prestige activities for STEM university applications. A published paper or research award at 16&ndash;18 is extraordinary.</div>')
a('<div class="grid">')

research_progs = [
    ("#7c3aed","&#11088;&#11088;&#11088;&#11088;&#11088; Tier 1","Regeneron Science Talent Search","Society for Science (US)",
     ["FREE","Research","Ages 17-18","US students only"],
     "The most prestigious pre-college science competition in the US. Submit an original research paper. Top 40 finalists invited to Washington DC. $250,000 top prize. Alumni include Nobel laureates and Fields Medal winners.",
     "https://www.societyforscience.org/regeneron-sts/","Nov 2025","FREE","US only"),
    ("#1e3a5f","&#11088;&#11088;&#11088;&#11088;&#11088; Tier 1","Regeneron ISEF","Society for Science (International)",
     ["FREE","Research","Ages 14-18","Worldwide"],
     "The world's largest international pre-college science competition. Win at your regional/national science fair to qualify.