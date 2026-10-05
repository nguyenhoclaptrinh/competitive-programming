#!/usr/bin/env python3
"""Spec bài 09: Hình học cơ bản (CCW, giao đoạn, điểm trong đa giác)."""
from template import section, quiz, code_block, stepper_btns

SLUG = "09-geometry-basics"
TITLE = "Bài 8: Hình học cơ bản — Hiểu sâu qua hình + tiếng"
H1 = "Bài 8: CCW + giao đoạn + điểm trong đa giác"

S1 = section("1/8 — CCW: rẽ trái, rẽ phải, thẳng hàng", "cross = x1·y2 − x2·y1, long long hết",
"""<p><code>ccw(a,b,c) = (b−a)×(c−a)</code>. Ví dụ a(0,0), b(1,0), c(0,1): (1,0)×(0,1) = 1·1−0·0 = <b>1 &gt; 0</b>.</p>
<svg class="tree" viewBox="0 0 500 180"><text x="10" y="20" fill="#94a3b8" font-size="13">Từ a nhìn sang b, c rẽ hướng nào?</text>
<line x1="60" y1="140" x2="220" y2="140" stroke="#0ea5e9" stroke-width="3"/><circle cx="60" cy="140" r="6" fill="#0ea5e9"/><text x="50" y="165" fill="#e2e8f0" font-size="13">a</text><text x="225" y="145" fill="#e2e8f0" font-size="13">b</text>
<line x1="60" y1="140" x2="140" y2="60" stroke="#22c55e" stroke-width="3"/><circle cx="140" cy="60" r="6" fill="#22c55e"/><text x="145" y="60" fill="#22c55e" font-size="13">c: CCW&gt;0 rẽ TRÁI</text>
<line x1="300" y1="140" x2="460" y2="140" stroke="#0ea5e9" stroke-width="3"/><circle cx="300" cy="140" r="6" fill="#0ea5e9"/>
<line x1="300" y1="140" x2="380" y2="60" stroke="#ef4444" stroke-width="3" stroke-dasharray="6,4"/><circle cx="380" cy="60" r="6" fill="#ef4444"/><text x="330" y="50" fill="#ef4444" font-size="13">CCW&lt;0 rẽ PHẢI</text></svg>
<table><tr><th>ccw</th><th>Ý nghĩa</th></tr><tr><td class="hl">&gt; 0</td><td class="hl">Rẽ trái (CCW)</td></tr><tr><td>&lt; 0</td><td>Rẽ phải (CW)</td></tr><tr><td>= 0</td><td>Thẳng hàng</td></tr></table>
<div class="warn">⛔ Tọa độ 1e9 → cross tới 1e18 → <b>long long bắt buộc</b>. Không double cho CCW.</div>""")

S2 = section("2/8 — Giao 2 đoạn: 2 phía + suy biến", "4 ccw + 4 onSegment, thiếu 1 là sai",
"""<p>AB cắt CD khi: <b>(1)</b> C,D hai phía AB <b>VÀ</b> A,B hai phía CD — hoặc <b>(2)</b> đầu mút nằm trên đoạn kia.</p>
<div class="formula"><code>onSegment(p,a,b)</code> = ccw==0 <b>VÀ</b> p trong hộp bao [min..max] cả x lẫn y.</div>
<div class="tip">Chỉ check ccw mà quên bounding box → nhận vơ giao nhau. Chỉ check proper mà quên suy biến → mất điểm biên.</div>""")

S3 = section("3/8 — Ray Casting: lẻ trong, chẵn ngoài", "Tia ngang + quy tắc nửa mở nửa đóng",
"""<p>Từ P bắn tia ngang sang phải. Đếm giao với cạnh đa giác: <b>lẻ → TRONG, chẵn → NGOÀI</b>.</p>
<div class="formula">Cạnh [A,B] chỉ xét khi <code>A.y ≤ P.y &lt; B.y</code> (sau khi swap cho A thấp hơn) — tia qua đỉnh không bị đếm 2 lần. Gặp <code>onSegment</code> → trả BIÊN ngay.</div>
<svg class="tree" viewBox="0 0 500 170"><text x="10" y="20" fill="#94a3b8" font-size="13">Vuông (0,0),(4,0),(4,4),(0,4). Tia từ P(2,2) giao cạnh phải 1 lần → TRONG.</text>
<rect x="120" y="30" width="160" height="120" fill="none" stroke="#0ea5e9" stroke-width="2"/><circle cx="200" cy="110" r="6" fill="#f59e0b"/><text x="195" y="135" fill="#fbbf24" font-size="13">P</text><line x1="200" y1="110" x2="340" y2="110" stroke="#f59e0b" stroke-width="2" stroke-dasharray="6,4"/><circle cx="280" cy="110" r="5" fill="#ef4444"/><text x="285" y="105" fill="#ef4444" font-size="12">giao</text></svg>""")

S4 = section("4/8 — Ví dụ số kép: giao đoạn + ray", "Bấm Next tính từng ccw",
"""<p>AB=(0,0)-(4,4), CD=(0,4)-(4,0). Vuông + P(2,2), P(5,2), P(4,2).</p>
<div class="cover" id="cov4">Bấm Next để tính 4 ccw.</div>
<div class="steps" id="cap4">ccw(A,B,C) = ?</div>
""" + stepper_btns("s4"))

S5 = section("5/8 — Code chuẩn C++20", "Point + ccw + onSegment + intersect + pip",
code_block("code9", "C++20 · Point/intersect/pointInPolygon", """<span class="kw">struct</span> <span class="type">Point</span>{<span class="type">ll</span> x,y; <span class="type">Point</span> <span class="kw">operator</span>-(o){...}
  <span class="type">ll</span> <span class="fn">cross</span>(o){<span class="kw">return</span> x*o.y-y*o.x;} };
<span class="type">ll</span> <span class="fn">ccw</span>(a,b,c){<span class="kw">return</span> (b-a).<span class="fn">cross</span>(c-a);}
<span class="type">bool</span> <span class="fn">intersect</span>(a,b,c,d){ cp1..cp4;
  <span class="kw">if</span>(cp1*cp2&lt;<span class="num">0</span> &amp;&amp; cp3*cp4&lt;<span class="num">0</span>)<span class="kw">return true</span>;
  <span class="kw">return</span> onS(c)||onS(d)||onS(a)||onS(b); }
<span class="com">// pip: onSegment→BOUND; nửa mở nửa đóng + ccw&gt;0 flip</span>""") + """
<div class="formula">📌 <b>Tóm tắt 30 giây:</b> ccw dấu → hướng · giao = 2 phía + biên · ray lẻ/chẵn + nửa mở.</div>""")

S6 = section("6/8 — Bẫy ICPC hình học", "long long, không double, thẳng hàng",
"""<ul><li>cross 1e9×1e9 = 1e18 → <code>long long</code>, <code>int</code> tràn ngay.</li>
<li>So sánh góc bằng cross, không <code>atan2/double</code>.</li>
<li>ccw = 0 (thẳng hàng 180°) → luôn kèm check bounding box.</li>
<li>Hướng đa giác: tổng cross cạnh kề &gt; 0 là CCW.</li></ul>""")

S7 = section("7/8 — Ứng dụng: diện tích, khoảng cách", "Shoelace + chiếu vuông góc",
"""<ul><li>Diện tích đa giác: <code>0.5·|Σ cross(p[i],p[i+1])|</code> — giữ long long, chia 2 cuối.</li>
<li>Khoảng cách điểm–đoạn: chiếu vuông góc; ngoài đoạn thì lấy min(dist 2 đầu).</li>
<li>Tâm ngoại tiếp: giao 2 đường trung trực (giải bằng cross).</li></ul>""")

S8 = section("8/8 — Tự kiểm tra 3 câu", "Đáp án đã kiểm chứng bằng code",
quiz(1, "ccw((0,0),(1,0),(0,1)) = ?", "✅ <b>1 &gt; 0</b> — rẽ trái (1·1−0·0).") +
quiz(2, "Đoạn (0,0)-(2,2) và (0,2)-(2,0) có giao?", "✅ <b>Có</b> — tại (1,1), 2 phía cả 2 chiều.") +
quiz(3, "Vuông (0,0),(4,0),(4,4),(0,4). P(2,2)?", "✅ <b>TRONG</b> — tia giao 1 lần (lẻ).") + """
<div class="formula">🎯 <b>Bài tiếp theo (Bài 9):</b> Bao lồi Andrew Monotone Chain.</div>""")

CUSTOM_JS = """
defSteps('s4','cap4',[
 {cap:'<b>ccw(A,B,C):</b> (4,4)×(0,4) = 4·4−4·0 = <b>+16</b>.',run:()=>{document.getElementById('cov4').innerHTML='ccw(A,B,C) = <b>+16</b>.';}},
 {cap:'<b>ccw(A,B,D):</b> (4,4)×(4,0) = 4·0−4·4 = <b>−16</b>. Trái dấu → C,D hai phía AB ✓.',run:()=>{document.getElementById('cov4').innerHTML='ccw(A,B,D) = <b>−16</b>. Hai phía ✓.';}},
 {cap:'<b>ccw(C,D,A)=−16, ccw(C,D,B)=+16</b> → A,B hai phía CD ✓ → <b>GIAO tại (2,2)</b>.',run:()=>{document.getElementById('cov4').innerHTML='Cả 2 chiều đều 2 phía → <b>GIAO tại (2,2)</b> ✓.';}},
 {cap:'<b>Ray:</b> P(2,2) giao 1 lần → TRONG. P(5,2) 0 lần → NGOÀI. P(4,2) trên cạnh → BIÊN.',run:()=>{document.getElementById('cov4').innerHTML='P(2,2)=<b>TRONG</b>, P(5,2)=<b>NGOÀI</b>, P(4,2)=<b>BIÊN</b>.';}}
],'ccw(A,B,C) = ?');
ST['s4'].reset=()=>{document.getElementById('cov4').innerHTML='Bấm Next để tính 4 ccw.';};
"""

MANIFEST = [
 ("Bài 8: Hình học — CCW, giao đoạn, điểm trong đa giác", "1/8 · ccw dấu cho hướng, long long", "Ví dụ ccw=1 rẽ trái", "", ""),
 ("Giao 2 đoạn: 2 phía 2 chiều + suy biến onSegment", "2/8 · 4 ccw + 4 check biên", "Thiếu 1 là sai", "", "2 phía 2 chiều // suy biến biên // box bao"),
 ("Ray casting: lẻ trong chẵn ngoài, nửa mở nửa đóng", "3/8 · tia qua đỉnh không đếm 2", "onSegment trả BIÊN ngay", "", "lẻ TRONG chẵn NGOÀI // nửa mở // BIÊN ngay"),
 ("Ví dụ số: 4 ccw ±16, giao (2,2); ray 3 điểm", "4/8 · tính tay từng ccw", "Mở slides.html Slide 4, bấm Next", "", ""),
 ("Code Point/ccw/onSegment/intersect/pip", "5/8 · long long hết", "Tóm tắt 30 giây cuối slide", "", "Point ll // ccw cross // giao+pip"),
 ("Bẫy: tràn int, cấm double, thẳng hàng, hướng", "6/8 · cross 1e18", "4 bẫy sống còn", "", "ll bắt buộc // cấm double // biên box"),
 ("Ứng dụng: Shoelace, điểm-đoạn, ngoại tiếp", "7/8 · giữ ll chia 2 cuối", "3 ứng dụng", "", "Shoelace // chiếu // ngoại tiếp"),
 ("Quiz: ccw=1; giao (1,1); P trong", "8/8 · đáp án kiểm chứng bằng code", "Tiếp theo: Bao lồi", "", "ccw 1 // giao 11 // P TRONG"),
]

SCRIPT_ROWS = [
 ("CCW dấu cho hướng, ví dụ ccw=1", "Slide 1: SVG rẽ + bảng"),
 ("Giao 2 đoạn 2 phía + suy biến", "Slide 2: điều kiện + onSegment"),
 ("Ray casting lẻ/chẵn + nửa mở", "Slide 3: SVG tia + quy tắc"),
 ("4 ccw ±16, giao (2,2), ray 3 điểm", "Slide 4: hoạt hình Next 4 bước"),
 ("Code Point/intersect/pip + tóm tắt", "Slide 5: code + recap"),
 ("4 bẫy hình học", "Slide 6: bẫy"),
 ("Shoelace, khoảng cách, ngoại tiếp", "Slide 7: ứng dụng"),
 ("3 câu quiz có đáp án + bài tiếp theo", "Slide 8: quiz + outro"),
]
