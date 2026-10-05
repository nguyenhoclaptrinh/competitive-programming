#!/usr/bin/env python3
"""Template dùng chung cho slides.html mọi bài: CSS + JS core (audio, autosync, steps engine)."""
CSS = """*{box-sizing:border-box}
body{margin:0;font-family:"Segoe UI",Roboto,"Noto Sans",Arial,sans-serif;background:#0f172a;color:#e2e8f0;line-height:1.65}
#progress-bar{position:fixed;top:0;left:0;height:4px;background:linear-gradient(90deg,#0ea5e9,#38bdf8,#a855f7);width:0%;z-index:99;transition:width 0.2s}
header{padding:12px 20px;background:#020617;border-bottom:1px solid #1e293b;display:flex;gap:16px;align-items:center;flex-wrap:wrap;position:sticky;top:0;z-index:10}
header h1{font-size:16px;margin:0;color:#f8fafc}
header p{margin:2px 0 0;font-size:12.5px;color:#94a3b8}
.audio-panel{display:flex;flex-direction:column;gap:5px;flex:1;min-width:280px}
.audio-ctrls{display:flex;align-items:center;gap:10px}
audio{height:32px;flex:1}
.speed-group{display:flex;gap:4px;align-items:center}
.btn-xs{background:#1e293b;border:1px solid #475569;color:#94a3b8;font-size:11px;padding:3px 7px;border-radius:6px;cursor:pointer;font-weight:600}
.btn-xs:hover,.btn-xs.active{background:#0ea5e9;color:#02131f;border-color:#0ea5e9}
main{max-width:1020px;margin:0 auto;padding:18px}
.slide{display:none;background:#1e293b;border:1px solid #334155;border-radius:16px;padding:26px;margin-bottom:14px}
.slide.active{display:block}
.slide h2{margin:0 0 6px;font-size:21px;color:#7dd3fc}
.sub{color:#94a3b8;font-size:13.5px;margin-bottom:14px}
.slide p{font-size:15px;margin:8px 0}
.slide ul,.slide ol{font-size:14.5px;margin:8px 0;padding-left:22px}
code{background:#020617;padding:2px 7px;border-radius:6px;color:#7dd3fc;font-size:13.5px;border:1px solid #1e293b}
pre{background:#020617;border-radius:10px;padding:14px;overflow:auto;font-size:13.5px;line-height:1.6;border:1px solid #334155}
.code-header{display:flex;justify-content:space-between;align-items:center;background:#0f172a;padding:8px 14px;border-radius:10px 10px 0 0;border:1px solid #334155;border-bottom:0;font-size:12px;color:#94a3b8}
.code-header+pre{border-top-left-radius:0;border-top-right-radius:0;margin-top:0}
.copy-btn{background:#334155;color:#e2e8f0;border:0;padding:4px 10px;border-radius:6px;font-size:11.5px;cursor:pointer;font-weight:600}
.kw{color:#f472b6;font-weight:700}.type{color:#38bdf8;font-weight:600}.fn{color:#a78bfa;font-weight:600}.com{color:#64748b;font-style:italic}.num{color:#fbbf24}
table{border-collapse:collapse;width:100%;margin:12px 0;font-size:14px}
th,td{border:1px solid #475569;padding:8px 9px;text-align:center}
th{background:#020617;color:#7dd3fc}
td.hl{background:#164e63;font-weight:700;color:#fff}
.grid8{display:grid;grid-template-columns:repeat(8,1fr);gap:6px;margin:12px 0}
.grid6{display:grid;grid-template-columns:repeat(6,1fr);gap:6px;margin:12px 0}
.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:12px 0}
.cell{background:#020617;border:1px solid #475569;border-radius:10px;padding:8px 4px;text-align:center;transition:all 0.2s}
.cell .idx{font-size:11px;color:#94a3b8}
.cell .val{font-size:19px;font-weight:800}
.cell.hit{background:#b45309;border-color:#f59e0b}
.cell.hit2{background:#166534;border-color:#22c55e}
.cell .note{font-size:11px;color:#fde68a}
.gcell{background:#020617;border:1px solid #475569;border-radius:8px;padding:10px 2px;text-align:center;font-weight:800;font-size:16px}
.gcell.hit{background:#b45309;border-color:#f59e0b}
.gcell.hit2{background:#166534;border-color:#22c55e}
.cover{border-radius:10px;padding:10px 12px;margin:8px 0;font-size:14px;border:1px solid #475569;background:#020617}
.cover b{color:#fbbf24}
svg.tree{width:100%;height:auto;background:#020617;border-radius:10px;border:1px solid #334155}
.steps{background:#020617;border-radius:10px;padding:13px;min-height:90px;font-size:14.5px;border:1px solid #334155}
.nav{display:flex;gap:10px;align-items:center;justify-content:center;margin:10px 0 26px}
button{background:#0ea5e9;border:0;color:#02131f;font-weight:700;padding:9px 16px;border-radius:9px;cursor:pointer;font-size:14px}
button.ghost{background:#334155;color:#e2e8f0}
#idx{font-size:14px;color:#94a3b8;font-weight:600}
.warn{background:#450a0a;border:1px solid #ef4444;border-radius:10px;padding:13px;font-size:14.5px}
.tip{background:#052e16;border:1px solid #22c55e;border-radius:10px;padding:13px;font-size:14.5px;margin-top:10px}
.formula{background:#082f49;border:1px solid #0ea5e9;border-radius:10px;padding:12px;font-size:15px;margin:10px 0}
kbd{background:#020617;border:1px solid #475569;border-radius:6px;padding:1px 7px;font-size:12px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:12px}
@media(max-width:700px){.two{grid-template-columns:1fr}}
.pill{display:inline-block;background:#0ea5e9;color:#02131f;font-weight:700;font-size:12px;border-radius:20px;padding:2px 10px;margin-right:6px}
.quiz-card{background:#020617;border:1px solid #334155;border-radius:10px;padding:12px 16px;margin:10px 0}
.quiz-q{font-weight:700;color:#f8fafc;display:flex;justify-content:space-between;align-items:center;gap:8px}
.quiz-ans{display:none;margin-top:10px;padding-top:10px;border-top:1px dashed #334155;color:#86efac;font-size:14px}
.quiz-ans.open{display:block}"""

CORE_JS = """let cur=0;
const slides=[...document.querySelectorAll('.slide')];
const progressBar=document.getElementById('progress-bar');
function show(i){cur=(i+slides.length)%slides.length;slides.forEach((s,k)=>s.classList.toggle('active',k===cur));document.getElementById('idx').textContent=(cur+1)+' / '+slides.length;window.scrollTo(0,0);}
function go(d){show(cur+d);}
const audioEl=document.querySelector('audio');
const chkAutoSync=document.getElementById('chkAutoSync');
document.addEventListener('keydown',e=>{
  if(e.target.tagName==='INPUT')return;
  if(e.key==='ArrowRight')go(1);
  if(e.key==='ArrowLeft')go(-1);
  if(e.code==='Space'){e.preventDefault();if(audioEl)audioEl.paused?audioEl.play():audioEl.pause();}
  if(e.key.toLowerCase()==='n'){const b=document.querySelector('.slide.active [data-next]');if(b)b.click();}
});
function setSpeed(rate){if(audioEl)audioEl.playbackRate=rate;document.querySelectorAll('.speed-group button').forEach(b=>b.classList.remove('active'));event.target.classList.add('active');}
function toggleAns(i){const el=document.getElementById('ans'+i);if(el)el.classList.toggle('open');}
function copyCode(id,btn){const pre=document.getElementById(id);const txt=pre?pre.innerText:'';const done=()=>{btn.textContent='✅ Đã sao chép!';setTimeout(()=>{btn.textContent='📋 Sao chép mã C++';},2000);};const fb=()=>{const ta=document.createElement('textarea');ta.value=txt;ta.style.position='fixed';ta.style.opacity='0';document.body.appendChild(ta);ta.select();try{if(document.execCommand('copy'))done();else alert('Trình duyệt chặn sao chép — hãy Ctrl+C thủ công.');}catch(e){alert('Trình duyệt chặn sao chép — hãy Ctrl+C thủ công.');}ta.remove();};if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(txt).then(done).catch(fb);}else{fb();}}
const slideStarts=/*__CUES__*/[];
if(audioEl){audioEl.addEventListener('timeupdate',()=>{if(audioEl.duration&&progressBar){progressBar.style.width=((audioEl.currentTime/audioEl.duration)*100)+'%';}if(!chkAutoSync||!chkAutoSync.checked)return;const t=audioEl.currentTime;let target=0;for(let k=0;k<slideStarts.length;k++){if(t>=slideStarts[k])target=k;}if(target!==cur){show(target);}});}
// Step engine: ST = {key:{steps:[{cap,run}], i, capId}}
const ST={};
function defSteps(key,capId,steps,startCap){ST[key]={steps:steps,i:0,capId:capId,startCap:startCap};}
function nextStep(key){const S=ST[key];if(!S)return;if(S.i<S.steps.length){const st=S.steps[S.i++];try{st.run();}catch(e){}document.getElementById(S.capId).innerHTML=st.cap+(S.i>=S.steps.length?'<br>✅ <b>Xong.</b>':'');}}
function resetSteps(key){const S=ST[key];if(!S)return;S.i=0;try{S.reset();}catch(e){}document.getElementById(S.capId).innerHTML=S.startCap;}
// Bars: vals=[{v,l}], S={h:{idx:cls}}
function drawBars(id,vals,S){const el=document.getElementById(id);if(!el)return;el.innerHTML='';S=S||{h:{}};vals.forEach((c,i)=>{const d=document.createElement('div');d.className='cell'+(S.h[i]?' '+S.h[i]:'');d.innerHTML='<div class="idx">'+(c.l||('['+(i+1)+']'))+'</div><div class="val">'+c.v+'</div>'+(c.n?'<div class="note">'+c.n+'</div>':'');el.appendChild(d);});}
// Grid 4x4: rows=[[..]], S={h:{"r,c":cls}}
function drawGrid(id,rows,S){const el=document.getElementById(id);if(!el)return;el.innerHTML='';S=S||{h:{}};const m=rows[0].length;el.style.display='grid';el.style.gridTemplateColumns='repeat('+m+',1fr)';el.style.gap='8px';el.style.margin='12px 0';rows.forEach((row,r)=>{row.forEach((v,c)=>{const d=document.createElement('div');const k=r+','+c;d.className='gcell'+(S.h[k]?' '+S.h[k]:'');d.textContent=v;el.appendChild(d);});});}
// Net graph: N=[{id,x,y,l}], E=[{a,b,l}], S={hn:[],he:[],el:{},nl:{}}
function drawNet(id,N,E,S){const el=document.getElementById(id);if(!el)return;S=S||{hn:[],he:[],el:{},nl:{}};let h='';E.forEach((e,i)=>{const A=N.find(n=>n.id===e.a),B=N.find(n=>n.id===e.b);const hi=S.he.indexOf(i)>=0;const col=hi?'#f59e0b':'#475569';const lbl=(i in S.el)?S.el[i]:(e.l||'');h+='<line x1="'+A.x+'" y1="'+A.y+'" x2="'+B.x+'" y2="'+B.y+'" stroke="'+col+'" stroke-width="'+(hi?3:2)+'"/>';if(lbl){h+='<text x="'+((A.x+B.x)/2)+'" y="'+((A.y+B.y)/2-6)+'" fill="'+(hi?'#fbbf24':'#94a3b8')+'" font-size="12" text-anchor="middle" font-weight="bold">'+lbl+'</text>';}});N.forEach(n=>{const hi=S.hn.indexOf(n.id)>=0;h+='<circle cx="'+n.x+'" cy="'+n.y+'" r="20" fill="'+(hi?'#f59e0b':'#0ea5e9')+'"/>';h+='<text x="'+n.x+'" y="'+(n.y+5)+'" fill="#02131f" font-size="14" text-anchor="middle" font-weight="bold">'+((n.id in S.nl)?S.nl[n.id]:n.l)+'</text>';});el.innerHTML=h;}"""

HEADER = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<style>__CSS__</style>
</head>
<body>
<div id="progress-bar"></div>
<header>
<div style="flex:2;min-width:260px">
<h1>__H1__</h1>
<p>Dùng phím ← → hoặc Trước/Sau. Space dừng/phát. Phím N chạy bước tiếp theo.</p>
</div>
<div class="audio-panel">
<div class="audio-ctrls">
<audio controls src="audio.mp3" preload="metadata"></audio>
<div class="speed-group">
<button class="btn-xs" onclick="setSpeed(0.75)">0.75x</button>
<button class="btn-xs active" onclick="setSpeed(1.0)">1.0x</button>
<button class="btn-xs" onclick="setSpeed(1.25)">1.25x</button>
<button class="btn-xs" onclick="setSpeed(1.5)">1.5x</button>
</div>
</div>
<label style="display:flex;align-items:center;gap:6px;font-size:12px;color:#7dd3fc;cursor:pointer;user-select:none">
<input type="checkbox" id="chkAutoSync" checked style="cursor:pointer;accent-color:#0ea5e9"> Tự động chuyển slide theo Audio (Auto-Sync)
</label>
</div>
</header>
<main>
"""

FOOTER = """<div class="nav">
<button class="ghost" onclick="go(-1)">← Trước</button>
<span id="idx">1 / __N__</span>
<button onclick="go(1)">Sau →</button>
</div>
</main>
<script>__CORE__
__CUSTOM__
</script>
</body>
</html>
"""


def build_page(title, h1, sections, custom_js, n):
    s = HEADER.replace("__TITLE__", title).replace("__H1__", h1).replace("__CSS__", CSS)
    s += "\n".join(sections)
    f = FOOTER.replace("__N__", str(n)).replace("__CORE__", CORE_JS).replace("__CUSTOM__", custom_js)
    return s + f


def section(h2, sub, body):
    return '<section class="slide">\n<h2>' + h2 + '</h2>\n<div class="sub">' + sub + '</div>\n' + body + '\n</section>'


def quiz(qid, q, ans):
    return ('<div class="quiz-card"><div class="quiz-q"><span>❓ <b>Câu ' + str(qid) +
            ':</b> ' + q + '</span><button class="btn-xs" onclick="toggleAns(' + str(qid) +
            ')">Xem đáp án</button></div><div class="quiz-ans" id="ans' + str(qid) + '">' + ans + '</div></div>')


def code_block(cid, label, code_html):
    return ('<div class="code-header"><span>' + label + '</span>' +
            '<button class="copy-btn" onclick="copyCode(\'' + cid + '\',this)">📋 Sao chép mã C++</button></div>' +
            '<pre id="' + cid + '">' + code_html + '</pre>')


def stepper_btns(key):
    return ('<p><button data-next onclick="nextStep(\'' + key + '\')">Next bước</button> ' +
            '<button class="ghost" onclick="resetSteps(\'' + key + '\')">Chạy lại</button></p>')
