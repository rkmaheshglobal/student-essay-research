"""Essay Prep App Part 4: Economics Q1 - Cashless Society"""

def get_econ_q1():
    return '''<!-- ECONOMICS Q1 -->
<div id="pg-eq1" class="pg">
  <div class="ph"><h2>💳 Q1: Should we fear a cashless society?</h2><p>Type: Evaluation/Fear Assessment · Theme: Monetary policy, Privacy, Financial inclusion</p></div>
  <div class="tabs">
    <button class="tab on" onclick="tab(this,'eq1a')">Overview</button>
    <button class="tab" onclick="tab(this,'eq1b')">The Debate</button>
    <button class="tab" onclick="tab(this,'eq1c')">Thesis Options</button>
    <button class="tab" onclick="tab(this,'eq1d')">Key Data</button>
    <button class="tab" onclick="tab(this,'eq1e')">Case Studies</button>
  </div>
  <div id="eq1a" class="tc on">
    <div class="card">
      <div class="ct">🔍 What the Question is Really Asking</div>
      <p style="font-family:sans-serif;font-size:13px;line-height:1.8;margin-bottom:14px">The word <b>"fear"</b> implies a rational assessment of risk serious enough to warrant action — not mere discomfort or nostalgia for cash. Distinguish: irrational fear (technophobia) vs. rational precaution vs. structural fear (systemic risks individuals cannot mitigate).</p>
      <div class="g2">
        <div><b style="font-family:sans-serif;font-size:12px">Key Terms to Define:</b><ul class="pts" style="margin-top:7px"><li><b>Fear</b> — rational precaution vs. irrational technophobia</li><li><b>Cashless society</b> — cash-light? near-cashless? fully cashless?</li><li><b>Society</b> — developed vs. developing countries differ enormously</li></ul></div>
        <div><b style="font-family:sans-serif;font-size:12px">Spectrum of Cashlessness:</b><ul class="pts" style="margin-top:7px"><li>Cash-light: UK, Australia</li><li>Near-cashless: Sweden (98% digital)</li><li>Fully cashless: No country has achieved this</li><li>Programmable: China's e-CNY experiments</li></ul></div>
      </div>
    </div>
    <div class="card">
      <div class="ct">✍️ Sample Opening Paragraph</div>
      <bq>"In 2016, the Indian government invalidated 86% of the country's currency overnight, forcing a billion people into a digital payment system many had never used. The chaos that followed — bank queues, business failures, and over 100 deaths — revealed what a cashless transition looks like when imposed rather than chosen. Sweden, by contrast, has achieved near-total cashlessness through gradual adoption, with robust safeguards for the elderly and unconnected. These two paths illuminate the real question: not whether to fear cashlessness, but whether to fear the particular cashless society being built."</bq>
    </div>
  </div>
  <div id="eq1b" class="tc">
    <div class="card">
      <div class="ct">⚖️ The Core Debate</div>
      <div class="g2">
        <div class="pro"><h4>✅ Arguments AGAINST Fear</h4><ul class="pts"><li><b>Efficiency:</b> Cash handling costs €50B/year in Europe (ECB)</li><li><b>Crime reduction:</b> Sweden robberies fell 70% as cash declined</li><li><b>Financial inclusion:</b> M-Pesa lifted 194,000 Kenyan households out of poverty (Suri & Jack, 2016)</li><li><b>Monetary policy:</b> Removes zero lower bound constraint on interest rates</li><li><b>Hygiene:</b> Cash carries bacteria; COVID highlighted this</li></ul></div>
        <div class="con"><h4>⚠️ Arguments FOR Fear</h4><ul class="pts"><li><b>Privacy:</b> Every transaction traceable; surveillance capitalism (Zuboff, 2019)</li><li><b>Exclusion:</b> 1.4B unbanked globally; elderly, homeless excluded</li><li><b>Fragility:</b> 302 UK payment outages in 4 years (FCA)</li><li><b>Programmable money:</b> China's e-CNY has expiry dates; Canada froze protesters' accounts (2022)</li><li><b>Private power:</b> Visa + Mastercard control 80%+ of transactions</li></ul></div>
      </div>
    </div>
    <div class="card">
      <div class="ct">🔄 Counterarguments & Responses</div>
      <table>
        <tr><th>Counterargument</th><th>Your Response</th></tr>
        <tr><td>"Cash enables crime and tax evasion"</td><td>Criminals adapt to crypto/hawala. The cost of eliminating cash (privacy, exclusion) exceeds the benefit. Most cash users are not criminals.</td></tr>
        <tr><td>"M-Pesa shows digital payments are more inclusive"</td><td>Context-dependent. Works in Kenya because mobile penetration > banking penetration. In developed countries, the unbanked are often also digitally excluded.</td></tr>
        <tr><td>"Sweden shows cashlessness can work well"</td><td>Sweden is the best-case scenario — and even Sweden reversed course. Riksbank now requires cash services; government recommends holding cash for emergencies.</td></tr>
        <tr><td>"Governments won't abuse surveillance powers"</td><td>Historical evidence says otherwise. Canada froze legal protesters' accounts (2022). China uses payment data for social control. Surveillance infrastructure outlasts the governments that create it.</td></tr>
      </table>
    </div>
  </div>
  <div id="eq1c" class="tc">
    <div class="card">
      <div class="ct">🎯 Three Winning Thesis Options</div>
      <div class="thesis"><div class="tl">⭐ Option A — Recommended: "Fear the Design, Not the Technology"</div><div class="tt">"We should fear not cashlessness itself, but the particular cashless societies being built. The risks — surveillance, exclusion, fragility, and loss of monetary freedom — are real and serious. But they are not inherent to digital payments; they are the result of design choices. Fear should motivate better design: privacy-preserving currencies, universal access, resilient infrastructure, and democratic accountability."</div></div>
      <div class="thesis"><div class="tl">Option B: "Yes, Fear It — But Conditionally"</div><div class="tt">"We should fear a cashless society as currently designed. The efficiency gains are real but modest; the risks — to privacy, inclusion, and freedom — are profound and unevenly distributed. Until digital payment systems can guarantee the anonymity, universality, and resilience of cash, eliminating it would be a serious mistake."</div></div>
      <div class="thesis"><div class="tl">Option C: "The Distributional Fear"</div><div class="tt">"Whether to fear a cashless society depends on who you are. For the digitally connected and financially secure, cashlessness is convenient and efficient. For the elderly, the poor, the marginalized, and those living under authoritarian governments, it is a source of genuine fear. A society that eliminates cash without safeguarding these groups has chosen efficiency over justice."</div></div>
    </div>
    <div class="card">
      <div class="ct">📐 Theoretical Frameworks</div>
      <table>
        <tr><th>Framework</th><th>Application</th><th>Source</th></tr>
        <tr><td><b>Public Goods</b></td><td>Cash is non-excludable, non-rivalrous — a public good. Eliminating it privatizes a public good.</td><td>Goodhart & Lastra (2018)</td></tr>
        <tr><td><b>Rawlsian Veil of Ignorance</b></td><td>If you might be elderly, homeless, or under authoritarian rule, would you choose cashlessness?</td><td>Rawls (1971)</td></tr>
        <tr><td><b>Institutional Economics</b></td><td>Strong institutions + cashlessness = Sweden. Weak institutions + cashlessness = surveillance state.</td><td>Acemoglu & Robinson (2012)</td></tr>
        <tr><td><b>Habermas: Lifeworld vs. System</b></td><td>Cash enables informal lifeworld transactions. Digital payments colonize them with system logic.</td><td>Habermas (1984)</td></tr>
      </table>
    </div>
  </div>
  <div id="eq1d" class="tc">
    <div class="card">
      <div class="ct">📊 Key Data Points with Academic Sources</div>
      <table>
        <tr><th>Statistic</th><th>Source</th><th>Use In Essay</th></tr>
        <tr><td>Sweden: 98% of transactions are digital</td><td><a href="https://www.riksbank.se/en-gb/payments--cash/payments-in-sweden/" target="_blank" rel="noopener" style="color:#ff6f00;font-size:11px;text-decoration:none;font-weight:600">Riksbank (2023) &#8599;</a></td><td>Leading example of cashlessness</td></tr>
        <tr><td>1.4 billion adults globally unbanked</td><td><a href="https://www.worldbank.org/en/publication/globalfindex" target="_blank" rel="noopener" style="color:#ff6f00;font-size:11px;text-decoration:none;font-weight:600">World Bank Findex (2022) &#8599;</a></td><td>Financial exclusion risk</td></tr>
        <tr><td>M-Pesa lifted 194,000 Kenyan households out of poverty</td><td><a href="https://scholar.google.com/scholar?q=Suri+Jack+mobile+money+poverty+Kenya+Science+2016" target="_blank" rel="noopener" style="color:#ff6f00;font-size:11px;text-decoration:none;font-weight:600">Suri &amp; Jack, Science (2016) &#8599;</a></td><td>Inclusion success story</td></tr>
        <tr><td>India demonetization: 86% of currency invalidated overnight</td><td><a href="https://www.rbi.org.in/" target="_blank" rel="noopener" style="color:#ff6f00;font-size:11px;text-decoration:none;font-weight:600">RBI (2016) &#8599;</a></td><td>Government power over money</td></tr>
        <tr><td>UK cash use: fell from 60% to 15% (2010–2023)</td><td><a href="https://www.ukfinance.org.uk/data-and-research/data/payments/payment-markets-report" target="_blank" rel="noopener" style="color:#ff6f00;font-size:11px;text-decoration:none;font-weight:600">UK Finance (2023) &#8599;</a></td><td>Trend toward cashlessness</td></tr>
        <tr><td>302 major UK payment system outages (2018–2022)</td><td><a href="https://www.fca.org.uk/publications/multi-firm-reviews/operational-resilience-payment-firms" target="_blank" rel="noopener" style="color:#ff6f00;font-size:11px;text-decoration:none;font-weight:600">FCA (2022) &#8599;</a></td><td>System fragility</td></tr>
        <tr><td>China social credit: 23 million people banned from flights/trains</td><td><a href="https://www.bbc.com/news/world-asia-china-47838096" target="_blank" rel="noopener" style="color:#ff6f00;font-size:11px;text-decoration:none;font-weight:600">Chinese govt data (2019) &#8599;</a></td><td>Surveillance risk</td></tr>
        <tr><td>Visa + Mastercard: 80%+ of global card transactions</td><td><a href="https://nilsonreport.com/" target="_blank" rel="noopener" style="color:#ff6f00;font-size:11px;text-decoration:none;font-weight:600">Nilson Report (2023) &#8599;</a></td><td>Private power concentration</td></tr>
      </table>
    </div>
  </div>
  <div id="eq1e" class="tc">
    <div class="card">
      <div class="ct">🌍 Case Studies: Cashless Societies Around the World</div>
      <table>
        <tr><th>Country</th><th>Key Facts</th><th>Lesson for Essay</th></tr>
        <tr>
          <td><b>🇸🇪 Sweden</b></td>
          <td>98% of transactions digital; Riksbank launched e-krona pilot; some elderly &amp; rural citizens excluded; Kontantupproret (cash uprising) movement formed</td>
          <td>Most advanced cashless case — use to show both benefits (efficiency) and costs (exclusion, fragility)</td>
        </tr>
        <tr>
          <td><b>🇮🇳 India</b></td>
          <td>2016 demonetization: 86% of currency invalidated overnight; GDP fell 1.5%; UPI payments grew 10x by 2023; 190M still unbanked</td>
          <td>Government-forced cashlessness — shows state power over money and transition costs</td>
        </tr>
        <tr>
          <td><b>🇰🇪 Kenya</b></td>
          <td>M-Pesa launched 2007; 96% of Kenyans use mobile money; lifted 194,000 households out of poverty (Suri &amp; Jack, 2016); works without smartphones</td>
          <td>Positive inclusion story — mobile money can reach the unbanked without full cashlessness</td>
        </tr>
        <tr>
          <td><b>🇨🇳 China</b></td>
          <td>WeChat Pay + Alipay: 94% of urban payments; social credit system linked to payment data; 23M people banned from travel; foreign visitors struggle without Chinese bank accounts</td>
          <td>Surveillance risk made concrete — digital payments enable state monitoring at scale</td>
        </tr>
        <tr>
          <td><b>🇳🇱 Netherlands</b></td>
          <td>70% cashless; De Nederlandsche Bank mandates cash acceptance by law; 2019 law requires retailers to accept cash to protect vulnerable groups</td>
          <td>Regulatory response — shows governments can mandate cash access even in cashless economies</td>
        </tr>
      </table>
    </div>
    <div class="card">
      <div class="ct">💡 How to Use Case Studies in Your Essay</div>
      <ul class="pts">
        <li><b>Don't just describe</b> — use each case to support or challenge a specific claim in your argument</li>
        <li><b>Compare across contexts</b> — Sweden (rich, high-trust) vs. India (developing, diverse) shows cashlessness is not one-size-fits-all</li>
        <li><b>Acknowledge complexity</b> — Kenya's M-Pesa shows digital payments can <em>increase</em> inclusion without eliminating cash</li>
        <li><b>Use specific data</b> — "86% of India's currency invalidated overnight" is more persuasive than "India tried demonetization"</li>
        <li><b>Strongest counter-case</b> — China shows that cashlessness + authoritarian government = surveillance infrastructure</li>
      </ul>
    </div>
  </div>
</div>
'''

if __name__ == "__main__":
    print(get_econ_q1())
    print("Part 4 (Economics Q1) ready")