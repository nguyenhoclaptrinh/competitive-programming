# Problem H: Raining — Writeup

## 1. Đề bài (tóm tắt)

Cho `q <= 1e5` điểm phân biệt `p1..pq` (sinh uniform ngẫu nhiên trong hình vuông
`[-1e9,1e9]^2`). Sau giây `t`, region mưa = bao lồi (convex hull) của `p1..pt`.
Damage = `2 * diện tích tam giác lớn nhất` có đỉnh nằm trong region.
In damage sau mỗi `t`. Đáp số là số nguyên (nhân 2 nên không cần số thực),
vừa trong `int64` (tối đa ~ `4e18`).

## 2. Nhận xét then chốt

- Tam giác diện tích lớn nhất trong một đa giác lồi luôn đạt được tại 3 đỉnh
  của đa giác. Vì vậy chỉ cần quan tâm tới đỉnh của convex hull, không cần
  toàn bộ miền liên tục.
- Điểm mấu chốt của đề: **điểm sinh uniform ngẫu nhiên**. Với điểm uniform
  trong hình vuông (hay mọi đa giác lồi cố định), số đỉnh hull kỳ vọng chỉ là
  `O(log n)` (với `n = 1e5` thực tế chỉ khoảng 20–35; test đo được hull cuối
  ~33). Nghĩa là hull rất nhỏ với xác suất cao.
- Do đó ta làm **online / incremental**: duy trì hull hiện tại; mỗi điểm mới
  nếu nằm trong hull thì đáp án giữ nguyên; nếu nằm ngoài mới cập nhật hull
  và tính lại tam giác lớn nhất. Số lần tính lại ít, mỗi lần rẻ vì `h` nhỏ.

## 3. Thuật toán

Duy trì `hull` (CCW, gọn, bỏ điểm thẳng hàng) và đáp án `cur`:

- `hull` rỗng / 1 điểm / đoạn thẳng: xử lý riêng (trường hợp thẳng hàng thì
  giữ cặp đường kính).
- Với `|hull| >= 3` và điểm mới `p`:
  - Kiểm tra `p` trong đa giác lồi: mọi cạnh `cross(h[i], h[i+1], p) >= 0`
    (bao cả biên). `O(h)` — vì `h` nhỏ nên đủ nhanh.
  - Nếu trong → `cur` không đổi.
  - Nếu ngoài → `newHull = convex_hull(hull + p)` (Andrew monotone chain,
    `O(h log h)`). Đúng vì `conv(p1..pt+1) = conv(hull_cu + p_{t+1})`:
    điểm trong cũ không bao giờ thành đỉnh mới.
  - Tính lại `cur = maxDoubleArea(newHull)`.

### Tam giác lớn nhất trong đa giác lồi — `O(h^2)` rotating calipers

Nhân đôi mảng hull (`q[i] = h[i % n]`). Với mỗi `i` cố định, duyệt `j = i+1..i+n-2`,
con trỏ `k` chỉ tiến (đơn điệu) sao cho `area(i,j,k)` cực đại:

```
best = 0
for i in 0..n-1:
    k = i+2
    for j in i+1..i+n-2:
        k = max(k, j+1)
        while k+1 < i+n and area(i,j,k+1) >= area(i,j,k): k++
        best = max(best, area(i,j,k))
```

Mỗi `i` tốn `O(n)` vì `j,k` mỗi con trỏ đi tối đa `n` bước → tổng `O(n^2)`.
Cross dùng `__int128` rồi ép về `long long` để tránh tràn
(`dx,dy` tới `2e9`, tích tới `4e18`, hiệu tới `8e18` — sát giới hạn `int64`).

## 4. Độ phức tạp

- Mỗi truy vấn: `O(h)` kiểm tra trong hull.
- Khi hull đổi (hiếm khi xảy ra với dữ liệu random, vì diện tích hull nhanh
  chóng phủ gần hết hình vuông): `O(h log h + h^2)`.
- Với `E[h] = O(log n)`: tổng kỳ vọng ~ `O(n log n)` cho `n = 1e5`, thực đo
  `~0.05s`. Bộ nhớ `O(h)`.
- Trường hợp xấu nhất (điểm trên đường tròn, `h = n`) thuật toán thành
  `O(n^3)` — nhưng theo đề bài test (trừ sample) là random nên không xảy ra.
  Sample nhỏ (`n = 10`) vẫn đúng.

## 5. Kiểm chứng

- Sample đề: `0 0 41 41 93 150 152 154 240 360` — khớp.
- Đối chiếu brute-force `O(t^3)` trên 20 test nhỏ ngẫu nhiên — đúng hết.
- Test random `n = 1e5`: `0.05s`, đáp án đơn điệu không giảm, hull cuối 33 đỉnh.
- Cạnh biên: 1 điểm, đoạn thẳng, thẳng hàng → đáp án `0`.
