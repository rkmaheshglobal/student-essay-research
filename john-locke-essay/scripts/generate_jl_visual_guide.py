#!/usr/bin/env python3
"""Generate the John Locke Institute Visual Guide HTML"""

import os

html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>John Locke Institute 2026 — Economics Essay Visual Guide</title>
<style>
:root{--navy:#0f1b35;--accent:#2563eb;--gold:#f59e0b;--green:#10b981;--red:#ef4444;--purple:#7c3aed;--light:#f8fafc;--card:#ffffff;--border:#e2e8f0;--text:#1e293b;--muted:#64748b;--q1:#0891b2;--q2:#7c3aed;--q3:#059669}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Georgia,serif;background:var(--light);color:var(--text);line-height:1.6}
.hero{background:linear-gradient(135deg,#0f1b35,#1a3a6b,#0f2d5e);color:#fff;padding:56px 32px 44px;text-align:center;position:relative;overflow:hidden}
.hero::before{content:\'\';position:absolute;inset:0;background:radial-gradient(circle at 30% 40%,rgba(37,99,235,.15),transparent 50%),radial-gradient(circle at 70% 60%,rgba(245,158,11,.1),transparent 50%);pointer-events:none}
.hero-badge{display:inline-block;background:rgba(245,158,11,.2);border:1px solid rgba(245,158,11,.5);color:#fbbf24;padding:5px 16px;border-radius:20px;font-size:11px;letter-spacing:2px;text-transform:uppercase;margin-bottom:18px;font-family:Arial,sans-serif}
.hero h1{font-size:clamp(24px,5vw,46px);font-weight:700;margin-bottom:10px}
.hero h1 span{color:#fbbf24}
.hero p{font-size:16px;opacity:.85;max-width:580px;margin:0 auto 32px;font-family:Arial,sans-serif}
.cg{display:flex;justify-content:center;gap:14px;flex-wrap:wrap}
.ci{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:12px;padding:12px 18px;min-width:105px;text-align:center}
.ci .num{font-size:30px;font-weight:700;color:#fbbf24;display:block;font-family:Arial,sans-serif}
.ci .lbl{font-size:10px;text-transform:uppercase;letter-spacing:1px;opacity:.7;font-family:Arial,sans-serif}
.nav-tabs{background:var(--navy);display:flex;overflow-x:auto;scrollbar-width:none;position:sticky;top:0;z-index:100;box-shadow:0 2px 10px rgba(0,0,0,.3)}
.nav-tabs::-webkit-scrollbar{display:none}
.nav-tab{padding:14px 20px;color:rgba(255,255,255,.6);cursor:pointer;white-space:nowrap;font-size:11px;font-family:Arial,sans-serif;font-weight:600;letter-spacing:.5px;border-bottom:3px solid transparent;transition:all .2s;text-transform:uppercase}
.nav-tab:hover{color:#fff;background:rgba(255,255,255,.05)}
.nav-tab.active{color:#fbbf24;border-bottom-color:#fbbf24}
.section{display:none;padding:32px;max-width:1200px;margin:0 auto}
.section.active{display:block}
.stitle{font-size:24px;font-weight:700;color:var(--navy);margin-bottom:5px}
.ssub{color:var(--muted);font-size:13px;margin-bottom:24px;font-family:Arial,sans-serif}
.card{background:var(--card);border-radius:14px;padding:22px;box-shadow:0 2px 12px rgba(0,0,0,.07);border:1px solid var(--border);margin-bottom:18px}
.ctitle{font-size:16px;font-weight:700;margin-bottom:10px;color:var(--navy)}
.sg{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px;margin-bottom:24px}
.sc{background:var(--card);border-radius:12px;padding:16px;text-align:center;border:1px solid var(--border)}
.si{font-size:24px;margin-bottom:5px}
.sv{font-size:19px;font-weight:700;color:var(--accent);font-family:Arial,sans-serif}
.sl{font-size:10px;color:var(--muted);text-transform:uppercase;letter-spacing:.5px;font-family:Arial,sans-serif}
.qs{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:16px;margin-bottom:24px}
.qc{border-radius:14px;padding:20px;cursor:pointer;transition:all .3s;border:2px solid transparent;position:relative;overflow:hidden}
.qc::before{content:\'\';position:absolute;top:0;left:0;right:0;height:4px}
.qc.q1{background:linear-gradient(135deg,#e0f2fe,#f0f9ff);border-color:#bae6fd}
.qc.q1::before{background:var(--q1)}
.qc.q2{background:linear-gradient(135deg,#ede9fe,#f5f3ff);border-color:#ddd6fe}
.qc.q2::before{background:var(--q2)}
.qc.q3{background:linear-gradient(135deg,#d1fae5,#ecfdf5);border-color:#a7f3d0}
.qc.q3::before{background:var(--q3)}
.qc:hover{transform:translateY(-3px);box-shadow:0 10px 28px rgba(0,0,0,.12)}
.qc.sel.q1{border-color:var(--q1);box-shadow:0 6px 20px rgba(8,145,178,.2)}
.qc.sel.q2{border-color:var(--q2);box-shadow:0 6px 20px rgba(124,58,237,.2)}
.qc.sel.q3{border-color:var(--q3);box-shadow:0 6px 20px rgba(5,150,105,.2)}
.qn{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:2px;margin-bottom:5px;font-family:Arial,sans-serif}
.qc.q1 .qn{color:var(--q1)}.qc.q2 .qn{color:var(--q2)}.qc.q3 .qn{color:var(--q3)}
.qc h3{font-size:15px;margin-bottom:7px;color:var(--navy);line-height:1.4}
.qtag{display:inline-block;padding:2px 9px;border-radius:20px;font-size:10px;font-family:Arial,sans-serif;font-weight:600;margin-bottom:8px}
.qc.q1 .qtag{background:rgba(8,145,178,.15);color:var(--q1)}
.qc.q2 .qtag{background:rgba(124,58,237,.15);color:var(--q2)}
.qc.q3 .qtag{background:rgba(5,150,105,.15);color:var(--q3)}
.qmeta{font-size:11px;color:var(--muted);font-family:Arial,sans-serif}
.qd{display:none}.qd.active{display:block}
.qdh{border-radius:14px;padding:22px;margin-bottom:18px;color:#fff}
.qdh.q1{background:linear-gradient(135deg,#0369a1,#0891b2)}
.qdh.q2{background:linear-gradient(135deg,#5b21b6,#7c3aed)}
.qdh.q3{background:linear-gradient(135deg,#065f46,#059669)}
.qdh .qt{font-size:10px;text-transform:uppercase;letter-spacing:2px;opacity:.8;font-family:Arial,sans-serif;margin-bottom:7px}
.qdh h2{font-size:20px;margin-bottom:10px;line-height:1.4}
.qdh .terms{font-size:12px;opacity:.85;font-family:Arial,sans-serif}
.qdh .terms span{background:rgba(255,255,255,.2);padding:2px 7px;border-radius:10px;margin-right:5px;display:inline-block;margin-bottom:3px}
.dg{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:18px}
@media(max-width:660px){.dg{grid-template-columns:1fr}}
.ds{border-radius:12px;padding:16px}
.ds.rs{background:#fef2f2;border:1px solid #fecaca}
.ds.gs{background:#f0fdf4;border:1px solid #bbf7d0}
.dh{display:flex;align-items:center;gap:7px;margin-bottom:10px;font-weight:700;font-size:12px;font-family:Arial,sans-serif}
.dh.r{color:#dc2626}.dh.g{color:#16a34a}
.dp{display:flex;gap:7px;margin-bottom:7px;font-size:11px;font-family:Arial,sans-serif}
.dp .ic{flex-shrink:0}
.dp strong{display:block;color:var(--text);font-size:11px}
.dp em{color:var(--muted);font-size:10px;font-style:normal}
.tg{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:12px;margin-bottom:18px}
.tc{border-radius:12px;padding:16px;border:1px solid var(--border);background:var(--card)}
.tl{font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;color:var(--accent);margin-bottom:7px;font-family:Arial,sans-serif}
.tt{font-size:12px;font-style:italic;color:var(--text);line-height:1.6;border-left:3px solid var(--accent);padding-left:10px}
.sf{display:flex;flex-direction:column;gap:0;margin-bottom:18px}
.ss{display:flex;gap:12px;align-items:flex-start;position:relative}
.ss:not(:last-child)::after{content:\'\';position:absolute;left:15px;top:32px;bottom:-5px;width:2px;background:var(--border)}
.sn{width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:12px;flex-shrink:0;font-family:Arial,sans-serif;z-index:1}
.sb{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:10px 14px;flex:1;margin-bottom:5px}
.stit{font-weight:700;font-size:12px;margin-bottom:2px;font-family:Arial,sans-serif}
.spct{font-size:9px;font-weight:600;padding:1px 6px;border-radius:10px;margin-left:5px;font-family:Arial,sans-serif}
.spts{font-size:11px;color:var(--muted);font-family:Arial,sans-serif;line-height:1.5}
.datagrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px;margin-bottom:18px}
.dc{background:var(--card);border-radius:10px;padding:12px;border:1px solid var(--border);border-left:4px solid var(--accent)}
.dstat{font-size:17px;font-weight:700;color:var(--accent);font-family:Arial,sans-serif;margin-bottom:2px}
.ddesc{font-size:11px;color:var(--text);margin-bottom:2px}
.dsrc{font-size:10px;color:var(--muted);font-family:Arial,sans-serif}
.sp{background:linear-gradient(135deg,#f8fafc,#f1f5f9);border-radius:12px;padding:20px 20px 20px 34px;border-left:4px solid var(--gold);font-style:italic;font-size:13px;line-height:1.8;color:var(--text);margin-bottom:18px;position:relative}
.sp::before{content:"\\201C";font-size:52px;color:var(--gold);opacity:.3;position:absolute;top:-6px;left:8px;font-family:Georgia,serif;line-height:1}
.al{list-style:none;margin-bottom:18px}
.al li{display:flex;gap:9px;padding:9px 12px;background:var(--card);border:1px solid var(--border);border-radius:8px;margin-bottom:7px;font-size:12px;font-family:Arial,sans-serif}
.al li .ai{font-size:14px;flex-shrink:0}
.al li strong{color:var(--navy)}
.timeline{position:relative;padding-left:32px;margin-bottom:24px}
.timeline::before{content:\'\';position:absolute;left:9px;top:0;bottom:0;width:3px;background:linear-gradient(to bottom,var(--accent),var(--gold),var(--green));border-radius:2px}
.ti{position:relative;margin-bottom:20px}
.td{position:absolute;left:-26px;top:4px;width:16px;height:16px;border-radius:50%;border:3px solid #fff;z-index:1}
.td.p1{background:var(--accent);box-shadow:0 0 0 2px var(--accent)}
.td.ms{background:var(--gold);box-shadow:0 0 0 2px var(--gold)}
.td.p2{background:var(--purple);box-shadow:0 0 0 2px var(--purple)}
.td.p3{background:var(--green);box-shadow:0 0 0 2px var(--green)}
.td.dl{background:var(--red);box-shadow:0 0 0 2px var(--red)}
.tdate{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--muted);margin-bottom:2px;font-family:Arial,sans-serif}
.ttitle{font-size:14px;font-weight:700;color:var(--navy);margin-bottom:4px}
.ttasks{font-size:11px;color:var(--muted);font-family:Arial,sans-serif;line-height:1.6}
.badge{display:inline-block;padding:2px 8px;border-radius:20px;font-size:10px;font-weight:600;font-family:Arial,sans-serif;margin-bottom:4px}
.bb{background:#dbeafe;color:#1d4ed8}.bg{background:#fef3c7;color:#92400e}.bp{background:#ede9fe;color:#5b21b6}.bgr{background:#d1fae5;color:#065f46}.br{background:#fee2e2;color:#991b1b}
.rg{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px;margin-bottom:24px}
.ri{background:var(--card);border-radius:12px;padding:16px;text-align:center;border:1px solid var(--border);position:relative;overflow:hidden}
.ri::after{content:\'\';position:absolute;bottom:0;left:0;right:0;height:4px}
.ri:nth-child(1)::after{background:#2563eb}.ri:nth-child(2)::after{background:#7c3aed}.ri:nth-child(3)::after{background:#0891b2}.ri:nth-child(4)::after{background:#059669}.ri:nth-child(5)::after{background:#f59e0b}
.rpct{font-size:36px;font-weight:700;font-family:Arial,sans-serif;line-height:1;margin-bottom:5px}
.ri:nth-child(1) .rpct{color:#2563eb}.ri:nth-child(2) .rpct{color:#7c3aed}.ri:nth-child(3) .rpct{color:#0891b2}.ri:nth-child(4) .rpct{color:#059669}.ri:nth-child(5) .rpct{color:#f59e0b}
.rname{font-size:12px;font-weight:700;color:var(--navy);margin-bottom:4px}
.rdesc{font-size:10px;color:var(--muted);font-family:Arial,sans-serif;line-height:1.4}
.rbar{height:5px;background:#e2e8f0;border-radius:3px;margin-top:8px;overflow:hidden}
.rfill{height:100%;border-radius:3px}
.ri:nth-child(1) .rfill{background:#2563eb;width:30%}.ri:nth-child(2) .rfill{background:#7c3aed;width:25%}.ri:nth-child(3) .rfill{background:#0891b2;width:20%}.ri:nth-child(4) .rfill{background:#059669;width:15%}.ri:nth-child(5) .rfill{background:#f59e0b;width:10%}
.readgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:12px;margin-bottom:18px}
.bk{background:var(--card);border-radius:12px;padding:16px;border:1px solid var(--border);display:flex;gap:10px;align-items:flex-start}
.bki{width:38px;height:48px;border-radius:4px;display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0}
.bkt{font-size:12px;font-weight:700;color:var(--navy);margin-bottom:2px}
.bka{font-size:10px;color:var(--muted);font-family:Arial,sans-serif;margin-bottom:4px}
.bktag{font-size:9px;padding:2px 6px;border-radius:10px;font-family:Arial,sans-serif;font-weight:600}
.tipgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px;margin-bottom:18px}
.tip{background:var(--card);border-radius:12px;padding:16px;border:1px solid var(--border);display:flex;gap:10px}
.tipn{width:28px;height:28px;border-radius:50%;background:var(--navy);color:#fff;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;flex-shrink:0;font-family:Arial,sans-serif}
.tipt{font-size:12px;font-weight:700;color:var(--navy);margin-bottom:2px}
.tipd{font-size:11px;color:var(--muted);font-family:Arial,sans-serif;line-height:1.5}
.themegrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:12px;margin-bottom:18px}
.thm{background:var(--card);border-radius:12px;padding:16px;border:1px solid var(--border);text-align:center}
.thmi{font-size:26px;margin-bottom:7px}
.thmt{font-size:12px;font-weight:700;color:var(--navy);margin-bottom:4px}
.thmd{font-size:10px;color:var(--muted);font-family:Arial,sans-serif;line-height:1.5}
.thmq{display:flex;justify-content:center;gap:3px;margin-top:7px}
.thmqb{width:18px;height:18px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:8px;font-weight:700;font-family:Arial,sans-serif;color:#fff}
.thmqb.q1{background:var(--q1)}.thmqb.q2{background:var(--q2)}.thmqb.q3{background:var(--q3)}
.cw{overflow-x:auto;margin-bottom:18px}
.ct{width:100%;border-collapse:collapse;font-family:Arial,sans-serif;font-size:11px}
.ct th{background:var(--navy);color:#fff;padding:10px 12px;text-align:left;font-size:10px;text-transform:uppercase;letter-spacing:.5px}
.ct td{padding:9px 12px;border-bottom:1px solid var(--border)}
.ct tr:nth-child(even) td{background:#f8fafc}
.ct tr:hover td{background:#f1f5f9}
.alert{border-radius:10px;padding:12px 16px;margin-bottom:14px;font-family:Arial,sans-serif;font-size:12px;display:flex;gap:9px;align-items:flex-start}
.alert.info{background:#eff6ff;border:1px solid #bfdbfe;color:#1e40af}
.alert.warn{background:#fffbeb;border:1px solid #fde68a;color:#92400e}
.alert.ok{background:#f0fdf4;border:1px solid #bbf7d0;color:#065f46}
.ai2{font-size:14px;flex-shrink:0}
.sh{font-size:15px;font-weight:700;color:var(--navy);margin:20px 0 12px;display:flex;align-items:center;gap:8px}
.sh::after{content:\'\';flex:1;height:1px;background:var(--border)}
.footer{background:var(--navy);color:rgba(255,255,255,.6);text-align:center;padding:22px;font-family:Arial,sans-serif;font-size:11px;margin-top:36px}
.footer a{color:#fbbf24;text-decoration:none}
hr.div{border:none;border-top:1px solid var(--border);margin:20px 0}
</style>
</head>
<body>

<div class="hero">
  <div class="hero-badge">&#127891; Student Visual Guide</div>
  <h1>John Locke Institute<br><span>Economics Essay 2026</span></h1>
  <p>Your complete visual companion — questions, arguments, essay structure, and winning strategy.</p>
  <div class="cg">
    <div class="ci"><span class="num" id="d1">18</span><span class="lbl">Days to Questions</span></div>
    <div class="ci"><span class="num" id="d2">57</span><span class="lbl">Days to Secondary</span></div>
    <div class="ci"><span class="num" id="d3">78</span><span class="lbl">Days to Deadline</span></div>
    <div class="ci"><span class="num">~2,000</span><span class="lbl">Word Limit</span></div>
  </div>
</div>

<div class="nav-tabs">
  <div class="nav-tab active" onclick="show(\'overview\')">&#127919; Overview</div>
  <div class="nav-tab" onclick="show(\'q1\')">&#128178; Q1: Cashless</div>
  <div class="nav-tab" onclick="show(\'q2\')">&#128200; Q2: Pricing</div>
  <div class="nav-tab" onclick="show(\'q3\')">&#128188; Q3: Bezos</div>
  <div class="nav-tab" onclick="show(\'timeline\')">&#128197; Timeline</div>
  <div class="nav-tab" onclick="show(\'scoring\')">&#127942; Scoring</div>
  <div class="nav-tab" onclick="show(\'resources\')">&#128218; Resources</div>
</div>

<!-- OVERVIEW -->
<div id="overview" class="section active">
  <div class="stitle">&#127919; Competition Overview</div>
  <div class="ssub">John Locke Institute Essay Competition 2026 — Economics Category</div>

  <div class="sg">
    <div class="sc"><div class="si">&#127942;</div><div class="sv">JLI 2026</div><div class="sl">Competition</div></div>
    <div class="sc"><div class="si">&#128197;</div><div class="sv">Apr 1</div><div class="sl">Questions Released</div></div>
    <div class="sc"><div class="si">&#128203;</div><div class="sv">May 10</div><div class="sl">Secondary Deadline</div></div>
    <div class="sc"><div class="si">&#127937;</div><div class="sv">May 31</div><div class="sl">Final Deadline</div></div>
    <div class="sc"><div class="si">&#128221;</div><div class="sv">~2,000</div><div class="sl">Word Limit</div></div>
    <div class="sc"><div class="si">&#128218;</div><div class="sv">3</div><div class="sl">Questions to Choose From</div></div>
  </div>

  <div class="sh">&#127775; The 3 Official Questions</div>
  <div class="qs">
    <div class="qc q1" onclick="show(\'q1\')">
      <div class="qn">Question 1 &bull; Evaluation</div>
      <div class="qtag">&#128178; Monetary Economics</div>
      <h3>Should we fear a cashless society?</h3>
      <div class="qmeta">Privacy &bull; Financial Inclusion &bull; Monetary Freedom &bull; Surveillance</div>
    </div>
    <div class="qc q2" onclick="show(\'q2\')">
      <div class="qn">Question 2 &bull; Effects Analysis</div>
      <div class="qtag">&#128200; Behavioural Economics</div>
      <h3>Technology now allows personalised pricing. If this came to be widely used, what effects should we expect?</h3>
      <div class="qmeta">Price Discrimination &bull; Efficiency &bull; Fairness &bull; Market Power</div>
    </div>
    <div class="qc q3" onclick="show(\'q3\')">
      <div class="qn">Question 3 &bull; Distributional Analysis</div>
      <div class="qtag">&#128188; Labour Economics</div>
      <h3>Did Jeff Bezos get rich at the expense of his customers, his employees, neither or both?</h3>
      <div class="qmeta">Wealth Creation &bull; Labour &bull; Consumer Surplus &bull; Inequality</div>
    </div>
  </div>

  <div class="sh">&#9878; Cross-Cutting Themes (appear in ALL questions)</div>
  <div class="themegrid">
    <div class="thm"><div class="thmi">&#9889;</div><div class="thmt">Technology &amp; Power</div><div class="thmd">All three questions involve technology shifting power between groups</div><div class="thmq"><span class="thmqb q1">1</span><span class="thmqb q2">2</span><span class="thmqb q3">3</span></div></div>
    <div class="thm"><div class="thmi">&#9878;</div><div class="thmt">Efficiency vs. Fairness</div><div class="thmd">The classic economic trade-off appears in each question</div><div class="thmq"><span class="thmqb q1">1</span><span class="thmqb q2">2</span><span class="thmqb q3">3</span></div></div>
    <div class="thm"><div class="thmi">&#128100;</div><div class="thmt">Who Bears the Costs?</div><div class="thmd">Distributional analysis is central to all three questions</div><div class="thmq"><span class="thmqb q1">1</span><span class="thmqb q2">2</span><span class="thmqb q3">3</span></div></div>
    <div class="thm"><div class="thmi">&#127963;</div><div class="thmt">Role of Institutions</div><div class="thmd">Regulation, law, and policy shape outcomes in each case</div><div class="thmq"><span class="thmqb q1">1</span><span class="thmqb q2">2</span><span class="thmqb q3">3</span></div></div>
    <div class="thm"><div class="thmi">&#128065;</div><div class="thmt">Visibility of Harm</div><div class="thmd">Some costs are visible (injuries), others hidden (privacy loss)</div><div class="thmq"><span class="thmqb q1">1</span><span class="thmqb q2">2</span><span class="thmqb q3">3</span></div></div>
  </div>

  <div class="sh">&#128202; Question Comparison — Which to Choose?</div>
  <div class="cw">
    <table class="ct">
      <tr><th>Factor</th><th>Q1: Cashless Society</th><th>Q2