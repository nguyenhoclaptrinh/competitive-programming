# Lời giải bài I: Danh the Happy Pig

## 1. Phân tích bài toán
Bài toán yêu cầu tìm tổng độ hạnh phúc lớn nhất mà chú heo Danh có thể đạt được khi nhảy qua các ô trên một bảng 1 chiều từ ô $0$ cho đến khi nhảy ra khỏi bảng (đến một ô có tọa độ $> n$).

Luật nhảy của Danh như sau:
- Bắt đầu từ ô $0$ ở bước $i=1$.
- Ở mỗi bước nhảy $i$, từ vị trí hiện tại $p$, Danh có thể nhảy tới $p+i$ hoặc $p+i+1$.
- Khi đáp xuống một ô $j \le n$, Danh nhận được độ hạnh phúc $a_j$. Nếu đáp ra ngoài bảng ($>n$), cuộc hành trình kết thúc và không nhận thêm hay mất đi độ hạnh phúc nào từ các ô ngoài bảng.

## 2. Nhận xét quan trọng
Khoảng cách Danh có thể đi được sau $k$ bước nhảy là bao nhiêu?
- Nếu luôn chọn nhảy bước nhỏ nhất (nhảy khoảng cách $i$), tổng khoảng cách sau $k$ bước là: $S_{min} = \sum_{i=1}^k i = \frac{k(k+1)}{2}$.
- Nếu luôn chọn nhảy bước lớn nhất (nhảy khoảng cách $i+1$), tổng khoảng cách sau $k$ bước là: $S_{max} = \sum_{i=1}^k (i+1) = \frac{k(k+3)}{2}$.

Một nhận xét rất thú vị là: tại mỗi bước, ta được chọn cộng thêm $0$ hoặc $1$ vào khoảng cách đi được. Do đó, tập hợp các vị trí có thể đến được sau đúng $k$ bước nhảy chính là toàn bộ các số nguyên nằm trong đoạn:
$$\left[ \frac{k(k+1)}{2}, \frac{k(k+3)}{2} \right]$$

Ta lại thấy rằng cận trên của đoạn ở bước $k-1$ là $\frac{(k-1)(k+2)}{2} = \frac{k^2+k-2}{2} = \frac{k(k+1)}{2} - 1$.
Điểm này chứng tỏ **các đoạn vị trí đạt được sau mỗi số bước $k$ hoàn toàn rời nhau và bao phủ toàn bộ tập số nguyên dương**. 
Nói cách khác, với mỗi một ô $p \ge 1$ bất kỳ, tồn tại **duy nhất** một số bước nhảy $k$ để đến được ô $p$. Số bước $k$ đó hoàn toàn phụ thuộc vào $p$.

## 3. Thuật toán Quy Hoạch Động
Vì $k$ (số bước nhảy đã thực hiện) phụ thuộc hoàn toàn vào vị trí hiện tại $p$, ta không cần lưu thời gian $i$ (hay $k$) trong trạng thái Quy hoạch động (DP). Trạng thái DP của ta chỉ cần là:
$dp[p]$: Tổng độ hạnh phúc lớn nhất có thể nhận thêm nếu hiện tại đang đứng ở ô $p$.

Khi ở vị trí $p$, số bước nhảy đã thực hiện $k$ thoả mãn:
$$\frac{k(k+1)}{2} \le p \le \frac{k(k+3)}{2}$$
Bước nhảy tiếp theo sẽ có độ dài là $k+1$ hoặc $k+2$. Do đó từ $p$ có thể nhảy tới $p+k+1$ hoặc $p+k+2$.

**Công thức truy hồi:**
$$dp[p] = a_p + \max(dp[p+k+1], dp[p+k+2])$$
(Quy ước $dp[x] = 0$ với mọi $x > n$)

Ta có thể tính DP ngược từ $p = n$ về $1$, sau đó kết quả của bài toán sẽ là:
$$ans = \max(dp[1], dp[2])$$

Để tối ưu, thay vì giải phương trình bậc 2 để tìm $k$ cho mỗi $p$, ta có thể duy trì biến $k$ giảm dần cùng với $p$ trong quá trình duyệt.

## 4. Độ phức tạp
- **Thời gian**: Vòng lặp chạy từ $n$ về $1$, biến $k$ chỉ giảm tối đa $\approx \sqrt{2n}$ lần. Độ phức tạp là $O(n)$, hoàn toàn vượt qua dễ dàng giới hạn thời gian $2$ giây với $n = 5 \cdot 10^6$.
- **Không gian bộ nhớ (Space)**: Mảng `dp` cần kích thước tối đa là $n + \max(k) + 2 \approx n + \sqrt{2n} + 5$. Không gian tốn cỡ $O(n)$, thỏa mãn thoải mái giới hạn bộ nhớ 1GB.
