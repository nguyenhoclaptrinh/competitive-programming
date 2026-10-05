# Giải đề bài A: Danh the Naughty Pig

## Tóm tắt bài toán
Cho một bảng kích thước $n \times n$ và $m$ ô có chứa chướng ngại vật. Cần chia tập hợp $m$ chướng ngại vật thành tối đa $k$ dãy ($k \le n$) sao cho mỗi dãy là một chuỗi các bước nhảy thỏa mãn:
1. Hai ô liên tiếp trong dãy phải nằm trên cùng một hàng hoặc cùng một cột.
2. Hướng di chuyển phải luân phiên (nếu bước trước đó di chuyển theo hàng thì bước tiếp theo phải di chuyển theo cột, và ngược lại).

## Phân tích
Bài toán yêu cầu chúng ta tìm các đường đi trong đó hướng di chuyển thay đổi liên tục giữa ngang và dọc. Ta có thể mô hình hóa bài toán này bằng **đồ thị hai phía (bipartite graph)**:
- Chia các đỉnh của đồ thị thành hai tập: tập các hàng $R = \{1, 2, \dots, n\}$ và tập các cột $C = \{1, 2, \dots, n\}$.
- Mỗi chướng ngại vật ở ô $(r, c)$ tương ứng với một cạnh nối giữa đỉnh hàng $r$ và đỉnh cột $c$.

Với cách biểu diễn này:
- Một bước nhảy giữa hai ô $(r, c_1)$ và $(r, c_2)$ (cùng hàng $r$) tương ứng với hai cạnh kề nhau cùng chung đỉnh $r$.
- Một bước nhảy luân phiên tiếp theo (từ ngang sang dọc) bắt buộc hai ô đó phải kề nhau và chung đỉnh cột $c_2$.
- Nhờ tính chất của đồ thị hai phía, mọi đường đi (walk) trên đồ thị này tự động luân phiên giữa tập đỉnh hàng $R$ và tập đỉnh cột $C$. Do đó, hai cạnh kề nhau trên đường đi luôn thay đổi giữa việc chung đỉnh hàng (nhảy ngang) và chung đỉnh cột (nhảy dọc).
- Việc chia các chướng ngại vật thành các dãy nhảy hợp lệ tương đương với việc **phân tách tập các cạnh của đồ thị thành các đường đi không giao nhau về cạnh**.

## Thuật toán
Chúng ta cần phân tách tập hợp các cạnh của đồ thị thành tối đa $n$ đường đi. Ta có thể sử dụng thuật toán tìm **Đường đi / Chu trình Euler** (Eulerian Path / Circuit):
1. Đối với đồ thị có các đỉnh bậc lẻ, ta thêm một đỉnh giả $0$ và nối các đỉnh bậc lẻ vào đỉnh giả này. (Vì số lượng đỉnh bậc lẻ trong bất kỳ thành phần liên thông nào luôn là số chẵn, đỉnh $0$ cũng sẽ có bậc chẵn).
2. Khi đó, tất cả các đỉnh trong thành phần liên thông chứa đỉnh giả $0$ đều có bậc chẵn, đảm bảo tồn tại một chu trình Euler đi qua tất cả các cạnh.
3. Chạy thuật toán tìm chu trình Euler (như thuật toán Hierholzer) xuất phát từ đỉnh $0$.
4. Sau khi có được chu trình Euler đi qua đỉnh $0$, ta bỏ đi các cạnh giả đã thêm vào. Chu trình lớn này sẽ bị cắt thành nhiều đoạn đường đi nhỏ, mỗi đoạn là một chuỗi nhảy hợp lệ cho Danh.
5. Đối với những thành phần liên thông không có đỉnh bậc lẻ, ta chỉ việc tìm một chu trình Euler trong thành phần đó và sử dụng toàn bộ chu trình đó làm 1 đường đi duy nhất.

**Chứng minh số lượng dãy $k \le n$:**
Giả sử đồ thị có $C_{even}$ thành phần liên thông toàn bậc chẵn, và $V_{odd}$ đỉnh bậc lẻ trong toàn bộ đồ thị. 
Số lượng đường đi tạo ra sẽ là $W = C_{even} + \frac{V_{odd}}{2}$.
- Mỗi thành phần chẵn chứa ít nhất 4 đỉnh (vì mỗi chu trình trong đồ thị hai phía đơn đồ thị cần ít nhất 4 đỉnh là 2 hàng, 2 cột).
- Các đỉnh bậc lẻ đóng góp 1 vào tổng $V_{odd}$.
Ta có thể chứng minh tổng số lượng đỉnh $2n \ge 4C_{even} + V_{odd}$, kéo theo:
$W = C_{even} + \frac{V_{odd}}{2} \le \frac{4C_{even} + 2V_{odd}}{4} \le \frac{2n}{2} = n$.
Do đó, số đường đi $W$ luôn $\le n$, thỏa mãn hoàn toàn yêu cầu bài toán.

## Độ phức tạp
Thuật toán Hierholzer thăm mỗi cạnh đúng một lần bằng cách dùng stack (tương tự khử đệ quy) để tránh tràn bộ nhớ.
- Độ phức tạp thời gian: $\mathcal{O}(n + m)$
- Độ phức tạp không gian: $\mathcal{O}(n + m)$
