# Bài 3: DSU nén đường đi + Sparse Table RMQ O(1) — Kịch bản giảng (hình + tiếng)

Nguồn: `ICPC-Handbook.md`. Slide: `slides.html` (8 slide). Audio: `audio.mp3`. Video: `video.mp4`.

## Cách học (hình + tiếng cùng lúc)

1. Mở `slides.html` trên trình duyệt. 2. Bấm Play ở thanh audio.
3. Bấm nút “Next bước” theo lời đọc. Phím N cũng chạy bước tiếp theo.

## Kịch bản theo mốc audio (do build đo lại từ timing.json)

| Mốc | Thời lượng | Lời giảng (tóm tắt) | Hình trên slide |
|---|:---:|---|---|
| 0:00 | 30.0s | DSU n=8, unite/same, mảng parentOrSize âm/dương | Slide 1: Slide 1: bài toán + mảng |
| 0:00 | 30.0s | unite(1,2) rồi unite(2,3), tập {1,2,3} gốc 1 | Slide 2: Slide 2: hoạt hình Next 2 bước |
| 0:00 | 30.0s | Path Compression vừa đi vừa nén, Union by Size | Slide 3: Slide 3: công thức + cảnh báo |
| 0:00 | 30.0s | Sparse st[j][i], build chẻ đôi, bảng ví dụ | Slide 4: Slide 4: bảng st đầy đủ |
| 0:00 | 30.0s | query(2,7): 2 khối đè, min(1,2)=1 | Slide 5: Slide 5: hoạt hình Next 2 bước |
| 0:00 | 30.0s | Code DSU + Sparse, cấm dùng sum | Slide 6: Slide 6: code + cảnh báo |
| 0:00 | 30.0s | Bẫy index, đệ quy, clz + tóm tắt | Slide 7: Slide 7: 2 cột bẫy + recap |
| 0:00 | 30.0s | 3 câu quiz có đáp án + bài tiếp theo | Slide 8: Slide 8: quiz + outro |
