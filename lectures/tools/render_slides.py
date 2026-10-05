#!/usr/bin/env python3
"""Render slide PNG 1280x720 từ slides.manifest.tsv (tab-separated: slide, [duration], title, sub, desc, [type], [content]).
BẮT BUỘC tiếng Việt có dấu — font DejaVuSans hỗ trợ đầy đủ.
Cách dùng: python3 render_slides.py <lecture-dir> [--vals 3,1,4,1,5,9,2,6]
  Đọc <lecture-dir>/slides.manifest.tsv, ghi <lecture-dir>/slides/slideN.png
"""
import csv, os, sys, textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720

def get_font(name, size):
    candidates = [
        f"/usr/share/fonts/truetype/dejavu/{name}.ttf",
        f"/usr/share/fonts/dejavu/{name}.ttf",
        f"/usr/share/fonts/{name}.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

F1 = get_font("DejaVuSans-Bold", 38)
F2 = get_font("DejaVuSans", 26)
F3 = get_font("DejaVuSansMono", 22)
F_CODE = get_font("DejaVuSansMono", 20)

def draw_wrapped_text(dr, pos, text, font, fill, max_width=1160, line_spacing=6):
    """Ngắt dòng theo độ rộng pixel ĐO THẬT (textlength), không ước lượng."""
    x, y = pos
    lines = []
    for para in text.split("\n"):
        cur = ""
        for w in para.split():
            # Token quá dài (code không dấu cách): chẻ theo ký tự cho vừa khung
            while dr.textlength(w, font=font) > max_width:
                k = max(1, int(len(w) * max_width / dr.textlength(w, font=font)))
                lines.append(w[:k])
                w = w[k:]
            t = (cur + " " + w).strip()
            if dr.textlength(t, font=font) <= max_width or not cur:
                cur = t
            else:
                lines.append(cur)
                cur = w
        if cur or not lines:
            lines.append(cur)
    for line in lines:
        dr.text((x, y), line, fill=fill, font=font)
        y += font.size + line_spacing
    return y

def main():
    lec = sys.argv[1] if len(sys.argv) > 1 else "."
    has_explicit_vals = False
    vals = [3, 1, 4, 1, 5, 9, 2, 6]
    for a in sys.argv[2:]:
        if a.startswith("--vals"):
            vals = [int(x) for x in a.split("=", 1)[1].split(",")]
            has_explicit_vals = True

    man = os.path.join(lec, "slides.manifest.tsv")
    out = os.path.join(lec, "slides")
    os.makedirs(out, exist_ok=True)
    rows = list(csv.DictReader(open(man, encoding="utf-8"), delimiter="\t"))
    assert rows, f"manifest rỗng: {man}"

    for r in rows:
        i = r["slide"]
        t = r["title"]
        s = r.get("sub", "")
        d = r.get("desc", "")
        stype = r.get("type", "").lower()
        content = r.get("content", "")

        im = Image.new("RGB", (W, H), (15, 23, 42))  # slate-900
        dr = ImageDraw.Draw(im)

        # Header bar
        dr.rectangle([0, 0, W, 120], fill=(2, 6, 23))  # slate-950
        dr.line([(0, 120), (W, 120)], fill=(30, 41, 59), width=2)
        dr.text((60, 36), t, fill=(125, 211, 252), font=F1)  # sky-300

        # Subtitle & Description
        cur_y = draw_wrapped_text(dr, (60, 150), s, F2, (226, 232, 240), max_width=1160)
        cur_y = draw_wrapped_text(dr, (60, cur_y + 12), d, F2, (148, 163, 184), max_width=1160)

        # Card / Graphic Area (y: 390 - 570)
        card_top = max(cur_y + 16, 380)
        card_bot = 580

        is_array_slide = (stype == "array") or (has_explicit_vals) or ("a=[" in t or "a=[" in d or "a=[" in s)

        if is_array_slide and vals:
            x0, ww = 60, 138
            for k, v in enumerate(vals[:8]):
                x = x0 + k * (ww + 8)
                dr.rectangle([x, card_top, x + ww, card_top + 130], outline=(14, 165, 233), width=2, fill=(2, 6, 23))
                dr.text((x + ww // 2, card_top + 32), f"a[{k+1}]", fill=(148, 163, 184), font=F3, anchor="mm")
                dr.text((x + ww // 2, card_top + 85), str(v), fill=(255, 255, 255), font=F1, anchor="mm")
        elif content:
            # Styled Card for formula or code content
            dr.rectangle([60, card_top, 1220, card_bot], outline=(56, 189, 248), width=2, fill=(8, 47, 73))
            draw_wrapped_text(dr, (80, card_top + 20), content, F_CODE, (241, 245, 249), max_width=1120)
        else:
            # Elegant default highlight card
            dr.rectangle([60, card_top, 1220, card_bot], outline=(30, 41, 59), width=2, fill=(2, 6, 23))
            hint = "[Meo] Mo slides.html trong trinh duyet de xem hoat hinh tung buoc!"
            dr.text((80, card_top + 45), hint, fill=(253, 224, 71), font=F3)
            dr.text((80, card_top + 95), "Tham chieu: ICPC Handbook", fill=(148, 163, 184), font=F3)

        # Footer tag
        tag = f"{os.path.basename(os.path.normpath(lec)).upper()} · SLIDE {i}/{len(rows)}"
        dr.rectangle([60, 615, 1220, 665], outline=(14, 165, 233), width=1, fill=(2, 6, 23))
        dr.text((80, 630), tag, fill=(103, 232, 249), font=F3)

        im.save(f"{out}/slide{i}.png")
    print(f"png ok: {len(rows)} slides -> {out}/")

if __name__ == "__main__":
    main()

