# Problem A — Danh the Naughty Pig: Writeup

## 1. Mô hình đồ thị

Mỗi obstacle $(r,c)$ là một cạnh nối đỉnh hàng $r$ với đỉnh cột $c$.
Ta có đồ thị hai phía với $2n$ đỉnh ($n$ hàng + $n$ cột) và $m$ cạnh.

Một dãy $c_1,\dots,c_l$ thỏa:
- $c_i,c_{i+1}$ chung hàng/cột $\iff$ hai cạnh kề nhau (chung đầu mút);
- vuông góc $\iff$ hai điểm chung liên tiếp nằm khác phía (một ở phía hàng, một ở phía cột).

Nhưng trong đồ thị hai phía, mọi trail (dãy cạnh kề nhau, không lặp cạnh)
tự động đổi phía đầu mút chung: đỉnh $v_0,v_1,\dots,v_l$ luân phiên
hàng/cột nên $v_1,v_2,\dots$ cũng luân phiên. Do đó:

> Dãy hợp lệ $\iff$ trail trong đồ thị hai phía trên.

Bài toán thành: phủ mọi cạnh bằng $k\le n$ trail rời cạnh nhau.

## 2. Thuật toán: bù Euler + mạch Euler

Với một liên thông $C_i$ có $o_i$ đỉnh bậc lẻ:
số trail tối thiểu phủ hết cạnh là $\max(1,o_i/2)$.
Cách dựng chuẩn: ghép cặp các đỉnh lẻ bằng cạnh giả, đồ thị thành Euler
(mọi bậc chẵn), tìm một mạch Euler, rồi xóa cạnh giả → tách thành
đúng $\max(1,o_i/2)$ trail.

Cài đặt:
1. Dựng kề cho $m$ cạnh thật (id $0..m-1$).
2. Với mỗi liên thông (BFS/DFS trên đỉnh có bậc $>0$), thu danh sách đỉnh lẻ,
   thêm cạnh giả nối từng cặp $(o_0,o_1),(o_2,o_3),\dots$ (có thể song song,
   có thể nối hàng–hàng hoặc cột–cột — không sao vì chỉ dùng để tìm mạch Euler).
3. Hierholzer lặp (stack + con trỏ `ptr`, mảng `used`) tìm mạch Euler cho
   từng liên thông đã bù.
4. Cắt mạch tại các cạnh giả: nếu không có cạnh giả → 1 trail;
   ngược lại xoay mạch để bắt đầu sau một cạnh giả rồi cắt thành các đoạn
   cạnh thật, bỏ đoạn rỗng.
5. Mỗi đoạn in ra theo thứ tự cạnh → thứ tự cell $(r,c)$.

Trường hợp $m=0$ in $0$.

## 3. Chứng minh $k \le n$

Chỉ xét các liên thông có cạnh, gọi $v_i$ là số đỉnh của nó ($v_i\ge 2$).
Đóng góp của nó là $\max(1,o_i/2)\le v_i/2$:
- nếu Euler ($o_i=0$): $1\le v_i/2$ vì $v_i\ge 2$;
- nếu không: $o_i/2\le v_i/2$ hiển nhiên.

Tổng $k\le \sum v_i/2 \le 2n/2 = n$.
(Chi tiết: liên thông Euler có cạnh trong đơn đồ thị hai phía thực ra có
$v_i\ge 4$, nên bất đẳng thức càng chặt; $v_i\ge 2$ đã đủ.)

Tính vuông góc được đảm bảo như mục 1 vì đồ thị gốc hai phía:
hai cạnh thật kề nhau trong trail chung đúng một đầu mút, và các đầu mút
chung liên tiếp nằm khác phía.

## 4. Độ phức tạp

- Đỉnh $2n\le 4\cdot10^5$, cạnh thật + giả $\le m+n\le 4\cdot10^5$.
- BFS tìm liên thông + Hierholzer: $O(n+m)$.
- Bộ nhớ $O(n+m)$.
- Thực đo: random $n=m=2\cdot10^5$ chạy $\approx 0.3$s.

## 5. Cách test

- Biên dịch: `g++ -O2 -std=c++17 -o A A.cpp`.
- 2 sample trong đề: đều PASS (validator kiểm tra: mỗi cell đúng 1 lần,
  kề nhau chung hàng/cột, bộ ba vuông góc, $k\le n$).
- Sample 1 cho $k=1$, sample 2 cho $k=3$ (cách chia có thể khác đáp án mẫu
  nhưng vẫn hợp lệ).
- Stress 200 test ngẫu nhiên $n\le 10$: PASS hết.
- Test lớn $n=m=200000$ ngẫu nhiên: $k=86538\le n$, thời gian $0.3$s.
- Validator dùng script Python đọc output, assert 4 điều kiện trên.
