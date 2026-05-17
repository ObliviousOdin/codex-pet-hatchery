# Ion Cache Mushroom

<p align="center">
  <img src="previews/ravenbyte-233-ion-cache-mushroom-showcase.gif" width="360" alt="Ion Cache Mushroom stitched multi-motion showcase">
</p>

**A mushroom-class Ravenbyte familiar that keeps cache work moving during long coding runs.**

Ion Cache Mushroom is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around mushroom relay bot with soft cap and signal motes, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Ion Cache Mushroom brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-233-ion-cache-mushroom-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-233-ion-cache-mushroom-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-233-ion-cache-mushroom-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-233-ion-cache-mushroom-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-233-ion-cache-mushroom-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-233-ion-cache-mushroom-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-233-ion-cache-mushroom-waiting.gif) |
| Running | ![Running](previews/ravenbyte-233-ion-cache-mushroom-running.gif) |
| Review | ![Review](previews/ravenbyte-233-ion-cache-mushroom-review.gif) |

Full contact sheet:

![Ion Cache Mushroom contact sheet](previews/ravenbyte-233-ion-cache-mushroom-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-233-ion-cache-mushroom
```

Or from anywhere with Git:

```bash
PET=ravenbyte-233-ion-cache-mushroom; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-233-ion-cache-mushroom/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-233-ion-cache-mushroom-showcase.gif
  ravenbyte-233-ion-cache-mushroom-idle.gif
  ravenbyte-233-ion-cache-mushroom-running-right.gif
  ravenbyte-233-ion-cache-mushroom-running-left.gif
  ravenbyte-233-ion-cache-mushroom-waving.gif
  ravenbyte-233-ion-cache-mushroom-jumping.gif
  ravenbyte-233-ion-cache-mushroom-failed.gif
  ravenbyte-233-ion-cache-mushroom-waiting.gif
  ravenbyte-233-ion-cache-mushroom-running.gif
  ravenbyte-233-ion-cache-mushroom-review.gif
  ravenbyte-233-ion-cache-mushroom-contact-sheet.png
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
