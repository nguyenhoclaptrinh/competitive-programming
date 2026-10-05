#!/usr/bin/env python3
"""TTS theo segment: segments/slideN.txt -> segments/slideN.mp3 -> audio.mp3.
- Tiền xử lý mỗi segment qua tools/pronunciation.tsv (literal theo thứ tự + regex re:).
- Tổng hợp từng đoạn bằng edge-tts, nối audio bằng ffmpeg concat, đo duration thật.
- Ghi segments/timing.json {durations, starts, total}.
- Đồng thời tái tạo narration.txt (nối các segment thô) để làm tài liệu tham khảo.
Cách dùng: python3 seg_tts.py <lecture-dir> [voice] [rate]
"""
import csv, json, os, re, shutil, subprocess, sys, tempfile

def find_edge_tts():
    cands = [shutil.which("edge-tts"), ".venv/bin/edge-tts",
             "/tmp/opencode/tts-env/bin/edge-tts"]
    for c in cands:
        if c and os.path.isfile(c) and os.access(c, os.X_OK):
            return c
    sys.exit("ERR: không tìm thấy edge-tts (cài: python3 -m venv /tmp/opencode/tts-env && .../pip install edge-tts)")

def load_dict(path):
    literals, regexes = [], []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line or line.startswith("#") or "\t" not in line:
                continue
            src, dst = line.split("\t", 1)
            if src.startswith("re:"):
                regexes.append((re.compile(src[3:]), dst))
            else:
                literals.append((src, dst))
    return literals, regexes

def space_binary(m):
    return " ".join(m.group(1))

def preprocess(text, literals, regexes):
    for src, dst in literals:
        text = text.replace(src, dst)
    for pat, dst in regexes:
        text = pat.sub(dst, text)
    text = re.sub(r"\b([01]{3,})\b", space_binary, text)
    return text

def ffprobe_dur(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                          "format=duration", "-of",
                          "default=noprint_wrappers=1:nokey=1", path],
                         capture_output=True, text=True, check=True)
    return float(out.stdout.strip())

def main():
    lec = sys.argv[1] if len(sys.argv) > 1 else "."
    voice = sys.argv[2] if len(sys.argv) > 2 else "vi-VN-HoaiMyNeural"
    rate = sys.argv[3] if len(sys.argv) > 3 else "-5%"
    edge = find_edge_tts()
    segdir = os.path.join(lec, "segments")
    files = sorted([f for f in os.listdir(segdir)
                    if f.startswith("slide") and f.endswith(".txt")],
                   key=lambda x: int("".join(filter(str.isdigit, x)) or 0))
    assert files, f"không có segments/*.txt trong {lec}"
    tools = os.path.dirname(os.path.abspath(__file__))
    literals, regexes = load_dict(os.path.join(tools, "pronunciation.tsv"))

    durations, raws = [], []
    for fn in files:
        raw = open(os.path.join(segdir, fn), encoding="utf-8").read().strip()
        raws.append(raw)
        clean = preprocess(raw, literals, regexes)
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False,
                                         encoding="utf-8") as tf:
            tf.write(clean)
            tmp = tf.name
        mp3 = os.path.join(segdir, fn.replace(".txt", ".mp3"))
        subprocess.run([edge, "--voice", voice, "--rate", rate,
                        "--file", tmp, "--write-media", mp3],
                       check=True, capture_output=True)
        os.unlink(tmp)
        d = ffprobe_dur(mp3)
        durations.append(round(d, 2))
        print(f"  {fn}: {d:.2f}s")

    # Nối các đoạn thành audio.mp3
    lst = os.path.join(segdir, "_concat.txt")
    with open(lst, "w", encoding="utf-8") as f:
        for fn in files:
            f.write(f"file '{os.path.abspath(os.path.join(segdir, fn.replace('.txt', '.mp3')))}'\n")
    audio = os.path.join(lec, "audio.mp3")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0",
                    "-i", lst, "-c", "copy", audio], check=True)
    os.unlink(lst)

    starts, acc = [], 0.0
    for d in durations:
        starts.append(round(acc, 2))
        acc += d
    json.dump({"files": files, "durations": durations, "starts": starts,
               "total": round(acc, 2), "voice": voice, "rate": rate},
              open(os.path.join(segdir, "timing.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    # narration.txt tham khảo = nối các segment thô
    open(os.path.join(lec, "narration.txt"), "w", encoding="utf-8").write(
        "\n\n".join(raws) + "\n")
    print(f"audio ok: {audio} ({acc:.2f}s, {len(files)} segments)")

if __name__ == "__main__":
    main()
