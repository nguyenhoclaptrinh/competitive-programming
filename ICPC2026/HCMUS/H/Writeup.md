# Lời giải bài H (Raining)

## Phân tích bài toán
Bài toán yêu cầu chúng ta theo dõi một tập hợp các điểm được cập nhật (thêm vào) qua từng giây. Tại mỗi giây, chúng ta cần tìm diện tích lớn nhất (nhân 2) của tam giác được tạo bởi 3 điểm nằm trong bao lồi của tập hợp các điểm đã xuất hiện.

Vì tam giác có diện tích lớn nhất luôn có 3 đỉnh nằm trên các đỉnh của bao lồi, chúng ta chỉ cần quan tâm đến các đỉnh của bao lồi hiện tại. Tuy nhiên, việc duy trì một bao lồi một cách linh hoạt (dynamic convex hull) cho các điểm được thêm vào có thể rất phức tạp và cần các cấu trúc dữ liệu tốn kém.

Một tính chất cực kỳ quan trọng được nêu trong đề bài là: **Các điểm $p_1, p_2, \dots, p_q$ được sinh ngẫu nhiên đồng đều (uniformly at random)** trong một hình vuông $[-10^9, 10^9] \times [-10^9, 10^9]$. Theo lý thuyết xác suất, số lượng điểm kỳ vọng nằm trên bao lồi của $n$ điểm sinh ngẫu nhiên trong hình vuông là $O(\log n)$. Hơn nữa, xác suất để điểm thứ $i$ làm thay đổi bao lồi cũng tỉ lệ thuận với $\frac{\log i}{i}$. Điều này có nghĩa là, hầu hết các điểm được thêm vào sẽ rơi vào bên trong bao lồi hiện tại và sẽ không làm thay đổi hình dáng của bao lồi. 

## Thuật toán
Dựa vào tính chất trên, ta có thể xây dựng thuật toán cực kì đơn giản như sau:

1. Duy trì một tập hợp $S$ chỉ chứa các đỉnh của bao lồi hiện tại. Ban đầu tập $S$ rỗng. Đồng thời duy trì biến `max_area` lưu diện tích lớn nhất hiện có.
2. Với mỗi điểm $p$ được thêm vào:
   - Kiểm tra xem $p$ có nằm trong (hoặc trên cạnh) của đa giác bao lồi $S$ hay không. Có thể kiểm tra bằng cách duyệt qua tất cả các cạnh có hướng của $S$ (theo thứ tự ngược chiều kim đồng hồ - CCW). Nếu $p$ nằm bên trái hoặc trên tất cả các đường thẳng chứa cạnh, thì $p$ nằm trong bao lồi.
   - Nếu $p$ nằm trong bao lồi, bao lồi không thay đổi, diện tích lớn nhất `max_area` cũng không đổi. Ta có thể bỏ qua $p$ và in ra `max_area`.
   - Nếu $p$ nằm ngoài bao lồi, ta thêm $p$ vào tập $S$, sau đó tính lại bao lồi của tập $S$ (bằng thuật toán Monotone Chain hoặc Graham Scan trong $O(k \log k)$ với $k = |S|$). Thuật toán này sẽ tự động loại bỏ những điểm cũ không còn nằm trên bao lồi.
   - Khi có bao lồi mới, ta duyệt qua tất cả các bộ 3 đỉnh trên bao lồi mới (độ phức tạp $O(k^3)$) để tính diện tích các tam giác và cập nhật `max_area`.
3. In ra `max_area` sau mỗi bước.

## Đánh giá độ phức tạp
- Do các điểm sinh ngẫu nhiên, số đỉnh trung bình trên bao lồi $k$ cực kỳ nhỏ (với $N = 10^5$, giá trị $k$ hiếm khi vượt qua 50).
- Số lần bao lồi thực sự thay đổi chỉ khoảng vài trăm lần (tổng của chuỗi $\sum \frac{\log i}{i}$). Do đó, phần lớn thời gian (với xác suất rất lớn) thuật toán chỉ thực hiện phép kiểm tra điểm trong đa giác mất $O(k)$. 
- Mỗi khi bao lồi thay đổi, ta duyệt $O(k^3)$ để tính diện tích lớn nhất. Vì $k$ rất nhỏ, $O(k^3)$ hoàn toàn không đáng kể. 
- Tổng độ phức tạp trung bình (Average-case time complexity) cho $Q$ truy vấn là $O(Q \log Q)$, chạy cực kì nhanh và an toàn.
- Diện tích tam giác lớn nhất nhân hai được tính theo tích có hướng (cross product) của 2 vector. Giới hạn tọa độ là $10^9$, hiệu tọa độ tối đa là $2 \times 10^9$. Tích vô hướng của chúng có thể đạt đến $4 \times 10^{18} - (-4 \times 10^{18}) = 8 \times 10^{18}$. Giá trị này vừa khít với giới hạn lưu trữ của kiểu dữ liệu `long long` (tối đa $\approx 9.22 \times 10^{18}$) trong C++ mà không xảy ra hiện tượng tràn số (overflow).
