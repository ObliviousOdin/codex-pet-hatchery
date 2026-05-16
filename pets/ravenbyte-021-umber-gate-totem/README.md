# Umber Gate Totem

<p align="center">
  <img src="previews/ravenbyte-021-umber-gate-totem-showcase.gif" width="360" alt="Umber Gate Totem stitched multi-motion showcase">
</p>

**A totem-class Ravenbyte familiar that keeps gate work moving during long coding runs.**

Umber Gate Totem is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around tall shrine totem bot with stacked status bars, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Umber Gate Totem brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-021-umber-gate-totem-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-021-umber-gate-totem-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-021-umber-gate-totem-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-021-umber-gate-totem-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-021-umber-gate-totem-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-021-umber-gate-totem-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-021-umber-gate-totem-waiting.gif) |
| Running | ![Running](previews/ravenbyte-021-umber-gate-totem-running.gif) |
| Review | ![Review](previews/ravenbyte-021-umber-gate-totem-review.gif) |

Full contact sheet:

![Umber Gate Totem contact sheet](previews/ravenbyte-021-umber-gate-totem-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-021-umber-gate-totem
```

Or from anywhere with Git:

```bash
PET=ravenbyte-021-umber-gate-totem; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-021-umber-gate-totem/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-021-umber-gate-totem-showcase.gif
  ravenbyte-021-umber-gate-totem-idle.gif
  ravenbyte-021-umber-gate-totem-running-right.gif
  ravenbyte-021-umber-gate-totem-running-left.gif
  ravenbyte-021-umber-gate-totem-waving.gif
  ravenbyte-021-umber-gate-totem-jumping.gif
  ravenbyte-021-umber-gate-totem-failed.gif
  ravenbyte-021-umber-gate-totem-waiting.gif
  ravenbyte-021-umber-gate-totem-running.gif
  ravenbyte-021-umber-gate-totem-review.gif
  ravenbyte-021-umber-gate-totem-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from tall shrine totem bot with stacked status bars, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
