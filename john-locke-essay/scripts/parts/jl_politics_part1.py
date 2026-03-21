"""Politics Part 1: Politics Overview Section with 2026 Questions"""

def get_politics_overview():
    return '''
<!-- POLITICS OVERVIEW -->
<div id="politics-overview" class="section">
<div class="stitle">&#127891; Politics Category Overview</div>
<div class="ssub">John Locke Institute Essay Competition 2026 &mdash; Politics Category</div>

<div class="sg">
<div class="sc"><div class="si">&#127942;</div><div class="sv">JLI 2026</div><div class="sl">Competition</div></div>
<div class="sc"><div class="si">&#128197;</div><div class="sv">Apr 1</div><div class="sl">Questions Released</div></div>
<div class="sc"><div class="si">&#128203;</div><div class="sv">May 10</div><div class="sl">Secondary Deadline</div></div>
<div class="sc"><div class="si">&#127937;</div><div class="sv">May 31</div><div class="sl">Final Deadline</div></div>
<div class="sc"><div class="si">&#128221;</div><div class="sv">~2,000</div><div class="sl">Word Limit</div></div>
<div class="sc"><div class="si">&#128218;</div><div class="sv">3</div><div class="sl">Questions to Choose</div></div>
</div>

<div class="sh">&#127775; The 3 Official 2026 Politics Questions</div>
<div class="qs">
<div class="qc q1" onclick="show('pol-q1')">
<div class="qn">Question 1 &bull; Normative/Limits Analysis</div>
<div class="qtag">&#127758; Self-Determination</div>
<h3>Is the right to self-determination absolute?</h3>
<div class="qmeta">Sovereignty &bull; Secession &bull; Territorial Integrity &bull; International Law</div>
</div>
<div class="qc q2" onclick="show('pol-q2')">
<div class="qn">Question 2 &bull; Rights/Sovereignty Analysis</div>
<div class="qtag">&#128679; Border Control</div>
<h3>Should states have the right to control their borders?</h3>
<div class="qmeta">Migration &bull; Sovereignty &bull; Human Rights &bull; Global Justice</div>
</div>
<div class="qc q3" onclick="show('pol-q3')">
<div class="qn">Question 3 &bull; Conceptual Compatibility</div>
<div class="qtag">&#127988; Nationalism &amp; Liberalism</div>
<h3>Is nationalism compatible with liberalism?</h3>
<div class="qmeta">Identity &bull; Individual Rights &bull; Civic vs. Ethnic &bull; Solidarity</div>
</div>
</div>

<div class="sh">&#9878; Cross-Cutting Themes (appear in ALL questions)</div>
<div class="themegrid">
<div class="thm"><div class="thmi">&#127758;</div><div class="thmt">Sovereignty &amp; Self-Governance</div><div class="thmd">All three questions involve the tension between collective self-governance and external constraints</div><div class="thmq"><span class="thmqb q1">1</span><span class="thmqb q2">2</span><span class="thmqb q3">3</span></div></div>
<div class="thm"><div class="thmi">&#9878;</div><div class="thmt">Individual vs. Collective Rights</div><div class="thmd">The tension between individual human rights and collective self-determination</div><div class="thmq"><span class="thmqb q1">1</span><span class="thmqb q2">2</span><span class="thmqb q3">3</span></div></div>
<div class="thm"><div class="thmi">&#128100;</div><div class="thmt">Who Belongs?</div><div class="thmd">Questions of membership, identity, and who counts as "the people"</div><div class="thmq"><span class="thmqb q1">1</span><span class="thmqb q2">2</span><span class="thmqb q3">3</span></div></div>
<div class="thm"><div class="thmi">&#127963;</div><div class="thmt">International Order</div><div class="thmd">How principles interact with the existing system of nation-states</div><div class="thmq"><span class="thmqb q1">1</span><span class="thmqb q2">2</span><span class="thmqb q3">3</span></div></div>
<div class="thm"><div class="thmi">&#128065;</div><div class="thmt">Universal vs. Particular</div><div class="thmd">Tension between universal principles and particular communities</div><div class="thmq"><span class="thmqb q1">1</span><span class="thmqb q2">2</span><span class="thmqb q3">3</span></div></div>
</div>

<div class="sh">&#128202; Question Selection Guide</div>
<div class="card"><div class="ctitle">Which Question Should You Choose?</div>
<div class="tipgrid">
<div class="tip"><div class="tipn" style="background:var(--q1)">Q1</div><div><div class="tipt">Self-Determination</div><div class="tipd">Best if you&apos;re interested in international law and political philosophy. Strong case studies available (Kosovo, Catalonia, Taiwan). Requires nuanced, conditional arguments.</div></div></div>
<div class="tip"><div class="tipn" style="background:var(--q2)">Q2</div><div><div class="tipt">Border Control</div><div class="tipd">Best if you&apos;re interested in migration and global justice. Clear contemporary relevance. Requires engaging with both sovereignty and human rights arguments.</div></div></div>
<div class="tip"><div class="tipn" style="background:var(--q3)">Q3</div><div><div class="tipt">Nationalism &amp; Liberalism</div><div class="tipd">Best if you enjoy political theory and intellectual history. Requires distinguishing between types of nationalism. Abstract conceptual analysis needed.</div></div></div>
</div></div>

<div class="sh">&#128203; Question Comparison Matrix</div>
<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:12px;font-family:Arial,sans-serif">
<tr style="background:#1e293b;color:#fff"><th style="padding:10px;text-align:left">Factor</th><th style="padding:10px">Q1: Self-Determination</th><th style="padding:10px">Q2: Border Control</th><th style="padding:10px">Q3: Nationalism</th></tr>
<tr style="background:#f8fafc"><td style="padding:9px;font-weight:600">Originality Potential</td><td style="padding:9px;text-align:center">High</td><td style="padding:9px;text-align:center">Medium</td><td style="padding:9px;text-align:center">Medium</td></tr>
<tr><td style="padding:9px;font-weight:600">Data Availability</td><td style="padding:9px;text-align:center">High (many cases)</td><td style="padding:9px;text-align:center">High</td><td style="padding:9px;text-align:center">Medium</td></tr>
<tr style="background:#f8fafc"><td style="padding:9px;font-weight:600">Counterargument Richness</td><td style="padding:9px;text-align:center">Very High</td><td style="padding:9px;text-align:center">Very High</td><td style="padding:9px;text-align:center">High</td></tr>
<tr><td style="padding:9px;font-weight:600">Risk of Clich&eacute;</td><td style="padding:9px;text-align:center">Medium</td><td style="padding:9px;text-align:center">High</td><td style="padding:9px;text-align:center">Medium</td></tr>
<tr style="background:#f8fafc"><td style="padding:9px;font-weight:600">Philosophical Depth</td><td style="padding:9px;text-align:center">Very High</td><td style="padding:9px;text-align:center">High</td><td style="padding:9px;text-align:center">Very High</td></tr>
</table></div>

<div class="sh">&#128161; Key Thinkers to Reference</div>
<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:12px;font-family:Arial,sans-serif">
<tr style="background:#1e293b;color:#fff"><th style="padding:10px;text-align:left">Thinker</th><th style="padding:10px;text-align:left">Area</th><th style="padding:10px;text-align:left">Key Idea</th></tr>
<tr style="background:#f8fafc"><td style="padding:9px;font-weight:600">John Locke</td><td style="padding:9px">Consent theory</td><td style="padding:9px">Government requires consent of the governed</td></tr>
<tr><td style="padding:9px;font-weight:600">John Rawls</td><td style="padding:9px">Justice</td><td style="padding:9px">Veil of ignorance, justice as fairness</td></tr>
<tr style="background:#f8fafc"><td style="padding:9px;font-weight:600">Allen Buchanan</td><td style="padding:9px">Secession</td><td style="padding:9px">Remedial right only theory</td></tr>
<tr><td style="padding:9px;font-weight:600">Margaret Moore</td><td style="padding:9px">Territory</td><td style="padding:9px">Primary right to territory</td></tr>
<tr style="background:#f8fafc"><td style="padding:9px;font-weight:600">Joseph Carens</td><td style="padding:9px">Migration</td><td style="padding:9px">Open borders argument</td></tr>
<tr><td style="padding:9px;font-weight:600">David Miller</td><td style="padding:9px">Nationalism</td><td style="padding:9px">Liberal nationalism, territorial rights</td></tr>
<tr style="background:#f8fafc"><td style="padding:9px;font-weight:600">Yael Tamir</td><td style="padding:9px">Nationalism</td><td style="padding:9px">Liberal nationalism thesis</td></tr>
<tr><td style="padding:9px;font-weight:600">Michael Walzer</td><td style="padding:9px">Communitarianism</td><td style="padding:9px">Spheres of justice, just war</td></tr>
<tr style="background:#f8fafc"><td style="padding:9px;font-weight:600">Will Kymlicka</td><td style="padding:9px">Minorities</td><td style="padding:9px">Multicultural citizenship</td></tr>
</table></div>

</div>
'''

if __name__ == "__main__":
    print(get_politics_overview())
    print("Politics Part 1 (Overview) ready")