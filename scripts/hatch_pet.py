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
            d.polygon([(x - 18, yy + 29), (x - 5, yy + 16 + tilt), (x + 16, yy + 23), (x + 21, yy + 39), (x - 15, yy + 43)], fill=outline)
            d.polygon([(x - 13, yy + 30), (x - 3, yy + 21), (x + 12, yy + 26), (x + 15, yy + 37), (x - 11, yy + 39)], fill=primary)
            for n in range(4):
                lx = x - 14 + n * 9
                d.line((lx, yy + 40, lx - 6 + ((i + n) % 3), yy + 51), fill=secondary, width=3)
        elif archetype == 3:  # crescent kite
            d.pieslice((x - 21, yy + 10, x + 21, yy + 52), 40 + tilt, 320 + tilt, fill=outline)
            d.pieslice((x - 16, yy + 15, x + 16, yy + 47), 45 + tilt, 315 + tilt, fill=primary)
            d.polygon([(x, yy + 16), (x + facing * (22 + pulse), yy + 30), (x, yy + 44), (x - facing * 7, yy + 30)], fill=secondary)
        elif archetype == 4:  # tall shrine totem
            w = 8 + (seed % 6)
            d.rounded_rectangle((x - w, yy + 6, x + w, yy + 49), radius=3, fill=outline)
            d.rectangle((x - w + 3, yy + 10, x + w - 3, yy + 45), fill=primary)
            for k in range(4):
                d.line((x - w - 6 + (k % 2), yy + 14 + k * 8, x + w + 6 - (k % 2), yy + 14 + k * 8), fill=[secondary, accent, glow][k % 3], width=2)
            d.polygon([(x, yy), (x + 14, yy + 9), (x - 14, yy + 9)], fill=accent)
        elif archetype == 5:  # serpent ribbon
            pts = []
            for k in range(6):
                pts.append((x - 20 + k * 8, yy + 28 + int(math.sin((i + k) / 2) * (5 + seed % 4))))
            d.line(pts, fill=outline, width=9)
            d.line(pts, fill=primary, width=5)
            hx, hy = pts[-1]
            d.polygon([(hx, hy - 6), (hx + facing * 12, hy), (hx, hy + 6)], fill=secondary)
        elif archetype == 6:  # crystal tripod
            d.polygon([(x, yy + 5), (x + 15, yy + 25), (x + 7, yy + 45), (x - 10, yy + 43), (x - 16, yy + 24)], fill=outline)
            d.polygon([(x, yy + 9), (x + 10, yy + 26), (x + 5, yy + 40), (x - 7, yy + 38), (x - 11, yy + 25)], fill=secondary)
            for lx in (-10, 0, 10):
                d.line((x + lx, yy + 42, x + lx + sway, yy + 55), fill=accent, width=3)
        elif archetype == 7:  # wheel drone
            r = 15 + (seed % 5)
            d.ellipse((x - r, yy + 20 - r, x + r, yy + 20 + r), fill=outline)
            d.ellipse((x - r + 4, yy + 24 - r, x + r - 4, yy + 16 + r), fill=primary)
            for a in range(0, 360, 60):
                ang = math.radians(a + i * 18)
                d.line((x, yy + 20, x + int(math.cos(ang) * r), yy + 20 + int(math.sin(ang) * r)), fill=glow, width=2)
            d.line((x + facing * r, yy + 20, x + facing * (r + 12), yy + 12 + sway), fill=accent, width=3)
        elif archetype == 8:  # mushroom relay
            capw = 15 + (seed % 9)
            d.pieslice((x - capw, yy + 8, x + capw, yy + 36), 180, 360, fill=outline)
            d.pieslice((x - capw + 3, yy + 11, x + capw - 3, yy + 34), 180, 360, fill=accent)
            d.rounded_rectangle((x - 8, yy + 27, x + 8, yy + 51), radius=4, fill=outline)
            d.rounded_rectangle((x - 5, yy + 29, x + 5, yy + 48), radius=3, fill=secondary)
        elif archetype == 9:  # split mask imp
            d.polygon([(x - 18, yy + 15), (x, yy + 4), (x + 18, yy + 15), (x + 14, yy + 43), (x, yy + 52), (x - 14, yy + 43)], fill=outline)
            d.polygon([(x - 14, yy + 17), (x, yy + 8), (x, yy + 48), (x - 10, yy + 40)], fill=primary)
            d.polygon([(x + 14, yy + 17), (x, yy + 8), (x, yy + 48), (x + 10, yy + 40)], fill=secondary)
            d.rectangle((x - 9, yy + 26, x + 9, yy + 29), fill=glow)
        elif archetype == 10:  # tiny train familiar
            d.rounded_rectangle((x - 22, yy + 28, x + 18, yy + 45), radius=3, fill=outline)
            d.rectangle((x - 18, yy + 31, x + 13, yy + 42), fill=primary)
            d.rectangle((x + 2, yy + 18, x + 18, yy + 32), fill=secondary)
            for wx in (x - 12, x + 8):
                d.ellipse((wx - 5, yy + 40, wx + 5, yy + 50), fill=accent)
            d.line((x + 18, yy + 23, x + 25, yy + 15 - pulse), fill=glow, width=2)
        elif archetype == 11:  # manta glider
            d.polygon([(x - 26, yy + 28), (x - 5, yy + 14 + tilt), (x + 26, yy + 28), (x + 5, yy + 40), (x, yy + 52), (x - 5, yy + 40)], fill=outline)
            d.polygon([(x - 18, yy + 29), (x - 3, yy + 19), (x + 18, yy + 29), (x + 3, yy + 37), (x, yy + 45), (x - 3, yy + 37)], fill=primary)
            d.line((x - 12, yy + 31, x + 12, yy + 31), fill=glow, width=2)
        elif archetype == 12:  # book golem
            d.polygon([(x - 18, yy + 17), (x, yy + 22), (x, yy + 50), (x - 18, yy + 45)], fill=outline)
            d.polygon([(x + 18, yy + 17), (x, yy + 22), (x, yy + 50), (x + 18, yy + 45)], fill=outline)
            d.polygon([(x - 14, yy + 21), (x - 2, yy + 24), (x - 2, yy + 45), (x - 14, yy + 42)], fill=secondary)
            d.polygon([(x + 14, yy + 21), (x + 2, yy + 24), (x + 2, yy + 45), (x + 14, yy + 42)], fill=primary)
            d.line((x, yy + 22, x, yy + 50), fill=accent, width=2)
        elif archetype == 13:  # asymmetric key guardian
            d.ellipse((x - 12, yy + 14, x + 12, yy + 38), fill=outline)
            d.ellipse((x - 8, yy + 18, x + 8, yy + 34), fill=primary)
            d.line((x + facing * 9, yy + 27, x + facing * (28 + pulse), yy + 27 + sway), fill=accent, width=5)
            kx0, kx1 = x + facing * 22, x + facing * 31
            d.rectangle((min(kx0, kx1), yy + 20 + sway, max(kx0, kx1), yy + 25 + sway), fill=secondary)
            d.line((x - facing * 9, yy + 35, x - facing * 16, yy + 50), fill=glow, width=3)
        elif archetype == 14:  # bell jellyfish
            d.pieslice((x - 17, yy + 10, x + 17, yy + 44), 180, 360, fill=outline)
            d.pieslice((x - 13, yy + 14, x + 13, yy + 40), 180, 360, fill=primary)
            for n in range(5):
                tx = x - 12 + n * 6
                d.line((tx, yy + 29, tx + ((n + i) % 3) - 1, yy + 51), fill=[secondary, accent, glow][n % 3], width=2)
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
        if spec is None:
            raise SystemExit(f"unknown pet {args.pet}; choices: {', '.join(specs)}")
    dest = hatch(spec, root, codex_home)
    print(dest)


if __name__ == "__main__":
    main()
