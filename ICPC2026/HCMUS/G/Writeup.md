# Lời giải Bài G: Whisper Chain

## Phân tích bài toán
Bài toán yêu cầu chúng ta xếp $n$ học sinh vào $n$ chiếc ghế xếp thành một hàng ngang sao cho số lượng mong muốn "thì thầm" được thoả mãn là lớn nhất.
Mỗi học sinh $i$ muốn thì thầm với học sinh $s_i$. Điều này chỉ được thực hiện nếu học sinh $s_i$ ngồi ngay sau học sinh $i$ (ghế của $s_i$ là $k+1$ nếu ghế của $i$ là $k$).

Chúng ta có thể mô hình hoá bài toán này bằng một đồ thị có hướng, trong đó mỗi học sinh là một đỉnh, và có một cạnh có hướng từ $i$ đến $s_i$.
Bởi vì mỗi học sinh chỉ muốn thì thầm với đúng một người, nên mỗi đỉnh trong đồ thị có bậc ra (out-degree) đúng bằng 1. Đây là đặc điểm của một **đồ thị hàm số** (functional graph).

Một cách sắp xếp chỗ ngồi hợp lệ tương đương với việc chọn ra một số lượng các cạnh sao cho:
1. Không có đỉnh nào có bậc vào lớn hơn 1 (một học sinh không thể có nhiều hơn một người ngồi ngay trước mình).
2. Không tạo thành chu trình (bởi vì các ghế xếp thành một hàng ngang, không phải vòng tròn).

Vì bậc ra của mọi đỉnh trong đồ thị gốc đã là 1, nên bất kỳ tập hợp con nào của các cạnh cũng sẽ luôn thoả mãn bậc ra $\le 1$.
Mục tiêu là chọn được số lượng cạnh nhiều nhất. Tập hợp các cạnh được chọn sẽ tạo thành các đường đi rời rạc (disjoint paths).

## Nhận xét thuật toán
Do đây là đồ thị hàm số, đồ thị sẽ bao gồm các thành phần liên thông yếu (weakly connected components - WCC). Mỗi WCC có cấu trúc giống hình một "mặt trời": một chu trình duy nhất kết hợp với các cây hướng vào chu trình đó.

Để tối đa hoá số lượng cạnh được chọn:
- Đối với mỗi đỉnh, ta chỉ có thể chọn tối đa một cạnh đi vào đỉnh đó. Số lượng cạnh lớn nhất có thể chọn trong một WCC chính là số lượng đỉnh có bậc vào $\ge 1$.
- Tuy nhiên, nếu chúng ta chọn tất cả các cạnh này, ta có thể vô tình bao gồm cả chu trình của WCC. Vì ta không được phép có chu trình, ta buộc phải loại bỏ ít nhất 1 cạnh trong chu trình đó.
- Phân loại các WCC:
  - **Chu trình đơn giản (Simple cycle):** Thành phần liên thông chỉ bao gồm đúng một chu trình (số lượng đỉnh của WCC bằng số lượng đỉnh của chu trình). Trong trường hợp này, ta bắt buộc phải loại bỏ một cạnh bất kỳ thuộc chu trình để phá vỡ nó. Số cạnh được chọn sẽ là $N_{WCC} - 1$.
  - **Chu trình có nhánh (Non-simple cycle):** Tồn tại ít nhất một đỉnh nằm ngoài chu trình có cạnh hướng vào chu trình. Điều này đồng nghĩa với việc tồn tại một đỉnh $v$ thuộc chu trình nhận một cạnh từ đỉnh $u$ nằm ngoài chu trình. Khi đó, thay vì chọn cạnh của chu trình đi vào $v$, ta **chọn cạnh $u \to v$**. Việc này sẽ ngay lập tức phá vỡ chu trình mà không làm giảm tổng số đỉnh có cạnh đi vào! Với các đỉnh khác, ta chỉ cần chọn tuỳ ý một cạnh đi vào bất kỳ.

## Thuật toán cụ thể
1. Duyệt qua từng thành phần liên thông yếu (WCC) của đồ thị.
2. Tìm chu trình duy nhất trong WCC đó.
3. Nếu WCC là một chu trình đơn giản:
   - Bỏ qua một cạnh bất kỳ trong chu trình. Chọn các cạnh còn lại của chu trình.
4. Nếu WCC không phải là chu trình đơn giản:
   - Tìm đỉnh `v_break` thuộc chu trình mà có cạnh đi vào từ một đỉnh `u_break` không thuộc chu trình.
   - Chọn cạnh `u_break` $\to$ `v_break`.
   - Với các đỉnh $x$ khác trong WCC có cạnh đi vào, ta chọn một cạnh đi vào bất kỳ (có thể là cạnh đầu tiên trong danh sách kề ngược).
5. Các cạnh được chọn sẽ tạo thành một tập hợp các đường đi rời rạc (do không có chu trình và bậc vào, bậc ra đều $\le 1$).
6. Nối tất cả các đường đi này lại với nhau (bằng cách đặt chúng cạnh nhau) cùng với các đỉnh cô lập để tạo ra một chuỗi $N$ học sinh.
7. Vị trí của học sinh $i$ trong chuỗi chính là số ghế $c_i$ cần in ra.

## Độ phức tạp
Tất cả các bước bao gồm tìm WCC, tìm chu trình, và chọn cạnh đều có thể thực hiện thông qua duyệt đồ thị (BFS hoặc DFS).
Độ phức tạp thời gian: $\mathcal{O}(N)$
Độ phức tạp không gian: $\mathcal{O}(N)$
Điều này hoàn toàn thoả mãn giới hạn thời gian $1s$ cho $N \le 10,000$.
