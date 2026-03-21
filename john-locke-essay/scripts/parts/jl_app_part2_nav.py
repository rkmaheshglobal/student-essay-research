"""Essay Prep App Part 2: Navigation Sidebar"""

def get_app_nav():
    return '''<button class="hamburger" id="hbtn" onclick="toggleNav()" aria-label="Toggle navigation">
  <span></span><span></span><span></span>
</button>
<div class="overlay" id="overlay" onclick="toggleNav()"></div>
<nav id="sidenav">
  <div class="sh"><h1>JLI Essay Prep 2026</h1><p>Economics & Politics</p></div>
  <a href="../../index.html" style="display:flex;align-items:center;gap:8px;padding:9px 16px;font-size:12px;color:rgba(255,255,255,.75);font-family:sans-serif;text-decoration:none;border-bottom:1px solid rgba(255,255,255,.1);transition:all .15s" onmouseover="this.style.background='rgba(255,255,255,.08)';this.style.color='#fff'" onmouseout="this.style.background='';this.style.color='rgba(255,255,255,.75)'">&#127968; Home</a>
  <div class="nl">Overview</div>
  <button class="ni active" onclick="go('dash')">🏠 Dashboard</button>
  <button class="ni" onclick="go('time')">📅 Timeline & Plan</button>
  <div class="nl" style="color:rgba(255,165,0,.6)">Economics 2026</div>
  <button class="ni" onclick="go('eq1')">💳 Q1: Cashless Society</button>
  <button class="ni" onclick="go('eq2')">💰 Q2: Personalised Pricing</button>
  <button class="ni" onclick="go('eq3')">📦 Q3: Jeff Bezos</button>
  <div class="nl" style="color:rgba(16,185,129,.6)">Politics 2026</div>
  <button class="ni" onclick="go('pq1')">🌍 Q1: Self-Determination</button>
  <button class="ni" onclick="go('pq2')">🚧 Q2: Border Control</button>
  <button class="ni" onclick="go('pq3')">🏳️ Q3: Nationalism</button>
  <div class="nl">Resources</div>
  <button class="ni" onclick="go('fw')">🧠 Argument Frameworks</button>
  <button class="ni" onclick="go('past')">📚 Past Questions</button>
  <button class="ni" onclick="go('read')">📖 Reading List</button>
  <div class="nl">Support</div>
  <button class="ni" onclick="go('ment')">🎓 Mentorship Orgs</button>
  <button class="ni" onclick="go('chk')">✅ My Checklist</button>
</nav>
<main>
'''

if __name__ == "__main__":
    print(get_app_nav())
    print("Part 2 (Navigation) ready")