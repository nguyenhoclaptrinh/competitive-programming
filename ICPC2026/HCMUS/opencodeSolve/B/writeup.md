# Problem B: Freezer — Writeup

## 1. Nhận xét chất lượng

- `q <= 3`: không bao giờ ăn được (mỗi món trong bữa cần `q >= 4`). Loại bỏ.
- `q == 4` (loại A): cần ghép với `q >= 5` vì `4+4=8 < 9`.
- `q >= 5` (loại B): ghép được với mọi món dùng được (`A` hoặc `B`), vì `5+4=9`.

Vậy một bữa hợp lệ = 1 món `B` + 1 món bất kỳ (`A`/`B`), cả hai còn hạn (`e >= d`).

## 2. Quy về bài toán ghép slot

Với `K` ngày cố định, mỗi ngày `d` cần 2 món. Tách mỗi ngày thành 2 slot:

- Slot `H_d`: bắt buộc món `B`, chấp nhận `i` nếu `e_i >= d`.
- Slot `X_d`: chấp nhận món `A` hoặc `B`, nếu `e_i >= d`.

Một lịch ăn tồn tại khi và chỉ khi `2K` slot đều được gán các món phân biệt thỏa điều kiện trên
(cặp `B+B`: một món vào `H`, một vào `X`; cặp `A+B`: `B` vào `H`, `A` vào `X`).

Đây là ghép đôi hai phía (bipartite matching) với vùng kề lồng nhau theo `d`.

## 3. Greedy từ ngày muộn về sớm

Xét các ngày `d = K, K-1, ..., 1`. Gọi pool là các món chưa dùng có `e >= d`.
Khi giảm `d`, pool chỉ phình ra (món mới có `e == d` được thêm vào), và mọi món
trong pool đều ăn được cho mọi ngày sớm hơn. Do đó trong cùng một loại (`A`/`B`),
các món trong pool là tương đương nhau đối với tương lai — chỉ số lượng từng loại
mới quan trọng.

Tại ngày `d` cần 1 món `B` cho `H` và 1 món bất kỳ cho `X`. Để dành `B` cho các
ngày sớm hơn (mỗi ngày đều cần 1 `B`), slot `X` ưu tiên lấy `A` nếu còn, ngược lại
lấy `B`. Cụ thể:

```
thêm mọi món dùng được có e >= d vào pool (poolA / poolB)
nếu poolB rỗng hoặc tổng pool < 2: K không khả thi
lấy 1 B cho H; lấy 1 A (nếu có) cho X, ngược lại lấy thêm 1 B
```

Lập luận đổi chỗ (exchange argument): sau mỗi bước, tổng số món còn lại luôn giảm
đúng 2, còn số `B` còn lại được giữ lớn nhất có thể khi ưu tiên `A` cho slot `X`.
Mọi lịch khả thi khác đều có thể đổi về lựa chọn này mà không hỏng tính khả thi
của các ngày `1..d-1`. Nên greedy đúng khi và chỉ khi `K` khả thi.

Tính đơn điệu: lịch cho `K` cắt bỏ ngày `K` cho lịch `K-1`, nên khả thi giảm đơn
điệu theo `K`. Chặt nhị phân `K` trong `[0, floor(usable/2)]`.

Độ phức tạp: sắp xếp `O(n log n)`, mỗi lần kiểm tra `O(n + K)`, tổng
`O(n log n)` với chặt nhị phân. `n <= 2000` dư sức dưới 1s.

## 4. Dựng lịch

Chạy lại greedy với `K` lớn nhất, lưu chỉ số món thật (`poolA`/`poolB` chứa
`idx`). Vì các món cùng loại là tương đương, lấy phần tử bất kỳ (cuối stack)
đều cho lịch hợp lệ. Xuất cặp `(H_d, X_d)` cho `d = 1..K`.

## 5. Kiểm chứng

- Sample 1 → `K=3`, lịch hợp lệ (ví dụ ngày 3 dùng `4+5=9`).
- Sample 2 → `K=2`, món `e=1` bắt buộc ăn ngày 1.
- Đối chiếu brute-force (max-flow `2K` slot) trên 2000+300 test ngẫu nhiên nhỏ:
  greedy và max-flow cho cùng tính khả thi và cùng `K` tối ưu; lịch xuất ra
  được validator kiểm tra `e_d`, `q>=4`, tổng `>=9`, không dùng lại món.
- Test lớn `n=2000` ngẫu nhiên: chạy ~2ms, lịch hợp lệ.
