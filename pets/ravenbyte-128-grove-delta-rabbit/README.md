# Grove Delta Rabbit

<p align="center">
  <img src="previews/ravenbyte-128-grove-delta-rabbit-showcase.gif" width="360" alt="Grove Delta Rabbit stitched multi-motion showcase">
</p>

**A rabbit-class Ravenbyte familiar that keeps delta work moving during long coding runs.**

Grove Delta Rabbit is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around scaffold rabbit bot with long signal ears, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Grove Delta Rabbit brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-128-grove-delta-rabbit-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-128-grove-delta-rabbit-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-128-grove-delta-rabbit-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-128-grove-delta-rabbit-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-128-grove-delta-rabbit-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-128-grove-delta-rabbit-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-128-grove-delta-rabbit-waiting.gif) |
| Running | ![Running](previews/ravenbyte-128-grove-delta-rabbit-running.gif) |
| Review | ![Review](previews/ravenbyte-128-grove-delta-rabbit-review.gif) |

Full contact sheet:

![Grove Delta Rabbit contact sheet](previews/ravenbyte-128-grove-delta-rabbit-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-128-grove-delta-rabbit
```

Or from anywhere with Git:

```bash
PET=ravenbyte-128-grove-delta-rabbit; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-128-grove-delta-rabbit/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-128-grove-delta-rabbit-showcase.gif
  ravenbyte-128-grove-delta-rabbit-idle.gif
  ravenbyte-128-grove-delta-rabbit-running-right.gif
  ravenbyte-128-grove-delta-rabbit-running-left.gif
  ravenbyte-128-grove-delta-rabbit-waving.gif
  ravenbyte-128-grove-delta-rabbit-jumping.gif
  ravenbyte-128-grove-delta-rabbit-failed.gif
  ravenbyte-128-grove-delta-rabbit-waiting.gif
  ravenbyte-128-grove-delta-rabbit-running.gif
  ravenbyte-128-grove-delta-rabbit-review.gif
  ravenbyte-128-grove-delta-rabbit-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from scaffold rabbit bot with long signal ears, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
