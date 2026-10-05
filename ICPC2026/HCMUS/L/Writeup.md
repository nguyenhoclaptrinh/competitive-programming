# L - Lucky Numbers - Writeup

## Phân tích bài toán
Bài toán yêu cầu chúng ta tìm ra số lượng tối đa các "số may mắn" (số chia hết cho 3) có thể được tạo ra từ một tập hợp các chữ số cho trước. Chúng ta được biết tần suất xuất hiện tối đa của từng chữ số từ $0$ đến $9$. Không được phép có số $0$ đứng đầu trong các số nhiều chữ số, nhưng riêng số `0` đứng một mình vẫn hợp lệ. Mỗi số tạo ra không bắt buộc phải sử dụng toàn bộ số lượng chữ số cho phép.

## Quan sát thuật toán
Một số chia hết cho 3 khi và chỉ khi tổng các chữ số của nó chia hết cho 3.
Vì chúng ta muốn tạo ra CÀNG NHIỀU số may mắn CÀNG TỐT, mỗi số nên sử dụng CÀNG ÍT chữ số CÀNG TỐT.

Dựa vào số dư khi chia cho 3, các chữ số từ 0 đến 9 được chia thành 3 nhóm:
- Nhóm dư 0: $\{0, 3, 6, 9\}$. Mỗi chữ số trong nhóm này bản thân nó đã tạo thành một số chia hết cho 3 (số có 1 chữ số). Số 0 cũng hợp lệ do đề bài cho phép số 0.
- Nhóm dư 1: $\{1, 4, 7\}$. 
- Nhóm dư 2: $\{2, 5, 8\}$.

Với các chữ số thuộc nhóm dư 0, ta chỉ việc tách mỗi chữ số thành một số riêng biệt (1 chữ số) để tối đa hoá số lượng số tạo thành. Tổng số lượng số tạo được từ nhóm này là: $d_0 + d_3 + d_6 + d_9$.

Với phần còn lại là các chữ số thuộc nhóm dư 1 và dư 2, không chữ số nào đứng một mình chia hết cho 3. Ta phải ghép chúng lại. Các cách ghép tối ưu là:
1. **Ghép 1 chữ số dư 1 với 1 chữ số dư 2** (Ví dụ: 12, 15, 24). Tổng số dư là $1 + 2 = 3 \equiv 0 \pmod 3$. Chi phí là 2 chữ số để tạo ra 1 số. Lưu ý là các chữ số dư 1 và dư 2 đều khác $0$, nên số ghép được chắc chắn sẽ không có số $0$ đứng đầu. Ta ghép được tối đa $\min(C_1, C_2)$ số, với $C_1$ là tổng số lượng chữ số dư 1 và $C_2$ là tổng số lượng chữ số dư 2.
2. **Ghép 3 chữ số dư 1 hoặc 3 chữ số dư 2**. Nếu sau khi ghép theo cặp (dư 1 + dư 2) mà vẫn còn thừa các chữ số của cùng một nhóm (dư 1 hoặc dư 2), ta phải ghép 3 chữ số lại với nhau (Ví dụ: 111, 222). Chi phí là 3 chữ số để tạo ra 1 số. Số lượng số tạo thêm là phần dư thừa chia cho 3 (lấy phần nguyên).

Tổng hợp lại, số lượng số tối đa có thể tạo được bằng tổng của 3 đại lượng trên.

## Độ phức tạp
- **Thời gian (Time Complexity)**: $O(1)$ vì luôn luôn duyệt và xử lý trên 10 phần tử một cách tuyến tính.
- **Không gian (Space/Memory Complexity)**: $O(1)$ để lưu mảng tần suất 10 phần tử.

## Cài đặt (C++)
Tham khảo file mã nguồn `L.cpp`.
