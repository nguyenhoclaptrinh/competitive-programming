# Bài 3: DSU nén đường đi + Sparse Table RMQ O(1) — Kịch bản giảng (hình + tiếng)

Nguồn: `ICPC-Handbook.md`. Slide: `slides.html` (8 slide). Audio: `audio.mp3`. Video: `video.mp4`.

## Cách học (hình + tiếng cùng lúc)

1. Mở `slides.html` trên trình duyệt. 2. Bấm Play ở thanh audio.
3. Bấm nút “Next bước” theo lời đọc. Phím N cũng chạy bước tiếp theo.

## Kịch bản theo mốc audio (do build đo lại từ timing.json)

| Mốc | Thời lượng | Lời giảng (tóm tắt) | Hình trên slide |
|---|:---:|---|---|
| 0:00 | 45.2s | DSU n=8, unite/same, mảng parentOrSize âm/dương | Slide 1: Slide 1: bài toán + mảng |
| 0:45 | 47.4s | unite(1,2) rồi unite(2,3), tập {1,2,3} gốc 1 | Slide 2: Slide 2: hoạt hình Next 2 bước |
| 1:33 | 40.6s | Path Compression vừa đi vừa nén, Union by Size | Slide 3: Slide 3: công thức + cảnh báo |
| 2:13 | 57.8s | Sparse st[j][i], build chẻ đôi, bảng ví dụ | Slide 4: Slide 4: bảng st đầy đủ |
| 3:11 | 56.9s | query(2,7): 2 khối đè, min(1,2)=1 | Slide 5: Slide 5: hoạt hình Next 2 bước |
| 4:08 | 41.8s | Code DSU + Sparse, cấm dùng sum | Slide 6: Slide 6: code + cảnh báo |
| 4:50 | 47.0s | Bẫy index, đệ quy, clz + tóm tắt | Slide 7: Slide 7: 2 cột bẫy + recap |
| 5:37 | 49.5s | 3 câu quiz có đáp án + bài tiếp theo | Slide 8: Slide 8: quiz + outro |
