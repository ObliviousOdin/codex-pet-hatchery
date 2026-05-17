# Xenon Patch Wheel

<p align="center">
  <img src="previews/ravenbyte-248-xenon-patch-wheel-showcase.gif" width="360" alt="Xenon Patch Wheel stitched multi-motion showcase">
</p>

**A wheel-class Ravenbyte familiar that keeps patch work moving during long coding runs.**

Xenon Patch Wheel is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around single-wheel drone with rotating spoke visor, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Xenon Patch Wheel brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-248-xenon-patch-wheel-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-248-xenon-patch-wheel-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-248-xenon-patch-wheel-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-248-xenon-patch-wheel-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-248-xenon-patch-wheel-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-248-xenon-patch-wheel-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-248-xenon-patch-wheel-waiting.gif) |
| Running | ![Running](previews/ravenbyte-248-xenon-patch-wheel-running.gif) |
| Review | ![Review](previews/ravenbyte-248-xenon-patch-wheel-review.gif) |

Full contact sheet:

![Xenon Patch Wheel contact sheet](previews/ravenbyte-248-xenon-patch-wheel-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-248-xenon-patch-wheel
```

Or from anywhere with Git:

```bash
PET=ravenbyte-248-xenon-patch-wheel; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-248-xenon-patch-wheel/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-248-xenon-patch-wheel-showcase.gif
  ravenbyte-248-xenon-patch-wheel-idle.gif
  ravenbyte-248-xenon-patch-wheel-running-right.gif
  ravenbyte-248-xenon-patch-wheel-running-left.gif
  ravenbyte-248-xenon-patch-wheel-waving.gif
  ravenbyte-248-xenon-patch-wheel-jumping.gif
  ravenbyte-248-xenon-patch-wheel-failed.gif
  ravenbyte-248-xenon-patch-wheel-waiting.gif
  ravenbyte-248-xenon-patch-wheel-running.gif
  ravenbyte-248-xenon-patch-wheel-review.gif
  ravenbyte-248-xenon-patch-wheel-contact-sheet.png
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
