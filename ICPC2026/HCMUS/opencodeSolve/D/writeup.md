# Problem D: Tidal Wave — Writeup

## 1. Mô hình

Grid `n × m`. Ô `(i,j)` đi được iff `L_j ≤ i ≤ R_j` với:
- `L_j = l_j + 1`
- `R_j = n - r_j`
- Nếu `L_j > R_j`: cột `j` bị chặn hoàn toàn.

Từ `(i,j)` chỉ đi tới `(i±1, j+1)`, không ra ngoài `[1,n]`.
Xuất phát `(1,1)` (đảm bảo `L_1 = 1`, `R_1 ≥ 1`).
Cần tới cột `m` bất kỳ ô nào đi được.

Nhận xét parity: `i+j` luôn chẵn (khởi đầu `1+1=2`, mỗi bước `+2/0`).
Nên cột `j` chỉ chứa hàng cùng parity với `j` (lẻ/lẻ, chẵn/chẵn).

## 2. Tập 도달 là interval chẵn/lẻ

Gọi `S_j ⊆ [L_j,R_j]` là tập hàng tới được ở cột `j`.
Công thức: `S_{j+1} = (S_j - 1 ∪ S_j + 1) ∩ [L_{j+1}, R_{j+1}]`.

**Mệnh đề:** `S_j = { x ∈ [lo_j, hi_j] : x ≡ p_j }` (interval liên tục theo bước 2).

Chứng minh quy nạp:
- `S_1 = {1} = [1,1]`, parity lẻ.
- Giả sử đúng cho `j`. Khi mở rộng `±1`:
  `[lo_j-1, hi_j+1]` với parity đảo `p_{j+1}=1-p_j`.
- Giao với `[L_{j+1},R_{j+1}]` (cũng là interval liên tục) vẫn là dạng trên:
  `[max(lo_j-1,L), min(hi_j+1,R)]` lọc theo parity.
- Nếu sau lọc rỗng → không tới được nữa.

Vì vật cản chỉ chặn trên/dưới (1 interval cho phép), tính liên tục được bảo toàn. Không cần BFS `O(n·m)`.

## 3. Thuật toán O(m)

```
lo=1, hi=1, p=1 (lẻ)
for j=2..m:
  nl=lo-1, nh=hi+1, np=p^1
  cl=max(nl,L_j), ch=min(nh,R_j)
  if cl>ch → NO
  if cl%2 != np → cl++
  if ch%2 != np → ch--
  if cl>ch → NO
  lo,hi,p = cl,ch,np
YES nếu không rỗng tới cuối.
```

Riêng `m=1`: `YES` (đã đứng ở cột đích).

## 4. Độ phức tạp

- Thời gian: `O(m)` mỗi test, tổng `O(Σm) ≤ 2e5`.
- Bộ nhớ: `O(1)`.
- `n,m ≤ 1e5`, `t ≤ 1000` thoải mái trong 1s.

## 5. Test mẫu

```
3 test → YES / NO / YES
```

Test 2: cột 2 `L=1,R=0` rỗng → `NO`.
Test 3: lan truyền cho `{1}→{2}→{3}→{4}→{3}→{2}→{3}→{4}→{5}` → `YES`.

Đã kiểm brute-force 200 case ngẫu nhiên `n,m ≤ 6` khớp hoàn toàn.
