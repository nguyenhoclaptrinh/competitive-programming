# Giải bài K: Lithium and Lithuania

## Tóm tắt bài toán
Cho 4 điểm thành phần IELTS của một thí sinh: Listening, Reading, Writing và Speaking. Các điểm này nằm trong khoảng từ $0.0$ đến $9.0$ và có đuôi là $.0$ hoặc $.5$.
Cần tính điểm Overall bằng cách lấy trung bình cộng của 4 điểm thành phần và làm tròn theo quy tắc:
- Làm tròn tới bội số gần nhất của $0.5$.
- Nếu phần thập phân của điểm trung bình là $.25$ hoặc $.75$ (tức là nằm chính giữa hai bội số của $0.5$), ta làm tròn **lên** bội số cao hơn.

## Phương pháp giải
Vì các điểm thành phần đều là các số thập phân với một chữ số sau dấu phẩy (và chỉ có thể là $.0$ hoặc $.5$), ta có thể đưa về bài toán xử lý số nguyên để tránh các sai số không mong muốn khi sử dụng kiểu số thực (floating-point precision).

1. Gọi $S = L + R + W + S$ là tổng của 4 điểm. Ta nhân $S$ với $10$ để được một số nguyên $X = S \times 10$.
2. Trung bình cộng của 4 điểm khi nhân với $10$ sẽ là $\frac{X}{4}$. Ta cần làm tròn giá trị $\frac{X}{40}$ (do ban đầu là $\frac{S}{4}$, giờ nhân thêm 10).
3. Sử dụng phép chia nguyên và phép chia lấy dư:
   - Gọi $Q = \lfloor \frac{X}{40} \rfloor$
   - Phần dư $R = X \bmod 40$

4. $R$ sẽ quyết định phần thập phân của điểm tổng. Do $X$ là bội số của $5$, $R$ có thể nhận các giá trị $0, 5, 10, 15, 20, 25, 30, 35$. Tương ứng với phần thập phân của điểm trung bình:
   - $R = 0 \Rightarrow .0 \Rightarrow$ giữ nguyên.
   - $R = 5 \Rightarrow .125 \Rightarrow$ làm tròn xuống $0$.
   - $R = 10 \Rightarrow .25 \Rightarrow$ làm tròn lên $0.5$.
   - $R = 15 \Rightarrow .375 \Rightarrow$ làm tròn lên $0.5$.
   - $R = 20 \Rightarrow .5 \Rightarrow$ giữ nguyên $0.5$.
   - $R = 25 \Rightarrow .625 \Rightarrow$ làm tròn xuống $0.5$.
   - $R = 30 \Rightarrow .75 \Rightarrow$ làm tròn lên $1.0$ (chuyển qua số nguyên tiếp theo).
   - $R = 35 \Rightarrow .875 \Rightarrow$ làm tròn lên $1.0$.

Dựa vào đây, ta có quy tắc cộng thêm vào $Q \times 10$:
- Nếu $R \ge 30$: điểm bằng $Q \times 10 + 10$
- Nếu $10 \le R < 30$: điểm bằng $Q \times 10 + 5$
- Nếu $R < 10$: điểm bằng $Q \times 10$

Cuối cùng, in ra kết quả với định dạng 1 chữ số thập phân bằng cách chia phần nguyên và phần dư cho $10$.

## Độ phức tạp
- **Thời gian (Time Complexity):** $O(1)$ cho mỗi test case. Tổng thời gian $O(T)$ rất nhỏ và hoàn toàn qua được giới hạn thời gian $1s$.
- **Không gian (Space Complexity):** $O(1)$.
