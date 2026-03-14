f = open("outputs/cambridge-essay/cambridge-essay-visual-guide.html", "a", encoding="utf-8")
w = f.write
# TIMELINE SECTION
w('<div id="timeline" class="section">\n')
w('<div class="sh">&#128197; 8-Week Writing Timeline</div>\n')
w('<div class="card">\n')
w('<div class="timeline">\n')
tl = [
    ("done","Now &mdash; Week 1","Choose Your Prompt","Score each prompt on interest, knowledge, and originality potential. Commit to one."),
    ("done","Week 1&ndash;2","Deep Research","Read 3&ndash;5 books from the professor reading list. Take notes with page numbers. Find 2&ndash;3 key data points."),
    ("","Week 2","Develop Your Thesis","Write 5 possible thesis statements. Choose the most specific and arguable one."),
    ("","Week 3","Write First Draft","Aim for 1,800 words. Don\'t edit as you write &mdash; just get the argument down."),
    ("","Week 4","Peer Review","Share with a teacher or trusted peer. Ask: Is the thesis clear? Is the counterargument addressed?"),
    ("","Week 5","Revise Argument","Strengthen weak paragraphs. Add missing evidence. Cut anything that doesn\'t support the thesis."),
    ("","Week 6","Polish Writing","Read aloud to catch awkward sentences. Vary sentence length. Check vocabulary precision."),
    ("","Week 7","Citations &amp; Format","Check every citation is in MLA 8. Format PDF. Remove your name and school from the document."),
    ("urgent","Submission","Submit via CCIR Portal","Double-check word count, PDF format, blind review compliance, and referee email."),
    ("","31 July 2026","Award Ceremony","King\'s College, Cambridge &mdash; if you win, you\'ll be invited here."),
]
for cls, date, title, desc in tl:
    w(f'<div class="tl-item {cls}">\n')
    w(f'<div class="tl-date">{date}</div>\n')
    w(f'<div class="tl-title">{title}</div>\n')
    w(f'<div class="tl-desc">{desc}</div>\n')
    w('</div>\n')
w('</div>\n</div>\n')
w('<div class="sh">&#128203; Prompt Decision Matrix</div>\n')
w('<div class="card">\n')
w('<div class="ctitle">Score each prompt (1&ndash;5) to find your best match</div>\n')
w('<table>\n')
w('<tr><th>Prompt</th><th>My Interest (1&ndash;5)</th><th>My Knowledge (1&ndash;5)</th><th>Originality Potential (1&ndash;5)</th><th>Total</th></tr>\n')
for i in range(1, 10):
    labels = ["","Populism","Nation-States","AI Legal Personhood","Colonial Artifacts","Meritocracy","Open Borders","Scientific Constraints","Technology Restrictions","What Does It Mean to Heal?"]
    w(f'<tr><td><strong>{i}. {labels[i]}</strong></td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>\n')
w('</table>\n</div>\n')
w('</div>\n')
f.close()
print("Part 8 done")