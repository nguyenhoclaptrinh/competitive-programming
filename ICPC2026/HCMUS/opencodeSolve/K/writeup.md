# Problem K: Lithium and Lithuania — Writeup

## 1. Đề bài (tóm tắt)
- `T <= 1e4`, mỗi test 4 điểm `L, R, W, S` trong `[0.0, 9.0]`, bước `0.5`, đúng 1 chữ số thập phân.
- Overall = trung bình 4 điểm, làm tròn tới bội `0.5` gần nhất; nếu đúng giữa (phần lẻ `.25`/`.75` của average) thì làm tròn **lên**.
- In mỗi overall đúng 1 chữ số thập phân.

Ví dụ đề: average `6.25 -> 6.5`, `6.75 -> 7.0`, `6.125 -> 6.0`, `6.875 -> 7.0`.

## 2. Ý tưởng (số nguyên, tránh float)
Mỗi điểm là bội của `0.5` nên nhân 2 thành số nguyên:
`a = L*2, ...` nguyên trong `[0, 18]`.

Đặt `S2 = a+b+c+d` (nguyên `0..72`). Trung bình:
`avg = S2 / 8`.

Cần `k` sao cho overall `= k*0.5` gần `avg` nhất, nửa giữa làm tròn lên:
`k = round(avg / 0.5) = round(S2 / 4)` với quy tắc half-up.

Với số nguyên không âm: `round_half_up(p/4) = floor((p+2)/4)`, nên:
`k = (S2 + 2) / 4` (chia nguyên).

In ra: phần nguyên `k/2`, phần lẻ `0` nếu `k` chẵn, `5` nếu `k` lẻ.

## 3. Kiểm chứng công thức
- `5 5 9 9`: `S2=56`, `k=58/4=14` → `7.0` ✓
- `6 6 9 9`: `S2=60`, `k=62/4=15` → `7.5` ✓
- `avg 6.125 (S2=49)`: `k=51/4=12` → `6.0` ✓
- `avg 6.875 (S2=55)`: `k=57/4=14` → `7.0` ✓
- `avg 6.25 (S2=50)`: `k=52/4=13` → `6.5` ✓
- `avg 6.75 (S2=54)`: `k=56/4=14` → `7.0` ✓

## 4. Parsing không dùng float
Đọc mỗi điểm dạng `string`, parse:
`val2 = intPart*2 + (dec=='5' ? 1 : 0)`.
Không dùng `double` nên không có sai số nhị phân.

## 5. Code
Xem `K.cpp`. Độ phức tạp `O(T)`, `O(1)` bộ nhớ.

## 6. Test
Sample:
```
2
5.0 5.0 9.0 9.0
6.0 6.0 9.0 9.0
```
Output:
```
7.0
7.5
```
Khớp sample.
