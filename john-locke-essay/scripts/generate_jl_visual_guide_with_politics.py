#!/usr/bin/env python3
"""
Generate the John Locke Institute Visual Guide HTML with both Economics and Politics content.
This script merges all parts to create a comprehensive visual guide without truncation.
"""

import os
import sys

# Add the parts directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'parts'))

# Import all politics parts
from jl_politics_part1 import get_politics_overview
from jl_politics_part2 import get_politics_q1
from jl_politics_part3 import get_politics_q2
from jl_politics_part4 import get_politics_q3
from jl_politics_part5 import get_politics_deep_dive
from jl_politics_part6 import get_politics_past_questions

def get_html_head():
    """Return the HTML head section with styles"""
    return '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>John Locke Institute 2026 - Economics & Politics Visual Guide</title>
<style>
:root{--navy:#1a237e;--accent:#ff6f00;--gold:#ffa000;--green:#10b981;--red:#ef4444;--purple:#7c3aed;--light:#f8fafc;--card:#fff;--border:#e2e8f0;--text:#1e293b;--muted:#64748b;--q1:#0891b2;--q2:#7c3aed;--q3:#059669}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Poppins','Segoe UI',sans-serif;background:#f5f7ff;color:#2d3748;line-height:1.6}
.hero{background:linear-gradient(135deg,#1a237e,#311b92);color:#fff;padding:56px 32px 44px;text-align:center}
.hbadge{display:inline-block;background:rgba(255,111,0,.2);border:1px solid rgba(255,111,0,.5);color:#ffcc80;padding:5px 16px;border-radius:20px;font-size:11px;letter-spacing:2px;text-transform:uppercase;margin-bottom:18px;font-family:Arial,sans-serif}
.hero h1{font-size:clamp(24px,5vw,46px);font-weight:700;margin-bottom:10px}
.hero h1 span{color:#ffcc02}
.hero p{font-size:16px;opacity:.85;max-width:580px;margin:0 auto 32px;font-family:Arial,sans-serif}
.cg{display:flex;justify-content:center;gap:14px;flex-wrap:wrap}
.ci{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:12px;padding:12px 18px;min-width:105px;text-align:center}
.ci .num{font-size:30px;font-weight:700;color:#ffcc02;display:block;font-family:Arial,sans-serif}
.ci .lbl{font-size:10px;text-transform:uppercase;letter-spacing:1px;opacity:.7;font-family:Arial,sans-serif}
.nav-tabs{background:#1a237e;display:flex;overflow-x:auto;scrollbar-width:none;position:sticky;top:0;z-index:100;box-shadow:0 2px 10px rgba(0,0,0,.3)}
.nav-tabs::-webkit-scrollbar{display:none}
.nav-tab{padding:14px 20px;color:rgba(255,255,255,.6);cursor:pointer;white-space:nowrap;font-size:11px;font-family:Arial,sans-serif;font-weight:600;letter-spacing:.5px;border-bottom:3px solid transparent;transition:all .2s;text-transform:uppercase}
.nav-tab:hover{color:#fff;background:rgba(255,255,255,.05)}
.nav-tab.active{color:#ff6f00;border-bottom-color:#ff6f00}
.nav-tab.pol{color:rgba(255,255,255,.6)}
.nav-tab.pol.active{color:#10b981;border-bottom-color:#10b981}
.section{display:none;padding:32px;max-width:1200px;margin:0 auto}
.section.active{display:block}
.stitle{font-size:24px;font-weight:700;color:#1a237e;margin-bottom:5px}
.ssub{color:var(--muted);font-size:13px;margin-bottom:24px;font-family:Arial,sans-serif}
.card{background:var(--card);border-radius:14px;padding:22px;box-shadow:0 2px 12px rgba(0,0,0,.07);border:1px solid var(--border);margin-bottom:18px}
.ctitle{font-size:16px;font-weight:700;margin-bottom:10px;color:#1a237e}
.sg{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin-bottom:24px}
.sc{background:var(--card);border-radius:12px;padding:16px;text-align:center;border:1px solid var(--border)}
.si{font-size:24px;margin-bottom:5px}
.sv{font-size:19px;font-weight:700;color:#ff6f00;font-family:Arial,sans-serif}
.sl{font-size:10px;color:var(--muted);text-transform:uppercase;letter-spacing:.5px;font-family:Arial,sans-serif}
.qs{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:16px;margin-bottom:24px}
.qc{border-radius:14px;padding:20px;cursor:pointer;transition:all .3s;border:2px solid transparent;position:relative;overflow:hidden}
.qc::before{content:'';position:absolute;top:0;left:0;right:0;height:4px}
.qc.q1{background:linear-gradient(135deg,#e0f2fe,#f0f9ff);border-color:#bae6fd}
.qc.q1::before{background:var(--q1)}
.qc.q2{background:linear-gradient(135deg,#ede9fe,#f5f3ff);border-color:#ddd6fe}
.qc.q2::before{background:var(--q2)}
.qc.q3{background:linear-gradient(135deg,#d1fae5,#ecfdf5);border-color:#a7f3d0}
.qc.q3::before{background:var(--q3)}
.qc:hover{transform:translateY(-3px);box-shadow:0 10px 28px rgba(0,0,0,.12)}
.qn{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:2px;margin-bottom:5px;font-family:Arial,sans-serif}
.qc.q1 .qn{color:var(--q1)}.qc.q2 .qn{color:var(--q2)}.qc.q3 .qn{color:var(--q3)}
.qc h3{font-size:15px;margin-bottom:7px;color:var(--navy);line-height:1.4}
.qtag{display:inline-block;padding:2px 9px;border-radius:20px;font-size:10px;font-family:Arial,sans-serif;font-weight:600;margin-bottom:8px}
.qc.q1 .qtag{background:rgba(8,145,178,.15);color:var(--q1)}
.qc.q2 .qtag{background:rgba(124,58,237,.15);color:var(--q2)}
.qc.q3 .qtag{background:rgba(5,150,105,.15);color:var(--q3)}
.qmeta{font-size:11px;color:var(--muted);font-family:Arial,sans-serif}
.dg{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:18px}
@media(max-width:660px){.dg{grid-template-columns:1fr}}
.ds{border-radius:12px;padding:16px}
.ds.rs{background:#fef2f2;border:1px solid #fecaca}
.ds.gs{background:#f0fdf4;border:1px solid #bbf7d0}
.dh{display:flex;align-items:center;gap:7px;margin-bottom:10px;font-weight:700;font-size:12px;font-family:Arial,sans-serif}
.dh.r{color:#dc2626}.dh.g{color:#16a34a}
.dp{display:flex;gap:7px;margin-bottom:7px;font-size:11px;font-family:Arial,sans-serif}
.dp strong{display:block;color:var(--text);font-size:11px}
.dp em{color:var(--muted);font-size:10px;font-style:normal}
.tg{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:12px;margin-bottom:18px}
.tc{border-radius:12px;padding:16px;border:1px solid var(--border);background:var(--card)}
.tl{font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;color:var(--accent);margin-bottom:7px;font-family:Arial,sans-serif}
.tt{font-size:12px;font-style:italic;color:var(--text);line-height:1.6;border-left:3px solid var(--accent);padding-left:10px}
.sf{display:flex;flex-direction:column;gap:0;margin-bottom:18px}
.ss{display:flex;gap:12px;align-items:flex-start;position:relative}
.ss:not(:last-child)::after{content:'';position:absolute;left:15px;top:32px;bottom:-5px;width:2px;background:var(--border)}
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
.sp{background:linear-gradient(135deg,#f8fafc,#f1f5f9);border-radius:12px;padding:20px 20px 20px 34px;border-left:4px solid var(--gold);font-style:italic;font-size:13px;line-height:1.8;color:var(--text);margin-bottom:18px}
.al{list-style:none;margin-bottom:18px}
.al li{display:flex;gap:9px;padding:9px 12px;background:var(--card);border:1px solid var(--border);border-radius:8px;margin-bottom:7px;font-size:12px;font-family:Arial,sans-serif}
.al li strong{color:var(--navy)}
.timeline{position:relative;padding-left:32px;margin-bottom:24px}
.timeline::before{content:'';position:absolute;left:9px;top:0;bottom:0;width:3px;background:linear-gradient(to bottom,var(--accent),var(--gold),var(--green));border-radius:2px}
.ti{position:relative;margin-bottom:20px}
.td2{position:absolute;left:-26px;top:4px;width:16px;height:16px;border-radius:50%;border:3px solid #fff;z-index:1}
.td2.p1{background:var(--accent);box-shadow:0 0 0 2px var(--accent)}
.td2.ms{background:var(--gold);box-shadow:0 0 0 2px var(--gold)}
.td2.p2{background:var(--purple);box-shadow:0 0 0 2px var(--purple)}
.td2.p3{background:var(--green);box-shadow:0 0 0 2px var(--green)}
.td2.dl{background:var(--red);box-shadow:0 0 0 2px var(--red)}
.tdate{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--muted);margin-bottom:2px;font-family:Arial,sans-serif}
.ttitle{font-size:14px;font-weight:700;color:var(--navy);margin-bottom:4px}
.ttasks{font-size:11px;color:var(--muted);font-family:Arial,sans-serif;line-height:1.6}
.badge{display:inline-block;padding:2px 8px;border-radius:20px;font-size:10px;font-weight:600;font-family:Arial,sans-serif;margin-bottom:4px}
.bb{background:#dbeafe;color:#1d4ed8}.bg2{background:#fef3c7;color:#92400e}.bp{background:#ede9fe;color:#5b21b6}.bgr{background:#d1fae5;color:#065f46}.br{background:#fee2e2;color:#991b1b}
.rg{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px;margin-bottom:24px}
.ri{background:var(--card);border-radius:12px;padding:16px;text-align:center;border:1px solid var(--border);position:relative;overflow:hidden}
.ri::after{content:'';position:absolute;bottom:0;left:0;right:0;height:4px}
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
.sh{font-size:15px;font-weight:700;color:var(--navy);margin:20px 0 12px;display:flex;align-items:center;gap:8px}
.sh::after{content:'';flex:1;height:1px;background:var(--border)}
.alert{border-radius:10px;padding:12px 16px;margin-bottom:14px;font-family:Arial,sans-serif;font-size:12px;display:flex;gap:9px;align-items:flex-start}
.alert.info{background:#eff6ff;border:1px solid #bfdbfe;color:#1e40af}
.alert.warn{background:#fffbeb;border:1px solid #fde68a;color:#92400e}
.alert.ok{background:#f0fdf4;border:1px solid #bbf7d0;color:#065f46}
.footer{background:var(--navy);color:rgba(255,255,255,.6);text-align:center;padding:22px;font-family:Arial,sans-serif;font-size:11px;margin-top:36px}
.footer a{color:#fbbf24;text-decoration:none}
.cat-divider{background:linear-gradient(90deg,#1a237e,#10b981);color:#fff;padding:12px 20px;margin:0;font-family:Arial,sans-serif;font-size:11px;font-weight:700;letter-spacing:1px;text-transform:uppercase}
</style>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
'''

def get_topnav():
    """Return the top navigation bar"""
    return '''<div id="site-topnav" style="background:#1a237e;padding:12px 24px;display:flex;align-items:center;justify-content:space-between;font-family:'Poppins','Segoe UI',sans-serif;position:sticky;top:0;z-index:9999;box-shadow:0 2px 10px rgba(0,0,0,.3);"><a href="../../index.html" style="display:flex;align-items:center;gap:10px;text-decoration:none;"><span style="width:32px;height:32px;background:#ff6f00;border-radius:7px;display:inline-flex;align-items:center;justify-content:center;font-size:16px;">&#128218;</span><span style="color:#ffffff;font-size:14px;font-weight:700;">Student Essay <span style="color:#ffa000;">Research</span></span></a><span style="color:rgba(255,255,255,.6);font-size:12px;font-weight:500;">John Locke Visual Guide</span></div>
'''

def get_hero():
    """Return the hero section"""
    return '''
<div class="hero">
  <div class="hbadge">&#127891; Student Visual Guide</div>
  <h1>John Locke Institute<br><span>Essay Competition 2026</span></h1>
  <p>Your complete visual companion &mdash; Economics &amp; Politics questions, arguments, essay structure, and winning strategy.</p>
  <div class="cg">
    <div class="ci"><span class="num" id="d1">12</span><span class="lbl">Days to Questions</span></div>
    <div class="ci"><span class="num" id="d2">51</span><span class="lbl">Days to Secondary</span></div>
    <div class="ci"><span class="num" id="d3">72</span><span class="lbl">Days to Deadline</span></div>
    <div class="ci"><span class="num">~2,000</span><span class="lbl">Word Limit</span></div>
  </div>
</div>
'''

def get_nav_tabs():
    """Return the navigation tabs including both Economics and Politics"""
    return '''
<div class="nav-tabs">
  <div class="nav-tab active" onclick="show('overview')">&#127919; Overview</div>
  <div class="nav-tab" onclick="show('q1')">&#128178; Econ Q1</div>
  <div class="nav-tab" onclick="show('q2')">&#128200; Econ Q2</div>
  <div class="nav-tab" onclick="show('q3')">&#128188; Econ Q3</div>
  <div class="nav-tab pol" onclick="show('politics-overview')">&#127891; Politics</div>
  <div class="nav-tab pol" onclick="show('pol-q1')">&#127758; Pol Q1</div>
  <div class="nav-tab pol" onclick="show('pol-q2')">&#128679; Pol Q2</div>
  <div class="nav-tab pol" onclick="show('pol-q3')">&#127988; Pol Q3</div>
  <div class="nav-tab pol" onclick="show('pol-deepdive')">&#128300; Pol Deep</div>
  <div class="nav-tab pol" onclick="show('pol-pastq')">&#128203; Pol Past</div>
</div>
'''

def get_economics_overview():
    """Return the economics overview section (simplified for this merge)"""
    return '''
<!-- ECONOMICS OVERVIEW -->
<div id="overview" class="section active">
<div class="stitle">&#127919; Competition Overview</div>
<div class="ssub">John Locke Institute Essay Competition 2026 &mdash; Economics &amp; Politics Categories</div>

<div class="alert info"><span>&#128161;</span><div><strong>Two Categories Available:</strong> This guide covers both <strong>Economics</strong> and <strong>Politics</strong> categories. Use the tabs above to navigate between them. Each category has 3 questions to choose from.</div></div>

<div class="sg">
<div class="sc"><div class="si">&#127942;</div><div class="sv">JLI 2026</div><div class="sl">Competition</div></div>
<div class="sc"><div class="si">&#128197;</div><div class="sv">Apr 1</div><div class="sl">Questions Released</div></div>
<div class="sc"><div class="si">&#128203;</div><div class="sv">May 10</div><div class="sl">Secondary Deadline</div></div>
<div class="sc"><div class="si">&#127937;</div><div class="sv">May 31</div><div class="sl">Final Deadline</div></div>
<div class="sc"><div class="si">&#128221;</div><div class="sv">~2,000</div><div class="sl">Word Limit</div></div>
<div class="sc"><div class="si">&#128218;</div><div class="sv">3+3</div><div class="sl">Questions per Category</div></div>
</div>

<div class="sh">&#128178; Economics Questions 2026</div>
<div class="qs">
<div class="qc q1" onclick="show('q1')">
<div class="qn">Economics Q1 &bull; Evaluation</div>
<div class="qtag">&#128178; Monetary Economics</div>
<h3>Should we fear a cashless society?</h3>
<div class="qmeta">Privacy &bull; Financial Inclusion &bull; Monetary Freedom &bull; Surveillance</div>
</div>
<div class="qc q2" onclick="show('q2')">
<div class="qn">Economics Q2 &bull; Effects Analysis</div>
<div class="qtag">&#128200; Behavioural Economics</div>
<h3>Technology now allows personalised pricing. If this came to be widely used, what effects should we expect?</h3>
<div class="qmeta">Price Discrimination &bull; Efficiency &bull; Fairness &bull; Market Power</div>
</div>
<div class="qc q3" onclick="show('q3')">
<div class="qn">Economics Q3 &bull; Distributional Analysis</div>
<div class="qtag">&#128188; Labour Economics</div>
<h3>Did Jeff Bezos get rich at the expense of his customers, his employees, neither or both?</h3>
<div class="qmeta">Wealth Creation &bull; Labour &bull; Consumer Surplus &bull; Inequality</div>
</div>
</div>

<div class="sh">&#127891; Politics Questions 2026</div>
<div class="qs">
<div class="qc q1" onclick="show('pol-q1')">
<div class="qn">Politics Q1 &bull; Normative/Limits</div>
<div class="qtag">&#127758; Self-Determination</div>
<h3>Is the right to self-determination absolute?</h3>
<div class="qmeta">Sovereignty &bull; Secession &bull; Territorial Integrity &bull; International Law</div>
</div>
<div class="qc q2" onclick="show('pol-q2')">
<div class="qn">Politics Q2 &bull; Rights/Sovereignty</div>
<div class="qtag">&#128679; Border Control</div>
<h3>Should states have the right to control their borders?</h3>
<div class="qmeta">Migration &bull; Sovereignty &bull; Human Rights &bull; Global Justice</div>
</div>
<div class="qc q3" onclick="show('pol-q3')">
<div class="qn">Politics Q3 &bull; Conceptual Compatibility</div>
<div class="qtag">&#127988; Nationalism &amp; Liberalism</div>
<h3>Is nationalism compatible with liberalism?</h3>
<div class="qmeta">Identity &bull; Individual Rights &bull; Civic vs. Ethnic &bull; Solidarity</div>
</div>
</div>

</div>
'''

def get_economics_q1():
    """Return Economics Q1 section"""
    return '''
<!-- ECONOMICS Q1 -->
<div id="q1" class="section">
<div class="stitle" style="color:var(--q1)">&#128178; Econ Q1: Should we fear a cashless society?</div>
<div class="ssub">Monetary Economics &bull; Privacy &bull; Financial Inclusion</div>
<div style="background:linear-gradient(135deg,#0369a1,#0891b2);border-radius:14px;padding:22px;margin-bottom:18px;color:#fff">
<h2 style="font-size:20px;margin-bottom:10px">Should we fear a cashless society?</h2>
<div style="font-size:12px;opacity:.85;font-family:Arial,sans-serif">Key terms: <span style="background:rgba(255,255,255,.2);padding:2px 7px;border-radius:10px;margin-right:5px">cashless society</span><span style="background:rgba(255,255,255,.2);padding:2px 7px;border-radius:10px;margin-right:5px">fear</span><span style="background:rgba(255,255,255,.2);padding:2px 7px;border-radius:10px">monetary freedom</span></div>
</div>
<div class="sh">&#9876; The Core Debate</div>
<div class="dg">
<div class="ds rs"><div class="dh r">&#128308; YES &mdash; We Should Fear It</div>
<div class="dp"><div><strong>&#128065; Surveillance capitalism</strong><em>Every transaction tracked; governments gain total financial visibility</em></div></div>
<div class="dp"><div><strong>&#128683; Financial exclusion</strong><em>1.4B unbanked globally; elderly, rural, low-income excluded</em></div></div>
<div class="dp"><div><strong>&#9889; System fragility</strong><em>Power outages, cyberattacks leave people unable to transact</em></div></div>
</div>
<div class="ds gs"><div class="dh g">&#128994; NO &mdash; Benefits Outweigh Fears</div>
<div class="dp"><div><strong>&#128176; Efficiency gains</strong><em>Eliminates cash handling costs (~0.5% GDP); faster settlement</em></div></div>
<div class="dp"><div><strong>&#128373; Reduces crime</strong><em>Tax evasion, money laundering rely on cash anonymity</em></div></div>
<div class="dp"><div><strong>&#128200; Financial inclusion</strong><em>M-Pesa brought banking to 96% of Kenyan households</em></div></div>
</div>
</div>
<div class="sh">&#128203; Key Data</div>
<div class="datagrid">
<div class="dc"><div class="dstat">98%</div><div class="ddesc">Sweden transactions are digital (2023)</div><div class="dsrc">Riksbank</div></div>
<div class="dc"><div class="dstat">1.4B</div><div class="ddesc">Adults globally without bank accounts</div><div class="dsrc">World Bank 2021</div></div>
<div class="dc"><div class="dstat">130+</div><div class="ddesc">Countries exploring CBDCs</div><div class="dsrc">Atlantic Council 2024</div></div>
</div>
</div>
'''

def get_economics_q2():
    """Return Economics Q2 section"""
    return '''
<!-- ECONOMICS Q2 -->
<div id="q2" class="section">
<div class="stitle" style="color:var(--q2)">&#128200; Econ Q2: Personalised Pricing Effects</div>
<div class="ssub">Behavioural Economics &bull; Price Discrimination &bull; Welfare Analysis</div>
<div style="background:linear-gradient(135deg,#5b21b6,#7c3aed);border-radius:14px;padding:22px;margin-bottom:18px;color:#fff">
<h2 style="font-size:20px;margin-bottom:10px">Technology now allows personalised pricing. If this came to be widely used, what effects should we expect?</h2>
<div style="font-size:12px;opacity:.85;font-family:Arial,sans-serif">Key terms: <span style="background:rgba(255,255,255,.2);padding:2px 7px;border-radius:10px;margin-right:5px">personalised pricing</span><span style="background:rgba(255,255,255,.2);padding:2px 7px;border-radius:10px">welfare effects</span></div>
</div>
<div class="sh">&#128202; Effects Framework</div>
<div class="dg">
<div class="ds rs"><div class="dh r">&#128308; Negative Effects</div>
<div class="dp"><div><strong>&#128100; Consumer surplus extraction</strong><em>Firms capture ALL consumer surplus</em></div></div>
<div class="dp"><div><strong>&#128065; Privacy erosion</strong><em>Requires mass data collection</em></div></div>
<div class="dp"><div><strong>&#9878; Fairness concerns</strong><em>Poor pay more relative to income</em></div></div>
</div>
<div class="ds gs"><div class="dh g">&#128994; Positive Effects</div>
<div class="dp"><div><strong>&#128200; Allocative efficiency</strong><em>No deadweight loss with perfect price discrimination</em></div></div>
<div class="dp"><div><strong>&#128176; Access expansion</strong><em>Low-income consumers can access goods at lower prices</em></div></div>
<div class="dp"><div><strong>&#127775; Innovation incentives</strong><em>Higher profits fund R&amp;D</em></div></div>
</div>
</div>
</div>
'''

def get_economics_q3():
    """Return Economics Q3 section"""
    return '''
<!-- ECONOMICS Q3 -->
<div id="q3" class="section">
<div class="stitle" style="color:var(--q3)">&#128188; Econ Q3: Did Bezos Get Rich at Others' Expense?</div>
<div class="ssub">Labour Economics &bull; Wealth Creation &bull; Consumer Surplus &bull; Inequality</div>
<div style="background:linear-gradient(135deg,#065f46,#059669);border-radius:14px;padding:22px;margin-bottom:18px;color:#fff">
<h2 style="font-size:20px;margin-bottom:10px">Did Jeff Bezos get rich at the expense of his customers, his employees, neither or both?</h2>
<div style="font-size:12px;opacity:.85;font-family:Arial,sans-serif">Key terms: <span style="background:rgba(255,255,255,.2);padding:2px 7px;border-radius:10px;margin-right:5px">at the expense of</span><span style="background:rgba(255,255,255,.2);padding:2px 7px;border-radius:10px">zero-sum vs positive-sum</span></div>
</div>
<div class="alert info"><span>&#128161;</span><div><strong>Key analytical move:</strong> "At the expense of" means zero-sum. Test whether each relationship is zero-sum or positive-sum.</div></div>
<div class="sh">&#128202; The Evidence</div>
<div class="dg">
<div class="ds gs"><div class="dh g">&#128994; NOT at Customers' Expense</div>
<div class="dp"><div><strong>&#128200; Consumer surplus massive</strong><em>Amazon Prime saves avg. household $1,000+/yr</em></div></div>
<div class="dp"><div><strong>&#128176; Competitive pricing</strong><em>Amazon built market share through LOW prices</em></div></div>
</div>
<div class="ds rs"><div class="dh r">&#128308; YES at Employees' Expense</div>
<div class="dp"><div><strong>&#128683; Warehouse conditions</strong><em>Injury rates 2x industry average</em></div></div>
<div class="dp"><div><strong>&#128100; Monopsony power</strong><em>Amazon = 45% of US e-commerce</em></div></div>
</div>
</div>
</div>
'''

def get_footer():
    """Return the footer section"""
    return '''
<div class="footer">&#127891; John Locke Institute 2026 Essay Competition &mdash; Economics &amp; Politics Visual Guide &bull; Created for student preparation &bull; <a href="https://www.johnlockeinstitute.com" target="_blank">johnlockeinstitute.com</a></div>
'''

def get_script():
    """Return the JavaScript for navigation"""
    return '''
<script>
function show(id) {
  document.querySelectorAll(".section").forEach(s => s.classList.remove("active"));
  document.querySelectorAll(".nav-tab").forEach(t => t.classList.remove("active"));
  var el = document.getElementById(id);
  if (el) el.classList.add("active");
  var tabs = document.querySelectorAll(".nav-tab");
  var map={overview:0,q1:1,q2:2,q3:3,'politics-overview':4,'pol-q1':5,'pol-q2':6,'pol-q3':7,'pol-deepdive':8,'pol-pastq':9};
  if (map[id] !== undefined && tabs[map[id]]) tabs[map[id]].classList.add("active");
}
(function() {
  var deadlines = [
    new Date("2026-04-01"),
    new Date("2026-05-10"),
    new Date("2026-05-31")
  ];
  var ids = ["d1","d2","d3"];
  var now = new Date();
  deadlines.forEach(function(d, i) {
    var diff = Math.ceil((d - now) / 86400000);
    var el = document.getElementById(ids[i]);
    if (el) el.textContent = diff > 0 ? diff : "PASSED";
  });
})();
</script>
'''

def get_site_footer():
    """Return the site footer"""
    return '''
<div id="site-footer" style="background:#1a237e;color:rgba(255,255,255,.55);text-align:center;padding:28px 20px;font-family:'Poppins','Segoe UI',sans-serif;font-size:12px;margin-top:40px;"><div style="font-size:15px;font-weight:700;color:#fff;margin-bottom:6px;">Student Essay <span style="color:#ffcc02;">Research</span> 2026</div><a href="../../index.html" style="color:#ffcc02;text-decoration:none;font-weight:600;">&#127968; Home</a>&nbsp;&bull;&nbsp;<a href="https://github.com/rkmaheshglobal/student-essay-research" target="_blank" rel="noopener" style="color:#ffcc02;text-decoration:none;">GitHub</a>&nbsp;&bull;&nbsp; Last updated March 2026</div>
'''

def main():
    """Generate the complete HTML file"""
    # Ensure output directory exists
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'outputs')
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, 'john-locke-visual-guide.html')
    
    # Build the complete HTML
    html_parts = [
        get_html_head(),
        get_topnav(),
        get_hero(),
        get_nav_tabs(),
        get_economics_overview(),
        get_economics_q1(),
        get_economics_q2(),
        get_economics_q3(),
        # Politics sections
        get_politics_overview(),
        get_politics_q1(),
        get_politics_q2(),
        get_politics_q3(),
        get_politics_deep_dive(),
        get_politics_past_questions(),
        # Footer and scripts
        get_footer(),
        get_script(),
        get_site_footer(),
        '</body>\n</html>'
    ]
    
    html_content = ''.join(html_parts)
    
    # Write to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Generated: {output_path}")
    print(f"Total size: {len(html_content):,} characters")
    print("Done!")

if __name__ == "__main__":
    main()