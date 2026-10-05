# Bài 1 - Fenwick Tree (BIT)

## 1. Bài toán mở đầu

Cho mảng `a[1..n]`. Hai thao tác lặp đi lặp lại:

* `add(p, v)`: `a[p] += v`
* `sum(p)`: tính `a[1] + ... + a[p]`

Nếu dùng mảng thường: `add` O(1) nhưng `sum` O(n).
Nếu dùng mảng prefix: `sum` O(1) nhưng `add` O(n).

Fenwick cho cả hai O(log n).

Ý tưởng: không lưu từng số, không lưu toàn bộ prefix,
mà lưu các **đoạn có độ dài là lũy thừa của 2**.

```
bit[i] = tổng của đoạn (i - lowbit(i) + 1 .. i)
lowbit(i) = i & (-i)  // số 1 cuối cùng trong nhị phân
```

Ví dụ `n = 8`:

```
i (nhị phân)  lowbit  bit[i] quản lý
1 (001)       1       a[1]
2 (010)       2       a[1..2]
3 (011)       1       a[3]
4 (100)       4       a[1..4]
5 (101)       1       a[5]
6 (110)       2       a[5..6]
7 (111)       1       a[7]
8 (1000)      8       a[1..8]
```

## 2. Hai thao tác

```cpp
// cộng v vào a[p], lan lên các nút cha
void add(int p, long long v) {
    for (; p <= n; p += p & -p) bit[p] += v;
}
// tổng a[1..p], nhảy lùi về các đoạn con
long long sumPrefix(int p) {
    long long s = 0;
    for (; p > 0; p -= p & -p) s += bit[p];
    return s;
}
long long rangeSum(int l, int r) {
    return sumPrefix(r) - sumPrefix(l - 1);
}
```

Ví dụ tay `a = [1,2,3,4,5]`, `bit` sau build:
`add(1,1), add(2,2), ...` rồi `sumPrefix(3)`:

* `p=3 (011)` lấy `bit[3]=a[3]=3`, `p -= 1` -> `p=2`
* `p=2 (010)` lấy `bit[2]=a[1]+a[2]=3`, `p -= 2` -> `p=0` dừng
* Tổng = 6 = 1+2+3. Đúng.

## 3. Dựng mảng ban đầu

Cách 1 (dễ hiểu, O(n log n)): gọi `add(i, a[i])` n lần.
Cách 2 (nhanh O(n)): `bit[i] = a[i]`, rồi lan truyền:

```cpp
for (int i = 1; i <= n; i++) {
    int j = i + (i & -i);
    if (j <= n) bit[j] += bit[i];
}
```

Đi thi cứ dùng cách 1 cho chắc, n <= 2e5 vẫn kịp.

## 4. Ứng dụng 1: Đếm nghịch thế

Cặp `(i<j)` mà `a[i] > a[j]`.
Duyệt từ phải sang trái, BIT lưu tần suất giá trị đã gặp:

```cpp
long long inv = 0;
for (int i = n; i >= 1; i--) {
    inv += bit.sumPrefix(a[i] - 1); // có bao nhiêu số nhỏ hơn a[i] ở bên phải
    bit.add(a[i], 1);
}
```

Nếu `a[i]` tới 1e9 thì **nén tọa độ** trước (xem template).

## 5. Ứng dụng 2: Tìm số 1 thứ k (K-th one)

Mảng 0/1, tìm vị trí nhỏ nhất mà `sumPrefix(p) >= k`.
Nhảy nhị phân trên cây BIT, O(log n):

```cpp
// giả sử tổng toàn mảng >= k, k >= 1
int kth(long long k) {
    int p = 0;
    for (int pw = highestPowerOfTwo; pw > 0; pw >>= 1) {
        int nxt = p + pw;
        if (nxt <= n && bit[nxt] < k) {
            k -= bit[nxt];
            p = nxt;
        }
    }
    return p + 1;
}
```

Đây là cách thay `ordered_set::find_by_order` mà nhanh hơn nhiều.

## 6. Khi nào dùng / không dùng

* DÙNG khi: tổng trên đoạn + cập nhật điểm, bài tần suất, nghịch thế.
* KHÔNG DÙNG khi: cần `min/max` trên đoạn có cập nhật (dùng segment tree),
  cần range-add + range-min (dùng segment lazy), mảng tĩnh không update
  mà query nhiều (dùng prefix sum hoặc Sparse Table cho O(1)).

## 7. Lỗi hay gặp

1. Quên 1-based: BIT chuẩn chạy từ 1. `p=0` là bẫy vòng lặp vô hạn.
2. Dùng `int` cho tổng -> tràn. Luôn `long long bit[]`.
3. `rangeSum(l,r)` quên `l-1`.
4. Nén tọa độ sai: sort + unique rồi `lower_bound + 1`.

## 8. Bài tập (làm theo thứ tự)

1. Tự cài `add/sum/rangeSum`, test với `n=5` bằng tay.
2. Inversion count: https://oj.vnoi.info/problem/nkiv (hoặc CSES 1642 sơ lược).
3. CSES 1646 Dynamic Range Sum Queries.
4. CSES 1740 / K-th one: mảng 0/1, query tìm vị trí số 1 thứ k.

Xong bài này hãy sang `02-rmq-lca/`.
