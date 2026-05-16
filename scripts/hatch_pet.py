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
import json
import math
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw

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
        x = 32
        d.polygon([(x - 12, y + 20), (x + 8, y + 14), (x + 15, y + 32), (x - 7, y + 43)], fill=outline)
        d.polygon([(x - 9, y + 22), (x + 7, y + 17), (x + 12, y + 31), (x - 5, y + 40)], fill=secondary)
        d.polygon([(x + 5, y + 15), (x + 24, y + 18), (x + 7, y + 22)], fill=accent)
        d.line((x - 4, y + 41, x - 9 - run, y + 53), fill=primary, width=3)
        d.line((x + 5, y + 39, x + 11 + run, y + 53), fill=primary, width=3)
        rect((x + 4, y + 21, x + 7, y + 23), glow)
        if anim == "waving":
            d.polygon([(x - 8, y + 27), (x - 24, y + 16 + i % 3), (x - 12, y + 35)], fill=hex_to_rgba(glow, 170))
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

        # MP4 via ffmpeg from GIF, best-effort.
        mp4_path = previews_dir / f"{spec.slug}-{anim}.mp4"
        try:
            subprocess.run([
                "ffmpeg", "-y", "-v", "error", "-i", str(gif_path),
                "-movflags", "faststart", "-pix_fmt", "yuv420p", "-vf", "scale=256:256:flags=neighbor",
                str(mp4_path),
            ], check=True)
        except Exception:
            pass


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
