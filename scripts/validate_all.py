#!/usr/bin/env python3
"""Validate every pet package in the repository."""
from __future__ import annotations

import json
import sys
from itertools import combinations
from pathlib import Path
from PIL import Image, ImageSequence

ROOT = Path(__file__).resolve().parents[1]
ANIMS = ["idle", "running-right", "running-left", "waving", "jumping", "failed", "waiting", "running", "review"]


def validate_pet(pet_dir: Path) -> list[str]:
    errors = []
    pj = pet_dir / "pet.json"
    ss = pet_dir / "spritesheet.webp"
    if not pj.exists():
        errors.append("missing pet.json")
        return errors
    if not ss.exists():
        errors.append("missing spritesheet.webp")
        return errors
    try:
        data = json.loads(pj.read_text())
    except Exception as exc:
        return [f"invalid pet.json: {exc}"]
    for key in ["name", "displayName", "frameWidth", "frameHeight", "framesPerRow", "spritesheet", "animations"]:
        if key not in data:
            errors.append(f"missing {key}")
    try:
        img = Image.open(ss)
        expected = (int(data.get("frameWidth", 0)) * int(data.get("framesPerRow", 0)), int(data.get("frameHeight", 0)) * len(data.get("animations", [])))
        if img.size != expected:
            errors.append(f"spritesheet size {img.size} != {expected}")
    except Exception as exc:
        errors.append(f"bad spritesheet: {exc}")
    names = [a.get("name") for a in data.get("animations", [])]
    if names != ANIMS:
        errors.append(f"animation rows {names} != {ANIMS}")

    showcase = pet_dir / "previews" / f"{pet_dir.name}-showcase.gif"
    if not showcase.exists():
        errors.append("missing stitched showcase GIF")
    else:
        try:
            gif = Image.open(showcase)
            frame_count = sum(1 for _ in ImageSequence.Iterator(gif))
            if gif.size[0] < 300 or gif.size[1] < 360:
                errors.append(f"showcase GIF too small: {gif.size}")
            if frame_count < 30:
                errors.append(f"showcase GIF has too few frames: {frame_count}")
        except Exception as exc:
            errors.append(f"bad showcase GIF: {exc}")
    return errors


def silhouette_mask(pet_dir: Path) -> set[tuple[int, int]]:
    """Return occupied pixels for the base pose, used to prevent clone-like pets."""
    source = pet_dir / "generated" / "base.png"
    if not source.exists():
        source = pet_dir / "spritesheet.webp"
    img = Image.open(source).convert("RGBA")
    if img.width != 64 or img.height != 64:
        img = img.crop((0, 0, 64, 64))
    return {(x, y) for y in range(img.height) for x in range(img.width) if img.getpixel((x, y))[3] > 24}


def silhouette_iou(a: set[tuple[int, int]], b: set[tuple[int, int]]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def main() -> int:
    pets = [p for p in sorted((ROOT / "pets").iterdir()) if p.is_dir()] if (ROOT / "pets").exists() else []
    failures = 0
    for pet in pets:
        errors = validate_pet(pet)
        if errors:
            failures += 1
            print(f"FAIL {pet.name}")
            for err in errors:
                print(f"  - {err}")
        else:
            print(f"OK {pet.name}")

    masks = {pet.name: silhouette_mask(pet) for pet in pets}
    for left, right in combinations(pets, 2):
        iou = silhouette_iou(masks[left.name], masks[right.name])
        if iou > 0.78:
            failures += 1
            print(f"FAIL visual-variation {left.name} vs {right.name}")
            print(f"  - silhouette overlap {iou:.2f} is too high; pets must not be palette swaps")
        else:
            print(f"OK visual-variation {left.name} vs {right.name}: {iou:.2f}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
