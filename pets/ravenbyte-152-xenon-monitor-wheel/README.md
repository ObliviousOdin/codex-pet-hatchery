# Xenon Monitor Wheel

<p align="center">
  <img src="previews/ravenbyte-152-xenon-monitor-wheel-showcase.gif" width="360" alt="Xenon Monitor Wheel stitched multi-motion showcase">
</p>

**A wheel-class Ravenbyte familiar that keeps monitor work moving during long coding runs.**

Xenon Monitor Wheel is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around single-wheel drone with rotating spoke visor, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Xenon Monitor Wheel brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-152-xenon-monitor-wheel-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-152-xenon-monitor-wheel-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-152-xenon-monitor-wheel-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-152-xenon-monitor-wheel-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-152-xenon-monitor-wheel-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-152-xenon-monitor-wheel-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-152-xenon-monitor-wheel-waiting.gif) |
| Running | ![Running](previews/ravenbyte-152-xenon-monitor-wheel-running.gif) |
| Review | ![Review](previews/ravenbyte-152-xenon-monitor-wheel-review.gif) |

Full contact sheet:

![Xenon Monitor Wheel contact sheet](previews/ravenbyte-152-xenon-monitor-wheel-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-152-xenon-monitor-wheel
```

Or from anywhere with Git:

```bash
PET=ravenbyte-152-xenon-monitor-wheel; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-152-xenon-monitor-wheel/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-152-xenon-monitor-wheel-showcase.gif
  ravenbyte-152-xenon-monitor-wheel-idle.gif
  ravenbyte-152-xenon-monitor-wheel-running-right.gif
  ravenbyte-152-xenon-monitor-wheel-running-left.gif
  ravenbyte-152-xenon-monitor-wheel-waving.gif
  ravenbyte-152-xenon-monitor-wheel-jumping.gif
  ravenbyte-152-xenon-monitor-wheel-failed.gif
  ravenbyte-152-xenon-monitor-wheel-waiting.gif
  ravenbyte-152-xenon-monitor-wheel-running.gif
  ravenbyte-152-xenon-monitor-wheel-review.gif
  ravenbyte-152-xenon-monitor-wheel-contact-sheet.png
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
