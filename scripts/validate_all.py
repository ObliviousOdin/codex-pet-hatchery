#!/usr/bin/env python3
"""Validate every pet package in the repository."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from PIL import Image

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
    return errors


def main() -> int:
    pets = sorted((ROOT / "pets").iterdir()) if (ROOT / "pets").exists() else []
    failures = 0
    for pet in pets:
        if not pet.is_dir():
            continue
        errors = validate_pet(pet)
        if errors:
            failures += 1
            print(f"FAIL {pet.name}")
            for err in errors:
                print(f"  - {err}")
        else:
            print(f"OK {pet.name}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
