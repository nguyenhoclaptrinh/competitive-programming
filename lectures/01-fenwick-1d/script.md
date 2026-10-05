# Bài 1: Fenwick Tree 1D — Kịch bản giảng (hình + tiếng)

Nguồn: `ICPC-Handbook.md` §1.1 — Cập nhật điểm, tổng đoạn, O(log N).
Thời lượng audio: ~153s. Slide: `slides.html` (8 slide). Audio: `audio.mp3`. Video: `video.mp4`.

## Cách học bài này (hình + tiếng cùng lúc)

1. Mở `slides.html` trên trình duyệt.
2. Bấm Play ở thanh audio (giọng tiếng Việt).
3. Bấm nút “Next bước” trên Slide 4 và Slide 5 theo lời đọc. Dùng phím ← → để chuyển slide.

## Kịch bản theo mốc audio

| Mốc | Thời lượng | Lời giảng (tóm tắt) | Hình trên slide |
|---|:---:|---|---|
| 0:00 | 36.5s | Hook: mảng 1e5, query + update liên tục, O(n) sẽ TLE | Slide 1: bài toán + mảng a=[3,1,4,1,5,9,2,6] |
| 0:36 | 35.1s | So sánh 3 cách: duyệt tay / prefix-sum / Fenwick | Slide 2: bảng độ phức tạp + ví dụ đổi tiền |
| 1:12 | 38.6s | LSB `p & -p`, nút p quản lý `(p-LSB, p]`, bảng p=1..8 | Slide 3: bảng nhị phân + sơ đồ thanh bao phủ SVG |
| 1:50 | 53.1s | Query(7): 7→[7,7], 6→[5,6], 4→[1,4] = 2+14+9=25 | Slide 4: hoạt hình Next bước + công thức sum(l,r) |
| 2:43 | 41.9s | Add(5,10): 5→6→8, tree[5,6,8] += 10 | Slide 5: hoạt hình Next bước + sơ đồ cha–con SVG |
| 3:25 | 46.0s | Bẫy 1-based: `add(0)` → `0+=0` → vòng lặp vô tận | Slide 6: code sai vs đúng, 0-based → +1 |
| 4:11 | 29.4s | Code chuẩn C++20 giải thích từng dòng | Slide 7: struct Fenwick + 3 điểm phải nhớ |
| 4:41 | 33.5s | Tự kiểm tra 3 câu + bài tập nghịch thế, K-th one | Slide 8: đáp án gợi ý + bài tiếp theo 1.2 |

## Công thức phải thuộc

- LSB: `p & -p`
- Query tiền tố: `for(; p>0; p -= p&-p) sum += tree[p]` (đi xuống)
- Add điểm: `for(; p<=n; p += p&-p) tree[p] += v` (đi lên)
- Tổng đoạn: `query(r) - query(l-1)`
- Bắt buộc 1-based. Đề 0-based → +1 mọi index.
- Mọi `sum` dùng `long long`.

## Code chuẩn (từ Handbook)

```cpp
struct Fenwick {
    int n; vector<long long> tree;
    Fenwick(int n): n(n), tree(n+1, 0) {}
    void add(int p, long long v){ for(; p<=n; p += p&-p) tree[p]+=v; }
    long long query(int p) const { long long s=0; for(; p>0; p -= p&-p) s+=tree[p]; return s; }
    long long queryRange(int l,int r) const { return l>r?0:query(r)-query(l-1); }
};
```

## Tự kiểm tra

1. `add(3,7)` chạm nút nào? (Đáp: 3, 4, 8)
2. `query(5)` chạm nút nào? (Đáp: 5, 4)
3. Vì sao `query(0)` an toàn nhưng `add(0,v)` treo? (Đáp: query thoát ngay ở `p>0`, add kẹt ở `p<=n` với `p+=0`)

Bài tiếp theo: 1.2 Range Update Range Query — mảng hiệu D, 2 cây BIT, công thức `S(p)=(p+1)*sumD - sum(j*D)`.
