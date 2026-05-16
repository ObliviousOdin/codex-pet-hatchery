#!/usr/bin/env python3
"""Render the README hero animation for Ravenbyte Familiars.

The visual direction is warm industrial minimalism: precise product-grid panels,
small useful machines, restrained color, and one celebratory line of motion.
"""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageSequence

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "hero" / "ravenbyte-familiars-hero.gif"
W, H = 1200, 520
FRAMES = 36
DURATION_MS = 70

BG = "#080A0F"
PANEL = "#E8E0D0"
INK = "#111827"
MUTED = "#8D877B"
GOLD = "#D6A84F"
CYAN = "#62E6FF"
EMBER = "#FF7A45"

PETS = [
    "kageframe-rx07",
    "shuriken-byte-zero",
    "ronin-build-fox",
    "compiler-oni-mini",
    "moonbase-tanuki-dev",
    "karakuri-patch-cat",
]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
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
            continue
    return ImageFont.load_default()


FONT_HERO = font(64, True)
FONT_SUB = font(25)
FONT_LABEL = font(18, True)
FONT_MONO = font(15)


def rounded(draw: ImageDraw.ImageDraw, xy, radius: int, fill, outline=None, width: int = 1):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def load_pet_frames(slug: str) -> list[Image.Image]:
    path = ROOT / "pets" / slug / "previews" / f"{slug}-idle.gif"
    im = Image.open(path)
    frames = []
    for frame in ImageSequence.Iterator(im):
        f = frame.convert("RGBA").resize((104, 104), Image.Resampling.NEAREST)
        frames.append(f)
    return frames or [im.convert("RGBA").resize((104, 104), Image.Resampling.NEAREST)]


def draw_switch(draw: ImageDraw.ImageDraw, x: int, y: int, active: bool, label: str):
    draw.text((x, y - 24), label, font=FONT_MONO, fill=INK)
    rounded(draw, (x, y, x + 72, y + 34), 17, fill="#D8D0C0", outline=INK, width=2)
    knob_x = x + 40 if active else x + 6
    rounded(draw, (knob_x, y + 5, knob_x + 24, y + 29), 12, fill=CYAN if active else MUTED, outline=INK, width=2)


def draw_robot_arm(draw: ImageDraw.ImageDraw, t: int):
    phase = math.sin((t / FRAMES) * math.tau)
    base = (1010, 305)
    joint = (945 + int(8 * phase), 248 + int(16 * math.cos((t / FRAMES) * math.tau)))
    hand = (900 + int(10 * phase), 315 + int(7 * math.sin((t / FRAMES) * math.tau + 1.2)))
    draw.line([base, joint, hand], fill=INK, width=18, joint="curve")
    draw.line([base, joint, hand], fill=GOLD, width=7, joint="curve")
    for cx, cy, r in [(base[0], base[1], 25), (joint[0], joint[1], 20), (hand[0], hand[1], 17)]:
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=PANEL, outline=INK, width=5)
        draw.ellipse((cx - 5, cy - 5, cx + 5, cy + 5), fill=CYAN, outline=INK, width=2)
    draw.arc((hand[0] - 28, hand[1] - 22, hand[0] + 28, hand[1] + 22), 205, 335, fill=EMBER, width=5)


def draw_orbit(draw: ImageDraw.ImageDraw, cx: int, cy: int, t: int):
    for i in range(8):
        a = (t / FRAMES) * math.tau + i * math.tau / 8
        x = cx + int(math.cos(a) * 130)
        y = cy + int(math.sin(a) * 32)
        color = CYAN if i % 2 == 0 else GOLD
        draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill=color)
    draw.arc((cx - 145, cy - 42, cx + 145, cy + 42), 0, 360, fill="#C9C0AE", width=2)


def render_frame(t: int, pet_frames: dict[str, list[Image.Image]]) -> Image.Image:
    im = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(im)

    # Outer product card: almost appliance-like, exact and calm.
    rounded(draw, (38, 34, W - 38, H - 34), 38, fill=PANEL, outline="#2A2D35", width=3)
    draw.rectangle((38, 116, W - 38, 120), fill=INK)
    draw.rectangle((84, 154, 640, 158), fill=INK)
    draw.rectangle((84, 166, 445, 169), fill=GOLD)

    # Header text.
    draw.text((84, 52), "RAVENBYTE", font=FONT_LABEL, fill=INK)
    draw.text((204, 52), "FAMILIARS", font=FONT_LABEL, fill=MUTED)
    draw.text((84, 187), "Tiny useful machines", font=FONT_HERO, fill=INK)
    draw.text((88, 260), "for long coding nights", font=FONT_HERO, fill=INK)
    draw.text((91, 350), "ROBOTS OF THE WORLD: WORK, REVIEW, REJOICE.", font=FONT_SUB, fill=INK)
    draw.text((93, 389), "Codex-compatible sprite packages · pet.json · spritesheet.webp", font=FONT_MONO, fill=MUTED)

    # Command strip.
    rounded(draw, (88, 432, 675, 476), 14, fill=INK)
    draw.text((114, 445), "python scripts/install_pet.py kageframe-rx07", font=FONT_MONO, fill=CYAN)
    draw.rectangle((654 + (t % 10), 445, 657 + (t % 10), 463), fill=GOLD)

    # Right control surface.
    rounded(draw, (735, 150, 1112, 455), 28, fill="#DCD4C4", outline=INK, width=4)
    draw.text((770, 179), "FAMILIAR CONSOLE", font=FONT_LABEL, fill=INK)
    draw.text((770, 211), "GOOD DESIGN IS ANIMATABLE", font=FONT_MONO, fill=MUTED)

    draw_switch(draw, 780, 278, True, "IMPORT")
    draw_switch(draw, 875, 278, t % 18 < 9, "BUILD")
    draw_switch(draw, 970, 278, True, "JOY")

    # Animated industrial robot arm.
    draw_robot_arm(draw, t)

    # Family orbit / workbench.
    draw_orbit(draw, 930, 382, t)
    xs = [760, 832, 904, 976, 1048, 866]
    ys = [360, 404, 355, 402, 358, 323]
    for idx, slug in enumerate(PETS):
        frames = pet_frames[slug]
        pf = frames[(t + idx * 2) % len(frames)]
        scale = 72 if idx < 5 else 62
        pf = pf.resize((scale, scale), Image.Resampling.NEAREST)
        shadow_x, shadow_y = xs[idx] + 9, ys[idx] + scale + 6
        draw.ellipse((shadow_x, shadow_y, shadow_x + scale - 18, shadow_y + 8), fill="#B9B09E")
        ybob = int(math.sin((t / FRAMES) * math.tau + idx) * 5)
        im.paste(pf, (xs[idx], ys[idx] + ybob), pf)

    # Small machine LEDs.
    for i in range(18):
        x = 773 + i * 18
        y = 244
        lit = (i + t // 2) % 5 == 0
        draw.rectangle((x, y, x + 8, y + 8), fill=CYAN if lit else "#B8B0A3", outline=INK)

    # Bottom rule and edition mark.
    draw.rectangle((84, 497, 1116, 500), fill=INK)
    draw.text((986, 469), "OBLIVIOUSODIN / 01", font=FONT_MONO, fill=MUTED)
    return im


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pet_frames = {slug: load_pet_frames(slug) for slug in PETS}
    frames = [render_frame(t, pet_frames).convert("P", palette=Image.Palette.ADAPTIVE, colors=128) for t in range(FRAMES)]
    frames[0].save(
        OUT,
        save_all=True,
        append_images=frames[1:],
        duration=DURATION_MS,
        loop=0,
        optimize=True,
        disposal=2,
    )
    print(OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
