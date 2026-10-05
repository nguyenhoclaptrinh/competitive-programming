#!/usr/bin/env python3
"""Spec bài 05: LCA Binary Lifting + 2-SAT."""
from template import section, quiz, code_block, stepper_btns

SLUG = "05-topo-lca"
TITLE = "Bài 5: LCA + 2-SAT — Hiểu sâu qua hình + tiếng"
H1 = "Bài 5: LCA Binary Lifting (BFS) + 2-SAT mệnh đề"

TREE_N = "[{id:1,x:280,y:30,l:'1'},{id:2,x:140,y:95,l:'2'},{id:3,x:420,y:95,l:'3'},{id:4,x:70,y:170,l:'4'},{id:5,x:210,y:170,l:'5'},{id:6,x:350,y:170,l:'6'},{id:7,x:490,y:170,l:'7'}]"
TREE_E = "[{a:1,b:2,l:''},{a:1,b:3,l:''},{a:2,b:4,l:''},{a:2,b:5,l:''},{a:3,b:6,l:''},{a:3,b:7,l:''}]"
SAT_N = "[{id:0,x:90,y:90,l:'x1'},{id:1,x:250,y:30,l:'¬x1'},{id:2,x:250,y:150,l:'x2'},{id:3,x:410,y:90,l:'¬x2'}]"
SAT_E = "[{a:1,b:2,l:'¬x1→x2'},{a:3,b:0,l:'¬x2→x1'},{a:0,b:2,l:'x1→x2'},{a:1,b:3,l:'¬x1→¬x2'},{a:2,b:0,l:'x2→x1'}]"

S1 = section("1/8 — LCA: cấm DFS đệ quy, dùng BFS", "n = 3·10⁵ đường thẳng → Stack Overflow",
"""<p><code>LCA(u,v)</code> = tổ tiên chung sâu nhất. Bảng nhảy <code>up[j][u]</code> = tổ tiên cấp 2<sup>j</sup>: <code>up[j][u] = up[j−1][up[j−1][u]]</code>.</p>
<div class="formula">BFS từ gốc tính <code>depth</code> + <code>up[0]</code>. LOG = 31 − clz(n) + 1. Build O(n log n).</div>
<div class="warn">⛔ DFS đệ quy 3·10⁵ tầng là đi luôn. BFS queue an toàn 100%.</div>""")

S2 = section("2/8 — LCA(4,7) step-by-step", "Bấm Next: cân depth rồi nhảy từ lớn về nhỏ",
"""<svg class="tree" id="t5" viewBox="0 0 560 210"></svg>
<div class="cover" id="cov2">depth: 4 và 7 đều = 2, khỏi cân. Bấm Next từng bước nhảy j.</div>
<div class="steps" id="cap2">j=1: up[1][4]=1, up[1][7]=1.</div>
""" + stepper_btns("s2"))

S3 = section("3/8 — distance + kiểm tra tổ tiên", "distance(u,v) = depth[u]+depth[v]−2·depth[lca]",
"""<p>Ví dụ: distance(4,7) = 2+2−2·0 = <b>4</b> (4→2→1→3→7).</p>
<ul><li>u là tổ tiên của v ⟺ <code>getLCA(u,v) == u</code>.</li>
<li>Trọng số đường đi: lưu thêm distRoot, đáp = distRoot[u]+distRoot[v]−2·distRoot[lca].</li>
<li>Ứng dụng: đường đi trên cây, jump pointer, centroid.</li></ul>""")

S4 = section("4/8 — 2-SAT: mệnh đề thành đồ thị suy diễn", "Mỗi (u∨v) → 2 cạnh: ¬u→v, ¬v→u",
"""<p>2 nút/biến: <code>2i</code> = x<sub>i</sub>, <code>2i+1</code> = ¬x<sub>i</sub>. Ví dụ 3 mệnh đề: (x1∨x2) ∧ (¬x1∨x2) ∧ (x1∨¬x2).</p>
<svg class="tree" id="t4" viewBox="0 0 500 190"></svg>
<div class="cover" id="cov4">5 cạnh suy diễn. Bấm Next để chạy Tarjan SCC.</div>
<div class="steps" id="cap4">Tarjan DFS tìm low-link.</div>
""" + stepper_btns("s4"))

S5 = section("5/8 — Code C++20 LCA + 2-SAT", "BFS + bảng up; Tarjan low-link",
code_block("code5", "C++20 · TreeLCA + TwoSat", """<span class="com">// BFS tính depth + up[0]; up[j][i]=up[j-1][up[j-1][i]]</span>
<span class="type">int</span> <span class="fn">getLCA</span>(<span class="type">int</span> u,<span class="type">int</span> v){ <span class="com">// cân depth rồi nhảy j lớn→nhỏ</span>
  <span class="kw">if</span>(up[j][u]!=up[j][v]){u=up[j][u];v=up[j][v];} <span class="kw">return</span> up[<span class="num">0</span>][u]; }
<span class="com">// 2-SAT: addClause thêm 2 cạnh; solve: Tarjan + gán theo topo ngược</span>
<span class="type">void</span> <span class="fn">addClause</span>(u,valU,v,valV){ adj[negU].<span class="fn">push_back</span>(nodeV);
  adj[negV].<span class="fn">push_back</span>(nodeU); }""") + """
<div class="formula">📌 <b>Tóm tắt 30 giây:</b> LCA = BFS + nhảy nhị phân · 2-SAT = mệnh đề→cạnh + SCC + topo ngược.</div>""")

S6 = section("6/8 — Bẫy ICPC", "LOG, Tarjan low, index biến",
"""<ul><li>LCA 1-based; LOG = 31 − clz(n) + 1 (≈20 với n = 3·10⁵).</li>
<li>Tarjan: nút chưa thăm → dfs rồi <code>min(low con)</code>; nút trong stack → <code>min(dfn)</code>. Đảo 2 nhánh là sai.</li>
<li>2-SAT biến 0..n−1, node = 2·i + (val?0:1). Vô nghiệm ⟺ <code>scc[2i] == scc[2i+1]</code>.</li></ul>""")

S7 = section("7/8 — Ứng dụng 2-SAT + LCA nâng cao", "Scheduling, 2-color, jump",
"""<ul><li>2-SAT: lịch thi (2 khung giờ), tô 2 màu ràng buộc, mở khóa logic game.</li>
<li>LCA + distRoot: trọng số đường đi, k-th ancestor (nhảy bit của k).</li>
<li>Kết hợp: LCA trên cây DFS của đồ thị (bridge, articulation).</li></ul>""")

S8 = section("8/8 — Tự kiểm tra 3 câu", "Đáp án đã kiểm chứng bằng code",
quiz(1, "Cây đường thẳng 1−2−3−4−5. LCA(4,5)?", "✅ <b>4</b> — 4 là tổ tiên của 5 (lca(u,v)==u).") +
quiz(2, "(x1∨x2) ∧ (¬x1∨¬x2) có nghiệm?", "✅ <b>Có</b> — x1=true, x2=false (hoặc ngược lại).") +
quiz(3, "2-SAT vô nghiệm khi nào?", "✅ <b>x<sub>i</sub> và ¬x<sub>i</sub> cùng SCC</b> — scc[2i]==scc[2i+1].") + """
<div class="formula">🎯 <b>Bài tiếp theo (Bài 6):</b> Dinic Max Flow.</div>""")

CUSTOM_JS = """
drawNet('t5',""" + TREE_N + """,""" + TREE_E + """);
drawNet('t4',""" + SAT_N + """,""" + SAT_E + """);
defSteps('s2','cap2',[
 {cap:'<b>j=1:</b> up[1][4]=1, up[1][7]=1 — bằng nhau nên <b>KHÔNG nhảy</b>.',run:()=>{drawNet('t5',""" + TREE_N + """,""" + TREE_E + """,{hn:[4,7],nl:{4:'4',7:'7'}});document.getElementById('cov2').innerHTML='Nhảy 2 bậc cùng về gốc thì mất LCA → bỏ qua.';}},
 {cap:'<b>j=0:</b> up[0][4]=2 ≠ up[0][7]=3 → nhảy cả hai: u=2, v=3.',run:()=>{drawNet('t5',""" + TREE_N + """,""" + TREE_E + """,{hn:[4,7,2,3],he:[2,5]});document.getElementById('cov2').innerHTML='u=2, v=3 — ngay dưới LCA.';}},
 {cap:'<b>Kết quả:</b> LCA = up[0][2] = <b>1</b> ✓. distance(4,7) = 2+2−0 = 4.',run:()=>{drawNet('t5',""" + TREE_N + """,""" + TREE_E + """,{hn:[4,7,2,3,1],he:[2,5,0,1]});document.getElementById('cov2').innerHTML='LCA(4,7) = <b>1</b>.';}}
],'j=1: up[1][4]=1, up[1][7]=1.');
ST['s2'].reset=()=>{drawNet('t5',""" + TREE_N + """,""" + TREE_E + """);document.getElementById('cov2').innerHTML='depth: 4 và 7 đều = 2, khỏi cân. Bấm Next từng bước nhảy j.';};
defSteps('s4','cap4',[
 {cap:'<b>Bước 1:</b> Chu trình 0→2→0: x1 và x2 dính nhau → cùng SCC {0,2}.',run:()=>{drawNet('t4',""" + SAT_N + """,""" + SAT_E + """,{hn:[0,2],he:[2,4]});document.getElementById('cov4').innerHTML='SCC {x1,x2} — cùng nhau thì không sao.';}},
 {cap:'<b>Bước 2:</b> {¬x1}, {¬x2} riêng lẻ. x1 (0,1) khác SCC ✓, x2 (2,3) khác SCC ✓ → <b>CÓ nghiệm</b>.',run:()=>{drawNet('t4',""" + SAT_N + """,""" + SAT_E + """,{hn:[0,2,1,3],he:[2,4]});document.getElementById('cov4').innerHTML='Không biến nào dính với phủ định của nó.';}},
 {cap:'<b>Bước 3:</b> Gán topo ngược: x1=true, x2=true. Kiểm tra 3 mệnh đề đều T ✓.',run:()=>{drawNet('t4',""" + SAT_N + """,""" + SAT_E + """,{hn:[0,2],he:[2,4],nl:{0:'x1=T',2:'x2=T'}});document.getElementById('cov4').innerHTML='Nghiệm: x1=<b>true</b>, x2=<b>true</b>.';}}
],'Tarjan DFS tìm low-link.');
ST['s4'].reset=()=>{drawNet('t4',""" + SAT_N + """,""" + SAT_E + """);document.getElementById('cov4').innerHTML='5 cạnh suy diễn. Bấm Next để chạy Tarjan SCC.';};
"""

MANIFEST = [
 ("Bài 5: LCA Binary Lifting + 2-SAT mệnh đề logic", "1/8 · BFS thay DFS đệ quy, bảng up[j][u]", "n=3e5 đường thẳng gây Stack Overflow", "", ""),
 ("LCA(4,7)=1: j=1 không nhảy, j=0 nhảy về 2,3", "2/8 · cân depth rồi nhảy lớn về nhỏ", "Mở slides.html Slide 2, bấm Next", "", ""),
 ("distance=depth[u]+depth[v]-2depth[lca], kiểm tra tổ tiên", "3/8 · distance(4,7)=4 · lca==u là tổ tiên", "Ứng dụng jump pointer, trọng số", "", "dist=u+v-2lca // lca==u là tổ tiên // k-th ancestor"),
 ("2-SAT: mệnh đề thành 2 cạnh suy diễn", "4/8 · 2 nút/biến, Tarjan SCC", "Ví dụ 3 mệnh đề, 5 cạnh", "", ""),
 ("SCC {x1,x2}, nghiệm x1=T x2=T, kiểm tra đúng", "5/8 · khác SCC với phủ định là có nghiệm", "Mở slides.html Slide 4, bấm Next", "", ""),
 ("Code LCA BFS + up, TwoSat Tarjan", "6/8 · getLCA O log n, solve bool", "Tóm tắt 30 giây cuối slide", "", "BFS+up // Tarjan low-link // topo ngược gán"),
 ("Bẫy: LOG đủ lớn, Tarjan min đúng nhánh, index 0-based", "7/8 · scc[2i]==scc[2i+1] là vô nghiệm", "Đảo nhánh Tarjan là sai", "", "LOG=31-clz+1 // min đúng nhánh // 0-based"),
 ("Quiz: LCA(4,5)=4; SAT có nghiệm; cùng SCC là vô nghiệm", "8/8 · đáp án kiểm chứng bằng code", "Tiếp theo: Dinic Max Flow", "", "LCA45=4 // SAT ok // cùng SCC vô nghiệm"),
]

SCRIPT_ROWS = [
 ("LCA: cấm DFS đệ quy, BFS + bảng up[j][u]", "Slide 1: vấn đề + công thức bảng"),
 ("LCA(4,7)=1 qua 3 bước nhảy", "Slide 2: cây + hoạt hình Next"),
 ("distance, kiểm tra tổ tiên, ứng dụng", "Slide 3: công thức + ví dụ"),
 ("2-SAT: mệnh đề thành đồ thị suy diễn", "Slide 4: đồ thị 4 nút 5 cạnh"),
 ("Tarjan SCC + gán nghiệm topo ngược", "Slide 4b: hoạt hình Next 3 bước"),
 ("Code LCA + TwoSat + tóm tắt", "Slide 5-6: code + recap + bẫy"),
 ("Bẫy LOG, Tarjan, index + ứng dụng", "Slide 7: bẫy + mở rộng"),
 ("3 câu quiz có đáp án + bài tiếp theo", "Slide 8: quiz + outro"),
]
