f = open("outputs/cambridge-essay/cambridge-essay-visual-guide.html", "a", encoding="utf-8")
w = f.write
# STRATEGY SECTION
w('<div id="strategy" class="section">\n')
w('<div class="sh">&#127919; Prompt Selection Strategy</div>\n')
w('<div class="card">\n')
w('<div class="ctitle">How to Choose Your Prompt</div>\n')
w('<ul class="al">\n')
w('<li><span>1</span><strong>Genuine interest</strong> &mdash; You will spend weeks on this. Pick something you actually want to think about.</li>\n')
w('<li><span>2</span><strong>Original angle</strong> &mdash; Can you say something the obvious essay won\'t say? If not, pick a different prompt.</li>\n')
w('<li><span>3</span><strong>Research access</strong> &mdash; Can you access 3&ndash;5 academic books or articles? Check your school library first.</li>\n')
w('<li><span>4</span><strong>Avoid the crowd</strong> &mdash; Prompts 1 (Populism) and 2 (Nation-states) will attract the most submissions. Harder to stand out.</li>\n')
w('</ul>\n</div>\n')
w('<div class="sh">&#128202; Prompt Comparison Matrix</div>\n')
w('<div style="overflow-x:auto"><table>\n')
w('<tr><th>#</th><th>Prompt</th><th>Competition Level</th><th>Originality Ceiling</th><th>Research Difficulty</th><th>Recommended For</th></tr>\n')
rows = [
    ("1","Populism","&#128308; Very High","Medium","Medium","Students with politics/history background"),
    ("2","Nation-states","&#128308; High","Medium","Medium-High","IR / geography students"),
    ("3","AI Legal Personhood","&#128992; Medium-High","High","Medium","Tech-interested students"),
    ("4","Colonial Artifacts","&#128992; Medium","High","Medium","History / ethics students"),
    ("5","Meritocracy","&#128992; Medium","High","Medium","Sociology / economics students"),
    ("6","Open Borders","&#128992; Medium","High","Medium","Philosophy / ethics students"),
    ("7","Scientific Constraints","&#128309; Medium-Low","Medium","Medium","Science students"),
    ("8","Technology Restrictions","&#128309; Medium-Low","High","Medium-High","Biology / philosophy students"),
    ("9","What Does It Mean to Heal?","&#128309; Low","Very High","Low-Medium","Creative / interdisciplinary students"),
]
for num, name, comp, orig, diff, rec in rows:
    w(f'<tr><td><strong>{num}</strong></td><td>{name}</td><td>{comp}</td><td>{orig}</td><td>{diff}</td><td>{rec}</td></tr>\n')
w('</table></div>\n')
w('<div class="sh">&#128161; What Makes a Winning Essay</div>\n')
w('<div class="grid2">\n')
w('<div class="card"><div class="ctitle">&#9989; Winning Essays Do This</div>\n')
w('<ul class="al">\n')
w('<li><span>&#10003;</span>Take a clear, specific, arguable thesis in the introduction</li>\n')
w('<li><span>&#10003;</span>Use academic sources from the professor reading lists</li>\n')
w('<li><span>&#10003;</span>Dedicate a full paragraph to the strongest counterargument</li>\n')
w('<li><span>&#10003;</span>Distinguish between types or cases (not all X is the same)</li>\n')
w('<li><span>&#10003;</span>End with a broader implication, not just a summary</li>\n')
w('<li><span>&#10003;</span>Cite every claim in MLA 8 format</li>\n')
w('</ul></div>\n')
w('<div class="card"><div class="ctitle">&#10060; Losing Essays Do This</div>\n')
w('<ul class="al">\n')
w('<li><span style="background:#ef4444">&#10007;</span>Summarise what others think without taking a position</li>\n')
w('<li><span style="background:#ef4444">&#10007;</span>Use Wikipedia or news articles as primary sources</li>\n')
w('<li><span style="background:#ef4444">&#10007;</span>Ignore the counterargument entirely</li>\n')
w('<li><span style="background:#ef4444">&#10007;</span>Write a vague thesis like "this is a complex issue"</li>\n')
w('<li><span style="background:#ef4444">&#10007;</span>Exceed 2,000 words</li>\n')
w('<li><span style="background:#ef4444">&#10007;</span>Use AI to write any part of the essay</li>\n')
w('</ul></div>\n')
w('</div>\n')
w('<div class="sh">&#128221; Sample Thesis Statements</div>\n')
theses = [
    ("Prompt 3 &mdash; AI Legal Personhood",
     "Although AI systems increasingly exhibit human-like reasoning, granting them legal personhood would create accountability gaps that undermine rather than strengthen human oversight &mdash; a more effective approach is enhanced corporate liability for AI developers."),
    ("Prompt 4 &mdash; Colonial Artifacts",
     "While universal museum arguments have merit, the case for repatriation is stronger: colonial acquisition was rarely consensual, and modern preservation technology eliminates the practical objections to return."),
    ("Prompt 6 &mdash; Open Borders",
     "Open borders are morally justified as an extension of the basic human right to freedom of movement, but their implementation requires phased institutional reform &mdash; the moral case is clear even if the political path is not."),
    ("Prompt 9 &mdash; What Does It Mean to Heal?",
     "Healing is not the restoration of a prior state but the creation of a new relationship with loss &mdash; a process that is irreducibly social and cultural, not merely medical, and that requires community as much as treatment."),
]
for label, thesis in theses:
    w('<div class="thesis-box">\n')
    w(f'<div class="thesis-label">{label}</div>\n')
    w(f'<div class="thesis-text">"{thesis}"</div>\n')
    w('</div>\n')
w('</div>\n')
f.close()
print("Part 5 done")