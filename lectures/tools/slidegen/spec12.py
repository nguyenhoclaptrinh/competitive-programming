#!/usr/bin/env python3
"""Spec bài 12: Số học (nCr, CRT, Pollard Rho)."""
from template import section, quiz, code_block, stepper_btns

SLUG = "12-math"
TITLE = "Bài 11: Số học — Hiểu sâu qua hình + tiếng"
H1 = "Bài 11: nCr modulo + CRT + Pollard Rho"

S1 = section("1/8 — nCr O(1): Fermat + giai thừa ngược", "fact xuôi 1 lần, invFact ngược 1 lần",
"""<p><code>C(n,r) = n!/(r!(n−r)!) mod MOD</code>, MOD nguyên tố. Fermat nhỏ: a<sup>−1</sup> = a<sup>MOD−2</sup>.</p>
<div class="grid8" id="f1"></div>
<div class="formula">fact[i] = fact[i−1]·i. invFact[MAX−1] = pow(fact[MAX−1],MOD−2). invFact[i] = invFact[i+1]·(i+1). Mỗi query đúng <b>1 phép nhân</b>.</div>""")

S2 = section("2/8 — CRT tổng quát: gcd > 1 vẫn gộp được", "Bấm Next gộp x≡2(3), x≡1(5) từng bước",
"""<p>x = m1·p+r1 = m2·q+r2 → m1·p − m2·q = r2−r1. Đặt g = gcd. <b>Có nghiệm ⟺ (r2−r1) ⋮ g</b>. Chu kỳ mới = lcm.</p>
<div class="cover" id="cov2">Ví dụ: x≡2 (mod 3), x≡1 (mod 5). Bấm Next.</div>
<div class="steps" id="cap2">g = gcd(3,5) = 1.</div>
""" + stepper_btns("s2"))

S3 = section("3/8 — Code extgcd + crtMerge + nCr", "Đệ quy Euclid mở rộng",
code_block("code12a", "C++20 · extgcd/crtMerge/nCr", """<span class="type">ll</span> <span class="fn">extgcd</span>(a,b,x,y){ <span class="kw">if</span>(!b){x=<span class="num">1</span>;y=<span class="num">0</span>;<span class="kw">return</span> a;}
  d=<span class="fn">extgcd</span>(b,a%b,x1,y1); x=y1; y=x1-y1*(a/b); <span class="kw">return</span> d; }
<span class="type">bool</span> <span class="fn">crtMerge</span>(r1,m1,r2,m2,rem,mod){ g=<span class="fn">extgcd</span>(m1,m2,x,y);
  <span class="kw">if</span>((r2-r1)%g) <span class="kw">return false</span>; <span class="com">// vô nghiệm</span>
  k=((r2-r1)/g%step)*(x%step)%step; <span class="kw">if</span>(k&lt;<span class="num">0</span>)k+=step;
  mod=m1/g*m2; rem=(r1+k*m1)%mod; <span class="kw">return true</span>; }""") + """
<div class="formula">📌 <b>Tóm tắt 30 giây:</b> nCr = fact·invFact · CRT = extgcd + check chia hết · Rho = random + gcd.</div>""")

S4 = section("4/8 — Pollard Rho: sinh nhật tìm ước", "Bấm Next xem vòng lặp Brent bắt ước",
"""<p>N tới 10<sup>18</sup>, √N = 10<sup>9</sup> thử chia là chết. Dãy giả ngẫu nhiên x ← (x²+c) mod N: chu trình modulo ước p xuất hiện sau O(√p) bước.</p>
<div class="cover" id="cov4">N = 91 = 7·13. x=2, y=2, c=1. Bấm Next từng vòng.</div>
<div class="steps" id="cap4">y = f(y) = 5, g = gcd(|2−5|,91) = gcd(3,91) = 1.</div>
""" + stepper_btns("s4") + """
<div class="tip">Miller-Rabin 12 cơ số {2..37} đúng 100% với N &lt; 2<sup>64</sup> — dùng để dừng Rho đúng lúc.</div>""")

S5 = section("5/8 — Code mulMod + Miller-Rabin + Rho", "__int128 nhân không tràn",
code_block("code12b", "C++20 · isPrime64/pollardRho/factorize", """<span class="type">ll</span> <span class="fn">mulMod</span>(a,b,m){ <span class="kw">return</span> (<span class="type">u128</span>)a*b%m; } <span class="com">// 128-bit</span>
<span class="type">bool</span> <span class="fn">isPrime64</span>(n){ small primes trial; d=n-<span class="num">1</span>,s=<span class="num">0</span>;
  <span class="kw">while</span>(!(d&amp;<span class="num">1</span>)){d&gt;&gt;=<span class="num">1</span>;s++;} <span class="kw">for</span>(a:bases){...} }
<span class="type">ll</span> <span class="fn">pollardRho</span>(n){ <span class="kw">if</span>(n%<span class="num">2</span>==<span class="num">0</span>)<span class="kw">return</span> <span class="num">2</span>;
  <span class="kw">if</span>(<span class="fn">isPrime64</span>(n))<span class="kw">return</span> n; Brent+GCD... }
<span class="type">void</span> <span class="fn">factorize</span>(n,f){ <span class="kw">if</span>(n==<span class="num">1</span>)<span class="kw">return</span>;
  <span class="kw">if</span>(prime)f.<span class="fn">push_back</span>(n); <span class="kw">else</span>{d=rho(n);recurse d,n/d;} }""") + """
<div class="warn">⛔ MSVC không có __int128 — cần mul portable. rand() yếu → dùng mt19937_64.</div>""")

S6 = section("6/8 — Bẫy ICPC số học", "MOD, tràn, seed, bases",
"""<ul><li>nCr: MOD phải nguyên tố, không thì Lucas/phân tích MOD.</li>
<li>CRT: m1/g·m2 tràn 128-bit → nhân bằng <code>__int128</code>.</li>
<li>Pollard seed bằng steady_clock; N &lt; 2³² chỉ cần bases {2,7,61}.</li></ul>""")

S7 = section("7/8 — Ứng dụng: ước, phi, Fib", "Từ factorize ra mọi thứ",
"""<ul><li>Số ước: Π(e<sub>i</sub>+1). Phi Euler: Π p<sub>i</sub><sup>e<sub>i</sub>−1</sup>(p<sub>i</sub>−1).</li>
<li>Fibonacci mod: ma trận [[1,1],[1,0]]<sup>n</sup> hoặc fast doubling O(log n).</li>
<li>Rho: phân tích N lớn cho đồng dư modulo hợp số.</li></ul>""")

S8 = section("8/8 — Tự kiểm tra 3 câu", "Đáp án đã kiểm chứng bằng code",
quiz(1, "nCr(10,3) mod 1e9+7?", "✅ <b>120</b> — 10·9·8/6.") +
quiz(2, "x≡2 (mod 4), x≡3 (mod 6). Nghiệm?", "✅ <b>Vô nghiệm</b> — g=2, (3−2)=1 không chia hết cho 2.") +
quiz(3, "isPrime64(1000000007)?", "✅ <b>true</b> — 1e9+7 nguyên tố, Miller-Rabin 12 cơ số xác định.") + """
<div class="formula">🎯 <b>Hết 11 bài giảng ICPC Handbook</b> — ôn lại bài 1→11 theo README.</div>""")

CUSTOM_JS = """
drawBars('f1',[{v:'0!',l:'fact'},{v:'1!',l:''},{v:'2!',l:''},{v:'…',l:''},{v:'N!',l:''},{v:'inv',l:'invF'},{v:'…',l:''},{v:'0',l:''}]);
defSteps('s2','cap2',[
 {cap:'<b>Bước 1:</b> g = gcd(3,5) = 1. (r2−r1) = −1 chia hết cho 1 → <b>có nghiệm</b>, chu kỳ 15.',run:()=>{document.getElementById('cov2').innerHTML='g=<b>1</b>, lcm=<b>15</b>.';}},
 {cap:'<b>Bước 2:</b> extgcd: 3·2 + 5·(−1) = 1 → x=2. k = (−1)·2 mod 5 = <b>3</b>.',run:()=>{document.getElementById('cov2').innerHTML='x=<b>2</b>, k=<b>3</b>.';}},
 {cap:'<b>Bước 3:</b> rem = (2 + 3·3) mod 15 = <b>11</b>. Kiểm tra: 11%3=2 ✓, 11%5=1 ✓.',run:()=>{document.getElementById('cov2').innerHTML='x ≡ <b>11</b> (mod 15) ✓.';}}
],'g = gcd(3,5) = 1.');
ST['s2'].reset=()=>{document.getElementById('cov2').innerHTML='Ví dụ: x≡2 (mod 3), x≡1 (mod 5). Bấm Next.';};
defSteps('s4','cap4',[
 {cap:'<b>Vòng 1:</b> y 2→5: g=gcd(3,91)=1. y 5→26: g=gcd(24,91)=1. Brent cho x nhảy lên 26.',run:()=>{document.getElementById('cov4').innerHTML='Chưa bắt được ước (g=1 liên tục).';}},
 {cap:'<b>Vòng 2:</b> y 26→40: g=gcd(14,91)=<b>7</b> → ước thật! 91=7·13, đệ quy 2 nhánh nguyên tố.',run:()=>{document.getElementById('cov4').innerHTML='g=<b>7</b> → 91 = 7·13 ✓. Đệ quy factorize 2 nhánh.';}}
],'y = f(y) = 5, g = gcd(|2−5|,91) = gcd(3,91) = 1.');
ST['s4'].reset=()=>{document.getElementById('cov4').innerHTML='N = 91 = 7·13. x=2, y=2, c=1. Bấm Next từng vòng.';};
"""

MANIFEST = [
 ("Bài 11: nCr modulo + CRT + Pollard Rho", "1/8 · Fermat fact/invFact O(1)", "MAX=1e6, 1 phép nhân/query", "", ""),
 ("CRT: gộp x≡2(3),x≡1(5) → x≡11(15)", "2/8 · extgcd + check chia hết", "Mở slides.html Slide 2, bấm Next", "", ""),
 ("Code extgcd/crtMerge/nCr", "3/8 · đệ quy Euclid mở rộng", "Tóm tắt 30 giây cuối slide", "", "extgcd // check g // k,rem,mod"),
 ("Pollard Rho N=91: Brent bắt ước 7", "4/8 · random+gcd, Miller-Rabin dừng", "Mở slides.html Slide 4, bấm Next", "", ""),
 ("Code mulMod128 + Rabin + Rho + factorize", "5/8 · u128 nhân không tràn", "MSVC/mt19937 lưu ý", "", "u128 // 12 bases // Brent // đệ quy"),
 ("Bẫy: MOD nguyên tố, tràn 128, seed, bases", "6/8 · Lucas nếu MOD hợp", "4 bẫy sống còn", "", "MOD ntố // 128-bit // seed clock // 2,7,61"),
 ("Ứng dụng: số ước, phi Euler, Fib ma trận", "7/8 · từ factorize ra hết", "3 ứng dụng", "", "ước // phi // Fib log n"),
 ("Quiz: 120; vô nghiệm; 1e9+7 prime", "8/8 · đáp án kiểm chứng bằng code", "Hết 11 bài giảng", "", "120 // vô nghiệm // prime true"),
]

SCRIPT_ROWS = [
 ("nCr Fermat fact/invFact O(1)", "Slide 1: công thức + bảng"),
 ("CRT gộp x≡11(15) 3 bước", "Slide 2: hoạt hình Next 3 bước"),
 ("Code extgcd/crtMerge/nCr", "Slide 3: code + recap"),
 ("Pollard Rho bắt ước 7 của 91", "Slide 4: hoạt hình Next 2 bước"),
 ("Code Rabin+Rho+factorize", "Slide 5: code + lưu ý"),
 ("4 bẫy số học", "Slide 6: bẫy"),
 ("Ước, phi, Fib", "Slide 7: ứng dụng"),
 ("3 câu quiz có đáp án, tổng kết", "Slide 8: quiz + outro"),
]
