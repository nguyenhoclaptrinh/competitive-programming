# Bài 3 - Dinic Max Flow

## 1. Bài toán

Mạng gồm nút nguồn `s`, nút đích `t`, mỗi cạnh có sức chứa `cap`.
Hỏi đẩy được bao nhiêu đơn vị dòng từ `s` tới `t`?

Ví dụ:

```
s --10--> A --10--> t
s --5---> B --5----> t
A --3---> B
```

Max flow = 15 (10 qua A-t + 5 qua B-t, cạnh A-B không cần dùng).

ICPC dùng flow cho: matching 2 phía, phân công, min-cut, đóng/mở dự án, grid thoát hiểm.

## 2. Ý tưởng Dinic

Lặp 2 bước cho tới khi hết đường:

1. **BFS** dựng `level[]` = khoảng cách (số cạnh) từ `s`. Chỉ giữ cạnh còn `cap > 0`.
   Nếu `t` không tới được -> dừng.
2. **DFS** đẩy flow trên level graph theo lớp tăng dần, dùng `it[]` (current arc)
   để không quét lại cạnh chết.

Độ phức tạp `O(E * V^2)` tổng quát, nhưng trên đồ thị 2 phía/matching chạy rất nhanh.

Thuật ngữ:

* **Residual graph:** mỗi cạnh `u->v cap c` có thêm cạnh ngược `v->u cap 0`
  để "hủy" flow đã đẩy sai.
* **Blocking flow:** DFS đẩy tới khi nghẽn hết đường tăng trong level hiện tại.

## 3. Code chuẩn (xem template.cpp)

```cpp
Dinic d(n);
d.addEdge(u, v, cap); // nếu vô hướng thì gọi 2 lần
cout << d.maxFlow(s, t);
```

Lưu ý: `addEdge` tự thêm cạnh ngược `cap=0`. Mọi `cap/flow` là `long long`.

## 4. Các mẫu dựng đồ thị hay gặp

**a) Bipartite matching (nam-nữ, việc-người):**
`source -> trái cap=1`, `trái -> phải cap=1` nếu có quan hệ, `phải -> sink cap=1`.
Max flow = số cặp tối đa.

**b) Min cut:** sau `maxFlow`, BFS trên residual từ `s`, nút nào thăm được thuộc phía S.
Tổng cap cắt = max flow.

**c) Grid / tách nút:** mỗi ô tách thành `in -> out cap=1` (giới hạn đi qua 1 lần),
cạnh kề `out -> in` của ô bên cạnh `cap=INF`.

## 5. Lỗi hay gặp

1. Dùng `int` cho cap/flow -> tràn khi cap tới 1e12. Luôn `long long`.
2. Quên `it[]` (current arc) -> TLE.
3. Đồ thị vô hướng mà chỉ `addEdge` 1 lần (thiếu chiều ngược có cap).
   Muốn vô hướng `c`: gọi `addEdge(u,v,c); addEdge(v,u,c);`
4. `INF` quá to (`4e18`) cộng dồn tràn. Dùng `INF = 4e14` hoặc `1e18` với kiểm tra.
5. DFS đệ quy sâu trên đồ thị dài 1e5 -> stack overflow. Flow thường đồ thị rộng
   nên OK, nhưng BFS/DFS phải iterative nếu cần.

## 6. Bài tập

1. CSES 1694 Download Speed (Dinic trần trụi).
2. CSES 1695 Police (in min-cut).
3. CSES 1707 / bipartite matching cơ bản (LOJ 1141, VNOJ `match1`).
4. VNOJ `nkflow` / evacuation grid.
