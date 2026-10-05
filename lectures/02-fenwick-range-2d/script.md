# Bài 2: Range Update Range Query + Fenwick 2D — O(log N) — Kịch bản giảng (hình + tiếng)

Nguồn: `ICPC-Handbook.md`. Slide: `slides.html` (8 slide). Audio: `audio.mp3`. Video: `video.mp4`.

## Cách học (hình + tiếng cùng lúc)

1. Mở `slides.html` trên trình duyệt. 2. Bấm Play ở thanh audio.
3. Bấm nút “Next bước” theo lời đọc. Phím N cũng chạy bước tiếp theo.

## Kịch bản theo mốc audio (do build đo lại từ timing.json)

| Mốc | Thời lượng | Lời giảng (tóm tắt) | Hình trên slide |
|---|:---:|---|---|
| 0:00 | 30.0s | Mảng 1e5, add đoạn + hỏi đoạn, RangeBIT 2 cây | Slide 1: Slide 1: bài toán + mảng a |
| 0:00 | 30.0s | Mảng sai phân D, công thức S(p) với 2 cây BIT | Slide 2: Slide 2: bảng a vs D + công thức |
| 0:00 | 30.0s | addRange(2,5,10): D[2]+=10, D[6]-=10 | Slide 3: Slide 3: hoạt hình Next 2 bước |
| 0:00 | 30.0s | queryPrefix(5)=40 là phần cộng thêm, tổng thực 54 | Slide 4: Slide 4: hoạt hình Next 2 bước |
| 0:00 | 30.0s | BIT 2D 32MB vs SegTree 512MB, bù trừ 4 góc | Slide 5: Slide 5: bảng bộ nhớ + công thức |
| 0:00 | 30.0s | add(2,2,5) chạm 4 ô, queryRect 4 góc | Slide 6: Slide 6: lưới 4x4 Next 2 bước |
| 0:00 | 30.0s | Code RangeFenwick + Fenwick2D, tóm tắt 30 giây | Slide 7: Slide 7: code + recap |
| 0:00 | 30.0s | 3 câu quiz có đáp án + bài tiếp theo | Slide 8: Slide 8: quiz + outro |
