f = open("outputs/cambridge-essay/cambridge-essay-visual-guide.html", "a", encoding="utf-8")
w = f.write
# READING LISTS SECTION
w('<div id="reading" class="section">\n')
w('<div class="sh">&#128218; Professor-Recommended Reading Lists</div>\n')
w('<div class="tip">&#128161; These books are directly recommended by the professors who wrote the prompts. Using them signals to judges that you engaged with the intended academic conversation.</div>\n')

reading = [
    ("p1","Prompt 1 &mdash; Populism","#ef4444",[
        ("What Is Populism?","Jan-Werner M&uuml;ller (2016)","Precise definition of populism; cuts through loose public usage. START HERE."),
        ("How Democracies Die","Levitsky &amp; Ziblatt (2018)","Concrete historical examples of democratic backsliding; connects theory to reality."),
        ("Populism: A Very Short Introduction","Mudde &amp; Kaltwasser (2017)","Clear mapping of the political landscape without oversimplification."),
        ("On Populist Reason","Ernesto Laclau (2005)","Demanding but forces you to consider populism as democratic possibility, not just pathology."),
        ("The Origins of Totalitarianism","Hannah Arendt (1951)","Shows how mass resentment evolves into something far more dangerous."),
    ]),
    ("p2","Prompt 2 &mdash; Nation-States","#f97316",[
        ("Imagined Communities","Benedict Anderson (1983)","Seminal argument that nations are socially constructed through shared stories."),
        ("Modernity at Large","Arjun Appadurai (1996)","Global cultural flows that destabilize borders and state authority."),
        ("Nations and Nationalism Since 1780","Eric Hobsbawm (1990)","Historical account of how nation-states emerged and how fragile they may be."),
        ("Globalization and Its Discontents","Joseph Stiglitz (2002)","Critique of global economic institutions and their impact on sovereignty."),
        ("Cosmopolitanism","Kwame Anthony Appiah (2006)","Moral argument for global citizenship grounded in shared human obligations."),
    ]),
    ("p3","Prompt 3 &mdash; AI Legal Personhood","#8b5cf6",[
        ("AI: A Guide for Thinking Humans","Melanie Mitchell (2019)","What AI actually does and where its limits lie. Grounds responsibility in human design."),
        ("The Machine Question","David J. Gunkel (2012)","Core question: to what extent should intelligent machines have moral/legal significance?"),
        ("The Age of Surveillance Capitalism","Shoshana Zuboff (2019)","How AI systems reshape power, accountability, and privacy."),
        ("Weapons of Math Destruction","Cathy O'Neil (2016)","Human consequences of algorithmic decisions; makes ethics impossible to ignore."),
        ("Superintelligence","Nick Bostrom (2014)","Speculative but influential on risks of advanced AI autonomy."),
    ]),
    ("p4","Prompt 4 &mdash; Colonial Artifacts","#10b981",[
        ("The Brutish Museums","Dan Hicks (2020)","Powerful critique of museum collections rooted in colonial violence."),
        ("Who Owns Antiquity?","James Cuno (2008)","Defense of universal museums and shared global heritage."),
        ("Culture and Imperialism","Edward Said (1993)","Foundational text on how culture sustains imperial power."),
        ("Africa's Struggle for Its Art","B&eacute;n&eacute;dicte Savoy (2022)","Insider account of restitution debates in European museums."),
        ("Empireland","Sathnam Sanghera (2021)","Contemporary reckoning with how empire continues to shape public institutions."),
    ]),
    ("p5","Prompt 5 &mdash; Meritocracy","#f59e0b",[
        ("The Tyranny of Merit","Michael Sandel (2020)","Critique of meritocracy as a moral framework; argues it breeds hubris and resentment."),
        ("The Rise of the Meritocracy","Michael Young (1958)","The original coining of the term &mdash; written as a dystopian warning, not a blueprint."),
        ("A Theory of Justice","John Rawls (1971)","The philosophical framework for thinking about fair distribution of opportunities."),
    ]),
    ("p6","Prompt 6 &mdash; Open Borders","#06b6d4",[
        ("The Ethics of Immigration","Joseph Carens (2013)","Most rigorous philosophical case for open borders as a basic moral right."),
        ("Strangers in Our Midst","David Miller (2016)","Principled defense of border controls grounded in democratic responsibility."),
        ("Exodus: How Migration Is Changing Our World","Paul Collier (2013)","Examines how large-scale migration affects both sending and receiving countries."),
        ("The Origins of Totalitarianism","Hannah Arendt (1951)","Discussion of statelessness; foundational for understanding lack of political membership."),
    ]),
    ("p7","Prompt 7 &mdash; Scientific Constraints","#ec4899",[
        ("The Ethics of Invention","Sheila Jasanoff (2016)","Political and moral responsibility involved in choosing which futures to pursue."),
        ("The Entrepreneurial State","Mariana Mazzucato (2013)","How transformative technologies emerged from high-risk public investment."),
        ("The Pleasure of Finding Things Out","Richard Feynman (1999)","Intellectual value of curiosity-driven research; the scientist's perspective."),
        ("Frontiers of Illusion","Daniel Sarewitz (1996)","Critique of the assumption that ambitious science automatically produces social benefit."),
    ]),
    ("p8","Prompt 8 &mdash; Technology Restrictions","#14b8a6",[
        ("Superintelligence","Nick Bostrom (2014)","Forces students to take existential risk seriously rather than dismissing it."),
        ("Homo Deus","Yuval Noah Harari (2016)","How narratives of progress can obscure ethical limits."),
        ("Frankenstein","Mary Shelley (1818)","Still unmatched as a literary exploration of scientific ambition without responsibility."),
        ("The Ethics of Invention","Sheila Jasanoff (2016)","Crucial text for examining governance failures in emerging science."),
        ("Laws of Fear","Cass Sunstein (2005)","Framework for thinking rationally about low-probability but high-impact risks."),
    ]),
    ("p9","Prompt 9 &mdash; What Does It Mean to Heal?","#6366f1",[
        ("Man's Search for Meaning","Viktor Frankl (1946)","Essential meditation on suffering, meaning, and survival."),
        ("The Body Keeps the Score","Bessel van der Kolk (2014)","Analysis of trauma and embodied memory; healing as a physical and social process."),
        ("Illness as Metaphor","Susan Sontag (1978)","Critique of how illness shapes identity and moral judgment."),
        ("Being Mortal","Atul Gawande (2014)","Reflection on medicine, aging, and the limits of cure."),
        ("Trauma and Recovery","Judith Herman (1992)","Foundational work on psychological effects of trauma; healing as a social process."),
    ]),
]

for pc, title, color, books in reading:
    w(f'<div class="card" style="border-top:3px solid {color};margin-bottom:16px">\n')
    w(f'<div class="ctitle">{title}</div>\n')
    w('<div class="book-grid">\n')
    for btitle, bauthor, bwhy in books:
        w(f'<div class="book-card" style="border-top-color:{color}">\n')
        w(f'<div class="book-title">{btitle}</div>\n')
        w(f'<div class="book-author">{bauthor}</div>\n')
        w(f'<div class="book-why">{bwhy}</div>\n')
        w('</div>\n')
    w('</div>\n</div>\n')

w('<div class="sh">&#127760; Free Academic Sources</div>\n')
w('<div class="grid2">\n')
w('<div class="card"><div class="ctitle">&#128269; Where to Find Sources</div>\n')
w('<ul class="al">\n')
w('<li><span>1</span><strong>Google Scholar</strong> (scholar.google.com) &mdash; search for author + title</li>\n')
w('<li><span>2</span><strong>JSTOR</strong> (jstor.org) &mdash; free access to many humanities journals</li>\n')
w('<li><span>3</span><strong>PhilPapers</strong> (philpapers.org) &mdash; philosophy papers, many free</li>\n')
w('<li><span>4</span><strong>SSRN</strong> (ssrn.com) &mdash; social science working papers</li>\n')
w('<li><span>5</span><strong>Project MUSE</strong> &mdash; humanities and social science journals</li>\n')
w('<li><span>6</span><strong>Your school library</strong> &mdash; ask for database access (EBSCO, ProQuest)</li>\n')
w('</ul></div>\n')
w('<div class="card"><div class="ctitle">&#128218; Reading Strategy</div>\n')
w('<ul class="al">\n')
w('<li><span>1</span>Read the <strong>introduction and conclusion</strong> of each book first &mdash; get the argument</li>\n')
w('<li><span>2</span>Find the <strong>chapter most relevant</strong> to your thesis and read it fully</li>\n')
w('<li><span>3</span>Note <strong>key quotes with page numbers</strong> as you read</li>\n')
w('<li><span>4</span>Look at the <strong>bibliography</strong> of each book for more sources</li>\n')
w('<li><span>5</span>Aim for <strong>5&ndash;8 sources</strong> minimum; quality over quantity</li>\n')
w('</ul></div>\n')
w('</div>\n')
w('</div>\n')
f.close()
print("Part 7 done")