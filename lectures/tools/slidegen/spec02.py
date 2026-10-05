#!/usr/bin/env python3
"""Spec bài 02: Range Update Range Query + BIT 2D."""
from template import section, quiz, code_block, stepper_btns

SLUG = "02-fenwick-range-2d"
TITLE = "Bài 2: Range Update + BIT 2D — Hiểu sâu qua hình + tiếng"
H1 = "Bài 2: Range Update Range Query + Fenwick 2D — O(log N)"

DVALS = "[{v:3,l:'D1'},{v:-2,l:'D2'},{v:3,l:'D3'},{v:-3,l:'D4'},{v:4,l:'D5'},{v:4,l:'D6'},{v:-7,l:'D7'},{v:4,l:'D8'}]"

S1 = section("1/8 — Bài toán: cộng cả đoạn + hỏi tổng đoạn", "Mở rộng bài 1: từ add điểm lên add đoạn",
"""<p>Mảng <code>a[1..8] = [3,1,4,1,5,9,2,6]</code>. Yêu cầu mới: <code>addRange(l,r,v)</code> cộng v vào <b>cả đoạn</b>, và <code>queryRange(l,r)</code> hỏi tổng đoạn — cả hai trong <code>O(log N)</code>.</p>
<ul><li>Duyệt tay mỗi lần tốn <code>O(n)</code> → TLE với 10<sup>5</sup> thao tác.</li>
<li>Segment Tree Lazy làm được nhưng dài ~80 dòng, dễ bug phòng thi.</li>
<li><b>Range BIT</b>: chỉ 2 cây Fenwick thường + mảng sai phân, ~20 dòng.</li></ul>
<div class="grid8" id="a2arr"></div>
<div class="formula">Ví dụ xuyên suốt: <code>addRange(2,5,10)</code> rồi hỏi tổng. Mảng a giữ nguyên để đối chiếu.</div>""")

S2 = section("2/8 — Mảng sai phân D: chìa khóa của mọi thứ", "D[i] = a[i] − a[i−1]; a[i] = tổng tiền tố của D",
"""<p>Đặt <code>D[i] = a[i] − a[i−1]</code> (quy ước <code>a[0] = 0</code>). Với a trên:</p>
<div class="grid8" id="d2arr"></div>
<p><code>D = [3,−2,3,−3,4,4,−7,4]</code>. Kiểm tra: a[5] = 3−2+3−3+4 = 5 ✓.</p>
<div class="formula">Tổng tiền tố <b>S(p) = Σ<sub>j≤p</sub>(p−j+1)·D[j] = (p+1)·ΣD[j] − Σ(j·D[j])</b><br>
→ chỉ cần 2 cây BIT: <code>b1</code> lưu D[j], <code>b2</code> lưu j·D[j].</div>
<div class="tip">Vì sao đúng? D[j] xuất hiện trong a[j],a[j+1],…,a[p] → đúng (p−j+1) lần.</div>""")

S3 = section("3/8 — addRange(l,r,v): chỉ 4 lệnh add điểm", "Bấm Next để xem D thay đổi khi addRange(2,5,10)",
"""<p>Cộng v vào a[l..r] ⟺ <code>D[l] += v</code> và <code>D[r+1] −= v</code>. Trên 2 cây BIT:</p>
<ul><li><code>b1.add(l,v)</code> và <code>b1.add(r+1,−v)</code></li>
<li><code>b2.add(l,v·l)</code> và <code>b2.add(r+1,−v·(r+1))</code></li></ul>
<div class="grid8" id="d3arr"></div>
<div class="cover" id="cov3">Bấm Next để xem từng lệnh add tác động vào D.</div>
<div class="steps" id="cap3">Hành trình: D[2]+=10 rồi D[6]−=10.</div>
""" + stepper_btns("s3"))

S4 = section("4/8 — queryPrefix: phân biệt phần cộng thêm và tổng thực", "Bấm Next để tính queryPrefix(5) từng bước",
"""<div class="formula"><code>queryPrefix(p) = b1.query(p)·(p+1) − b2.query(p)</code> = tổng <b>phần cộng thêm</b> vào [1..p].</div>
<div class="grid8" id="d4arr"></div>
<div class="cover" id="cov4">Sau addRange(2,5,10): bấm Next để đọc b1.query(5) và b2.query(5).</div>
<div class="steps" id="cap4">Phần cộng thêm vào [1..5] = ?</div>
""" + stepper_btns("s4") + """
<div class="tip">Tổng thực tế = tổng gốc + phần cộng thêm = 14 + 40 = <b>54</b>. Muốn query ra tổng thực: dựng RangeBIT từ mảng gốc trước (n lần addRange điểm).</div>""")

S5 = section("4/8b — BIT 2D: vì sao không Segment Tree 2D?", "512 MB so với 32 MB với n = m = 2000",
"""<table><tr><th>Cấu trúc</th><th>Bộ nhớ (n=m=2000)</th><th>Tốc độ</th></tr>
<tr><td>Segment Tree 2D (4n×4m)</td><td>8000×8000×8 byte ≈ <b>512 MB → MLE</b></td><td>chậm</td></tr>
<tr><td class="hl">Fenwick 2D ((n+1)×(m+1))</td><td class="hl">2001×2001×8 byte ≈ <b>32 MB</b></td><td class="hl">nhanh 5–10× (cache liên tục)</td></tr></table>
<p><code>add(x,y,v)</code>: i từ x lên n (<code>i += i&−i</code>), trong mỗi i: j từ y lên m. <code>O(log n·log m)</code>.</p>
<div class="formula">Tổng hình chữ nhật = <b>Q(x2,y2) − Q(x1−1,y2) − Q(x2,y1−1) + Q(x1−1,y1−1)</b> (bù trừ 4 góc).</div>""")

S6 = section("6/8 — Ví dụ 2D step-by-step trên lưới 4×4", "Bấm Next: add(2,2,5) rồi queryRect(2,2,3,3)",
"""<div id="g6"></div>
<div class="cover" id="cov6">Bấm Next để xem từng ô bị chạm.</div>
<div class="steps" id="cap6">add(2,2,5) chạm những ô nào?</div>
""" + stepper_btns("s6"))

S7 = section("7/8 — Code chuẩn C++20", "RangeFenwick + Fenwick2D, học thuộc khung",
code_block("code2", "C++20 · RangeFenwick + Fenwick2D", """<span class="kw">struct</span> <span class="fn">RangeFenwick</span> {
    <span class="type">int</span> n; <span class="fn">Fenwick</span> b1, b2;
    <span class="fn">RangeFenwick</span>(<span class="type">int</span> n) : n(n), b1(n), b2(n) {}
    <span class="type">void</span> <span class="fn">addRange</span>(<span class="type">int</span> l, <span class="type">int</span> r, <span class="type">long long</span> v) {
        b1.<span class="fn">add</span>(l, v); b1.<span class="fn">add</span>(r + <span class="num">1</span>, -v);
        b2.<span class="fn">add</span>(l, v * l); b2.<span class="fn">add</span>(r + <span class="num">1</span>, -v * (r + <span class="num">1</span>));
    }
    <span class="type">long long</span> <span class="fn">queryPrefix</span>(<span class="type">int</span> p) <span class="kw">const</span> {
        <span class="kw">return</span> b1.<span class="fn">query</span>(p) * (p + <span class="num">1</span>) - b2.<span class="fn">query</span>(p);
    }
};""") + """
<div class="two"><div class="tip"><b>Nhớ:</b> b1 ↔ D[j], b2 ↔ j·D[j]. Mọi <code>sum</code> dùng <code>long long</code>, 1-based.</div>
<div class="tip"><b>2D:</b> add/query 2 vòng lặp lồng <code>i += i&−i</code>, <code>j += j&−j</code>; rect = 4 góc bù trừ.</div></div>
<div class="formula">📌 <b>Tóm tắt 30 giây:</b> range-add ⟺ 2 điểm trên D · prefix = (p+1)·b1 − b2 · 2D = 4 góc bù trừ.</div>""")

S8 = section("8/8 — Tự kiểm tra 3 câu", "Đáp án đã kiểm chứng bằng code",
quiz(1, "RangeBIT n=8, <code>addRange(2,5,10)</code>. b1 gọi add nào?", "✅ <b>b1.add(2,10), b1.add(6,−10)</b>. b2 gọi add(2,20), add(6,−60).") +
quiz(2, "BIT 2D 4×4, <code>add(2,2,5)</code> chạm những ô nào?", "✅ <b>(2,2), (2,4), (4,2), (4,4)</b>. i: 2→4; j: 2→4.") +
quiz(3, "<code>queryRect(2,2,3,3)</code> gồm 4 góc nào?", "✅ <b>Q(3,3)−Q(1,3)−Q(3,1)+Q(1,1)</b>.") + """
<div class="formula">🎯 <b>Bài tiếp theo (Bài 3):</b> DSU nén đường đi + Sparse Table RMQ O(1).</div>""")

CUSTOM_JS = """
drawBars('a2arr',[{v:3,l:'a1'},{v:1,l:'a2'},{v:4,l:'a3'},{v:1,l:'a4'},{v:5,l:'a5'},{v:9,l:'a6'},{v:2,l:'a7'},{v:6,l:'a8'}]);
drawBars('d2arr',""" + DVALS + """);
drawBars('d3arr',""" + DVALS + """);
drawBars('d4arr',[{v:3,l:'D1'},{v:8,l:'D2'},{v:3,l:'D3'},{v:-3,l:'D4'},{v:4,l:'D5'},{v:-6,l:'D6'},{v:-7,l:'D7'},{v:4,l:'D8'}]);
defSteps('s3','cap3',[
 {cap:'<b>Bước 1:</b> D[2] += 10 (−2 → 8). Trên b1: add(2,10); trên b2: add(2,20).',run:()=>{drawBars('d3arr',[{v:3,l:'D1'},{v:8,l:'D2'},{v:3,l:'D3'},{v:-3,l:'D4'},{v:4,l:'D5'},{v:4,l:'D6'},{v:-7,l:'D7'},{v:4,l:'D8'}],{h:{1:'hit'}});document.getElementById('cov3').innerHTML='D[2]: −2 → <b>8</b>. b1.add(2,10), b2.add(2,20).';}},
 {cap:'<b>Bước 2:</b> D[6] −= 10 (4 → −6). Trên b1: add(6,−10); trên b2: add(6,−60).',run:()=>{drawBars('d3arr',[{v:3,l:'D1'},{v:8,l:'D2'},{v:3,l:'D3'},{v:-3,l:'D4'},{v:4,l:'D5'},{v:-6,l:'D6'},{v:-7,l:'D7'},{v:4,l:'D8'}],{h:{1:'hit',5:'hit'}});document.getElementById('cov3').innerHTML='D[6]: 4 → <b>−6</b>. Chỉ 2 điểm D đổi → 4 lệnh add điểm.';}}
], 'Hành trình: D[2]+=10 rồi D[6]−=10.');
ST['s3'].reset=()=>{drawBars('d3arr',""" + DVALS + """);document.getElementById('cov3').innerHTML='Bấm Next để xem từng lệnh add tác động vào D.';};
defSteps('s4','cap4',[
 {cap:'<b>Bước 1:</b> b1.query(5) = 10 (chỉ có +10 tại 2; −10 tại 6 nằm ngoài).',run:()=>{document.getElementById('cov4').innerHTML='b1.query(5) = <b>10</b>.';}},
 {cap:'<b>Bước 2:</b> b2.query(5) = 20 (chỉ có +20 tại 2). Phần cộng thêm = 10·6 − 20 = <b>40</b>.',run:()=>{document.getElementById('cov4').innerHTML='b2.query(5) = <b>20</b>. Phần cộng thêm vào [1..5] = 10·6 − 20 = <b>40</b>.';}}
], 'Phần cộng thêm vào [1..5] = ?');
ST['s4'].reset=()=>{document.getElementById('cov4').innerHTML='Sau addRange(2,5,10): bấm Next để đọc b1.query(5) và b2.query(5).';};
const G4=[['·','·','·','·'],['·','·','·','·'],['·','·','·','·'],['·','·','·','·']];
drawGrid('g6',G4);
defSteps('s6','cap6',[
 {cap:'<b>Bước 1:</b> add(2,2,5). i: 2→4, j: 2→4 → chạm (2,2),(2,4),(4,2),(4,4).',run:()=>{drawGrid('g6',G4,{h:{'1,1':'hit','1,3':'hit','3,1':'hit','3,3':'hit'}});document.getElementById('cov6').innerHTML='add(2,2,5) chạm <b>4 ô</b>.';}},
 {cap:'<b>Bước 2:</b> queryRect(2,2,3,3) = Q(3,3)−Q(1,3)−Q(3,1)+Q(1,1) — 4 góc bù trừ.',run:()=>{drawGrid('g6',G4,{h:{'2,2':'hit2','0,2':'hit','2,0':'hit','0,0':'hit'}});document.getElementById('cov6').innerHTML='4 góc bù trừ cho hình chữ nhật [2..3]×[2..3].';}}
], 'add(2,2,5) chạm những ô nào?');
ST['s6'].reset=()=>{drawGrid('g6',G4);document.getElementById('cov6').innerHTML='Bấm Next để xem từng ô bị chạm.';};
"""

MANIFEST = [
 ("Bài 2: Range Update + BIT 2D — cộng cả đoạn O(log N)", "1/8 · Từ add điểm lên add đoạn [l,r]", "Ví dụ a=[3,1,4,1,5,9,2,6] · addRange(2,5,10)", "", ""),
 ("Mảng sai phân D: D[i]=a[i]-a[i-1], S(p)=(p+1)sumD-sum(jD)", "2/8 · D=[3,-2,3,-3,4,4,-7,4] · b1 lưu D, b2 lưu jD", "D[j] xuất hiện đúng (p-j+1) lần trong S(p)", "", "D=[3,-2,3,-3,4,4,-7,4] // b1 ↔ D[j] // b2 ↔ j·D[j]"),
 ("addRange(2,5,10): D[2]+=10, D[6]-=10 → 4 lệnh add", "3/8 · b1.add(2,10),add(6,-10) · b2.add(2,20),add(6,-60)", "Mở slides.html Slide 3, bấm Next từng bước", "", ""),
 ("queryPrefix(5)=10*6-20=40 là PHẦN CỘNG THÊM (gốc 14 → tổng 54)", "4/8 · prefix=b1*(p+1)-b2 · thực=gốc+cộng thêm", "Mở slides.html Slide 4, bấm Next từng bước", "", ""),
 ("BIT 2D: 32MB thay vì 512MB, nhanh 5-10 lần", "5/8 · add/query 2 vòng lồng i,j · rect=4 góc bù trừ", "Segment Tree 2D 8000x8000x8 byte tràn nhớ", "", "512MB → MLE // 32MB BIT 2D // rect = 4 góc bù trừ"),
 ("2D step-by-step: add(2,2,5) chạm 4 ô, rect 4 góc", "6/8 · i:2→4, j:2→4 · Q(3,3)-Q(1,3)-Q(3,1)+Q(1,1)", "Mở slides.html Slide 6, bấm Next từng bước", "array", ""),
 ("Code chuẩn: RangeFenwick 4 lệnh + Fenwick2D 2 vòng lồng", "7/8 · long long · 1-based · prefix=(p+1)b1-b2", "Tóm tắt 30 giây cuối slide 7", "", "addRange = 4 add điểm // prefix = (p+1)*b1 − b2 // 2D: 2 vòng lồng + 4 góc"),
 ("Tự kiểm tra: b1.add(2,10)+add(6,-10); 4 ô 2D; 4 góc", "8/8 · đáp án đã kiểm chứng bằng code", "Tiếp theo: DSU + Sparse Table", "", "b1: (2,10),(6,-10) // 2D: (2,2),(2,4),(4,2),(4,4)"),
]

SCRIPT_ROWS = [
 ("Mảng 1e5, add đoạn + hỏi đoạn, RangeBIT 2 cây", "Slide 1: bài toán + mảng a"),
 ("Mảng sai phân D, công thức S(p) với 2 cây BIT", "Slide 2: bảng a vs D + công thức"),
 ("addRange(2,5,10): D[2]+=10, D[6]-=10", "Slide 3: hoạt hình Next 2 bước"),
 ("queryPrefix(5)=40 là phần cộng thêm, tổng thực 54", "Slide 4: hoạt hình Next 2 bước"),
 ("BIT 2D 32MB vs SegTree 512MB, bù trừ 4 góc", "Slide 5: bảng bộ nhớ + công thức"),
 ("add(2,2,5) chạm 4 ô, queryRect 4 góc", "Slide 6: lưới 4x4 Next 2 bước"),
 ("Code RangeFenwick + Fenwick2D, tóm tắt 30 giây", "Slide 7: code + recap"),
 ("3 câu quiz có đáp án + bài tiếp theo", "Slide 8: quiz + outro"),
]
