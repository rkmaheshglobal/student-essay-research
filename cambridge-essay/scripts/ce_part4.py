f = open("outputs/cambridge-essay/cambridge-essay-visual-guide.html", "a", encoding="utf-8")
w = f.write
# PROMPTS SECTION
w('<div id="prompts" class="section">\n')
w('<div class="sh">&#10067; All 9 Prompts &mdash; Senior Division 2026</div>\n')
w('<div class="tip">&#128161; Click any prompt card to see thesis ideas and key arguments. Choose <strong>ONE</strong> prompt only.</div>\n')

prompts = [
    ("p1","1","Politics / Democracy","Is populism inevitably a destructive force in democracy, or can it be reimagined as a positive force for change?",
     "hot","High Competition","Contributed by Harvard Professor",
     "The core tension: populism exposes real elite corruption but often slides into authoritarianism. Your angle: distinguish between <em>form</em> (people vs. elites narrative) and <em>content</em> (exclusionary vs. inclusive). Argue that populism is a symptom, not a cause.",
     "M&uuml;ller: <em>What Is Populism?</em> (2016) &bull; Levitsky &amp; Ziblatt: <em>How Democracies Die</em> (2018) &bull; Mudde &amp; Kaltwasser: <em>Populism: A Very Short Introduction</em> (2017)"),
    ("p2","2","IR / Political Theory","Can the nation-state survive the pressures of globalisation, climate change, and forced migration?",
     "","Broad Scope","Contributed by Stanford Professor",
     "Three pressures identified by the professor: (1) digital flows states can't control, (2) climate costs, (3) forced migration. The rightward tilt is a reaction that may <em>accelerate</em> state decline. Your angle: distinguish between state <em>form</em> and state <em>function</em> &mdash; functions may survive even if forms change.",
     "Anderson: <em>Imagined Communities</em> (1983) &bull; Appadurai: <em>Modernity at Large</em> (1996) &bull; Hobsbawm: <em>Nations and Nationalism Since 1780</em> (1990)"),
    ("p3","3","AI / Law / Ethics","Should AI systems have legal personhood?",
     "orig","Highly Topical","Contributed by Berkeley Professor",
     "The professor's framing: legal personhood requires answering whether AI can be sued, can live independently, and can exist outside ownership. Current answer: no. Your angle: argue that the real question is not personhood but <em>accountability</em> &mdash; enhanced corporate liability is more effective than personhood.",
     "Mitchell: <em>AI: A Guide for Thinking Humans</em> (2019) &bull; Gunkel: <em>The Machine Question</em> (2012) &bull; Zuboff: <em>The Age of Surveillance Capitalism</em> (2019)"),
    ("p4","4","History / Ethics","Should colonial-era artifacts in Western museums be repatriated to their countries of origin, or preserved where they are as part of global heritage?",
     "orig","Rich Literature","Contributed by Cornell Professor",
     "Two sides: universal museum argument (artifacts belong to all humanity; Western museums have preservation capacity) vs. repatriation argument (colonial acquisition was non-consensual; modern technology solves preservation concerns). Your angle: the <em>consent</em> question is decisive &mdash; acquisition without consent cannot be legitimised by subsequent stewardship.",
     "Hicks: <em>The Brutish Museums</em> (2020) &bull; Cuno: <em>Who Owns Antiquity?</em> (2008) &bull; Said: <em>Culture and Imperialism</em> (1993)"),
    ("p5","5","Sociology / Economics","Can meritocracy and structural inequality coexist, or does one inevitably undermine the other?",
     "hard","Nuanced","Contributed by UPenn Professor",
     "The professor's framing: definitions matter &mdash; what kind of meritocracy? What kind of structural inequality? Your angle: formal meritocracy (equal rules) can coexist with structural inequality, but <em>substantive</em> meritocracy (equal outcomes of effort) cannot &mdash; because structural inequality determines who can compete.",
     "Sandel: <em>The Tyranny of Merit</em> (2020) &bull; Young: <em>The Rise of the Meritocracy</em> (1958) &bull; Rawls: <em>A Theory of Justice</em> (1971)"),
    ("p6","6","Ethics / Migration","Are open borders morally justified?",
     "orig","Clear Framework","Contributed by Princeton Professor",
     "The professor's framing: borders are moral boundaries that determine who gets safety and opportunity. Evidence shows immigrants strengthen economies. Your angle: open borders are morally justified as an extension of freedom of movement, but the argument must address the <em>social trust</em> objection (Miller) directly.",
     "Carens: <em>The Ethics of Immigration</em> (2013) &bull; Miller: <em>Strangers in Our Midst</em> (2016) &bull; Arendt: <em>The Origins of Totalitarianism</em> (1951)"),
    ("p7","7","Philosophy of Science","Should the pursuit of scientific knowledge be constrained by ethical considerations?",
     "","Classic Debate","Contributed by Oxford Professor",
     "The tension: scientific freedom vs. ethical responsibility. Your angle: the question is not <em>whether</em> but <em>how</em> &mdash; distinguish between restricting <em>research</em> (problematic) and restricting <em>application</em> (necessary). Use genome editing as the case study.",
     "Jasanoff: <em>The Ethics of Invention</em> (2016) &bull; Mazzucato: <em>The Entrepreneurial State</em> (2013) &bull; Feynman: <em>The Pleasure of Finding Things Out</em> (1999)"),
    ("p8","8","Bioethics / Technology","Should some technologies be restricted even if they could eliminate disease or extend human life?",
     "hard","High Stakes","Contributed by Columbia Professor",
     "The professor's example: genome editing in human embryos &mdash; could eliminate Huntington's disease but risks are irreversible. Your angle: the <em>irreversibility</em> criterion is key &mdash; technologies that permanently alter the human gene pool or social fabric require a higher burden of proof before deployment.",
     "Bostrom: <em>Superintelligence</em> (2014) &bull; Harari: <em>Homo Deus</em> (2016) &bull; Shelley: <em>Frankenstein</em> (1818)"),
    ("p9","9","Philosophy / Medicine / Culture","What does it mean to heal?",
     "orig","Most Original","Contributed by Cambridge Professor",
     "The professor's framing: healing comes from Old English <em>h&aelig;lan</em> &mdash; to make whole. Modern tension: quick-fix wellness culture vs. deep understanding of trauma and rehabilitation. Your angle: healing is not restoration of a prior state but <em>integration of loss</em> &mdash; a social and cultural process, not merely a medical one.",
     "Frankl: <em>Man's Search for Meaning</em> (1946) &bull; van der Kolk: <em>The Body Keeps the Score</em> (2014) &bull; Sontag: <em>Illness as Metaphor</em> (1978)"),
]

for pc, num, theme, question, tag_class, tag_text, src, analysis, books in prompts:
    w(f'<div class="prompt-card {pc}" onclick="toggle(\'d{num}\')">\n')
    w(f'<div class="prompt-num">Prompt {num} &bull; {theme} &bull; {src}</div>\n')
    w(f'<div class="prompt-q">{question}</div>\n')
    w(f'<div class="prompt-meta"><span class="tag {tag_class}">{tag_text}</span><span class="tag">Click to expand</span></div>\n')
    w(f'<div class="detail-box" id="d{num}">\n')
    w(f'<div class="ctitle">&#128161; Strategic Analysis</div><p style="margin-bottom:10px;color:#475569">{analysis}</p>\n')
    w(f'<div class="ctitle">&#128218; Key Books</div><p style="color:#475569;font-size:13px">{books}</p>\n')
    w('</div>\n</div>\n')

w('</div>\n')
f.close()
print("Part 4 done")
