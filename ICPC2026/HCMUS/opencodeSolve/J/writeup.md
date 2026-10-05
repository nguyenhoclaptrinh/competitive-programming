# Problem J: Crafting Costs — Writeup

## 1. Mô hình

- `dist[i]` = chi phí rẻ nhất để có 1 linh kiện loại `i`.
- Luôn có lựa chọn mua: `dist[i] <= p[i]`.
- Mỗi công thức `j`: `t_j` từ các inputs phân biệt `a_1..a_k`, phí `c_j`:
  `dist[t_j] <= c_j + Σ dist[a_s]`.
- Dùng công thức bao nhiêu lần cũng được, đồ dùng rồi mất (mỗi chỗ cần là một bản riêng — đúng bằng công thức cộng tổng ở trên, không dùng chung).
- Đồ thị có thể có chu trình (kể cả tháo máy lớn lấy linh kiện nhỏ).

Mục tiêu: với mỗi `i`, tìm chi phí của cây suy dẫn hữu hạn rẻ nhất có gốc `i`, lá là các lần mua.

## 2. Quan sát then chốt

Mọi chi phí tối ưu đều `>= 1` (vì `p_i >= 1`, `c_j >= 0`, mỗi công thức cộng tổng các chi phí dương).
Do đó với công thức `j`:

```
cost(j) = c_j + Σ dist[input] >= max dist[input]
```

dấu `=` chỉ khi `k = 1, c = 0`; còn nếu `k >= 2` thì `cost(j) >` từng input một cách chặt
(vì các inputs còn lại mỗi cái `>= 1`).

Hệ quả: chi phí công thức luôn "trội" hơn input lớn nhất của nó. Đây chính là điều kiện
để chạy kiểu Dijkstra trên siêu-đồ-thị (hypergraph): một công thức chỉ có thể cho ra
giá trị `< v` khi mọi input của nó đã có giá trị cuối `< v` (hoặc `<= v` trong trường hợp
`k = 1, c = 0`). Chu trình không bao giờ có lợi: mọi suy dẫn chứa chu trình đều đắt hơn
nghiêm ngặt (hoặc bằng, với chu trình 0-phí đơn) so với bản cắt chu trình.

## 3. Thuật toán (Dijkstra trên hypergraph)

- Khởi tạo `dist[i] = p[i]`, ném cả `n` đỉnh vào min-heap.
- Mỗi công thức `j` lưu:
  - `rem[j]` = số inputs chưa "chốt" (finalized),
  - `sum[j]` = tổng `dist` cuối của các inputs đã chốt.
- Lặp: pop `(d, v)` nhỏ nhất khỏi heap (bỏ entry cũ). Chốt `v` (`done[v] = true`,
  `d` chính là đáp án tối ưu — chứng minh ở mục 4). Với mỗi công thức `r` nhận `v`
  làm input mà `t_r` chưa chốt: `sum[r] += d; rem[r]--`. Khi `rem[r] == 0`
  (mọi input đã chốt), tính `cand = sum[r] + c[r]`; nếu `cand < dist[t_r]` thì
  nới lỏng `dist[t_r] = cand` và push heap.
- Công thức có `t_r` đã chốt thì bỏ qua (không thể cải thiện nữa).

Độ phức tạp: mỗi cạnh input→công thức duyệt đúng 1 lần khi input được chốt:
`O((n + Σk) log n)`, bộ nhớ `O(n + Σk)`. Với `Σk <= 5e5` thoải mái trong 3s/256MB.
Dùng `int64` vì tổng có thể tới `~2·10^14`.

## 4. Vì sao pop-min là đáp án cuối (phác thảo đúng đắn)

- Bất biến: `dist` hiện tại luôn là cận trên của đáp án thật `d*`
  (mua trực tiếp là một phương án; mỗi `cand` từ cận trên cũng là cận trên).
- Xét tập chưa chốt `U`, gọi `v = argmin d*` trên `U`. Lấy cây suy dẫn tối ưu của `v`
  có độ sâu nhỏ nhất. Nếu công thức gốc của nó có `k >= 2` hoặc `c > 0` thì mọi input
  đều có `d*` nhỏ hơn chặt → đã nằm trong tập chốt `F`. Nếu là chuỗi `k = 1, c = 0`
  thì đi xuống input (cùng `d*`, độ sâu nhỏ hơn) cho tới khi gặp nút dùng công thức
  loại kia hoặc mua trực tiếp — nút đó dùng toàn `F`/mua và đã được nới lỏng đúng
  bằng `d*`. Chu trình 0-phí cũng phải neo vào một lần mua nên lập luận vẫn dừng.
- Vậy tồn tại nút trong `U` mà `dist` hiện tại đã bằng `d*` và bằng `min d*` trên `U`;
  mà mọi nút khác có `dist >= d* >=` giá trị đó, nên min-heap pop đúng nút tối ưu.
  Quy nạp theo thứ tự pop ⇒ mọi nút chốt đều đúng, và công thức kích hoạt khi đủ
  inputs cho ra đúng `cost` thật nên không có nới lỏng muộn nào cải thiện nút đã chốt.

## 5. Kiểm thử

- Sample 1 → `75 30 40 78 10` ✓ (khớp đề).
- Sample 2 (`m = 0`) → `7 3 9 2` ✓.
- Sample 3 (cần 2 linh kiện loại 3) → `12 6 6` ✓.
- Tự kiểm: chu trình 0-phí `1↔2, p=[5,7]` → `5 5`; chuỗi `3→2→1` → `1 1 1`.

## 6. Code

Xem `J.cpp` (C++17, `int64`, fast IO).
