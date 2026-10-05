# Problem I — Danh the Happy Pig

## 1. Mô hình bước nhảy

Đứng tại `p` ở bước `i`, nhảy tới `p+i` hoặc `p+i+1`.
Sau `t` lần nhảy, vị trí là:

```
p = sum_{k=1..t} (k + b_k) = T_t + B
```

với `T_t = t(t+1)/2`, `b_k ∈ {0,1}`, `B = sum b_k ∈ [0,t]`.
Ngược lại mọi `p` đều viết được duy nhất dưới dạng này.

Điểm mấu chốt: các đoạn `[T_t, T_t+t]` rời nhau và phủ kín `N0`,
vì `T_{t+1} = T_t + t + 1`. Do đó **mỗi `p` thuộc đúng một tầng `t(p)`**,
chính là số bước nhảy đã đi để tới `p`.

## 2. Quy hoạch động

`dp[p]` = tổng happiness lớn nhất để tới được `p` (bao gồm `a_p`), `dp[0]=0`.

Nhảy cuối cùng tới `p` (ở tầng `t`) có độ dài `t` hoặc `t+1`,
nên tiền nhiệm chỉ có thể là `q = p-t` hoặc `q = p-t-1`,
và `q` phải ở tầng `t-1`, tức `T_{t-1} ≤ q ≤ T_{t-1}+t-1`.

Viết `p = T_t + b` (`0 ≤ b ≤ t`), thì `q1 = T_{t-1}+b`, `q2 = T_{t-1}+b-1`:

- `b = 0`: chỉ `q1` hợp lệ.
- `b = t`: chỉ `q2` hợp lệ.
- còn lại: cả hai hợp lệ, lấy max.

```
dp[T_t+b] = a_{T_t+b} + max(dp tiền nhiệm hợp lệ)
```

Mỗi `p` có ≤ 2 tiền nhiệm nên toàn bộ DP là `O(n)`.

## 3. Điều kiện kết thúc

Từ `p` (tầng `t`), bước tiếp theo dài `t+1` hoặc `t+2`.
Có thể thoát ngay từ `p` khi cú nhảy dài nhất vượt `n`:

```
p + t + 2 > n
```

Đáp án:

```
ans = max{ dp[p] : p ≤ n, p + t(p) + 2 > n }
```

Trường hợp biên `n = 1`: từ `0` có thể nhảy `2 > 1` thoát ngay được `0`
mà không ăn gì, nên khởi tạo `ans = 0`. Với `n ≥ 2` cả hai cú nhảy
đầu đều đáp xuống board nên bắt buộc ăn ít nhất một món.

## 4. Độ phức tạp

- Thời gian `O(n)`, `n ≤ 5e6` (~0.4s thực đo).
- Bộ nhớ `O(n)` cho `dp` int64 (~40MB) + mảng `a`; vừa dưới 1GB.
  (Có thể lăn 2 tầng để còn `O(√n)` bộ nhớ.)
- Dùng `int64` vì tổng tới `±5e15`; `ios::sync_with_stdio(false)`.

## 5. Kiểm chứng

- Sample `5 / 5 -2 8 0 -9` → `13` (đường `0→1→3→thoát`, `5+8`).
- Brute-force mũ (duyệt hết 2 lựa chọn mỗi bước) trên 300 test ngẫu nhiên
  `n ≤ 12` đều khớp.
- Test `n = 5e6` ngẫu nhiên chạy ~0.46s.
