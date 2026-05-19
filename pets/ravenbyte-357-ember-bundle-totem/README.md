# Ember Bundle Totem

<p align="center">
  <img src="previews/ravenbyte-357-ember-bundle-totem-showcase.gif" width="360" alt="Ember Bundle Totem stitched multi-motion showcase">
</p>

**A totem-class Ravenbyte familiar that keeps bundle work moving during long coding runs.**

Ember Bundle Totem is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around tall shrine totem bot with stacked status bars, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Ember Bundle Totem brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-357-ember-bundle-totem-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-357-ember-bundle-totem-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-357-ember-bundle-totem-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-357-ember-bundle-totem-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-357-ember-bundle-totem-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-357-ember-bundle-totem-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-357-ember-bundle-totem-waiting.gif) |
| Running | ![Running](previews/ravenbyte-357-ember-bundle-totem-running.gif) |
| Review | ![Review](previews/ravenbyte-357-ember-bundle-totem-review.gif) |

Full contact sheet:

![Ember Bundle Totem contact sheet](previews/ravenbyte-357-ember-bundle-totem-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-357-ember-bundle-totem
```

Or from anywhere with Git:

```bash
PET=ravenbyte-357-ember-bundle-totem; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-357-ember-bundle-totem/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-357-ember-bundle-totem-showcase.gif
  ravenbyte-357-ember-bundle-totem-idle.gif
  ravenbyte-357-ember-bundle-totem-running-right.gif
  ravenbyte-357-ember-bundle-totem-running-left.gif
  ravenbyte-357-ember-bundle-totem-waving.gif
  ravenbyte-357-ember-bundle-totem-jumping.gif
  ravenbyte-357-ember-bundle-totem-failed.gif
  ravenbyte-357-ember-bundle-totem-waiting.gif
  ravenbyte-357-ember-bundle-totem-running.gif
  ravenbyte-357-ember-bundle-totem-review.gif
  ravenbyte-357-ember-bundle-totem-contact-sheet.png
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
