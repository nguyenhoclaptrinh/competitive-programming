#!/usr/bin/env python3
"""Spec bài 11: Manacher + Aho-Corasick."""
from template import section, quiz, code_block, stepper_btns

SLUG = "11-string"
TITLE = "Bài 10: Xâu ký tự — Hiểu sâu qua hình + tiếng"
H1 = "Bài 10: Manacher O(N) + Aho-Corasick đa mẫu"

S1 = section("1/8 — Manacher: chèn # biến mọi thứ thành lẻ", "s=abba → t=^#a#b#b#a#$, tâm # là palindrome chẵn",
"""<p>Palindrome lẻ tâm tại ký tự, chẵn tâm giữa 2 ký tự. Chèn <code>#</code> + lính canh <code>^ $</code>: mọi palindrome thành <b>lẻ</b> trên t. <code>P[i]</code> = bán kính = độ dài thực.</p>
<div class="grid8" id="t1"></div>
<div class="formula">Tâm tại ký tự → palindrome lẻ. Tâm tại <code>#</code> → palindrome chẵn. <code>^ $</code> chặn tràn biên.</div>""")

S2 = section("2/8 — Đối xứng C,R: kế thừa rồi mở rộng", "Bấm Next: i phẩy = 2C−i, P[i] ≥ min(R−i, P[i'])",
"""<div class="grid8" id="t2"></div>
<div class="cover" id="cov2">Duy trì C (tâm xa nhất), R (biên phải). Bấm Next quét i.</div>
<div class="steps" id="cap2">R chỉ tăng đơn điệu → tổng so sánh ≤ 2N.</div>
""" + stepper_btns("s2"))

S3 = section("3/8 — Code Manacher + ứng dụng", "while mở rộng + cập nhật C,R",
code_block("code11a", "C++20 · manacher", """<span class="type">vector</span>&lt;<span class="type">int</span>&gt; <span class="fn">manacher</span>(<span class="kw">const</span> <span class="type">string</span>& s){
  <span class="type">string</span> t=<span class="str">"^"</span>; <span class="kw">for</span>(c:s){t+=<span class="str">'#'</span>;t+=c;} t+=<span class="str">"#$"</span>;
  <span class="type">vector</span>&lt;<span class="type">int</span>&gt; p(m,<span class="num">0</span>); <span class="type">int</span> c=<span class="num">0</span>,r=<span class="num">0</span>;
  <span class="kw">for</span>(i){ <span class="type">int</span> mir=<span class="num">2</span>*c-i; <span class="kw">if</span>(r&gt;i)p[i]=<span class="fn">min</span>(r-i,p[mir]);
    <span class="kw">while</span>(t[i+<span class="num">1</span>+p[i]]==t[i-<span class="num">1</span>-p[i]])p[i]++;
    <span class="kw">if</span>(i+p[i]&gt;r){c=i;r=i+p[i];} } <span class="kw">return</span> p; }""") + """
<div class="tip">Ứng dụng: palindrome dài nhất, đếm palindrome con, kiểm tra substring O(1).</div>""")

S4 = section("4/8 — Aho-Corasick: Trie + failure link", "link = hậu tố dài nhất cũng là tiền tố mẫu",
"""<p>Pattern {"ab","bc"} trên text "abc". Trie rồi BFS dựng fail. Không có cạnh c → <code>next[fail][c]</code> (DFA hoàn thiện, mỗi ký tự đúng 1 bước).</p>
<svg class="tree" id="a4" viewBox="0 0 500 200"></svg>
<div class="cover" id="cov4">Fail("ab") = node "b" (hậu tố "b" là tiền tố pattern "bc"). Bấm Next duyệt text.</div>
<div class="steps" id="cap4">Đọc 'a' → node "a".</div>
""" + stepper_btns("s4"))

S5 = section("5/8 — Code Aho + search", "insert + build BFS + search O(text+match)",
code_block("code11b", "C++20 · AhoCorasick", """<span class="type">void</span> <span class="fn">build</span>(){ <span class="type">queue</span>&lt;<span class="type">int</span>&gt; q; <span class="com">// BFS từ con root</span>
  <span class="kw">while</span>(!q.<span class="fn">empty</span>()){u=q.<span class="fn">front</span>();q.<span class="fn">pop</span>();f=link[u];
    exitLink[u]=out[f].<span class="fn">empty</span>()?exitLink[f]:f;
    <span class="kw">for</span>(c){ <span class="kw">if</span>(next[u][c]){link[next]=next[f][c];q.<span class="fn">push</span>(next);}
      <span class="kw">else</span> next[u][c]=next[f][c]; } } } <span class="com">// DFA: không while lùi</span>""") + """
<div class="formula">📌 <b>Tóm tắt 30 giây:</b> Manacher = # + đối xứng C,R · Aho = Trie + fail + DFA.</div>""")

S6 = section("6/8 — Bẫy ICPC xâu", "Biên, alphabet, exitLink",
"""<ul><li>Manacher: t dài 2n+3, <code>^ $</code> chặn tràn; p[i] có thể 0.</li>
<li>Aho: ALPHABET đúng (26/52/128). link root = 0, exitLink = 0 nếu fail không output.</li>
<li>Chuỗi exitLink dài → mỗi match O(k). Tổng O(text + matches).</li></ul>""")

S7 = section("7/8 — Ứng dụng nâng cao", "Hash, Aho trên cây, đa alphabet",
"""<ul><li>Manacher + hash: palindrome substring O(1).</li>
<li>Aho trên cây: DFS giữ state Aho, tìm pattern trên đường đi.</li>
<li>Đa alphabet: nén char→id hoặc unordered_map next.</li></ul>""")

S8 = section("8/8 — Tự kiểm tra 3 câu", "Đáp án đã kiểm chứng bằng code",
quiz(1, 's="aba". Tâm b (i=4), P[4] = ?', "✅ <b>3</b> — mở rộng #,a,# rồi kẹt $/^ (độ dài thực 3).") +
quiz(2, 'Pattern ["ab","bc"], text "abc". Match ở đâu?', "✅ <b>ab kết thúc index 1, bc kết thúc index 2</b>.") +
quiz(3, 'Fail link của node ab là gì?', "✅ <b>Node 'b'</b> — hậu tố dài nhất cũng là tiền tố mẫu.") + """
<div class="formula">🎯 <b>Bài tiếp theo (Bài 11):</b> Số học — nCr, CRT, Pollard Rho.</div>""")

CUSTOM_JS = """
const T1=['^','#','a','#','b','#','b','#','a','#','$'];
function drawT(id,hi){const el=document.getElementById(id);el.innerHTML='';el.style.display='grid';el.style.gridTemplateColumns='repeat(11,1fr)';el.style.gap='4px';el.style.margin='12px 0';T1.forEach((c,i)=>{const d=document.createElement('div');d.className='gcell'+(hi&&hi[i]?' '+hi[i]:'');d.style.fontSize='14px';d.innerHTML='<div style="font-size:10px;color:#94a3b8">'+i+'</div>'+(c==='#'?'<span style="color:#64748b">#</span>':c);el.appendChild(d);});}
drawT('t1');drawT('t2');
defSteps('s2','cap2',[
 {cap:'<b>Tâm # tại i=5</b> ("abba"): t[6]=b==t[4]=b → P=1… mở rộng tới P=<b>4</b> (a,#,a,# đối xứng).',run:()=>{const h={};[1,2,3,4,5,6,7,8,9].forEach(i=>h[i]='hit');h[5]='hit2';drawT('t2',h);document.getElementById('cov2').innerHTML='P[5]=<b>4</b> → palindrome chẵn dài 4 "abba".';}},
 {cap:'<b>Kế thừa:</b> các i khác dùng i phẩy, chỉ mở rộng khi chạm R. R đơn điệu → <b>O(N)</b>.',run:()=>{document.getElementById('cov2').innerHTML='Tổng so sánh ≤ 2N vì R không bao giờ lùi.';}}
],'R chỉ tăng đơn điệu → tổng so sánh ≤ 2N.');
ST['s2'].reset=()=>{drawT('t2');document.getElementById('cov2').innerHTML='Duy trì C (tâm xa nhất), R (biên phải). Bấm Next quét i.';};
const AN=[{id:0,x:60,y:100,l:'root'},{id:1,x:200,y:50,l:'a'},{id:2,x:340,y:50,l:'ab*'},{id:3,x:200,y:150,l:'b'},{id:4,x:340,y:150,l:'bc*'}];
const AE=[{a:0,b:1,l:'a'},{a:1,b:2,l:'b'},{a:0,b:3,l:'b'},{a:3,b:4,l:'c'}];
drawNet('a4',AN,AE);
defSteps('s4','cap4',[
 {cap:"<b>Đọc 'a':</b> root→node a. Chưa output.",run:()=>{drawNet('a4',AN,AE,{hn:[0,1],he:[0]});document.getElementById('cov4').innerHTML="state=node a.";}},
 {cap:"<b>Đọc 'b':</b> node a→node ab. Output <b>ab kết thúc index 1</b>.",run:()=>{drawNet('a4',AN,AE,{hn:[0,1,2],he:[0,1]});document.getElementById('cov4').innerHTML="<b>Match ab @1</b>.";}},
 {cap:"<b>Đọc 'c':</b> ab không có cạnh c → fail về node b → node bc. Output <b>bc kết thúc index 2</b>.",run:()=>{drawNet('a4',AN,AE,{hn:[0,2,3,4],he:[1,3]});document.getElementById('cov4').innerHTML="<b>Match bc @2</b>. Đúng 1 bước/ký tự nhờ DFA.";}}
],"Đọc 'a' → node \\"a\\".");
ST['s4'].reset=()=>{drawNet('a4',AN,AE);document.getElementById('cov4').innerHTML='Fail("ab") = node "b" (hậu tố "b" là tiền tố pattern "bc"). Bấm Next duyệt text.';};
"""

MANIFEST = [
 ("Bài 10: Manacher O(N) + Aho-Corasick đa mẫu", "1/8 · chèn # thành lẻ, P[i]=bán kính", "abba tâm # P=4", "", ""),
 ("Đối xứng C,R: kế thừa min(R-i,P[i']) rồi mở rộng", "2/8 · R đơn điệu nên O(N)", "Mở slides.html Slide 2, bấm Next", "", ""),
 ("Code manacher + ứng dụng palindrome", "3/8 · while mở rộng + cập nhật C,R", "Dài nhất, đếm, substring", "", "while mở rộng // C,R đơn điệu // O(N)"),
 ("Aho: Trie + fail + DFA, duyệt abc match 2", "4/8 · fail(ab)=node b", "Mở slides.html Slide 4, bấm Next", "", ""),
 ("Code build BFS + search O(text+match)", "5/8 · exitLink chuỗi output", "Tóm tắt 30 giây cuối slide", "", "BFS fail // DFA hoàn thiện // exitLink"),
 ("Bẫy: biên ^$, alphabet, exitLink O(k)", "6/8 · p[i] có thể 0", "3 bẫy sống còn", "", "lính canh // alphabet đúng // exit O(k)"),
 ("Ứng dụng: hash, Aho trên cây, đa alphabet", "7/8 · DFS giữ state", "3 mở rộng", "", "hash O1 // cây DFS // nén char"),
 ("Quiz: P=3; match @1,@2; fail=b", "8/8 · đáp án kiểm chứng bằng code", "Tiếp theo: Số học", "", "P3 // @1@2 // fail b"),
]

SCRIPT_ROWS = [
 ("Manacher chèn #, P=bán kính", "Slide 1: chuỗi t + công thức"),
 ("Đối xứng C,R kế thừa + mở rộng", "Slide 2: hoạt hình Next 2 bước"),
 ("Code manacher + ứng dụng", "Slide 3: code"),
 ("Aho Trie+fail, duyệt abc", "Slide 4: trie + Next 3 bước"),
 ("Code build+search + tóm tắt", "Slide 5: code + recap"),
 ("3 bẫy xâu", "Slide 6: bẫy"),
 ("Hash, cây, đa alphabet", "Slide 7: mở rộng"),
 ("3 câu quiz có đáp án + bài tiếp theo", "Slide 8: quiz + outro"),
]
