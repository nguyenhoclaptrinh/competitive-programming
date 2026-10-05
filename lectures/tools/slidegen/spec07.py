#!/usr/bin/env python3
"""Spec bài 07: Dinic Max Flow."""
from template import section, quiz, code_block, stepper_btns

SLUG = "07-max-flow"
TITLE = "Bài 6: Dinic Max Flow — Hiểu sâu qua hình + tiếng"
H1 = "Bài 6: Dinic Max Flow — BFS tầng + DFS chặn + ptr"

NET_N = "[{id:1,x:70,y:100,l:'s=1'},{id:2,x:230,y:50,l:'2'},{id:3,x:230,y:150,l:'3'},{id:4,x:400,y:100,l:'t=4'}]"
NET_E = "[{a:1,b:2,l:'10'},{a:1,b:3,l:'10'},{a:2,b:3,l:'2'},{a:2,b:4,l:'8'},{a:3,b:4,l:'9'}]"

S1 = section("1/8 — Max Flow: đẩy nhiều nhất từ s đến t", "Dinic = BFS dựng tầng + DFS đẩy chặn, lặp lại",
"""<p>Mỗi cạnh có capacity. Ví dụ: s=1, t=4, 5 cạnh như hình. Max flow = <b>17</b>.</p>
<svg class="tree" id="n1" viewBox="0 0 470 200"></svg>
<div class="formula">Vượt Edmonds-Karp nhờ <b>Level Graph</b> (chỉ đi tầng k→k+1) + con trỏ <code>ptr[u]</code> (không duyệt lại cạnh chết).</div>""")

S2 = section("2/8 — BFS dựng Level Graph", "Bấm Next: level lan từ s qua cạnh còn dư",
"""<svg class="tree" id="n2" viewBox="0 0 470 200"></svg>
<div class="cover" id="cov2">level khởi tạo −1. Bấm Next từng lớp.</div>
<div class="steps" id="cap2">level[s]=0, queue=[1].</div>
""" + stepper_btns("s2"))

S3 = section("3/8 — DFS đẩy Blocking Flow + ptr[u] tham chiếu", "Bấm Next: 2 lần DFS đẩy 8 rồi 9",
"""<div class="formula"><code>for (int &cid = ptr[u]; …)</code> — dấu <code>&</code> giữ vị trí cạnh dở dang. Cạnh bão hòa là bỏ luôn.</div>
<svg class="tree" id="n3" viewBox="0 0 470 200"></svg>
<div class="cover" id="cov3">Bấm Next để đẩy từng đường.</div>
<div class="steps" id="cap3">DFS(1,INF): 1→2→4.</div>
""" + stepper_btns("s3"))

S4 = section("4/8 — Toàn cảnh 2 vòng + Min Cut", "Vòng 2 BFS không tới t → dừng, flow 17",
"""<p>Vòng 1: BFS level [0,1,1,2] → DFS đẩy 8 (1-2-4) + 9 (1-3-4) = <b>17</b>.</p>
<p>Vòng 2: 1→2 dư 2, 1→3 dư 1; mọi cạnh vào 4 bão hòa → level[4]=−1 → <b>dừng</b>.</p>
<div class="formula">Min cut {1,2,3}|{4} = 8+9 = <b>17</b> = Max flow (định lý Max-Flow Min-Cut).</div>""")

S5 = section("5/8 — Code chuẩn C++20 Dinic", "Edge + rev, bfs, dfs, maxFlow",
code_block("code7", "C++20 · Dinic", """<span class="kw">struct</span> <span class="type">Edge</span>{<span class="type">int</span> to; <span class="type">ll</span> cap,flow; <span class="type">int</span> rev;};
<span class="type">void</span> <span class="fn">addEdge</span>(u,v,c){adj[u].<span class="fn">push_back</span>({v,c,<span class="num">0</span>,szV});
  adj[v].<span class="fn">push_back</span>({u,<span class="num">0</span>,<span class="num">0</span>,szU-<span class="num">1</span>});} <span class="com">// cạnh ngược cap 0</span>
<span class="type">bool</span> <span class="fn">bfs</span>(){ <span class="com">// level, chỉ cạnh cap&gt;flow</span> }
<span class="type">ll</span> <span class="fn">dfs</span>(u,p){ <span class="kw">for</span>(<span class="type">int</span>&amp;cid=ptr[u];cid&lt;sz;++cid){...} }
<span class="type">ll</span> <span class="fn">maxFlow</span>(){f=<span class="num">0</span>;<span class="kw">while</span>(<span class="fn">bfs</span>()){ptr=<span class="num">0</span>;<span class="kw">while</span>(p=<span class="fn">dfs</span>(s,INF))f+=p;}<span class="kw">return</span> f;}""") + """
<div class="formula">📌 <b>Tóm tắt 30 giây:</b> BFS tầng → DFS chặn → ptr tham chiếu · cạnh ngược cap 0 · long long.</div>""")

S6 = section("6/8 — Min Cut + rút về matching", "BFS thặng dư từ s: tới được = S",
"""<ul><li>Sau maxFlow, BFS qua cạnh cap&gt;flow từ s. Min cut = cạnh gốc nối S→T.</li>
<li>Ghép 2 phía → flow: source→trái (cap 1), phải→sink (cap 1). Unit network: <code>O(E√V)</code>.</li>
<li>Ứng dụng: chọn dự án, phân đoạn ảnh, lịch thi đấu.</li></ul>""")

S7 = section("7/8 — Bẫy ICPC", "ptr, cạnh ngược, đệ quy, INF",
"""<ul><li><code>ptr[u]</code> thiếu <code>&</code> → duyệt lại → <b>TLE chắc</b>.</li>
<li>BFS chỉ xét <code>cap &gt; flow</code> — cạnh ngược tự tham gia đúng.</li>
<li>DFS đệ quy sâu ≤ V; V = 3·10⁵ đường thẳng → viết lặp hoặc đổi thuật toán.</li>
<li>INF = 1e18 (1e9 tràn khi cộng flow), mọi cap/flow <code>long long</code>.</li></ul>""")

S8 = section("8/8 — Tự kiểm tra 3 câu", "Đáp án đã kiểm chứng (maxflow=6 tay + code)",
quiz(1, "s→a(5), a→b(3), b→t(4), s→b(2), a→t(2). Max flow?", "✅ <b>6</b> — 3 qua a→b→t, 2 qua a→t, 1 qua s→b→t (min cut {s,a,b}|{t}=4+2).") +
quiz(2, "Vì sao ptr[u] phải là tham chiếu?", "✅ <b>Giữ vị trí cạnh dở dang</b> — cạnh bão hòa bỏ luôn, không duyệt lại → giữ O(V²E).") +
quiz(3, "Tìm Min Cut sau khi có max flow?", "✅ <b>BFS thặng dư từ s</b> — đỉnh tới được là S, cạnh gốc S→T là min cut.") + """
<div class="formula">🎯 <b>Bài tiếp theo (Bài 7):</b> Hopcroft-Karp Bipartite Matching.</div>""")

CUSTOM_JS = """
drawNet('n1',""" + NET_N + """,""" + NET_E + """);
drawNet('n2',""" + NET_N + """,""" + NET_E + """);
drawNet('n3',""" + NET_N + """,""" + NET_E + """);
defSteps('s2','cap2',[
 {cap:'<b>Lớp 0→1:</b> 1→2 (dư 10), 1→3 (dư 10) → level 2,3 = 1.',run:()=>{drawNet('n2',""" + NET_N + """,""" + NET_E + """,{hn:[1,2,3],he:[0,1],nl:{1:'L0',2:'L1',3:'L1'}});document.getElementById('cov2').innerHTML='level: 1→<b>0</b>, 2→<b>1</b>, 3→<b>1</b>.';}},
 {cap:'<b>Lớp 1→2:</b> 2→4 (dư 8) → level 4 = 2. level[t] ≠ −1 → có đường tăng.',run:()=>{drawNet('n2',""" + NET_N + """,""" + NET_E + """,{hn:[1,2,3,4],he:[0,1,3],nl:{1:'L0',2:'L1',3:'L1',4:'L2'}});document.getElementById('cov2').innerHTML='level[4]=<b>2</b> → chạy DFS.';}}
],'level[s]=0, queue=[1].');
ST['s2'].reset=()=>{drawNet('n2',""" + NET_N + """,""" + NET_E + """);document.getElementById('cov2').innerHTML='level khởi tạo −1. Bấm Next từng lớp.';};
defSteps('s3','cap3',[
 {cap:'<b>DFS 1:</b> 1→2→4 đẩy <b>8</b> (kẹt ở 2→4). flow=8.',run:()=>{drawNet('n3',""" + NET_N + """,""" + NET_E + """,{hn:[1,2,4],he:[0,3],el:{0:'10',3:'8/8'}});document.getElementById('cov3').innerHTML='flow=<b>8</b>. Cạnh 2→4 bão hòa.';}},
 {cap:'<b>DFS 2:</b> 1→2 còn dư 2 nhưng 2→3 chặn level, 2→4 hết → lui; 1→3→4 đẩy <b>9</b>. flow=17.',run:()=>{drawNet('n3',""" + NET_N + """,""" + NET_E + """,{hn:[1,2,3,4],he:[0,1,3,4],el:{0:'10',1:'10',3:'8/8',4:'9/9'}});document.getElementById('cov3').innerHTML='flow=<b>17</b>. ptr bỏ qua cạnh chết.';}}
],'DFS(1,INF): 1→2→4.');
ST['s3'].reset=()=>{drawNet('n3',""" + NET_N + """,""" + NET_E + """);document.getElementById('cov3').innerHTML='Bấm Next để đẩy từng đường.';};
"""

MANIFEST = [
 ("Bài 6: Dinic Max Flow — BFS tầng + DFS chặn", "1/8 · Level Graph + ptr, ví dụ maxflow 17", "s=1,t=4, 5 cạnh", "", ""),
 ("BFS dựng level: 1→0, 2,3→1, 4→2", "2/8 · chỉ cạnh còn dư, level[t]≠-1 là có đường", "Mở slides.html Slide 2, bấm Next", "", ""),
 ("DFS đẩy 8 rồi 9, ptr tham chiếu giữ vị trí", "3/8 · cạnh bão hòa bỏ luôn", "Mở slides.html Slide 3, bấm Next", "", ""),
 ("Vòng 2 dừng, min cut {1,2,3}|{4}=17", "4/8 · maxflow = mincut", "8+9=17 khớp định lý", "", "vòng2 dừng // mincut 8+9 // flow=mincut"),
 ("Code Dinic: Edge+rev, bfs, dfs, maxFlow", "5/8 · cạnh ngược cap 0, long long", "Tóm tắt 30 giây cuối slide", "", "Edge rev // bfs tầng // dfs chặn // ptr &"),
 ("Min cut BFS thặng dư + rút matching về flow", "6/8 · unit network O(E√V)", "Ứng dụng chọn dự án, ảnh", "", "BFS thặng dư // S-T cut // unit O(E√V)"),
 ("Bẫy: ptr&, cạnh ngược, đệ quy sâu, INF 1e18", "7/8 · thiếu & là TLE chắc", "4 bẫy sống còn", "", "ptr & bắt buộc // rev tự đúng // INF 1e18"),
 ("Quiz: maxflow 6; ptr giữ vị trí; BFS thặng dư", "8/8 · đáp án kiểm chứng bằng code", "Tiếp theo: Hopcroft-Karp", "", "flow 6 // ptr vị trí // cut BFS"),
]

SCRIPT_ROWS = [
 ("Max flow s-t, Dinic 2 pha, ví dụ 17", "Slide 1: mạng + công thức"),
 ("BFS dựng level từng lớp", "Slide 2: hoạt hình Next 2 bước"),
 ("DFS đẩy 8 rồi 9, ptr tham chiếu", "Slide 3: hoạt hình Next 2 bước"),
 ("Vòng 2 dừng + min cut 17", "Slide 4: tổng kết + định lý"),
 ("Code Dinic + tóm tắt", "Slide 5: code + recap"),
 ("Min cut + rút matching, ứng dụng", "Slide 6: cut + ứng dụng"),
 ("4 bẫy: ptr, ngược, đệ quy, INF", "Slide 7: bẫy"),
 ("3 câu quiz có đáp án + bài tiếp theo", "Slide 8: quiz + outro"),
]
