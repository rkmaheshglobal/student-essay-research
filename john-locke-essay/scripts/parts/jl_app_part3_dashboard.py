"""Essay Prep App Part 3: Dashboard with Economics & Politics"""

def get_app_dashboard():
    return '''<!-- DASHBOARD -->
<div id="pg-dash" class="pg on">
  <div class="ph"><h2>📊 Competition Dashboard</h2><p>John Locke Institute Essay Competition 2026 — Economics & Politics</p></div>
  <div class="g3">
    <div class="cc r"><div class="cd" id="dq">–</div><div class="cl">Days Until Questions Open</div><div class="cdt">April 1, 2026</div></div>
    <div class="cc o"><div class="cd" id="ds">–</div><div class="cl">Days to Secondary Deadline</div><div class="cdt">May 10, 2026</div></div>
    <div class="cc"><div class="cd" id="dd">–</div><div class="cl">Days to Final Deadline</div><div class="cdt">May 31, 2026</div></div>
  </div>
  
  <div class="g2">
    <div class="card">
      <div class="ct" style="color:#ff6f00">📈 Economics 2026 Questions &nbsp;<a href="https://www.johnlockeinstitute.com/essay-competition" target="_blank" rel="noopener" style="font-size:11px;color:var(--a);font-weight:400">&#128279; JLI Page</a></div>
      <div style="font-family:sans-serif;font-size:13px;line-height:1.9">
        <div style="padding:7px 0;border-bottom:1px solid var(--b)"><span class="badge bb">Q1</span> &nbsp;Should we fear a cashless society?</div>
        <div style="padding:7px 0;border-bottom:1px solid var(--b)"><span class="badge by">Q2</span> &nbsp;Technology now allows personalised pricing. What effects should we expect?</div>
        <div style="padding:7px 0"><span class="badge br">Q3</span> &nbsp;Did Jeff Bezos get rich at the expense of his customers, his employees, neither or both?</div>
      </div>
    </div>
    <div class="card">
      <div class="ct" style="color:#10b981">🏛️ Politics 2026 Questions &nbsp;<a href="https://www.johnlockeinstitute.com/essay-competition" target="_blank" rel="noopener" style="font-size:11px;color:var(--pol);font-weight:400">&#128279; JLI Page</a></div>
      <div style="font-family:sans-serif;font-size:13px;line-height:1.9">
        <div style="padding:7px 0;border-bottom:1px solid var(--b)"><span class="badge bg">Q1</span> &nbsp;Is the right to self-determination absolute?</div>
        <div style="padding:7px 0;border-bottom:1px solid var(--b)"><span class="badge bg">Q2</span> &nbsp;Should states have the right to control their borders?</div>
        <div style="padding:7px 0"><span class="badge bg">Q3</span> &nbsp;Is nationalism compatible with liberalism?</div>
      </div>
    </div>
  </div>
  
  <div class="card">
    <div class="ct">🔑 What Judges Look For</div>
    <div style="font-family:sans-serif;font-size:12px">
      <div style="margin-bottom:9px"><div style="display:flex;justify-content:space-between;margin-bottom:3px"><span>Original Thinking</span><b style="color:var(--a)">30%</b></div><div class="pb"><div class="pf" style="width:30%"></div></div></div>
      <div style="margin-bottom:9px"><div style="display:flex;justify-content:space-between;margin-bottom:3px"><span>Clear Argumentation</span><b style="color:var(--a)">25%</b></div><div class="pb"><div class="pf" style="width:25%"></div></div></div>
      <div style="margin-bottom:9px"><div style="display:flex;justify-content:space-between;margin-bottom:3px"><span>Counterargument Engagement</span><b style="color:var(--a)">20%</b></div><div class="pb"><div class="pf" style="width:20%"></div></div></div>
      <div style="margin-bottom:9px"><div style="display:flex;justify-content:space-between;margin-bottom:3px"><span>Evidence-Based Reasoning</span><b style="color:var(--a)">15%</b></div><div class="pb"><div class="pf" style="width:15%"></div></div></div>
      <div><div style="display:flex;justify-content:space-between;margin-bottom:3px"><span>Writing Quality</span><b style="color:var(--a)">10%</b></div><div class="pb"><div class="pf" style="width:10%"></div></div></div>
    </div>
  </div>
  
  <div class="g2">
    <div class="card">
      <div class="ct">📊 Economics Question Selection</div>
      <table>
        <tr><th>Factor</th><th>Q1</th><th>Q2</th><th>Q3</th></tr>
        <tr><td><b>Originality</b></td><td><span class="badge by">Med</span></td><td><span class="badge bg">High⭐</span></td><td><span class="badge by">Med</span></td></tr>
        <tr><td><b>Cliché Risk</b></td><td><span class="badge by">Med</span></td><td><span class="badge bg">Low⭐</span></td><td><span class="badge br">High</span></td></tr>
        <tr><td><b>Data</b></td><td><span class="badge bg">High</span></td><td><span class="badge by">Med</span></td><td><span class="badge bg">High</span></td></tr>
      </table>
    </div>
    <div class="card">
      <div class="ct">📊 Politics Question Selection</div>
      <table>
        <tr><th>Factor</th><th>Q1</th><th>Q2</th><th>Q3</th></tr>
        <tr><td><b>Originality</b></td><td><span class="badge bg">High⭐</span></td><td><span class="badge by">Med</span></td><td><span class="badge bg">High⭐</span></td></tr>
        <tr><td><b>Cliché Risk</b></td><td><span class="badge by">Med</span></td><td><span class="badge br">High</span></td><td><span class="badge by">Med</span></td></tr>
        <tr><td><b>Theory</b></td><td><span class="badge bg">Rich</span></td><td><span class="badge bg">Rich</span></td><td><span class="badge bg">Rich</span></td></tr>
      </table>
    </div>
  </div>
  
  <div class="card">
    <div class="ct">⚡ Quick Start — This Week</div>
    <div class="g2">
      <div class="pro"><h4>✅ Free Actions (Do Today)</h4><ul class="pts"><li>Read all question deep dives in this app</li><li>Email your teacher for mentorship</li><li>Sign up for Marginal Revolution University (free)</li><li>Read past JLI winning essays on their website</li></ul></div>
      <div class="con"><h4>📌 This Week (Invest)</h4><ul class="pts"><li>Choose your category (Economics or Politics)</li><li>Choose your top 1-2 questions to focus on</li><li>Start reading from the reading list</li><li>Build your sources document</li></ul></div>
    </div>
  </div>
</div>

<!-- TIMELINE -->
<div id="pg-time" class="pg">
  <div class="ph"><h2>📅 Timeline & Action Plan</h2><p>Week-by-week execution plan for the 2026 competition</p></div>
  <div class="card">
    <div class="ct">🗓️ Key Dates</div>
    <div class="tl-w">
      <div class="tli"><div class="tld" style="background:#e74c3c"></div><div class="td">March 13–31, 2026</div><div class="tt2">Phase 1: Preparation</div><div class="td2">Foundation building, deep research, question analysis prep</div></div>
      <div class="tli"><div class="tld" style="background:#f39c12"></div><div class="td">April 1, 2026</div><div class="tt2">🎯 Questions Released</div><div class="td2">Official questions published — analyze immediately, choose your question</div></div>
      <div class="tli"><div class="tld"></div><div class="td">April 3–9, 2026</div><div class="tt2">Thesis & Outline</div><div class="td2">Develop clear thesis, create detailed outline, get mentor feedback</div></div>
      <div class="tli"><div class="tld"></div><div class="td">April 10–16, 2026</div><div class="tt2">First Draft</div><div class="td2">Complete rough first draft (~2,000 words)</div></div>
      <div class="tli"><div class="tld"></div><div class="td">April 17–30, 2026</div><div class="tt2">Revision Rounds 1 & 2</div><div class="td2">Strengthen arguments, address counterarguments, incorporate feedback</div></div>
      <div class="tli"><div class="tld" style="background:#f39c12"></div><div class="td">May 10, 2026</div><div class="tt2">📝 Secondary Competition Deadline</div><div class="td2">Submit to secondary competition for early feedback</div></div>
      <div class="tli"><div class="tld"></div><div class="td">May 11–28, 2026</div><div class="tt2">Final Polish</div><div class="td2">Incorporate feedback, final proofread, format citations</div></div>
      <div class="tli"><div class="tld" style="background:#27ae60"></div><div class="td">May 31, 2026</div><div class="tt2">🏁 John Locke Deadline</div><div class="td2">Final submission — verify confirmation received</div></div>
    </div>
  </div>
  <div class="card">
    <div class="ct">📋 Essay Structure Template (2,000 words)</div>
    <table>
      <tr><th>Section</th><th>%</th><th>Words</th><th>Purpose</th></tr>
      <tr><td><b>Introduction</b></td><td>10%</td><td>~200</td><td>Hook, define key terms, state thesis, roadmap</td></tr>
      <tr><td><b>Background/Context</b></td><td>15%</td><td>~300</td><td>Historical context, current state of debate</td></tr>
      <tr><td><b>Main Argument 1</b></td><td>20%</td><td>~400</td><td>Claim + evidence + analysis + link to thesis</td></tr>
      <tr><td><b>Main Argument 2</b></td><td>20%</td><td>~400</td><td>Claim + evidence + analysis + link to thesis</td></tr>
      <tr><td><b>Counterarguments</b></td><td>20%</td><td>~400</td><td>Strongest objections + your responses</td></tr>
      <tr><td><b>Conclusion</b></td><td>15%</td><td>~300</td><td>Restate thesis, implications, memorable close</td></tr>
    </table>
  </div>
</div>
'''

if __name__ == "__main__":
    print(get_app_dashboard())
    print("Part 3 (Dashboard) ready")