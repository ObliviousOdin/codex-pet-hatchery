# Obsidian Yield Jelly

<p align="center">
  <img src="previews/ravenbyte-367-obsidian-yield-jelly-showcase.gif" width="360" alt="Obsidian Yield Jelly stitched multi-motion showcase">
</p>

**A jelly-class Ravenbyte familiar that keeps yield work moving during long coding runs.**

Obsidian Yield Jelly is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around bell jellyfish familiar with dangling trace tendrils, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Obsidian Yield Jelly brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-367-obsidian-yield-jelly-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-367-obsidian-yield-jelly-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-367-obsidian-yield-jelly-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-367-obsidian-yield-jelly-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-367-obsidian-yield-jelly-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-367-obsidian-yield-jelly-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-367-obsidian-yield-jelly-waiting.gif) |
| Running | ![Running](previews/ravenbyte-367-obsidian-yield-jelly-running.gif) |
| Review | ![Review](previews/ravenbyte-367-obsidian-yield-jelly-review.gif) |

Full contact sheet:

![Obsidian Yield Jelly contact sheet](previews/ravenbyte-367-obsidian-yield-jelly-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-367-obsidian-yield-jelly
```

Or from anywhere with Git:

```bash
PET=ravenbyte-367-obsidian-yield-jelly; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-367-obsidian-yield-jelly/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-367-obsidian-yield-jelly-showcase.gif
  ravenbyte-367-obsidian-yield-jelly-idle.gif
  ravenbyte-367-obsidian-yield-jelly-running-right.gif
  ravenbyte-367-obsidian-yield-jelly-running-left.gif
  ravenbyte-367-obsidian-yield-jelly-waving.gif
  ravenbyte-367-obsidian-yield-jelly-jumping.gif
  ravenbyte-367-obsidian-yield-jelly-failed.gif
  ravenbyte-367-obsidian-yield-jelly-waiting.gif
  ravenbyte-367-obsidian-yield-jelly-running.gif
  ravenbyte-367-obsidian-yield-jelly-review.gif
  ravenbyte-367-obsidian-yield-jelly-contact-sheet.png
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
- Symmetric design: no
- `running-left`: drawn as a separate row because this familiar has side-specific details
- Author: `ObliviousOdin`

## Design notes

The design is intentionally original. It uses broad visual language from bell jellyfish familiar with dangling trace tendrils, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
