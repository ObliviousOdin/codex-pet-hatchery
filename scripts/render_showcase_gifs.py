#!/usr/bin/env python3
"""Render stitched multi-motion showcase GIFs for every familiar.

The small per-row GIFs are useful for verification, but the README needs a more
expressive preview than a single idle loop. This script stitches several states
into one polished product-card animation per familiar.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FRAME = 64
FRAMES_PER_ROW = 6
CANVAS = (360, 420)
SCALE = 3
MOTIONS = [
    ("idle", "IDLE", 2),
    ("running-right", "RUN", 2),
    ("jumping", "JUMP", 2),
    ("review", "REVIEW", 2),
    ("failed", "FAIL", 1),
    ("waving", "HELLO", 1),
]
PALETTE = {
    "bg": "#080A0F",
    "panel": "#E8E0D0",
    "ink": "#111827",
    "muted": "#7C7569",
    "gold": "#D6A84F",
    "cyan": "#62E6FF",
    "ember": "#FF7A45",
}


def font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Futura.ttc",
        "/System/Library/Fonts/Supplemental/Avenir Next.ttc",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size=size, index=1 if bold and path.endswith(".ttc") else 0)
        except Exception:
            pass
    return ImageFont.load_default()


FONT_NAME = font(20, True)
FONT_LABEL = font(15, True)
FONT_TINY = font(12)


def fit_text(text: str, max_chars: int = 29) -> str:
    return text if len(text) <= max_chars else text[: max_chars - 1].rstrip() + "…"


def rounded(draw: ImageDraw.ImageDraw, xy, r: int, fill, outline=None, width: int = 1) -> None:
    draw.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)


def load_row(sheet: Image.Image, row: int) -> list[Image.Image]:
    frames = []
    for i in range(FRAMES_PER_ROW):
        frame = sheet.crop((i * FRAME, row * FRAME, (i + 1) * FRAME, (row + 1) * FRAME))
        frames.append(frame.convert("RGBA"))
    return frames


def render_showcase(pet_dir: Path) -> Path:
    data = json.loads((pet_dir / "pet.json").read_text())
    name = data.get("displayName", pet_dir.name)
    desc = data.get("description", "")
    anim_rows = {anim["name"]: int(anim["row"]) for anim in data["animations"]}
    sheet = Image.open(pet_dir / data.get("spritesheet", "spritesheet.webp")).convert("RGBA")
    accent = data.get("showcaseAccent") or PALETTE["cyan"]

    output_frames: list[Image.Image] = []
    global_idx = 0
    for motion, label, loops in MOTIONS:
        row_frames = load_row(sheet, anim_rows[motion])
        for _ in range(loops):
            for local_idx, sprite in enumerate(row_frames):
                canvas = Image.new("RGB", CANVAS, PALETTE["bg"])
                d = ImageDraw.Draw(canvas)

                # Product-card shell: calm, precise, and GitHub-readable.
                rounded(d, (14, 14, CANVAS[0] - 14, CANVAS[1] - 14), 28, PALETTE["panel"], outline="#2A2D35", width=3)
                d.rectangle((36, 62, CANVAS[0] - 36, 65), fill=PALETTE["ink"])
                d.rectangle((36, 72, 132, 75), fill=PALETTE["gold"])
                d.text((36, 30), "RAVENBYTE FAMILIAR", font=FONT_TINY, fill=PALETTE["muted"])
                d.text((36, 88), fit_text(name, 26), font=FONT_NAME, fill=PALETTE["ink"])
                d.text((36, 116), fit_text(desc, 42), font=FONT_TINY, fill=PALETTE["muted"])

                # Stage and sprite.
                rounded(d, (56, 146, 304, 356), 22, "#111827", outline=PALETTE["ink"], width=3)
                d.ellipse((104, 324, 256, 339), fill="#05070C")
                # small motion rail behind the sprite
                rail = (global_idx * 11) % 128
                for n in range(5):
                    x = 80 + ((rail + n * 34) % 196)
                    d.rectangle((x, 164, x + 18, 167), fill=accent if n % 2 == 0 else PALETTE["gold"])
                size = FRAME * SCALE
                sprite_big = sprite.resize((size, size), Image.Resampling.NEAREST)
                bob = -8 if motion == "jumping" and local_idx in (2, 3) else 0
                if motion == "running-right":
                    bob += [0, -2, 0, 2, 0, -2][local_idx]
                canvas.paste(sprite_big, ((CANVAS[0] - size) // 2, 132 + bob), sprite_big)

                # Motion label chip.
                chip_fill = PALETTE["ember"] if motion == "failed" else accent
                rounded(d, (124, 366, 236, 392), 13, chip_fill, outline=PALETTE["ink"], width=2)
                label_w = d.textlength(label, font=FONT_LABEL)
                d.text((180 - label_w / 2, 371), label, font=FONT_LABEL, fill=PALETTE["ink"])

                # Keep full RGB frames until Pillow writes the GIF. Pre-quantizing
                # every card frame independently can make some decoders collapse
                # the showcase into a static-looking first frame, which defeats the
                # README proof requirement that this is a stitched multi-motion
                # preview rather than a one-frame card.
                output_frames.append(canvas)
                global_idx += 1

    out = pet_dir / "previews" / f"{pet_dir.name}-showcase.gif"
    ffmpeg = shutil.which("ffmpeg")
    if ffmpeg:
        with tempfile.TemporaryDirectory(prefix="ravenbyte-showcase-") as tmp:
            tmp_dir = Path(tmp)
            for idx, frame in enumerate(output_frames):
                frame.save(tmp_dir / f"frame_{idx:03d}.png")
            palette = tmp_dir / "palette.png"
            frame_pattern = str(tmp_dir / "frame_%03d.png")
            subprocess.run(
                [
                    ffmpeg,
                    "-y",
                    "-v",
                    "error",
                    "-framerate",
                    "12",
                    "-i",
                    frame_pattern,
                    "-vf",
                    "palettegen=max_colors=128",
                    str(palette),
                ],
                check=True,
            )
            subprocess.run(
                [
                    ffmpeg,
                    "-y",
                    "-v",
                    "error",
                    "-framerate",
                    "12",
                    "-i",
                    frame_pattern,
                    "-i",
                    str(palette),
                    "-lavfi",
                    "paletteuse=dither=bayer",
                    "-loop",
                    "0",
                    str(out),
                ],
                check=True,
            )
    else:
        output_frames[0].save(out, save_all=True, append_images=output_frames[1:], duration=88, loop=0, disposal=2, optimize=False)
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--pet", help="Only render one familiar slug")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    pet_dirs = [root / "pets" / args.pet] if args.pet else sorted(p for p in (root / "pets").iterdir() if p.is_dir())
    for pet_dir in pet_dirs:
        if (pet_dir / "pet.json").exists() and (pet_dir / "spritesheet.webp").exists():
            out = render_showcase(pet_dir)
            print(out.relative_to(root))


if __name__ == "__main__":
    main()
