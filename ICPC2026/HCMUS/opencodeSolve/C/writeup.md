# Problem C: Fluorine's Fun Function — Writeup

## 1. Đề bài (tóm tắt)
- Mảng `a[1..n]`, `F(1)=F(2)=1`, `F(k)=F(k-1)+F(k-2)`.
- Query `1 l r x`: `a[i] += x` với mọi `i in [l,r]` (đảm bảo `a[i] >= 1` mọi thời điểm).
- Query `2 l r`: tính `sum F(a[i]) mod 1e9+7`.
- `n,q <= 2e5`, `a[i],|x| <= 1e9`.

## 2. Ý tưởng
Dùng ma trận Fibonacci:

```
M = |1 1|
    |1 0|,  V(n) = |F(n+1)|,  V(n+1) = M * V(n).
                 |F(n)  |
```

Cộng `x` vào chỉ số tương đương nhân vector với `M^x`:

```
V(n+x) = M^x * V(n).
```

Tổng trên đoạn cũng biến đổi tuyến tính như vậy. Với mỗi node segment tree lưu:

- `S0 = sum F(a[i])`, `S1 = sum F(a[i]+1)`.
- lazy là ma trận `2x2` `L` (ban đầu `I`), ý nghĩa đoạn này còn nợ phép nhân `L`.

Khi áp ma trận `Mx = M^x` vào node:

```
[S1'] = Mx * [S1]
[S0']         [S0]
L' = Mx * L
```

Push lan `L` xuống 2 con rồi reset về `I`.

## 3. Tính `M^x`, kể cả `x` âm
Với `F0=0, F1=1` và `x >= 0` (fast doubling):

```
M^x = |F(x+1) F(x)  |
      |F(x)   F(x-1)|
```

`M` khả nghịch (`det = -1`) nên `x` âm vẫn có nghĩa (tương ứng trừ chỉ số Fibonacci).
Với `n = |x| > 0`, `Fn=F(n)`, `Fn1=F(n+1)`, `Fnm1=Fn1-Fn`:

```
M^{-n} = (-1)^n * | Fnm1  -Fn |
                   | -Fn    Fn1|
```

Đây cũng chính là công thức Negafibonacci `F(-n)=(-1)^{n+1}F(n)`.
Điểm mấu chốt về hiệu năng: mỗi query type-1 chỉ tính `Mx` **một lần** bằng fast doubling
`O(log|x|)`, rồi áp vào `O(log n)` node, mỗi node chỉ `O(1)` (nhân ma trận `2x2` với
vector và hợp nhất lazy). Không tính lại Fibonacci cho từng node.

## 4. Độ phức tạp
- Build: `n` lần fast doubling `O(n log Amax)`.
- Mỗi `1 l r x`: `O(log|x| + log n)`.
- Mỗi `2 l r`: `O(log n)`.
- Bộ nhớ: `4n` node, mỗi node 2 tổng + 4 số lazy.

Tổng: `O((n+q) log n + q log C)`, đủ cho `2e5` trong 2s.

## 5. Chi tiết cài đặt (`C.cpp`)
- `fib_pair(n)`: fast doubling đệ quy trả về `{F(n),F(n+1)}` mod `1e9+7`, `n >= 0`.
- `mat_pow_shift(x)`: trả về `M^x` theo 2 trường hợp `x>=0` / `x<0` như trên, chú ý
  `(-1)^n`: `n` chẵn `-> +1`, `n` lẻ `-> -1` (mod `MOD`).
- Segment tree mảng `sum0,sum1,lz00,lz01,lz10,lz11`, hàm `apply_node/push/build/update/query`.
- `x == 0` thì bỏ qua để đỡ tốn công.
- Mọi phép nhân dùng `long long` (`(MOD-1)*(MOD-1) < 2^63`).

## 6. Test
- Sample: `4 4 / 1 2 3 4 ...` -> `7 11 9` (khớp).
- Stress 100 test ngẫu nhiên `n<=20` đối chiếu brute-force (Fib tính trực tiếp): pass.
- Test `a=14, x=-6 -> F(8)=21`; `a=7,+7,-6 -> 21`: pass (từng sai dấu `(-1)^n` đã sửa).
