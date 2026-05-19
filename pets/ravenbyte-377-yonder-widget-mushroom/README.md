# Yonder Widget Mushroom

<p align="center">
  <img src="previews/ravenbyte-377-yonder-widget-mushroom-showcase.gif" width="360" alt="Yonder Widget Mushroom stitched multi-motion showcase">
</p>

**A mushroom-class Ravenbyte familiar that keeps widget work moving during long coding runs.**

Yonder Widget Mushroom is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around mushroom relay bot with soft cap and signal motes, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Yonder Widget Mushroom brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-377-yonder-widget-mushroom-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-377-yonder-widget-mushroom-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-377-yonder-widget-mushroom-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-377-yonder-widget-mushroom-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-377-yonder-widget-mushroom-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-377-yonder-widget-mushroom-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-377-yonder-widget-mushroom-waiting.gif) |
| Running | ![Running](previews/ravenbyte-377-yonder-widget-mushroom-running.gif) |
| Review | ![Review](previews/ravenbyte-377-yonder-widget-mushroom-review.gif) |

Full contact sheet:

![Yonder Widget Mushroom contact sheet](previews/ravenbyte-377-yonder-widget-mushroom-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-377-yonder-widget-mushroom
```

Or from anywhere with Git:

```bash
PET=ravenbyte-377-yonder-widget-mushroom; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-377-yonder-widget-mushroom/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-377-yonder-widget-mushroom-showcase.gif
  ravenbyte-377-yonder-widget-mushroom-idle.gif
  ravenbyte-377-yonder-widget-mushroom-running-right.gif
  ravenbyte-377-yonder-widget-mushroom-running-left.gif
  ravenbyte-377-yonder-widget-mushroom-waving.gif
  ravenbyte-377-yonder-widget-mushroom-jumping.gif
  ravenbyte-377-yonder-widget-mushroom-failed.gif
  ravenbyte-377-yonder-widget-mushroom-waiting.gif
  ravenbyte-377-yonder-widget-mushroom-running.gif
  ravenbyte-377-yonder-widget-mushroom-review.gif
  ravenbyte-377-yonder-widget-mushroom-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from mushroom relay bot with soft cap and signal motes, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
