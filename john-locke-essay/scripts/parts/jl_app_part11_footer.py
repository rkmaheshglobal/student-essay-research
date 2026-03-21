"""Essay Prep App Part 11: Checklist, Footer, and JavaScript"""

def get_app_footer():
    return '''<!-- CHECKLIST -->
<div id="pg-chk" class="pg">
  <div class="ph"><h2>✅ My Competition Checklist</h2><p>Track your progress through the JLI 2026 preparation</p></div>
  <div class="card">
    <div class="ct">📅 Phase 1: Preparation (Now — April 1)</div>
    <ul class="cl-list">
      <li><input type="checkbox" id="c1"><label for="c1">Read all question deep dives in this app (Economics & Politics)</label></li>
      <li><input type="checkbox" id="c2"><label for="c2">Choose your category: Economics or Politics</label></li>
      <li><input type="checkbox" id="c3"><label for="c3">Choose your top 1-2 questions to focus on</label></li>
      <li><input type="checkbox" id="c4"><label for="c4">Email your teacher for mentorship</label></li>
      <li><input type="checkbox" id="c5"><label for="c5">Sign up for Marginal Revolution University (free)</label></li>
      <li><input type="checkbox" id="c6"><label for="c6">Read at least one book from the reading list</label></li>
      <li><input type="checkbox" id="c7"><label for="c7">Read 3 past JLI winning essays on their website</label></li>
      <li><input type="checkbox" id="c8"><label for="c8">Build a sources document with 10+ academic references</label></li>
    </ul>
  </div>
  <div class="card">
    <div class="ct">📝 Phase 2: Writing (April 1 — May 10)</div>
    <ul class="cl-list">
      <li><input type="checkbox" id="c9"><label for="c9">Read official questions carefully on April 1</label></li>
      <li><input type="checkbox" id="c10"><label for="c10">Choose your final question within 24 hours</label></li>
      <li><input type="checkbox" id="c11"><label for="c11">Write 3 possible thesis statements; choose the strongest</label></li>
      <li><input type="checkbox" id="c12"><label for="c12">Create a detailed outline (section by section)</label></li>
      <li><input type="checkbox" id="c13"><label for="c13">Get outline feedback from teacher/mentor</label></li>
      <li><input type="checkbox" id="c14"><label for="c14">Complete first draft (~2,000 words)</label></li>
      <li><input type="checkbox" id="c15"><label for="c15">Check: does every paragraph advance the thesis?</label></li>
      <li><input type="checkbox" id="c16"><label for="c16">Check: have you engaged with the strongest counterargument?</label></li>
      <li><input type="checkbox" id="c17"><label for="c17">Submit to secondary competition by May 10</label></li>
    </ul>
  </div>
  <div class="card">
    <div class="ct">🏁 Phase 3: Final Polish (May 11 — May 31)</div>
    <ul class="cl-list">
      <li><input type="checkbox" id="c18"><label for="c18">Incorporate feedback from secondary competition</label></li>
      <li><input type="checkbox" id="c19"><label for="c19">Read essay aloud — fix any awkward sentences</label></li>
      <li><input type="checkbox" id="c20"><label for="c20">Verify all citations are accurate and properly formatted</label></li>
      <li><input type="checkbox" id="c21"><label for="c21">Check word count is within limits</label></li>
      <li><input type="checkbox" id="c22"><label for="c22">Get a final proofread from someone else</label></li>
      <li><input type="checkbox" id="c23"><label for="c23">Submit before May 31 deadline — confirm receipt</label></li>
    </ul>
  </div>
</div>

</main>
<script>
function toggleNav(){
  var nav=document.getElementById('sidenav');
  var btn=document.getElementById('hbtn');
  var ov=document.getElementById('overlay');
  nav.classList.toggle('open');
  btn.classList.toggle('open');
  ov.classList.toggle('on');
}
function go(id){
  document.querySelectorAll('.pg').forEach(function(p){p.classList.remove('on')});
  var el=document.getElementById('pg-'+id);
  if(el)el.classList.add('on');
  document.querySelectorAll('.ni').forEach(function(n){n.classList.remove('active')});
  event.target.classList.add('active');
  if(window.innerWidth<=768){
    var nav=document.getElementById('sidenav');
    var btn=document.getElementById('hbtn');
    var ov=document.getElementById('overlay');
    nav.classList.remove('open');
    btn.classList.remove('open');
    ov.classList.remove('on');
  }
}
function tab(el,id){
  var pg=el.closest('.pg');
  if(!pg)return;
  pg.querySelectorAll('.tc').forEach(function(t){t.classList.remove('on')});
  pg.querySelectorAll('.tab').forEach(function(t){t.classList.remove('on')});
  var target=document.getElementById(id);
  if(target)target.classList.add('on');
  el.classList.add('on');
}
(function(){
  var dates=[new Date('2026-04-01'),new Date('2026-05-10'),new Date('2026-05-31')];
  var ids=['dq','ds','dd'];
  var now=new Date();
  dates.forEach(function(d,i){
    var diff=Math.ceil((d-now)/86400000);
    var el=document.getElementById(ids[i]);
    if(el)el.textContent=diff>0?diff:'PASSED';
  });
})();
</script>
</body>
</html>
'''

if __name__ == "__main__":
    print(get_app_footer())
    print("Part 11 (Footer) ready")