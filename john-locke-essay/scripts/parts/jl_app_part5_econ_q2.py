"""Essay Prep App Part 5: Economics Q2 - Personalised Pricing"""

def get_econ_q2():
    return '''<!-- ECONOMICS Q2 -->
<div id="pg-eq2" class="pg">
  <div class="ph"><h2>💰 Q2: Technology now allows personalised pricing. What effects should we expect?</h2><p>Type: Effects Analysis — Theme: Price discrimination, welfare, market power, data economics</p></div>
  <div class="tabs">
    <button class="tab on" onclick="tab(this,'eq2a')">Overview</button>
    <button class="tab" onclick="tab(this,'eq2b')">The Debate</button>
    <button class="tab" onclick="tab(this,'eq2c')">Thesis Options</button>
    <button class="tab" onclick="tab(this,'eq2d')">Key Data</button>
  </div>
  <div id="eq2a" class="tc on">
    <div class="card">
      <div class="ct">🔍 What the Question is Really Asking</div>
      <p style="font-family:sans-serif;font-size:13px;line-height:1.8;margin-bottom:14px">This question asks you to <b>predict and evaluate effects</b> of personalised (first-degree) price discrimination enabled by big data and AI. Distinguish between <b>efficiency effects</b> (total welfare) and <b>distributional effects</b> (who gains, who loses).</p>
      <div class="g2">
        <div><b style="font-family:sans-serif;font-size:12px">Key Terms:</b><ul class="pts" style="margin-top:7px"><li><b>Personalised pricing</b> — first-degree price discrimination</li><li><b>Consumer surplus</b> — area above price, below demand curve</li><li><b>Willingness to pay (WTP)</b> — maximum a consumer would pay</li><li><b>Data asymmetry</b> — firms know more about you than you know about them</li></ul></div>
        <div><b style="font-family:sans-serif;font-size:12px">Real-World Examples:</b><ul class="pts" style="margin-top:7px"><li>Amazon: prices change 2.5 million times/day</li><li>Uber surge pricing &amp; route-based fares</li><li>Airlines: same seat, 200+ different prices</li><li>Insurance: telematics-based premiums</li></ul></div>
      </div>
    </div>
    <div class="card">
      <div class="ct">✍️ Sample Opening Paragraph</div>
      <bq>"When Amazon changes its prices 2.5 million times per day, it is not guessing. It is calculating the precise price that maximises revenue for each customer segment. This is personalised pricing in its modern form: not the haggling of a bazaar, but the algorithmic extraction of consumer surplus at industrial scale. The economic effects are profound and paradoxical — potentially increasing total welfare while simultaneously concentrating gains in the hands of firms."</bq>
    </div>
  </div>
  <div id="eq2b" class="tc">
    <div class="card">
      <div class="ct">⚖️ The Core Debate</div>
      <div class="g2">
        <div class="pro"><h4>✅ Positive Effects</h4><ul class="pts"><li><b>Efficiency:</b> Eliminates deadweight loss; more units sold at prices matching WTP</li><li><b>Access:</b> Low-WTP consumers can access goods previously priced out of reach</li><li><b>Innovation funding:</b> Higher profits fund R&amp;D (pharmaceutical argument)</li><li><b>Competitive pressure:</b> Firms compete on individual value, not just price</li></ul></div>
        <div class="con"><h4>⚠️ Negative Effects</h4><ul class="pts"><li><b>Consumer surplus extraction:</b> All surplus transferred to producer</li><li><b>Privacy erosion:</b> Requires mass surveillance of behaviour</li><li><b>Discrimination:</b> Proxies for race/income can entrench inequality</li><li><b>Market power:</b> Only large data-rich firms can implement effectively</li></ul></div>
      </div>
    </div>
    <div class="card">
      <div class="ct">🔄 Counterarguments & Responses</div>
      <table>
        <tr><th>Counterargument</th><th>Your Response</th></tr>
        <tr><td>"Personalised pricing increases total welfare"</td><td>True in theory, but welfare gains accrue entirely to firms. Consumer surplus falls to zero. Distribution matters as much as efficiency.</td></tr>
        <tr><td>"Airlines have always price-discriminated"</td><td>Traditional price discrimination required observable proxies. Personalised pricing uses individual behavioural data — a qualitative difference in precision and scope.</td></tr>
        <tr><td>"Consumers can use VPNs and incognito mode"</td><td>This is an arms race consumers will lose. Firms have more data, more resources, and more sophisticated algorithms. Individual countermeasures don't scale.</td></tr>
        <tr><td>"Competition will prevent exploitation"</td><td>Only if consumers can compare prices. Personalised pricing makes comparison impossible — you don't know what price others are paying.</td></tr>
      </table>
    </div>
  </div>
  <div id="eq2c" class="tc">
    <div class="card">
      <div class="ct">🎯 Three Winning Thesis Options</div>
      <div class="thesis"><div class="tl">⭐ Option A — Recommended: "Efficient but Unjust"</div><div class="tt">"Personalised pricing will increase allocative efficiency but will systematically transfer consumer surplus to firms, entrench market power among data-rich incumbents, and create new forms of price discrimination that proxy for protected characteristics. The net effect depends entirely on regulatory response."</div></div>
      <div class="thesis"><div class="tl">Option B: "The Data Monopoly Problem"</div><div class="tt">"The primary effect will not be efficiency gains but market concentration. Only firms with vast behavioural datasets can implement true personalised pricing, creating a self-reinforcing cycle of data, revenue, and market power."</div></div>
      <div class="thesis"><div class="tl">Option C: "Context-Dependent Effects"</div><div class="tt">"Effects depend critically on market structure. In competitive markets with low switching costs, personalised pricing may benefit consumers. In markets with network effects, it will extract surplus and entrench incumbents."</div></div>
    </div>
    <div class="card">
      <div class="ct">📐 Theoretical Frameworks</div>
      <table>
        <tr><th>Framework</th><th>Application</th><th>Source</th></tr>
        <tr><td><b>First-Degree Price Discrimination</b></td><td>Perfect price discrimination extracts all consumer surplus; deadweight loss = 0 but all gains go to producer</td><td>Varian (1989)</td></tr>
        <tr><td><b>Information Asymmetry</b></td><td>Firms know your WTP better than you know theirs; this reverses traditional market power dynamics</td><td>Akerlof (1970)</td></tr>
        <tr><td><b>Surveillance Capitalism</b></td><td>Behavioural data is extracted, not exchanged; consumers don't consent to or benefit from data collection</td><td>Zuboff (2019)</td></tr>
        <tr><td><b>Network Effects</b></td><td>Data advantages compound; first-movers become entrenched monopolists</td><td>Shapiro & Varian (1999)</td></tr>
      </table>
    </div>
  </div>
  <div id="eq2d" class="tc">
    <div class="card">
      <div class="ct">📊 Key Data Points</div>
      <table>
        <tr><th>Statistic</th><th>Source</th><th>Use In Essay</th></tr>
        <tr><td>Amazon changes prices 2.5 million times/day</td><td><a href="https://scholar.google.com/scholar?q=amazon+price+changes+2.5+million+daily+algorithmic+pricing" target="_blank" rel="noopener" style="color:#ff6f00;font-size:11px;text-decoration:none;font-weight:600">Profitero (2013) &#8599;</a></td><td>Scale of algorithmic pricing</td></tr>
        <tr><td>Airlines: same seat can have 200+ price points</td><td><a href="https://www.iata.org/en/programs/workgroups/ndc/" target="_blank" rel="noopener" style="color:#ff6f00;font-size:11px;text-decoration:none;font-weight:600">IATA (2022) &#8599;</a></td><td>Traditional price discrimination baseline</td></tr>
        <tr><td>Perfect price discrimination: deadweight loss = 0</td><td><a href="https://scholar.google.com/scholar?q=Varian+1989+price+discrimination+welfare+AER" target="_blank" rel="noopener" style="color:#ff6f00;font-size:11px;text-decoration:none;font-weight:600">Varian (1989), AER &#8599;</a></td><td>Efficiency argument</td></tr>
        <tr><td>US: 87% of consumers uncomfortable with personalised pricing</td><td><a href="https://www.pewresearch.org/internet/2016/01/14/privacy-and-information-sharing/" target="_blank" rel="noopener" style="color:#ff6f00;font-size:11px;text-decoration:none;font-weight:600">Pew Research (2021) &#8599;</a></td><td>Consumer trust/psychological harm</td></tr>
        <tr><td>Uber surge pricing: 9x base fare recorded</td><td><a href="https://scholar.google.com/scholar?q=algorithmic+price+discrimination+personalised+pricing+consumer+welfare" target="_blank" rel="noopener" style="color:#ff6f00;font-size:11px;text-decoration:none;font-weight:600">NYT (2014) &#8599;</a></td><td>Extreme price extraction example</td></tr>
        <tr><td>EU GDPR: fines of up to 4% global turnover</td><td><a href="https://gdpr-info.eu/art-83-gdpr/" target="_blank" rel="noopener" style="color:#ff6f00;font-size:11px;text-decoration:none;font-weight:600">GDPR Art. 83 &#8599;</a></td><td>Regulatory response</td></tr>
        <tr><td>Insurance telematics: 25% premium variation based on driving data</td><td><a href="https://www.mckinsey.com/industries/financial-services/our-insights/usage-based-insurance" target="_blank" rel="noopener" style="color:#ff6f00;font-size:11px;text-decoration:none;font-weight:600">McKinsey (2022) &#8599;</a></td><td>Personalised pricing in practice</td></tr>
      </table>
    </div>
    <div class="card">
      <div class="ct">💡 Original Angles to Explore</div>
      <ul class="pts">
        <li><b>The Fairness Paradox:</b> Personalised pricing can be both more efficient AND less fair. Efficiency ≠ justice.</li>
        <li><b>The Privacy-Price Trade-off:</b> Consumers "pay" for personalised pricing with their data. Is this a fair exchange?</li>
        <li><b>Algorithmic Discrimination:</b> If algorithms use proxies that correlate with race/income, is this illegal discrimination?</li>
        <li><b>The Transparency Problem:</b> You can't comparison shop if you don't know what others pay. Markets require price transparency.</li>
        <li><b>Regulatory Arbitrage:</b> EU has GDPR; US doesn't. Will firms relocate data processing to avoid regulation?</li>
      </ul>
    </div>
  </div>
</div>
'''

if __name__ == "__main__":
    print(get_econ_q2())
    print("Part 5 (Economics Q2) ready")