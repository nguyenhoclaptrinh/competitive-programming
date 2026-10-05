# Bài giảng ICPC-Handbook: Hình ảnh Trực quan + Giọng đọc Tự nhiên

Hệ thống số hóa **22 chuyên đề** trọng tâm từ `ICPC-Handbook.md` thành chuỗi bài giảng đa phương tiện (slides tương tác offline HTML, audio TTS chuẩn tiếng Việt, video MP4 đồng bộ chuẩn xác).

> **Bản mẫu hoàn thiện**: [01-fenwick-1d/](01-fenwick-1d/) (314s audio + video MP4 + slide HTML tương tác có hoạt hình từng bước).  
> Mở file `01-fenwick-1d/slides.html` trên trình duyệt, bấm **Play** ở thanh audio để tự động nghe giảng và xem slide nhảy tự động (Auto-Sync).

---

## 1. Lộ trình 12 chuyên đề chuẩn hóa

Nhằm đảm bảo mỗi bài giảng truyền tải sâu sắc trong **3–5 phút (tối đa 8 slide)** mà không gây quá tải nhận thức, 22 mục trong Handbook được phân bổ thành 12 bài chuyên đề:

| Bài | Chuyên đề Handbook | Thư mục | Trạng thái |
|:---:|---|---|:---:|
| **01** | §1.1 Fenwick Tree 1D (Point Update, Range Sum) | `01-fenwick-1d/` | **HOÀN THÀNH** |
| **02** | §1.2 Range-BIT (Mảng hiệu), §1.3 Fenwick 2D | `02-fenwick-range-2d/` | **SEGMENTS SẴN SÀNG** |
| **03** | §1.4 Disjoint Set Union (DSU), §1.5 Sparse Table | `03-dsu-sparse/` | **SEGMENTS SẴN SÀNG** |
| **04** | §2.1 Topological Sort, §2.2 0-1 BFS, §2.3 Bellman-Ford, §2.4 Floyd-Warshall | `04-shortest-path/` | **SEGMENTS SẴN SÀNG** |
| **05** | §2.5 LCA (Binary Lifting), §2.6 2-SAT | `05-topo-lca/` | **SEGMENTS SẴN SÀNG** |
| **06** | §3.1 Dinic Max Flow | `07-max-flow/` | **SEGMENTS SẴN SÀNG** |
| **07** | §3.2 Hopcroft-Karp Bipartite Matching | `08-matching/` | **SEGMENTS SẴN SÀNG** |
| **08** | §4.1 CCW, §4.2 Giao đoạn, §4.3 Điểm trong đa giác | `09-geometry-basics/` | **SEGMENTS SẴN SÀNG** |
| **09** | §4.4 Bao lồi Andrew Monotone Chain | `10-convex-hull/` | **SEGMENTS SẴN SÀNG** |
| **10** | §5.1 Manacher, §5.2 Aho-Corasick | `11-string/` | **SEGMENTS SẴN SÀNG** |
| **11** | §6.1 nCr modulo, §6.2 CRT, §6.3 Pollard Rho | `12-math/` | **SEGMENTS SẴN SÀNG** |

---

## 2. Cấu trúc mỗi gói bài giảng

Mỗi thư mục bài giảng gồm đúng tệp tiêu chuẩn:

1. `segments/slideN.txt` — Lời thoại thô từng slide (nguồn sự thật duy nhất cho TTS).
2. `narration.txt` — **DO BUILD TÁI TẠO** từ segments (tài liệu tham khảo, không sửa tay).
3. `script.md` — Kịch bản sư phạm: mốc audio ↔ slide **DO BUILD VIẾT LẠI** từ timing.json.
4. `slides.html` — Slide tương tác offline (100% inline CSS/JS/SVG, không CDN, có Auto-Sync, nút "Next bước").
5. `slides.manifest.tsv` — Bảng dữ liệu slide (cột `duration` khớp chuẩn xác với audio).
6. `slides/slideN.png` — Khung hình 1280x720, kết xuất bằng `tools/render_slides.py`.
7. `audio.mp3` — Nối các segment bằng ffmpeg concat.
8. `video.mp4` — Video MP4 (H.264/AAC) ghép PNG + audio qua FFmpeg Concat filter.

---

## 3. Cách chạy quy trình sinh bài giảng

### Cách 1: Tự động hóa 1 lệnh (Khuyên dùng)
```bash
./lectures/tools/build_lecture.sh lectures/02-fenwick-range-2d [voice] [rate]
# vd giọng nam, tốc độ gốc: .../build_lecture.sh lectures/02-fenwick-range-2d vi-VN-NamMinhNeural +0%
```
Tự động: TTS từng `segments/slideN.txt` (phiên âm qua `pronunciation.tsv`) → đo durations thật → đồng bộ manifest + `script.md` + cues HTML → xuất PNG 1280x720 → ghép video MP4 (lệch 0.02s) → kiểm định nghiệm thu.

### Cách 2: Legacy khi chưa tách segments (không khuyến khích)
```bash
LEC=lectures/01-fenwick-1d

# 1. Sinh audio thuyết minh từ narration.txt
./lectures/tools/tts.sh $LEC/narration.txt $LEC/audio.mp3

# 2. Kết xuất hình ảnh slide PNG 1280x720
python3 lectures/tools/render_slides.py $LEC

# 3. Ghép video đồng bộ hoàn hảo theo duration từng slide
./lectures/tools/make_video.sh $LEC
```

---

## 4. Build toàn bộ 11 bài còn lại (chạy tuần tự)

```bash
for d in \
  02-fenwick-range-2d \
  03-dsu-sparse \
  04-shortest-path \
  05-topo-lca \
  07-max-flow \
  08-matching \
  09-geometry-basics \
  10-convex-hull \
  11-string \
  12-math
do
  echo "=== Building $d ==="
  ./lectures/tools/build_lecture.sh lectures/$d vi-VN-HoaiMyNeural -5%
done
```

Mỗi bài ~300-400s audio, build mất ~2-3 phút. Tổng ~30 phút.