import os
os.makedirs("outputs/cambridge-essay", exist_ok=True)

html = open("outputs/cambridge-essay/cambridge-essay-visual-guide.html", "w", encoding="utf-8")
w = html.write

w("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cambridge Re:think Essay Competition 2026 — Student Visual Guide</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',Arial,sans-serif;background:#f0f4f8;color:#1e293b;line-height:1.6}
.hero{background:linear-gradient(135deg,#1e3a5f 0%,#2563eb 60%,#7c3aed 100%);color:#fff;padding:40px 24px 32px;text-align:center}
.hero h1{font-size:clamp(22px,4vw,36px);font-weight:800;letter-spacing:-0.5px;margin-bottom:8px}
.hero .sub{font-size:15px;opacity:0.88;margin-bottom:20px}
.badges{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-bottom:20px}
.badge{background:rgba(255,255,255,0.18);border:1px solid rgba(255,255,255,0.35);border-radius:20px;padding:5px 14px;font-size:13px;font-weight:600}
.countdown-row{display:flex;gap:16px;justify-content:center;flex-wrap:wrap}
.cd-box{background:rgba(255,255,255,0.15);border-radius:10px;padding:12px 20px;text-align:center;min-width:80px}
.cd-box .num{font-size:28px;font-weight:800;display:block}
.cd-box .lbl{font-size:11px;opacity:0.8;text-transform:uppercase;letter-spacing:1px}
nav{background:#1e293b;display:flex;flex-wrap:wrap;gap:2px;padding:8px 12px;position:sticky;top:0;z-index:100}
.nav-tab{background:transparent;border:none;color:#94a3b8;padding:7px 14px;border-radius:6px;cursor:pointer;font-size:13px;font-weight:500;transition:all 0.2s}
.nav-tab:hover,.nav-tab.active{background:#2563eb;color:#fff}
.section{display:none;max-width:960px;margin:0 auto;padding:24px 16px}
.section.active{display:block}
.sh{font-size:18px;font-weight:700;color:#1e3a5f;border-left:4px solid #2563eb;padding-left:12px;margin:24px 0 14px}
.card{background:#fff;border-radius:12px;padding:18px 20px;margin-bottom:14px;box-shadow:0 2px 8px rgba(0,0,0,0.07)}
.ctitle{font-weight:700;font-size:15px;color:#1e3a5f;margin-bottom:8px}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px;margin-bottom:14px}
.grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin-bottom:14px}
.stat-box{background:#fff;border-radius:10px;padding:16px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,0.07)}
.stat-num{font-size:28px;font-weight:800;color:#2563eb;display:block}
.stat-lbl{font-size:12px;color:#64748b;margin-top:4px}
.prompt-card{background:#fff;border-radius:12px;padding:18px 20px;margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,0.07);border-left:4px solid #2563eb;cursor:pointer;transition:all 0.2s}
.prompt-card:hover{transform:translateY(-2px);box-shadow:0 4px 16px rgba(37,99,235,0.15)}
.prompt-card.p1{border-color:#ef4444}
.prompt-card.p2{border-color:#f97316}
.prompt-card.p3{border-color:#8b5cf6}
.prompt-card.p4{border-color:#10b981}
.prompt-card.p5{border-color:#f59e0b}
.prompt-card.p6{border-color:#06b6d4}
.prompt-card.p7{border-color:#ec4899}
.prompt-card.p8{border-color:#14b8a6}
.prompt-card.p9{border-color:#6366f1}
.prompt-num{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:#64748b;margin-bottom:4px}
.prompt-q{font-size:15px;font-weight:700;color:#1e293b;margin-bottom:8px}
.prompt-meta{display:flex;gap:8px;flex-wrap:wrap}
.tag{background:#f1f5f9;border-radius:12px;padding:3px 10px;font-size:12px;color:#475569;font-weight:500}
.tag.hot{background:#fef2f2;color:#dc2626}
.tag.orig{background:#f0fdf4;color:#16a34a}
.tag.hard{background:#faf5ff;color:#7c3aed}
.detail-box{background:#f8fafc;border-radius:8px;padding:14px;margin-top:10px;display:none;font-size:14px}
.detail-box.open{display:block}
.al{list-style:none;padding:0}
.al li{display:flex;gap:10px;padding:8px 0;border-bottom:1px solid #f1f5f9;font-size:14px;align-items:flex-start}
.al li:last-child{border-bottom:none}
.al li span{background:#2563eb;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;flex-shrink:0;margin-top:1px}
.prize-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin-bottom:14px}
.prize-box{border-radius:10px;padding:14px;text-align:center}
.prize-box.gold{background:linear-gradient(135deg,#fef3c7,#fde68a);border:2px solid #f59e0b}
.prize-box.silver{background:linear-gradient(135deg,#f1f5f9,#e2e8f0);border:2px solid #94a3b8}
.prize-box.bronze{background:linear-gradient(135deg,#fef3c7,#fed7aa);border:2px solid #d97706}
.prize-box.special{background:linear-gradient(135deg,#ede9fe,#ddd6fe);border:2px solid #7c3aed}
.prize-box .pname{font-weight:700;font-size:14px;margin-bottom:4px}
.prize-box .pamount{font-size:20px;font-weight:800;color:#1e293b}
.prize-box .pdesc{font-size:11px;color:#64748b;margin-top:4px}
.timeline{position:relative;padding-left:28px}
.timeline::before{content:'';position:absolute;left:8px;top:0;bottom:0;width:2px;background:#e2e8f0}
.tl-item{position:relative;margin-bottom:16px}
.tl-item::before{content:'';position:absolute;left:-24px;top:4px;width:12px;height:12px;border-radius:50%;background:#2563eb;border:2px solid #fff;box-shadow:0 0 0 2px #2563eb}
.tl-item.done::before{background:#10b981;box-shadow:0 0 0 2px #10b981}
.tl-item.urgent::before{background:#ef4444;box-shadow:0 0 0 2px #ef4444}
.tl-date{font-size:12px;font-weight:700;color:#2563eb;text-transform:uppercase;letter-spacing:0.5px}
.tl-title{font-weight:600;font-size:14px;color:#1e293b}
.tl-desc{font-size:13px;color:#64748b;margin-top:2px}
.thesis-box{background:linear-gradient(135deg,#eff6ff,#dbeafe);border:1px solid #bfdbfe;border-radius:10px;padding:16px;margin-bottom:12px}
.thesis-label{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:#2563eb;margin-bottom:6px}
.thesis-text{font-size:14px;font-style:italic;color:#1e3a5f;line-height:1.6}
.book-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px}
.book-card{background:#fff;border-radius:8px;padding:12px;box-shadow:0 1px 4px rgba(0,0,0,0.08);border-top:3px solid #2563eb}
.book-title{font-weight:700;font-size:13px;color:#1e293b;margin-bottom:3px}
.book-author{font-size:12px;color:#64748b;margin-bottom:4px}
.book-why{font-size:12px;color:#475569;font-style:italic}
.warn{background:#fef2f2;border:1px solid #fecaca;border-radius:8px;padding:12px 14px;margin-bottom:10px;font-size:13px;color:#dc2626}
.tip{background:#f0fdf4;border:1px solid #bbf7d0;border-radius:8px;padding:12px 14px;margin-bottom:10px;font-size:13px;color:#15803d}
.footer{background:#1e293b;color:#94a3b8;text-align:center;padding:20px;font-size:13px;margin-top:24px}
.footer a{color:#60a5fa;text-decoration:none}
table{width:100%;border-collapse:collapse;font-size:13px}
th{background:#1e293b;color:#fff;padding:10px;text-align:left}
td{padding:9px 10px;border-bottom:1px solid #f1f5f9}
tr:nth-child(even){background:#f8fafc}
.score-bar{height:8px;border-radius:4px;background:#e2e8f0;margin-top:4px}
.score-fill{height:8px;border-radius:4px;background:linear-gradient(90deg,#2563eb,#7c3aed)}
</style>
</head>
<body>
<div class="hero">
<h1>&#127891; Cambridge Re:think Essay Competition 2026</h1>
<div class="sub">Senior Division (Ages 14–18) &bull; Visual Study Guide &bull; 9 Prompts from Harvard, Stanford, Oxford &amp; Cambridge Professors</div>
<div class="badges">
<span class="badge">&#127381; FREE Entry</span>
<span class="badge">&#128196; Max 2,000 Words</span>
<span class="badge">&#127942; $150 Gold Prize + Cambridge Ceremony</span>
<span class="badge">&#127758; Open Worldwide</span>
<span class="badge">&#128683; No AI Assistance</span>
</div>
<div class="countdown-row">
<div class="cd-box"><span class="num" id="d1">--</span><span class="lbl">Days to Deadline</span></div>
<div class="cd-box"><span class="num" id="d2">--</span><span class="lbl">Days to Results</span></div>
<div class="cd-box"><span class="num" id="d3">--</span><span class="lbl">Days to Cambridge</span></div>
</div>
</div>
<nav>
<button class="nav-tab active" onclick="show('overview')">&#127968; Overview</button>
<button class="nav-tab" onclick="show('prompts')">&#10067; All 9 Prompts</button>
<button class="nav-tab" onclick="show('strategy')">&#127919; Strategy</button>
<button class="nav-tab" onclick="show('structure')">&#128196; Essay Structure</button>
<button class="nav-tab" onclick="show('reading')">&#128218; Reading Lists</button>