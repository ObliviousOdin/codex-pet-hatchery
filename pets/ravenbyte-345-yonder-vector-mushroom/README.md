# Yonder Vector Mushroom

<p align="center">
  <img src="previews/ravenbyte-345-yonder-vector-mushroom-showcase.gif" width="360" alt="Yonder Vector Mushroom stitched multi-motion showcase">
</p>

**A mushroom-class Ravenbyte familiar that keeps vector work moving during long coding runs.**

Yonder Vector Mushroom is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around mushroom relay bot with soft cap and signal motes, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Yonder Vector Mushroom brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-345-yonder-vector-mushroom-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-345-yonder-vector-mushroom-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-345-yonder-vector-mushroom-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-345-yonder-vector-mushroom-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-345-yonder-vector-mushroom-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-345-yonder-vector-mushroom-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-345-yonder-vector-mushroom-waiting.gif) |
| Running | ![Running](previews/ravenbyte-345-yonder-vector-mushroom-running.gif) |
| Review | ![Review](previews/ravenbyte-345-yonder-vector-mushroom-review.gif) |

Full contact sheet:

![Yonder Vector Mushroom contact sheet](previews/ravenbyte-345-yonder-vector-mushroom-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-345-yonder-vector-mushroom
```

Or from anywhere with Git:

```bash
PET=ravenbyte-345-yonder-vector-mushroom; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-345-yonder-vector-mushroom/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-345-yonder-vector-mushroom-showcase.gif
  ravenbyte-345-yonder-vector-mushroom-idle.gif
  ravenbyte-345-yonder-vector-mushroom-running-right.gif
  ravenbyte-345-yonder-vector-mushroom-running-left.gif
  ravenbyte-345-yonder-vector-mushroom-waving.gif
  ravenbyte-345-yonder-vector-mushroom-jumping.gif
  ravenbyte-345-yonder-vector-mushroom-failed.gif
  ravenbyte-345-yonder-vector-mushroom-waiting.gif
  ravenbyte-345-yonder-vector-mushroom-running.gif
  ravenbyte-345-yonder-vector-mushroom-review.gif
  ravenbyte-345-yonder-vector-mushroom-contact-sheet.png
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
