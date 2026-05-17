# Brass Xray Train

<p align="center">
  <img src="previews/ravenbyte-219-brass-xray-train-showcase.gif" width="360" alt="Brass Xray Train stitched multi-motion showcase">
</p>

**A train-class Ravenbyte familiar that keeps xray work moving during long coding runs.**

Brass Xray Train is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around tiny train familiar hauling hotfix cargo, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Brass Xray Train brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-219-brass-xray-train-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-219-brass-xray-train-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-219-brass-xray-train-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-219-brass-xray-train-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-219-brass-xray-train-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-219-brass-xray-train-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-219-brass-xray-train-waiting.gif) |
| Running | ![Running](previews/ravenbyte-219-brass-xray-train-running.gif) |
| Review | ![Review](previews/ravenbyte-219-brass-xray-train-review.gif) |

Full contact sheet:

![Brass Xray Train contact sheet](previews/ravenbyte-219-brass-xray-train-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-219-brass-xray-train
```

Or from anywhere with Git:

```bash
PET=ravenbyte-219-brass-xray-train; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-219-brass-xray-train/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-219-brass-xray-train-showcase.gif
  ravenbyte-219-brass-xray-train-idle.gif
  ravenbyte-219-brass-xray-train-running-right.gif
  ravenbyte-219-brass-xray-train-running-left.gif
  ravenbyte-219-brass-xray-train-waving.gif
  ravenbyte-219-brass-xray-train-jumping.gif
  ravenbyte-219-brass-xray-train-failed.gif
  ravenbyte-219-brass-xray-train-waiting.gif
  ravenbyte-219-brass-xray-train-running.gif
  ravenbyte-219-brass-xray-train-review.gif
  ravenbyte-219-brass-xray-train-contact-sheet.png
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
