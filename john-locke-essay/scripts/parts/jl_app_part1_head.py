"""Essay Prep App Part 1: HTML Head and Styles"""

def get_app_head():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>JLI Essay Prep 2026 - Economics & Politics</title>
<style>
:root{--p:#1a237e;--a:#ff6f00;--al:#fff3e0;--bg:#f5f7ff;--c:#fff;--t:#1e2d3d;--m:#6b7c93;--b:#e2e8f0;--ok:#2d7d46;--w:#b45309;--bad:#c0392b;--sw:250px;--pol:#10b981}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Poppins','Segoe UI',sans-serif;background:var(--bg);color:var(--t);display:flex;min-height:100vh}
nav{width:var(--sw);background:var(--p);position:fixed;top:0;left:0;height:100vh;overflow-y:auto;z-index:100}
.sh{padding:20px 16px 14px;border-bottom:1px solid rgba(255,255,255,.1)}
.sh h1{font-size:14px;font-weight:700;color:var(--a)}
.sh p{font-size:11px;color:rgba(255,255,255,.45);font-family:sans-serif;margin-top:3px}
.nl{font-size:10px;text-transform:uppercase;letter-spacing:1px;color:rgba(255,255,255,.3);padding:10px 16px 3px;font-family:sans-serif}
.ni{display:flex;align-items:center;gap:8px;padding:9px 16px;cursor:pointer;font-size:12px;color:rgba(255,255,255,.75);font-family:sans-serif;border:none;background:none;width:100%;text-align:left;transition:all .15s}
.ni:hover{background:rgba(255,255,255,.08);color:#fff}
.ni.active{background:var(--a);color:var(--p);font-weight:700}
.ni.pol-active{background:var(--pol);color:#fff;font-weight:700}
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
.cc.r{background:var(--bad)}.cc.o{background:var(--w)}.cc.g{background:var(--pol)}
.cd{font-size:38px;font-weight:700;color:var(--a);line-height:1}
.cl{font-size:11px;color:rgba(255,255,255,.65);margin-top:5px;font-family:sans-serif}
.cdt{font-size:12px;color:rgba(255,255,255,.85);margin-top:3px;font-family:sans-serif}
.tabs{display:flex;gap:3px;border-bottom:2px solid #e2e8f0;margin-bottom:16px;flex-wrap:wrap}
.tab{padding:7px 14px;font-size:12px;cursor:pointer;border-radius:5px 5px 0 0;font-family:sans-serif;border:none;background:none;color:var(--m)}
.tab.on{background:#ff6f00;color:#fff}
.tc{display:none}.tc.on{display:block}
.thesis{background:var(--al);border-left:4px solid var(--a);border-radius:0 8px 8px 0;padding:14px;margin-bottom:10px}
.tl{font-size:10px;text-transform:uppercase;letter-spacing:1px;color:var(--w);font-family:sans-serif;font-weight:700;margin-bottom:5px}
.tt{font-style:italic;color:var(--p);line-height:1.6;font-size:13px}
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
.pro h4{color:var(--ok);font-size:12px;font-family:sans-serif;margin-bottom:7px}
.con h4{color:var(--bad);font-size:12px;font-family:sans-serif;margin-bottom:7px}
ul.pts{padding-left:15px}.pts li{font-size:12px;font-family:sans-serif;line-height:1.7}
.tl-w{position:relative;padding-left:22px}
.tl-w::before{content:'';position:absolute;left:7px;top:0;bottom:0;width:2px;background:var(--b)}
.tli{position:relative;margin-bottom:18px}
.tld{position:absolute;left:-19px;top:3px;width:11px;height:11px;border-radius:50%;background:var(--a);border:2px solid var(--p)}
.td{font-size:10px;color:var(--m);font-family:sans-serif;font-weight:700;text-transform:uppercase;letter-spacing:.5px}
.tt2{font-size:14px;font-weight:700;color:var(--p);margin:2px 0}
.td2{font-size:12px;color:var(--m);font-family:sans-serif}
.cl-list{list-style:none}
.cl-list li{display:flex;align-items:flex-start;gap:9px;padding:7px 0;border-bottom:1px solid var(--b);font-family:sans-serif;font-size:13px}
.cl-list input[type=checkbox]{width:16px;height:16px;cursor:pointer;flex-shrink:0;margin-top:2px;accent-color:var(--p)}
.cl-list label{cursor:pointer;line-height:1.4}
.cl-list input:checked+label{text-decoration:line-through;color:var(--m)}
bq{display:block;border-left:4px solid var(--a);padding:11px 14px;background:var(--al);border-radius:0 7px 7px 0;font-style:italic;margin:10px 0;line-height:1.6;font-size:13px}
.org{background:var(--c);border-radius:9px;border:1px solid var(--b);padding:16px;margin-bottom:12px}
.on2{font-size:15px;font-weight:700;color:var(--p)}
.ou{font-size:11px;color:var(--a);font-family:sans-serif;margin:2px 0 7px}
.od{font-size:12px;color:var(--m);font-family:sans-serif;line-height:1.5}
.book{display:flex;gap:10px;padding:10px 0;border-bottom:1px solid var(--b);align-items:flex-start}
.bi{font-size:22px;flex-shrink:0}
.bt{font-size:13px;font-weight:700;color:var(--p)}
.ba{font-size:11px;color:var(--m);font-family:sans-serif}
.bw{font-size:11px;color:var(--m);font-family:sans-serif;margin-top:3px;font-style:italic}
.hamburger{display:none;position:fixed;top:12px;left:12px;z-index:200;background:var(--p);border:none;border-radius:8px;padding:9px 10px;cursor:pointer;flex-direction:column;gap:5px;box-shadow:0 2px 8px rgba(0,0,0,.3)}
.hamburger span{display:block;width:22px;height:2px;background:var(--a);border-radius:2px;transition:transform .3s,opacity .3s}
.hamburger.open span:nth-child(1){transform:translateY(7px) rotate(45deg)}
.hamburger.open span:nth-child(2){opacity:0}
.hamburger.open span:nth-child(3){transform:translateY(-7px) rotate(-45deg)}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.45);z-index:99}
.overlay.on{display:block}
@media(max-width:768px){.hamburger{display:flex}nav{transform:translateX(-100%);transition:transform .3s ease;z-index:150}nav.open{transform:translateX(0)}main{margin-left:0!important}.pg{padding:16px;padding-top:60px}.g2,.g3{grid-template-columns:1fr}}
</style>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
'''

if __name__ == "__main__":
    print(get_app_head())
    print("Part 1 (Head) ready")