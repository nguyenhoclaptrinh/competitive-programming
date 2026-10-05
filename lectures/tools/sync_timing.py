#!/usr/bin/env python3
"""Đồng bộ timing từ segments/timing.json vào 3 nơi (nguồn sự thật duy nhất):
1. slides.manifest.tsv      -> cột duration (giữ nguyên các cột khác, kể cả type/content)
2. script.md                -> bảng mốc (cột mốc MM:SS + cột thời lượng)
3. slides.html              -> mảng slideStarts tại placeholder /*__CUES__*/[...]
Cách dùng: python3 sync_timing.py <lecture-dir>
"""
import csv, io, json, os, re, sys

def fmt_mss(sec):
    m, s = divmod(int(round(sec)), 60)
    return f"{m}:{s:02d}"

def main():
    lec = sys.argv[1] if len(sys.argv) > 1 else "."
    timing = json.load(open(os.path.join(lec, "segments", "timing.json"),
                            encoding="utf-8"))
    durations, starts = timing["durations"], timing["starts"]
    n = len(durations)

    # 1. manifest
    man = os.path.join(lec, "slides.manifest.tsv")
    rows = list(csv.DictReader(open(man, encoding="utf-8"), delimiter="\t"))
    assert len(rows) == n, f"manifest {len(rows)} dòng != {n} segments"
    if "duration" not in (rows[0].keys()):
        raise SystemExit("ERR: manifest thiếu cột duration")
    for r, d in zip(rows, durations):
        r["duration"] = f"{d:.2f}"
    with open(man, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    # 2. script.md: thay 2 cột đầu của các dòng bảng mốc "| M:SS | D.Ds |..."
    sc = os.path.join(lec, "script.md")
    lines = open(sc, encoding="utf-8").read().split("\n")
    idx = 0
    for k, ln in enumerate(lines):
        if re.match(r"^\| \d+:\d+ \| [\d.]+s", ln):
            assert idx < n, "script.md dư dòng mốc so với segments"
            lines[k] = re.sub(r"^\| \d+:\d+ \| [\d.]+s",
                              f"| {fmt_mss(starts[idx])} | {durations[idx]:.1f}s",
                              ln)
            idx += 1
    open(sc, "w", encoding="utf-8").write("\n".join(lines))
    assert idx == n, f"script.md thiếu dòng mốc ({idx}/{n})"

    # 3. slides.html cues
    html = os.path.join(lec, "slides.html")
    s = open(html, encoding="utf-8").read()
    cues = "[" + ", ".join(f"{x:.2f}" for x in starts) + "]"
    pat = r"/\*__CUES__\*/\[[^\]]*\]"
    assert len(re.findall(pat, s)) == 1, "slides.html thiếu placeholder /*__CUES__*/"
    s = re.sub(pat, "/*__CUES__*/" + cues, s)
    open(html, "w", encoding="utf-8").write(s)

    print(f"sync ok: manifest + script.md + cues = {cues}")

if __name__ == "__main__":
    main()
