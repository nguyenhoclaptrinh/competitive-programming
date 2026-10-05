# Lời giải bài C - Fluorine's Fun Function

## Tóm tắt đề bài
Bài toán yêu cầu chúng ta thực hiện 2 loại truy vấn trên một mảng $a$ gồm $n$ số nguyên dương:
1. `1 l r x`: Cộng $x$ vào tất cả phần tử $a_i$ với $l \le i \le r$. (Lưu ý $x$ có thể âm, nhưng đề bài đảm bảo $a_i$ luôn là số nguyên dương).
2. `2 l r`: Tính tổng các số Fibonacci thứ $a_i$ trong đoạn $[l, r]$ modulo $10^9 + 7$. Cụ thể là tính $\sum_{i=l}^r F(a_i) \pmod{10^9 + 7}$.

## Phương pháp giải
Dãy Fibonacci có tính chất nổi bật là có thể biểu diễn qua phép nhân ma trận. Xét ma trận cơ sở:
$$M = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$$
Ta có tính chất:
$$M^k = \begin{pmatrix} F_{k+1} & F_k \\ F_k & F_{k-1} \end{pmatrix}$$

Như vậy, giá trị $F_k$ chính là phần tử ở hàng 0, cột 1 (hoặc hàng 1, cột 0) của ma trận $M^k$.

Thay vì lưu giá trị của $a_i$ tại mỗi vị trí, ta sẽ lưu ma trận $M^{a_i}$. Lúc này, bài toán quy về việc quản lý mảng các ma trận $2 \times 2$:
1. **Truy vấn 1 (Cộng thêm $x$)**:
   Khi $a_i$ tăng thêm $x$, ma trận $M^{a_i}$ sẽ được nhân thêm với $M^x$:
   $$M^{a_i + x} = M^{a_i} \times M^x$$
   Do phép nhân ma trận có tính chất phân phối với phép cộng: $A \times P + B \times P = (A + B) \times P$, ta có thể sử dụng cấu trúc dữ liệu **Segment Tree** (Cây phân đoạn) kết hợp với **Lazy Propagation** (Cập nhật lười) để quản lý mảng ma trận này.
   - Nếu $x > 0$: Ta nhân với $M^x$.
   - Nếu $x < 0$: Ta nhân với ma trận nghịch đảo $M^{-x}$. Ma trận nghịch đảo của $M$ modulo $10^9 + 7$ là $M^{-1} = \begin{pmatrix} 0 & 1 \\ 1 & -1 \end{pmatrix} \equiv \begin{pmatrix} 0 & 1 \\ 1 & 10^9+6 \end{pmatrix} \pmod{10^9+7}$.

2. **Truy vấn 2 (Tính tổng Fibonacci)**:
   Để tính tổng các $F(a_i)$ trong đoạn $[l, r]$, ta chỉ cần gọi truy vấn tổng các ma trận trên Segment Tree trong đoạn đó.
   Kết quả trả về là một ma trận tổng $S = \sum_{i=l}^r M^{a_i}$. Giá trị cần tìm chính là phần tử ở hàng 0, cột 1 của ma trận $S$.

## Độ phức tạp
- Việc tính $M^x$ mất $O(\log |x|)$.
- Mỗi truy vấn trên Segment Tree mất $O(\log N)$ phép nhân và cộng ma trận $2 \times 2$. Phép toán trên ma trận $2 \times 2$ có thể xem là $O(1)$.
- Độ phức tạp thời gian tổng cộng: $O(N \log (\max A) + Q (\log N + \log |x|))$. Với $N, Q \le 2 \cdot 10^5$, thời gian này hoàn toàn đủ vượt qua giới hạn 2 giây.
- Độ phức tạp không gian: $O(N)$ để lưu Segment Tree.
