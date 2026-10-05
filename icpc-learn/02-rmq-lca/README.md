# Bài 2 - RMQ + LCA

## 1. RMQ là gì?

RMQ = Range Minimum/Maximum Query.
Cho mảng tĩnh `a[0..n-1]` (không update), hỏi nhiều lần `min(l,r)`.

* Prefix sum chỉ làm được tổng, không làm được min.
* Segment tree làm được O(log n)/query, nhưng quá thừa cho mảng tĩnh.
* Sparse Table làm O(1)/query sau khi build O(n log n).

## 2. Sparse Table

Chia mọi đoạn thành 2 nửa chồng lấp có độ dài lũy thừa của 2.

```
st[k][i] = min của đoạn dài 2^k bắt đầu tại i
st[0][i] = a[i]
st[k][i] = min(st[k-1][i], st[k-1][i + 2^(k-1)])
```

Truy vấn `[l, r]` (inclusive):

```
len = r - l + 1, k = floor(log2(len))
ans = min(st[k][l], st[k][r - 2^k + 1])
```

Hai nửa chồng nhau cũng không sao vì `min` có tính幂 đẳng (idempotent).
Tổng/gcd cũng OK. Tổng thì không vì chồng sẽ đếm 2 lần.

Ví dụ `a = [5,2,8,1,9]`, hỏi `min(1,3) = min(2,8,1)`:

* `len=3, k=1 (2^1=2)`
* `min(st[1][1], st[1][2]) = min(min(2,8), min(8,1)) = min(2,1) = 1`. Đúng.

**Nhớ:** tính `lg[i] = floor(log2(i))` bằng mảng, đừng gọi `log2()` float.

## 3. Khi nào dùng Sparse Table vs Segment vs Fenwick

| Cấu trúc | Update? | Query | Dùng khi |
|---|---|---|---|
| Prefix sum | không (hoặc O(n)) | tổng O(1) | mảng tĩnh, chỉ tổng |
| Sparse Table | không | min/max/gcd O(1) | mảng tĩnh, nhiều query |
| Fenwick | có (điểm) | tổng O(log n) | tổng động |
| Segment tree | có | mọi thứ O(log n) | min/max/sum động |

## 4. LCA - Tổ tiên chung gần nhất

Cây có gốc (ví dụ gốc 1). `LCA(u,v)` là nút sâu nhất vừa là tổ tiên của `u` vừa của `v`.

Ứng dụng: `dist(u,v) = depth[u] + depth[v] - 2*depth[lca]`.

### Binary lifting (cách chuẩn để học)

Tiền xử lý `up[k][v]` = tổ tiên nhảy `2^k` bước từ `v`.

```
up[0][v] = cha trực tiếp
up[k][v] = up[k-1][ up[k-1][v] ]
```

Nâng `u` lên cùng độ sâu với `v`, rồi nâng cả hai cùng lúc từ to xuống nhỏ.

Ví dụ cây: `1-2, 1-3, 2-4, 2-5`. `LCA(4,5)=2`, `LCA(4,3)=1`.

Các bước `lca(4,5)`:

* `depth[4]=depth[5]` nên không cần cân.
* Thử nhảy `2^1=2`: `up[1][4]=1, up[1][5]=1` bằng nhau -> không nhảy.
* Nhảy `2^0=1`: `up[0][4]=2, up[0][5]=2` bằng nhau -> không nhảy, nhưng cha của chúng là đáp án.
* Trả `up[0][4] = 2`. Đúng.

Code chi tiết xem `template.cpp` (bản iterative BFS, không đệ quy để tránh stack overflow n=1e5).

## 5. Lỗi hay gặp

1. Dùng `log2()` float -> sai 1 đơn vị với số lớn. Dùng mảng `lg[]`.
2. Sparse Table để `st[20][MAXN]` sai chiều gây cache miss / tràn stack nếu để local. Để `vector<vector<>>` hoặc static global.
3. LCA đệ quy DFS trên cây thẳng 1e5 -> segfault. Dùng BFS/stack.
4. Quên `depth[root]=0`, `up[*][root]=root` hoặc 0 và xử lý tương ứng.
5. Nhầm 0-based/1-based giữa các template.

## 6. Bài tập

1. CSES 1647 Static Range Minimum Queries (Sparse Table).
2. CSES 1688 Company Queries I (binary lifting cơ bản).
3. CSES 1687 / 1688 LCA + distance `dist(u,v)`.
4. SPOJ LCA hoặc VNOJ `lca` cơ bản.
