# Problem G: Whisper Chain — Writeup

## 1. Phát biểu lại

`n` học sinh, mỗi `i` muốn `s_i` ngồi ngay sau mình: `chair(s_i) = chair(i)+1`.
Xếp hoán vị ghế (thứ tự `p[1..n]` là học sinh trên ghế `1..n`) để số cặp kề
`(p[k], p[k+1])` thỏa `s_{p[k]} = p[k+1]` là lớn nhất.
Xuất `M` tối đa và mảng `c[i]` (ghế của học sinh `i`, là nghịch đảo của `p`).

`n ≤ 10000`, `s_i ≠ i`.

## 2. Nhận xét then chốt: path cover

Lấy một cách xếp `p` và chỉ giữ các cạnh kề **thỏa wish**.
Mỗi đỉnh có ≤ 1 cạnh vào và ≤ 1 cạnh ra trong `p`, nên các cạnh thỏa tạo thành
tập các **đường đi rời nhau** mà mỗi cạnh đều thuộc đồ thị wish `i → s_i`.

Ngược lại, mọi phủ bằng đường đi rời nhau (path cover) mà cạnh đều là wish
có thể nối đuôi nhau thành một hoán vị đầy đủ: giả sử có `P` đường đi thì
nối chúng lại được `n - P` cạnh thỏa.

Vậy **max wish = max số cạnh trong path cover = `n − min số đường đi`**.

## 3. Đồ thị hàm (functional graph)

`s` là hàm: mỗi đỉnh ra đúng 1 cạnh. Mỗi thành phần liên thông yếu gồm
1 chu trình có hướng + cây hướng vào chu trình.

Chọn tập cạnh con của `s` sao cho mỗi đỉnh vào ≤ 1 (ra ≤ 1 tự động đúng)
và không có chu trình có hướng. Vì chu trình có hướng duy nhất có thể có
là các chu trình gốc của `s`, bài toán thành:

> Mỗi đỉnh `v` có bậc vào `> 0` thì giữ tối đa 1 cạnh vào; mỗi chu trình gốc
> phải hở ít nhất 1 chỗ.

Gọi:
- `Z` = số đỉnh bậc vào 0 (không ai muốn ngồi sau, không thể có cạnh vào được chọn),
- `C0` = số thành phần là **chu trình đơn thuần** (mọi đỉnh bậc vào đúng 1,
  không có cây bám vào).

Cận trên: tối đa `n − Z` cạnh (mỗi đỉnh có bậc vào > 0 giữ 1 cạnh).
Mỗi chu trình đơn thuần nếu giữ hết sẽ thành vòng tròn (không phải đường đi),
nên phải bỏ thêm ≥ 1 cạnh. Các thành phần khác nhau rời nhau nên:

```
M ≤ n − Z − C0
```

Cận này đạt được:
- Mỗi `v` có người muốn thì tạm chọn 1 cha `pred[v][0]`.
- Với mỗi chu trình gốc: nếu nó chưa được chọn hết (đã hở) thì xong;
  nếu được chọn hết thì: có cây bám vào (tồn tại `v` có `|pred[v]| ≥ 2`)
  thì đổi `choice[v]` sang cha ngoài chu trình (vẫn giữ đủ số cạnh,
  chu trình hở); nếu là chu trình đơn thuần thì xóa 1 cạnh (`choice = −1`).

Kết quả có đúng `n − Z − C0` cạnh, bậc vào ≤ 1, bậc ra ≤ 1, vô chu trình
→ là path cover tối ưu.

Việc nối các đường đi theo thứ tự bất kỳ đều cho đúng số wish đó:
đuôi `u` của một đường đi có `s[u]` là đỉnh trong (đã có cạnh vào) hoặc là
đầu của chính đường đó (trường hợp chu trình thuần), không bao giờ là đầu
của đường khác (khác thành phần liên thông), nên cạnh nối luôn không thỏa
(trừ đỉnh cuối cùng vốn không tính). Không có wish phụ nào phát sinh làm
sai số đếm, và tính tối đa đảm bảo không thể gộp thêm.

## 4. Thuật toán O(n)

1. Dựng `pred`, bậc vào.
2. `choice[v] = pred[v][0]` nếu có.
3. Tìm đỉnh chu trình bằng khử topo (queue bậc vào 0).
4. Với mỗi chu trình: kiểm tra có được chọn hết không; nếu có thì swap sang
   nhánh cây hoặc drop 1 cạnh nếu thuần.
5. Dựng `next[u] = s[u]` nếu `choice[s[u]] == u`.
6. Từ mỗi đỉnh `choice == −1` đi theo `next` thu thập đường đi, nối lại
   thành `order p`, nghịch đảo thành `c`, đếm `M`.

## 5. Đúng trên sample

- Sample 1: bậc vào 0 là `{1,5}` → `Z=2`; chu trình `(2,3,7)` có cây,
  chu trình `(4,8,6)` thuần → `C0=1`; `M = 9−2−1 = 6`. ✔
- Sample 2: một chu trình 5 đỉnh thuần → `Z=0, C0=1`, `M = 4`. ✔

Đã brute-force `n ≤ 8` trên 200 test ngẫu nhiên: `M` của chương trình trùng
max vét cạn; test `n = 10000` chạy ~4ms.

## 6. Code

`G.cpp`: C++17, O(n) thời gian, O(n) bộ nhớ.
