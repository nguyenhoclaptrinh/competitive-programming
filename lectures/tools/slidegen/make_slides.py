#!/usr/bin/env python3
"""Sinh slides.html + slides.manifest.tsv + script.md cho mọi bài từ spec.
Cách dùng: python3 make_slides.py [slug...]  (không đối số = tất cả)
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template import build_page

import spec02, spec03, spec04, spec05, spec07, spec08, spec09, spec10, spec11, spec12

SPECS = [spec02, spec03, spec04, spec05, spec07, spec08, spec09, spec10, spec11, spec12]
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def fmt_mss(sec):
    m, s = divmod(int(round(sec)), 60)
    return f"{m}:{s:02d}"


def main():
    only = set(sys.argv[1:])
    for sp in SPECS:
        if only and sp.SLUG not in only:
            continue
        lec = os.path.join(ROOT, sp.SLUG)
        os.makedirs(os.path.join(lec, "slides"), exist_ok=True)
        secs = sp.__dict__
        slides = [secs[f"S{i}"] for i in range(1, 9)]
        html = build_page(sp.TITLE, sp.H1, slides, sp.CUSTOM_JS, 8)
        assert html.count('<section class="slide">') == 8, sp.SLUG
        assert "/*__CUES__*/" in html, sp.SLUG
        import re as _re
        assert not _re.search(r"\\(cdot|sum|frac|times|pmod|begin|end|\(|\)|\[)", html), sp.SLUG + " latex?"
        open(os.path.join(lec, "slides.html"), "w", encoding="utf-8").write(html)

        man = os.path.join(lec, "slides.manifest.tsv")
        with open(man, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, delimiter="\t")
            w.writerow(["slide", "duration", "title", "sub", "desc", "type", "content"])
            for i, row in enumerate(sp.MANIFEST, 1):
                assert len(row) == 5, (sp.SLUG, i)
                w.writerow([i, "30.00"] + list(row))

        sc = os.path.join(lec, "script.md")
        src = "ICPC-Handbook.md"
        lines = [f"# {sp.H1} — Kịch bản giảng (hình + tiếng)", "",
                 f"Nguồn: `{src}`. Slide: `slides.html` (8 slide). Audio: `audio.mp3`. Video: `video.mp4`.", "",
                 "## Cách học (hình + tiếng cùng lúc)", "",
                 "1. Mở `slides.html` trên trình duyệt. 2. Bấm Play ở thanh audio.",
                 "3. Bấm nút “Next bước” theo lời đọc. Phím N cũng chạy bước tiếp theo.", "",
                 "## Kịch bản theo mốc audio (do build đo lại từ timing.json)", "",
                 "| Mốc | Thời lượng | Lời giảng (tóm tắt) | Hình trên slide |",
                 "|---|:---:|---|---|"]
        for i, (summary, note) in enumerate(sp.SCRIPT_ROWS, 1):
            lines.append(f"| 0:00 | 30.0s | {summary} | Slide {i}: {note} |")
        open(sc, "w", encoding="utf-8").write("\n".join(lines) + "\n")
        print(f"slides ok: {sp.SLUG}")


if __name__ == "__main__":
    main()
