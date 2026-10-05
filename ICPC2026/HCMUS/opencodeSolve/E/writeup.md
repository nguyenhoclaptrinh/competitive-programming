# Problem E — Danh the Pig Emperor (Hợp các tam giác vuông cân)

## 1. Hình học của một kim tự tháp

Tam giác thứ `i` có đáy `[l_i, r_i]` trên `Ox`, đỉnh góc vuông hướng lên.
Gọi `w = r - l`, trung điểm `m = (l+r)/2`.

Vì là tam giác vuông cân, cạnh huyền là đáy, đường cao từ góc vuông
xuống cạnh huyền bằng nửa cạnh huyền:

```
h = w / 2, đỉnh tại (m, h).
```

Với mỗi `x in [l, r]`, lát cắt đứng của tam giác là đoạn `[0, f_i(x)]` với:

```
f_i(x) = min(x - l_i, r_i - x),  x in [l_i, r_i]
f_i(x) = không xác định (rỗng) ngoài đoạn này.
```

Đây là hàm "lều" (tent): tăng slope `+1` trên `[l, m]`, giảm slope `-1`
trên `[m, r]`, đỉnh `h` tại `m`.

## 2. Quy về bao trên (upper envelope)

Mọi tam giác đều bám đáy `y = 0`, nên với mỗi `x` cố định, hợp các lát cắt
`[0, f_i(x)]` cũng là một đoạn `[0, max_i f_i(x)]` (quy ước max rỗng = 0).

Do đó:

```
Area(union) = ∫ max_i f_i(x) dx
```

Bài toán thành tính diện tích dưới đường bao trên của `N` hàm lều.

## 3. Nhân đôi tọa độ để tránh số lẻ

`m = (l+r)/2` có thể lẻ `.5`. Đặt `X = 2x`, `l' = 2l`, `r' = 2r`, `m' = l+r`
(đều nguyên). Đặt:

```
g(X) = 2 * f(X/2) = min(X - l', r' - X), X in [l', r'].
```

Đổi biến: `dx = dX/2`, `f = g/2` nên:

```
Area = (1/4) ∫ g(X) dX  =>  Area*4 = ∫ g(X) dX.
```

Đáp án cần in chính là tích phân này — số nguyên theo đề bài.
Mọi breakpoint `l', m', r'` đều nguyên; `a' = 2l`, `b' = 2r` đều chẵn nên
giao điểm của một nhánh tăng và một nhánh giảm `(a'+b')/2` cũng nguyên.
Vì vậy mọi công thức hình thang đều có tử số chẵn ở tổng toàn cục
(xem mục 5), dùng `__int128` là an toàn.

Chặn trên: `X` trong `[-2e9, 2e9]`, `g <= 2e9`, nên `Area*4 <= 8e18`
vừa khít `int64`, nhưng tổng trung gian `(v0+v1)*D` có thể tới `~3.2e19`
nên bắt buộc dùng `__int128` cho biến tích lũy.

## 4. Sweep line: chỉ cần min l và max r

Tách mỗi lều thành 2 chân:

- chân trái trên `[l', m']`: `g(X) = X - l'`, slope `+1`;
- chân phải trên `[m', r']`: `g(X) = r' - X`, slope `-1`.

Thu thập mọi breakpoint phân biệt:

```
P = {2l_i} ∪ {l_i + r_i} ∪ {2r_i}, sắp xếp, |P| <= 6e5.
```

Giữa hai điểm liên tiếp `[P_k, P_{k+1}]`, không có đỉnh lều nào ở trong,
nên mỗi chân đang active sẽ phủ kín cả đoạn.
Trong cùng một đoạn, mọi chân trái song song nhau (slope `+1`), nên chân
tốt nhất là chân có `l'` nhỏ nhất; tương tự chân phải tốt nhất là chân có
`r'` lớn nhất:

```
bestA(X) = X - min_l,   bestB(X) = max_r - X.
g_max(X) = max(bestA, bestB, 0).
```

Vậy sweep chỉ cần duy trì:

- multiset các `l'` đang active (truy vấn min),
- multiset các `r'` đang active (truy vấn max).

Sự kiện tại `l'`: thêm chân trái; tại `m'`: xóa chân trái + thêm chân phải;
tại `r'`: xóa chân phải. Thứ tự xóa/thêm tại cùng `P_k` không quan trọng
vì thuộc 2 tập khác nhau (chứng minh trong code: không bao giờ có
add+remove cùng giá trị cùng vị trí).

Cài đặt hiệu quả không dùng `multiset` (nhiều cấp phát): nén `l'` và `r'`
về index, dùng 2 heap + mảng lazy-deletion `del[]`:

- `add`: push index vào heap;
- `remove`: `del[idx]++`;
- `query`: while heap top bị đánh dấu xóa thì pop.

Tổng `O((N+M) log N)`, thực đo `2e5` interval ngẫu nhiên ~0.25s.

## 5. Tích phân trên một đoạn elementary

Gọi `D = P_{k+1} - P_k`, `vA0, vA1` là `bestA` tại 2 đầu, `vB0, vB1` tương tự.

- Chỉ có A: `(vA0+vA1)*D/2`.
- Chỉ có B: `(vB0+vB1)*D/2`.
- Có cả hai:
  - nếu A trội khắp (`d0,d1 >= 0`) hoặc B trội khắp: như trên;
  - nếu cắt nhau trong đoạn: `X* = (a+b)/2` (nguyên), `Vc = (b-a)/2`,
    `D1 = X* - P_k`, `D2 = P_{k+1} - X*`, cộng 2 hình thang 2 bên.

Mỗi hình thang riêng lẻ có thể `.5` (ví dụ tam giác `0 1`: mỗi nửa cho
`0.5`), nhưng tổng toàn cục là nguyên. Vì vậy code cộng dồn tử số:

```
S += (v0+v1)*D   (cả 2 mảnh khi cắt nhau)
đáp án = S / 2.
```

`S` là `__int128`, chia 2 ở cuối rồi in thập phân thủ công.

## 6. Kiểm thử

- Sample: `2 / 0 4 / 2 6 -> 28` ✓.
- Đơn: `0 1 -> 1` (diện tích 0.25), `0 4 -> 16` ✓.
- Lồng nhau `0 6 + 1 3 -> 36` (chỉ tam giác lớn) ✓.
- Rời nhau `0 2 + 5 7 -> 8` ✓.
- Brute-force Python (bao gồm mọi giao điểm `(l_i+r_j)` và kiểm tra đỉnh
  giữa) trên 500 test ngẫu nhiên `N <= 8`, tọa độ `[-5, 6]`: khớp 100%.
- Perf: `N = 2e5` ngẫu nhiên 0.25s; worst-case trùng nhau / rời nhau 0.09s.

## 7. Độ phức tạp

Thời gian `O(N log N)`, bộ nhớ `O(N)`.
