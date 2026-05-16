# Keystone Harvester Train

<p align="center">
  <img src="previews/ravenbyte-203-keystone-harvester-train-showcase.gif" width="360" alt="Keystone Harvester Train stitched multi-motion showcase">
</p>

**A train-class Ravenbyte familiar that keeps harvester work moving during long coding runs.**

Keystone Harvester Train is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around tiny train familiar hauling hotfix cargo, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Keystone Harvester Train brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-203-keystone-harvester-train-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-203-keystone-harvester-train-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-203-keystone-harvester-train-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-203-keystone-harvester-train-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-203-keystone-harvester-train-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-203-keystone-harvester-train-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-203-keystone-harvester-train-waiting.gif) |
| Running | ![Running](previews/ravenbyte-203-keystone-harvester-train-running.gif) |
| Review | ![Review](previews/ravenbyte-203-keystone-harvester-train-review.gif) |

Full contact sheet:

![Keystone Harvester Train contact sheet](previews/ravenbyte-203-keystone-harvester-train-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-203-keystone-harvester-train
```

Or from anywhere with Git:

```bash
PET=ravenbyte-203-keystone-harvester-train; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-203-keystone-harvester-train/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-203-keystone-harvester-train-showcase.gif
  ravenbyte-203-keystone-harvester-train-idle.gif
  ravenbyte-203-keystone-harvester-train-running-right.gif
  ravenbyte-203-keystone-harvester-train-running-left.gif
  ravenbyte-203-keystone-harvester-train-waving.gif
  ravenbyte-203-keystone-harvester-train-jumping.gif
  ravenbyte-203-keystone-harvester-train-failed.gif
  ravenbyte-203-keystone-harvester-train-waiting.gif
  ravenbyte-203-keystone-harvester-train-running.gif
  ravenbyte-203-keystone-harvester-train-review.gif
  ravenbyte-203-keystone-harvester-train-contact-sheet.png
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
