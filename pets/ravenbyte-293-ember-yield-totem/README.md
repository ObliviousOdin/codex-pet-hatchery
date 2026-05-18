# Ember Yield Totem

<p align="center">
  <img src="previews/ravenbyte-293-ember-yield-totem-showcase.gif" width="360" alt="Ember Yield Totem stitched multi-motion showcase">
</p>

**A totem-class Ravenbyte familiar that keeps yield work moving during long coding runs.**

Ember Yield Totem is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around tall shrine totem bot with stacked status bars, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Ember Yield Totem brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-293-ember-yield-totem-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-293-ember-yield-totem-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-293-ember-yield-totem-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-293-ember-yield-totem-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-293-ember-yield-totem-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-293-ember-yield-totem-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-293-ember-yield-totem-waiting.gif) |
| Running | ![Running](previews/ravenbyte-293-ember-yield-totem-running.gif) |
| Review | ![Review](previews/ravenbyte-293-ember-yield-totem-review.gif) |

Full contact sheet:

![Ember Yield Totem contact sheet](previews/ravenbyte-293-ember-yield-totem-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-293-ember-yield-totem
```

Or from anywhere with Git:

```bash
PET=ravenbyte-293-ember-yield-totem; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-293-ember-yield-totem/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-293-ember-yield-totem-showcase.gif
  ravenbyte-293-ember-yield-totem-idle.gif
  ravenbyte-293-ember-yield-totem-running-right.gif
  ravenbyte-293-ember-yield-totem-running-left.gif
  ravenbyte-293-ember-yield-totem-waving.gif
  ravenbyte-293-ember-yield-totem-jumping.gif
  ravenbyte-293-ember-yield-totem-failed.gif
  ravenbyte-293-ember-yield-totem-waiting.gif
  ravenbyte-293-ember-yield-totem-running.gif
  ravenbyte-293-ember-yield-totem-review.gif
  ravenbyte-293-ember-yield-totem-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from tall shrine totem bot with stacked status bars, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
