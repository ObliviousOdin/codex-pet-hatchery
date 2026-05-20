# Keystone Nexus Train

<p align="center">
  <img src="previews/ravenbyte-395-keystone-nexus-train-showcase.gif" width="360" alt="Keystone Nexus Train stitched multi-motion showcase">
</p>

**A train-class Ravenbyte familiar that keeps nexus work moving during long coding runs.**

Keystone Nexus Train is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around tiny train familiar hauling hotfix cargo, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Keystone Nexus Train brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-395-keystone-nexus-train-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-395-keystone-nexus-train-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-395-keystone-nexus-train-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-395-keystone-nexus-train-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-395-keystone-nexus-train-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-395-keystone-nexus-train-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-395-keystone-nexus-train-waiting.gif) |
| Running | ![Running](previews/ravenbyte-395-keystone-nexus-train-running.gif) |
| Review | ![Review](previews/ravenbyte-395-keystone-nexus-train-review.gif) |

Full contact sheet:

![Keystone Nexus Train contact sheet](previews/ravenbyte-395-keystone-nexus-train-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-395-keystone-nexus-train
```

Or from anywhere with Git:

```bash
PET=ravenbyte-395-keystone-nexus-train; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-395-keystone-nexus-train/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-395-keystone-nexus-train-showcase.gif
  ravenbyte-395-keystone-nexus-train-idle.gif
  ravenbyte-395-keystone-nexus-train-running-right.gif
  ravenbyte-395-keystone-nexus-train-running-left.gif
  ravenbyte-395-keystone-nexus-train-waving.gif
  ravenbyte-395-keystone-nexus-train-jumping.gif
  ravenbyte-395-keystone-nexus-train-failed.gif
  ravenbyte-395-keystone-nexus-train-waiting.gif
  ravenbyte-395-keystone-nexus-train-running.gif
  ravenbyte-395-keystone-nexus-train-review.gif
  ravenbyte-395-keystone-nexus-train-contact-sheet.png
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
