#!/usr/bin/env python3
"""Generate raster favicons from the site icon design."""

from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent / "static"
BRAND = (22, 101, 52, 255)  # #166534
WHITE = (255, 255, 255, 255)
INK = (22, 101, 52, 255)


def draw_icon(size: int) -> Image.Image:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    r = max(2, round(size * 0.22))

    draw.rounded_rectangle((0, 0, size - 1, size - 1), radius=r, fill=BRAND)

    pad = size * 0.19
    doc_w = size * 0.56
    doc_h = size * 0.62
    x0 = (size - doc_w) / 2
    y0 = pad
    x1 = x0 + doc_w
    y1 = y0 + doc_h

    draw.rounded_rectangle((x0, y0, x1, y1), radius=max(1, round(size * 0.05)), fill=WHITE)

    fold = size * 0.16
    fold_x = x1 - fold
    fold_y = y0
    draw.polygon(
        [
            (fold_x, fold_y),
            (x1, fold_y),
            (x1, fold_y + fold),
            (fold_x, fold_y + fold),
        ],
        fill=WHITE,
    )
    draw.polygon(
        [
            (fold_x, fold_y),
            (x1, fold_y + fold),
            (fold_x, fold_y + fold),
        ],
        fill=(230, 245, 236, 255),
    )

    line_y1 = y0 + doc_h * 0.42
    line_y2 = y0 + doc_h * 0.58
    line_x0 = x0 + doc_w * 0.18
    line_x1 = x1 - doc_w * 0.18
    stroke = max(1, round(size * 0.045))
    draw.line((line_x0, line_y1, line_x1, line_y1), fill=INK, width=stroke)
    draw.line((line_x0, line_y2, line_x1, line_y2), fill=INK, width=stroke)

    return img


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)

    img16 = draw_icon(16)
    img32 = draw_icon(32)
    img180 = draw_icon(180)

    img16.save(ROOT / "favicon-16x16.png", format="PNG", optimize=True)
    img32.save(ROOT / "favicon-32x32.png", format="PNG", optimize=True)
    img180.save(ROOT / "apple-touch-icon.png", format="PNG", optimize=True)

    img32.save(
        ROOT / "favicon.ico",
        format="ICO",
        sizes=[(16, 16), (32, 32)],
        append_images=[img16],
    )

    print("Wrote favicon.ico, favicon-16x16.png, favicon-32x32.png, apple-touch-icon.png")


if __name__ == "__main__":
    main()
