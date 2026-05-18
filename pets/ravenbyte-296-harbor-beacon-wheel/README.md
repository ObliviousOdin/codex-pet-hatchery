# Harbor Beacon Wheel

<p align="center">
  <img src="previews/ravenbyte-296-harbor-beacon-wheel-showcase.gif" width="360" alt="Harbor Beacon Wheel stitched multi-motion showcase">
</p>

**A wheel-class Ravenbyte familiar that keeps beacon work moving during long coding runs.**

Harbor Beacon Wheel is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around single-wheel drone with rotating spoke visor, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Harbor Beacon Wheel brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-296-harbor-beacon-wheel-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-296-harbor-beacon-wheel-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-296-harbor-beacon-wheel-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-296-harbor-beacon-wheel-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-296-harbor-beacon-wheel-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-296-harbor-beacon-wheel-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-296-harbor-beacon-wheel-waiting.gif) |
| Running | ![Running](previews/ravenbyte-296-harbor-beacon-wheel-running.gif) |
| Review | ![Review](previews/ravenbyte-296-harbor-beacon-wheel-review.gif) |

Full contact sheet:

![Harbor Beacon Wheel contact sheet](previews/ravenbyte-296-harbor-beacon-wheel-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-296-harbor-beacon-wheel
```

Or from anywhere with Git:

```bash
PET=ravenbyte-296-harbor-beacon-wheel; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-296-harbor-beacon-wheel/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-296-harbor-beacon-wheel-showcase.gif
  ravenbyte-296-harbor-beacon-wheel-idle.gif
  ravenbyte-296-harbor-beacon-wheel-running-right.gif
  ravenbyte-296-harbor-beacon-wheel-running-left.gif
  ravenbyte-296-harbor-beacon-wheel-waving.gif
  ravenbyte-296-harbor-beacon-wheel-jumping.gif
  ravenbyte-296-harbor-beacon-wheel-failed.gif
  ravenbyte-296-harbor-beacon-wheel-waiting.gif
  ravenbyte-296-harbor-beacon-wheel-running.gif
  ravenbyte-296-harbor-beacon-wheel-review.gif
  ravenbyte-296-harbor-beacon-wheel-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from single-wheel drone with rotating spoke visor, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
