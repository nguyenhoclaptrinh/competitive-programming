#!/usr/bin/env python3
"""Spec bài 08: Hopcroft-Karp."""
from template import section, quiz, code_block, stepper_btns

SLUG = "08-matching"
TITLE = "Bài 7: Hopcroft-Karp Matching — Hiểu sâu qua hình + tiếng"
H1 = "Bài 7: Hopcroft-Karp — ghép 2 phía O(E√V)"

HK_N = "[{id:1,x:80,y:40,l:'1'},{id:2,x:80,y:90,l:'2'},{id:3,x:80,y:140,l:'3'},{id:4,x:380,y:40,l:'4'},{id:5,x:380,y:90,l:'5'},{id:6,x:380,y:140,l:'6'}]"
HK_E = "[{a:1,b:4,l:''},{a:1,b:5,l:''},{a:2,b:5,l:''},{a:2,b:6,l:''},{a:3,b:6,l:''}]"
HK2_N = "[{id:1,x:60,y:30,l:'1'},{id:2,x:60,y:90,l:'2'},{id:3,x:60,y:150,l:'3'},{id:4,x:60,y:210,l:'4'},{id:5,x:400,y:30,l:'5'},{id:6,x:400,y:90,l:'6'},{id:7,x:400,y:150,l:'7'},{id:8,x:400,y:210,l:'8'}]"
HK2_E = "[{a:1,b:5,l:''},{a:1,b:6,l:''},{a:2,b:5,l:''},{a:2,b:7,l:''},{a:3,b:6,l:''},{a:3,b:8,l:''},{a:4,b:7,l:''},{a:4,b:8,l:''}]"

S1 = section("1/8 — Đường mở: đảo ngược là +1 cặp", "Kuhn tuần tự O(VE) vs HK theo lớp O(E√V)",
"""<p>Đường xen kẽ cạnh chưa/ghép đã ghép, 2 đầu chưa ghép. Đảo ngược → tăng đúng 1 cặp.</p>
<svg class="tree" id="m1" viewBox="0 0 460 190"></svg>
<div class="formula">Hopcroft-Karp: BFS tìm <b>tất cả đường mở NGẮN NHẤT cùng lúc</b>, DFS tăng đồng thời trên đường không giao nhau.</div>""")

S2 = section("2/8 — BFS phân tầng đến NIL", "Bấm Next: dist lan từ đỉnh chưa ghép",
"""<p><code>dist[0]</code> = khoảng cách đến NIL (đỉnh ảo). Chỉ mở rộng khi <code>dist[u] &lt; dist[0]</code>.</p>
<svg class="tree" id="m2" viewBox="0 0 460 190"></svg>
<div class="cover" id="cov2">Ban đầu chưa ghép gì. Bấm Next.</div>
<div class="steps" id="cap2">dist[1]=dist[2]=dist[3]=0.</div>
""" + stepper_btns("s2"))

S3 = section("3/8 — DFS ghép theo tầng", "Bấm Next: ghép 1-4, 2-5, 3-6",
"""<svg class="tree" id="m3" viewBox="0 0 460 190"></svg>
<div class="cover" id="cov3">Chỉ đi cạnh dist[pairV[v]] == dist[u]+1. Bấm Next từng cặp.</div>
<div class="steps" id="cap3">DFS(1): 1→4→NIL.</div>
""" + stepper_btns("s3"))

S4 = section("4/8 — Ví dụ 4×4: matching hoàn hảo", "Bấm Next: BFS 1 lớp rồi ghép 4 cặp",
"""<p>Trái 1..4, phải 5..8. Cạnh: 1-5,1-6,2-5,2-7,3-6,3-8,4-7,4-8.</p>
<svg class="tree" id="m4" viewBox="0 0 460 250"></svg>
<div class="cover" id="cov4">Bấm Next để ghép.</div>
<div class="steps" id="cap4">BFS: mọi đỉnh trái dist 0, NIL dist 1.</div>
""" + stepper_btns("s4"))

S5 = section("5/8 — Code chuẩn C++20", "bfs + dfs + maxMatching",
code_block("code8", "C++20 · HopcroftKarp", """<span class="type">bool</span> <span class="fn">bfs</span>(){ <span class="com">// dist[0]=NIL; chỉ mở dist[u]&lt;dist[0]</span>
  <span class="kw">for</span>(u) <span class="kw">if</span>(!pairU[u]){dist[u]=<span class="num">0</span>;q.<span class="fn">push</span>(u);} <span class="kw">else</span> dist[u]=INF;
  dist[<span class="num">0</span>]=INF; ... <span class="kw">return</span> dist[<span class="num">0</span>]!=INF; }
<span class="type">bool</span> <span class="fn">dfs</span>(u){ <span class="kw">if</span>(u!=<span class="num">0</span>){ <span class="kw">for</span>(v:adj[u])
  <span class="kw">if</span>(dist[pairV[v]]==dist[u]+<span class="num">1</span>&amp;&amp;<span class="fn">dfs</span>(pairV[v]))
   {pairV[v]=u;pairU[u]=v;<span class="kw">return true</span>;} dist[u]=INF;<span class="kw">return false</span>;}
  <span class="kw">return true</span>; }""") + """
<div class="formula">📌 <b>Tóm tắt 30 giây:</b> BFS tầng→NIL · DFS đúng tầng · lặp đến khi hết đường mở.</div>""")

S6 = section("6/8 — Min Vertex Cover (Kőnig) + Độc lập cực đại", "BFS từ trái chưa ghép: chưa ghép đi, đã ghép về",
"""<ul><li>Trái→phải: chỉ cạnh <b>chưa ghép</b>. Phải→trái: chỉ cạnh <b>đã ghép</b>.</li>
<li>Cover = trái <b>KHÔNG</b> tới được + phải <b>tới được</b>. |Cover| = |Matching|.</li>
<li>Độc lập cực đại = bù của Cover.</li></ul>""")

S7 = section("7/8 — Bẫy ICPC + Dinic tương đương", "Kích thước mảng, INF, hằng số",
"""<ul><li>pairU cỡ n+1, pairV cỡ m+1, dist cỡ n+1. 1-based dùng trực tiếp.</li>
<li>Dinic với source→trái→phải→sink cap 1 cũng O(E√V) — HK nhẹ hơn (không struct Edge).</li>
<li>DFS sâu ≤ √V nên đệ quy an toàn. INF = 1e9.</li></ul>""")

S8 = section("8/8 — Tự kiểm tra 3 câu", "Đáp án đã kiểm chứng bằng code",
quiz(1, "dist[0] là gì? dist[0]!=INF nghĩa là gì?", "✅ <b>Khoảng cách đến NIL</b> — khác INF nghĩa là tồn tại đường mở.") +
quiz(2, "Vì sao DFS chỉ đi khi dist[pairV[v]]==dist[u]+1?", "✅ <b>Chỉ theo đường mở NGẮN NHẤT</b> mà BFS vừa phân tầng.") +
quiz(3, "Min Vertex Cover = ?", "✅ <b>Trái KHÔNG tới được + phải tới được</b> qua BFS Kőnig.") + """
<div class="formula">🎯 <b>Bài tiếp theo (Bài 8):</b> Hình học — CCW, giao đoạn, điểm trong đa giác.</div>""")

CUSTOM_JS = """
drawNet('m1',""" + HK_N + """,""" + HK_E + """);
drawNet('m2',""" + HK_N + """,""" + HK_E + """);
drawNet('m3',""" + HK_N + """,""" + HK_E + """);
drawNet('m4',""" + HK2_N + """,""" + HK2_E + """);
defSteps('s2','cap2',[
 {cap:'<b>BFS:</b> 1,2,3 chưa ghép → dist 0. Hàng xóm phải đều về NIL → dist[0]=1. Có đường mở!',run:()=>{drawNet('m2',""" + HK_N + """,""" + HK_E + """,{hn:[1,2,3],nl:{1:'1:0',2:'2:0',3:'3:0'}});document.getElementById('cov2').innerHTML='dist[0]=<b>1</b> → tồn tại đường mở độ dài 1.';}}
],'dist[1]=dist[2]=dist[3]=0.');
ST['s2'].reset=()=>{drawNet('m2',""" + HK_N + """,""" + HK_E + """);document.getElementById('cov2').innerHTML='Ban đầu chưa ghép gì. Bấm Next.';};
defSteps('s3','cap3',[
 {cap:'<b>Cặp 1:</b> 1→4→NIL. Ghép 1-4.',run:()=>{drawNet('m3',""" + HK_N + """,""" + HK_E + """,{hn:[1,4],he:[0]});document.getElementById('cov3').innerHTML='pairU[1]=4, pairV[4]=1.';}},
 {cap:'<b>Cặp 2:</b> 2→5→NIL. Ghép 2-5.',run:()=>{drawNet('m3',""" + HK_N + """,""" + HK_E + """,{hn:[1,4,2,5],he:[0,3]});document.getElementById('cov3').innerHTML='pairU[2]=5, pairV[5]=2.';}},
 {cap:'<b>Cặp 3:</b> 3→6→NIL. Ghép 3-6. Matching=<b>3</b>.',run:()=>{drawNet('m3',""" + HK_N + """,""" + HK_E + """,{hn:[1,4,2,5,3,6],he:[0,3,4]});document.getElementById('cov3').innerHTML='Matching=<b>3</b> (tối đa).';}}
],'DFS(1): 1→4→NIL.');
ST['s3'].reset=()=>{drawNet('m3',""" + HK_N + """,""" + HK_E + """);document.getElementById('cov3').innerHTML='Chỉ đi cạnh dist[pairV[v]] == dist[u]+1. Bấm Next từng cặp.';};
defSteps('s4','cap4',[
 {cap:'<b>Ghép:</b> 1-5, 2-7 (bỏ 2-5 vì 5 đã có chủ? DFS thử 2→5: pairV[5]=1 đã ghép, dist[1]≠… → chuyển 2→7).',run:()=>{drawNet('m4',""" + HK2_N + """,""" + HK2_E + """,{hn:[1,5,2,7],he:[0,3]});document.getElementById('cov4').innerHTML='1-5, 2-7 đã ghép.';}},
 {cap:'<b>Ghép nốt:</b> 3-6, 4-8. Matching=<b>4 hoàn hảo</b>.',run:()=>{drawNet('m4',""" + HK2_N + """,""" + HK2_E + """,{hn:[1,5,2,7,3,6,4,8],he:[0,3,4,7]});document.getElementById('cov4').innerHTML='Matching=<b>4</b> hoàn hảo ✓.';}}
],'BFS: mọi đỉnh trái dist 0, NIL dist 1.');
ST['s4'].reset=()=>{drawNet('m4',""" + HK2_N + """,""" + HK2_E + """);document.getElementById('cov4').innerHTML='Bấm Next để ghép.';};
"""

MANIFEST = [
 ("Bài 7: Hopcroft-Karp — ghép 2 phía O(E√V)", "1/8 · đường mở đảo ngược +1 cặp", "Kuhn O(VE) vs HK theo lớp", "", ""),
 ("BFS phân tầng từ đỉnh chưa ghép đến NIL", "2/8 · dist[0]=1 là có đường mở", "Mở slides.html Slide 2, bấm Next", "", ""),
 ("DFS ghép 1-4, 2-5, 3-6 theo đúng tầng", "3/8 · dist[pairV]==dist[u]+1", "Mở slides.html Slide 3, bấm Next", "", ""),
 ("Ví dụ 4x4 matching hoàn hảo 4 cặp", "4/8 · BFS 1 lớp rồi ghép hết", "Mở slides.html Slide 4, bấm Next", "", ""),
 ("Code bfs+dfs+maxMatching", "5/8 · NIL=0, INF, 1-based", "Tóm tắt 30 giây cuối slide", "", "bfs tầng // dfs đúng tầng // lặp hết đường"),
 ("Min Vertex Cover Kőnig + độc lập cực đại", "6/8 · chưa ghép đi, đã ghép về", "Cover=trái không tới+phải tới", "", "trái-phải chưa ghép // phải-trái đã ghép // bù là độc lập"),
 ("Bẫy mảng, INF, Dinic tương đương", "7/8 · pairU n+1 pairV m+1", "HK nhẹ hơn Dinic", "", "mảng đủ cỡ // INF 1e9 // DFS an toàn"),
 ("Quiz: NIL, đúng tầng, Cover", "8/8 · đáp án kiểm chứng bằng code", "Tiếp theo: Hình học", "", "NIL tồn tại // đúng tầng // Cover Kőnig"),
]

SCRIPT_ROWS = [
 ("Đường mở đảo ngược +1, Kuhn vs HK", "Slide 1: đồ thị + công thức"),
 ("BFS phân tầng đến NIL", "Slide 2: hoạt hình Next"),
 ("DFS ghép 3 cặp theo tầng", "Slide 3: hoạt hình Next 3 bước"),
 ("Ví dụ 4x4 matching hoàn hảo", "Slide 4: hoạt hình Next 2 bước"),
 ("Code bfs+dfs+maxMatching", "Slide 5: code + recap"),
 ("Min Cover Kőnig + độc lập", "Slide 6: quy tắc BFS"),
 ("Bẫy mảng, INF, Dinic", "Slide 7: bẫy"),
 ("3 câu quiz có đáp án + bài tiếp theo", "Slide 8: quiz + outro"),
]
