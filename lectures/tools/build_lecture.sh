#!/bin/bash
# ==============================================================================
# All-In-One Lecture Builder & Verification Pipeline
# Cách dùng: ./lectures/tools/build_lecture.sh <lecture-dir> [voice] [rate]
# Ví dụ:   ./lectures/tools/build_lecture.sh lectures/01-fenwick-1d
#          ./lectures/tools/build_lecture.sh lectures/01-fenwick-1d vi-VN-NamMinhNeural +0%
# Nguồn sự thật duy nhất: segments/slideN.txt (+ tools/pronunciation.tsv).
# Fallback legacy: narration.txt (không có segments/) -> tts.sh whole-file.
# ==============================================================================
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LEC="${1:?Thiếu thư mục bài giảng (ví dụ: lectures/01-fenwick-1d)}"
VOICE="${2:-vi-VN-HoaiMyNeural}"
RATE="${3:--5%}"

LEC_NAME="$(basename "$LEC")"
echo "================================================================================"
echo "BẮT ĐẦU XÂY DỰNG BÀI GIẢNG: $LEC_NAME (voice=$VOICE, rate=$RATE)"
echo "================================================================================"

# 1. Kiểm tra đầu vào
test -f "$LEC/slides.html" || { echo "❌ Thiếu $LEC/slides.html" >&2; exit 1; }
test -f "$LEC/slides.manifest.tsv" || { echo "❌ Thiếu $LEC/slides.manifest.tsv" >&2; exit 1; }
mkdir -p "$LEC/slides" "$LEC/segments"

# 2. Sinh Audio TTS
if ls "$LEC"/segments/slide*.txt >/dev/null 2>&1; then
  echo "[Bước 1/5] TTS theo segment + đo duration thật..."
  python3 "$DIR/seg_tts.py" "$LEC" "$VOICE" "$RATE"
  echo "[Bước 2/5] Đồng bộ manifest + script.md + cues HTML..."
  python3 "$DIR/sync_timing.py" "$LEC"
else
  echo "[Bước 1/5] (legacy, không có segments/) TTS whole-file..."
  test -f "$LEC/narration.txt" || { echo "❌ Thiếu narration.txt và segments/" >&2; exit 1; }
  "$DIR/tts.sh" "$LEC/narration.txt" "$LEC/audio.mp3" "$VOICE"
  echo "[Bước 2/5] (legacy) bỏ qua sync_timing — kiểm tra cues tay."
fi

# 3. Kết xuất ảnh slide PNG 1280x720
echo "[Bước 3/5] Kết xuất ảnh slide PNG 1280x720..."
python3 "$DIR/render_slides.py" "$LEC"

# 4. Ghép Video MP4 đồng bộ
echo "[Bước 4/5] Ghép video MP4 theo duration manifest..."
"$DIR/make_video.sh" "$LEC"

# 5. Kiểm định nghiệm thu
echo "[Bước 5/5] Kiểm định chất lượng..."

AUD_DUR=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$LEC/audio.mp3")
VID_DUR=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$LEC/video.mp4")
DIFF=$(python3 -c "print(abs($AUD_DUR - $VID_DUR))")

N_SEC=$(grep -c "<section class=\"slide" "$LEC/slides.html" || true)
N_MAN=$(tail -n +2 "$LEC/slides.manifest.tsv" | wc -l)
N_PNG=$(ls -1 "$LEC"/slides/slide*.png 2>/dev/null | wc -l)
N_SEG=$(ls -1 "$LEC"/segments/slide*.txt 2>/dev/null | wc -l)
N_CUES=$(python3 -c "import re;print(len(eval(re.search(r'/\*__CUES__\*/(\[[^\]]*\])', open('$LEC/slides.html',encoding='utf-8').read()).group(1))))" 2>/dev/null || echo 0)

echo "--------------------------------------------------------------------------------"
echo "BÁO CÁO NGHIỆM THU: $LEC_NAME"
echo "  • Thời lượng Audio : ${AUD_DUR}s"
echo "  • Thời lượng Video : ${VID_DUR}s (lệch: ${DIFF}s, ngưỡng < 1.0s)"
echo "  • Segments / HTML / Manifest / PNG / Cues: $N_SEG / $N_SEC / $N_MAN / $N_PNG / $N_CUES"
echo "--------------------------------------------------------------------------------"

python3 - <<EOF
assert $DIFF < 1.0, f"LỖI: Audio và Video lệch quá 1s! ({$DIFF} s)"
assert $N_SEC == $N_MAN == $N_PNG, f"LỖI: Không khớp số slide! HTML=$N_SEC, Manifest=$N_MAN, PNG=$N_PNG"
assert $N_SEG == 0 or $N_SEG == $N_SEC, f"LỖI: segments ($N_SEG) != slides ($N_SEC)"
assert $N_CUES == 0 or $N_CUES == $N_SEC, f"LỖI: cues ($N_CUES) != slides ($N_SEC)"
print("TẤT CẢ TIÊU CHÍ NGHIỆM THU ĐẠT.")
EOF

echo "HOÀN TẤT GÓI BÀI GIẢNG: $LEC"
