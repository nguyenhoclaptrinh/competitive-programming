#!/usr/bin/env python3
"""Spec bài 03: DSU + Sparse Table."""
from template import section, quiz, code_block, stepper_btns

SLUG = "03-dsu-sparse"
TITLE = "Bài 3: DSU + Sparse Table — Hiểu sâu qua hình + tiếng"
H1 = "Bài 3: DSU nén đường đi + Sparse Table RMQ O(1)"

P0 = "[{v:-1,l:'1'},{v:-1,l:'2'},{v:-1,l:'3'},{v:-1,l:'4'},{v:-1,l:'5'},{v:-1,l:'6'},{v:-1,l:'7'},{v:-1,l:'8'}]"
P1 = "[{v:-2,l:'1'},{v:1,l:'2'},{v:-1,l:'3'},{v:-1,l:'4'},{v:-1,l:'5'},{v:-1,l:'6'},{v:-1,l:'7'},{v:-1,l:'8'}]"
P2 = "[{v:-3,l:'1'},{v:1,l:'2'},{v:1,l:'3'},{v:-1,l:'4'},{v:-1,l:'5'},{v:-1,l:'6'},{v:-1,l:'7'},{v:-1,l:'8'}]"

S1 = section("1/8 — DSU: gộp tập hợp trong O(1) gần như tuyệt đối", "unite + same với 1 mảng parentOrSize",
"""<p>n = 8 phần tử. <code>unite(1,2), unite(2,3), unite(5,6)</code>. Hỏi <code>same(1,3)</code>? true. <code>same(1,5)</code>? false.</p>
<div class="formula">Một mảng duy nhất: <b>âm = gốc</b> (cỡ tập = −giá trị), <b>dương = chỉ số cha</b>. Khởi tạo toàn <code>−1</code>.</div>
<div class="grid8" id="d1"></div>
<div class="tip">Ví dụ: parentOrSize[1] = −3 nghĩa là 1 là gốc của tập 3 phần tử.</div>""")

S2 = section("2/8 — unite step-by-step: Union by Size", "Bấm Next: unite(1,2) rồi unite(2,3)",
"""<div class="grid8" id="d2"></div>
<div class="cover" id="cov2">Bấm Next để gộp từng cặp.</div>
<div class="steps" id="cap2">unite(1,2): hai gốc cỡ 1 → gắn 2 dưới 1.</div>
""" + stepper_btns("s2"))

S3 = section("3/8 — Path Compression: find vừa đi vừa nén", "2 tối ưu bắt buộc, thiếu 1 là TLE",
"""<p><code>find(u)</code>: nếu gốc thì trả về; không thì <code>parentOrSize[u] = find(parentOrSize[u])</code> — mọi nút trên đường đi trỏ thẳng về gốc.</p>
<div class="formula">find(3) với 3→2→1: sau 1 lần gọi, 3 và 2 đều trỏ thẳng về 1. Lần sau O(1).</div>
<ul><li><b>Union by Size:</b> cây nhỏ gắn dưới cây lớn → cao ≤ log n.</li>
<li>Kết hợp: <code>O(α(n))</code> — α là Ackermann ngược, ≤ 4 với mọi n thực tế.</li></ul>
<div class="warn">⛔ Quên Path Compression → cây dài → TLE. Quên Union by Size + find đệ quy sâu → Stack Overflow.</div>""")

S4 = section("4/8 — Sparse Table: min đoạn tĩnh trong O(1)", "st[j][i] = min đoạn [i, i+2<sup>j</sup>−1], a 0-based",
"""<p>a = [3,1,4,1,5,9,2,6]. Tiền xử lý <code>O(n log n)</code>:</p>
<table><tr><th>j (độ dài)</th><th>i=0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th></tr>
<tr><td>0 (len 1)</td><td>3</td><td>1</td><td>4</td><td>1</td><td>5</td><td>9</td><td>2</td><td>6</td></tr>
<tr><td>1 (len 2)</td><td>1</td><td>1</td><td>1</td><td>1</td><td>5</td><td>2</td><td>2</td><td>–</td></tr>
<tr><td>2 (len 4)</td><td class="hl">1</td><td>1</td><td class="hl">1</td><td>1</td><td class="hl">2</td><td>–</td><td>–</td><td>–</td></tr></table>
<div class="formula"><code>st[j][i] = min(st[j−1][i], st[j−1][i+2<sup>j−1</sup>])</code> — chẻ đôi đoạn dài.</div>""")

S5 = section("5/8 — Query đè đoạn: 2 khối phủ kín [l,r]", "Bấm Next: query(2,7) với len=6, k=2",
"""<p>len = r−l+1, k = 31 − clz(len). Phủ [l,r] bằng <code>[l, l+2<sup>k</sup>−1]</code> và <code>[r−2<sup>k</sup>+1, r]</code>. Phần đè nhau không ảnh hưởng min.</p>
<div class="grid8" id="d5"></div>
<div class="cover" id="cov5">Bấm Next để xem 2 khối được chọn.</div>
<div class="steps" id="cap5">query(2,7): len=6, k=2, khối dài 4.</div>
""" + stepper_btns("s5") + """
<div class="tip">Vì sao không <code>log2()</code>? double chậm 30–50 chu kỳ + sai làm tròn. <code>__builtin_clz</code> đúng 1 chu kỳ CPU.</div>""")

S6 = section("6/8 — Code chuẩn C++20", "DSU 15 dòng + Sparse 20 dòng",
code_block("code3", "C++20 · DSU + SparseTable", """<span class="type">int</span> <span class="fn">find</span>(<span class="type">int</span> u){ <span class="kw">return</span> p[u]&lt;<span class="num">0</span>?u:p[u]=<span class="fn">find</span>(p[u]); }
<span class="type">bool</span> <span class="fn">unite</span>(<span class="type">int</span> u,<span class="type">int</span> v){ u=<span class="fn">find</span>(u);v=<span class="fn">find</span>(v);
  <span class="kw">if</span>(u==v)<span class="kw">return false</span>;
  <span class="kw">if</span>(p[u]&gt;p[v])<span class="fn">swap</span>(u,v); p[u]+=p[v]; p[v]=u; <span class="kw">return true</span>; }
<span class="com">// Sparse: st[j][i]=min(st[j-1][i],st[j-1][i+(1&lt;&lt;(j-1))])</span>
<span class="type">int</span> <span class="fn">query</span>(<span class="type">int</span> l,<span class="type">int</span> r){ <span class="type">int</span> j=<span class="num">31</span>-__builtin_clz(r-l+<span class="num">1</span>);
  <span class="kw">return</span> <span class="fn">min</span>(st[j][l],st[j][r-(<span class="num">1</span>&lt;&lt;j)+<span class="num">1</span>]); }""") + """
<div class="warn">⛔ Sparse Table <b>chỉ dùng cho phép idempotent</b> (min/max/gcd). Sum KHÔNG dùng được vì phần đè bị cộng 2 lần.</div>""")

S7 = section("7/8 — Bẫy ICPC", "Index + đệ quy + clz",
"""<div class="two"><div><p><b>DSU (1-based):</b></p><ul>
<li>Đề 0-based → +1 mọi index.</li>
<li>find đệ quy: cây cao log n nên an toàn, nhưng quên Union by Size là nguy.</li></ul></div>
<div><p><b>Sparse (0-based):</b></p><ul>
<li><code>__builtin_clz(0)</code> là undefined — nhưng len ≥ 1 nên an toàn.</li>
<li>Nhớ guard <code>i + (1&lt;&lt;j) &lt;= n</code> khi build.</li></ul></div></div>
<div class="formula">📌 <b>Tóm tắt 30 giây:</b> DSU = 1 mảng âm/dương · find nén + gộp theo cỡ · Sparse = bảng lũy thừa 2 + query đè đoạn.</div>""")

S8 = section("8/8 — Tự kiểm tra 3 câu", "Đáp án đã kiểm chứng bằng code",
quiz(1, "DSU n=8, unite(1,2), unite(2,3), unite(3,4). parentOrSize[1] = ?", "✅ <b>−4</b> — gốc của tập 4 phần tử {1,2,3,4}.") +
quiz(2, "a=[3,1,4,1,5,9,2,6]. st[2][2] = ?", "✅ <b>1</b> — min(a[2..5]) = min(4,1,5,9) = 1.") +
quiz(3, "Vì sao Sparse Table không dùng cho sum?", "✅ <b>sum không idempotent</b> — phần đè nhau bị cộng 2 lần, đáp án sai.") + """
<div class="formula">🎯 <b>Bài tiếp theo (Bài 4):</b> Topo Sort + 0-1 BFS + Bellman-Ford + Floyd-Warshall.</div>""")

CUSTOM_JS = """
drawBars('d1',""" + P0 + """);
drawBars('d2',""" + P0 + """);
drawBars('d5',[{v:3,l:'a0'},{v:1,l:'a1'},{v:4,l:'a2'},{v:1,l:'a3'},{v:5,l:'a4'},{v:9,l:'a5'},{v:2,l:'a6'},{v:6,l:'a7'}]);
defSteps('s2','cap2',[
 {cap:'<b>Bước 1:</b> unite(1,2): hai gốc cỡ 1 → gắn 2 dưới 1. p[1]=−2, p[2]=1.',run:()=>{drawBars('d2',""" + P1 + """,{h:{0:'hit',1:'hit'}});document.getElementById('cov2').innerHTML='p[1]=<b>−2</b>, p[2]=1.';}},
 {cap:'<b>Bước 2:</b> unite(2,3): find(2)=1 (nén luôn), gộp 3 vào 1. p[1]=−3, p[3]=1.',run:()=>{drawBars('d2',""" + P2 + """,{h:{0:'hit',1:'hit2',2:'hit'}});document.getElementById('cov2').innerHTML='Tập {1,2,3} gốc 1. size(2) = <b>3</b>.';}}
],'unite(1,2): hai gốc cỡ 1 → gắn 2 dưới 1.');
ST['s2'].reset=()=>{drawBars('d2',""" + P0 + """);document.getElementById('cov2').innerHTML='Bấm Next để gộp từng cặp.';};
defSteps('s5','cap5',[
 {cap:'<b>Bước 1:</b> Khối 1: st[2][2] = min(a[2..5]) = min(4,1,5,9) = <b>1</b>.',run:()=>{drawBars('d5',[{v:3,l:'a0'},{v:1,l:'a1'},{v:4,l:'a2'},{v:1,l:'a3'},{v:5,l:'a4'},{v:9,l:'a5'},{v:2,l:'a6'},{v:6,l:'a7'}],{h:{2:'hit',3:'hit',4:'hit',5:'hit'}});document.getElementById('cov5').innerHTML='Khối [2..5] → <b>1</b>.';}},
 {cap:'<b>Bước 2:</b> Khối 2: st[2][4] = min(a[4..7]) = min(5,9,2,6) = <b>2</b>. Đáp án min(1,2) = <b>1</b>.',run:()=>{drawBars('d5',[{v:3,l:'a0'},{v:1,l:'a1'},{v:4,l:'a2'},{v:1,l:'a3'},{v:5,l:'a4'},{v:9,l:'a5'},{v:2,l:'a6'},{v:6,l:'a7'}],{h:{2:'hit',3:'hit',4:'hit2',5:'hit2',6:'hit2',7:'hit2'}});document.getElementById('cov5').innerHTML='Khối [4..7] → <b>2</b>. min chung = <b>1</b> ✓.';}}
],'query(2,7): len=6, k=2, khối dài 4.');
ST['s5'].reset=()=>{drawBars('d5',[{v:3,l:'a0'},{v:1,l:'a1'},{v:4,l:'a2'},{v:1,l:'a3'},{v:5,l:'a4'},{v:9,l:'a5'},{v:2,l:'a6'},{v:6,l:'a7'}]);document.getElementById('cov5').innerHTML='Bấm Next để xem 2 khối được chọn.';};
"""

MANIFEST = [
 ("Bài 3: DSU + Sparse Table — gộp tập O(1), min đoạn O(1)", "1/8 · unite/same · parentOrSize âm/dương", "Ví dụ n=8: unite(1,2),(2,3),(5,6)", "", ""),
 ("unite step-by-step: p[1]=-2 rồi -3, tập {1,2,3}", "2/8 · Union by Size · find nén đường", "Mở slides.html Slide 2, bấm Next", "", ""),
 ("Path Compression + Union by Size = O(alpha n)", "3/8 · find vừa đi vừa nén · cao cây log n", "Thiếu 1 tối ưu là TLE", "", "find nén đường // gộp cây nhỏ vào lớn // O alpha n"),
 ("Sparse: st[j][i] min đoạn dài 2^j, build chẻ đôi", "4/8 · a 0-based · st[1] len2, st[2] len4", "Bảng st đầy đủ trong slide", "", "st[j][i] chẻ đôi // build O n log n // query O 1"),
 ("Query đè đoạn: query(2,7)=min(st[2][2],st[2][4])=1", "5/8 · len=6,k=2 · đè nhau không sao với min", "Mở slides.html Slide 5, bấm Next", "", ""),
 ("Code: DSU 15 dòng + Sparse 20 dòng, cấm sum", "6/8 · idempotent mới dùng Sparse", "sum đè bị cộng 2 lần", "", "DSU: find+unite // Sparse: build+query // cấm sum"),
 ("Bẫy: DSU 1-based, Sparse 0-based, clz(0) UB", "7/8 · đệ quy log n an toàn · guard build", "Tóm tắt 30 giây cuối slide", "", "DSU +1 nếu 0-based // Sparse len≥1 // guard build"),
 ("Quiz: p[1]=-4; st[2][2]=1; sum cấm vì đè", "8/8 · đáp án kiểm chứng bằng code", "Tiếp theo: đường đi ngắn nhất", "", "p1=-4 // st22=1 // sum không idempotent"),
]

SCRIPT_ROWS = [
 ("DSU n=8, unite/same, mảng parentOrSize âm/dương", "Slide 1: bài toán + mảng"),
 ("unite(1,2) rồi unite(2,3), tập {1,2,3} gốc 1", "Slide 2: hoạt hình Next 2 bước"),
 ("Path Compression vừa đi vừa nén, Union by Size", "Slide 3: công thức + cảnh báo"),
 ("Sparse st[j][i], build chẻ đôi, bảng ví dụ", "Slide 4: bảng st đầy đủ"),
 ("query(2,7): 2 khối đè, min(1,2)=1", "Slide 5: hoạt hình Next 2 bước"),
 ("Code DSU + Sparse, cấm dùng sum", "Slide 6: code + cảnh báo"),
 ("Bẫy index, đệ quy, clz + tóm tắt", "Slide 7: 2 cột bẫy + recap"),
 ("3 câu quiz có đáp án + bài tiếp theo", "Slide 8: quiz + outro"),
]
