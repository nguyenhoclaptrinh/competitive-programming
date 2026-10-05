# Lời giải Bài E: Danh the Pig Emperor

## Phân tích bài toán
Bài toán yêu cầu tính tổng diện tích (nhân với 4) của hợp các tam giác vuông cân có cạnh huyền nằm trên trục hoành $(Ox)$. Mỗi tam giác được xác định bởi đoạn thẳng trên trục hoành có hoành độ từ $l_i$ đến $r_i$.

Đỉnh của tam giác thứ $i$ sẽ nằm ở tọa độ $\left(\frac{l_i + r_i}{2}, \frac{r_i - l_i}{2}\right)$.
Diện tích của một tam giác này là $\frac{1}{2} \times \text{đáy} \times \text{chiều cao} = \frac{1}{2} \times (r_i - l_i) \times \frac{r_i - l_i}{2} = \frac{(r_i - l_i)^2}{4}$.
Vì bài toán yêu cầu nhân tổng diện tích với 4, nên giá trị đại diện cho một tam giác (nếu không giao nhau) sẽ chính là $(r_i - l_i)^2$.

## Thuật toán
Khi nhiều tam giác giao nhau, đường bao phía trên (upper envelope) của chúng có cấu trúc rất đặc biệt. 
Ta có thể chuyển đổi tọa độ theo trục $u = x + y$ và $v = x - y$. Khi đó các tam giác trở thành các hình chữ nhật bị cắt bởi một đường chéo $u = v$. Hợp của các tam giác tương đương với hợp của các hình chữ nhật (tạo thành một hình đa giác bậc thang). 

Dựa vào tính chất của hợp các "bậc thang" (staircase polygon), ta có thể rút ra một kết luận quan trọng:
1. Nếu có một tam giác hoàn toàn nằm trong một tam giác khác (tức là $l_j \le l_i$ và $r_i \le r_j$), ta có thể bỏ qua tam giác nhỏ hơn.
2. Sau khi đã loại bỏ các tam giác bị bao trùm, ta thu được một dãy các tam giác có $l_i$ tăng ngặt và $r_i$ cũng tăng ngặt.
3. Khi đó, diện tích hợp của toàn bộ các hình bằng **tổng diện tích của từng hình** trừ đi **tổng diện tích phần giao của các cặp hình kề nhau**.
4. Cụ thể, phần giao của hình $i$ và hình $i+1$ (nếu có) chính là tam giác có đáy từ $l_{i+1}$ đến $r_i$. Kích thước phần giao (nhân 4) là $(r_i - l_{i+1})^2$ (với điều kiện $r_i > l_{i+1}$).

## Các bước thực hiện
1. Đọc danh sách các đoạn $[l_i, r_i]$.
2. Sắp xếp các đoạn tăng dần theo $l_i$. Nếu $l_i$ bằng nhau, sắp xếp giảm dần theo $r_i$.
3. Dùng một mảng `valid` để lưu các đoạn không bị bao trùm. Biến `max_r` lưu trữ giá trị $r$ lớn nhất đã duyệt qua.
   - Với mỗi đoạn, nếu $r_i > max\_r$, ta thêm nó vào `valid` và cập nhật $max\_r = r_i$.
   - Nếu $r_i \le max\_r$, đoạn này hoàn toàn bị bao trùm bởi một đoạn trước đó, ta bỏ qua.
4. Tính tổng diện tích (nhân 4):
   - Cộng thêm $(valid[i].r - valid[i].l)^2$ với mỗi $i$.
   - Trừ đi $(valid[i-1].r - valid[i].l)^2$ nếu $valid[i-1].r > valid[i].l$.
5. **Chú ý kiểu dữ liệu**: Tổng bình phương khoảng cách có thể lên tới $N \times (2 \cdot 10^9)^2 = 2 \cdot 10^5 \times 4 \cdot 10^{18} = 8 \cdot 10^{23}$. Giá trị này vượt qua giới hạn của `unsigned long long` (khoảng $1.8 \cdot 10^{19}$), do đó ta cần dùng `__int128` (hoặc `unsigned __int128`) để lưu trữ tổng và tự viết hàm in ra kết quả.

## Độ phức tạp
- Thời gian: $O(N \log N)$ do bước sắp xếp. Quá trình lọc và tính toán chỉ mất $O(N)$.
- Không gian: $O(N)$ để lưu trữ danh sách các đoạn.
Đây là thuật toán tối ưu hoàn toàn phù hợp với giới hạn thời gian 1s và $N = 2 \cdot 10^5$.
