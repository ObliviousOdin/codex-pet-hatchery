# Yonder Nexus Mushroom

<p align="center">
  <img src="previews/ravenbyte-089-yonder-nexus-mushroom-showcase.gif" width="360" alt="Yonder Nexus Mushroom stitched multi-motion showcase">
</p>

**A mushroom-class Ravenbyte familiar that keeps nexus work moving during long coding runs.**

Yonder Nexus Mushroom is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around mushroom relay bot with soft cap and signal motes, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Yonder Nexus Mushroom brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-089-yonder-nexus-mushroom-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-089-yonder-nexus-mushroom-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-089-yonder-nexus-mushroom-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-089-yonder-nexus-mushroom-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-089-yonder-nexus-mushroom-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-089-yonder-nexus-mushroom-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-089-yonder-nexus-mushroom-waiting.gif) |
| Running | ![Running](previews/ravenbyte-089-yonder-nexus-mushroom-running.gif) |
| Review | ![Review](previews/ravenbyte-089-yonder-nexus-mushroom-review.gif) |

Full contact sheet:

![Yonder Nexus Mushroom contact sheet](previews/ravenbyte-089-yonder-nexus-mushroom-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-089-yonder-nexus-mushroom
```

Or from anywhere with Git:

```bash
PET=ravenbyte-089-yonder-nexus-mushroom; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-089-yonder-nexus-mushroom/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-089-yonder-nexus-mushroom-showcase.gif
  ravenbyte-089-yonder-nexus-mushroom-idle.gif
  ravenbyte-089-yonder-nexus-mushroom-running-right.gif
  ravenbyte-089-yonder-nexus-mushroom-running-left.gif
  ravenbyte-089-yonder-nexus-mushroom-waving.gif
  ravenbyte-089-yonder-nexus-mushroom-jumping.gif
  ravenbyte-089-yonder-nexus-mushroom-failed.gif
  ravenbyte-089-yonder-nexus-mushroom-waiting.gif
  ravenbyte-089-yonder-nexus-mushroom-running.gif
  ravenbyte-089-yonder-nexus-mushroom-review.gif
  ravenbyte-089-yonder-nexus-mushroom-contact-sheet.png
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
