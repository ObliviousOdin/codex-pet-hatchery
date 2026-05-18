# Xenon Query Wheel

<p align="center">
  <img src="previews/ravenbyte-280-xenon-query-wheel-showcase.gif" width="360" alt="Xenon Query Wheel stitched multi-motion showcase">
</p>

**A wheel-class Ravenbyte familiar that keeps query work moving during long coding runs.**

Xenon Query Wheel is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around single-wheel drone with rotating spoke visor, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Xenon Query Wheel brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-280-xenon-query-wheel-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-280-xenon-query-wheel-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-280-xenon-query-wheel-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-280-xenon-query-wheel-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-280-xenon-query-wheel-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-280-xenon-query-wheel-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-280-xenon-query-wheel-waiting.gif) |
| Running | ![Running](previews/ravenbyte-280-xenon-query-wheel-running.gif) |
| Review | ![Review](previews/ravenbyte-280-xenon-query-wheel-review.gif) |

Full contact sheet:

![Xenon Query Wheel contact sheet](previews/ravenbyte-280-xenon-query-wheel-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-280-xenon-query-wheel
```

Or from anywhere with Git:

```bash
PET=ravenbyte-280-xenon-query-wheel; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-280-xenon-query-wheel/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-280-xenon-query-wheel-showcase.gif
  ravenbyte-280-xenon-query-wheel-idle.gif
  ravenbyte-280-xenon-query-wheel-running-right.gif
  ravenbyte-280-xenon-query-wheel-running-left.gif
  ravenbyte-280-xenon-query-wheel-waving.gif
  ravenbyte-280-xenon-query-wheel-jumping.gif
  ravenbyte-280-xenon-query-wheel-failed.gif
  ravenbyte-280-xenon-query-wheel-waiting.gif
  ravenbyte-280-xenon-query-wheel-running.gif
  ravenbyte-280-xenon-query-wheel-review.gif
  ravenbyte-280-xenon-query-wheel-contact-sheet.png
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
