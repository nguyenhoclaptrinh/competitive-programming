#!/bin/bash
# Ghép slides/slide*.png + audio.mp3 thành video.mp4, mỗi slide đúng duration trong manifest.
# Phương pháp: -loop 1 -t <dur> cho từng ảnh + concat filter (chính xác từng khung hình,
# tránh lỗi concat demuxer cộng dư thời lượng với input ảnh tĩnh).
# Cách dùng: ./make_video.sh <lecture-dir> [audio.mp3] [video.mp4]
set -e
LEC="${1:?Thiếu lecture-dir}"; AUD="${2:-$LEC/audio.mp3}"; VID="${3:-$LEC/video.mp4}"
MAN="$LEC/slides.manifest.tsv"

if [ ! -f "$AUD" ]; then echo "ERR: Không tìm thấy $AUD" >&2; exit 1; fi

python3 - "$LEC" "$AUD" "$VID" "$MAN" <<'EOF'
import csv, os, subprocess, sys

lec, aud, vid, man = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
sdir = os.path.join(lec, "slides")
pngs = sorted([f for f in os.listdir(sdir) if f.startswith("slide") and f.endswith(".png")],
              key=lambda x: int("".join(filter(str.isdigit, x)) or 0))
assert pngs, f"Không tìm thấy ảnh slide trong {sdir}"
n = len(pngs)

def ffprobe(p):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                          "format=duration", "-of",
                          "default=noprint_wrappers=1:nokey=1", p],
                         capture_output=True, text=True, check=True)
    return float(out.stdout.strip())

total = ffprobe(aud)
durs = None
if os.path.exists(man):
    with open(man, encoding="utf-8") as f:
        r = csv.DictReader(f, delimiter="\t")
        cols = r.fieldnames or []
        c = next((c for c in ["duration", "sec", "time", "s"] if c in cols), None)
        if c:
            vals = [row.get(c, "").strip() for row in r]
            if len(vals) == n and all(vals):
                durs = [float(v) for v in vals]
if durs is None:
    durs = [total / n] * n
else:
    s = sum(durs)
    if s > 0 and abs(s - total) > 0.05:  # co giãn giữ tỷ lệ để khớp audio
        k = total / s
        durs = [d * k for d in durs]
        print(f"-> co giãn durations x{k:.4f} để khớp audio ({total:.2f}s)")

cmd = ["ffmpeg", "-y", "-v", "error"]
for png, d in zip(pngs, durs):
    cmd += ["-loop", "1", "-t", f"{d:.2f}", "-i",
            os.path.abspath(os.path.join(sdir, png))]
cmd += ["-i", os.path.abspath(aud),
        "-filter_complex", "".join(f"[{i}:v]" for i in range(n)) +
        f"concat=n={n}:v=1:a=0[v]",
        "-map", "[v]", "-map", f"{n}:a",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
        "-c:a", "aac", "-shortest", vid]
print(f"slides={n} audio={total:.2f}s")
subprocess.run(cmd, check=True)
out = ffprobe(vid)
print(f"video ok: {vid} ({out:.2f}s, lech {abs(out-total):.2f}s)")
EOF
ls -lh "$VID"
