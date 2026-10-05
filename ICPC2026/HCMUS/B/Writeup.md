# Writeup Bài B: Freezer

## 1. Phân tích bài toán
- Mỗi ngày Khanh cần chọn **chính xác 2 phần ăn**. Cả 2 phần ăn này phải chưa hết hạn, tức là hạn sử dụng (expiration day) của chúng phải $\ge d$.
- Yêu cầu về chất lượng:
  - Mỗi phần ăn đều phải có chất lượng $q \ge 4$. Những phần có $q < 4$ chắc chắn không dùng được, ta có thể bỏ qua.
  - Tổng chất lượng 2 phần ăn phải $\ge 9$.
- Nhận xét về điều kiện tổng chất lượng: Vì tất cả các phần ăn ta xét đều có chất lượng $\ge 4$, nên tổng của bất kỳ 2 phần ăn nào cũng sẽ $\ge 8$. Cặp duy nhất **không hợp lệ** là cặp có chất lượng $(4, 4)$ vì tổng của nó bằng $8 < 9$. Tất cả các cặp khác như $(4, \ge 5)$ hay $(\ge 5, \ge 5)$ đều có tổng $\ge 9$ và hoàn toàn hợp lệ.
- Từ đây, ta có thể đơn giản hoá bài toán bằng cách chia các phần ăn hợp lệ ($q_i \ge 4$) thành hai nhóm:
  - **Nhóm Good (Tốt):** Có $q_i \ge 5$.
  - **Nhóm Bad (Kém):** Có $q_i = 4$.
- Chốt lại, mỗi ngày ta phải chọn ra **1 phần ăn Good** và **1 phần ăn tùy ý** (có thể là Good hoặc Bad).

## 2. Chiến thuật xếp lịch (Tham lam - Greedy)
- Giả sử ta muốn kiểm tra xem có thể xếp lịch ăn trong $K$ ngày được hay không, ta sẽ ưu tiên lên lịch ngược từ ngày $K$ lùi dần về ngày $1$. 
- Tại ngày $d$ (từ $K$ giảm dần về $1$):
  - Ta đưa tất cả các phần ăn có hạn sử dụng bằng $d$ vào 2 danh sách chờ chung (Pool Good và Pool Bad). *Riêng với ngày lớn nhất $K$, ta đưa tất cả các phần ăn có hạn sử dụng $\ge K$ vào.*
  - Cần lấy ra 2 phần ăn cho ngày $d$:
    - Bắt buộc phải lấy ra 1 phần ăn từ danh sách Pool Good. Nếu Pool Good trống, ta kết luận không thể xếp lịch cho $K$ ngày.
    - Phần ăn thứ 2: Ta sẽ ưu tiên lấy từ Pool Bad để giải quyết các phần ăn kém linh hoạt (vì nhóm Bad chỉ đóng vai trò ghép cặp phụ). Nếu Pool Bad trống, ta mới lấy phần ăn thứ 2 từ Pool Good.
- **Tính đúng đắn:** Việc xét từ ngày $K$ lùi về ngày $1$ rất tối ưu, bởi vì bất kỳ phần ăn nào tồn tại trong Pool tại ngày $d$ thì chắc chắn nó đã có hạn sử dụng $\ge d$. Do đó, đối với những ngày còn lại (nhỏ hơn $d$), phần ăn này *vẫn luôn còn hạn*. Nghĩa là các phần ăn nằm trong Pool lúc này hoàn toàn tương đương nhau về mặt thời gian, ta có thể tuỳ ý lấy phần ăn nào ở vị trí hiện tại cũng không làm ảnh hưởng đến các ngày sau, điều duy nhất cần quan tâm là ưu tiên dùng Bad trước thay vì Good.

## 3. Tối ưu bằng Tìm kiếm Nhị phân
- Gọi đáp án là $K$. Do tổng số phần ăn $N \le 2000$, số ngày ăn tối đa chỉ là $N / 2 \le 1000$.
- Ta có thể tìm kiếm nhị phân (Binary Search) giá trị $K$ lớn nhất trong đoạn $[0, N/2]$. Mỗi bước dùng thuật toán tham lam ở trên để kiểm tra `check(K)`.
- Độ phức tạp mỗi lần kiểm tra là $O(N)$ (do mỗi phần ăn chỉ push và pop ra khỏi pool đúng một lần). Tổng thời gian cho toàn bộ thuật toán là $O(N \log N)$, cực kì nhanh và vượt qua giới hạn $1s$ một cách dễ dàng.
