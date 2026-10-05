#!/usr/bin/env python3
"""Spec bài 10: Bao lồi Andrew."""
from template import section, quiz, code_block, stepper_btns

SLUG = "10-convex-hull"
TITLE = "Bài 9: Bao lồi Andrew — Hiểu sâu qua hình + tiếng"
H1 = "Bài 9: Bao lồi Andrew Monotone Chain O(n log n)"

PTS = [[0,0],[1,-1],[1,1],[2,0],[2,2],[3,1]]
def sc(pt):
    return (60 + pt[0]*110, 200 - pt[1]*55)

S1 = section("1/8 — Andrew vs Graham: sort (x,y) là đủ", "Không góc cực, không double",
"""<p>Graham sort theo góc → <code>atan2/double</code> sai số. Andrew chỉ sort Descartes + quét 2 lượt.</p>
<div class="formula">Vỏ dưới (trái→phải) + vỏ trên (phải→trái), luật duy nhất: <code>ccw ≤ 0 → POP</code>. Ghép lại, bỏ điểm cuối trùng đầu.</div>
<p>Điểm ví dụ (đã sort): (0,0),(1,−1),(1,1),(2,0),(2,2),(3,1).</p>""")

S2 = section("2/8 — Vỏ dưới step-by-step (có POP!)", "Bấm Next: giữ hay pop từng điểm",
"""<svg class="tree" id="h2" viewBox="0 0 420 260"></svg>
<div class="cover" id="cov2">h=[(0,0),(1,−1)]. Bấm Next thêm từng điểm.</div>
<div class="steps" id="cap2">Thêm (1,1): ccw = ?</div>
""" + stepper_btns("s2"))

S3 = section("3/8 — Vỏ trên + ghép: 4 đỉnh cuối", "Bấm Next: chú ý 2 lần pop thẳng hàng",
"""<svg class="tree" id="h3" viewBox="0 0 420 260"></svg>
<div class="cover" id="cov3">Vỏ dưới xong [(0,0),(1,−1),(3,1)], t=4. Bấm Next duyệt ngược.</div>
<div class="steps" id="cap3">Thêm (2,2): k=3 &lt; t=4 nên giữ luôn.</div>
""" + stepper_btns("s3"))

S4 = section("4/8 — Code chuẩn C++20", "sort + unique + 2 vòng + resize(k−1)",
code_block("code10", "C++20 · convexHull", """<span class="fn">sort</span>(pts.<span class="fn">begin</span>(),pts.<span class="fn">end</span>()); <span class="com">// (x,y)</span>
pts.<span class="fn">erase</span>(<span class="fn">unique</span>(...),pts.<span class="fn">end</span>()); <span class="com">// bỏ trùng BẮT BUỘC</span>
<span class="kw">for</span>(p:pts){ <span class="kw">while</span>(k&gt;=<span class="num">2</span> &amp;&amp; <span class="fn">ccw</span>(h[k-<span class="num">2</span>],h[k-<span class="num">1</span>],p)&lt;=<span class="num">0</span>)k--; h[k++]=p; }
<span class="kw">for</span>(p:reverse){ <span class="kw">while</span>(k&gt;=t &amp;&amp; <span class="fn">ccw</span>(...)&lt;=<span class="num">0</span>)k--; h[k++]=p; }
h.<span class="fn">resize</span>(k-<span class="num">1</span>); <span class="com">// bỏ cuối trùng đầu</span>""") + """
<div class="formula">📌 <b>Tóm tắt 30 giây:</b> sort → dưới POP ccw≤0 → trên POP ccw≤0 → resize(k−1).</div>""")

S5 = section("5/8 — Rotating Calipers: đường kính O(k)", "j chỉ tăng, tổng ≤ 2n bước",
"""<p>Cặp xa nhất (đường kính): i quét, j leo khi diện tích tăng: <code>ccw(h[i],h[i+1],h[j+1]) &gt; ccw(h[i],h[i+1],h[j])</code>.</p>
<div class="formula">ans = max dist²(h[i],h[j]). Tương tự: chu vi, min width, min area rect.</div>""")

S6 = section("6/8 — Bẫy ICPC bao lồi", "Trùng, thẳng hàng, n nhỏ, long long",
"""<ul><li>Điểm trùng: <b>unique sau sort</b>, không là pop sai.</li>
<li>Thẳng hàng hết → chỉ giữ 2 đầu (luật ≤ 0).</li>
<li>n ≤ 2: trả về luôn (resize(k−1) sai khi k &lt; 2).</li>
<li>ccw <code>long long</code>; sort bằng <code>operator&lt;</code> (x rồi y).</li></ul>""")

S7 = section("7/8 — Ứng dụng: diện tích, chu vi, đường kính", "Shoelace trên h",
"""<ul><li>Diện tích: Shoelace trên h (giữ ll, chia 2 cuối).</li>
<li>Chu vi: Σ dist(h[i],h[i+1]).</li>
<li>Điểm ngẫu nhiên: kỳ vọng O(log n) đỉnh hull.</li></ul>""")

S8 = section("8/8 — Tự kiểm tra 3 câu", "Đáp án đã kiểm chứng bằng code",
quiz(1, "Đổi luật thành <code>ccw &lt; 0</code> mới pop thì sao?", "✅ <b>Giữ điểm thẳng hàng trên cạnh</b> — hull có đỉnh dư (collinear).") +
quiz(2, "(0,0),(1,0),(2,0) thẳng hàng → mấy đỉnh?", "✅ <b>2</b> — chỉ đầu và cuối.") +
quiz(3, "Calipers: j tăng tổng cộng bao nhiêu bước?", "✅ <b>≤ 2n</b> — j đơn điệu, i tăng n lần.") + """
<div class="formula">🎯 <b>Bài tiếp theo (Bài 10):</b> Manacher + Aho-Corasick.</div>""")

CUSTOM_JS = """
const HP=[[0,0],[1,-1],[1,1],[2,0],[2,2],[3,1]];
function sc(p){return [60+p[0]*110, 200-p[1]*55];}
function drawHull(id,pts,hi,pop){const el=document.getElementById(id);let h='<text x="10" y="18" fill="#94a3b8" font-size="12">Lưới điểm (mỗi ô = 1 đơn vị)</text>';for(let gx=0;gx<=3;gx++){for(let gy=-1;gy<=2;gy++){const x=60+gx*110,y=200-gy*55;h+='<circle cx="'+x+'" cy="'+y+'" r="2" fill="#334155"/>';}}
pts.forEach((p,i)=>{const s=sc(p);const isHi=hi&&hi.indexOf(i)>=0;const isPop=pop&&pop.indexOf(i)>=0;h+='<circle cx="'+s[0]+'" cy="'+s[1]+'" r="9" fill="'+(isPop?'#475569':isHi?'#f59e0b':'#0ea5e9')+'"/>';h+='<text x="'+s[0]+'" y="'+(s[1]-14)+'" fill="'+(isPop?'#64748b':'#e2e8f0')+'" font-size="11" text-anchor="middle">'+(isPop?'✕':'('+p[0]+','+p[1]+')')+'</text>';});
el.innerHTML=h;}
drawHull('h2',HP);drawHull('h3',HP);
defSteps('s2','cap2',[
 {cap:'<b>(1,1):</b> ccw((0,0),(1,−1),(1,1)) = 2 &gt; 0 → <b>GIỮ</b>.',run:()=>{drawHull('h2',HP,[0,1,2]);document.getElementById('cov2').innerHTML='h=[(0,0),(1,−1),(1,1)].';}},
 {cap:'<b>(2,0):</b> ccw((1,−1),(1,1),(2,0)) = −2 → <b>POP (1,1)</b>; ccw((0,0),(1,−1),(2,0)) = 2 → GIỮ.',run:()=>{drawHull('h2',HP,[0,1,3],[2]);document.getElementById('cov2').innerHTML='h=[(0,0),(1,−1),(2,0)].';}},
 {cap:'<b>(2,2):</b> ccw = 2 → GIỮ. <b>(3,1):</b> ccw((2,0),(2,2),(3,1))=−2 POP (2,2); ccw((1,−1),(2,0),(3,1))=0 (thẳng hàng!) POP (2,0); ccw((0,0),(1,−1),(3,1))=4 GIỮ.',run:()=>{drawHull('h2',HP,[0,1,5],[3,4]);document.getElementById('cov2').innerHTML='Vỏ dưới = <b>[(0,0),(1,−1),(3,1)]</b>. (2,0) nằm trên cạnh nên bị loại.';}}
],'Thêm (1,1): ccw = ?');
ST['s2'].reset=()=>{drawHull('h2',HP);document.getElementById('cov2').innerHTML='h=[(0,0),(1,−1)]. Bấm Next thêm từng điểm.';};
defSteps('s3','cap3',[
 {cap:'<b>(2,2):</b> k=3 &lt; t=4 → GIỮ luôn.',run:()=>{drawHull('h3',HP,[5]);document.getElementById('cov3').innerHTML='h thêm (2,2).';}},
 {cap:'<b>(2,0):</b> ccw((3,1),(2,2),(2,0)) = 2 → GIỮ. <b>(1,1):</b> ccw((2,2),(2,0),(1,1)) = −2 → POP (2,0); ccw((3,1),(2,2),(1,1)) = 2 → GIỮ.',run:()=>{drawHull('h3',HP,[5,3,2],[4]);document.getElementById('cov3').innerHTML='(2,0) bị pop, (1,1) vào.';}},
 {cap:'<b>(1,−1):</b> ccw = 2 → GIỮ. <b>(0,0):</b> ccw((1,1),(1,−1),(0,0)) = −2 POP (1,−1); ccw((2,2),(1,1),(0,0)) = 0 (thẳng hàng, (1,1) trên cạnh) POP (1,1); ccw((3,1),(2,2),(0,0)) = 4 GIỮ.',run:()=>{drawHull('h3',HP,[0,1,5,4],[3,2]);document.getElementById('cov3').innerHTML='Bỏ cuối trùng đầu → hull <b>4 đỉnh</b>: (0,0),(1,−1),(3,1),(2,2).';}}
],'Thêm (2,2): k=3 < t=4 nên giữ luôn.');
ST['s3'].reset=()=>{drawHull('h3',HP);document.getElementById('cov3').innerHTML='Vỏ dưới xong [(0,0),(1,−1),(3,1)], t=4. Bấm Next duyệt ngược.';};
"""

MANIFEST = [
 ("Bài 9: Bao lồi Andrew — sort (x,y) + quét 2 lượt", "1/8 · ccw≤0 là pop, không góc cực", "Ví dụ 6 điểm đã sort", "", ""),
 ("Vỏ dưới: pop (1,1), pop (2,2), pop thẳng hàng (2,0)", "2/8 · ccw 2,-2,-2,0,4", "Mở slides.html Slide 2, bấm Next", "", ""),
 ("Vỏ trên + ghép: pop (2,0),(1,-1),(1,1) → 4 đỉnh", "3/8 · t=4, resize(k-1)", "Mở slides.html Slide 3, bấm Next", "", ""),
 ("Code Andrew: sort+unique+2 vòng+resize", "4/8 · bỏ trùng bắt buộc", "Tóm tắt 30 giây cuối slide", "", "sort unique // 2 vòng pop // resize k-1"),
 ("Rotating Calipers: j đơn điệu, đường kính O(k)", "5/8 · diện tích tăng thì leo j", "ans=max dist bình phương", "", "j đơn điệu // ≤2n bước // max dist2"),
 ("Bẫy: trùng, thẳng hàng, n≤2, long long", "6/8 · unique sau sort", "4 bẫy sống còn", "", "unique // collinear 2 đỉnh // n≤2 // ll"),
 ("Ứng dụng: diện tích, chu vi, đỉnh ngẫu nhiên", "7/8 · Shoelace trên h", "3 ứng dụng", "", "Shoelace // chu vi // log n đỉnh"),
 ("Quiz: luật <0 giữ collinear; thẳng hàng 2 đỉnh; j≤2n", "8/8 · đáp án kiểm chứng bằng code", "Tiếp theo: Xâu ký tự", "", "collinear dư // 2 đỉnh // j 2n"),
]

SCRIPT_ROWS = [
 ("Andrew vs Graham, luật pop ccw≤0", "Slide 1: so sánh + ví dụ điểm"),
 ("Vỏ dưới 3 bước pop", "Slide 2: SVG điểm + Next 3 bước"),
 ("Vỏ trên + ghép 4 đỉnh", "Slide 3: SVG + Next 3 bước"),
 ("Code Andrew + tóm tắt", "Slide 4: code + recap"),
 ("Rotating Calipers đường kính", "Slide 5: calipers"),
 ("4 bẫy bao lồi", "Slide 6: bẫy"),
 ("Diện tích, chu vi, ngẫu nhiên", "Slide 7: ứng dụng"),
 ("3 câu quiz có đáp án + bài tiếp theo", "Slide 8: quiz + outro"),
]
