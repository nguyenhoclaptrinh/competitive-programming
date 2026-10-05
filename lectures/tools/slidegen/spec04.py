#!/usr/bin/env python3
"""Spec bài 04: Topo + 0-1 BFS + Bellman-Ford + Floyd."""
from template import section, quiz, code_block, stepper_btns

SLUG = "04-shortest-path"
TITLE = "Bài 4: Đường đi ngắn nhất — Hiểu sâu qua hình + tiếng"
H1 = "Bài 4: Topo + 0-1 BFS + Bellman-Ford + Floyd-Warshall"

TOPO_N = "[{id:1,x:80,y:90,l:'1'},{id:2,x:250,y:40,l:'2'},{id:3,x:250,y:140,l:'3'},{id:4,x:420,y:90,l:'4'}]"
TOPO_E = "[{a:1,b:2,l:''},{a:1,b:3,l:''},{a:2,b:4,l:''},{a:3,b:4,l:''}]"
B01_N = "[{id:1,x:60,y:90,l:'1'},{id:2,x:200,y:90,l:'2'},{id:3,x:340,y:90,l:'3'},{id:4,x:480,y:90,l:'4'}]"
B01_E = "[{a:1,b:2,l:'0'},{a:2,b:3,l:'1'},{a:1,b:3,l:'1'},{a:3,b:4,l:'0'}]"

S1 = section("1/8 — Topo Sort Kahn: bóc đỉnh nguồn", "DAG + inDegree + queue, Bấm Next chạy ví dụ",
"""<p>Thứ tự topo: mọi cạnh u→v thì u đứng trước v. Chỉ tồn tại trên <b>DAG</b>.</p>
<svg class="tree" id="g1" viewBox="0 0 500 180"></svg>
<div class="cover" id="cov1">indeg: 1:0, 2:1, 3:1, 4:2. Bấm Next để bóc từng đỉnh.</div>
<div class="steps" id="cap1">Queue khởi đầu: [1].</div>
""" + stepper_btns("s1"))

S2 = section("2/8 — 0-1 BFS: deque thay heap", "w=0 đẩy đầu, w=1 đẩy cuối, Bấm Next",
"""<p>Trọng số chỉ 0/1 → Dijkstra O(m log n) là lãng phí. Deque cho <code>O(n+m)</code>: hàng đợi luôn có dạng [d,d,…,d+1,…,d+1].</p>
<svg class="tree" id="g2" viewBox="0 0 560 180"></svg>
<div class="cover" id="cov2">Bấm Next để chạy từ đỉnh 1.</div>
<div class="steps" id="cap2">dist[1]=0, deque=[1].</div>
""" + stepper_btns("s2"))

S3 = section("3/8 — Bellman-Ford: nới lỏng n−1 vòng + bắt chu trình âm", "Bấm Next xem dist thay đổi",
"""<p>Đồ thị: 1→2(5), 2→3(−10), 3→1(3). Chu trình tổng −2 → chu trình âm, đỉnh 1 tới được.</p>
<div class="grid6" id="d3"></div>
<div class="cover" id="cov3">dist khởi tạo: [0, INF, INF]. Bấm Next từng vòng lặp.</div>
<div class="steps" id="cap3">Vòng 1: duyệt 3 cạnh.</div>
""" + stepper_btns("s3") + """
<div class="tip">Tối ưu dừng sớm + <code>max(−INF, …)</code> chống underflow. Chu trình âm chỉ bắt được nếu <b>tới được từ nguồn</b>.</div>""")

S4 = section("4/8 — Floyd-Warshall: k NGOÀI CÙNG bắt buộc", "Bấm Next xem ma trận sau mỗi k",
"""<p><code>dist[i][j]</code> = đường ngắn nhất i→j chỉ qua trung gian {1..k}. Đồ thị: 1→2(1), 2→3(2), 1→3(100).</p>
<div id="g4"></div>
<div class="cover" id="cov4">Ma trận khởi tạo (INF = ∞). Bấm Next từng k.</div>
<div class="steps" id="cap4">k=1: chỉ dùng đỉnh 1 làm trung gian.</div>
""" + stepper_btns("s4") + """
<div class="warn">⛔ Đưa k vào trong là sai hoàn toàn. Phát hiện chu trình âm: <code>dist[i][i] &lt; 0</code>.</div>""")

S5 = section("5/8 — Chọn thuật toán nào?", "Bảng quyết định 10 giây",
"""<table><tr><th>Tình huống</th><th>Thuật toán</th><th>Độ phức tạp</th></tr>
<tr><td>DAG, 1 nguồn</td><td class="hl">Topo + DP</td><td class="hl">O(n+m)</td></tr>
<tr><td>Trọng số ≥ 0</td><td>Dijkstra</td><td>O(m log n)</td></tr>
<tr><td>Trọng số chỉ 0/1</td><td class="hl">0-1 BFS</td><td class="hl">O(n+m)</td></tr>
<tr><td>Trọng số âm, 1 nguồn</td><td class="hl">Bellman-Ford</td><td class="hl">O(n·m)</td></tr>
<tr><td>Mọi cặp (n ≤ 500)</td><td class="hl">Floyd-Warshall</td><td class="hl">O(n³)</td></tr></table>""")

S6 = section("6/8 — Code chuẩn C++20", "4 thuật toán, long long hết",
code_block("code4", "C++20 · Topo + 0-1 BFS + Bellman + Floyd", """<span class="com">// Topo Kahn: indeg + queue; order.size&lt;n → chu trình</span>
<span class="type">queue</span>&lt;<span class="type">int</span>&gt; q; <span class="kw">for</span>(u) <span class="kw">if</span>(!indeg[u])q.<span class="fn">push</span>(u);
<span class="kw">while</span>(!q.<span class="fn">empty</span>()){u=q.<span class="fn">front</span>();q.<span class="fn">pop</span>();order.<span class="fn">push_back</span>(u);
  <span class="kw">for</span>(v:adj[u]) <span class="kw">if</span>(--indeg[v]==<span class="num">0</span>)q.<span class="fn">push</span>(v);}
<span class="com">// 0-1 BFS: w==0 push_front else push_back</span>
<span class="type">deque</span>&lt;<span class="type">int</span>&gt; dq; <span class="kw">if</span>(w==<span class="num">0</span>)dq.<span class="fn">push_front</span>(v);<span class="kw">else</span>dq.<span class="fn">push_back</span>(v);
<span class="com">// Bellman: n-1 vòng + check vòng n; Floyd: k NGOÀI CÙNG</span>""") + """
<div class="formula">📌 <b>Tóm tắt 30 giây:</b> DAG→Topo · 0/1→deque · âm→Bellman · mọi cặp→Floyd(k ngoài).</div>""")

S7 = section("7/8 — Bẫy ICPC", "Trọng số, vòng lặp, tràn số",
"""<ul><li>0-1 BFS có cạnh trọng số 2 là <b>sai ngay</b> — kiểm tra đề kỹ.</li>
<li>Bellman quên <code>max(−INF,…)</code> → underflow long long.</li>
<li>Floyd n=500, mảng tĩnh <code>ll dist[505][505]</code>, bật −O2.</li>
<li>Mọi dist dùng <code>long long</code>, INF = 4e18? Dùng 1e18, cộng an toàn.</li></ul>""")

S8 = section("8/8 — Tự kiểm tra 3 câu", "Đáp án đã kiểm chứng bằng code",
quiz(1, "Đồ thị 1→2, 2→3, 3→1. Topo được không?", "✅ <b>Không</b> — có chu trình, order rỗng (size 0 &lt; 3).") +
quiz(2, "Cạnh 1−2(0), 2−3(1). dist[3] từ nguồn 1?", "✅ <b>1</b> — đường 1→2→3 tổng 0+1.") +
quiz(3, "1→2(1), 2→3(2), 1→3(100). dist[1][3] sau Floyd?", "✅ <b>3</b> — qua đỉnh 2 ở vòng k=2.") + """
<div class="formula">🎯 <b>Bài tiếp theo (Bài 5):</b> LCA Binary Lifting + 2-SAT.</div>""")

CUSTOM_JS = """
drawNet('g1',""" + TOPO_N + """,""" + TOPO_E + """);
drawNet('g2',""" + B01_N + """,""" + B01_E + """);
drawBars('d3',[{v:0,l:'d1'},{v:'∞',l:'d2'},{v:'∞',l:'d3'}]);
const F0=[['0','1','100'],['∞','0','2'],['∞','∞','0']];
drawGrid('g4',F0);
defSteps('s1','cap1',[
 {cap:'<b>Bước 1:</b> pop 1 (indeg 0). Giảm 2→0, 3→0. Queue=[2,3]. order=[1].',run:()=>{drawNet('g1',""" + TOPO_N + """,""" + TOPO_E + """,{hn:[1],nl:{1:'1✓',2:'2:0',3:'3:0'}});document.getElementById('cov1').innerHTML='order=[<b>1</b>], queue=[2,3].';}},
 {cap:'<b>Bước 2:</b> pop 2. Giảm 4→1. order=[1,2].',run:()=>{drawNet('g1',""" + TOPO_N + """,""" + TOPO_E + """,{hn:[1,2],he:[0],nl:{4:'4:1'}});document.getElementById('cov1').innerHTML='order=[<b>1,2</b>], queue=[3].';}},
 {cap:'<b>Bước 3:</b> pop 3. Giảm 4→0, push 4. order=[1,2,3].',run:()=>{drawNet('g1',""" + TOPO_N + """,""" + TOPO_E + """,{hn:[1,2,3],he:[0,1],nl:{4:'4:0'}});document.getElementById('cov1').innerHTML='order=[<b>1,2,3</b>], queue=[4].';}},
 {cap:'<b>Bước 4:</b> pop 4. order=[1,2,3,4], size=4=n → <b>DAG hợp lệ</b>.',run:()=>{drawNet('g1',""" + TOPO_N + """,""" + TOPO_E + """,{hn:[1,2,3,4],he:[0,1,2,3]});document.getElementById('cov1').innerHTML='order=<b>[1,2,3,4]</b> ✓.';}}
],'Queue khởi đầu: [1].');
ST['s1'].reset=()=>{drawNet('g1',""" + TOPO_N + """,""" + TOPO_E + """);document.getElementById('cov1').innerHTML='indeg: 1:0, 2:1, 3:1, 4:2. Bấm Next để bóc từng đỉnh.';};
defSteps('s2','cap2',[
 {cap:'<b>Bước 1:</b> pop 1. 1→2 (w=0): dist=0, <b>push_front</b>. 1→3 (w=1): dist=1, push_back. deque=[2,3].',run:()=>{drawNet('g2',""" + B01_N + """,""" + B01_E + """,{hn:[1],he:[0],nl:{2:'2:0',3:'3:1'}});document.getElementById('cov2').innerHTML='dist=[0,0,1,∞], deque=[<b>2,3</b>].';}},
 {cap:'<b>Bước 2:</b> pop 2 (đầu). 2→3 (w=1): 0+1=1 không tốt hơn 1 → bỏ. deque=[3].',run:()=>{drawNet('g2',""" + B01_N + """,""" + B01_E + """,{hn:[1,2],he:[0]});document.getElementById('cov2').innerHTML='dist 3 giữ nguyên 1.';}},
 {cap:'<b>Bước 3:</b> pop 3. 3→4 (w=0): dist=1, push_front. deque=[4]. pop 4 → xong. dist[4]=<b>1</b>.',run:()=>{drawNet('g2',""" + B01_N + """,""" + B01_E + """,{hn:[1,2,3,4],he:[0,3],nl:{4:'4:1'}});document.getElementById('cov2').innerHTML='dist[4]=<b>1</b> đường 1→2→3→4 (0+1+0).';}}
],'dist[1]=0, deque=[1].');
ST['s2'].reset=()=>{drawNet('g2',""" + B01_N + """,""" + B01_E + """);document.getElementById('cov2').innerHTML='Bấm Next để chạy từ đỉnh 1.';};
defSteps('s3','cap3',[
 {cap:'<b>Vòng 1:</b> 1→2: dist[2]=5. 2→3: dist[3]=−5. 3→1: 0+3? −2&lt;0 → dist[1]=−2!',run:()=>{drawBars('d3',[{v:-2,l:'d1'},{v:5,l:'d2'},{v:-5,l:'d3'}],{h:{0:'hit',1:'hit',2:'hit'}});document.getElementById('cov3').innerHTML='dist=[<b>−2,5,−5</b>] — nguồn cũng bị kéo xuống!';}},
 {cap:'<b>Vòng 2 (=n−1):</b> tiếp tục giảm: dist=[−4,3,−7]… Vòng 3 (kiểm tra): vẫn nới được → <b>chu trình âm</b>.',run:()=>{drawBars('d3',[{v:-4,l:'d1'},{v:3,l:'d2'},{v:-7,l:'d3'}],{h:{0:'hit',1:'hit',2:'hit'}});document.getElementById('cov3').innerHTML='Vòng n còn nới lỏng được → <b>có chu trình âm</b> (tổng −2).';}}
],'Vòng 1: duyệt 3 cạnh.');
ST['s3'].reset=()=>{drawBars('d3',[{v:0,l:'d1'},{v:'∞',l:'d2'},{v:'∞',l:'d3'}]);document.getElementById('cov3').innerHTML='dist khởi tạo: [0, INF, INF]. Bấm Next từng vòng lặp.';};
defSteps('s4','cap4',[
 {cap:'<b>k=1:</b> qua đỉnh 1: dist[1][2]=1, dist[1][3]=min(100,–)=100. Chưa cải thiện.',run:()=>{drawGrid('g4',F0,{h:{'0,1':'hit','0,2':'hit'}});document.getElementById('cov4').innerHTML='Chưa có đường nào qua 1 tốt hơn.';}},
 {cap:'<b>k=2:</b> qua đỉnh 2: dist[1][3]=min(100, 1+2)=<b>3</b> ✓.',run:()=>{drawGrid('g4',[['0','1','3'],['∞','0','2'],['∞','∞','0']],{h:{'0,2':'hit2'}});document.getElementById('cov4').innerHTML='dist[1][3] = <b>3</b> qua đỉnh 2.';}},
 {cap:'<b>k=3:</b> không cải thiện thêm. Xong: dist[1][3]=3.',run:()=>{drawGrid('g4',[['0','1','3'],['∞','0','2'],['∞','∞','0']],{h:{'0,2':'hit2'}});document.getElementById('cov4').innerHTML='Kết quả cuối: dist[1][3]=<b>3</b>.';}}
],'k=1: chỉ dùng đỉnh 1 làm trung gian.');
ST['s4'].reset=()=>{drawGrid('g4',F0);document.getElementById('cov4').innerHTML='Ma trận khởi tạo (INF = ∞). Bấm Next từng k.';};
"""

MANIFEST = [
 ("Bài 4: Đường đi ngắn nhất — Topo, 0-1 BFS, Bellman, Floyd", "1/8 · Topo Kahn: indeg 0 vào queue, bóc dần", "Ví dụ 1→2,1→3,2→4,3→4", "", ""),
 ("0-1 BFS: w0 đẩy đầu, w1 đẩy cuối deque", "2/8 · O(n+m) thay Dijkstra O(m log n)", "Mở slides.html Slide 2, bấm Next", "", ""),
 ("Bellman-Ford: nới lỏng n-1 vòng, vòng n bắt chu trình âm", "3/8 · ví dụ chu trình tổng -2", "Mở slides.html Slide 3, bấm Next", "", "relax n-1 vòng // vòng n còn nới → âm // dừng sớm"),
 ("Floyd: k NGOÀI CÙNG, dist[1][3]=3 qua đỉnh 2", "4/8 · 1→2(1),2→3(2),1→3(100)", "Mở slides.html Slide 4, bấm Next", "", ""),
 ("Bảng chọn thuật toán 10 giây theo tình huống", "5/8 · DAG/Dijkstra/01/Bellman/Floyd", "Nhớ bảng này đi thi", "", "DAG→Topo // 0-1→deque // âm→Bellman // all→Floyd"),
 ("Code 4 thuật toán: queue, deque, relax, k-i-j", "6/8 · long long hết, INF 1e18", "Tóm tắt 30 giây cuối slide", "", "Topo queue // deque 0-1 // relax n-1 // k ngoài cùng"),
 ("Bẫy: trọng số 2, underflow, Floyd 500^3, long long", "7/8 · kiểm tra đề kỹ", "0-1 BFS sai nếu có w=2", "", "w=2 là sai // max -INF // mảng tĩnh O2"),
 ("Quiz: chu trình topo rỗng; dist=1; Floyd=3", "8/8 · đáp án kiểm chứng bằng code", "Tiếp theo: LCA + 2-SAT", "", "topo rỗng // dist3=1 // Floyd13=3"),
]

SCRIPT_ROWS = [
 ("Topo Kahn: indeg 0 vào queue, bóc dần 1-2-3-4", "Slide 1: đồ thị + hoạt hình Next 4 bước"),
 ("0-1 BFS: w0 đầu, w1 cuối deque, dist[4]=1", "Slide 2: hoạt hình Next 3 bước"),
 ("Bellman: nới lỏng, chu trình âm tổng -2", "Slide 3: dist bars Next 2 bước"),
 ("Floyd k ngoài cùng, dist[1][3]=3", "Slide 4: ma trận Next 3 bước"),
 ("Bảng chọn thuật toán theo tình huống", "Slide 5: bảng quyết định"),
 ("Code 4 thuật toán + tóm tắt", "Slide 6: code + recap"),
 ("Bẫy trọng số, underflow, hiệu năng", "Slide 7: 4 bẫy"),
 ("3 câu quiz có đáp án + bài tiếp theo", "Slide 8: quiz + outro"),
]
