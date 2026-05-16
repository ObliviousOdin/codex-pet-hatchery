#!/usr/bin/env python3
"""Batch-hatch deterministic Ravenbyte Familiars until the collection passes a target count.

This is intentionally separate from the recurring one-pet cron path. It creates
only missing generated familiars and never deletes existing repo packages.
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

# Keep large surge hatches practical. GIFs/showcases remain generated and are
# validated; MP4s can be requested explicitly for smaller release runs.
os.environ.setdefault("RAVENBYTE_RENDER_MP4", "0")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from hatch_pet import PetSpec, hatch  # noqa: E402

PALETTE = [
    ("#111827", "#e5e7eb", "#f59e0b", "#22d3ee"),
    ("#1e1b4b", "#ddd6fe", "#fb7185", "#a78bfa"),
    ("#052e2b", "#ccfbf1", "#facc15", "#2dd4bf"),
    ("#2a160f", "#ffedd5", "#f97316", "#fef08a"),
    ("#0f172a", "#dbeafe", "#38bdf8", "#818cf8"),
    ("#1f2937", "#f5f5f4", "#ef4444", "#fbbf24"),
    ("#3b0764", "#fae8ff", "#d946ef", "#67e8f9"),
    ("#172554", "#ecfeff", "#14b8a6", "#fde68a"),
    ("#312e81", "#eef2ff", "#f472b6", "#c4b5fd"),
    ("#132a13", "#f7fee7", "#84cc16", "#bef264"),
]

ADJECTIVES = [
    "Ash", "Basilisk", "Cipher", "Dawn", "Ember", "Frost", "Glyph", "Harbor",
    "Ion", "Jade", "Keystone", "Lumen", "Morrow", "Nimbus", "Obsidian", "Prairie",
    "Quartz", "Rune", "Signal", "Tundra", "Umber", "Violet", "Warden", "Xenon",
    "Yonder", "Zephyr", "Brass", "Cobalt", "Drift", "Echo", "Fable", "Grove",
]

ROLES = [
    "Audit", "Beacon", "Cache", "Delta", "Engine", "Forge", "Graph", "Harvester",
    "Index", "Junction", "Kernel", "Latch", "Monitor", "Nexus", "Oracle", "Patch",
    "Query", "Relay", "Sentinel", "Triage", "Uplink", "Vector", "Widget", "Xray",
    "Yield", "Zenith", "Bundle", "Circuit", "Diff", "Event", "Flux", "Gate",
]

FORMS = [
    "Beetle", "Lantern", "Crawler", "Kite", "Totem", "Serpent", "Crystal", "Wheel",
    "Mushroom", "Mask", "Train", "Manta", "Book", "Key", "Jelly", "Rabbit",
]

THEMES = {
    "Beetle": "antenna beetle slab robot with code-shell wing plates",
    "Lantern": "floating lantern stack spirit with tiny build lights",
    "Crawler": "multi-leg crawler bridge familiar for dependency paths",
    "Kite": "crescent kite drone with asymmetric review wing",
    "Totem": "tall shrine totem bot with stacked status bars",
    "Serpent": "serpent ribbon automaton that coils around flaky tests",
    "Crystal": "crystal tripod familiar with facet armor and lint sparks",
    "Wheel": "single-wheel drone with rotating spoke visor",
    "Mushroom": "mushroom relay bot with soft cap and signal motes",
    "Mask": "split-mask imp familiar with two-tone review face",
    "Train": "tiny train familiar hauling hotfix cargo",
    "Manta": "manta glider bot with quiet night-shift wings",
    "Book": "open-book golem companion with diff-page armor",
    "Key": "asymmetric key guardian with unlock beam",
    "Jelly": "bell jellyfish familiar with dangling trace tendrils",
    "Rabbit": "scaffold rabbit bot with long signal ears",
}


def slugify(parts: list[str], number: int) -> str:
    stem = "-".join(p.lower() for p in parts)
    return f"ravenbyte-{number:03d}-{stem}"


def generated_specs(total: int = 256) -> list[PetSpec]:
    specs: list[PetSpec] = []
    for n in range(1, total + 1):
        adjective = ADJECTIVES[(n - 1) % len(ADJECTIVES)]
        role = ROLES[((n - 1) // len(ADJECTIVES) + n * 3) % len(ROLES)]
        form = FORMS[(n - 1) % len(FORMS)]
        slug = slugify([adjective, role, form], n)
        display = f"{adjective} {role} {form}"
        palette = PALETTE[(n - 1) % len(PALETTE)]
        specs.append(
            PetSpec(
                slug=slug,
                display_name=display,
                tagline=f"A {form.lower()}-class Ravenbyte familiar that keeps {role.lower()} work moving during long coding runs.",
                theme=THEMES[form],
                primary=palette[0],
                secondary=palette[1],
                accent=palette[2],
                glow=palette[3],
                symmetric=False,
            )
        )
    return specs


def pet_count(root: Path) -> int:
    pets = root / "pets"
    if not pets.exists():
        return 0
    return sum(1 for p in pets.iterdir() if p.is_dir() and (p / "pet.json").exists())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=int, default=205, help="minimum total pet count to reach")
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--codex-home", default=str(Path.home() / ".codex"))
    parser.add_argument("--limit", type=int, default=None, help="max number to hatch in this run")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    codex_home = Path(args.codex_home).expanduser().resolve()
    before = pet_count(root)
    needed = max(args.target - before, 0)
    if args.limit is not None:
        needed = min(needed, args.limit)
    print(f"current_pet_count={before} target={args.target} to_hatch={needed}")
    if needed == 0:
        return

    existing = {p.name for p in (root / "pets").iterdir() if p.is_dir()} if (root / "pets").exists() else set()
    hatched = []
    for spec in generated_specs(max(args.target + 64, 256)):
        if len(hatched) >= needed:
            break
        if spec.slug in existing:
            continue
        dest = hatch(spec, root, codex_home)
        existing.add(spec.slug)
        hatched.append(spec.slug)
        print(f"hatched {len(hatched)}/{needed}: {spec.slug} -> {dest}")

    after = pet_count(root)
    print(f"final_pet_count={after}")
    if after < args.target:
        raise SystemExit(f"only reached {after}; target was {args.target}")

    subprocess.run([sys.executable, str(root / "scripts" / "render_readme_hero.py")], cwd=root, check=True)
    subprocess.run([sys.executable, str(root / "scripts" / "sync_readme.py")], cwd=root, check=True)
    print("synced README and hero")


if __name__ == "__main__":
    main()
