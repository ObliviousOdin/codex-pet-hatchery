#!/usr/bin/env python3
"""Deterministic Codex/Open Design familiar generator.

Generates a complete pet package:
  - generated/base.png
  - row strips for every animation
  - spritesheet.webp
  - pet.json
  - contact sheet and GIF/MP4 previews

This intentionally avoids copyrighted characters. Prompts can reference broad
mecha/ninja/anime energy, but final names and silhouettes are original.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw
from render_showcase_gifs import render_showcase

FRAME = 64
FRAMES = 6
ANIMS = [
    "idle",
    "running-right",
    "running-left",
    "waving",
    "jumping",
    "failed",
    "waiting",
    "running",
    "review",
]


@dataclass(frozen=True)
class PetSpec:
    slug: str
    display_name: str
    tagline: str
    theme: str
    primary: str
    secondary: str
    accent: str
    glow: str
    symmetric: bool = True


PRESETS: list[PetSpec] = [
    PetSpec(
        slug="kageframe-rx07",
        display_name="Kageframe RX-07",
        tagline="A chibi shadow-mecha shinobi that reviews code with a plasma scarf.",
        theme="original ninja-mecha coding companion; giant-mecha-scale courage, shinobi discipline, no copied character traits",
        primary="#17213d",
        secondary="#eef2ff",
        accent="#ffb347",
        glow="#55f0ff",
        symmetric=True,
    ),
    PetSpec(
        slug="shuriken-byte-zero",
        display_name="Shuriken Byte Zero",
        tagline="A stealthy robot courier with spinning debug shuriken drones.",
        theme="black chrome ninja robot with teal debug drones",
        primary="#101820",
        secondary="#d8e2dc",
        accent="#f77f00",
        glow="#00f5d4",
        symmetric=True,
    ),
    PetSpec(
        slug="ronin-build-fox",
        display_name="Ronin Build Fox",
        tagline="A fox-masked build guardian with tiny servo tails and CI charms.",
        theme="kitsune ronin robot, warm white mask, red cable tails",
        primary="#2d1b2f",
        secondary="#fff4e6",
        accent="#e63946",
        glow="#ffd166",
        symmetric=False,
    ),
    PetSpec(
        slug="compiler-oni-mini",
        display_name="Compiler Oni Mini",
        tagline="A tiny red oni bot that bonks failing tests with a foam kanabo.",
        theme="red oni festival robot with safe toy club and glowing lint sparks",
        primary="#3a0b16",
        secondary="#ffd6a5",
        accent="#ef476f",
        glow="#fca311",
        symmetric=True,
    ),
    PetSpec(
        slug="moonbase-tanuki-dev",
        display_name="Moonbase Tanuki Dev",
        tagline="A sleepy rover-tanuki with a leaf antenna and lunar debug pouches.",
        theme="round tanuki moon rover robot with soft green leaf antenna",
        primary="#273043",
        secondary="#f4f1de",
        accent="#7cb518",
        glow="#a9def9",
        symmetric=False,
    ),
    PetSpec(
        slug="karakuri-patch-cat",
        display_name="Karakuri Patch Cat",
        tagline="A wooden clockwork cat automaton that bats TODOs into shape.",
        theme="clockwork karakuri cat robot with brass whiskers and patchwork panels",
        primary="#5c4033",
        secondary="#f2cc8f",
        accent="#c77dff",
        glow="#ffd166",
        symmetric=False,
    ),
    PetSpec(
        slug="nebula-courier-mech",
        display_name="Nebula Courier Mech",
        tagline="A star-courier micro-mech that sprints commits through hyperspace.",
        theme="space courier mini mech with thruster boots and postal star badge",
        primary="#111827",
        secondary="#e0e7ff",
        accent="#f72585",
        glow="#4cc9f0",
        symmetric=True,
    ),
    PetSpec(
        slug="lotus-firewall-monk",
        display_name="Lotus Firewall Monk",
        tagline="A cyber-monk bot that reviews diffs behind shield-petal armor.",
        theme="calm lotus firewall monk robot with petal shield halo",
        primary="#1b4332",
        secondary="#d8f3dc",
        accent="#ffafcc",
        glow="#80ffdb",
        symmetric=True,
    ),
    PetSpec(
        slug="samurai-cache-crab",
        display_name="Samurai Cache Crab",
        tagline="A side-stepping armor crab that guards build artifacts and cache hits.",
        theme="samurai robot crab with tiny kabuto shell and cache crystal claws",
        primary="#132a13",
        secondary="#ecf39e",
        accent="#f9844a",
        glow="#90be6d",
        symmetric=True,
    ),
    PetSpec(
        slug="ramen-debug-drone",
        display_name="Ramen Debug Drone",
        tagline="A noodle-shop hover drone that serves hot fixes in a tiny bowl.",
        theme="friendly ramen shop hover robot with chopstick antenna and steam pixels",
        primary="#2b2d42",
        secondary="#fff3b0",
        accent="#e85d04",
        glow="#ffd60a",
        symmetric=False,
    ),
    PetSpec(
        slug="origami-test-heron",
        display_name="Origami Test Heron",
        tagline="A folded-paper cyber-heron that pecks flaky tests until they settle.",
        theme="origami bird robot with folded white armor and blue circuit seams",
        primary="#0f172a",
        secondary="#f8fafc",
        accent="#38bdf8",
        glow="#c084fc",
        symmetric=False,
    ),
]


def hex_to_rgba(h: str, a: int = 255) -> tuple[int, int, int, int]:
    h = h.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), a


def pix(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], fill: str | tuple[int, int, int, int]) -> None:
    draw.rectangle(xy, fill=fill)



def draw_specialized_frame(spec: PetSpec, anim: str, i: int, mirrored: bool = False) -> Image.Image | None:
    """Draw high-variation silhouettes for non-default familiars.

    The fallback mech body is intentionally reserved for Kageframe-style humanoid
    pets. Every other preset should get a materially different body plan so the
    collection does not become palette swaps.
    """
    slug = spec.slug
    if slug == "kageframe-rx07":
        return None

    img = Image.new("RGBA", (FRAME, FRAME), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    primary, secondary, accent, glow = spec.primary, spec.secondary, spec.accent, spec.glow
    outline = "#070912"
    shadow = (0, 0, 0, 55)
    bob = int(round(math.sin(i / FRAMES * math.tau) * 2))
    run = [0, 2, 1, 0, -1, -2][i % FRAMES]
    jump = -8 if i in (2, 3) else (-4 if i in (1, 4) else 0)
    y = 10 + (jump if anim == "jumping" else bob if anim in {"idle", "waiting", "review"} else 0)
    if anim == "failed":
        y += 3

    def rect(xy, fill):
        pix(d, xy, fill)

    def eye_line(cx, cy, angry=False):
        rect((cx - 8, cy, cx + 8, cy + 2), accent)
        if angry or anim == "failed":
            d.line((cx - 8, cy, cx - 3, cy + 4), fill=outline, width=1)
            d.line((cx + 8, cy, cx + 3, cy + 4), fill=outline, width=1)

    # Shared state signals.
    def draw_state_fx():
        if anim == "waiting":
            for n in range(3):
                cx = 45 + n * 5
                cy = 14 - ((i + n) % 3)
                d.ellipse((cx, cy, cx + 2, cy + 2), fill=glow)
        if anim == "review":
            d.rounded_rectangle((40, 35, 57, 47), radius=2, fill=outline)
            d.rectangle((43, 37, 54, 44), fill="#111827")
            d.line((44, 39, 52, 39), fill=glow)
            d.line((44, 42, 50, 42), fill=accent)
        if anim == "jumping":
            d.arc((18, 49, 46, 62), 205, 335, fill=hex_to_rgba(glow, 150), width=2)

    d.ellipse((15, 54, 49, 60), fill=shadow)

    if slug == "shuriken-byte-zero":
        # Hovering shuriken courier: no shared humanoid mech body, large orbiting blades.
        x = 32 + (run if anim in {"running-right", "running-left", "running"} else 0)
        spin = i % FRAMES
        tilt = -3 if anim in {"running-right", "running"} else (3 if anim == "running-left" else 0)
        if anim == "failed":
            tilt = 8
        # Oversized orbital shuriken blades carry the silhouette.
        for cx, cy, phase, scale in ((13, y + 21, spin, 1), (51, y + 31, spin + 2, 1)):
            r = 8 + (phase % 2)
            d.polygon([(cx, cy - r), (cx + 4, cy - 2), (cx, cy + 2), (cx - 4, cy - 2)], fill=outline)
            d.polygon([(cx + r, cy), (cx + 2, cy + 4), (cx - 2, cy), (cx + 2, cy - 4)], fill=outline)
            d.polygon([(cx, cy - r + 2), (cx + 2, cy - 1), (cx, cy + 1), (cx - 2, cy - 1)], fill=accent if phase % 2 else secondary)
            d.polygon([(cx + r - 2, cy), (cx + 1, cy + 2), (cx - 1, cy), (cx + 1, cy - 2)], fill=glow)
            d.arc((cx - 11, cy - 11, cx + 11, cy + 11), phase * 25, phase * 25 + 190, fill=hex_to_rgba(glow, 130), width=1)
        # Central folded-star body, deliberately diamond/wasp-like instead of bipedal.
        d.polygon([(x, y + 10 + tilt), (x + 17, y + 25), (x + 8, y + 44), (x - 12, y + 43), (x - 18, y + 25)], fill=outline)
        d.polygon([(x, y + 14 + tilt), (x + 13, y + 26), (x + 6, y + 39), (x - 9, y + 38), (x - 14, y + 26)], fill=primary)
        d.polygon([(x - 9, y + 21), (x + 11, y + 18 + tilt), (x + 7, y + 30), (x - 8, y + 32)], fill=secondary)
        # Mask/visor is a diagonal slash across the star body.
        d.polygon([(x - 7, y + 24), (x + 9, y + 21), (x + 8, y + 25), (x - 8, y + 28)], fill=accent)
        if anim == "failed":
            d.line((x - 7, y + 23, x - 1, y + 29), fill=outline, width=1)
            d.line((x - 1, y + 23, x - 7, y + 29), fill=outline, width=1)
            d.line((x + 3, y + 22, x + 9, y + 27), fill=outline, width=1)
            d.line((x + 9, y + 22, x + 3, y + 27), fill=outline, width=1)
        # Energy wake / scarf becomes the motion system instead of legs.
        wake = abs(run) + (3 if anim in {"running-right", "running-left", "running"} else 0)
        d.polygon([(x - 13, y + 36), (x - 30 - wake, y + 43), (x - 13, y + 45)], fill=hex_to_rgba(glow, 185))
        d.polygon([(x + 7, y + 40), (x + 16, y + 55 + (spin % 2)), (x - 1, y + 43)], fill=hex_to_rgba(accent, 150))
        if anim == "waving":
            d.arc((x + 14, y + 4, x + 34, y + 24), 210, 330, fill=glow, width=2)
        draw_state_fx()
    elif "fox" in slug:
        x = 31
        # Masked fox familiar with three servo tails.
        for t, off in enumerate((-12, 0, 12)):
            d.polygon([(x - 5, y + 36), (x + off, y + 19 + (i + t) % 3), (x + off + 5, y + 35)], fill=outline)
            d.polygon([(x - 3, y + 36), (x + off, y + 23 + (i + t) % 3), (x + off + 3, y + 35)], fill=accent if t == 1 else primary)
        d.ellipse((x - 15, y + 25, x + 15, y + 45), fill=outline)
        d.ellipse((x - 12, y + 27, x + 12, y + 43), fill=primary)
        d.polygon([(x - 13, y + 12), (x - 20, y + 3), (x - 7, y + 8)], fill=outline)
        d.polygon([(x + 13, y + 12), (x + 20, y + 3), (x + 7, y + 8)], fill=outline)
        d.rounded_rectangle((x - 14, y + 9, x + 14, y + 27), radius=6, fill=secondary)
        eye_line(x, y + 17)
        for lx in (x - 9 - run, x + 7 + run):
            rect((lx, y + 43, lx + 5, y + 52), primary)
        draw_state_fx()
    elif "cat" in slug:
        # Low quadruped karakuri cat: long horizontal body, tall ears,
        # curled clockwork tail, brass whiskers, and paw-skitter motion.
        x = 31 + (run if anim in {"running-right", "running-left", "running"} else 0)
        tail_swing = [0, 2, 3, 1, -1, -2][i % FRAMES]
        # Big asymmetric curled tail drives a silhouette unlike the round oni bot.
        d.arc((x + 11, y + 18 + tail_swing, x + 38, y + 47 + tail_swing), 115, 330, fill=outline, width=7)
        d.arc((x + 13, y + 20 + tail_swing, x + 35, y + 44 + tail_swing), 115, 330, fill=accent, width=3)
        d.ellipse((x + 25, y + 26 + tail_swing, x + 31, y + 32 + tail_swing), fill=glow)
        # Long wooden chassis and patchwork side panels.
        d.rounded_rectangle((x - 22, y + 27, x + 15, y + 45), radius=6, fill=outline)
        d.rounded_rectangle((x - 19, y + 29, x + 12, y + 43), radius=5, fill=primary)
        d.rectangle((x - 12, y + 31, x - 2, y + 39), fill=secondary)
        d.rectangle((x + 1, y + 32, x + 10, y + 40), fill="#8b5e34")
        d.line((x - 2, y + 31, x - 2, y + 40), fill=outline, width=1)
        d.line((x + 1, y + 32, x + 1, y + 41), fill=outline, width=1)
        # Compact head set forward with triangular ears.
        d.polygon([(x - 25, y + 26), (x - 30, y + 13), (x - 17, y + 22)], fill=outline)
        d.polygon([(x - 12, y + 25), (x - 7, y + 13), (x - 3, y + 25)], fill=outline)
        d.rounded_rectangle((x - 27, y + 22, x - 4, y + 38), radius=5, fill=outline)
        d.rounded_rectangle((x - 24, y + 24, x - 7, y + 36), radius=4, fill=secondary)
        rect((x - 20, y + 29, x - 16, y + 31), accent if anim != "failed" else "#ff3344")
        rect((x - 13, y + 29, x - 10, y + 31), glow if anim == "review" else accent)
        # Brass whiskers and key slot.
        for wy in (30, 33):
            d.line((x - 25, y + wy - 24, x - 35, y + wy - 27), fill=glow, width=1)
            d.line((x - 7, y + wy - 24, x + 2, y + wy - 27), fill=glow, width=1)
        d.ellipse((x + 4, y + 24, x + 10, y + 30), fill=accent)
        d.line((x + 10, y + 27, x + 15, y + 27), fill=accent, width=2)
        # Four small paws make a skitter rather than a biped run.
        paw_offsets = [(-17, 0), (-7, 2), (4, -1), (12, 1)]
        for n, (px, lift) in enumerate(paw_offsets):
            step = ((i + n) % 3) - 1 if anim in {"running-right", "running-left", "running"} else 0
            py = y + 44 + (lift if anim in {"running-right", "running-left", "running"} else 0)
            rect((x + px + step, py, x + px + step + 4, py + 8), outline)
            rect((x + px + step + 1, py + 1, x + px + step + 3, py + 7), secondary)
        if anim == "waving":
            d.arc((x - 34, y + 18, x - 14, y + 38), 210, 340, fill=glow, width=2)
            rect((x - 29, y + 36, x - 24, y + 42), accent)
        if anim == "failed":
            d.line((x - 20, y + 28, x - 16, y + 32), fill=outline, width=1)
            d.line((x - 16, y + 28, x - 20, y + 32), fill=outline, width=1)
            d.line((x - 13, y + 28, x - 9, y + 32), fill=outline, width=1)
            d.line((x - 9, y + 28, x - 13, y + 32), fill=outline, width=1)
            d.line((x + 18, y + 23, x + 24, y + 17), fill=accent, width=2)
        draw_state_fx()
    elif "lotus" in slug or "monk" in slug:
        # Lotus Firewall Monk: a calm shrine-bot with a tall incense-core body,
        # orbiting shield petals, and a cross-legged hover base. This avoids the
        # round biped silhouette used by oni/tanuki-style familiars.
        x = 32
        sway = [0, 1, 2, 1, 0, -1][i % FRAMES]
        petal_lift = -3 if anim == "jumping" and i in (2, 3) else 0
        if anim in {"running-right", "running-left", "running"}:
            sway += run
        # Wide lotus shield halo around the upper body.
        petals = [
            (x, y + 11 + petal_lift, 0),
            (x - 16, y + 20 + petal_lift + (i % 2), -1),
            (x + 16, y + 20 + petal_lift + ((i + 1) % 2), 1),
            (x - 24, y + 32 + petal_lift, -2),
            (x + 24, y + 32 + petal_lift, 2),
        ]
        for px, py, lean in petals:
            d.polygon([(px, py - 11), (px + 7 + lean, py + 1), (px, py + 13), (px - 7 + lean, py + 1)], fill=outline)
            d.polygon([(px, py - 8), (px + 4 + lean, py + 1), (px, py + 9), (px - 4 + lean, py + 1)], fill=accent if abs(lean) != 2 else secondary)
            d.line((px - 1, py - 5, px + lean, py + 7), fill=hex_to_rgba(glow, 190), width=1)
        # Thin vertical monk-core, deliberately not round.
        d.rounded_rectangle((x - 8 + sway, y + 20, x + 8 + sway, y + 48), radius=4, fill=outline)
        d.rounded_rectangle((x - 5 + sway, y + 23, x + 5 + sway, y + 46), radius=3, fill=primary)
        d.rectangle((x - 4 + sway, y + 27, x + 4 + sway, y + 33), fill=secondary)
        rect((x - 5 + sway, y + 31, x + 5 + sway, y + 33), glow if anim == "review" else accent)
        # Floating prayer beads / firewall nodes.
        for n, bx in enumerate((x - 14, x - 10, x + 10, x + 14)):
            by = y + 39 + ((i + n) % 2)
            d.ellipse((bx - 2, by - 2, bx + 2, by + 2), fill=outline)
            d.ellipse((bx - 1, by - 1, bx + 1, by + 1), fill=glow)
        # Lotus hover base with cross-legged shape instead of feet.
        d.polygon([(x - 22, y + 50), (x - 5, y + 43), (x + 3, y + 50)], fill=outline)
        d.polygon([(x + 22, y + 50), (x + 5, y + 43), (x - 3, y + 50)], fill=outline)
        d.polygon([(x - 18, y + 49), (x - 5, y + 45), (x + 1, y + 49)], fill=secondary)
        d.polygon([(x + 18, y + 49), (x + 5, y + 45), (x - 1, y + 49)], fill=secondary)
        d.arc((x - 22, y + 43, x + 22, y + 57), 200, 340, fill=hex_to_rgba(glow, 170), width=2)
        if anim == "waving":
            d.arc((x + 9, y + 18, x + 34, y + 38), 205, 335, fill=glow, width=2)
            d.line((x + 8, y + 31, x + 21, y + 24 - (i % 3)), fill=secondary, width=3)
        if anim == "failed":
            d.line((x - 4 + sway, y + 27, x, y + 31), fill=outline, width=1)
            d.line((x, y + 27, x - 4 + sway, y + 31), fill=outline, width=1)
            d.line((x + 1 + sway, y + 27, x + 5 + sway, y + 31), fill=outline, width=1)
            d.line((x + 5 + sway, y + 27, x + 1 + sway, y + 31), fill=outline, width=1)
            d.line((x - 18, y + 16, x - 26, y + 10), fill=accent, width=2)
            d.line((x + 18, y + 16, x + 26, y + 10), fill=accent, width=2)
        draw_state_fx()
    elif "crab" in slug:
        x = 32
        d.ellipse((x - 18, y + 24, x + 18, y + 45), fill=outline)
        d.ellipse((x - 15, y + 26, x + 15, y + 43), fill=primary)
        d.rectangle((x - 9, y + 27, x + 9, y + 35), fill=secondary)
        eye_line(x, y + 30)
        for side in (-1, 1):
            d.arc((x + side * 17 - 12, y + 16, x + side * 17 + 12, y + 40), 210 if side < 0 else -30, 80 if side < 0 else 150, fill=outline, width=4)
            d.pieslice((x + side * 28 - 7, y + 17, x + side * 28 + 7, y + 31), 25, 325, fill=accent)
            for n in range(3):
                lx = x + side * (6 + n * 6)
                d.line((lx, y + 42, lx + side * (4 + run), y + 52), fill=secondary, width=3)
        draw_state_fx()
    elif slug == "ramen-debug-drone":
        # Ramen Debug Drone: an asymmetric noodle-bowl hover familiar, not the
        # oval courier body. The bowl, steam curls, chopstick antenna, and ladle
        # arm create a distinct silhouette and motion language.
        x = 32
        bowl_y = y + 30
        steam_phase = (i % FRAMES) - 2
        tilt = 2 if anim in {"running-right", "running"} else (-2 if anim == "running-left" else 0)
        if anim == "failed":
            tilt = 5
        # Wide ramen bowl hull with heavy rim.
        d.pieslice((x - 24, bowl_y - 7 + tilt, x + 24, bowl_y + 31 + tilt), 0, 180, fill=outline)
        d.rectangle((x - 23, bowl_y + 9 + tilt, x + 23, bowl_y + 18 + tilt), fill=outline)
        d.pieslice((x - 20, bowl_y - 4 + tilt, x + 20, bowl_y + 27 + tilt), 0, 180, fill=secondary)
        d.rectangle((x - 19, bowl_y + 9 + tilt, x + 19, bowl_y + 16 + tilt), fill=primary)
        d.rectangle((x - 13, bowl_y + 4 + tilt, x + 13, bowl_y + 8 + tilt), fill=accent)
        # Noodles across the rim; failed frames spill one strand lower.
        for nx in range(-14, 15, 7):
            drop = 7 if anim == "failed" and nx > 3 else 2 + ((i + nx) % 3)
            d.line((x + nx, bowl_y + 5 + tilt, x + nx + 3, bowl_y + 5 + drop + tilt), fill="#fff3b0", width=2)
        # Tiny face panel embedded in bowl.
        if anim == "failed":
            d.line((x - 8, bowl_y + 12 + tilt, x - 3, bowl_y + 16 + tilt), fill=glow, width=2)
            d.line((x - 3, bowl_y + 12 + tilt, x - 8, bowl_y + 16 + tilt), fill=glow, width=2)
            d.line((x + 3, bowl_y + 12 + tilt, x + 8, bowl_y + 16 + tilt), fill=glow, width=2)
            d.line((x + 8, bowl_y + 12 + tilt, x + 3, bowl_y + 16 + tilt), fill=glow, width=2)
        else:
            eye_line(x, bowl_y + 12 + tilt)
        # Uneven hover pods below the bowl.
        left_pod_y = bowl_y + 20 + (run if anim in {"running-right", "running-left", "running"} else 0)
        right_pod_y = bowl_y + 18 - (run if anim in {"running-right", "running-left", "running"} else 0)
        d.ellipse((x - 24, left_pod_y, x - 11, left_pod_y + 8), fill=outline)
        d.ellipse((x + 12, right_pod_y, x + 25, right_pod_y + 8), fill=outline)
        d.arc((x - 26, left_pod_y - 3, x - 9, left_pod_y + 11), i * 45, i * 45 + 220, fill=glow, width=2)
        d.arc((x + 10, right_pod_y - 3, x + 27, right_pod_y + 11), 180 + i * 45, 400 + i * 45, fill=glow, width=2)
        # Asymmetric chopstick antenna and serving ladle arm.
        d.line((x + 10, bowl_y - 6 + tilt, x + 22, bowl_y - 25 + steam_phase), fill=outline, width=4)
        d.line((x + 12, bowl_y - 6 + tilt, x + 24, bowl_y - 24 + steam_phase), fill=accent, width=2)
        ladle_lift = -9 if anim == "waving" and i in (1, 2, 3) else 0
        d.line((x - 18, bowl_y + 2 + tilt, x - 33, bowl_y - 9 + ladle_lift), fill=outline, width=4)
        d.ellipse((x - 39, bowl_y - 14 + ladle_lift, x - 30, bowl_y - 5 + ladle_lift), fill=accent)
        # Steam curls are the signature waiting/review/readability cue.
        for sx, phase in ((x - 10, 0), (x, 2), (x + 8, 4)):
            top = bowl_y - 19 - ((i + phase) % 4)
            d.arc((sx - 5, top, sx + 5, top + 14), 90, 265, fill=hex_to_rgba(glow, 170), width=2)
        if anim == "review":
            d.rounded_rectangle((42, 20, 59, 32), radius=2, fill=outline)
            d.rectangle((45, 22, 56, 29), fill="#1b263b")
            d.line((46, 24, 54, 24), fill=glow)
            d.line((46, 27, 52, 27), fill=accent)
        if anim == "jumping":
            d.arc((18, 51, 47, 63), 205, 335, fill=hex_to_rgba(glow, 150), width=2)
        draw_state_fx()
    elif "drone" in slug or "courier" in slug or "nebula" in slug:
        x = 32
        d.ellipse((x - 19, y + 24, x + 19, y + 43), fill=outline)
        d.ellipse((x - 15, y + 26, x + 15, y + 41), fill=primary)
        d.rectangle((x - 9, y + 30, x + 9, y + 34), fill=secondary)
        eye_line(x, y + 31)
        for px in (x - 25, x + 25):
            d.ellipse((px - 7, y + 25, px + 7, y + 39), outline)
            d.arc((px - 10, y + 21, px + 10, y + 43), i * 35, i * 35 + 220, fill=glow, width=2)
        d.polygon([(x - 7, y + 42), (x, y + 54 + abs(run)), (x + 7, y + 42)], fill=hex_to_rgba(accent, 210))
        draw_state_fx()
    elif "heron" in slug:
        # Origami Test Heron: a tall folded-paper wading bird with a long
        # angular neck, direction-specific beak, crane legs, and wing panels.
        # The silhouette is intentionally vertical/avian rather than bot/hover.
        facing = -1 if anim == "running-left" else 1
        x = 31 + (facing * run if anim in {"running-right", "running-left", "running"} else 0)
        peck = 4 if anim in {"running-right", "running-left", "running"} and i in (1, 4) else 0
        neck_bob = -2 if anim == "review" and i % 2 else 0
        if anim == "failed":
            peck = 7
            neck_bob = 4
        # Folded tail and angular paper body.
        tail = [(x - facing * 10, y + 34), (x - facing * 27, y + 26 + (i % 2)), (x - facing * 13, y + 44)]
        body_outer = [(x - 14, y + 23), (x + 6, y + 16), (x + 18, y + 34), (x - 5, y + 46), (x - 18, y + 37)]
        body_inner = [(x - 10, y + 25), (x + 5, y + 19), (x + 14, y + 33), (x - 4, y + 42), (x - 14, y + 36)]
        d.polygon(tail, fill=outline)
        d.polygon([(px + facing * 2, py + 1) for px, py in tail], fill=hex_to_rgba(accent, 175))
        d.polygon(body_outer, fill=outline)
        d.polygon(body_inner, fill=secondary)
        # Faceted wing panel changes shape by state so rows read differently.
        wing_lift = -8 if anim in {"waving", "jumping"} and i in (1, 2, 3) else (3 if anim == "failed" else 0)
        d.polygon([(x - 11, y + 28), (x + 8, y + 22 + wing_lift), (x + 5, y + 38), (x - 13, y + 41)], fill=primary)
        d.line((x - 9, y + 30, x + 5, y + 24 + wing_lift), fill=glow, width=1)
        d.line((x - 8, y + 35, x + 4, y + 37), fill=accent, width=1)
        # Long folded neck and triangular beak face the active run direction.
        neck = [(x + facing * 6, y + 21), (x + facing * 13, y + 10 + neck_bob), (x + facing * 18, y + 13 + neck_bob), (x + facing * 11, y + 25)]
        d.polygon(neck, fill=outline)
        d.polygon([(x + facing * 8, y + 21), (x + facing * 14, y + 13 + neck_bob), (x + facing * 16, y + 15 + neck_bob), (x + facing * 10, y + 24)], fill=secondary)
        head = (x + facing * 18, y + 9 + neck_bob)
        d.polygon([(head[0] - facing * 2, head[1] + 1), (head[0] + facing * (8 + peck), head[1] + 4), (head[0] - facing * 1, head[1] + 8)], fill=outline)
        d.polygon([(head[0], head[1] + 3), (head[0] + facing * (7 + peck), head[1] + 4), (head[0], head[1] + 6)], fill=accent)
        rect((head[0] - 1 if facing > 0 else head[0] - 3, head[1] + 3, head[0] + 1 if facing > 0 else head[0] - 1, head[1] + 5), glow if anim != "failed" else "#ff3344")
        # Crane legs: alternating high-knee steps; failed state buckles.
        step_a = [0, -3, -1, 0, 3, 1][i % FRAMES] if anim in {"running-right", "running-left", "running"} else 0
        step_b = -step_a
        if anim == "failed":
            step_a, step_b = 4, -1
        for lx, step, knee in ((x - 6, step_a, -5), (x + 6, step_b, 4)):
            d.line((lx, y + 43, lx + facing * step, y + 51), fill=outline, width=4)
            d.line((lx + facing * step, y + 51, lx + facing * (step + knee), y + 56), fill=outline, width=3)
            d.line((lx, y + 43, lx + facing * step, y + 51), fill=primary, width=2)
            d.line((lx + facing * step, y + 51, lx + facing * (step + knee), y + 56), fill=glow, width=1)
        if anim == "waiting":
            d.line((x - 18, y + 18, x - 25, y + 14 - (i % 3)), fill=glow, width=1)
            d.line((x - 25, y + 14 - (i % 3), x - 30, y + 19), fill=accent, width=1)
        if anim == "review":
            d.rounded_rectangle((7, 34, 25, 46), radius=2, fill=outline)
            d.rectangle((10, 36, 22, 43), fill="#1b263b")
            d.line((11, 38, 20, 38), fill=glow)
            d.line((11, 41, 18, 41), fill=accent)
        draw_state_fx()
    elif slug.startswith("ravenbyte-"):
        # Surge familiars: deterministic, hash-varied glyph machines designed for
        # high-count hatching without palette-swap silhouettes. Each slug changes
        # body plan, pose anchors, appendages, and orbiting props so validation can
        # compare hundreds of packages mechanically.
        seed = int(hashlib.sha256(slug.encode()).hexdigest()[:16], 16)
        archetype = seed % 16
        # Respect the generated form suffix for future hatches so a queued
        # "mushroom" cannot accidentally render as a wheel/crystal-like body
        # solely because of hash collision. Existing packages remain untouched.
        form_archetypes = {
            "beetle": 0,
            "lantern": 1,
            "crawler": 2,
            "kite": 3,
            "totem": 4,
            "serpent": 5,
            "crystal": 6,
            "wheel": 7,
            "mushroom": 8,
            "mask": 9,
            "train": 10,
            "manta": 11,
            "book": 12,
            "key": 13,
            "jelly": 14,
            "rabbit": 15,
        }
        for suffix, forced_archetype in form_archetypes.items():
            if slug.endswith(f"-{suffix}"):
                archetype = forced_archetype
                break
        x = 20 + ((seed >> 4) % 25)
        yy = y + ((seed >> 9) % 7) - 3
        facing = -1 if (anim == "running-left" or (seed >> 2) & 1) else 1
        if anim == "running-right":
            facing = 1
        if anim == "running-left":
            facing = -1
        sway = [0, 2, 1, 0, -1, -2][i % FRAMES]
        pulse = 1 + ((seed >> (i % 8)) & 1)
        tilt = -3 if anim in {"running-right", "running"} else (3 if anim == "running-left" else 0)
        if anim == "failed":
            yy += 4
            tilt = 6
        # Hash-specific satellite glyphs occupy different coordinates, lowering
        # silhouette overlap while giving every familiar a signature read.
        if archetype == 2:
            # Crawler-class familiars get a low, bridge-like trail instead of
            # generic orbiting glyphs. This keeps their base silhouette from
            # overlapping tall mask/imp familiars while preserving a signature
            # dependency-path read.
            for n in range(5):
                ox = x - 25 + n * 12 + ((seed >> (n + 7)) % 3)
                oy = yy + 54 + ((i + n) % 2)
                d.rounded_rectangle((ox - 4, oy - 2, ox + 4, oy + 2), radius=2, fill=outline)
                d.rectangle((ox - 2, oy - 1, ox + 2, oy + 1), fill=glow if n % 2 else accent)
        else:
            for n in range(3 + (seed % 3)):
                ox = 6 + ((seed >> (n * 5 + 3)) % 52)
                oy = 8 + ((seed >> (n * 5 + 11)) % 42)
                r = 2 + ((seed >> (n * 3 + 19)) % 4)
                if anim in {"waiting", "review"}:
                    oy -= (i + n) % 3
                d.ellipse((ox - r - 1, oy - r - 1, ox + r + 1, oy + r + 1), fill=outline)
                d.ellipse((ox - r, oy - r, ox + r, oy + r), fill=glow if n % 2 else accent)
        if archetype == 0:  # antenna beetle slab
            w, h = 13 + (seed % 8), 18 + ((seed >> 5) % 8)
            d.rounded_rectangle((x - w, yy + 20, x + w, yy + 20 + h), radius=4, fill=outline)
            d.rounded_rectangle((x - w + 3, yy + 23, x + w - 3, yy + 18 + h), radius=3, fill=primary)
            for side in (-1, 1):
                d.line((x + side * w, yy + 30, x + side * (w + 7 + pulse), yy + 24 + sway), fill=accent, width=3)
                d.line((x + side * (w - 2), yy + 40, x + side * (w + 9), yy + 48 - sway), fill=secondary, width=3)
            d.arc((x - 20, yy + 5, x, yy + 28), 210, 330, fill=glow, width=2)
            d.arc((x, yy + 5, x + 20, yy + 28), 210, 330, fill=glow, width=2)
        elif archetype == 1:  # floating lantern stack
            for k in range(3):
                yy2 = yy + 10 + k * (10 + (seed % 3))
                d.polygon([(x, yy2 - 6), (x + 12 + k, yy2), (x + 8, yy2 + 8), (x - 8, yy2 + 8), (x - 12 - k, yy2)], fill=outline)
                d.polygon([(x, yy2 - 3), (x + 8 + k, yy2 + 1), (x + 5, yy2 + 6), (x - 5, yy2 + 6), (x - 8 - k, yy2 + 1)], fill=[primary, secondary, accent][k % 3])
            d.line((x, yy + 5, x + facing * (17 + pulse), yy + 2 + sway), fill=glow, width=2)
        elif archetype == 2:  # crawler bridge
            # Long, low dependency bridge with separated legs and antenna masts.
            # The flattened footprint deliberately differs from the tall split
            # masks in the generated queue while still animating like a crawler.
            stride = [0, 2, 4, 2, 0, -2][i % FRAMES] if anim in {"running-right", "running-left", "running"} else sway
            deck_y = yy + 36 + (1 if anim == "failed" else 0)
            nose = x + facing * (28 + pulse)
            tail = x - facing * 27
            d.rounded_rectangle((x - 28, deck_y - 5, x + 25, deck_y + 8), radius=5, fill=outline)
            d.rounded_rectangle((x - 24, deck_y - 2, x + 20, deck_y + 5), radius=3, fill=primary)
            d.polygon([(nose, deck_y - 3), (nose + facing * 8, deck_y + 3), (nose, deck_y + 9)], fill=outline)
            d.polygon([(tail, deck_y - 1), (tail - facing * 9, deck_y + 5), (tail, deck_y + 10)], fill=accent)
            for n in range(6):
                lx = x - 23 + n * 9
                foot = lx + (-3 if n % 2 else 4) + stride
                d.line((lx, deck_y + 7, foot, yy + 54 - (n % 2)), fill=secondary, width=3)
                d.rectangle((foot - 3, yy + 53 - (n % 2), foot + 4, yy + 56 - (n % 2)), fill=outline)
            for n in range(3):
                mx = x - 16 + n * 15
                d.line((mx, deck_y - 4, mx + facing * (3 + n), deck_y - 16 - pulse + n), fill=glow, width=2)
                d.ellipse((mx + facing * (2 + n) - 2, deck_y - 18 - pulse + n, mx + facing * (2 + n) + 2, deck_y - 14 - pulse + n), fill=accent if n == 1 else glow)
        elif archetype == 3:  # crescent kite
            # Slender asymmetric glider: use separated wing/tail points instead
            # of a filled oval so kite familiars do not collapse into mask-like
            # silhouettes in large collection validation.
            wing = 24 + (seed % 5)
            nose = yy + 13 + tilt
            mid = yy + 30 + sway // 2
            tail = yy + 50 - sway
            outer = [
                (x - facing * 8, mid - 2),
                (x + facing * wing, nose),
                (x + facing * (wing - 5), mid + 8),
                (x + facing * 7, tail),
                (x - facing * 13, mid + 6),
            ]
            inner = [
                (x - facing * 3, mid),
                (x + facing * (wing - 8), nose + 5),
                (x + facing * (wing - 10), mid + 6),
                (x + facing * 5, tail - 6),
                (x - facing * 8, mid + 5),
            ]
            d.polygon(outer, fill=outline)
            d.polygon(inner, fill=primary)
            d.line((x - facing * 14, mid + 8, x - facing * (25 + pulse), yy + 56 - sway), fill=accent, width=3)
            d.line((x + facing * 3, mid + 2, x + facing * (wing + 8), mid - 5 - pulse), fill=glow, width=2)
            d.polygon([(x + facing * 3, mid - 6), (x + facing * (18 + pulse), mid), (x + facing * 2, mid + 9)], fill=secondary)
        elif archetype == 4:  # tall shrine totem
            # Totems are intentionally asymmetric: a side pennant, directional
            # review mast, and run-step offset keep left/right rows from being
            # accidental mirrors or identical static pillars.
            w = 8 + (seed % 6)
            run_step = [0, 2, 4, 2, 0, -2][i % FRAMES] if anim in {"running-right", "running-left", "running"} else 0
            x += facing * run_step
            pennant = 8 + pulse
            d.rounded_rectangle((x - w, yy + 6 + abs(run_step) // 2, x + w, yy + 49), radius=3, fill=outline)
            d.rectangle((x - w + 3, yy + 10 + abs(run_step) // 2, x + w - 3, yy + 45), fill=primary)
            for k in range(4):
                yk = yy + 14 + k * 8 + (sway if k == 0 and anim in {"waving", "waiting"} else 0)
                d.line((x - w - 6 + (k % 2), yk, x + w + 6 - (k % 2), yk), fill=[secondary, accent, glow][k % 3], width=2)
            d.polygon([(x, yy), (x + 14, yy + 9), (x - 14, yy + 9)], fill=accent)
            d.line((x + facing * (w + 2), yy + 13, x + facing * (w + 2), yy + 32), fill=outline, width=2)
            d.polygon([(x + facing * (w + 3), yy + 14), (x + facing * (w + 3 + pennant), yy + 18 + sway), (x + facing * (w + 3), yy + 23)], fill=secondary)
            d.line((x - facing * (w + 2), yy + 39, x - facing * (w + 10 + pulse), yy + 47 - sway), fill=glow, width=2)
        elif archetype == 5:  # serpent ribbon
            pts = []
            for k in range(6):
                pts.append((x - 20 + k * 8, yy + 28 + int(math.sin((i + k) / 2) * (5 + seed % 4))))
            d.line(pts, fill=outline, width=9)
            d.line(pts, fill=primary, width=5)
            hx, hy = pts[-1]
            d.polygon([(hx, hy - 6), (hx + facing * 12, hy), (hx, hy + 6)], fill=secondary)
        elif archetype == 6:  # crystal tripod
            # Faceted tripod with state-specific motion: running scuttles on
            # three legs, waiting/review pulses orbit shards, and failed shows
            # animated crack/spark frames instead of freezing as a static gem.
            step = [0, 3, 1, -1, -3, 1][i % FRAMES] if anim in {"running-right", "running-left", "running"} else sway
            lean = facing * (2 if anim in {"running-right", "running"} else (-2 if anim == "running-left" else 0))
            if anim == "jumping":
                lean = [0, 1, 2, 0, -1, -2][i % FRAMES]
            top = (x + lean, yy + 5)
            right = (x + 15 + lean, yy + 25)
            lower_right = (x + 7 + step // 2, yy + 45)
            lower_left = (x - 10 + step // 3, yy + 43)
            left = (x - 16 + lean, yy + 24)
            d.polygon([top, right, lower_right, lower_left, left], fill=outline)
            d.polygon(
                [
                    (top[0], top[1] + 4),
                    (x + 10 + lean, yy + 26),
                    (x + 5 + step // 2, yy + 40),
                    (x - 7 + step // 3, yy + 38),
                    (x - 11 + lean, yy + 25),
                ],
                fill=secondary,
            )
            d.line((top[0], top[1] + 5, x - 2 + step // 2, yy + 39), fill=glow, width=2)
            d.line((x - 10 + lean, yy + 25, x + 9 + lean, yy + 26), fill=primary, width=2)
            leg_phase = [0, 3, 1, -1, -3, 1][i % FRAMES]
            for idx, lx in enumerate((-12, 0, 12)):
                foot = x + lx + (leg_phase if idx != 1 else -leg_phase // 2)
                d.line((x + lx // 2, yy + 42, foot, yy + 55 - (idx % 2)), fill=outline, width=4)
                d.line((x + lx // 2, yy + 42, foot, yy + 55 - (idx % 2)), fill=accent, width=2)
            if anim == "failed":
                crack = [(x - 2, yy + 12), (x + 3 + (i % 2), yy + 20), (x - 1, yy + 28), (x + 5, yy + 36)]
                d.line(crack, fill=outline, width=2)
                spark_x = x + [-18, 17, -14, 14, -10, 12][i % FRAMES]
                spark_y = yy + [15, 19, 23, 17, 27, 21][i % FRAMES]
                d.line((spark_x - 3, spark_y, spark_x + 3, spark_y), fill=glow, width=2)
                d.line((spark_x, spark_y - 3, spark_x, spark_y + 3), fill=glow, width=2)
            elif anim in {"waiting", "review"}:
                shard_x = x + facing * (18 + (i % 3))
                shard_y = yy + 11 + ((i + seed) % 4)
                d.polygon([(shard_x, shard_y - 4), (shard_x + 4, shard_y), (shard_x, shard_y + 4), (shard_x - 4, shard_y)], fill=glow)
        elif archetype == 7:  # wheel drone
            if slug == "ravenbyte-264-harbor-audit-wheel":
                # Harbor Audit Wheel: make this wheel-class familiar read as a
                # dockside winch buoy, not another crystal/tripod silhouette.
                # The low offset tire, high crane mast, dangling audit hook, and
                # side fenders materially reduce overlap with prior crystal pets.
                roll = [0, 2, 5, 2, 0, -2][i % FRAMES] if anim in {"running-right", "running-left", "running"} else sway
                hub_x = max(20, min(44, x - 8 + facing * (roll // 2)))
                hub_y = yy + 39 + (2 if anim == "failed" else 0)
                r = 13
                mast_x = hub_x + facing * (15 + pulse)
                mast_top = yy + 5 + (sway if anim in {"waiting", "review"} else 0)
                # Pier skid / shadow.
                d.rounded_rectangle((hub_x - 27, yy + 54, hub_x + 29, yy + 59), radius=2, fill=outline)
                d.rectangle((hub_x - 22, yy + 55, hub_x + 24, yy + 57), fill=accent)
                # Offset tire body.
                d.ellipse((hub_x - r - 2, hub_y - r - 2, hub_x + r + 2, hub_y + r + 2), fill=outline)
                d.ellipse((hub_x - r + 2, hub_y - r + 2, hub_x + r - 2, hub_y + r - 2), fill=primary)
                d.ellipse((hub_x - 5, hub_y - 5, hub_x + 5, hub_y + 5), fill=secondary)
                for a in range(0, 360, 90):
                    ang = math.radians(a + i * 28 + (0 if facing == 1 else 12))
                    d.line((hub_x, hub_y, hub_x + int(math.cos(ang) * (r - 2)), hub_y + int(math.sin(ang) * (r - 2))), fill=glow, width=2)
                # Tall asymmetric harbor crane mast and audit hook.
                d.line((hub_x + facing * 8, hub_y - 7, mast_x, mast_top), fill=outline, width=5)
                d.line((hub_x + facing * 8, hub_y - 7, mast_x, mast_top), fill=secondary, width=3)
                boom_end = mast_x - facing * (22 + pulse)
                boom_y = mast_top + 5 + (sway // 2)
                d.line((mast_x, mast_top, boom_end, boom_y), fill=outline, width=4)
                d.line((mast_x, mast_top, boom_end, boom_y), fill=glow, width=2)
                hook_y = yy + 24 + (i % 3 if anim in {"waiting", "review"} else 0)
                d.line((boom_end, boom_y, boom_end, hook_y), fill=outline, width=2)
                d.arc((boom_end - 6, hook_y - 1, boom_end + 6, hook_y + 11), 20, 300, fill=accent, width=3)
                # Harbor fenders / audit pennants create a broad, non-crystal read.
                for n in range(3):
                    fx = hub_x - 25 + n * 12 + (roll if n == 2 and anim in {"running-right", "running-left", "running"} else 0)
                    fy = yy + 43 + ((i + n) % 2)
                    d.rounded_rectangle((fx - 4, fy - 7, fx + 4, fy + 7), radius=3, fill=outline)
                    d.rectangle((fx - 2, fy - 5, fx + 2, fy + 5), fill=glow if n % 2 else accent)
                if anim == "waving":
                    d.line((mast_x, yy + 18, mast_x + facing * (13 + pulse), yy + 10 + sway), fill=accent, width=3)
                    d.polygon([(mast_x + facing * 13, yy + 9 + sway), (mast_x + facing * 24, yy + 14 + sway), (mast_x + facing * 13, yy + 19 + sway)], fill=glow)
                if anim == "review":
                    d.rectangle((boom_end - 5, hook_y + 12, boom_end + 13, hook_y + 20), fill=outline)
                    d.rectangle((boom_end - 3, hook_y + 14, boom_end + 11, hook_y + 18), fill=primary)
                    d.line((boom_end + 12, hook_y + 14, boom_end + 24, hook_y + 8 + sway), fill=glow, width=2)
            else:
                r = 15 + (seed % 5)
                d.ellipse((x - r, yy + 20 - r, x + r, yy + 20 + r), fill=outline)
                d.ellipse((x - r + 4, yy + 24 - r, x + r - 4, yy + 16 + r), fill=primary)
                for a in range(0, 360, 60):
                    ang = math.radians(a + i * 18)
                    d.line((x, yy + 20, x + int(math.cos(ang) * r), yy + 20 + int(math.sin(ang) * r)), fill=glow, width=2)
                d.line((x + facing * r, yy + 20, x + facing * (r + 12), yy + 12 + sway), fill=accent, width=3)
        elif archetype == 8:  # mushroom relay
            # Broad cap + offset sprout dish keeps mushroom familiars visually
            # distinct from crystal/totem silhouettes in large generated sets.
            capw = 21 + (seed % 6)
            caph = 20 + ((seed >> 6) % 5)
            cap_y = yy + 11 + (sway // 2)
            d.pieslice((x - capw, cap_y, x + capw, cap_y + caph), 180, 360, fill=outline)
            d.rectangle((x - capw + 1, cap_y + caph // 2, x + capw - 1, cap_y + caph // 2 + 5), fill=outline)
            d.pieslice((x - capw + 4, cap_y + 4, x + capw - 4, cap_y + caph - 1), 180, 360, fill=accent)
            d.rectangle((x - capw + 5, cap_y + caph // 2, x + capw - 5, cap_y + caph // 2 + 3), fill=accent)
            d.rounded_rectangle((x - 7, yy + 30, x + 6, yy + 48), radius=5, fill=outline)
            d.rounded_rectangle((x - 4, yy + 32, x + 3, yy + 46), radius=3, fill=secondary)
            for sx, sy, rr in ((x - capw + 9, cap_y + 13, 3), (x - 3, cap_y + 9, 2), (x + capw - 11, cap_y + 14, 3)):
                d.ellipse((sx - rr, sy - rr, sx + rr, sy + rr), fill=glow)
            d.line((x - 13, yy + 45, x - 24 - pulse, yy + 53), fill=primary, width=3)
            d.line((x + 11, yy + 45, x + 24 + pulse, yy + 52), fill=primary, width=3)
            d.line((x + facing * (capw - 5), cap_y + 8, x + facing * (capw + 8), cap_y + 1 + sway), fill=glow, width=2)
        elif archetype == 9:  # split mask imp
            if slug == "ravenbyte-282-zephyr-widget-mask":
                # Zephyr Widget Mask: break away from an older key-guardian
                # silhouette. Render it as a wide floating dashboard mask with
                # offset widget pods and wind-vane whiskers rather than a tall
                # key-like body, keeping the familiar visibly original while
                # preserving its mask/widget theme.
                step = [0, 3, 5, 2, -1, -3][i % FRAMES] if anim in {"running-right", "running-left", "running"} else 0
                cx = max(24, min(40, x + facing * step))
                dash_y = yy + 31 + (2 if anim == "failed" else 0)
                blink = [0, 1, 2, 1, 0, -1][i % FRAMES]
                # A shallow dashboard face makes the body plan wide and low.
                d.rounded_rectangle((cx - 28, dash_y - 10, cx + 26, dash_y + 10), radius=9, fill=outline)
                d.rounded_rectangle((cx - 24, dash_y - 7, cx + 22, dash_y + 7), radius=6, fill=primary)
                d.polygon([(cx - 22, dash_y - 7), (cx - 3, dash_y - 12 + blink), (cx + 20, dash_y - 5), (cx + 12, dash_y + 4), (cx - 18, dash_y + 3)], fill=secondary)
                d.rectangle((cx - 18, dash_y - 2 + blink, cx + 14, dash_y + 1 + blink), fill=glow)
                # Floating widget pods and connecting telemetry lines are the
                # signature prop and reduce overlap with key/mask silhouettes.
                pods = [
                    (cx - 30, yy + 17 + sway, 4),
                    (cx - 12, yy + 8 - pulse, 3),
                    (cx + 14, yy + 11 + blink, 4),
                    (cx + 31, yy + 24 - sway, 3),
                ]
                for a, b in zip(pods, pods[1:]):
                    d.line((a[0], a[1], b[0], b[1]), fill=outline, width=3)
                    d.line((a[0], a[1], b[0], b[1]), fill=glow, width=1)
                for n, (px, py, rr) in enumerate(pods):
                    d.rounded_rectangle((px - rr - 2, py - rr - 2, px + rr + 2, py + rr + 2), radius=3, fill=outline)
                    d.rectangle((px - rr, py - rr, px + rr, py + rr), fill=accent if n % 2 else glow)
                # Wind-vane whiskers and low skids keep the bottom silhouette
                # different from dangling tassel masks.
                for side in (-1, 1):
                    d.line((cx + side * 19, dash_y + 5, cx + side * (33 + pulse), yy + 46 - side * sway), fill=outline, width=3)
                    d.line((cx + side * 19, dash_y + 5, cx + side * (33 + pulse), yy + 46 - side * sway), fill=accent if side < 0 else glow, width=1)
                for n, lx in enumerate((cx - 20, cx + 2, cx + 22)):
                    foot = lx + [-5, 2, 5][n] + (step if n == 2 else -step // 2)
                    d.line((lx, dash_y + 8, foot, yy + 55 - (n % 2)), fill=outline, width=3)
                    d.line((lx, dash_y + 8, foot, yy + 55 - (n % 2)), fill=secondary, width=1)
                    d.rectangle((foot - 5, yy + 54 - (n % 2), foot + 5, yy + 58 - (n % 2)), fill=outline)
                if anim == "waving":
                    wx = cx - facing * 25
                    d.line((wx, dash_y - 5, wx - facing * (13 + pulse), yy + 13 + sway), fill=outline, width=4)
                    d.line((wx, dash_y - 5, wx - facing * (13 + pulse), yy + 13 + sway), fill=glow, width=2)
                    d.polygon([(wx - facing * 13, yy + 11 + sway), (wx - facing * 23, yy + 17 + sway), (wx - facing * 13, yy + 22 + sway)], fill=accent)
                if anim == "review":
                    scan_x = cx + facing * 30
                    d.rectangle((scan_x - 6, dash_y + 12, scan_x + 13, dash_y + 22), fill=outline)
                    d.rectangle((scan_x - 3, dash_y + 14, scan_x + 10, dash_y + 19), fill=primary)
                    d.line((scan_x + 12, dash_y + 15, scan_x + 23, dash_y + 9 + sway), fill=glow, width=2)
                if anim == "failed":
                    d.line((cx - 26, yy + 19, cx - 35, yy + 10), fill=accent, width=2)
                    d.line((cx + 24, yy + 16, cx + 35, yy + 8), fill=accent, width=2)
            elif slug == "ravenbyte-266-jade-graph-mask":
                # Jade Graph Mask: break away from the default tall imp-mask
                # silhouette. This familiar is a low, side-mounted graph visor
                # riding on three data-node legs with a tall asymmetric antenna,
                # so it does not read as a palette/costume swap of earlier masks.
                step = [0, 2, 4, 2, 0, -2][i % FRAMES] if anim in {"running-right", "running-left", "running"} else 0
                cx = max(22, min(42, x + facing * step))
                base_y = yy + 34 + (2 if anim == "failed" else 0)
                brow = [0, -1, -2, -1, 1, 2][i % FRAMES]
                # Offset crescent visor body, intentionally wide and shallow.
                d.rounded_rectangle((cx - 25, base_y - 10, cx + 20, base_y + 9), radius=8, fill=outline)
                d.rounded_rectangle((cx - 21, base_y - 7, cx + 16, base_y + 6), radius=6, fill=primary)
                d.polygon([(cx - 20, base_y - 7), (cx - 3, base_y - 13 + brow), (cx + 15, base_y - 6), (cx + 5, base_y + 1), (cx - 14, base_y + 2)], fill=secondary)
                d.rectangle((cx - 17, base_y - 2 + brow, cx + 11, base_y + 1 + brow), fill=glow)
                # Graph nodes and connecting edges are the signature prop.
                nodes = [
                    (cx - 25, yy + 17 + sway),
                    (cx - 8, yy + 10 - pulse),
                    (cx + 12, yy + 17 - sway),
                    (cx + 25, yy + 27 + pulse),
                ]
                for a, b in zip(nodes, nodes[1:]):
                    d.line((a[0], a[1], b[0], b[1]), fill=outline, width=4)
                    d.line((a[0], a[1], b[0], b[1]), fill=glow, width=2)
                for n, (nx, ny) in enumerate(nodes):
                    r = 4 if n in (1, 3) else 3
                    d.ellipse((nx - r - 1, ny - r - 1, nx + r + 1, ny + r + 1), fill=outline)
                    d.ellipse((nx - r, ny - r, nx + r, ny + r), fill=accent if n % 2 else glow)
                # Tripod data legs keep the bottom silhouette unlike a hanging tassel mask.
                for n, lx in enumerate((cx - 17, cx, cx + 16)):
                    foot = lx + [-4, 2, 5][n] + (step if n == 2 else -step // 2)
                    d.line((lx, base_y + 7, foot, yy + 55 - (n % 2)), fill=outline, width=4)
                    d.line((lx, base_y + 7, foot, yy + 55 - (n % 2)), fill=secondary if n == 1 else accent, width=2)
                    d.rectangle((foot - 4, yy + 54 - (n % 2), foot + 4, yy + 58 - (n % 2)), fill=outline)
                # State-specific motions read clearly in the stitched showcase.
                if anim == "waving":
                    wx = cx + facing * 21
                    d.line((wx, base_y - 2, wx + facing * (13 + pulse), yy + 14 + sway), fill=outline, width=4)
                    d.line((wx, base_y - 2, wx + facing * (13 + pulse), yy + 14 + sway), fill=accent, width=2)
                    d.ellipse((wx + facing * 13 - 3, yy + 11 + sway, wx + facing * 13 + 3, yy + 17 + sway), fill=glow)
                if anim == "review":
                    tx0, tx1 = cx + facing * 18 - 2, cx + facing * 34 + 2
                    sx0, sx1 = cx + facing * 20, cx + facing * 32
                    d.rectangle((min(tx0, tx1), base_y + 10, max(tx0, tx1), base_y + 22), fill=outline)
                    d.rectangle((min(sx0, sx1), base_y + 12, max(sx0, sx1), base_y + 19), fill=primary)
                    d.line((cx + facing * 21, base_y + 14, cx + facing * 31, base_y + 14), fill=glow, width=1)
                if anim == "failed":
                    d.line((cx - 20, yy + 18, cx - 27, yy + 8), fill=accent, width=2)
                    d.line((cx + 18, yy + 16, cx + 27, yy + 9), fill=accent, width=2)
            else:
                # Wide cheek fins and dangling tassels keep mask familiars from
                # collapsing into wheel/lantern-like ovals in silhouette checks.
                d.polygon([(x - 16, yy + 15), (x, yy + 3), (x + 17, yy + 16), (x + 12, yy + 40), (x, yy + 50), (x - 13, yy + 41)], fill=outline)
                d.polygon([(x - 12, yy + 17), (x, yy + 8), (x, yy + 45), (x - 8, yy + 38)], fill=primary)
                d.polygon([(x + 13, yy + 18), (x, yy + 8), (x, yy + 45), (x + 8, yy + 38)], fill=secondary)
                d.polygon([(x - 16, yy + 23), (x - 33 - pulse, yy + 16 + sway), (x - 27, yy + 31)], fill=outline)
                d.polygon([(x + 17, yy + 23), (x + 31 + pulse, yy + 35 - sway), (x + 25, yy + 18)], fill=outline)
                d.polygon([(x - 19, yy + 24), (x - 29 - pulse, yy + 19 + sway), (x - 25, yy + 28)], fill=accent)
                d.polygon([(x + 19, yy + 24), (x + 28 + pulse, yy + 32 - sway), (x + 24, yy + 21)], fill=glow)
                d.line((x - 7, yy + 45, x - 19, yy + 58), fill=accent, width=3)
                d.line((x + 7, yy + 45, x + 19, yy + 57), fill=glow, width=3)
                d.rectangle((x - 9, yy + 26, x + 9, yy + 29), fill=glow)
        elif archetype == 10:  # tiny train familiar
            # Low locomotive silhouette with separated chimney, caboose, wheels,
            # and smoke puffs. This intentionally avoids the arched bridge/crawler
            # footprint that earlier train hatches could overlap in alpha masks.
            roll = [0, 2, 4, 2, 0, -2][i % FRAMES]
            if anim in {"running-right", "running-left", "running"}:
                x += facing * roll
            if anim == "failed":
                yy += 3
            track_y = yy + 50
            d.line((x - 27, track_y, x + 28, track_y), fill=outline, width=2)
            d.rounded_rectangle((x - 25, yy + 32, x + 12, yy + 44), radius=3, fill=outline)
            d.rectangle((x - 21, yy + 34, x + 8, yy + 41), fill=primary)
            d.rectangle((x + 9, yy + 23, x + 24, yy + 43), fill=outline)
            d.rectangle((x + 12, yy + 27, x + 21, yy + 40), fill=secondary)
            d.rectangle((x - 19, yy + 22, x - 12, yy + 33), fill=outline)
            d.rectangle((x - 17, yy + 19, x - 10, yy + 23), fill=accent)
            d.polygon([(x + 24, yy + 31), (x + 31, yy + 36), (x + 24, yy + 42)], fill=glow)
            for n, wx in enumerate((x - 18, x - 4, x + 14)):
                r = 5 if n != 1 else 4
                d.ellipse((wx - r - 1, yy + 40 - r, wx + r + 1, yy + 40 + r), fill=outline)
                d.ellipse((wx - r, yy + 40 - r, wx + r, yy + 40 + r), fill=accent if n != 1 else glow)
                d.line((wx, yy + 40, wx + ((i + n) % 3) - 1, yy + 40 - r), fill=outline, width=1)
            for n in range(3):
                sx = x - 17 - n * 7 - (i % 2)
                sy = yy + 14 - n * 3 - (pulse if anim != "failed" else -1)
                rr = 2 + n
                d.ellipse((sx - rr, sy - rr, sx + rr, sy + rr), fill=glow if n % 2 else secondary)
            if anim == "waving":
                # A semaphore flag makes the train's wave read clearly even
                # though it has no arms.
                mast_x = x + 19
                mast_top = yy + 9 + [0, -2, -4, -2, 1, 2][i % FRAMES]
                d.line((mast_x, yy + 24, mast_x, mast_top), fill=outline, width=2)
                flag_tip = mast_x + facing * (9 + pulse)
                d.polygon([(mast_x, mast_top), (flag_tip, mast_top + 3 + sway), (mast_x, mast_top + 8)], fill=accent)
                d.line((mast_x + facing, mast_top + 2, flag_tip - facing, mast_top + 4 + sway), fill=glow, width=1)
            elif anim == "failed":
                # Drooping hazard sign and jittering sparks keep failure from
                # looking like a barely-shifted idle frame.
                sign_x = x - 24 + [0, 1, -1, 0, 1, -1][i % FRAMES]
                d.line((sign_x, yy + 28, sign_x - 5, yy + 42), fill=outline, width=2)
                d.polygon([(sign_x - 7, yy + 25), (sign_x + 2, yy + 27), (sign_x - 4, yy + 35)], fill=accent)
                for n in range(4):
                    sx = x + 24 + n * 3
                    sy = yy + 18 + ((i + n) % 4)
                    d.line((sx, sy, sx + 2, sy - 3), fill=glow if n % 2 else accent, width=1)
        elif archetype == 11:  # manta glider
            # Wide glider body with animated wingbeats.  Manta familiars should
            # read as soaring/swimming companions, not static diamond sprites.
            flap = [0, -3, -5, -2, 2, 4][i % FRAMES]
            if anim in {"running-right", "running-left", "running"}:
                flap += [0, -4, -2, 3, 5, 1][i % FRAMES]
                x += facing * [0, 2, 4, 2, 0, -2][i % FRAMES]
            elif anim == "waving":
                flap += [-1, -6, -8, -5, 1, 3][i % FRAMES]
            elif anim == "jumping":
                flap += [-3, -6, -9, -7, -2, 1][i % FRAMES]
            elif anim == "failed":
                flap += [4, 5, 6, 5, 4, 3][i % FRAMES]
            elif anim == "review":
                flap += [0, -1, -2, -1, 1, 2][i % FRAMES]
            tail_wave = [0, 2, 4, 1, -2, -3][i % FRAMES]
            nose = yy + 14 + tilt + (flap // 2)
            left_tip = yy + 28 + flap
            right_tip = yy + 28 - flap
            tail_y = yy + 52 + tail_wave
            outer = [(x - 28, left_tip), (x - 7, nose), (x + 27, right_tip), (x + 7, yy + 40 - flap // 2), (x, tail_y), (x - 7, yy + 40 + flap // 2)]
            inner = [(x - 19, yy + 29 + flap // 2), (x - 3, yy + 20 + flap // 3), (x + 18, yy + 29 - flap // 2), (x + 3, yy + 37), (x, yy + 45 + tail_wave // 2), (x - 3, yy + 37)]
            d.polygon(outer, fill=outline)
            d.polygon(inner, fill=primary)
            # Directional fins make left/right rows visibly distinct for the
            # asymmetric generated queue.
            d.polygon([(x + facing * 14, yy + 32), (x + facing * (28 + pulse), yy + 27 + sway), (x + facing * 18, yy + 37)], fill=secondary)
            d.line((x - 13, yy + 31 + flap // 3, x + 13, yy + 31 - flap // 3), fill=glow, width=2)
            d.line((x, yy + 44, x + facing * (9 + pulse), tail_y + 5), fill=accent, width=2)
        elif archetype == 12:  # book golem
            # Open-book familiars need visible page language, not a static badge.
            # Animate the covers differently per state: running skims forward,
            # waving flips a bright page, failed droops, and review projects a
            # scan bookmark.  This keeps book-class hatches from reading as a
            # one-motion/static pet in README showcases.
            page = [0, 3, 6, 3, -2, -4][i % FRAMES]
            bob = [0, -1, -2, -1, 1, 2][i % FRAMES]
            if anim in {"running-right", "running-left", "running"}:
                x += facing * [0, 2, 4, 2, 0, -2][i % FRAMES]
                yy += bob
                page += facing * [0, 2, 4, 1, -2, -3][i % FRAMES]
            elif anim == "waving":
                page += [0, 5, 9, 5, 1, -2][i % FRAMES]
            elif anim == "failed":
                page = -5 + [0, -1, -2, -1, 0, 1][i % FRAMES]
            elif anim == "review":
                page += [0, 1, 3, 5, 3, 1][i % FRAMES]
            left_outer = [(x - 18 - page // 3, yy + 17 + bob), (x, yy + 22), (x, yy + 50), (x - 18 + page // 4, yy + 45 - bob)]
            right_outer = [(x + 18 + page // 2, yy + 17 - bob), (x, yy + 22), (x, yy + 50), (x + 18 - page // 3, yy + 45 + bob)]
            left_inner = [(x - 14 - page // 3, yy + 21 + bob), (x - 2, yy + 24), (x - 2, yy + 45), (x - 14 + page // 4, yy + 42 - bob)]
            right_inner = [(x + 14 + page // 2, yy + 21 - bob), (x + 2, yy + 24), (x + 2, yy + 45), (x + 14 - page // 3, yy + 42 + bob)]
            d.polygon(left_outer, fill=outline)
            d.polygon(right_outer, fill=outline)
            d.polygon(left_inner, fill=secondary)
            d.polygon(right_inner, fill=primary)
            d.line((x, yy + 22, x, yy + 50), fill=accent, width=2)
            d.line((x - 11, yy + 29 + bob, x - 4, yy + 31 + bob), fill=glow, width=1)
            d.line((x + 5, yy + 34 - bob, x + 13 + page // 3, yy + 36 - bob), fill=secondary, width=1)
            if anim == "waving":
                d.arc((x + 7, yy + 8 - page // 2, x + 31, yy + 31), 200, 335, fill=glow, width=2)
                d.line((x + 14, yy + 20, x + 24 + page // 2, yy + 12 - bob), fill=accent, width=2)
            if anim == "review":
                d.line((x + facing * 13, yy + 24, x + facing * (27 + page), yy + 16 + bob), fill=glow, width=2)
                bx0, bx1 = x + facing * 20, x + facing * 25
                d.rectangle((min(bx0, bx1), yy + 13, max(bx0, bx1), yy + 17), fill=accent)
            if slug == "ravenbyte-253-drift-flux-book":
                # Flux Book needs to differ materially from earlier book/mask
                # silhouettes. Give it a wind-swept codex mast, separated page
                # pennants, and a low ribbon tail so the base silhouette is not a
                # clone of prior open-book familiars while preserving its book read.
                mast_x = x + facing * 19
                d.line((mast_x, yy + 10 + bob, mast_x - facing * 7, yy + 1 + bob), fill=outline, width=4)
                d.line((mast_x, yy + 10 + bob, mast_x - facing * 7, yy + 1 + bob), fill=glow, width=2)
                for n in range(3):
                    px = mast_x - facing * (8 + n * 5)
                    py = yy + 4 + n * 7 + ((i + n) % 2)
                    d.polygon(
                        [(px, py), (px - facing * (8 + n), py + 3), (px, py + 7), (px + facing * 2, py + 3)],
                        fill=outline,
                    )
                    d.polygon(
                        [(px, py + 1), (px - facing * (5 + n), py + 3), (px, py + 5), (px + facing, py + 3)],
                        fill=accent if n % 2 else glow,
                    )
                tail_y = yy + 51 + bob
                d.arc((x - 31, tail_y - 8, x + 31, tail_y + 8), 190, 350, fill=outline, width=4)
                d.arc((x - 30, tail_y - 7, x + 30, tail_y + 7), 190, 350, fill=accent, width=2)
                if anim in {"running-right", "running-left", "running"}:
                    d.line((x - facing * 23, tail_y + 1, x - facing * 31, tail_y + 6 + sway), fill=glow, width=2)
            if slug == "ravenbyte-269-morrow-patch-book":
                # Patch Book almost overlapped an older lantern stack in the
                # alpha-mask check. Add a low repair-bench silhouette, separated
                # patch tabs, and a side needle mast so it reads as a mending
                # codex rather than a vertical hanging lantern.
                bench_y = yy + 53 + bob
                d.rounded_rectangle((x - 30, bench_y - 3, x + 28, bench_y + 3), radius=2, fill=outline)
                d.rectangle((x - 25, bench_y - 1, x + 23, bench_y + 1), fill=accent)
                for n, tab_x in enumerate((x - 24, x - 14, x + 17, x + 27)):
                    lift = ((i + n) % 2) if anim in {"running-right", "running-left", "running", "waiting"} else 0
                    d.rectangle((tab_x - 3, yy + 39 - lift, tab_x + 3, yy + 48 - lift), fill=outline)
                    d.rectangle((tab_x - 2, yy + 41 - lift, tab_x + 2, yy + 46 - lift), fill=glow if n % 2 else accent)
                mast_x = x - facing * (22 + pulse)
                d.line((x - facing * 14, yy + 25, mast_x, yy + 6 + sway), fill=outline, width=4)
                d.line((x - facing * 14, yy + 25, mast_x, yy + 6 + sway), fill=secondary, width=2)
                d.ellipse((mast_x - 4, yy + 3 + sway, mast_x + 4, yy + 11 + sway), fill=glow)
                if anim == "failed":
                    d.line((x - 25, bench_y - 7, x + 25, bench_y + 5), fill="#ff3344", width=2)
                elif anim == "review":
                    d.line((mast_x, yy + 7 + sway, mast_x - facing * 12, yy + 1), fill=accent, width=2)
        elif archetype == 13:  # asymmetric key guardian
            # Key-class familiars need to read as more than a static lollipop.
            # Give the bow, shaft, teeth, tether, and beacon halo independent
            # state motion so showcases prove multiple authored motions.
            step = [0, 2, 4, 2, 0, -2][i % FRAMES] if anim in {"running-right", "running-left", "running"} else 0
            spin = [0, 2, 4, 1, -2, -3][i % FRAMES]
            wave = [0, -3, -6, -3, 1, 3][i % FRAMES] if anim == "waving" else 0
            if anim in {"running-right", "running-left", "running"}:
                x += facing * step
                yy += [0, -1, -2, -1, 1, 2][i % FRAMES]
            if anim == "failed":
                yy += 3
                spin = 6
            if anim == "jumping":
                spin -= 3
            bow_cy = yy + 25 + spin // 3
            d.ellipse((x - 15, bow_cy - 14, x + 15, bow_cy + 14), fill=outline)
            d.ellipse((x - 10, bow_cy - 9, x + 10, bow_cy + 9), fill=primary)
            d.ellipse((x - 4, bow_cy - 4, x + 4, bow_cy + 4), fill=outline)
            # Directional shaft and teeth; left/right rows are intentionally not mirrored copies.
            shaft_y = yy + 28 + sway + wave // 3
            d.line((x + facing * 10, shaft_y, x + facing * (31 + pulse), shaft_y + spin // 2), fill=outline, width=7)
            d.line((x + facing * 10, shaft_y, x + facing * (31 + pulse), shaft_y + spin // 2), fill=accent, width=4)
            tooth_x = x + facing * (25 + pulse)
            d.rectangle((min(tooth_x, tooth_x + facing * 11), shaft_y - 8, max(tooth_x, tooth_x + facing * 11), shaft_y - 3), fill=secondary)
            d.rectangle((min(tooth_x + facing * 5, tooth_x + facing * 15), shaft_y + 4, max(tooth_x + facing * 5, tooth_x + facing * 15), shaft_y + 9), fill=glow)
            # Tether and beacon tag sell motion in waving/review states.
            tail_x = x - facing * 11
            d.line((tail_x, yy + 35, tail_x - facing * (11 + pulse), yy + 51 - spin), fill=outline, width=5)
            d.line((tail_x, yy + 35, tail_x - facing * (11 + pulse), yy + 51 - spin), fill=glow, width=3)
            tag_x = tail_x - facing * (13 + pulse)
            d.polygon([(tag_x, yy + 49 - spin), (tag_x - facing * 6, yy + 54 - spin + wave // 2), (tag_x, yy + 58 - spin)], fill=accent)
            if anim == "waving":
                d.arc((x - 27, yy + 5 + wave, x + 27, yy + 35), 205, 335, fill=glow, width=3)
                d.line((x - facing * 3, yy + 15, x - facing * 20, yy + 7 + wave), fill=secondary, width=2)
            if anim == "review":
                d.arc((x - 24, yy + 5, x + 24, yy + 47), 210, 330, fill=accent, width=2)
                d.line((x + facing * 18, yy + 18, x + facing * 34, yy + 8 + spin), fill=glow, width=2)
            if anim == "failed":
                d.line((x - 8, bow_cy - 8, x + 8, bow_cy + 8), fill="#ff3344", width=2)
                d.line((x + 8, bow_cy - 8, x - 8, bow_cy + 8), fill="#ff3344", width=2)
        elif archetype == 14:  # bell jellyfish
            # Bell jelly familiars are asymmetric: a side scanner fin and
            # direction-leaning tendrils make running-left genuinely distinct
            # from running-right instead of a duplicated row.
            swim = [0, 2, 4, 2, 0, -2][i % FRAMES]
            if anim in {"running-right", "running-left", "running"}:
                x += facing * swim
                yy += [0, -1, -2, -1, 1, 2][i % FRAMES]
            bell_w = 17 + (pulse % 2)
            d.pieslice((x - bell_w, yy + 10, x + bell_w, yy + 44), 180, 360, fill=outline)
            d.pieslice((x - 13, yy + 14, x + 13, yy + 40), 180, 360, fill=primary)
            # Directional scanner fin / delta rudder.
            d.polygon(
                [(x + facing * 11, yy + 24), (x + facing * (26 + pulse), yy + 18 + sway), (x + facing * 18, yy + 35)],
                fill=secondary,
            )
            d.line((x + facing * 9, yy + 28, x + facing * (24 + pulse), yy + 25 + sway), fill=glow, width=2)
            for n in range(5):
                tx = x - 12 + n * 6
                lean = facing * (2 + ((n + i) % 3)) if anim in {"running-right", "running-left", "running"} else ((n + i) % 3) - 1
                d.line((tx, yy + 29, tx + lean, yy + 51), fill=[secondary, accent, glow][n % 3], width=2)
            if anim == "review":
                ax0, ax1 = x - facing * 28, x - facing * 6
                d.arc((min(ax0, ax1), yy + 10, max(ax0, ax1), yy + 34), 200, 330, fill=accent, width=2)
            if anim == "failed":
                d.line((x - 11, yy + 22, x + 10, yy + 37), fill="#ff3344", width=2)
        else:  # scaffold rabbit
            d.rounded_rectangle((x - 12, yy + 22, x + 12, yy + 45), radius=5, fill=outline)
            d.rounded_rectangle((x - 9, yy + 25, x + 9, yy + 42), radius=4, fill=primary)
            d.line((x - 6, yy + 24, x - 15, yy + 4 + sway), fill=secondary, width=5)
            d.line((x + 6, yy + 24, x + 16, yy + 7 - sway), fill=accent, width=5)
            d.line((x - 7, yy + 44, x - 14 - pulse, yy + 53), fill=glow, width=3)
            d.line((x + 7, yy + 44, x + 15 + pulse, yy + 53), fill=glow, width=3)
        # Common face and state language, drawn last so it remains readable.
        d.rectangle((x - 6, yy + 28, x + 6, yy + 30), fill=outline)
        d.rectangle((x - 5, yy + 28, x + 5, yy + 29), fill=glow if anim != "failed" else "#ff3344")
        if anim == "waving":
            d.arc((x - 27, yy + 8, x - 5, yy + 30), 190, 330, fill=glow, width=2)
        draw_state_fx()
    else:
        # Round spirit/animal automaton silhouette for oni, tanuki, cat, monk, etc.
        x = 32
        d.ellipse((x - 17, y + 21, x + 17, y + 47), fill=outline)
        d.ellipse((x - 14, y + 24, x + 14, y + 45), fill=primary)
        if "oni" in slug:
            d.polygon([(x - 10, y + 18), (x - 15, y + 4), (x - 4, y + 16)], fill=accent)
            d.polygon([(x + 10, y + 18), (x + 15, y + 4), (x + 4, y + 16)], fill=accent)
        elif "cat" in slug:
            d.polygon([(x - 12, y + 22), (x - 18, y + 10), (x - 6, y + 17)], fill=secondary)
            d.polygon([(x + 12, y + 22), (x + 18, y + 10), (x + 6, y + 17)], fill=secondary)
            d.arc((x + 10, y + 34, x + 31, y + 55), 190, 330, fill=accent, width=3)
        elif "tanuki" in slug:
            d.ellipse((x - 22, y + 24, x - 13, y + 40), fill=accent)
            d.ellipse((x + 13, y + 24, x + 22, y + 40), fill=accent)
            d.polygon([(x, y + 11), (x + 5, y + 2), (x + 2, y + 13)], fill="#7cb518")
        d.rounded_rectangle((x - 10, y + 28, x + 10, y + 36), radius=3, fill=secondary)
        eye_line(x, y + 31)
        for lx in (x - 10 - run, x + 6 + run):
            rect((lx, y + 45, lx + 6, y + 53), secondary)
        draw_state_fx()

    if mirrored:
        img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    return img

def draw_pet_frame(spec: PetSpec, anim: str, i: int, mirrored: bool = False) -> Image.Image:
    specialized = draw_specialized_frame(spec, anim, i, mirrored=mirrored)
    if specialized is not None:
        return specialized

    img = Image.new("RGBA", (FRAME, FRAME), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    # Animation offsets.
    bob = int(round(math.sin(i / FRAMES * math.tau) * 2))
    run = [0, 2, 1, 0, -1, -2][i % FRAMES]
    jump = -8 if i in (2, 3) else (-4 if i in (1, 4) else 0)
    wait = 1 if i % 2 else 0
    fail_slump = 3 if anim == "failed" else 0
    y = 10 + (jump if anim == "jumping" else bob if anim in {"idle", "waiting", "review"} else 0) + fail_slump
    x = 32

    primary = spec.primary
    secondary = spec.secondary
    accent = spec.accent
    glow = spec.glow
    outline = "#070912"
    shadow = (0, 0, 0, 55)

    # Directional pose.
    leg_phase = run if anim in {"running-right", "running-left", "running"} else 0
    arm_wave = -8 if anim == "waving" and i in (1, 2, 3) else 0
    review_tilt = -2 if anim == "review" and i % 2 else 0

    # Ground shadow.
    d.ellipse((17, 54, 47, 60), fill=shadow)

    # Energy scarf / code ribbon.
    scarf_y = y + 18 + wait
    if anim in {"running-right", "running-left", "running"}:
        tail = [(x - 9, scarf_y), (x - 24 - abs(run), scarf_y - 2), (x - 19, scarf_y + 4)]
    elif anim == "review":
        tail = [(x - 8, scarf_y), (x - 22, scarf_y + review_tilt), (x - 19, scarf_y + 5)]
    else:
        tail = [(x - 8, scarf_y), (x - 18, scarf_y - 1), (x - 15, scarf_y + 4)]
    d.polygon(tail, fill=hex_to_rgba(glow, 190))

    # Legs.
    left_leg = (x - 10 - leg_phase, y + 34, x - 4 - leg_phase, y + 49)
    right_leg = (x + 4 + leg_phase, y + 34, x + 10 + leg_phase, y + 49)
    for leg in (left_leg, right_leg):
        pix(d, (leg[0]-1, leg[1]-1, leg[2]+1, leg[3]+1), outline)
        pix(d, leg, primary)
        pix(d, (leg[0]+1, leg[3]-4, leg[2]+2, leg[3]+1), secondary)

    # Torso armor.
    d.polygon([(x - 15, y + 19), (x + 15, y + 19), (x + 12, y + 38), (x - 12, y + 38)], fill=outline)
    d.polygon([(x - 12, y + 21), (x + 12, y + 21), (x + 10, y + 35), (x - 10, y + 35)], fill=primary)
    d.polygon([(x - 7, y + 22), (x + 7, y + 22), (x + 5, y + 31), (x - 5, y + 31)], fill=secondary)
    pix(d, (x - 2, y + 25, x + 2, y + 31), glow)

    # Arms / kunai panels.
    left_arm_y = y + 23 + (arm_wave if anim == "waving" else 0)
    right_arm_y = y + 23
    arms = [
        (x - 20, left_arm_y, x - 13, left_arm_y + 16),
        (x + 13, right_arm_y, x + 20, right_arm_y + 16),
    ]
    if anim == "failed":
        arms = [(x - 21, y + 29, x - 14, y + 45), (x + 14, y + 29, x + 21, y + 45)]
    for a in arms:
        pix(d, (a[0]-1, a[1]-1, a[2]+1, a[3]+1), outline)
        pix(d, a, primary)
        d.polygon([(a[0], a[3]), ((a[0]+a[2])//2, a[3]+5), (a[2], a[3])], fill=accent)

    # Head and helmet.
    d.rounded_rectangle((x - 15, y + 2, x + 15, y + 22), radius=5, fill=outline)
    d.rounded_rectangle((x - 12, y + 5, x + 12, y + 20), radius=4, fill=secondary)
    d.polygon([(x - 14, y + 5), (x - 5, y - 2), (x - 5, y + 7)], fill=outline)
    d.polygon([(x + 14, y + 5), (x + 5, y - 2), (x + 5, y + 7)], fill=outline)
    pix(d, (x - 9, y + 11, x + 9, y + 15), outline)
    if anim == "failed":
        pix(d, (x - 8, y + 11, x - 4, y + 15), accent)
        pix(d, (x + 4, y + 11, x + 8, y + 15), accent)
        d.line((x - 8, y + 12, x - 4, y + 15), fill=outline, width=1)
        d.line((x - 4, y + 12, x - 8, y + 15), fill=outline, width=1)
        d.line((x + 4, y + 12, x + 8, y + 15), fill=outline, width=1)
        d.line((x + 8, y + 12, x + 4, y + 15), fill=outline, width=1)
    else:
        pix(d, (x - 8, y + 12, x + 8, y + 14), accent)
        if anim == "review":
            pix(d, (x + 2, y + 12, x + 8, y + 14), glow)

    # State props.
    if anim == "waiting":
        for n in range(3):
            cx = 44 + n * 5
            cy = 15 - ((i + n) % 3)
            d.ellipse((cx, cy, cx + 2, cy + 2), fill=glow)
    if anim == "review":
        d.rounded_rectangle((39, 34, 56, 46), radius=2, fill=outline)
        d.rectangle((42, 36, 53, 43), fill="#1b263b")
        d.line((43, 38, 51, 38), fill=glow)
        d.line((43, 41, 49, 41), fill=accent)
    if anim == "jumping":
        d.arc((20, 48, 44, 61), 205, 335, fill=hex_to_rgba(glow, 150), width=2)

    if mirrored:
        img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    return img


def save_strip(frames: list[Image.Image], path: Path) -> None:
    strip = Image.new("RGBA", (FRAME * len(frames), FRAME), (0, 0, 0, 0))
    for idx, frame in enumerate(frames):
        strip.alpha_composite(frame, (idx * FRAME, 0))
    strip.save(path)


def compose_sheet(rows: list[Image.Image], path: Path) -> None:
    sheet = Image.new("RGBA", (FRAME * FRAMES, FRAME * len(rows)), (0, 0, 0, 0))
    for idx, row in enumerate(rows):
        sheet.alpha_composite(row, (0, idx * FRAME))
    sheet.save(path, "WEBP", lossless=True, quality=100, method=6)


def make_contact_sheet(spec: PetSpec, sheet_path: Path, out: Path) -> None:
    sheet = Image.open(sheet_path).convert("RGBA")
    scale = 3
    margin = 16
    label_w = 128
    out_img = Image.new("RGBA", (label_w + sheet.width * scale + margin * 2, sheet.height * scale + margin * 2), "#0b1020")
    d = ImageDraw.Draw(out_img)
    for row, anim in enumerate(ANIMS):
        y = margin + row * FRAME * scale + 22
        d.text((margin, y), anim, fill="#dbeafe")
    resized = sheet.resize((sheet.width * scale, sheet.height * scale), Image.Resampling.NEAREST)
    out_img.alpha_composite(resized, (label_w, margin))
    d.text((margin, 4), spec.display_name, fill="#ffffff")
    out_img.convert("RGB").save(out)


def make_gifs_and_videos(spec: PetSpec, strips_dir: Path, previews_dir: Path) -> None:
    previews_dir.mkdir(parents=True, exist_ok=True)
    for anim in ANIMS:
        strip = Image.open(strips_dir / f"{anim}.png").convert("RGBA")
        frames = [strip.crop((i * FRAME, 0, (i + 1) * FRAME, FRAME)).resize((FRAME * 4, FRAME * 4), Image.Resampling.NEAREST) for i in range(FRAMES)]
        gif_path = previews_dir / f"{spec.slug}-{anim}.gif"
        frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=110, loop=0, disposal=2)

        # MP4 via ffmpeg from GIF, best-effort. Disabled by default for large
        # batch hatches because GIFs/showcases are the README proof media and
        # validation does not require MP4 exports. Set RAVENBYTE_RENDER_MP4=1
        # for release runs that need video attachments.
        if os.environ.get("RAVENBYTE_RENDER_MP4") == "1":
            mp4_path = previews_dir / f"{spec.slug}-{anim}.mp4"
            try:
                subprocess.run([
                    "ffmpeg", "-y", "-v", "error", "-i", str(gif_path),
                    "-movflags", "faststart", "-pix_fmt", "yuv420p", "-vf", "scale=256:256:flags=neighbor",
                    str(mp4_path),
                ], check=True)
            except Exception:
                pass


def make_pet_readme(spec: PetSpec, pet_root: Path) -> None:
    motion_notes = {
        "samurai-cache-crab": (
            "side-stepping with cache-crystal claws, kabuto-shell armor bob, "
            "waving pincer clicks, jump-snap arcs, failed-state spark slumps, "
            "waiting beacon dots, and review-tablet scan posture"
        ),
        "ramen-debug-drone": (
            "hovering bowl-body drift, chopstick antenna wobble, steam-pixel bursts, "
            "hot-fix serving gestures, and review-tablet scan sweeps"
        ),
        "origami-test-heron": (
            "folded-paper wing tilts, long-leg test pecks, jump glides, "
            "flaky-test alert sparks, and precise review scans"
        ),
    }
    note = motion_notes.get(
        spec.slug,
        "distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows",
    )
    rows = "\n".join(
        f"| {anim.replace('-', ' ').title()} | ![{anim.replace('-', ' ').title()}](previews/{spec.slug}-{anim}.gif) |"
        for anim in ANIMS
    )
    mirrored = (
        f"- `running-left`: mirrored from `running-right` because {spec.display_name} is intentionally symmetric"
        if spec.symmetric
        else "- `running-left`: drawn as a separate row because this familiar has side-specific details"
    )
    content = f"""# {spec.display_name}

<p align="center">
  <img src="previews/{spec.slug}-showcase.gif" width="360" alt="{spec.display_name} stitched multi-motion showcase">
</p>

**{spec.tagline}**

{spec.display_name} is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around {spec.theme}, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

{spec.display_name} brings a distinct motion language to Ravenbyte Familiars: {note}.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
{rows}

Full contact sheet:

![{spec.display_name} contact sheet](previews/{spec.slug}-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py {spec.slug}
```

Or from anywhere with Git:

```bash
PET={spec.slug}; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${{CODEX_HOME:-$HOME/.codex}}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${{CODEX_HOME:-$HOME/.codex}}/pets/{spec.slug}/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  {spec.slug}-showcase.gif
  {spec.slug}-idle.gif
  {spec.slug}-running-right.gif
  {spec.slug}-running-left.gif
  {spec.slug}-waving.gif
  {spec.slug}-jumping.gif
  {spec.slug}-failed.gif
  {spec.slug}-waiting.gif
  {spec.slug}-running.gif
  {spec.slug}-review.gif
  {spec.slug}-contact-sheet.png
generated/
  base.png
  imagegen-prompt.json
  strips/*.png
```

## Sprite metadata

- Frame size: `64×64`
- Frames per row: `6`
- Rows: `9`
- Spritesheet: `384×576`
- Symmetric design: {'yes' if spec.symmetric else 'no'}
{mirrored}
- Author: `ObliviousOdin`

## Design notes

The design is intentionally original. It uses broad visual language from {spec.theme}, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
"""
    (pet_root / "README.md").write_text(content)


def validate_package(pkg: Path) -> None:
    pet_json = pkg / "pet.json"
    sheet_path = pkg / "spritesheet.webp"
    assert pet_json.exists(), f"missing {pet_json}"
    assert sheet_path.exists(), f"missing {sheet_path}"
    data = json.loads(pet_json.read_text())
    assert data["frameWidth"] == FRAME
    assert data["frameHeight"] == FRAME
    assert data["framesPerRow"] == FRAMES
    assert [a["name"] for a in data["animations"]] == ANIMS
    sheet = Image.open(sheet_path)
    assert sheet.size == (FRAME * FRAMES, FRAME * len(ANIMS)), sheet.size
    assert sheet.mode in ("RGBA", "RGB")


def hatch(spec: PetSpec, root: Path, codex_home: Path) -> Path:
    pet_root = root / "pets" / spec.slug
    gen = pet_root / "generated"
    strips = gen / "strips"
    previews = pet_root / "previews"
    for p in (gen, strips, previews):
        p.mkdir(parents=True, exist_ok=True)

    # 1. Deterministic base look fallback. The intended imagegen prompt is saved
    #    for auditability even when no image provider is configured.
    prompt = {
        "imagegen_prompt": f"Tiny original Codex pet sprite: {spec.display_name}. {spec.theme}. chibi full-body pixel art, transparent background, thick outline, readable at 64x64, no text, no logos.",
        "note": "If $imagegen is configured, generate base.png from this prompt before running compose. This run used deterministic vector fallback because imagegen was unavailable.",
    }
    (gen / "imagegen-prompt.json").write_text(json.dumps(prompt, indent=2) + "\n")
    base = draw_pet_frame(spec, "idle", 0)
    base.save(gen / "base.png")

    # 2. Generate every row strip.
    rows = []
    for anim in ANIMS:
        mirrored = anim == "running-left" and spec.symmetric
        source_anim = "running-right" if mirrored else anim
        frames = [draw_pet_frame(spec, source_anim, i, mirrored=mirrored) for i in range(FRAMES)]
        strip_path = strips / f"{anim}.png"
        save_strip(frames, strip_path)
        rows.append(Image.open(strip_path).convert("RGBA"))

    # 3. Compose and validate.
    spritesheet = pet_root / "spritesheet.webp"
    compose_sheet(rows, spritesheet)

    pet_json = {
        "schemaVersion": 1,
        "name": spec.slug,
        "displayName": spec.display_name,
        "description": spec.tagline,
        "author": "ObliviousOdin",
        "frameWidth": FRAME,
        "frameHeight": FRAME,
        "framesPerRow": FRAMES,
        "spritesheet": "spritesheet.webp",
        "symmetric": spec.symmetric,
        "animations": [
            {"name": name, "row": idx, "frames": FRAMES, "fps": 9 if "running" in name else 7, "loop": True}
            for idx, name in enumerate(ANIMS)
        ],
        "states": {
            "idle": "idle",
            "running-right": "running-right",
            "running-left": "running-left",
            "waving": "waving",
            "jumping": "jumping",
            "failed": "failed",
            "waiting": "waiting",
            "running": "running",
            "review": "review",
        },
        "install": {
            "codexHomeRelativePath": f"pets/{spec.slug}",
            "openDesign": "Settings → Pets → Import Codex sprite",
        },
    }
    (pet_root / "pet.json").write_text(json.dumps(pet_json, indent=2) + "\n")

    make_contact_sheet(spec, spritesheet, previews / f"{spec.slug}-contact-sheet.png")
    make_gifs_and_videos(spec, strips, previews)
    render_showcase(pet_root)
    make_pet_readme(spec, pet_root)
    validate_package(pet_root)

    # 4. Package to Codex home.
    dest = codex_home / "pets" / spec.slug
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(pet_root, dest)
    validate_package(dest)
    return dest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pet", default="kageframe-rx07", help="pet slug or 'next'")
    parser.add_argument("--root", default=".")
    parser.add_argument("--codex-home", default=str(Path.home() / ".codex"))
    args = parser.parse_args()

    root = Path(args.root).resolve()
    codex_home = Path(args.codex_home).expanduser().resolve()
    specs = {p.slug: p for p in PRESETS}
    if args.pet == "next":
        existing = [p for p in PRESETS if not (root / "pets" / p.slug).exists()]
        spec = existing[0] if existing else PRESETS[0]
    else:
        spec = specs.get(args.pet)
        if spec is None and args.pet.startswith("ravenbyte-"):
            from hatch_surge import generated_specs

            generated = {p.slug: p for p in generated_specs(512)}
            spec = generated.get(args.pet)
        if spec is None:
            raise SystemExit(f"unknown pet {args.pet}; choices: {', '.join(specs)}")
    dest = hatch(spec, root, codex_home)
    print(dest)


if __name__ == "__main__":
    main()
