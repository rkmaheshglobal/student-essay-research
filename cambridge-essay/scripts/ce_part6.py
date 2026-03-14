f = open("outputs/cambridge-essay/cambridge-essay-visual-guide.html", "a", encoding="utf-8")
w = f.write
# ESSAY STRUCTURE SECTION
w('<div id="structure" class="section">\n')
w('<div class="sh">&#128196; Essay Structure (2,000 Words)</div>\n')
w('<div class="tip">&#128161; This structure works for all 9 prompts. Adapt the word counts slightly based on your argument complexity.</div>\n')
w('<div class="card">\n')
w('<div class="ctitle">&#128196; Recommended Word Budget</div>\n')
w('<table>\n')
w('<tr><th>Section</th><th>Words</th><th>Purpose</th><th>Key Elements</th></tr>\n')
w('<tr><td><strong>Introduction</strong></td><td>150&ndash;200</td><td>Hook, context, thesis, roadmap</td><td>Start with a striking fact or paradox; state thesis clearly in last sentence</td></tr>\n')
w('<tr><td><strong>Body 1 &mdash; Strongest Argument</strong></td><td>350&ndash;400</td><td>Your best evidence for the thesis</td><td>Topic sentence + academic source + data + analysis + link to thesis</td></tr>\n')
w('<tr><td><strong>Body 2 &mdash; Second Argument</strong></td><td>350&ndash;400</td><td>Different type of evidence</td><td>Use a different evidence type (e.g., historical example if BP1 used data)</td></tr>\n')
w('<tr><td><strong>Body 3 &mdash; Counterargument</strong></td><td>350&ndash;400</td><td>Address the strongest objection</td><td>State it fairly &rarr; concede what is valid &rarr; rebut why thesis still holds</td></tr>\n')
w('<tr><td><strong>Conclusion</strong></td><td>150&ndash;200</td><td>Synthesis + broader implication</td><td>Restate thesis (different words) + summarise + end with a memorable sentence</td></tr>\n')
w('</table>\n</div>\n')
w('<div class="sh">&#128270; Introduction Formula</div>\n')
w('<div class="card">\n')
w('<div class="ctitle">The 4-Sentence Introduction</div>\n')
w('<ul class="al">\n')
w('<li><span>1</span><strong>Hook</strong> &mdash; A striking statistic, paradox, or concrete example that makes the reader want to continue</li>\n')
w('<li><span>2</span><strong>Context</strong> &mdash; Why does this question matter right now? What is at stake?</li>\n')
w('<li><span>3</span><strong>Tension</strong> &mdash; Briefly acknowledge the complexity (the two sides of the debate)</li>\n')
w('<li><span>4</span><strong>Thesis</strong> &mdash; Your clear, arguable position. This is the most important sentence in the essay.</li>\n')
w('</ul>\n</div>\n')
w('<div class="sh">&#128161; Sample Hooks by Prompt</div>\n')
hooks = [
    ("Prompt 1 &mdash; Populism",
     "In 2024, for the first time in American history, a convicted felon won the presidency with 77 million votes. Whether this represents democracy working or democracy failing depends entirely on how one defines populism."),
    ("Prompt 3 &mdash; AI Legal Personhood",
     "In 2023, a Colombian judge cited ChatGPT in a legal ruling. In 2024, an AI system was listed as a co-inventor on a patent application. The question of whether AI should have legal personhood is no longer theoretical."),
    ("Prompt 4 &mdash; Colonial Artifacts",
     "The Benin Bronzes were looted from Nigeria in 1897 by British soldiers who described the raid as a 'punitive expedition.' Today, 900 of them sit in the British Museum. The question of who owns them is also a question of who owns history."),
    ("Prompt 6 &mdash; Open Borders",
     "Every year, thousands of people die attempting to cross borders that their grandparents crossed freely. The question of whether borders are morally justified is also a question of whether birthplace should determine destiny."),
    ("Prompt 9 &mdash; What Does It Mean to Heal?",
     "The English word 'heal' comes from the Old English h&aelig;lan &mdash; to make whole. But what does wholeness mean after loss? This question, which medicine has largely abandoned to philosophy, may be the most important question of our time."),
]
for label, hook in hooks:
    w('<div class="card" style="margin-bottom:10px">\n')
    w(f'<div class="ctitle">{label}</div>\n')
    w(f'<p style="font-style:italic;color:#475569;font-size:14px">"{hook}"</p>\n')
    w('</div>\n')
w('<div class="sh">&#128221; MLA 8 Citation Quick Reference</div>\n')
w('<div class="card">\n')
w('<table>\n')
w('<tr><th>Source Type</th><th>Format</th><th>Example</th></tr>\n')
w('<tr><td>Book</td><td>Last, First. <em>Title</em>. Publisher, Year.</td><td>M&uuml;ller, Jan-Werner. <em>What Is Populism?</em> U of Pennsylvania P, 2016.</td></tr>\n')
w('<tr><td>Journal Article</td><td>Last, First. "Title." <em>Journal</em>, vol. #, no. #, Year, pp. #&ndash;#.</td><td>Carens, Joseph. "Aliens and Citizens." <em>Review of Politics</em>, vol. 49, no. 2, 1987, pp. 251&ndash;73.</td></tr>\n')
w('<tr><td>In-text</td><td>(Author Page)</td><td>(M&uuml;ller 45) or (Carens 252)</td></tr>\n')
w('</table>\n</div>\n')
w('</div>\n')
f.close()
print("Part 6 done")