# Brass Yield Train

<p align="center">
  <img src="previews/ravenbyte-251-brass-yield-train-showcase.gif" width="360" alt="Brass Yield Train stitched multi-motion showcase">
</p>

**A train-class Ravenbyte familiar that keeps yield work moving during long coding runs.**

Brass Yield Train is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around tiny train familiar hauling hotfix cargo, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Brass Yield Train brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-251-brass-yield-train-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-251-brass-yield-train-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-251-brass-yield-train-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-251-brass-yield-train-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-251-brass-yield-train-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-251-brass-yield-train-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-251-brass-yield-train-waiting.gif) |
| Running | ![Running](previews/ravenbyte-251-brass-yield-train-running.gif) |
| Review | ![Review](previews/ravenbyte-251-brass-yield-train-review.gif) |

Full contact sheet:

![Brass Yield Train contact sheet](previews/ravenbyte-251-brass-yield-train-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-251-brass-yield-train
```

Or from anywhere with Git:

```bash
PET=ravenbyte-251-brass-yield-train; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-251-brass-yield-train/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-251-brass-yield-train-showcase.gif
  ravenbyte-251-brass-yield-train-idle.gif
  ravenbyte-251-brass-yield-train-running-right.gif
  ravenbyte-251-brass-yield-train-running-left.gif
  ravenbyte-251-brass-yield-train-waving.gif
  ravenbyte-251-brass-yield-train-jumping.gif
  ravenbyte-251-brass-yield-train-failed.gif
  ravenbyte-251-brass-yield-train-waiting.gif
  ravenbyte-251-brass-yield-train-running.gif
  ravenbyte-251-brass-yield-train-review.gif
  ravenbyte-251-brass-yield-train-contact-sheet.png
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
