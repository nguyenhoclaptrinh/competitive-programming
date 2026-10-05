---
name: lecture-builder
description: Biến 1 mục ICPC-Handbook thành gói bài giảng đa phương tiện hoàn chỉnh (slides.html tương tác offline, audio TTS vi-VN, video mp4 đồng bộ). Dùng khi tạo bài giảng mới hoặc nâng cấp bài cũ.
---

# Skill: Lecture Builder (ICPC Handbook → Bài giảng Đa phương tiện)

## 1. Khi nào kích hoạt

- Người dùng yêu cầu: "làm bài giảng", "làm tiếp bài N", "sửa slide", "thêm animation/hình", "thiếu dấu tiếng Việt", "đồng bộ video".
- Đầu vào: 1 chuyên đề trong [ICPC-Handbook.md](../../ICPC-Handbook.md).
- Đầu ra: Thư mục `lectures/<slug>/` chuẩn hóa đủ tệp theo [PIPELINE.md](../PIPELINE.md): `segments/`, `narration.txt`, `script.md`, `slides.html`, `slides.manifest.tsv`, `slides/slideN.png`, `audio.mp3`, `video.mp4`.

---

## 2. Kiến trúc Sư phạm Chuẩn (8-Slide Rubric)

Mỗi bài giảng bắt buộc tuân theo cấu trúc 8 slide nhằm đạt hiệu quả tiếp thu tối đa trong 3–5 phút:

1. **Slide 1: Hook & Vấn đề Thực tế**: Bối cảnh $N, Q = 10^5$, cách làm ngây thơ duyệt mảng bị quá thời gian (TLE).
2. **Slide 2: Trực giác Cốt lõi & So sánh**: Bảng so sánh độ phức tạp với các giải thuật khác; ẩn dụ trực quan (ví dụ: đổi tiền lũy thừa 2).
3. **Slide 3: Nền tảng Toán học / Phép biến đổi Bit**: Giải thích cốt lõi (ví dụ `p & -p`, LSB, phân hoạch đoạn) kèm bảng tra cứu và sơ đồ bao phủ SVG.
4. **Slide 4: Thao tác Truy vấn (Query)**: Giải thích đường đi, có nút `Next bước` chạy hoạt hình từng bước với mảng ví dụ số thực tế. Đáp án cuối **chỉ hiện sau bước cuối** (progressive reveal, không spoil trong cover).
5. **Slide 5: Thao tác Cập nhật (Update/Build)**: Giải thích đường đi lên cây cha-con, có nút `Next bước` và sơ đồ SVG. Đáp án cuối reveal dần như Slide 4.
6. **Slide 6: Bẫy phòng thi ICPC (ít nhất 2 bẫy)**: Lỗi kinh điển (1-based vs 0-based, tràn số 32-bit → `long long`, lặp vô tận, trường hợp biên như `query(0)` an toàn).
7. **Slide 7: Code Template C++20 Chuẩn Thi Đấu**: Struct tối ưu, chú thích từng dòng, có hộp `.code-header` và nút sao chép (phải có fallback khi mở `file://`), khối tóm tắt 30 giây cuối slide.
8. **Slide 8: Tự kiểm tra & Bài tập Rèn luyện**: 3 câu hỏi kèm thẻ ẩn `[Xem đáp án]` (interactive accordion) + 2–3 bài tập trên Codeforces/LQDOJ + hướng mở rộng bài tiếp theo. **Cấm công thức LaTeX thô** (`$...$`) — viết text thường.

---

## 3. Quy chuẩn Soạn thảo Lời thoại TTS (`segments/slideN.txt`)

Mỗi slide 1 file text trong `segments/`. Được phép viết ký hiệu gọn (`O(log n)`, `p & -p`, `tree[7]`, `LSB`) — bước tiền xử lý tự chuyển thành cách đọc qua **bản máy đọc** [`tools/pronunciation.tsv`](pronunciation.tsv) (literal theo thứ tự + regex `re:` + tách số nhị phân). Chỉ thêm dòng mới vào file đó khi gặp thuật ngữ mới; không sửa nghĩa các dòng cũ.

Để giọng đọc máy `vi-VN-HoaiMyNeural` phát âm tự nhiên, bản TSV bảo đảm các quy tắc sau:

| Ký hiệu gốc | Cách đọc sau tiền xử lý |
|---|---|
| `O(log N)` | `O log n` |
| `O(1)`, `O(N)` | `O 1`, `O n` |
| `p & -p` | `p và trừ p` |
| `p += p & -p` | `p cộng bằng p và trừ p` |
| `LSB` | `L S B` (tách rời từng chữ cái) |
| `TLE` | `T L E` |
| `BIT`, `DSU`, `LCA`, `BFS`, `DFS` | tách rời từng chữ cái |
| Nhị phân `0110` | `0 1 1 0` (đọc rời từng số) |
| `tree[7]`, `a[5]` | `tree 7`, `a 5` (bỏ ngoặc vuông) |

---

## 4. Quy trình Thực thi (Segment-First Workflow)

### Bước 1: Soạn nội dung & Manifest
- Tạo thư mục `lectures/<slug>/` với `segments/slide1.txt...` (số file = số slide theo rubric).
- Lập `script.md` (bảng mốc để tạm — build sẽ đo lại), `slides.html` offline (kế thừa class từ `01-fenwick-1d/slides.html`; mảng cues để placeholder `/*__CUES__*/[]` — **cấm hardcode mốc giờ**), `slides.manifest.tsv` (cột `duration` để tạm; cột `type`/`content` để PNG giàu: `array` vẽ mảng ví dụ, `content` vẽ thẻ công thức/code).
- `narration.txt` do build tái tạo từ segments — không sửa tay.

### Bước 2: Chạy bộ công cụ All-In-One
```bash
./lectures/tools/build_lecture.sh lectures/<slug> [voice] [rate]
# vd: ./lectures/tools/build_lecture.sh lectures/02-fenwick-range-2d vi-VN-NamMinhNeural +0%
```
Lệnh này tự động:
1. TTS từng segment bằng [seg_tts.py](seg_tts.py) (tiền xử lý dict → `segments/slideN.mp3` → nối thành `audio.mp3` → `timing.json` durations đo thật).
2. Đồng bộ bằng [sync_timing.py](sync_timing.py): ghi durations vào manifest, viết lại mốc `script.md`, inject cues vào `slides.html`.
3. Kết xuất PNG 1280x720 bằng [render_slides.py](render_slides.py).
4. Ghép video MP4 H.264 qua FFmpeg Concat bằng [make_video.sh](make_video.sh).
5. Kiểm định nghiệm thu tự động (ngưỡng lệch < 1.0s).

Fallback legacy (chỉ khi chưa tách segments): `tts.sh` whole-file + tự căn cues tay.

---

## 5. Bảng Tiêu chí Kiểm định Bắt buộc (Verification Gate)

Trước khi báo cáo hoàn thành, Agent phải xác nhận 6 tiêu chí (`build_lecture.sh` tự kiểm tra):
1. **Đồng bộ Thời lượng**: `ffprobe` của `audio.mp3` và `video.mp4` chênh lệch **< 1.0 giây**.
2. **Khớp Số lượng**: segments = `<section class="slide"` trong HTML = số dòng data trong `manifest.tsv` = số ảnh trong `slides/` = số cues trong `slideStarts`.
3. **Hiển thị Tiếng Việt**: kiểm tra ngẫu nhiên ít nhất 1 ảnh PNG và tệp HTML đảm bảo không lỗi font tiếng Việt có dấu (DejaVuSans; cấm emoji màu trong PNG PIL).
4. **Tính Năng Tương tác**: nút `Next bước` chạy hoạt hình trơn tru, checkbox `Auto-Sync` bắt đúng mốc `audio.timeupdate`, nút sao chép code có fallback `execCommand` khi `file://`.
5. **Độ sạch Mã nguồn**: không còn `TODO`, `FIXME`, LaTeX thô `$...$`, link tuyệt đối `file:///`, hay `__pycache__`.
6. **Đúng Nội dung**: mọi số trong slide/quiz (giá trị tree, đáp án) đã kiểm chứng bằng code biên dịch thật (`g++ -std=c++20`), không tính nhẩm.
