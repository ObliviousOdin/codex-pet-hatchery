# Ember Xray Totem

<p align="center">
  <img src="previews/ravenbyte-261-ember-xray-totem-showcase.gif" width="360" alt="Ember Xray Totem stitched multi-motion showcase">
</p>

**A totem-class Ravenbyte familiar that keeps xray work moving during long coding runs.**

Ember Xray Totem is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around tall shrine totem bot with stacked status bars, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Ember Xray Totem brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-261-ember-xray-totem-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-261-ember-xray-totem-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-261-ember-xray-totem-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-261-ember-xray-totem-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-261-ember-xray-totem-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-261-ember-xray-totem-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-261-ember-xray-totem-waiting.gif) |
| Running | ![Running](previews/ravenbyte-261-ember-xray-totem-running.gif) |
| Review | ![Review](previews/ravenbyte-261-ember-xray-totem-review.gif) |

Full contact sheet:

![Ember Xray Totem contact sheet](previews/ravenbyte-261-ember-xray-totem-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-261-ember-xray-totem
```

Or from anywhere with Git:

```bash
PET=ravenbyte-261-ember-xray-totem; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-261-ember-xray-totem/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-261-ember-xray-totem-showcase.gif
  ravenbyte-261-ember-xray-totem-idle.gif
  ravenbyte-261-ember-xray-totem-running-right.gif
  ravenbyte-261-ember-xray-totem-running-left.gif
  ravenbyte-261-ember-xray-totem-waving.gif
  ravenbyte-261-ember-xray-totem-jumping.gif
  ravenbyte-261-ember-xray-totem-failed.gif
  ravenbyte-261-ember-xray-totem-waiting.gif
  ravenbyte-261-ember-xray-totem-running.gif
  ravenbyte-261-ember-xray-totem-review.gif
  ravenbyte-261-ember-xray-totem-contact-sheet.png
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
