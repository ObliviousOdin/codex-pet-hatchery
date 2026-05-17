# Keystone Junction Train

<p align="center">
  <img src="previews/ravenbyte-267-keystone-junction-train-showcase.gif" width="360" alt="Keystone Junction Train stitched multi-motion showcase">
</p>

**A train-class Ravenbyte familiar that keeps junction work moving during long coding runs.**

Keystone Junction Train is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around tiny train familiar hauling hotfix cargo, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Keystone Junction Train brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-267-keystone-junction-train-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-267-keystone-junction-train-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-267-keystone-junction-train-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-267-keystone-junction-train-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-267-keystone-junction-train-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-267-keystone-junction-train-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-267-keystone-junction-train-waiting.gif) |
| Running | ![Running](previews/ravenbyte-267-keystone-junction-train-running.gif) |
| Review | ![Review](previews/ravenbyte-267-keystone-junction-train-review.gif) |

Full contact sheet:

![Keystone Junction Train contact sheet](previews/ravenbyte-267-keystone-junction-train-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-267-keystone-junction-train
```

Or from anywhere with Git:

```bash
PET=ravenbyte-267-keystone-junction-train; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-267-keystone-junction-train/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-267-keystone-junction-train-showcase.gif
  ravenbyte-267-keystone-junction-train-idle.gif
  ravenbyte-267-keystone-junction-train-running-right.gif
  ravenbyte-267-keystone-junction-train-running-left.gif
  ravenbyte-267-keystone-junction-train-waving.gif
  ravenbyte-267-keystone-junction-train-jumping.gif
  ravenbyte-267-keystone-junction-train-failed.gif
  ravenbyte-267-keystone-junction-train-waiting.gif
  ravenbyte-267-keystone-junction-train-running.gif
  ravenbyte-267-keystone-junction-train-review.gif
  ravenbyte-267-keystone-junction-train-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from tiny train familiar hauling hotfix cargo, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
