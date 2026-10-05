# Pipeline: Handbook → Bài giảng Hình + Tiếng

Chuẩn quy trình hóa bài giảng đa phương tiện đồng bộ cho toàn bộ 22 chuyên đề ICPC Handbook.
Nguồn sự thật duy nhất của lời thoại: **`segments/slideN.txt`** (1 file/slide). Mọi timing (manifest, script.md, cues HTML) do build đo và đồng bộ tự động — cấm sửa tay.

---

## 0. Chuẩn bị môi trường (một lần duy nhất)

```bash
python3 -m venv /tmp/opencode/tts-env
/tmp/opencode/tts-env/bin/pip install edge-tts
# Giọng chuẩn: vi-VN-HoaiMyNeural (nữ) hoặc vi-VN-NamMinhNeural (nam); rate mặc định -5%
```

Yêu cầu hệ thống: `ffmpeg`, `ffprobe`, `python3 + PIL`.
Font chữ: **DejaVuSans** (hỗ trợ đầy đủ tiếng Việt có dấu; cấm emoji màu trong PNG vì PIL không có font emoji).

---

## 1. Cấu trúc chuẩn mỗi bài giảng

```
lectures/<slug>/
  segments/slideN.txt  # Lời thoại thô từng slide (được viết ký hiệu gọn, dict tự phiên âm)
  segments/slideN.mp3  # Audio từng đoạn (đo duration thật) + timing.json
  narration.txt        # DO BUILD TÁI TẠO từ segments (tài liệu tham khảo, không sửa tay)
  script.md            # Kịch bản: mốc audio ↔ slide DO BUILD VIẾT LẠI từ timing.json
  slides.html          # Slide tương tác OFFLINE: SVG + Next bước + <audio> + cues /*__CUES__*/[]
  slides.manifest.tsv  # slide<TAB>duration<TAB>title<TAB>sub<TAB>desc<TAB>type<TAB>content
  slides/slideN.png    # 1280x720, kết xuất bằng tools/render_slides.py
  audio.mp3            # Nối các segment bằng ffmpeg concat
  video.mp4            # Ghép PNG + audio: mỗi ảnh -loop 1 -t dur riêng + concat filter
```

---

## 2. Quy trình thực hiện mỗi bài mới (segment-first)

```bash
LEC=lectures/02-fenwick-range-2d
# B0. Soạn: segments/slideN.txt + slides.html (cues để placeholder) + slides.manifest.tsv + script.md
# B1. Build 1 lệnh (TTS từng đoạn, sync timing, render PNG, ghép video, nghiệm thu):
./lectures/tools/build_lecture.sh $LEC [voice] [rate]
```

Fallback legacy (chỉ khi chưa tách segments): `tts.sh` whole-file → `render_slides.py` → `make_video.sh` → tự căn cues tay trong HTML.

---

## 3. Quy ước chất lượng bắt buộc (Invariants)

1. **Tiếng Việt có dấu 100%** ở mọi tệp: segments, narration, slide HTML, PNG, script, README. Không để tiêu đề không dấu.
2. Segment được viết ký hiệu gọn; [`tools/pronunciation.tsv`](tools/pronunciation.tsv) chịu trách nhiệm phiên âm (`p & -p` → `p và trừ p`, `LSB` → `L S B`, `tree[7]` → `tree 7`, số nhị phân đọc rời). Thêm thuật ngữ mới = thêm dòng vào TSV.
3. `slides.html`: Offline hoàn toàn (inline CSS/JS/SVG, không CDN). Mỗi thuật toán có ví dụ số cụ thể, slide Query/Add có nút `Next bước` + progressive reveal (đáp án chỉ hiện sau bước cuối), header có `Auto-Sync` + nút tốc độ. Nút sao chép code phải có fallback `execCommand` (mở `file://` không có clipboard API).
4. **Một nguồn sự thật timing**: `segments/timing.json` (đo thật). `sync_timing.py` ghi đè durations manifest + mốc script.md + cues HTML. Cấm hardcode mốc giờ trong HTML.
5. Slide áp chót là code C++ chuẩn giải thích từng dòng (+ tóm tắt 30 giây); slide cuối là 3 câu tự kiểm tra có đáp án + bài tập. Cấm LaTeX thô `$...$` trong HTML.
6. Số slide 6–8 slide/bài. PNG giàu nội dung qua cột `type` (`array` vẽ mảng ví dụ) và `content` (thẻ công thức/code ≤ 5 dòng).
7. Mọi số trong slide/quiz phải kiểm chứng bằng code biên dịch thật trước khi build.

---

## 4. Bẫy kỹ thuật đã giải quyết

| Hiện tượng | Nguyên nhân | Giải pháp chuẩn hóa trong Pipeline |
|---|---|---|
| Video lệch hình so với tiếng (concat demuxer cộng dư ~23s) | Concat demuxer không tôn trọng duration với input ảnh tĩnh | TTS từng segment → durations đo thật → mỗi ảnh `-loop 1 -t dur` riêng + concat filter (lệch 0.02s). |
| Mất dấu tiếng Việt trên ảnh PNG | PIL dùng font bitmap mặc định | Font `DejaVuSans`/`DejaVuSansMono`; cấm emoji màu trong PNG. |
| Treo hoặc mất môi trường `edge-tts` | Đường dẫn venv `/tmp` bị dọn dẹp | `tts.sh`/`seg_tts.py` fallback: `command -v edge-tts` → `.venv` → `/tmp`. |
| Slide HTML không tự chuyển theo audio | Audio độc lập với DOM | `audio.timeupdate` + `chkAutoSync`; cues do build inject từ manifest. |
| Cues HTML lệch sau khi sửa narration | Mốc hardcode 2 nơi | Placeholder `/*__CUES__*/[]` + `sync_timing.py` ghi đè mỗi build. |
| Nút sao chép im lặng khi mở `file://` | clipboard API cần secure context | Fallback `textarea.execCommand('copy')` + `catch` báo thủ công. |
| Đầy màn hình/tràn chữ trên slide PNG | Text dài hơn chiều rộng cố định | `textwrap` trong `render_slides.py` + cột `content` ngắn gọn. |
| Link gãy trên máy khác | Link tuyệt đối `file:///...` | Chỉ dùng relative path trong mọi `.md`. |

---

## 5. Lộ trình triển khai (12 Chuyên đề)

Xem chi tiết bảng phân bổ 12 chuyên đề tại [README.md](README.md).
Mỗi chuyên đề được đóng gói độc lập theo đúng cấu trúc ở Mục 1. Quy tắc: **làm chỉn chu từng bài (nội dung + media + gate xanh) rồi mới qua bài mới**.
