# Lumen Latch Manta

<p align="center">
  <img src="previews/ravenbyte-236-lumen-latch-manta-showcase.gif" width="360" alt="Lumen Latch Manta stitched multi-motion showcase">
</p>

**A manta-class Ravenbyte familiar that keeps latch work moving during long coding runs.**

Lumen Latch Manta is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around manta glider bot with quiet night-shift wings, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Lumen Latch Manta brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-236-lumen-latch-manta-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-236-lumen-latch-manta-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-236-lumen-latch-manta-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-236-lumen-latch-manta-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-236-lumen-latch-manta-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-236-lumen-latch-manta-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-236-lumen-latch-manta-waiting.gif) |
| Running | ![Running](previews/ravenbyte-236-lumen-latch-manta-running.gif) |
| Review | ![Review](previews/ravenbyte-236-lumen-latch-manta-review.gif) |

Full contact sheet:

![Lumen Latch Manta contact sheet](previews/ravenbyte-236-lumen-latch-manta-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-236-lumen-latch-manta
```

Or from anywhere with Git:

```bash
PET=ravenbyte-236-lumen-latch-manta; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-236-lumen-latch-manta/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-236-lumen-latch-manta-showcase.gif
  ravenbyte-236-lumen-latch-manta-idle.gif
  ravenbyte-236-lumen-latch-manta-running-right.gif
  ravenbyte-236-lumen-latch-manta-running-left.gif
  ravenbyte-236-lumen-latch-manta-waving.gif
  ravenbyte-236-lumen-latch-manta-jumping.gif
  ravenbyte-236-lumen-latch-manta-failed.gif
  ravenbyte-236-lumen-latch-manta-waiting.gif
  ravenbyte-236-lumen-latch-manta-running.gif
  ravenbyte-236-lumen-latch-manta-review.gif
  ravenbyte-236-lumen-latch-manta-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from manta glider bot with quiet night-shift wings, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
