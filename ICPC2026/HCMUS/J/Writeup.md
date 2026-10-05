# Giải bài J - Crafting Costs (ICPC 2026)

## 1. Tóm tắt bài toán
- Có $n$ loại linh kiện. Mỗi loại có thể mua trực tiếp trên thị trường với giá $p_i$.
- Có $m$ công thức chế tạo. Công thức $j$ tạo ra 1 linh kiện loại $t_j$, cần chi phí nhân công $c_j$ và một danh sách gồm $k_j$ loại linh kiện đầu vào khác nhau.
- Các linh kiện đầu vào bị tiêu hao hoàn toàn trong quá trình chế tạo. Do đó, nếu nhiều nơi cần dùng linh kiện $X$, ta phải trả chi phí để có đủ số lượng $X$ tương ứng.
- Yêu cầu: Tìm chi phí nhỏ nhất để có được 1 linh kiện của từng loại (từ 1 đến $n$).

## 2. Phân tích thuật toán
- Chi phí để tạo ra một linh kiện qua một công thức bằng tổng chi phí của các linh kiện đầu vào cộng với chi phí nhân công $c_j$.
- Do giá mua ban đầu $p_i \ge 1$ và chi phí nhân công $c_j \ge 0$, chi phí để tạo ra một linh kiện luôn **lớn hơn hoặc bằng** chi phí của bất kỳ linh kiện đầu vào nào của nó.
- Tính chất đơn điệu này (trọng số không âm) cho phép chúng ta sử dụng **thuật toán Dijkstra** mở rộng trên siêu đồ thị (hypergraph) để tìm đường đi ngắn nhất (chi phí nhỏ nhất).

**Mô hình hóa thuật toán:**
1. Khởi tạo mảng `best_cost[i] = p_i` đại diện cho chi phí tốt nhất để có được linh kiện $i$.
2. Đẩy tất cả các loại linh kiện vào hàng đợi ưu tiên (Priority Queue - PQ) dưới dạng `(best_cost[i], i)`, trong đó giá trị chi phí nhỏ hơn sẽ được lấy ra trước.
3. Với mỗi công thức, ta quản lý:
   - `unsettled`: Số lượng loại linh kiện đầu vào chưa chốt được chi phí tối ưu (khởi tạo bằng $k_j$).
   - `current_sum`: Tổng chi phí hiện tại của công thức (khởi tạo bằng $c_j$).
4. Trong vòng lặp chính của thuật toán:
   - Lấy `(c, u)` có chi phí nhỏ nhất từ PQ. 
   - Nếu `c > best_cost[u]`, đây là một giá trị cũ đã được cập nhật tốt hơn, ta bỏ qua (stale entry). Ngược lại, linh kiện $u$ chính thức được chốt chi phí tối ưu là `c`.
   - Duyệt qua tất cả các công thức yêu cầu linh kiện $u$ làm đầu vào. Với mỗi công thức đó:
     - Trừ `unsettled` đi 1.
     - Cộng `c` vào `current_sum`.
     - Nếu `unsettled == 0`, tức là toàn bộ linh kiện đầu vào của công thức này đều đã có giá tối ưu, ta kiểm tra xem `current_sum` có nhỏ hơn `best_cost[t_j]` (chi phí tốt nhất hiện tại của linh kiện đích) hay không.
     - Nếu có, ta cập nhật `best_cost[t_j] = current_sum` và đẩy `(current_sum, t_j)` vào hàng đợi ưu tiên.

**Tại sao thuật toán chính xác?**
- Khi một linh kiện đích của công thức được chốt giá tối ưu và được dùng để xét tiếp, tất cả các linh kiện đầu vào của công thức đó chắc chắn đã được lấy ra khỏi PQ từ trước (vì tổng chi phí công thức $\ge$ chi phí của từng thành phần). Do đó, chúng ta không bao giờ bỏ lỡ một kết quả tốt hơn.
- Việc tính tổng thay vì lấy max không làm thay đổi tính đúng đắn của quá trình sắp xếp theo trọng số, vì tất cả các chi phí thành phần đều $\ge 0$.
- Các biến đổi tính toán đều nằm trong giới hạn $\sim 10^9 \cdot 2 \cdot 10^5 \approx 2 \cdot 10^{14}$, hoàn toàn nằm gọn trong kiểu dữ liệu 64-bit (`long long`) mà không bị tràn số học.

## 3. Độ phức tạp
- **Thời gian (Time Complexity):** $O((N + M + \sum k_j) \log N)$. Mỗi loại linh kiện đầu vào của mỗi công thức được xử lý đúng 1 lần khi linh kiện tương ứng của nó được pop khỏi PQ. Thao tác trên hàng đợi ưu tiên tốn $O(\log N)$. Giới hạn thời gian 3 giây là rất thoải mái cho độ phức tạp này.
- **Không gian (Space Complexity):** $O(N + M + \sum k_j)$ để lưu đồ thị danh sách kề và các trạng thái của đồ thị.
