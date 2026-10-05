---
name: lecture-builder
description: Biến 1 mục ICPC-Handbook thành gói bài giảng đa phương tiện hoàn chỉnh (slides.html tương tác offline, audio TTS vi-VN, video mp4 đồng bộ). Dùng khi tạo bài giảng mới hoặc nâng cấp bài cũ.
---

# Skill: Lecture Builder (ICPC Handbook → Bài giảng Đa phương tiện)

## 1. Khi nào kích hoạt

- Người dùng yêu cầu: "làm bài giảng", "làm tiếp bài N", "sửa slide", "thêm animation/hình", "thiếu dấu tiếng Việt", "đồng bộ video".
- Đầu vào: 1 chuyên đề trong [ICPC-Handbook.md](file:///mnt/Data/Workspaces/Competitive%20Programming/ICPC-Handbook.md).
- Đầu ra: Thư mục `lectures/<slug>/` chuẩn hóa đủ 7 tệp theo [PIPELINE.md](file:///mnt/Data/Workspaces/Competitive%20Programming/lectures/PIPELINE.md).

---

## 2. Kiến trúc Sư phạm Chuẩn (8-Slide Rubric)

Mỗi bài giảng bắt buộc tuân theo cấu trúc 8 slide nhằm đạt hiệu quả tiếp thu tối đa trong 3–5 phút:

1. **Slide 1: Hook & Vấn đề Thực tế**: Bối cảnh $N, Q = 10^5$, cách làm ngây thơ duyệt mảng bị quá thời gian (TLE).
2. **Slide 2: Trực giác Cốt lõi & So sánh**: Bảng so sánh độ phức tạp với các giải thuật khác; ẩn dụ trực quan (ví dụ: đổi tiền lũy thừa 2).
3. **Slide 3: Nền tảng Toán học / Phép biến đổi Bit**: Giải thích cốt lõi (ví dụ `p & -p`, LSB, phân hoạch đoạn) kèm bảng tra cứu và sơ đồ bao phủ SVG.
4. **Slide 4: Thao tác Truy vấn (Query)**: Giải thích đường đi, có nút `Next bước` chạy hoạt hình từng bước với mảng ví dụ số thực tế.
5. **Slide 5: Thao tác Cập nhật (Update/Build)**: Giải thích đường đi lên cây cha-con, có nút `Next bước` và sơ đồ SVG.
6. **Slide 6: Bẫy phòng thi ICPC (Corner Cases)**: Chỉ rõ lỗi sai kinh điển (1-based vs 0-based, tràn số 32-bit `long long`, lặp vô tận, đồ thị không liên thông).
7. **Slide 7: Code Template C++20 Chuẩn Thi Đấu**: Struct tối ưu, chú thích từng dòng, có hộp `.code-header` và nút `📋 Sao chép mã C++`.
8. **Slide 8: Tự kiểm tra & Bài tập Rèn luyện**: 3 câu hỏi kèm thẻ ẩn `[Xem đáp án]` (interactive accordion) + 2–3 bài tập trên Codeforces/LQDOJ + hướng mở rộng bài tiếp theo.

---

## 3. Quy chuẩn Soạn thảo Lời thoại TTS (`narration.txt`)

Để giọng đọc máy `vi-VN-HoaiMyNeural` phát âm tự nhiên, chuẩn xác, bắt buộc tuân theo từ điển phiên âm:

| Ký hiệu gốc | Cách viết trong `narration.txt` |
|---|---|
| `O(log N)` | `O log n` hoặc `độ phức tạp log n` |
| `O(1)`, `O(N)` | `O 1`, `O n` |
| `p & -p` | `p và trừ p` |
| `p += p & -p` | `p cộng bằng p và trừ p` |
| `LSB` | `L S B` (viết tách rời từng chữ cái) |
| `TLE` | `quá thời gian thi đấu T L E` |
| `BIT` | `B I T` |
| `DSU` | `D S U` |
| `LCA` | `L C A` |
| `2-SAT` | `hai S A T` |
| `BFS`, `DFS` | `B F S`, `D F S` |
| Nhị phân `0110` | `0 1 1 0` (đọc rời từng số nhị phân) |
| Không dùng | Tuyệt đối không để nguyên công thức LaTeX `$`, ký hiệu `&`, `^`, `|` |

---

## 4. Quy trình Thực thi (All-In-One Workflow)

### Bước 1: Soạn nội dung & Manifest
- Tạo thư mục `lectures/<slug>/`.
- Viết `narration.txt` (~600–900 từ, ~3–4 phút).
- Lập `script.md` khớp mốc thời gian.
- Tạo `slides.html` offline (kế thừa các class giao diện từ `01-fenwick-1d/slides.html`: Auto-Sync, Speed buttons, Syntax highlighting, Interactive Quiz cards).
- Khai báo `slides.manifest.tsv` có cột `duration` khớp chính xác thời lượng thoại từng slide.

### Bước 2: Chạy bộ công cụ All-In-One
Chạy lệnh tự động hóa toàn bộ quy trình:
```bash
./lectures/tools/build_lecture.sh lectures/<slug> [voice]
```
Lệnh này sẽ tự động:
1. Sinh âm thanh TTS bằng [tts.sh](file:///mnt/Data/Workspaces/Competitive%20Programming/lectures/tools/tts.sh).
2. Kết xuất 8 slide PNG 1280x720 bằng [render_slides.py](file:///mnt/Data/Workspaces/Competitive%20Programming/lectures/tools/render_slides.py).
3. Ghép video MP4 chuẩn H.264 qua FFmpeg Concat bằng [make_video.sh](file:///mnt/Data/Workspaces/Competitive%20Programming/lectures/tools/make_video.sh).
4. Thực hiện kiểm định nghiệm thu tự động.

---

## 5. Bảng Tiêu chí Kiểm định Bắt buộc (Verification Gate)

Trước khi báo cáo hoàn thành, Agent phải xác nhận 5 tiêu chí:
1. **Đồng bộ Thời lượng**: `ffprobe` của `audio.mp3` và `video.mp4` chênh lệch $< 0.5$ giây.
2. **Khớp Số lượng Slide**: Đếm `<section class="slide"` trong HTML = số dòng data trong `manifest.tsv` = số ảnh trong `slides/` (chuẩn 8 slide).
3. **Hiển thị Tiếng Việt**: Kiểm tra ngẫu nhiên ít nhất 1 ảnh PNG và tệp HTML đảm bảo không lỗi font tiếng Việt có dấu.
4. **Tính Năng Tương tác**: Nút `Next bước` chạy hoạt hình trơn tru, checkbox `Auto-Sync` bắt đúng mốc thời gian `audio.timeupdate`.
5. **Độ sạch Mã nguồn**: Không còn `TODO`, `FIXME` hay mã rác trong thư mục bài giảng.
