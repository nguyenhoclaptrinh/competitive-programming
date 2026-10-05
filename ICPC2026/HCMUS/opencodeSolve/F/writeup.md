# Problem F — Wagon Sorting: Writeup

## 1. Mô hình

- Main track là queue vào `S[1..N]`.
- Siding là queue FIFO: `push_back` từ main, `pop_front` ra train.
- Train yêu cầu là tiền tố `1..M` theo đúng thứ tự.
- Wagon đã lên train thì ở yên; các wagon khác được phép nằm trên main hoặc siding.

## 2. Quan sát then chốt: kiểm tra `M` là đơn định (greedy ép buộc)

Cố định `M`, xét nhu cầu `need = 1..M` tăng dần, với con trỏ `i` trên main và hàng đợi `q` của siding.

Tại thời điểm cần `need = k`, chỉ có hai nơi chứa `k`:
- đầu siding (`q.front()`), hoặc
- phần chưa duyệt của main (`S[i..]`).

Vì các nhãn phân biệt, tối đa một nơi trùng. Nước đi bị ép buộc:

1. Nếu `q.front() == k`: cách duy nhất ra `k` là pop siding (vì `k` đã rời main, không còn trong `S[i..]`).
2. Ngược lại (`q` rỗng hoặc front khác `k`):
   - Không được pop siding (sẽ đưa wagon sai lên train).
   - Phải tiến `i` trên main tới vị trí của `k`, mọi wagon bị lướt qua đều **bắt buộc** vào siding (chúng khác `k` nên không được lên train, mà muốn tới `k` phải dời chúng đi).
   - Nếu `k` đã nằm trong `q` nhưng không ở front → tắc FIFO → không đạt được.
   - Nếu duyệt hết main mà không thấy `k` → không đạt được (trường hợp này chính là `k` bị kẹt trong siding).

Không có lựa chọn nào khác: thứ tự pop/push không ảnh hưởng thứ tự tương đối trong `q`. Vậy mọi chuỗi thành công đều phải trùng với greedy trên. Greedy thành công ⟺ `M` khả thi.

Hệ quả đơn điệu: đạt được `M` thì tiền tố của nó đạt được `M-1`, nên tập khả thi là `0..Mmax`.

## 3. Từ kiểm tra nhị phân về một pass tuyến tính

Kiểm tra `check(M)` theo greedy tốn `O(N)` vì `i` chỉ tiến, mỗi wagon vào/ra `q` tối đa một lần.

Nhưng vòng `need = 1,2,...` của `check(N)` khi giới hạn ở `k` bước đầu chính là `check(k)`. Do đó chỉ cần mô phỏng một lần từ `1..N`, dừng ở `k` đầu tiên thất bại; đáp án là `k-1` (hoặc `N` nếu không thất bại). Tổng `O(N)` thời gian, `O(N)` bộ nhớ.

```text
q = rỗng; i = 0; ans = 0
for need = 1..N:
  if q nonempty và q.front == need: q.pop_front(); ans = need; continue
  while i < N và S[i] != need: q.push_back(S[i]); i++
  if i == N: break        // need kẹt sau front của siding
  i++                    // S[i] == need đi thẳng lên train
  ans = need
in ans
```

Lưu ý: front của siding là wagon `> M` vẫn được phép nằm yên trong khi `need` lấy từ main (ví dụ `S = 3 1 2`, `M = 2`: `q = [3]`, lấy `2` từ main, train `[1,2]` hợp lệ). Code trên xử lý đúng vì không bắt pop khi front khác `need`.

## 4. Ví dụ

- `3 1 5 4 2 6`: sau `need=1,2`, `q=[3,5,4]`; lấy `3`; `need=4` bị chặn sau `5` → đáp án `3`.
- `2 4 1 3 5`: `1` lấy từ main sau khi đẩy `2,4`; pop `2`; lấy `3` từ main; pop `4,5` → đáp án `5`.

## 5. Độ phức tạp và chứng minh nhanh

- Thời gian `O(N)`, bộ nhớ `O(N)`, `N ≤ 1e5` dư sức dưới `1s`.
- Tính đúng: đã brute-force (BFS trạng thái) đối chiếu với greedy trên mọi hoán vị `N ≤ 6` và ngẫu nhiên `N = 10` — trùng khớp hoàn toàn.
- Hai sample đều ra `3` và `5`.
