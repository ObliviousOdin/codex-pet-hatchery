#!/usr/bin/env python3
"""Synchronize README.md from the current familiar packages.

Keeps the public homepage honest as the recurring hatch job adds pets. The card
grid intentionally uses stitched showcase GIFs rather than single idle loops.
"""

from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAUNCH_ORDER = [
    "kageframe-rx07",
    "shuriken-byte-zero",
    "ronin-build-fox",
    "compiler-oni-mini",
    "moonbase-tanuki-dev",
    "karakuri-patch-cat",
]


def pet_rows() -> list[tuple[str, str, str]]:
    pets = []
    for d in sorted((ROOT / "pets").iterdir()):
        if not d.is_dir() or not (d / "pet.json").exists():
            continue
        data = json.loads((d / "pet.json").read_text())
        pets.append((d.name, data.get("displayName", d.name), data.get("description", "")))
    rank = {slug: i for i, slug in enumerate(LAUNCH_ORDER)}
    return sorted(pets, key=lambda item: rank.get(item[0], 999))


def pet_card(slug: str, display: str, desc: str) -> str:
    return f'''<td width="33%" align="center" valign="top">
  <a href="pets/{slug}/README.md"><img src="pets/{slug}/previews/{slug}-showcase.gif" width="240" alt="{html.escape(display)} stitched multi-motion showcase"></a><br>
  <strong>{html.escape(display)}</strong><br>
  <sub>{html.escape(desc)}</sub><br>
  <a href="pets/{slug}/README.md">README</a> · <a href="pets/{slug}/spritesheet.webp">spritesheet</a>
</td>'''


def pet_grid(pets: list[tuple[str, str, str]]) -> str:
    rows = []
    for i in range(0, len(pets), 3):
        rows.append("<tr>\n" + "\n".join(pet_card(*p) for p in pets[i : i + 3]) + "\n</tr>")
    return "<table>\n" + "\n".join(rows) + "\n</table>"


def render() -> str:
    return f'''<p align="center">
  <img src="assets/hero/ravenbyte-familiars-hero.gif" width="100%" alt="Ravenbyte Familiars hero animation: tiny robot companions working, reviewing, and rejoicing around a minimalist industrial console">
</p>

<p align="center">
  <strong>Tiny mythic coding companions for Codex-compatible and Open Design pet import workflows.</strong><br>
  Original animated familiars packaged with <code>pet.json</code> and <code>spritesheet.webp</code>.
</p>

<p align="center">
  <a href="#familiars">Familiars</a> ·
  <a href="#one-command-install">Install</a> ·
  <a href="#package-format">Package format</a> ·
  <a href="#variation-standard">Variation standard</a> ·
  <a href="#development-and-verification">Development</a>
</p>

---

## What this is

**Ravenbyte Familiars** is an **ObliviousOdin** sprite collection for long coding nights: raven-dark, rune-lit, wild-hearted little machines and spirits that can be imported through **Settings → Pets → Import Codex sprite**.

The repo is intentionally practical: each familiar ships as a complete import package, with animation previews, a per-familiar README, deterministic generation artifacts, and validation scripts.

## Design direction

The header animation is the visual north star: calm industrial product discipline, precise panels, useful machines, and tiny companions that make the workbench feel alive. The collection should feel premium and restrained, not childish or corporate.

| Principle | Meaning here |
| --- | --- |
| Useful first | Every familiar has a real importable package, not just preview art. |
| Less, but better | Strong silhouettes, few accents, readable motion at `64×64`. |
| More than idle | README cards use stitched showcase GIFs that move through idle, run, jump, review, fail, and wave states. |
| Original mythology | Broad mecha/spirit/adventure energy, no copied characters or logos. |
| Built to verify | `pet.json`, spritesheet dimensions, previews, showcase GIFs, and visual variation are checked before publishing. |

## Brand palette

| Token | Hex | Use |
| --- | --- | --- |
| Void Black | `#080A0F` | deep background |
| Raven Ink | `#111827` | panels and outlines |
| Bone White | `#E8E0D0` | readable text and masks |
| Rune Gold | `#D6A84F` | mythic accent |
| Plasma Cyan | `#62E6FF` | code energy and motion |
| Signal Ember | `#FF7A45` | warnings, failed states, sparks |

## Familiars

Each card below is a **stitched multi-motion showcase**, not a single idle loop. It cycles through several real rows from the import spritesheet so the README better reflects how each familiar behaves in Open Design.

{pet_grid(pet_rows())}

Each familiar includes the same import-critical animation states:

<table>
<tr>
<td><code>idle</code></td><td><code>running-right</code></td><td><code>running-left</code></td>
<td><code>waving</code></td><td><code>jumping</code></td><td><code>failed</code></td>
<td><code>waiting</code></td><td><code>running</code></td><td><code>review</code></td>
</tr>
</table>

`running-left` is mirrored from `running-right` only for genuinely symmetric familiars.

## One-command install

From any machine with Python 3 and Git:

```bash
PET=kageframe-rx07; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${{CODEX_HOME:-$HOME/.codex}}/pets/$PET"
```

Then import the generated sprite package in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Choose:

```text
${{CODEX_HOME:-$HOME/.codex}}/pets/kageframe-rx07/spritesheet.webp
```

The metadata file is next to it:

```text
${{CODEX_HOME:-$HOME/.codex}}/pets/kageframe-rx07/pet.json
```

## Hatch a familiar manually

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/hatch_pet.py --pet ronin-build-fox --root .
python scripts/validate_all.py
git diff --check
```

The hatch script performs the deterministic pipeline:

1. stores the intended image-generation prompt in `generated/imagegen-prompt.json`,
2. creates or extracts a base look into `generated/base.png`,
3. composes row strips under `generated/strips/`,
4. builds `spritesheet.webp`,
5. writes `pet.json`,
6. validates dimensions and animation rows,
7. exports contact sheets plus per-state GIF/MP4 previews,
8. renders a stitched multi-motion `previews/<pet>-showcase.gif`,
9. packages the familiar into `${{CODEX_HOME:-$HOME/.codex}}/pets/<pet-name>/`.

To regenerate README media after adding familiars:

```bash
python scripts/render_showcase_gifs.py
python scripts/render_readme_hero.py
python scripts/sync_readme.py
```

## Package format

Each familiar directory is self-contained:

```text
pets/<pet-name>/
  README.md
  pet.json
  spritesheet.webp
  previews/
    <pet-name>-showcase.gif
    <pet-name>-contact-sheet.png
    <pet-name>-idle.gif
    ...
  generated/
    base.png
    imagegen-prompt.json
    strips/
      idle.png
      running-right.png
      running-left.png
      waving.png
      jumping.png
      failed.png
      waiting.png
      running.png
      review.png
```

The current spritesheet layout is `384×576`: six `64×64` frames per row and nine animation rows.

## Variation standard

A new familiar should not look like the previous familiar with different colors. Before publishing, check:

- silhouette overlap against existing familiars is not too high,
- head/body plan changes materially,
- motion language changes materially,
- at least one signature prop or creature feature is obvious at `64×64`,
- failed/waiting/review states are readable,
- README showcase cycles through multiple visibly different motions,
- no generated art claims to be a copyrighted character.

`python scripts/validate_all.py` includes a silhouette-overlap check and requires stitched showcase GIFs to catch clone-like or under-presented pets.

## Familiar ideas queued

Future hatches should rotate body plans instead of making the same mecha repeatedly:

- **Nebula Courier Mech** — courier robot with launch-thruster running animations.
- **Lotus Firewall Monk** — meditating cyber-monk bot with shield-petal review frames.
- **Samurai Cache Crab** — side-stepping armor crab with cache-crystal claws.
- **Ramen Debug Drone** — noodle-shop hover drone that serves hot fixes in a tiny bowl.
- **Origami Test Heron** — folded-paper cyber-heron that pecks flaky tests.

## Development and verification

```bash
python scripts/validate_all.py
python scripts/render_showcase_gifs.py
python scripts/render_readme_hero.py
python scripts/sync_readme.py
git diff --check
```

Before publishing a new familiar, check:

- `pet.json` exists and points to `spritesheet.webp`.
- All required animation rows exist.
- The root README links to the familiar README and shows aligned stitched showcase GIFs.
- GIF/MP4 previews are generated.
- The familiar installs into `${{CODEX_HOME:-$HOME/.codex}}/pets/<pet-name>/`.
- The new familiar is structurally distinct from earlier familiars.

## Project status

Early collection. The current familiars are usable now. New familiars are added as reviewable commits with validated packages.
'''


def main() -> None:
    (ROOT / "README.md").write_text(render())
    print("README.md")


if __name__ == "__main__":
    main()
