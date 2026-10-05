# Problem L — Lucky Numbers (Số may mắn)

## 1. Phát biểu lại

Số lucky là số chia hết cho 3 (kể cả 0).
Cho `d[i]` = số lần tối đa được dùng chữ số `i`.
Có thể viết nhiều số (trùng nhau được), mỗi số viết thường
(không có số 0 ở đầu, trừ bản thân số `0`), không cần dùng hết chữ số.
Hỏi viết được nhiều nhất bao nhiêu số lucky?

## 2. Ý tưởng

Chỉ tổng các chữ số mod 3 quyết định chia hết cho 3.
Phân nhóm theo dư mod 3:

- `c0 = d0+d3+d6+d9` (dư 0)
- `c1 = d1+d4+d7` (dư 1)
- `c2 = d2+d5+d8` (dư 2)

### 2.1. Nhóm dư 0 luôn tách riêng

Mỗi chữ số dư 0 đứng một mình (`0,3,6,9`) đều chia hết cho 3,
kể cả số `0` một chữ số là hợp lệ.

Gộp một chữ số dư 0 vào nhóm khác không bao giờ có lợi:
nếu nhóm hợp lệ chứa chữ số dư 0, bỏ chữ số đó ra thì phần còn lại
vẫn có tổng chia hết cho 3. Tách ra được:

- `1 nhóm -> 2 nhóm` (ví dụ `{3,1,2} -> {3} + {1,2}`),
- hoặc nhiều hơn (ví dụ `{3,1,1,1} -> {3} + {1,1,1}`).

Trường hợp phần còn lại là số có nhiều chữ số 0 (như `00`, cấm
viết vì số 0 ở đầu) thì tách thành các số `0` đơn còn lợi hơn.
Vậy tồn tại nghiệm tối ưu giữ toàn bộ `c0` chữ số làm `c0` số đơn.
Không mất mát gì.

Hệ quả: ràng buộc "không số 0 ở đầu" coi như hết hiệu lực, vì:

- các số từ nhóm `c0` là số 1 chữ số (hợp lệ),
- các chữ số dư 1, dư 2 đều khác 0 (`1,4,7,2,5,8`),
  nên mọi số ghép từ chúng tự động không có số 0 ở đầu.

### 2.2. Nhóm dư 1 và dư 2

Chỉ còn `c1, c2`. Muốn tổng chia hết cho 3:

- 1 chữ số dư 1 + 1 chữ số dư 2 (2 chữ số -> 1 số, ví dụ `12`),
- 3 chữ số dư 1 (3 chữ số -> 1 số, ví dụ `111`),
- 3 chữ số dư 2 (3 chữ số -> 1 số, ví dụ `222`).

Loại cặp `(1,2)` dùng ít chữ số nhất cho mỗi số (2 chữ số/số
so với 3 chữ số/số) nên ưu tiên ghép cặp trước:

```
pairs = min(c1, c2)
c1 -= pairs; c2 -= pairs
extra = pairs + c1/3 + c2/3
ans = c0 + extra
```

Tính tối ưu: mỗi số 3 chữ số cùng dư có thể thay bằng đối chứng
ghép cặp mà không giảm số lượng (lập luận đổi chỗ chuẩn cho bài
chia hết cho 3). Nên tham lam cặp trước là tối ưu.

## 3. Công thức

```
c0 = d0+d3+d6+d9
c1 = d1+d4+d7
c2 = d2+d5+d8
pairs = min(c1,c2); c1 -= pairs; c2 -= pairs
ans = c0 + pairs + c1/3 + c2/3
```

Kiểm tra sample:

1. `1 1 1 0 0 3 0 0 0 1`: `c0=2, c1=1, c2=4` -> `2+1+1=4`.
2. `0 1 0 0 1 0 0 0 0 0`: `c0=0, c1=2, c2=0` -> `0`.
3. `2 4 0 1 3 1 0 0 2 0`: `c0=3, c1=7, c2=3` -> `3+3+1=7`.

## 4. Độ phức tạp & cài đặt

- Thời gian `O(1)`, bộ nhớ `O(1)`.
- Dùng `int64` (`long long`) vì tổng có thể tới `1e7`.
- C++17, đọc 10 số, in 1 số.
