#!/usr/bin/env python3
"""Generate the JLI Essay Prep 2026 web application."""
import os, sys

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'outputs', 'john-locke-essay', 'essay-prep-app.html')
os.makedirs(os.path.dirname(out_path), exist_ok=True)

CSS = """<style>
:root{--p:#1a3a5c;--a:#c8a84b;--al:#f0e6c8;--bg:#f5f7fa;--c:#fff;--t:#1e2d3d;--m:#6b7c93;--b:#e2e8f0;--ok:#2d7d46;--w:#b45309;--bad:#c0392b;--sw:250px}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Georgia,serif;background:var(--bg);color:var(--t);display:flex;min-height:100vh}
nav{width:var(--sw);background:var(--p);position:fixed;top:0;left:0;height:100vh;overflow-y:auto;z-index:100}
.sh{padding:20px 16px 14px;border-bottom:1px solid rgba(255,255,255,.1)}
.sh h1{font-size:14px;font-weight:700;color:var(--a)}
.sh p{font-size:11px;color:rgba(255,255,255,.45);font-family:sans-serif;margin-top:3px}
.nl{font-size:10px;text-transform:uppercase;letter-spacing:1px;color:rgba(255,255,255,.3);padding:10px 16px 3px;font-family:sans-serif}
.ni{display:flex;align-items:center;gap:8px;padding:9px 16px;cursor:pointer;font-size:12px;color:rgba(255,255,255,.75);font-family:sans-serif;border:none;background:none;width:100%;text-align:left;transition:all .15s}
.ni:hover{background:rgba(255,255,255,.08);color:#fff}
.ni.active{background:var(--a);color:var(--p);font-weight:700}
main{margin-left:var(--sw);flex:1}
.pg{display:none;padding:28px;max-width:1050px}
.pg.on{display:block}
.ph h2{font-size:24px;color:var(--p);margin-bottom:6px}
.ph p{color:var(--m);font-family:sans-serif;font-size:13px;margin-bottom:24px}
.card{background:var(--c);border-radius:10px;padding:20px;border:1px solid var(--b);margin-bottom:18px}
.ct{font-size:15px;font-weight:700;color:var(--p);margin-bottom:12px}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:18px}
.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-bottom:20px}
.cc{background:var(--p);color:#fff;border-radius:10px;padding:18px;text-align:center}
.cc.r{background:var(--bad)}.cc.o{background:var(--w)}
.cd{font-size:38px;font-weight:700;color:var(--a);line-height:1}
.cl2{font-size:11px;color:rgba(255,255,255,.65);margin-top:5px;font-family:sans-serif}
.cdt{font-size:12px;color:rgba(255,255,255,.85);margin-top:3px;font-family:sans-serif}
.tabs{display:flex;gap:3px;border-bottom:2px solid var(--b);margin-bottom:16px;flex-wrap:wrap}
.tab{padding:7px 14px;font-size:12px;cursor:pointer;border-radius:5px 5px 0 0;font-family:sans-serif;border:none;background:none;color:var(--m)}
.tab.on{background:var(--p);color:#fff}
.tc{display:none}.tc.on{display:block}
.thesis{background:var(--al);border-left:4px solid var(--a);border-radius:0 8px 8px 0;padding:14px;margin-bottom:10px}
.thl{font-size:10px;text-transform:uppercase;letter-spacing:1px;color:var(--w);font-family:sans-serif;font-weight:700;margin-bottom:5px}
.tht{font-style:italic;color:var(--p);line-height:1.6;font-size:13px}
table{width:100%;border-collapse:collapse;font-size:12px;font-family:sans-serif}
th{background:var(--p);color:#fff;padding:9px 11px;text-align:left;font-size:11px}
td{padding:9px 11px;border-bottom:1px solid var(--b);vertical-align:top;line-height:1.5}
tr:hover td{background:#f8fafc}
.badge{display:inline-block;padding:2px 8px;border-radius:20px;font-size:10px;font-family:sans-serif;font-weight:700}
.bb{background:#dbeafe;color:#1e40af}.bg{background:#dcfce7;color:#166534}
.by{background:#fef9c3;color:#854d0e}.br{background:#fee2e2;color:#991b1b}
.pb{background:var(--b);border-radius:10px;height:7px;overflow:hidden;margin:6px 0}
.pf{background:var(--a);height:100%;border-radius:10px}
.pro{background:#f0fdf4;border:1px solid #86efac;border-radius:8px;padding:14px}
.con{background:#fef2f2;border:1px solid #fca5a5;border-radius:8px;padding:14px}
.pro h4,.con h4{font-size:12px;font-family:sans-serif;margin-bottom:7px}
.pro h4{color:var(--ok)}.con h4{color:var(--bad)}
ul.pts{padding-left:15px}.pts li{font-size:12px;font-family:sans-serif;line-height:1.7}
.tlw{position:relative;padding-left:22px}
.tlw::before{content:'';position:absolute;left:7px;top:0;bottom:0;width:2px;background:var(--b)}
.tli{position:relative;margin-bottom:18px}
.tld{position:absolute;left:-19px;top:3px;width:11px;height:11px;border-radius:50%;background:var(--a);border:2px solid var(--p)}
.tdate{font-size:10px;color:var(--m);font-family:sans-serif;font-weight:700;text-transform:uppercase;letter-spacing:.5px}
.ttitle{font-size:14px;font-weight:700;color:var(--p);margin:2px 0}
.tdesc{font-size:12px;color:var(--m);font-family:sans-serif}
.cl-list{list-style:none}
.cl-list li{display:flex;align-items:flex-start;gap:9px;padding:7px 0;border-bottom:1px solid var(--b);font-family:sans-serif;font-size:13px}
.cl-list input[type=checkbox]{width:16px;height:16px;cursor:pointer;flex-shrink:0;margin-top:2px;accent-color:var(--p)}
.cl-list label{cursor:pointer;line-height:1.4}
.cl-list input:checked+label{text-decoration:line-through;color:var(--m)}
.bq{border-left:4px solid var(--a);padding:11px 14px;background:var(--al);border-radius:0 7px 7px 0;font-style:italic;margin:10px 0;line-height:1.6;font-size:13px}
.org{background:var(--c);border-radius:9px;border:1px solid var(--b);padding:16px;margin-bottom:14px}
.oname{font-size:15px;font-weight:700;color:var(--p)}
.ourl{font-size:11px;color:var(--a);font-family:sans-serif;margin:2px 0 7px}
.odesc{font-size:12px;color:var(--m);font-family:sans-serif;line-height:1.5}
.book{display:flex;gap:10px;padding:10px 0;border-bottom:1px solid var(--b);align-items:flex-start}
.bicon{font-size:22px;flex-shrink:0}
.btitle{font-size:13px;font-weight:700;color:var(--p)}
.bauth,.bwhy{font-size:11px;color:var(--m);font-family:sans-serif}
.bwhy{font-style:italic;margin-top:3px}
</style>"""

JS = """<script>
function go(id){
  document.querySelectorAll('.pg').forEach(p=>p.classList.remove('on'));
  document.querySelectorAll('.ni').forEach(n=>n.classList.remove('active'));
  document.getElementById('pg-'+id).classList.add('on');
  event.currentTarget.classList.add('active');
}
function stab(btn,id){
  var pg=btn.closest('.pg');
  pg.querySelectorAll('.tab').forEach(t=>t.classList.remove('on'));
  pg.querySelectorAll('.tc').forEach(t=>t.classList.remove('on'));
  btn.classList.add('on');
  document.getElementById(id).classList.add('on');
}
function days(d){var n=new Date(),t=new Date(d);return Math.ceil((t-n)/86400000);}
window.onload=function(){
  document.getElementById('dq').textContent=Math.max(0,days('2026-04-01'));
  document.getElementById('ds').textContent=Math.max(0,days('2026-05-10'));
  document.getElementById('dd').textContent=Math.max(0,days('2026-05-31'));
  var saved=JSON.parse(localStorage.getItem('jli-checks')||'{}');
  document.querySelectorAll('.cl-list input').forEach(function(cb){
    if(saved[cb.id])cb.checked=true;
    cb.addEventListener('change',function(){
      saved[cb.id]=cb.checked;
      localStorage.setItem('jli-checks',JSON.stringify(saved));
    });
  });
};
</script>"""

NAV = """<nav>
  <div class="sh"><h1>JLI Essay Prep 2026</h1><p>Economics Competition</p></div>
  <div class="nl">Overview</div>
  <button class="ni active" onclick="go('dash')">&#127968; Dashboard</button>
  <button class="ni" onclick="go('time')">&#128197; Timeline &amp; Plan</button>
  <div class="nl">2026 Questions</div>
  <button class="ni" onclick="go('q1')">&#128179; Q1: Cashless Society</button>
  <button class="ni" onclick="go('q2')">&#128176; Q2: Personalised Pricing</button>
  <button class="ni" onclick="go('q3')">&#128230; Q3: Jeff Bezos</button>
  <div class="nl">Research</div>
  <button class="ni" onclick="go('fw')">&#129504; Argument Frameworks</button>
  <button class="ni" onclick="go('past')">&#128218; Past Questions</button>
  <button class="ni" onclick="go('read')">&#128214; Reading List</button>
  <div class="nl">Support</div>
  <button class="ni" onclick="go('ment')">&#127891; Mentorship Orgs</button>
  <button class="ni" onclick="go('chk')">&#9989; My Checklist</button>
</nav>"""

DASH = """<div id="pg-dash" class="pg on">
<div class="ph"><h2>&#128202; Competition Dashboard</h2><p>John Locke Institute Essay Competition 2026 &mdash; Economics</p></div>
<div class="g3">
  <div class="cc r"><div class="cd" id="dq">-</div><div class="cl2">Days Until Questions Open</div><div class="cdt">April 1, 2026</div></div>
  <div class="cc o"><div class="cd" id="ds">-</div><div class="cl2">Days to Secondary Deadline</div><div class="cdt">May 10, 2026</div></div>
  <div class="cc"><div class="cd" id="dd">-</div><div class="cl2">Days to Final Deadline</div><div class="cdt">May 31, 2026</div></div>
</div>
<div class="g2">
  <div class="card"><div class="ct">&#127942; Official 2026 Questions</div>
    <div style="font-family:sans-serif;font-size:13px;line-height:1.9">
      <div style="padding:7px 0;border-bottom:1px solid var(--b)"><span class="badge bb">Q1</span> &nbsp;Should we fear a cashless society?</div>
      <div style="padding:7px 0;border-bottom:1px solid var(--b)"><span class="badge by">Q2</span> &nbsp;Technology now allows personalised pricing. What effects should we expect?</div>
      <div style="padding:7px 0"><span class="badge br">Q3</span> &nbsp;Did Jeff Bezos get rich at the expense of his customers, his employees, neither or both?</div>
    </div>
  </div>
  <div class="card"><div class="ct">&#128273; What Judges Look For</div>
    <div style="font-family:sans-serif;font-size:12px">
      <div style="margin-bottom:9px"><div style="display:flex;justify-content:space-between;margin-bottom:3px"><span>Original Thinking</span><b style="color:var(--a)">30%</b></div><div class="pb"><div class="pf" style="width:30%"></div></div></div>
      <div style="margin-bottom:9px"><div style="display:flex;justify-content:space-between;margin-bottom:3px"><span>Clear Argumentation</span><b style="color:var(--a)">25%</b></div><div class="pb"><div class="pf" style="width:25%"></div></div></div>
      <div style="margin-bottom:9px"><div style="display:flex;justify-content:space-between;margin-bottom:3px"><span>Counterargument Engagement</span><b style="color:var(--a)">20%</b></div><div class="pb"><div class="pf" style="width:20%"></div></div></div>
      <div style="margin-bottom:9px"><div style="display:flex;justify-content:space-between;margin-bottom:3px"><span>Evidence-Based Reasoning</span><b style="color:var(--a)">15%</b></div><div class="pb"><div class="pf" style="width:15%"></div></div></div>
      <div><div style="display:flex;justify-content:space-between;margin-bottom:3px"><span>Writing Quality</span><b style="color:var(--a)">10%</b></div><div class="pb"><div class="pf" style="width:10%"></div></div></div>
    </div>
  </div>
</div>
<div class="card"><div class="ct">&#128202; Question Selection Guide</div>
  <table><tr><th>Factor</th><th>Q1: Cashless Society</th><th>Q2: Personalised Pricing</th><th>Q3: Jeff Bezos</th></tr>
  <tr><td><b>Originality Potential</b></td><td><span class="badge by">Medium</span></td><td><span class="badge bg">High &#11088;</span></td><td><span class="badge by">Medium</span></td></tr>
  <tr><td><b>Risk of Cliche</b></td><td><span class="badge by">Medium</span></td><td><span class="badge bg">Low &#11088;</span></td><td><span class="badge br">High</span></td></tr>
  <tr><td><b>Data Availability</b></td><td><span class="badge bg">High</span></td><td><span class="badge by">Medium</span></td><td><span class="badge bg">High</span></td></tr>
  <tr><td><b>Theory Required</b></td><td>Monetary economics</td><td>Price discrimination</td><td>Labor + consumer surplus</td></tr></table>
</div>
<div class="card"><div class="ct">&#9889; Quick Start</div>
  <div class="g2">
    <div class="pro"><h4>&#9989; Free Actions (Do Today)</h4><ul class="pts"><li>Read Q1, Q2, Q3 deep dives in this app</li><li>Email your economics teacher for mentorship</li><li>Sign up for Marginal Revolution University (free)</li><li>Read past JLI winning essays on their website</li></ul></div>
    <div class="con"><h4>&#128204; This Week</h4><ul class="pts"><li>Choose your top 1-2 questions to focus on</li><li>Start reading "Good Economics for Hard Times"</li><li>Contact Polygence or Lumiere for mentorship</li><li>Build your sources document</li></ul></div>
  </div>
</div>
</div>"""

TIME = """<div id="pg-time" class="pg">
<div class="ph"><h2>&#128197; Timeline &amp; Action Plan</h2><p>Week-by-week execution plan for the 2026 competition</p></div>
<div class="card"><div class="ct">&#128197; Key Dates</div>
  <div class="tlw">
    <div class="tli"><div class="tld" style="background:#e74c3c"></div><div class="tdate">March 13-31, 2026</div><div class="ttitle">Phase 1: Preparation</div><div class="tdesc">Foundation building, deep research, question analysis prep</div></div>
    <div class="tli"><div class="tld" style="background:#f39c12"></div><div class="tdate">April 1, 2026</div><div class="ttitle">&#127919; Questions Released</div><div class="tdesc">Official questions published - analyze immediately, choose your question</div></div>
    <div class="tli"><div class="tld"></div><div class="tdate">April 3-9, 2026</div><div class="ttitle">Thesis &amp; Outline</div><div class="tdesc">Develop clear thesis, create detailed outline, get mentor feedback</div></div>
    <div class="tli"><div class="tld"></div><div class="tdate">April 10-16, 2026</div><div class="ttitle">First Draft</div><div class="tdesc">Complete rough first draft (~2,000 words)</div></div>
    <div class="tli"><div class="tld"></div><div class="tdate">April 17-30, 2026</div><div class="ttitle">Revision Rounds 1 &amp; 2</div><div class="tdesc">Strengthen arguments, address counterarguments, incorporate feedback</div></div>
    <div class="tli"><div class="tld" style="background:#f39c12"></div><div class="tdate">May 10, 2026</div><div class="ttitle">&#128221; Secondary Competition Deadline</div><div class="tdesc">Submit to secondary competition for early feedback</div></div>
    <div class="tli"><div class="tld"></div><div class="tdate">May 11-28, 2026</div><div class="ttitle">Final Polish</div><div class="tdesc">Incorporate feedback, final proofread, format citations</div></div>
    <div class="tli"><div class="tld" style="background:#27ae60"></div><div class="tdate">May 31, 2026</div><div class="ttitle">&#127937; John Locke Deadline</div><div class="tdesc">Final submission - verify confirmation received</div></div>
  </div>
</div>
<div class="card"><div class="ct">&#128203; Essay Structure Template (2,000 words)</div>
  <table><tr><th>Section</th><th>%</th><th>Words</th><th>Purpose</th></tr>
  <tr><td><b>Introduction</b></td><td>10%</td><td>~200</td><td>Hook, define key terms, state thesis, roadmap</td></tr>
  <tr><td><b>Background/Context</b></td><td>15%</td><td>~300</td><td>Historical context, current state of debate</td></tr>
  <tr><td><b>Main Argument 1</b></td><td>20%</td><td>~400</td><td>Claim + evidence + analysis + link to thesis</td></tr>
  <tr><td><b>Main Argument 2</b></td><td>20%</td><td>~400</td><td>Claim + evidence + analysis + link to thesis</td></tr>
  <tr><td><b>Counterarguments</b></td><td>20%</td><td>~400</td><td>Strongest objections + your responses</td></tr>
  <tr><td><b>Conclusion</b></td><td>15%</td><td>~300</td><td>Restate thesis, implications, memorable close</td></tr></table>
</div>
</div>"""

Q1 = """<div id="pg-q1" class="pg">
<div class="ph"><h2>&#128179; Q1: Should we fear a cashless society?</h2><p>Type: Evaluation/Fear Assessment - Theme: Monetary policy, Privacy, Financial inclusion</p></div>
<div class="tabs">
  <button class="tab on" onclick="stab(this,'q1a')">Overview</button>
  <button class="tab" onclick="stab(this,'q1b')">The Debate</button>
  <button class="tab" onclick="stab(this,'q1c')">Thesis Options</button>
  <button class="tab" onclick="stab(this,'q1d')">Key Data</button>
  <button class="tab" onclick="stab(this,'q1e')">Case Studies</button>
</div>
<div id="q1a" class="tc on">
  <div class="card"><div class="ct">&#128269; What the Question is Really Asking</div>
    <p style="font-family:sans-serif;font-size:13px;line-height:1.8;margin-bottom:14px">The word <b>"fear"</b> implies a rational assessment of risk serious enough to warrant action - not mere discomfort or nostalgia for cash. Distinguish: irrational fear (technophobia) vs. rational precaution vs. structural fear (systemic risks individuals cannot mitigate).</p>
    <div class="g2">
      <div><b style="font-family:sans-serif;font-size:12px">Key Terms to Define:</b><ul class="pts" style="margin-top:7px"><li><b>Fear</b> - rational precaution vs. irrational technophobia</li><li><b>Cashless society</b> - cash-light? near-cashless? fully cashless?</li><li><b>Society</b> - developed vs. developing countries differ enormously</li></ul></div>
      <div><b style="font-family:sans-serif;font-size:12px">Spectrum of Cashlessness:</b><ul class="pts" style="margin-top:7px"><li>Cash-light: UK, Australia</li><li>Near-cashless: Sweden (98% digital)</li><li>Fully cashless: No country has achieved this</li><li>Programmable: China's e-CNY experiments</li></ul></div>
    </div>
  </div>
  <div class="card"><div class="ct">&#9997; Sample Opening Paragraph</div>
    <div class="bq">"In 2016, the Indian government invalidated 86% of the country's currency overnight, forcing a billion people into a digital payment system many had never used. The chaos that followed - bank queues, business failures, and over 100 deaths - revealed what a cashless transition looks like when imposed rather than chosen. Sweden, by contrast, has achieved near-total cashlessness through gradual adoption, with robust safeguards for the elderly and unconnected. These two paths illuminate the real question: not whether to fear cashlessness, but whether to fear the particular cashless society being built."</div>
  </div>
</div>
<div id="q1b" class="tc">
  <div class="card"><div class="ct">&#9878; The Core Debate</div>
    <div class="g2">
      <div class="pro"><h4>&#9989; Arguments AGAINST Fear</h4><ul class="pts"><li><b>Efficiency:</b> Cash handling costs 50B EUR/year in Europe (ECB)</li><li><b>Crime reduction:</b> Sweden robberies fell 70% as cash declined</li><li><b>Financial inclusion:</b> M-Pesa lifted 194,000 Kenyan households out of poverty (Suri &amp; Jack, 2016)</li><li><b>Monetary policy:</b> Removes zero lower bound constraint on interest rates</li></ul></div>
      <div class="con"><h4>&#9888; Arguments FOR Fear</h4><ul class="pts"><li><b>Privacy:</b> Every transaction traceable; surveillance capitalism (Zuboff, 2019)</li><li><b>Exclusion:</b> 1.4B unbanked globally; elderly, homeless excluded</li><li><b>Fragility:</b> 302 UK payment outages in 4 years (FCA)</li><li><b>Programmable money:</b> China's e-CNY has expiry dates; Canada froze protesters' accounts (2022)</li><li><b>Private power:</b> Visa + Mastercard control 80%+ of transactions</li></ul></div>
    </div>
  </div>
  <div class="card"><div class="ct">&#128260; Counterarguments &amp; Responses</div>
    <table><tr><th>Counterargument</th><th>Your Response</th></tr>
    <tr><td>"Cash enables crime and tax evasion"</td><td>Criminals adapt to crypto/hawala. The cost of eliminating cash (privacy, exclusion) exceeds the benefit. Most cash users are not criminals.</td></tr>
    <tr><td>"M-Pesa shows digital payments are more inclusive"</td><td>Context-dependent. Works in Kenya because mobile penetration &gt; banking penetration. In developed countries, the unbanked are often also digitally excluded.</td></tr>
    <tr><td>"Sweden shows cashlessness can work well"</td><td>Sweden is the best-case scenario - and even Sweden reversed course. Riksbank now requires cash services; government recommends holding cash for emergencies.</td></tr>
    <tr><td>"