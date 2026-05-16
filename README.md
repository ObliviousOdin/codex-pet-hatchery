# Codex Pet Hatchery

**Original animated coding pets for Codex-compatible and Open Design pet import workflows.**

This repo packages small, original sprite companions with `pet.json` and `spritesheet.webp` so they can be imported into Open Design via **Settings → Pets → Import Codex sprite**.

The pets are inspired by broad mecha, ninja-robot, and anime-adventure energy, but every pet here uses original names, palettes, silhouettes, and lore. No copyrighted characters, logos, or exact costume designs are copied.

## What ships today

| Pet | Theme | Animation | More |
| --- | --- | --- | --- |
| Kageframe RX-07 | chibi shadow-mecha shinobi with an energy scarf | ![Kageframe RX-07 idle animation](pets/kageframe-rx07/previews/kageframe-rx07-idle.gif) | [Pet README](pets/kageframe-rx07/README.md) |
| Shuriken Byte Zero | black-chrome ninja robot with teal debug drones | ![Shuriken Byte Zero idle animation](pets/shuriken-byte-zero/previews/shuriken-byte-zero-idle.gif) | [Pet README](pets/shuriken-byte-zero/README.md) |

Each pet includes rows for:

- `idle`
- `running-right`
- `running-left`
- `waving`
- `jumping`
- `failed`
- `waiting`
- `running`
- `review`

`running-left` is mirrored from `running-right` only for symmetric pets.

## One-command install

From any machine with Python 3 and Git:

```bash
PET=kageframe-rx07; REPO=https://github.com/ObliviousOdin/codex-pet-hatchery.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Then import the generated sprite package in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Choose:

```text
${CODEX_HOME:-$HOME/.codex}/pets/kageframe-rx07/spritesheet.webp
```

The metadata file is next to it:

```text
${CODEX_HOME:-$HOME/.codex}/pets/kageframe-rx07/pet.json
```

## Hatch a pet manually

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install pillow
python scripts/hatch_pet.py --pet kageframe-rx07 --root .
python scripts/validate_all.py
```

The hatch script performs the deterministic pipeline:

1. stores the intended `$imagegen` prompt in `generated/imagegen-prompt.json`,
2. creates/extracts a base look into `generated/base.png`,
3. composes row strips under `generated/strips/`,
4. builds `spritesheet.webp`,
5. writes `pet.json`,
6. validates dimensions and animation rows,
7. exports contact sheets plus GIF/MP4 previews,
8. packages the pet into `${CODEX_HOME:-$HOME/.codex}/pets/<pet-name>/`.

> Note: this environment currently lacks the image-generation backend key, so the first pet uses the deterministic vector fallback while preserving the imagegen prompt for repeatability.

## Package format

Each pet directory is self-contained:

```text
pets/<pet-name>/
  README.md
  pet.json
  spritesheet.webp
  previews/
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

## Pet ideas queued

Variety matters. Future manual hatches should rotate styles instead of making the same mecha repeatedly:

- **Ronin Build Fox** — fox-masked build guardian with servo tails and CI charms.
- **Compiler Oni Mini** — tiny red oni robot that bonks failing tests with a foam kanabo.
- **Moonbase Tanuki Dev** — round tanuki rover with a leaf-shaped antenna and sleepy review mode.
- **Patchwork Karakuri Cat** — wooden clockwork cat automaton with brass whiskers.
- **Nebula Courier Mech** — courier robot with launch-thruster running animations.
- **Lotus Firewall Monk** — meditating cyber-monk bot with shield-petal review frames.

## Development and verification

```bash
python scripts/hatch_pet.py --pet kageframe-rx07 --root .
python scripts/validate_all.py
git diff --check
```

Before publishing a new pet, check:

- `pet.json` exists and points to `spritesheet.webp`.
- All required animation rows exist.
- The root README links to the pet README and shows an animation.
- GIF/MP4 previews are generated.
- The pet installs into `${CODEX_HOME:-$HOME/.codex}/pets/<pet-name>/`.
- No generated art claims to be a copyrighted character.

## Project status

Early hatchery. The first pet is usable now. New pets are added intentionally through manual hatches and reviewable commits.
