# Jade Flux Mask

<p align="center">
  <img src="previews/ravenbyte-010-jade-flux-mask-showcase.gif" width="360" alt="Jade Flux Mask stitched multi-motion showcase">
</p>

**A mask-class Ravenbyte familiar that keeps flux work moving during long coding runs.**

Jade Flux Mask is an original Codex-compatible coding familiar by **ObliviousOdin**. It is built around split-mask imp familiar with two-tone review face, with a readable `64×64` silhouette and no copied named character, logo, costume, or insignia.

## Personality

Jade Flux Mask brings a distinct motion language to Ravenbyte Familiars: distinct idle, run, wave, jump, failed, waiting, and review poses rendered from the generated sprite rows.

## Showcase

The top card stitches several real animation rows together — idle, run, jump, review, failed, and wave — so the familiar is not represented by a single idle loop.

## Animation preview

| State | Preview |
| --- | --- |
| Idle | ![Idle](previews/ravenbyte-010-jade-flux-mask-idle.gif) |
| Running Right | ![Running Right](previews/ravenbyte-010-jade-flux-mask-running-right.gif) |
| Running Left | ![Running Left](previews/ravenbyte-010-jade-flux-mask-running-left.gif) |
| Waving | ![Waving](previews/ravenbyte-010-jade-flux-mask-waving.gif) |
| Jumping | ![Jumping](previews/ravenbyte-010-jade-flux-mask-jumping.gif) |
| Failed | ![Failed](previews/ravenbyte-010-jade-flux-mask-failed.gif) |
| Waiting | ![Waiting](previews/ravenbyte-010-jade-flux-mask-waiting.gif) |
| Running | ![Running](previews/ravenbyte-010-jade-flux-mask-running.gif) |
| Review | ![Review](previews/ravenbyte-010-jade-flux-mask-review.gif) |

Full contact sheet:

![Jade Flux Mask contact sheet](previews/ravenbyte-010-jade-flux-mask-contact-sheet.png)

## Install

From the repository root:

```bash
python3 scripts/install_pet.py ravenbyte-010-jade-flux-mask
```

Or from anywhere with Git:

```bash
PET=ravenbyte-010-jade-flux-mask; REPO=https://github.com/ObliviousOdin/ravenbyte-familiars.git; TMP=$(mktemp -d); git clone --depth 1 "$REPO" "$TMP" && python3 "$TMP/scripts/install_pet.py" "$PET" && echo "Installed to ${CODEX_HOME:-$HOME/.codex}/pets/$PET"
```

Import this sprite in Open Design:

```text
Settings → Pets → Import Codex sprite
```

Use this spritesheet after install:

```text
${CODEX_HOME:-$HOME/.codex}/pets/ravenbyte-010-jade-flux-mask/spritesheet.webp
```

## Package contents

```text
pet.json
spritesheet.webp
previews/
  ravenbyte-010-jade-flux-mask-showcase.gif
  ravenbyte-010-jade-flux-mask-idle.gif
  ravenbyte-010-jade-flux-mask-running-right.gif
  ravenbyte-010-jade-flux-mask-running-left.gif
  ravenbyte-010-jade-flux-mask-waving.gif
  ravenbyte-010-jade-flux-mask-jumping.gif
  ravenbyte-010-jade-flux-mask-failed.gif
  ravenbyte-010-jade-flux-mask-waiting.gif
  ravenbyte-010-jade-flux-mask-running.gif
  ravenbyte-010-jade-flux-mask-review.gif
  ravenbyte-010-jade-flux-mask-contact-sheet.png
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

The design is intentionally original. It uses broad visual language from split-mask imp familiar with two-tone review face, pixel companions, and coding robots, but does not copy any named character, logo, or exact costume design.
