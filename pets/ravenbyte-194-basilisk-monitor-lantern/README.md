# Basilisk Monitor Lantern

<p align="center">
  <img src="previews/ravenbyte-194-basilisk-monitor-lantern-showcase.gif" width="360" alt="Basilisk Monitor Lantern stitched multi-motion showcase">
</p>

**A lantern-class Ravenbyte familiar that keeps monitor work moving during long coding runs.**

Basilisk Monitor Lantern is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around floating lantern stack spirit with tiny build lights, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Basilisk Monitor Lantern brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-194-basilisk-monitor-lantern-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-194-basilisk-monitor-lantern-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-194-basilisk-monitor-lantern-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-194-basilisk-monitor-lantern-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-194-basilisk-monitor-lantern-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-194-basilisk-monitor-lantern-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-194-basilisk-monitor-lantern-waiting.gif) |
| Running | ![Running](previews/ravenbyte-194-basilisk-monitor-lantern-running.gif) |
| Review | ![Review](previews/ravenbyte-194-basilisk-monitor-lantern-review.gif) |

Full contact sheet:

![Basilisk Monitor Lantern contact sheet](previews/ravenbyte-194-basilisk-monitor-lantern-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-194-basilisk-monitor-lantern
```

Or from anywhere with Git:

```bash
PET=ravenbyte-194-basilisk-monitor-lantern; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-194-basilisk-monitor-lantern/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-194-basilisk-monitor-lantern-showcase.gif
  ravenbyte-194-basilisk-monitor-lantern-idle.gif
  ravenbyte-194-basilisk-monitor-lantern-running-right.gif
  ravenbyte-194-basilisk-monitor-lantern-running-left.gif
  ravenbyte-194-basilisk-monitor-lantern-waving.gif
  ravenbyte-194-basilisk-monitor-lantern-jumping.gif
  ravenbyte-194-basilisk-monitor-lantern-failed.gif
  ravenbyte-194-basilisk-monitor-lantern-waiting.gif
  ravenbyte-194-basilisk-monitor-lantern-running.gif
  ravenbyte-194-basilisk-monitor-lantern-review.gif
  ravenbyte-194-basilisk-monitor-lantern-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from floating lantern stack spirit with tiny build lights, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
