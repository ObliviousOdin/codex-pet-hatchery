# Prairie Uplink Rabbit

<p align="center">
  <img src="previews/ravenbyte-144-prairie-uplink-rabbit-showcase.gif" width="360" alt="Prairie Uplink Rabbit stitched multi-motion showcase">
</p>

**A rabbit-class Ravenbyte familiar that keeps uplink work moving during long coding runs.**

Prairie Uplink Rabbit is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around scaffold rabbit bot with long signal ears, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Prairie Uplink Rabbit brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-144-prairie-uplink-rabbit-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-144-prairie-uplink-rabbit-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-144-prairie-uplink-rabbit-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-144-prairie-uplink-rabbit-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-144-prairie-uplink-rabbit-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-144-prairie-uplink-rabbit-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-144-prairie-uplink-rabbit-waiting.gif) |
| Running | ![Running](previews/ravenbyte-144-prairie-uplink-rabbit-running.gif) |
| Review | ![Review](previews/ravenbyte-144-prairie-uplink-rabbit-review.gif) |

Full contact sheet:

![Prairie Uplink Rabbit contact sheet](previews/ravenbyte-144-prairie-uplink-rabbit-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-144-prairie-uplink-rabbit
```

Or from anywhere with Git:

```bash
PET=ravenbyte-144-prairie-uplink-rabbit; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-144-prairie-uplink-rabbit/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-144-prairie-uplink-rabbit-showcase.gif
  ravenbyte-144-prairie-uplink-rabbit-idle.gif
  ravenbyte-144-prairie-uplink-rabbit-running-right.gif
  ravenbyte-144-prairie-uplink-rabbit-running-left.gif
  ravenbyte-144-prairie-uplink-rabbit-waving.gif
  ravenbyte-144-prairie-uplink-rabbit-jumping.gif
  ravenbyte-144-prairie-uplink-rabbit-failed.gif
  ravenbyte-144-prairie-uplink-rabbit-waiting.gif
  ravenbyte-144-prairie-uplink-rabbit-running.gif
  ravenbyte-144-prairie-uplink-rabbit-review.gif
  ravenbyte-144-prairie-uplink-rabbit-contact-sheet.png
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
