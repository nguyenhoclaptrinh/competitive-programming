# Lời giải bài D - Tidal Wave (ICPC 2026 - HCMUS)

## Phân tích bài toán
- Bảng có kích thước $n \times m$.
- Nhân vật xuất phát tại ô $(1, 1)$.
- Tại mỗi bước từ $(i, j)$, nhân vật chỉ có thể di chuyển đến ô $(i+1, j+1)$ hoặc $(i-1, j+1)$.
- Cột $j$ sẽ bị chặn $l_j$ ô từ trên xuống và $r_j$ ô từ dưới lên. Nghĩa là các ô hợp lệ phải nằm trong đoạn $[l_j + 1, n - r_j]$.
- Mục tiêu là kiểm tra xem nhân vật có thể đến được cột thứ $m$ hay không.

## Quan sát
1. **Tính chẵn lẻ (Parity):** Do mỗi bước tiến $j$ tăng 1, $i$ cũng tăng hoặc giảm 1, nên tổng hoặc hiệu của $i$ và $j$ luôn bảo toàn tính chẵn lẻ. Ở vị trí $(1, 1)$, ta có $1 \equiv 1 \pmod 2$. Do đó tại mọi ô $(i, j)$ có thể đến được, chỉ số hàng $i$ và cột $j$ phải luôn có cùng tính chẵn lẻ ($i \equiv j \pmod 2$).
2. **Tập các ô hợp lệ:** Vì các bước nhảy là $\pm 1$ và ta luôn tiến về phía trước (tăng $j$), tập hợp các ô hợp lệ trên cột $j$ (nếu bỏ qua các chướng ngại vật) sẽ luôn là một đoạn liên tiếp các hàng cách nhau 2 đơn vị. 
3. **Cập nhật khoảng:** Giả sử ở cột $j-1$, nhân vật có thể ở các hàng nằm trong khoảng $[min\_r_{j-1}, max\_r_{j-1}]$. 
   Khi bước sang cột $j$:
   - Khả năng mở rộng tối đa theo hàng: $min\_r_j = min\_r_{j-1} - 1$ và $max\_r_j = max\_r_{j-1} + 1$.
   - Ràng buộc tại cột $j$: Giới hạn lại khoảng này bởi $l_j + 1$ và $n - r_j$. 
     Ta có: 
     - $min\_r_j = \max(min\_r_j, l_j + 1)$
     - $max\_r_j = \min(max\_r_j, n - r_j)$
   - Do tính chẵn lẻ ở quan sát 1, ta cần điều chỉnh lại $min\_r_j$ tăng lên 1 (nếu khác tính chẵn lẻ của $j$) và $max\_r_j$ giảm đi 1 (nếu khác tính chẵn lẻ của $j$).
4. Nếu sau khi giới hạn mà $min\_r_j > max\_r_j$, nghĩa là nhân vật không thể sống sót qua cột $j$. Kết quả bài toán sẽ là `NO`.
5. Nếu quá trình tiếp tục được đến cột $m$ mà khoảng duy trì được (tức là $min\_r_m \le max\_r_m$), thì kết quả là `YES`.

## Độ phức tạp thuật toán
- **Thời gian (Time Complexity):** Ở mỗi test case, ta duyệt qua $m$ cột. Tại mỗi cột, thời gian xử lý là $O(1)$. Do đó, thời gian cho mỗi test case là $O(m)$, dẫn đến tổng thời gian cho toàn bộ input là $O(\sum m) = O(2 \cdot 10^5)$, hoàn toàn tối ưu và dư dả so với giới hạn 1 giây của bài toán.
- **Không gian (Space Complexity):** Thuật toán chỉ sử dụng một vài biến cục bộ để lưu khoảng $[min\_r, max\_r]$ và thông số của cột hiện tại. Nên tốn độ phức tạp $O(1)$ về mặt bộ nhớ. 

## Cài đặt
- Chỉ cần một vòng lặp chạy $j$ từ 1 đến $m$.
- Biến trạng thái `possible` theo dõi tính khả thi.
- Tính cẩn thận trong việc sử dụng kiểu dữ liệu (mặc dù $n \le 10^5$ nên kiểu `int` là đủ). Đọc input nhanh `cin.tie(NULL)` để tối ưu hóa I/O.
